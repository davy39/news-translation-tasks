---
title: Comment créer une application météo avec R Shiny
subtitle: ''
author: Elabonga Atuo
co_authors: []
series: null
date: '2024-12-09T15:30:42.626Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-weather-app-with-r-shiny
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733174501446/a177379f-3c32-424a-9fbe-6608310f2ea6.png
tags:
- name: rshiny
  slug: rshiny
- name: Semantic UI
  slug: semantic-ui
- name: R Language
  slug: r
seo_title: Comment créer une application météo avec R Shiny
seo_desc: 'In this tutorial, you’ll learn how to build a weather app in R. Really
  – a weather app, in R? Wait, hear me out.

  When you think of R, you probably imagine someone wearing chunky thick prescription
  glasses and devouring a book. You know, a statisticia...'
---

Dans ce tutoriel, vous apprendrez à créer une application météo en R. Vraiment – une application météo, en R ? Attendez, laissez-moi vous expliquer.

Quand vous pensez à R, vous imaginez probablement quelqu'un portant des lunettes épaisses et dévorant un livre. Vous savez, un statisticien traitant des modèles complexes, une quantité folle d'équations mathématiques et des quantités copieuses de données.

Mais R est bien plus qu'un simple outil pour les statistiques. Il excelle lorsque vous devez transformer des données brutes en informations exploitables et présenter ces informations de manière claire et engageante.

Avec des frameworks comme Shiny, R va encore plus loin, vous permettant de créer des applications web entièrement interactives sans avoir à vous soucier des frontends, des backends ou d'apprendre un tout nouveau langage de programmation.

Dans ce tutoriel, vous allez créer une simple application météo qui récupère des données depuis une API et affiche les résultats dans une application esthétique.

## Table des matières

1. [Aperçu du projet](#heading-aperçu-du-projet)

2. [Installation du projet](#heading-installation-du-projet)

3. [Clés API : Stockage et Récupération](#heading-clés-api-stockage-et-récupération)

4. [Comment faire votre premier appel API](#heading-comment-faire-votre-premier-appel-api)

5. [Comment construire l'application Shiny](#heading-comment-construire-lapplication-shiny)

6. [Conclusion](#heading-conclusion)

## Aperçu du projet

Voici ce que nous allons construire :

![Démonstration de l'application météo R Shiny](https://cdn.hashnode.com/res/hashnode/image/upload/v1733341336823/dd605385-5531-43c5-924d-dde24b38846b.gif align="center")

Pour que l'application météo fonctionne, vous devrez faire deux appels API distincts. Nous utiliserons l'API One Call 3.0 pour mettre à jour les données météo et l'API OpenWeather pour le géocodage. Vous pouvez obtenir votre clé API [ici](https://openweathermap.org/api). Gardez simplement à l'esprit que si c'est la première fois que vous vous inscrivez pour une clé API, l'activation peut prendre jusqu'à 24 heures.

L'application météo prendra l'emplacement/la ville depuis l'entrée de l'utilisateur. L'entrée sera ensuite géocodée en faisant l'appel à l'API OpenWeather. Ensuite, à partir de sa réponse, les coordonnées (latitude et longitude) seront extraites. Les coordonnées seront utilisées comme arguments de requête pour l'appel à l'API One Call afin d'obtenir les données météo au format JSON.

### Prérequis :

Pour suivre ce tutoriel, vous aurez besoin de :

* Connaissances en programmation R

* Connaissances en HTML et un peu de JavaScript

* R Studio installé

![Flux de l'API de mise à jour météo](https://cdn.hashnode.com/res/hashnode/image/upload/v1733172415724/c4f884f6-b583-4f13-b0f8-eb564ab6531f.png align="center")

## Installation du projet

Créez un dossier dans le répertoire de votre choix. Définissez et confirmez le dossier du projet comme répertoire de travail en utilisant la commande suivante dans la console R :

```r
setwd("chemin/vers/votre/dossier/projet")
getwd()
```

Créez un projet dans le chemin défini en utilisant la commande suivante :

```r
# créer un projet R
usethis::create_project(path = ".", open = FALSE)
```

Vous devriez avoir une structure de dossier qui ressemble à ceci.

![structure du dossier du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1733166096334/93e004da-4449-4cb4-8ddd-d3082e5687d8.png align="center")

Créez un fichier R dans le répertoire racine et enregistrez-le sous `app.R`. Tout votre code R sera contenu ici.

Installez et chargez les bibliothèques suivantes avec lesquelles vous allez travailler :

```r
library(shiny)
library(bslib)
library(shinyjs)
library(httr2)
library(lubridate)
library(shiny.semantic)
```

## Clés API : Stockage et Récupération

Stocker vos identifiants dans un emplacement séparé de vos scripts et de l'environnement global est une bonne pratique. Cela garantit la sécurité, la scalabilité et la flexibilité, surtout lorsque vous travaillez dans des environnements partagés ou de production. Le fichier `.Renviron` sert au mieux cet objectif.

Ouvrez et éditez votre fichier `.Renviron` de la manière suivante :

```r
# ouvrir et éditer .Renviron
usethis::edit_r_environ(scope=c("project")
```

L'argument scope défini sur `project` configure le `.Renviron` spécifiquement pour votre projet. Dans le fichier nouvellement ouvert, ajoutez votre clé API comme suit :

```r
OPENWEATHERAPIKEY="votrecléapi"
```

## Comment faire votre premier appel API

Vous allez utiliser la bibliothèque httr2 (construite sur la base de httr) pour obtenir des données depuis l'API. Elle vous donne plus de contrôle sur la manière dont vous faites des requêtes sur le web.

### Rendre la clé API accessible dans le script

Tout d'abord, vous devrez accéder et stocker la clé API dans le script de manière sécurisée sans la coder en dur. Vous pouvez faire cela comme ceci :

```r
# accéder aux clés API dans le script
readenviron(".Renviron")
api_key = Sys.getenv("OPENWEATHERAPIKEY")
```

### Définir la fonction de géocodage

Vous allez créer une fonction qui prend un emplacement et une clé API comme entrées, envoie une requête à l'API de géocodage OpenWeather, et retourne les coordonnées de l'emplacement spécifié.

Commencez par créer une requête. L'opérateur pipe (`|>`) facilite l'enchaînement des requêtes HTTP étape par étape de manière claire et lisible. L'URL de géocodage prend deux paramètres : l'emplacement, désigné par `q`, et la clé API, désignée par `app_id`. La fonction `req_url_query()` ajoute ces paramètres à la requête.

Enchaînez la requête pour effectuer la requête et l'action de récupération, et enfin obtenez la réponse au format JSON en utilisant l'avant-dernière ligne.

```r
# URL de géocodage
geocoding_url <- "https://api.openweathermap.org/data/2.5/weather"
geocode <- function(location, api_key) {
  request(geocoding_url) |> 
    req_url_query(`q` = location, `appid` = api_key) |> 
    req_perform() |> 
    resp_body_json() |>
    coordinates()
}
```

![Un exemple de réponse à l'API de géocodage](https://cdn.hashnode.com/res/hashnode/image/upload/v1733342454801/feed01b2-a7a1-4c69-8297-2dcfdc8ec39f.png align="center")

### Définir la fonction d'extraction des coordonnées

La fonction `coordinates()` est une fonction auxiliaire qui extrait les valeurs de latitude et de longitude de la réponse JSON. Un rapide examen de la réponse JSON révèle la position des coordonnées. L'objet JSON est simplement une longue liste de listes et vous pouvez accéder aux éléments en les sous-ensemblant.

Un corps de données vide impliquerait que la ville/l'emplacement est indisponible, et vous obtiendriez le message *"No such city exists!"*. Si le JSON contient un élément, la longueur serait supérieure à 0 – c'est une liste après tout.

```r
coordinates <- function(body) {
  if(length(body) != 0) { 
    lat <- body$coord$lat
    lng <- body$coord$lon
    town <- body$name
    c(lat, lng, town)
  } else {
    "No such city exists!"
  }
}
```

### Définir la fonction de mise à jour météo

Vous allez créer une fonction qui envoie une requête à l'API OpenWeather avec des paramètres de requête spécifiés, gère les erreurs en utilisant une fonction prédéfinie, et retourne la réponse JSON analysée contenant les données météo.

Comme implémenté dans la fonction de géocodage, commencez par créer une requête et ajoutez les paramètres de requête nécessaires en utilisant la fonction `req_url_query()`. La fonction `openweather_json()` accepte deux arguments principaux :

* `api_key` : Il s'agit d'un argument requis utilisé pour l'authentification avec l'API OpenWeather, apparié par position.

* `...` : Cela représente des arguments de mots-clés optionnels que vous pouvez utiliser pour personnaliser la requête. Vous pouvez passer autant de paramètres supplémentaires que nécessaire, à condition qu'ils soient spécifiés comme arguments nommés.

```r
openweather_json <- function(api_key, ...) { 
  request(current_weather_url) |> 
    req_url_query(..., `appid` = api_key, `units` = "metric") |> 
    req_error(body = openweather_error_body) |>
    req_perform() |> 
    resp_body_json()
}
```

### Gestion des erreurs : Extraction et gestion des codes de statut

Vous allez créer une fonction de gestion des erreurs qui extrait les codes de statut non-200 d'une réponse et définit comment les gérer. La structure de cette fonction dépend de la manière dont l'API signale les erreurs et de l'endroit où les informations pertinentes sont stockées.

#### Définir le corps de l'erreur de mise à jour météo

Le `req_error()` dans `openweather_json()` introduit un nouveau concept : la gestion des erreurs. Les requêtes API peuvent lever des exceptions, et obtenir les codes de statut vous aide à savoir quel message afficher à l'utilisateur et comment le résoudre.

Créez un corps d'erreur qui est une fonction qui capture le code d'erreur si le code de statut n'est pas 200 (ce qui signifie que tout est OK).

La fonction prend une réponse et extrait la réponse de statut stockée dans la réponse JSON au sous-ensemble `$message`. Le soulignement `(_)` est un espace réservé pour l'objet JSON.

```r
openweather_error_body <- function(resp) {
  resp |> resp_body_json() |> _$message 
}
```

#### Définir le corps de l'erreur de géocodage

Cette fonction de corps d'erreur s'avérera utile dans l'application Shiny. Voici un guide simple.

La fonction `req_error()` vous permet de personnaliser la manière dont les erreurs de réponse sont gérées. Son argument `is_error` détermine si une réponse donnée doit être considérée comme une erreur. En définissant `is_error` sur `\(resp) FALSE` (une fonction anonyme qui retourne toujours FALSE), toutes les réponses, quel que soit le code de statut, sont traitées comme réussies. Cela empêche l'application de se fermer en raison de codes de statut non-200.

Avec cette configuration, vous pouvez extraire le code de statut du corps de la réponse et le transmettre à la fonction `resp_status()` pour récupérer le code exact.

```r
openstreetmap_error_body <- function(location, api_key) {
  resp <- request(geocoding_url) |> 
    req_url_query(`q` = location, `appid` = api_key) |> 
    req_error(is_error = \(resp) FALSE) |>
    req_perform() |>  resp_status()
  resp
}
```

## Comment construire l'application Shiny

Maintenant que vous avez compris comment obtenir des données depuis l'API, il est temps de rendre les résultats dans un format interprétable et interactif. Pour cela, vous allez utiliser Shiny. Shiny est un framework qui vous permet de créer des applications web interactives.

Une application Shiny est composée de deux composants :

* L'UI : ce avec quoi l'utilisateur interagit. Elle définit la disposition et l'apparence de l'application.

* Le serveur : contient la logique et le comportement de l'application.

### Construire l'UI Shiny

L'UI Shiny fournit une collection d'éléments qui permettent aux utilisateurs de saisir des données, de faire des sélections et de déclencher des événements de manière transparente.

Vous allez inclure un élément `textInput` qui prend l'emplacement et les données météo seront récupérées et rendues lors de la soumission. Le bouton `input_task_button` empêche l'utilisateur de cliquer lorsqu'un appel API est en cours. Les autres éléments sont des éléments de sortie où les données météo seront affichées et un bouton de changement de mode.

#### Styliser l'application Shiny

Vous pouvez utiliser `shiny.semantic`, une bibliothèque construite sur Fomantic-UI, pour styliser votre tableau de bord Shiny. Fomantic-UI est un framework frontal qui fournit une riche collection de composants HTML pré-stylisés comme des boutons, des modales, des entrées de formulaire, et plus encore. Il simplifie la conception de l'UI en permettant aux développeurs de créer des interfaces visuellement attrayantes et réactives sans avoir besoin de connaissances approfondies en CSS ou HTML personnalisé.

Le style Fomantic-UI est appliqué en enveloppant les éléments dans leurs classes correspondantes, qui définissent leur comportement et leur apparence.

Une grille dans Fomantic-UI est un système de mise en page flexible utilisé pour organiser le contenu. Elle agit comme une toile qui divise la mise en page en lignes (alignées horizontalement) et en colonnes (alignées verticalement). Une grille racine peut contenir jusqu'à 16 colonnes, ce qui la rend idéale pour créer des designs structurés et réactifs.

Pour spécifier la largeur d'une colonne, vous ajoutez des classes comme wide et la taille (un nombre de 1 à 16) pour représenter son étendue. La largeur totale de toutes les colonnes dans une ligne doit être égale à 16.

Un segment regroupe le contenu lié, tandis qu'une carte affiche des éléments détaillés et riches en contenu, comme le profil d'un utilisateur sur les réseaux sociaux. Les diviseurs sont des éléments visuels utilisés pour séparer les sections ou le contenu dans une mise en page.

Pour l'application météo, créez d'abord une div de classe `grid` dans laquelle vous imbriquerez les divers éléments.

![démonstration de la mise en page de la page sémantique](https://cdn.hashnode.com/res/hashnode/image/upload/v1733137762676/12d5695c-2ed7-4606-8267-44243c2bee57.png align="center")

##### **Section de la barre de recherche**

Divisez la grille en seize colonnes et créez un segment qui regroupe les éléments dans la section de la barre de recherche. Ajoutez un bouton de bascule de thème, une entrée de localisation qui prend l'entrée de l'utilisateur, un bouton de recherche pour soumettre la localisation à l'API, et un bouton de notification, en définissant leur largeur par la taille de la colonne.

```r
div(class = "sixteen wide column",
          div(class = "ui segment",
              div(class = "ui grid",
                  div(class = "two wide column",
                      button(
                        class = "ui button icon basic",
                        input_id = "darkmode",
                        label = NULL,
                        icon = icon("moon icon")
                      )
                  ),
                  div(class = "ten wide column",
                      textInput(
                        "location",
                        label = NULL,
                        placeholder = "Recherchez votre ville préférée"
                      )
                  ),
                  div(class = "two wide column",
                      tags$div(
                        class = "ui button",
                        id = "my-custom-button",
                        input_task_button("search", label = "Rechercher", icon = icon("search"))
                      )
                  ),
                  div(class = "two wide column",
                      actionButton("show_alert", label = icon("bell"), class = "bell-no-alert"),
                      textOutput("alert_message")
                  )
              )
          )
      )
```

##### **Section de localisation et de météo actuelle**

Divisez la grille en seize colonnes et imbriquez une autre grille dans les partitions qui hébergeront deux colonnes.

Dans la grille, définissez deux colonnes. La première colonne est pour les données de temps, de localisation et de date, et la deuxième colonne contiendra les données météo actuelles.

Ensuite, créez des éléments de carte pour contenir chaque paramètre météo, son unité de mesure et l'icône correspondante.

```r
div(class = "sixteen wide column",
          div(class = "ui equal-height-grid grid",
              div(class = "left floated center aligned four wide column",
                  div(class = "ui raised equal-height-two-segment segment",
                      style = "flex: 1;",
                      div(class = "column center aligned",
                          div(class = "ui hidden section divider"),
                          span(class = "ui large text", textOutput("city")),
                          div(class = "ui hidden section divider"),
                          span(class = "ui big text", textOutput("currentTime")),
                          div(class = "ui hidden section divider"),
                          span(class = "ui large text", textOutput("currentDate")),
                          div(class = "ui hidden section divider")
                      )
                  )
              ),
              div(class = "right floated center aligned twelve wide column",
                  div(class = "ui raised segment",
                      div(class = "ui horizontal equal width segments",
                          div(class = "ui equal-height-two-segment segment",
                              style = "flex: 3;",
                              div(class = "column",
                                  span(class = "ui big text centered", textOutput("currentTemp")),
                                  textOutput("feelsLike"),
                                  card(
                                    class = "ui mini",
                                    div(class = "content", icon(class = "large sun"),
                                        div(class = "sub header", "Lever du soleil"),
                                        div(class = "description", textOutput("sunriseTime"))
                                    )
                                  ),
                                  card(
                                    class = "ui mini",
                                    div(class = "content", icon(class = "large moon"),
                                        div(class = "sub header", "Coucher du soleil"),
                                        div(class = "description", textOutput("sunsetTime"))
                                    )
                                  )
                              )
                          ),
                          div(class = "ui segment",
                              style = "flex: 3;",
                              div(
                                class = "column center aligned",
                                div(class = "ui hidden divider"),
                                htmlOutput("currentWeatherIcon"),
                                span(class = "ui large text", textOutput("currentWeatherDescription"))
                              )
                          ),
                          div(class = "ui segment",
                              style = "flex: 3;",
                              div(class = "column",
                                  card(
                                    class = "ui tiny",
                                    div(class = "content", icon(class = "big tint"),
                                        div(class = "sub header", "Humidité"),
                                        div(class = "description", textOutput("currentHumidity"))
                                    )
                                  ),
                                  card(
                                    class = "ui tiny",
                                    div(class = "content", icon(class = "big tachometer alternate"),
                                        div(class = "sub header", "Pression"),
                                        div(class = "description", textOutput("currentPressure"))
                                    )
                                  )
                              )
                          ),
                          div(class = "ui segment",
                              style = "flex: 3;",
                              div(class = "column center aligned",
                                  card(
                                    class = "ui tiny",
                                    div(class = "content", icon(class = "big wind"),
                                        div(class = "sub header", "Vitesse du vent"),
                                        div(class = "description", textOutput("currentWindSpeed"))
                                    )
                                  ),
                                  card(
                                    class = "ui tiny",
                                    div(class = "content", icon(class = "big umbrella"),
                                        div(class = "sub header", "Indice UV"),
                                        div(class = "description", textOutput("currentUV"))
                                    )
                                  )
                              )
                          )
                      )
                  )
              )
          )
      )
```

**Section des prévisions**

Cette section contient les données prévues. Divisez la grille en seize colonnes et imbriquez une autre grille dans les partitions hébergeant deux colonnes.

Dans la grille, définissez deux colonnes. La première colonne contient les données de *Prévisions sur 5 jours*. Séparez les éléments contenant différentes valeurs en utilisant des lignes. La deuxième colonne contient les données de *Prévisions horaires*. Séparez les éléments contenant différentes valeurs en utilisant des colonnes.

```r
      # Section des prévisions
      div(class = "sixteen wide column",
          div(class = "ui grid equal-height-grid",
              div(class = "left floated center aligned six wide column",
                  div(class = "ui raised segment special-segment equal-height-segment",
                      h4("Prévisions sur 5 jours :"),
                      div(class = "ui three column special-column grid",
                          # Prévisions journalières
                          div(class = "row",
                              div(class = "five wide column", textOutput("dailyDtOne")),
                              div(class = "three wide column", textOutput("dailyTempOne")),
                              div(class = "three wide column", htmlOutput("dailyIconOne"))
                          ),
                          div(class = "row",
                              div(class = "five wide column", textOutput("dailyDtTwo")),
                              div(class = "three wide column", textOutput("dailyTempTwo")),
                              div(class = "three wide column", htmlOutput("dailyIconTwo"))
                          ),
                          div(class = "row",
                              div(class = "five wide column", textOutput("dailyDtThree")),
                              div(class = "three wide column", textOutput("dailyTempThree")),
                              div(class = "three wide column", htmlOutput("dailyIconThree"))
                          ),
                          div(class = "row",
                              div(class = "five wide column", textOutput("dailyDtFour")),
                              div(class = "three wide column", textOutput("dailyTempFour")),
                              div(class = "three wide column", htmlOutput("dailyIconFour"))
                          ),
                          div(class = "row",
                              div(class = "five wide column", textOutput("dailyDtFive")),
                              div(class = "three wide column", textOutput("dailyTempFive")),
                              div(class = "three wide column", htmlOutput("dailyIconFive"))
                          )
                      )
                  )
              ),
              div(class = "right floated center aligned ten wide column",
                  div(class = "ui raised segment special-segment equal-height-segment",
                      h4("Prévisions horaires :"),
                      div(
                        class = "ui grid",
                        style = "display: flex; flex-direction: row; align-items: center; justify-content: space-around; flex-wrap: wrap; height: 100%;",
                        # Prévisions horaires
                        div(class = "column",
                            textOutput("hourlyDtOne"),
                            htmlOutput("hourlyIconOne"),
                            textOutput("hourlyTempOne")
                        ),
                        div(class = "column",
                            textOutput("hourlyDtTwo"),
                            htmlOutput("hourlyIconTwo"),
                            textOutput("hourlyTempTwo")
                        ),
                        div(class = "column",
                            textOutput("hourlyDtThree"),
                            htmlOutput("hourlyIconThree"),
                            textOutput("hourlyTempThree")
                        ),
                        div(class = "column",
                            textOutput("hourlyDtFour"),
                            htmlOutput("hourlyIconFour"),
                            textOutput("hourlyTempFour")
                        ),
                        div(class = "column",
                            textOutput("hourlyDtFive"),
                            htmlOutput("hourlyIconFive"),
                            textOutput("hourlyTempFive")
                        )
                      )
                  )
              )
          )
      )
  )
```

### Construire le serveur Shiny

Chaque élément dans la section UI a un ID (identifiant unique) qui est utilisé pour manipuler les données/informations qui y seront affichées.

L'ensemble des fonctions `render*()` définit le type de visualisation tandis que les fonctions `output$*` sous-ensemblent les éléments. Ces deux fonctions sont utilisées pour lier le visuel à la logique. La plupart des éléments auront des données extraites de la liste JSON, à l'exception des icônes météo (pour lesquelles un lien externe comme source sera référencé).

#### Réactivité

La réactivité est ce qui rend les applications Shiny dynamiques—les sorties se mettent à jour automatiquement lorsque leurs dépendances changent.

Deux composants clés de la réactivité sont les réactifs et les observateurs. Un réactif calcule et retourne une valeur basée sur ses dépendances, tandis qu'un observateur surveille les valeurs réactives et exécute du code qui provoque des effets secondaires, comme la journalisation ou la mise à jour d'une base de données.

Pour contrôler la réactivité, vous pouvez utiliser `bindEvent()` pour retarder l'exécution jusqu'à ce qu'un événement spécifique se produise ou `observeEvent()` pour écouter une action de l'utilisateur et déclencher un bloc de code. Ensemble, ces outils offrent de la flexibilité pour gérer le comportement de l'application.

#### Le code du serveur

1. **Réactif** `location`

Le réactif location inclut un bloc conditionnel if-else qui définit quel message afficher en fonction du code de statut. La variable query contient la ville/l'emplacement qui sera géocodé pour obtenir les coordonnées. Le flux est transmis à `bindEvent()`. Cela garantit que l'appel à l'API de géocodage est terminé avant qu'un autre appel ne puisse être fait, ce qui réduit les requêtes inutiles.

```r
location <- reactive({
    query <- input$location
    if(openstreetmap_error_body(query, api_key) == "404"){
      validate("Aucune ville/lieu n'existe. Vérifiez votre orthographe !")
    }
    else if(openstreetmap_error_body(query, api_key) == "400"){
      validate("Mauvaise requête")
    }
    coords <- geocode(query, api_key)
  }) %>% bindEvent(input$search)
```

2. **Réactif** `weather_data`

Le réactif weather combine un appel à l'API de géocodage et un appel à l'API de mise à jour météo en utilisant les coordonnées obtenues et extraites de `location()` :

```r
  weather_data <- reactive({
    loc <- location()
    openweather_json(api_key, lat = loc[1], lon = loc[2])
  })
```

Pour accéder aux objets JSON retournés par l'appel à l'API, vous appelez le réactif comme s'il s'agissait d'une fonction. Les valeurs spécifiques à extraire peuvent ensuite être accessibles en sous-ensemblant la valeur JSON.

```r
# sous-ensemblage des données météo.
  output$city <- renderText({
    location()[3]
  })
  
  output$currentWeatherDescription <- renderText({
    weather_data()$current$weather[[1]]$description
  })
```

3. **Créer une fonction Parse Date**

Toutes les données de temps dans la réponse JSON, prévues ou actuelles, sont fournies au format UNIX. Pour rendre cette information conviviale, elle doit être convertie dans un format lisible par l'homme. Vous pouvez faire cela en créant une fonction qui prend les données de temps comme entrée et utilise les fonctions du package `lubridate` pour gérer la conversion.

Tout d'abord, convertissez l'élément timestamp en un objet datetime. Formatez l'élément de temps dans un système d'horloge 12 heures et un élément de date pour inclure le jour de la semaine, la date et le mois.

* `%I` : Affiche l'heure dans un format d'horloge 12 heures (01-12).

* `%M` : Affiche les minutes (00-59).

* `%p` : Ajoute l'indicateur AM/PM.

La fonction paste concatène les valeurs. La fonction retourne un vecteur contenant les valeurs de date et d'heure à extraire par sous-ensemblage.

```r
parse_date <- function(timestamp) {
  datetime <- as_datetime(timestamp) 
  date <- paste(weekdays(datetime), ",", day(datetime), months(datetime))
  time <- format(as.POSIXct(datetime), format = "%I:%M %p")
  c(date, time)
}
```

4. **Ajouter une modale pour afficher les messages d'erreur**

Le réactif `location` fournit un moyen de gérer les erreurs. Vous pouvez incorporer une modale pour améliorer l'expérience utilisateur en superposant la page et en désactivant son contenu jusqu'à ce que l'utilisateur complète une action spécifiée chaque fois qu'une erreur se produit.

Vous ajouterez du JavaScript pour contrôler quand et comment la modale s'affiche.

Ajoutez deux modales dans la section UI, chacune présentant une explication de l'erreur (en-tête) et un aperçu de l'action requise (contenu). La classe `action` inclut un bouton qui permet à l'utilisateur de fermer la modale.

```r
# modales - UI
  div(id = "notFound", class = "ui modal",
      div(class = "header", "Lieu non trouvé"),
      div(class = "content", "Aucune ville/lieu n'existe. Vérifiez votre orthographe !"),
      div(class = "actions",
          div(class = "ui button", id = "closeNotFound", "OK"))
  ),
  div(id = "badRequest", class = "ui modal",
      div(class = "header", "Requête invalide"),
      div(class = "content", "Mauvaise requête. Veuillez réessayer avec des détails valides."),
      div(class = "actions",
          div(class = "ui button", id = "closeBadRequest", "OK"))
  )
```

Ajustez légèrement le réactif location pour incorporer la modale. Le code commenté sera remplacé par les lignes JavaScript. La fonction `runjs` affiche la modale en fonction de l'erreur rencontrée. `req(FALSE)` termine le flux réactif.

```r
# afficher et masquer les modales - Serveur
location <- reactive({
    query <- input$location
    if(openstreetmap_error_body(query, api_key) == "404"){
      #validate("Aucune ville/lieu n'existe. Vérifiez votre orthographe !")
      runjs("$('#notFound').modal('show');")
      req(FALSE)
    }
    else if(openstreetmap_error_body(query, api_key) == "400"){
      #validate("Mauvaise requête")
      runjs("$('#badRequest').modal('show');")
      req(FALSE)
    }
    coords <- geocode(query, api_key)
  }) %>% bindEvent(input$search)

# écoute le clic sur le bouton des modales pour masquer la modale
observeEvent(input$closeNotFound, {
    runjs("$('#notFound').modal('hide');")
  })
  
observeEvent(input$closeBadRequest, {
    runjs("$('#badRequest').modal('hide');")
  })
  
```

## Conclusion

Dans ce tutoriel, vous avez construit une application météo utilisant Shiny qui récupère les données météo depuis une API et les affiche de manière interactive et visuellement attrayante.

Pour ce faire, vous avez utilisé les bibliothèques suivantes :

* `httr2` pour faire des requêtes API et gérer les réponses

* `shiny.semantic` pour styliser l'application

* `lubridate` pour travailler avec et formater les données de temps

* `shinyjs` pour intégrer des fonctionnalités JavaScript dans l'application

Cette combinaison d'outils vous a permis de créer une application météo fonctionnelle et conviviale.

Vous pouvez trouver le code complet du projet [ici](https://github.com/elabongaatuo/R-weather-app).

La Fin !