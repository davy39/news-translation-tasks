---
title: Web Scraping avec RSelenium (Chrome Driver) et Rvest
subtitle: ''
author: Elabonga Atuo
co_authors: []
series: null
date: '2025-03-17T13:44:10.011Z'
originalURL: https://freecodecamp.org/news/web-scraping-with-rselenium-chrome-driver-and-rvest
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742219025681/47c07711-cfa5-482f-a72b-d127bc5b63bc.png
tags:
- name: Rselenium
  slug: rselenium
- name: RVest
  slug: rvest
- name: selenium
  slug: selenium
- name: R Programming
  slug: r-programming
- name: 'webscraping '
  slug: webscraping
- name: chromedriver
  slug: chromedriver
seo_title: Web Scraping avec RSelenium (Chrome Driver) et Rvest
seo_desc: 'Web scraping lets you automatically extract data from websites, so you
  can store it in a structured format for later use.

  In this article, you''ll explore how to use popular R libraries for web scraping
  to extract data from a website. The target websi...'
---

Le web scraping vous permet d'extraire automatiquement des données de sites web, afin de les stocker dans un format structuré pour une utilisation ultérieure.

Dans cet article, vous explorerez comment utiliser des bibliothèques R populaires pour le web scraping afin d'extraire des données d'un site web. Le site web cible affiche différents livres sur plusieurs pages, nécessitant une navigation entre elles. Vous apprendrez à utiliser RVest pour l'extraction de données et RSelenium pour automatiser les clics sur les boutons.

Il existe quelques règles de base lorsque vous récoltez des données sur Internet :

* **Inspecter le fichier robots.txt** : Vérifiez le fichier robots.txt d'un site web pour comprendre quelles données vous êtes autorisé à extraire. Vous pouvez trouver ce fichier en ajoutant « /robots.txt » à l'URL d'accueil du site web.

* **Lire les termes et conditions** : Avant de scraper, lisez les termes et conditions du site web pour comprendre les attentes légales concernant l'extraction de données.

* **Limiter les requêtes** : Évitez de surcharger le serveur avec des requêtes en implémentant une limitation de débit. La bibliothèque [polite](https://dmi3kno.github.io/polite/) dans R peut aider à gérer efficacement les taux de requêtes.

Commençons !

## Table des matières

* [Aperçu du projet](#heading-aperçu-du-projet)

* [Installation du projet](#heading-installation-du-projet)

* [Comment comprendre et inspecter une page web](#heading-comment-comprendre-et-inspecter-une-page-web)

* [Comment extraire des données avec RVest](#heading-comment-extraire-des-données-avec-rvest)

* [Comment imiter le comportement humain avec RSelenium](#heading-comment-imiter-le-comportement-humain-avec-rselenium)

* [Comment combiner RSelenium et RVest et sauvegarder en CSV](#heading-comment-combiner-rselenium-et-rvest-et-sauvegarder-en-csv)

* [Tout rassembler](#heading-tout-rassembler)

* [Conclusion](#heading-conclusion)

## Aperçu du projet

Voici ce que nous allons construire :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1739891904874/e10f91f5-f5ba-4a9d-82d7-bd297b409b1b.gif align="center")

Cette approche de web scraping vous permet de voir le navigateur en action alors qu'il navigue et extrait des données du site web. Contrairement à la navigation sans tête, où tout s'exécute en arrière-plan sans interface visible, cette méthode fournit une interface graphique, ce qui facilite la surveillance et le débogage du processus.

Pour pratiquer vos compétences en extraction de données, vous allez extraire des données d'un site web conçu spécifiquement pour cela : [Books To Scrape](https://books.toscrape.com/). Vous allez utiliser un driver pour contrôler un navigateur qui ouvrira ensuite votre site web cible. Il naviguera depuis la première page, en imitant le comportement humain (en cliquant sur le bouton suivant) tout en collectant des données sur les livres, jusqu'à la dernière page.

## Installation du projet

### **Prérequis :**

Pour suivre ce tutoriel, vous aurez besoin de :

* Connaissances en programmation R

* Connaissances en HTML

* R Studio installé

Notez que je construis ce tutoriel sur une machine Windows.

### Installation et configuration du Chrome Driver

Tout d'abord, vous voulez vérifier que Java est installé sur votre ordinateur en exécutant cette commande de terminal :

```bash
java -version
```

S'il n'est pas présent, téléchargez et installez Java [ici](https://www.java.com/en/download/).

Ensuite, installez le navigateur Chrome si vous ne l'avez pas déjà. Une fois installé, vérifiez la version de votre navigateur dans la section des paramètres.

Ensuite, vous pouvez télécharger le Driver du navigateur qui correspond à votre version de navigateur [ici](https://developer.chrome.com/docs/chromedriver/downloads/version-selection). Vérifiez où les autres drivers de navigateur sont stockés sur votre appareil en exécutant ceci dans le terminal de RStudio :

```r
# installer et charger les packages wdman et binman
install.packages("wdman")
library(wdman)

install.packages("binman")
library(binman)

# vérifier les drivers déjà installés
binman::list_versions(appname = "chromedriver")

# vérifier les emplacements des drivers de navigateur
wdman::selenium(retcommand = TRUE, check = FALSE)
```

Extrayez le driver « .exe » et stockez-le à l'emplacement du dossier spécifié. Cela se trouve généralement à l'emplacement suivant :

```bash
"C:\\Users\\YourName\\AppData\\Local\\binman\\binman_chromedriver\\win32\\version\\chromedriver.exe"
```

Maintenant, ajoutez les drivers à votre chemin système en spécifiant le chemin du dossier à l'exclusion de l'application. Confirmez l'installation en exécutant la commande de terminal suivante.

```bash
# CHEMIN SYSTÈME DE Chromedriver : "C:\\Users\\YourName\\AppData\\Local\\binman\\binman_chromedriver\\win32\\version\\"
# vérifier l'installation de chromedriver
chromedriver -version
```

## Comment comprendre et inspecter une page web

Une page web est une représentation visuelle d'un document HTML disponible sur Internet et accessible via un navigateur web. Les composants d'une page web, appelés éléments, sont structurés hiérarchiquement dans un arbre DOM HTML (Document Object Model). Chaque élément peut être localisé en utilisant des chemins spécifiques appelés sélecteurs ou localisateurs, que vous pouvez lire plus en détail [ici](https://testrigor.com/blog/css-selector-vs-xpath-your-pocket-cheat-sheet/).

Les outils de développement sont un ensemble d'outils disponibles dans votre navigateur. Ils sont utiles pour inspecter et analyser la structure d'une page web. La fonction « Inspecter » aide à examiner la structure et le style d'un élément spécifique. Vous pouvez accéder à cette fonction en sélectionnant l'élément que vous souhaitez inspecter, en cliquant dessus avec le bouton droit de la souris et en cliquant sur « Inspecter ».

![Inspection d'un élément](https://cdn.hashnode.com/res/hashnode/image/upload/v1739974770342/59c960b1-2c88-4c1d-a23d-d9e9fee91dc5.gif align="center")

## Comment extraire des données avec RVest

RVest est un package R qui contient un ensemble de fonctions permettant d'extraire des données de pages web HTML et XML.

Nous sommes intéressés par l'extraction des informations suivantes sur les livres de chaque page du catalogue du site web :

* Titre du livre

* Note du livre

* Prix du livre

* Lien individuel vers le livre

* Lien vers l'image de couverture

Passons en revue les étapes pour utiliser RVest afin d'extraire ces données.

### **Étape 1 : Charger la page web**

Pour charger la première page de votre site web cible et analyser le document HTML en utilisant le package RVest dans R, suivez ces étapes :

1. **Installer et charger le package RVest** : Si vous n'avez pas encore installé le package RVest, vous pouvez le faire en exécutant la commande suivante dans R :

```r
install.packages("rvest")
```

Ensuite, chargez le package :

```r
library(rvest)
```

2. **Charger la page web et analyser le HTML** : Utilisez la fonction `read_html()` du package RVest pour récupérer et analyser le contenu HTML de la page web. Voici un exemple de la manière de procéder :

```r
# Spécifiez l'URL du site web cible
url <- "https://books.toscrape.com/"

# Récupérez et analysez le contenu HTML
webpage <- read_html(url)
```

Ce code téléchargera le contenu HTML de la page web spécifiée et le convertira en un document XML, ce qui facilitera la structuration et l'organisation des données pour un traitement ou un stockage ultérieur.

### **Étape 2 : Identifier les éléments cibles**

Les éléments cibles sont les éléments HTML qui contiennent les données spécifiques que vous souhaitez extraire.

Une inspection rapide de la page web à l'aide des outils de développement montre que les informations de chaque livre sont contenues dans une balise `article` et font partie d'une liste ordonnée. Il est important de spécifier la balise `<ol>` dans le chemin, car il existe d'autres listes dans l'arbre.

L'opérateur pipe `%>%` facilite l'enchaînement des opérations, ce qui rend plus facile l'extraction des éléments étape par étape. `html_element()` retourne le premier élément correspondant tandis que `html_elements()` retourne tous les éléments qui correspondent au chemin défini.

```r
# définir le chemin à partir duquel d'autres détails seront extraits
book <- books %>% html_element("ol")  %>% html_elements("li") %>% html_element("article")

# extraction des détails en utilisant des localisateurs css.
# titre
title <- book %>% 
  html_element("h3 a") %>% 
  html_attr("title")

# note
rating <- book %>% 
  html_element("p") %>% 
  html_attr("class")

# prix
price <- book %>% 
  html_element(".product_price p") %>% 
  html_text2()

# lien vers la page du livre
book_link <- book %>% 
  html_element("h3 a") %>% 
  html_attr("href")

# lien vers l'image de la page de couverture
cover_page_link <- book %>% 
  html_element(".image_container a img") %>% 
  html_attr("src")

# inspecter le bon format en sélectionnant le premier élément de chaque détail
title[[1]]
rating[[1]]
price[[1]]
book_link[[1]]
cover_page_link[[1]]
```

### **Étape 3 : Nettoyer les données de « note »**

Pour nettoyer les données de « star-rating », vous pouvez utiliser le package `stringr` dans R pour supprimer le texte inutile et rogner les espaces blancs. Voici comment procéder :

```r
library(stringr)

# Exemple de données de note extraites
rating_data <- "star-rating Three"

# Supprimer "star-rating " et rogner les espaces blancs
cleaned_rating <- str_trim(str_replace(rating_data, "star-rating ", ""))

# Afficher la note nettoyée
cleaned_rating
```

Ce code affichera « Three », supprimant ainsi le préfixe « star-rating » et les espaces blancs en début ou fin de chaîne.

## Comment imiter le comportement humain avec RSelenium

### **Comment fonctionne Selenium**

Selenium est un outil qui vous permet de simuler les actions de l'utilisateur sur un site web, généralement à des fins de test. RSelenium est une bibliothèque R qui vous permet d'accéder à cette fonctionnalité.

![Diagramme illustrant l'architecture de Selenium. Il montre un client avec un script Selenium communiquant avec un serveur de driver de navigateur en utilisant le protocole JSON Wire Protocol sur HTTP. Le serveur envoie ensuite une requête HTTP à un navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1739961235501/f358a1e1-6a2f-45dd-a0b0-12925811cab1.png align="center")

Nous avons besoin d'un script, d'un navigateur et d'un driver de navigateur pour imiter le comportement de l'utilisateur. Le code que vous écrivez et qui contient les instructions détaillant les actions que vous souhaitez automatiser est le script. Le driver du navigateur agit comme un pont entre votre script et le navigateur et exécute vos actions souhaitées en traduisant le script en actions.

Le script, lorsqu'il est exécuté, est le client qui demande et reçoit des informations du serveur du driver du navigateur.

Lorsque vous exécutez un script, le script est converti en données au format JSON qui sont ensuite transférées au driver du navigateur via le protocole JSON Wire Protocol. Un protocole est simplement un ensemble de règles qui définissent comment les données doivent être gérées et traitées lors du transfert entre les appareils.

Le driver reçoit et valide les données reçues. Si cela réussit, il communique les actions définies dans le script au navigateur. Si cela échoue, une erreur est envoyée au client.

Lors de l'initialisation du navigateur, le driver exécute les actions étape par étape. Cela continue jusqu'à la fin ou jusqu'à ce qu'une erreur soit rencontrée (éléments manquants, erreurs de serveur, etc.). La communication bidirectionnelle entre le driver et le navigateur se fait via HTTP. Enfin, les résultats sont renvoyés au client et le navigateur est fermé.

### Automatisation de la navigation entre les pages et de la collecte de données avec RSelenium

```r
# installer et charger RSelenium
install.packages("RSelenium")
library(RSelenium)

# initialiser et exécuter le driver chrome
rD <- rsDriver(browser = "chrome", port = 4567L)

# extraire et assigner le client
remDr <- rD[["client"]]
```

L'exécution de `rsDriver()` démarre un serveur Selenium qui lance ChromeDriver. Extrayez et assigner `rD[["client"]]` à une variable. Cette variable vous permet de contrôler et d'interagir avec le navigateur.

Parfois, le démarrage du driver peut échouer pour des raisons telles que des restrictions de permission, des dépendances manquantes ou une configuration incorrecte. Si cela se produit, vous pouvez lancer manuellement ChromeDriver en ajoutant le bloc de code suivant juste après le chargement des bibliothèques en haut du script. Il est important de s'assurer que les numéros de port correspondent.

```r
cDrv <- chrome(verbose = FALSE, check = FALSE, port = 4567L)
cDrv$process
```

Maintenant, naviguez vers la page web cible :

```r
# naviguer vers le site cible
remDr$navigate("https://books.toscrape.com/")

# maximiser la taille de la fenêtre Chrome
remDr$maxWindowSize()
```

Et faites défiler jusqu'en bas de la page :

```r
# faire défiler jusqu'en bas de la page
webElem <- remDr$findElement("css", "body")
webElem$sendKeysToElement(list(key = "end"))
```

Le code ci-dessus localise l'élément body et simule l'appui sur la touche bas jusqu'à la fin de la page.

Maintenant, cliquez sur Suivant pour naviguer vers la page suivante :

```r
# localiser le bouton suivant et cliquer sur suivant
nextPage <-  remDr$findElement(using = "css selector",
                               value = ".next > a")
nextPage$clickElement()
```

Trouvez l'élément qui contient le lien vers la page suivante et cliquez dessus pour vous rediriger.

Maintenant, nous allons écrire une boucle while qui navigue à travers toutes les pages, jusqu'à la page 50, puis ferme le navigateur une fois terminé.

Une boucle while exécute un morceau de code tant qu'une condition spécifique est remplie. Une fois la condition non remplie, la boucle se termine.

```r
while(condition is TRUE){
    #FAIRE QUELQUE CHOSE
}
```

Écrivez une boucle qui assure que le bouton de la page suivante est cliqué tant que l'élément contenant le lien vers la page suivante est visible dans le DOM HTML.

Tout d'abord, localisez l'élément du bouton suivant. Sa présence dans la page web ouverte assure que la boucle s'exécute.

La dernière page n'a pas de bouton suivant, donc la boucle se terminera lorsqu'elle atteindra cette page (et Selenium générera une erreur en raison de l'élément manquant).

```r
nextPage <- remDr$findElement(using = "css selector", value = ".next > a")
```

Enveloppez la recherche de l'élément nextPage dans un bloc `tryCatch()`. Cela empêche le script de planter si le bouton 'Suivant' est manquant. Si une erreur se produit, `tryCatch()` retourne `NULL`, signalant qu'il n'y a plus de pages à naviguer.

Un bloc `if` vérifie ensuite une valeur `NULL`. Si elle est rencontrée, un message est affiché pour informer le client qu'aucun bouton 'Suivant' n'a été trouvé, et l'instruction `break` quitte la boucle.

Enfin, fermez le navigateur une fois que le driver a navigué jusqu'à la dernière page (page 50 dans le catalogue) pour libérer les ressources système en utilisant `remDr$close()`.

```r

while (TRUE) {  
  # Essayer de trouver et cliquer sur le bouton "Suivant"
  nextPage <- tryCatch({
    remDr$findElement(using = "css selector", value = ".next > a")
  }, error = function(e) {
    return(NULL)  # Plus de pages
  })
  
  if (is.null(nextPage)) {
    message("Aucun bouton 'Suivant' trouvé. Sortie de la boucle.")
    break
  }
  
  nextPage$clickElement()
  Sys.sleep(3)  # Permettre à la page suivante de se charger
   
}
print("fin du scraping")
remDr$close()
```

## Comment combiner RSelenium et RVest et sauvegarder en CSV

Maintenant que nous avons extrait des données d'éléments HTML spécifiques en utilisant RVest et automatisé les actions de l'utilisateur en utilisant RSelenium, combinons les deux pour extraire des données de toutes les pages du site web.

### **Créer une fonction de scraping de livres**

Vous allez sauvegarder les informations des livres extraites dans un fichier CSV. Tout d'abord, créez un dataframe vide pour contenir les données extraites :

```r
# installer et charger dplyr pour la manipulation de dataframe
install.packages("dplyr")
library(dplyr)

# créer un dataframe pour contenir les informations sur les livres
Books <-  data.frame()
```

### Récupérer et analyser la page web

Pour que Rvest fonctionne avec RSelenium, vous devez récupérer la source HTML de la page web actuellement chargée dans le navigateur contrôlé par Selenium en utilisant `remDr$getPageSource()[[1]]` pour extraire le contenu HTML.

```r
page <- remDr$getPageSource()[[1]]
```

Convertissez le contenu HTML en XML en utilisant `read_html()` comme ceci :

```r
 # définir le chemin à partir duquel d'autres détails seront extraits
    books <- read_html(page)  %>% html_element("ol")  %>% html_elements("li") %>% html_element("article")
```

Extrayez les détails de chaque livre en utilisant des sélecteurs CSS avec les fonctions `rvest`. Les objets extraits retournés sont des objets XML et des listes. Ils doivent être formatés en chaînes de caractères, évitant ainsi les problèmes de type de données inattendus lors de la manipulation des données. Faites cela en ajoutant `as.character()` à la toute fin de chaque détail extrait.

```r
    # titre
    title <- book %>% 
      html_element("h3 a") %>% 
      html_attr("title") %>% 
      as.character() 
```

Enveloppez le bloc de code utilisé pour extraire les détails des éléments HTML dans une fonction et retournez un dataframe dont les valeurs de colonnes sont les détails des livres. Cela rend le code réutilisable et modulaire.

```r

scrape_books <- function() {
    page <- remDr$getPageSource()[[1]]
      
    # définir le chemin à partir duquel d'autres détails seront extraits
    books <- read_html(page)  %>% html_element("ol")  %>% html_elements("li") %>% html_element("article")
    
    # extraction des détails en utilisant des localisateurs css.
    # titre
    title <- book %>% 
      html_element("h3 a") %>% 
      html_attr("title") %>% 
      as.character() 
    
    # note
    rating <- book %>% 
      html_element("p") %>% 
      html_attr("class") %>% 
      as.character() 
    
    cleaned_rating <- str_trim(gsub("star-rating", "", rating))
    
    # prix
    price <- book %>% 
      html_element(".product_price p") %>% 
      html_text2() %>% 
      as.character() 
    
    # lien vers la page du livre
    book_link <- book %>% 
      html_element("h3 a") %>% 
      html_attr("href") %>% 
      as.character() 
    
    # lien vers l'image
    cover_page_link <- book %>% 
      html_element(".image_container a img") %>% 
      html_attr("src") %>% 
      as.character() 
        
    return(data.frame(title,cleaned_rating,price,book_link,cover_page_link, stringsAsFactors = FALSE))
}
```

### **Écrire dans un CSV**

Enregistrez le dataframe dans un fichier CSV enregistré sous le nom « books.csv » :

```r
write.csv(Books, file = "./books.csv", fileEncoding = "UTF-8")
```

## Tout rassembler

Récapitulons ce que nous avons fait jusqu'à présent : Tout d'abord, le script pour extraire les données des livres commence par charger le navigateur, maximiser la taille de la fenêtre et naviguer vers la page Books To Scrape.

Ensuite, nous avons créé un dataframe vide pour contenir les données extraites. Nous avons ensuite extrait les données de la première page, les avons enregistrées dans le dataframe et avons localisé le bouton 'Suivant' afin de naviguer vers la page suivante - à partir de laquelle nous avons extrait des données et les avons stockées.

Le processus d'extraction, d'ajout au dataframe et de clic sur le bouton de la page suivante continue jusqu'à ce que le bouton 'Suivant' ne soit plus disponible dans le DOM HTML.

Une fois la dernière page atteinte, le code quitte la boucle et enregistre les données dans un fichier CSV. Enfin, il ferme le driver pour libérer les ressources système.

```r
# charger les bibliothèques
library(wdman)
library(binman)
library(rvest)
library(stringr)
library(RSelenium)
library(dplyr)


cDrv <- chrome(verbose = FALSE, check = FALSE, port = 4450L)
cDrv$process

rD <- rsDriver(browser = "chrome", port = 4450L)
remDr <- rD[["client"]]


remDr$navigate("https://books.toscrape.com/")
remDr$maxWindowSize()

page <- remDr$getPageSource()[[1]]
webElem <- remDr$findElement("css", "body")
webElem$sendKeysToElement(list(key = "end"))

nextPage <-  remDr$findElement(using = "css selector",
                               value = ".next > a")
nextPage$clickElement()


# convertir les listes contenant les données extraites en un dataframe 
Books <-  data.frame(title = character(), rating = character(), stringsAsFactors = FALSE)

scrape_books <- function() {
    page <- remDr$getPageSource()[[1]]
      
    # définir le chemin à partir duquel d'autres détails seront extraits
    books <- read_html(page)  %>% html_element("ol")  %>% html_elements("li") %>% html_element("article")
    
    # extraction des détails en utilisant des localisateurs css.
    # titre
    title <- book %>% 
      html_element("h3 a") %>% 
      html_attr("title") %>% 
      as.character() 
    
    # note
    rating <- book %>% 
      html_element("p") %>% 
      html_attr("class") %>% 
      as.character() 
    
    cleaned_rating <- str_trim(gsub("star-rating", "", rating))
    
    # prix
    price <- book %>% 
      html_element(".product_price p") %>% 
      html_text2() %>% 
      as.character() 
    
    # lien vers la page du livre
    book_link <- book %>% 
      html_element("h3 a") %>% 
      html_attr("href") %>% 
      as.character() 
    
    # lien vers l'image
    cover_page_link <- book %>% 
      html_element(".image_container a img") %>% 
      html_attr("src") %>% 
      as.character() 
        
    return(data.frame(title,cleaned_rating,price,book_link,cover_page_link, stringsAsFactors = FALSE))
}

# extraire la première page
Books <- rbind(Books, scrape_books())

while (TRUE) {
  # extraire la page actuelle
  Books <- rbind(Books, scrape_books())
  
  # trouver et cliquer sur le bouton "suivant"
  nextPage <- tryCatch({
    remDr$findElement(using = "css selector", value = ".next > a")
  }, error = function(e) {
    return(NULL)  # Plus de pages
  })
  
  # quitter la boucle si le bouton "suivant" est manquant
  if (is.null(nextPage)) {
    message("Aucun bouton 'Suivant' trouvé. Sortie de la boucle.")
    break
  }
  
  nextPage$clickElement()
  # Permettre à la page suivante de se charger
  Sys.sleep(3)  
 
}

write.csv(Books, file = "./books.csv", fileEncoding = "UTF-8")
print("fin du scraping")
remDr$close()
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1740129915080/2ee1344b-58a8-477b-a568-719ba4336c95.png align="center")

## Conclusion

Dans ce tutoriel, vous avez appris comment combiner efficacement RSelenium et RVest pour extraire des données d'un site web. En utilisant RSelenium, vous pouvez automatiser les interactions de l'utilisateur et naviguer à travers les pages web, tandis que RVest vous permet d'extraire des données spécifiques à partir d'éléments HTML.

Cette approche offre une méthode puissante et flexible pour le web scraping, vous permettant de gérer du contenu dynamique et d'imiter le comportement humain. En suivant les étapes décrites ici, vous pouvez extraire avec succès des données de plusieurs pages et les sauvegarder dans un fichier CSV pour une analyse ultérieure.