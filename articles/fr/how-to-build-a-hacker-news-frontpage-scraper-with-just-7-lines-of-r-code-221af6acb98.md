---
title: Comment créer un scraper pour la page d'accueil de Hacker News avec seulement
  7 lignes de code R
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-06T20:54:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-hacker-news-frontpage-scraper-with-just-7-lines-of-r-code-221af6acb98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P7CAV7kEQ4aBBzozOCYGsA.jpeg
tags:
- name: General Programming
  slug: programming
- name: R Programming
  slug: r-programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
- name: web scraping
  slug: web-scraping
seo_title: Comment créer un scraper pour la page d'accueil de Hacker News avec seulement
  7 lignes de code R
seo_desc: 'By AMR

  Web scraping used to be a difficult task requiring expertise in XML Tree parsing
  and HTTP Requests. But with new-age scraping libraries like beautifulsoup (for Python)
  and rvest (for R), web scraping has become a toy for any beginner to play w...'
---

Par AMR

Le web scraping était autrefois une tâche difficile nécessitant une expertise en analyse d'arborescences XML et en requêtes HTTP. Mais avec les nouvelles bibliothèques de scraping comme beautifulsoup (pour Python) et rvest (pour R), le web scraping est devenu un jeu d'enfant pour tout débutant.

Cet article vise à expliquer à quel point il est simple d'utiliser R, un langage de programmation très agréable, pour effectuer de l'analyse de données et de la visualisation de données. La tâche à accomplir est très simple. Construire un scraper web qui extrait le contenu de l'une des pages les plus populaires sur Internet (au moins parmi les codeurs) : [Hacker News Front Page](https://news.ycombinator.com/).

### Installation et chargement du package

Le package R que nous allons utiliser est `rvest`. `rvest` peut être installé depuis [CRAN](https://cran.r-project.org/web/packages/rvest/index.html) et chargé dans R comme suit :

```
library(rvest)
```

La fonction `read_html()` de `rvest` peut être utilisée pour extraire le contenu HTML de l'URL donnée en argument à la fonction read_html.

```
content <- read_html('https://news.ycombinator.com/')
```

Pour que `read_html()` fonctionne sans problème, assurez-vous de ne pas être derrière un pare-feu d'organisation. Si c'est le cas, configurez votre RStudio avec un proxy pour contourner le pare-feu, sinon vous pourriez rencontrer une `erreur de délai de connexion`.

Ci-dessous, une capture d'écran de la disposition de la page d'accueil de HN (avec les éléments clés mis en évidence) :

![Image](https://cdn-media-1.freecodecamp.org/images/4rSb9LXlF3ZcRyLEGeKrT2yX8vsQJkACkaXi)

Maintenant, avec le contenu HTML de la page d'accueil de Hacker News chargé dans l'objet R _content_, extrayons les données dont nous avons besoin — en commençant par le titre.

Il y a un aspect particulièrement important pour réussir toute tâche de web scraping. Il s'agit d'identifier les bons sélecteurs CSS, ou valeurs XPath, des éléments HTML dont les valeurs doivent être extraites. Le moyen le plus simple d'obtenir la bonne valeur d'élément est d'utiliser `l'outil d'inspection` dans les outils de développement de n'importe quel navigateur.

Voici une capture d'écran de la valeur du sélecteur CSS. Elle est mise en évidence à l'aide de l'outil d'inspection de Chrome lorsque l'on survole le titre des liens présents sur la page d'accueil de Hacker News.

![Image](https://cdn-media-1.freecodecamp.org/images/IEJOiDb3aUyj90KuhWzWyAO4eoQ3Z1jUcpNM)

```
title <- content %>% html_nodes('a.storylink') %>% html_text()title [1] "Magic Leap One"                                                                   [2] "Show HN: Terminal – native micro-GUIs for shell scripts and command line apps"    [3] "Tokio internals: Understanding Rust's async I/O framework"                        [4] "Funding Yourself as a Free Software Developer"                                    [5] "US Federal Ban on Making Lethal Viruses Is Lifted"                                [6] "Pass-Thru Income Deduction"                                                       [7] "Orson Welles' first attempt at movie-making"                                      [8] "D’s Newfangled Name Mangling"                                                     [9] "Apple Plans Combined iPhone, iPad, and Mac Apps to Create One User Experience"    [10] "LiteDB – A .NET NoSQL Document Store in a Single Data File"                      [11] "Taking a break from Adblock Plus development"                                    [12] "SpaceX’s Falcon Heavy rocket sets up at Cape Canaveral ahead of launch"          [13] "This is not a new year’s resolution"                                             [14] "Artists and writers whose works enter the public domain in 2018"                 [15] "Open Beta of Texpad 1.8, macOS LaTeX editor with integrated real-time typesetting"[16] "The triumph and near-tragedy of the first Moon landing"                          [17] "Retrotechnology – PC desktop screenshots from 1983-2005"                         [18] "Google Maps' Moat"                                                               [19] "Regex Parser in C Using Continuation Passing"                                    [20] "AT&T giving $1000 bonus to all its employees because of tax reform"              [21] "How a PR Agency Stole Our Kickstarter Money"                                     [22] "Google Hangouts now on Firefox without plugins via WebRTC"                       [23] "Ubuntu 17.10 corrupting BIOS of many Lenovo laptop models"                       [24] "I Know What You Download on BitTorrent"                                          [25] "Carrie Fisher’s Private Philosophy Coach"                                        [26] "Show HN: Library of API collections for Postman"                                 [27] "Uber is officially a cab firm, says European court"                              [28] "The end of the Iceweasel Age (2016)"                                             [29] "Google will turn on native ad-blocking in Chrome on February 15"                 [30] "Bitcoin Cash deals frozen as insider trading is probed"
```

Le package rvest prend en charge l'opérateur pipe %>%. Ainsi, l'objet R contenant le contenu de la page HTML (lu avec read_html) peut être pipé avec html_nodes() qui prend un sélecteur CSS ou XPath comme argument. Il peut ensuite extraire l'arborescence XML respective (ou la valeur du nœud HTML) dont la valeur texte pourrait être extraite avec la fonction html_text().

La beauté de rvest est qu'il abstrait toute l'opération d'analyse XML sous le capot des fonctions comme html_nodes() et html_text(). Ainsi, il nous est plus facile d'atteindre notre objectif de scraping avec un code minimal.

Comme avec le titre, la valeur du sélecteur CSS des autres éléments requis de la page web peut être identifiée avec l'outil d'inspection de Chrome. Ils peuvent également être passés en argument à la fonction html_nodes() et les valeurs respectives peuvent être extraites et stockées dans des objets R.

```
link_domain <- content %>% html_nodes('span.sitestr') %>% html_text()score <- content %>% html_nodes('span.score') %>% html_text()age <- content %>% html_nodes('span.age') %>% html_text()
```

Toutes les pièces essentielles d'information ont été extraites de la page. Maintenant, un data frame R peut être créé avec les éléments extraits pour mettre les données extraites dans un format structuré.

```
df <- data.frame(title = title, link_domain = link_domain, score = score, age = age)
```

Ci-dessous, une capture d'écran du data frame final dans le visualiseur RStudio :

![Image](https://cdn-media-1.freecodecamp.org/images/hEnsMstgI7-hwhOHGx9LrexwgAEoOb8q5bmK)

Ainsi, en seulement 7 lignes de code, nous avons réussi à créer un scraper pour la page d'accueil de Hacker News en R.

R est un langage merveilleux pour effectuer de l'analyse de données et de la visualisation de données. Le code utilisé ici est disponible [sur mon github](https://github.com/amrrs/HN_scraper_in_R).