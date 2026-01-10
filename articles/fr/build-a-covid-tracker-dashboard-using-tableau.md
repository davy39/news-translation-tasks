---
title: Tutoriel Tableau – Comment créer votre propre tableau de bord de suivi COVID
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-03-18T18:15:46.000Z'
originalURL: https://freecodecamp.org/news/build-a-covid-tracker-dashboard-using-tableau
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Blue-and-Ivory-Photo-Musician-Influencer-Digital-Brutalism-YouTube-Thumbnail-Set--2-.png
tags:
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: tableau
  slug: tableau
seo_title: Tutoriel Tableau – Comment créer votre propre tableau de bord de suivi
  COVID
seo_desc: 'I don’t use Tableau for my data science work, but I have done a couple
  of mini-projects to help me review the interface and learn what the hype is all
  about.

  So yesterday, I decided to create a complete dashboard using Tableau.

  I wanted to compare th...'
---

Je n'utilise pas Tableau pour mon travail en science des données, mais j'ai réalisé quelques mini-projets pour m'aider à revoir l'interface et comprendre ce qui fait tout ce battage médiatique.

Alors hier, j'ai décidé de créer un tableau de bord complet en utilisant Tableau.

Je voulais comparer la facilité de construction, le temps nécessaire pour compléter le projet et la qualité du tableau de bord. J'ai donc choisi de le baser sur le nombre de cas de nouveau coronavirus dans le monde, puisque j'avais construit un [tableau de bord similaire affichant les cas de COVID en utilisant Python, Jupyter Notebook et Voila](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb).

## Prérequis pour ce tutoriel rapide

Il n'y a rien de majeur – assurez-vous simplement d'avoir [Tableau public installé](https://public.tableau.com/en-us/s/download).

Pour mieux comprendre la différence marquée entre les deux approches – c'est-à-dire, construire un [tableau de bord](https://covid-19-voila-dashboard.herokuapp.com/) en utilisant la programmation versus le construire avec Tableau – parcourez simplement mon [article sur la construction d'un tableau de bord interactif COVID-19 à partir de Jupyter Notebooks](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb) ou regardez la vidéo [ici](https://youtu.be/FngV4VdYrkA).

Vous pouvez voir mon tableau de bord basé sur Python [ici](https://covid-19-voila-dashboard.herokuapp.com/).

Commençons à construire...

# Comment trouver une bonne source de données

La première étape consiste à trouver une source de données crédible étant donné la gravité du sujet que nous avons choisi.

Pour cela, nous allons utiliser le [Dépôt de données COVID-19 du Center for Systems Science and Engineering (CSSE) de l'Université Johns Hopkins](https://github.com/CSSEGISandData/COVID-19)¹.

Ce dépôt est maintenu par un certain nombre de contributeurs de l'université et est mis à jour régulièrement.

Il existe de nombreux types de jeux de données différents, mais pour garder les choses simples pour l'instant, nous allons utiliser les données spécifiques aux pays qui nous donnent le nombre le plus récent de différents types de cas (actifs, confirmés, décès, rétablis) pour différents pays/régions du monde.

Voici le lien brut vers le fichier :

[https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv)

Il s'agit d'un fichier CSV qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/2-1.png align="left")

# Comment charger les données dans Tableau

Il existe plusieurs façons de charger des données dans Tableau, notamment :

* Télécharger des fichiers depuis votre machine locale — Excel, CSV, texte, JSON, PDF, Spatial, et ainsi de suite.

* Se connecter à des données stockées sur un serveur — vous pouvez charger directement des données depuis Tableau Server, Google Cloud Storage/Analytics, MS SQL Server, et autres. Vous pouvez utiliser des connecteurs de données déjà disponibles pour ces sources.

* Vous pouvez également vous connecter à des sources auxquelles vous vous êtes déjà connecté.

Dans notre cas, nous voulons charger le fichier CSV brut disponible sur GitHub directement dans Tableau. À cette fin, nous pouvons utiliser un connecteur web CSV développé par Keshia Rose.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/3.png align="left")

Voici le lien vers le connecteur : [https://basic-csv-wdc.herokuapp.com/](https://basic-csv-wdc.herokuapp.com/)

Et voici les étapes pour charger les données :

* Dans le panneau Connexion, cliquez sur `**Web Data Connector**`.

* Ajoutez l'URL du connecteur dans le champ qui apparaît et appuyez sur `Entrée`.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/4.png align="left")

* Maintenant, ajoutez le lien vers le fichier CSV brut dans le champ de recherche et cliquez sur `**Get Data!**`.

Il faudra quelques secondes pour charger les données, puis vous pourrez cliquer sur `Update now` pour enfin jeter un coup d'œil aux données disponibles dans le fichier :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/5.png align="left")

# Comment explorer les données dans Tableau

Tableau présente les données de manière très intuitive. Nous pouvons en apprendre davantage sur les attributs de base des données et leurs types directement à partir de l'aperçu et des métadonnées.

À partir de l'aperçu, nous pouvons découvrir les caractéristiques que nous avons dans le jeu de données, ce qui définit davantage les questions qui nous intéressent concernant le problème en question.

À partir de la vue des métadonnées, nous pouvons découvrir les types de données (catégorielles/quantitatives/DateTime, etc.) de ces caractéristiques, ce qui nous indique comment nous pouvons analyser ces caractéristiques en combinaison avec d'autres.

En cliquant sur la vue des métadonnées, les colonnes s'affichent avec leurs noms et types :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-15-at-4.11.21-AM.png align="left")

Il est important de comprendre la signification des caractéristiques et leurs types de données :

**Comment trouver le type de données d'une variable** — représenté par les notations.
`**#**` — désigne le type de données numérique.
`**Abc**` — désigne le type de données catégorielles/chaîne.
`🌐` — désigne les valeurs géographiques.

En plus de ceux-ci, nous avons également des notations DateTime, clusters et booléennes.

Cela devrait nous aider à comprendre ce que nous pouvons faire avec ce jeu de données.

Puisque les données sont déjà propres et formatées, nous pouvons sauter la partie de nettoyage et passer à la définition de ce que nous voulons de cette analyse.

Alors, passons à l'étape suivante.

# Comment définir des questions basées sur les colonnes

En fonction des caractéristiques que nous avons et de leurs types de données, nous pouvons chercher à répondre aux questions suivantes :

* Quel est le nombre actuel de cas de COVID dans le monde (total actif, confirmé, décès) ?

* Quel est l'état actuel des pays — si nous pouvons visualiser cela dans un seul cadre ?

* Quels sont les pays les plus touchés en termes de nombre de cas et de taux de mortalité ?

Vous pouvez ajouter et définir plus ou différentes questions, mais je vais vous guider à travers celles-ci pour l'instant.

Il est temps de se mettre à répondre à ces questions.

# Comment fonctionne l'interface de Tableau

Voici un rapide tour de l'interface de Tableau.

→ En bas, vous verrez qu'il y a un certain nombre d'icônes, celles-ci sont pour :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-15-at-5.12.58-PM.png align="left")

* vérifier la source de données connectée

* ajouter de nouvelles feuilles

* ajouter de nouveaux tableaux de bord

* ajouter de nouvelles histoires.

→ Cliquez sur la Feuille 1 qui est créée pour nous par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1_fzpOZKI0SHyEMZvTYG0Lcg.png align="left")

Sur l'image ci-dessus, j'ai annoté uniquement les parties importantes de l'interface. Nous pouvons effectuer la plupart de l'analyse en faisant glisser et en déposant des caractéristiques dans les colonnes et les lignes.

# Comment créer des visualisations dans Tableau

Nous allons maintenant passer en revue chaque question et créer une feuille dédiée pour analyser les données afin de répondre à cette question.

## #1 Nombre total de cas

Pour répondre à cela, nous allons utiliser les colonnes suivantes :

* Confirmés

* Décès

* Actifs

Maintenant, Tableau sait que ce sont des mesures quantitatives et ajoute un agrégateur par défaut (SOMME dans ce cas) dès que vous essayez de faire glisser et de déposer l'une de celles-ci. Vous pouvez changer l'agrégateur à tout moment en utilisant les Marques.

Pour visualiser le nombre total (SOMME) de cas, il suffit de faire glisser chacune des caractéristiques ci-dessus et de les placer dans le champ des colonnes en haut.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/6.png align="left")

> *À tout moment, si quelque chose ne va pas, vous pouvez utiliser* `_Cmd/Ctrl + z_` *pour annuler.*

![Image](https://www.freecodecamp.org/news/content/images/2021/03/7.png align="left")

De plus, vous pouvez changer la couleur de chacune des barres en utilisant les Marques dans le panneau de gauche.

Vous pouvez également jouer avec la police, la couleur du texte, l'ombre, et plus encore en cliquant avec le bouton droit sur la visualisation de données que vous souhaitez formater.

Voici à quoi ressemble ma visualisation formatée après quelques changements (couleur et largeur).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/8.png align="left")

→ Suffisamment décent pour la quantité d'efforts que nous avons mis. Cela aurait pris beaucoup plus de temps et d'efforts pour coder cela.

Super, passons à la partie suivante.

## #2 Carte du monde qui affiche les cas de COVID dans chaque pays/région

Puisque nous avons des dimensions géospatiales dans les données, nous pouvons chercher à tracer les nombres sur une carte du monde pour visualiser la situation dans chaque pays par rapport à notre variable de choix.

Je vais tracer le nombre de cas (confirmés, actifs et décès) sur la carte du monde en utilisant les colonnes Latitude et Longitude. Celles-ci sont générées par Tableau à partir des variables Lat/Long et sont en italique dans le panneau des Tables.

Comment faire cela :

* La première étape consiste à ajouter une nouvelle feuille en cliquant sur l'icône adjacente à `Feuille 1`

* Faites glisser la *Longitude* *(générée)* et déposez-la dans Colonnes

* Faites glisser *Latitude* *(générée)* et déposez-la dans Lignes. Après avoir fait cela, vous aurez une carte du monde vierge dans la vue principale.

* Pour ajouter les noms des pays, déposez la colonne `Région du pays` dans la boîte des détails du panneau des Marques. Cela produira la carte des symboles avec les noms des pays s'affichant dans l'infobulle.

* Maintenant, nous avons un panneau `Show Me` en haut à droite qui nous montre toutes les visualisations que vous pouvez utiliser. Les graphiques qui sont grisés ne sont pas applicables et lorsque vous passez la souris dessus, il vous indiquera tous les types de colonnes dont vous avez besoin pour rendre ce graphique applicable. Faites-le pour la carte du monde et vous apprendrez que nous avons besoin d'au moins 1 dimension géospatiale, 0 ou plusieurs dimensions, et 0 ou 1 mesure.

* Il est temps d'ajouter la mesure, c'est-à-dire la variable que nous voulons visualiser. Je choisis le nombre de cas confirmés. Faites glisser et déposez la colonne Confirmés dans la boîte des Étiquettes du panneau des Marques.

Vous pouvez également ajouter d'autres variables à la boîte des détails si vous souhaitez les ajouter aux informations.

Voici à quoi ressemble ma carte des symboles :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/9.png align="left")

N'hésitez pas à jouer avec l'autre carte, à ajouter des couleurs ou à formater ce que vous voulez voir sur la carte.

## #3 Pays les plus touchés

Les nombres totaux et la carte du monde ne peuvent vous donner qu'un bref aperçu de la pandémie.

Alors, plongeons un peu plus profondément pour voir quels pays sont les plus touchés en termes de cas confirmés, de décès et de taux de mortalité, et quels pays ont des taux de rétablissement élevés.

Ces données sont très simples à tracer. Voici les étapes :

* Ajoutez une nouvelle feuille.

* Faites glisser et déposez la caractéristique `Région du pays` dans Colonnes.

* Faites glisser et déposez `SOMME(Confirmés)` dans Lignes. Vous aurez un graphique à barres prêt pour vous dans la vue principale avec les pays sur l'axe X et le nombre de cas confirmés sur l'axe Y.

* Puisque nous devons examiner les pays les plus touchés, nous devons trier les données, et Tableau le rend très facile pour nous. Tout ce que nous devons faire est de cliquer sur l'icône `Trier par ordre décroissant` dans la barre des tâches en haut.

* Avec toutes les barres alignées par ordre décroissant, nous voulons simplement en sélectionner quelques-unes qui sont au-dessus d'un certain seuil – disons les 10 premières. Maintenez votre curseur dans un état cliqué et faites-le glisser sur le nombre de barres que vous souhaitez présélectionner.

* Passez la souris sur les barres présélectionnées et cliquez sur Conserver uniquement dans la fenêtre contextuelle qui apparaît. Cela vous donnera un graphique épuré.

* Vous pouvez activer les étiquettes à partir de la barre des tâches ou déposer SOMME (Confirmés) dans la boîte des Étiquettes.

Et encore une fois, vous pouvez ajouter des couleurs, formater comme vous le souhaitez, annoter et faire plus avec ces données.

Voici les graphiques que j'ai créés en utilisant les étapes ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-5.55.49-AM.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-5.56.08-AM.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-17-at-5.56.35-AM.png align="left")

> *N'oubliez pas de renommer vos feuilles selon leur cas d'utilisation.*

## Comment créer un tableau de bord à partir de ces feuilles

Avec suffisamment de visualisations et de chiffres, nous pouvons maintenant tout mettre sur un seul écran pour créer un tableau de bord interactif rapide.

Cette dernière étape est très simple – tout ce que vous avez à faire est de cliquer sur l'icône `Nouveau tableau de bord` en bas.

Cela créera une vue de tableau de bord vide, vous invitant à déposer les feuilles que vous souhaitez voir apparaître dans votre tableau de bord depuis le panneau de gauche.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/10.png align="left")

Vous pouvez faire glisser et déposer les feuilles vers le tableau de bord, puis les positionner pour rendre votre tableau de bord perspicace et attrayant.

Voici mon tableau de bord final :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/11.png align="left")

Si vous souhaitez apporter des modifications à l'une des visualisations, vous pouvez revenir à cette feuille et les modifications seront automatiquement reflétées dans le tableau de bord.

## Comment partager votre tableau de bord

Vous pouvez enregistrer toutes vos modifications dans vos notebooks/tableau de bord sur le serveur public de Tableau en créant votre propre compte personnel.

L'enregistrement du tableau de bord créera un lien public que vous pourrez partager avec vos collègues analystes, collaborateurs ou amis.

Vous pouvez voir mon tableau de bord ici :

[https://public.tableau.com/profile/harshit.tyagi#!/vizhome/covid_book/Dashboard1](https://public.tableau.com/profile/harshit.tyagi#!/vizhome/covid_book/Dashboard1).

# Conclusion

Après avoir construit ce tableau de bord en utilisant Tableau, je l'ai comparé à la quantité d'efforts qu'il m'a fallu pour créer le même en utilisant Python et Jupyter Notebook. J'ai essayé d'évaluer les deux méthodologies sur différentes métriques sur une échelle de 1 à 5, où 5 est le meilleur et 1 est le pire :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/12.png align="left")

Tableau s'avère être le grand gagnant ici !

Je peux dire que Tableau semble être un choix judicieux et efficace en termes de temps, au moins pour ce type de scénarios.

> Avertissement : Il peut être incorrect de comparer un langage de programmation avec un logiciel d'analyse de données. Il s'agit d'une comparaison amusante qui n'est applicable que dans ce type de tâche de construction de tableau de bord. Il s'agit de mon opinion personnelle selon mes expériences et vous devriez trouver le meilleur choix d'outil pour vous-même.

## Projet en direct

Si vous souhaitez travailler sur quelque chose de similaire mais plus avancé, vous devriez consulter mon projet en direct sur [Manning](https://www.manning.com/liveproject/predicting-disease-outbreaks-with-time-series-analysis?utm_source=harshit&utm_medium=affiliate&utm_campaign=liveproject_tyagi_predicting_3_11_21&a_aid=harshit&a_bid=f5119f17).

## **Version vidéo de ce blog !**

%[https://youtu.be/EeMfwaPf4IQ]

Si ce tutoriel vous a été utile, vous devriez consulter mes cours de science des données et de machine learning sur [Wiplane Academy](https://www.wiplane.com/). Ils sont complets mais compacts et vous aident à construire une base solide de travail à présenter.

Citation(s) :

[1] : Dong E, Du H, Gardner L. Un tableau de bord web interactif pour suivre COVID-19 en temps réel. Lancet Inf Dis. 20(5):533–534. doi: 10.1016/S1473–3099(20)30120–1