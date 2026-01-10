---
title: Comment créer une course de graphiques à barres sur les cas de COVID-19 en
  5 minutes avec Tableau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-24T10:22:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-bar-chart-race-on-covid-19-cases-in-tableau
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b79740569d1a4ca2c0c.jpg
tags:
- name: Covid-19
  slug: covid-19
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: tableau
  slug: tableau
- name: Tutorial
  slug: tutorial
seo_title: Comment créer une course de graphiques à barres sur les cas de COVID-19
  en 5 minutes avec Tableau
seo_desc: "By Black Raven\nWhen you build a bar chart race, you're creating many discrete\
  \ pages of bar charts and then stringing them together. This is just like how traditional\
  \ cartoon animation works. \nIn December 2019, Tableau released version 2020.1 beta\
  \ wit..."
---

Par Black Raven

Lorsque vous créez une course de graphiques à barres, vous créez de nombreuses pages discrètes de graphiques à barres que vous assemblez ensuite. Cela fonctionne comme l'animation traditionnelle de dessins animés. 

En décembre 2019, Tableau a publié la version 2020.1 bêta avec une nouvelle fonctionnalité d'Animations pour les paramètres dynamiques. Cela signifie que la [course de graphiques à barres](https://public.tableau.com/profile/blackraven#!/vizhome/COVIT-19DailyInfectedCases/COVIT-19DailyInfectedCases) ci-dessous est désormais très facile à créer.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_Rv9h7WGf9JJn43BfqRBKsA.gif)
_Regardez-la en action : [https://www.youtube.com/watch?v=3iZrMkZ3948](https://www.youtube.com/watch?v=3iZrMkZ3948" rel="noopener nofollow)_

## Prérequis

Téléchargez et installez [Tableau Public](https://public.tableau.com/s/) (version 2020.1.2 ou ultérieure). Il est totalement gratuit et dispose de toutes les fonctionnalités. Le seul inconvénient est que tous vos travaux ne peuvent être publiés que sur le serveur Tableau Public, et non sauvegardés localement sur votre bureau. Cela est acceptable si les données ne sont pas sensibles ou privées.

Téléchargez les dernières [données sur le COVID-19](https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-04-22.xlsx) (au format *.xlsx) depuis le site du Centre européen de prévention et de contrôle des maladies [website](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide), et renommez-le avec un nom générique comme "COVID-19-geographic-distribution-worldwide.xlsx". Vous pouvez remplacer ce fichier par des données mises à jour plus tard, en utilisant le même nom de fichier.

Ouvrez l'application Tableau Public, et dans le menu "Connect", cliquez sur "Microsoft Excel" et sélectionnez le fichier de données que vous avez téléchargé. Cliquez sur l'onglet "Sheet 1" en bas à gauche.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_ejwEHqjx6YjF4jA2vLOapg.png)
_Connecter Tableau Public au jeu de données_

## Identifier la quantité à animer

Il y a 2 quantités utiles que vous pouvez choisir d'animer dans ce jeu de données :

* Cas infectés quotidiens, ou
* Cas de décès quotidiens.

Pour choisir la quantité à animer comme cas infectés quotidiens, glissez "Cases" vers Colonnes.

Pour étiqueter le graphique à barres avec les noms des pays, glissez "Countries And Territories" vers Label.

Pour avoir les barres en différentes couleurs, glissez "Countries And Territories" vers Color.

## Créer un classement pour les pays

Cette section nécessite une simple ligne de code de programmation.

Cliquez sur Dimensions → menu déroulant → Create Calculated Field.  
Créez un nouveau champ "Rank", et entrez le code ci-dessous :

**RANK_UNIQUE(Sum([Cases]))**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_MiqkR2XocHAAj277ErV1jg.png)
_Pour coder le champ calculé "Rank"_

Cliquez sur "Apply" pour vous assurer que le calcul est valide, puis cliquez sur "OK".

Glissez "Rank" vers Rows.  
Cliquez sur (Rows) Rank → menu déroulant → Discrete.  
Cliquez sur (Rows) Rank → menu déroulant → Compute Using → "Countries And Territories".

## Configurer l'animation (Nouvelle fonctionnalité pour la version 2020.1)

Pour créer une capture des frames d'animation, glissez "Date Rep" vers Pages.   
Cliquez sur (Pages) Date Rep → menu déroulant → Exact Date.

Activez les animations, sélectionnez Format → Animations → On.  
Pour définir la durée de la transition : Duration → "1.00 seconds (Slow)".  
Fermez la fenêtre Animations en cliquant sur "X".

Cherchez un petit contrôle d'Animations qui apparaît lorsque la fonctionnalité d'animations est activée, puis cliquez sur l'icône "forward play". Faites glisser la barre de défilement à une date différente ou utilisez le bouton gauche/droit pour choisir une date.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_Lc4M3sx0DSp5PrRA6znFjQ.png)
_Contrôle des animations_

## Ajouter une personnalisation simple

### Pour améliorer les couleurs :

Cliquez sur Label → assurez-vous que "Show mark labels" est coché.  
Cliquez sur Color → Edit Colors → remplacez les couleurs similaires si nécessaire.  
(J'ai remplacé les couleurs pour les USA, l'Espagne, l'Italie)

Vous pouvez masquer la carte de légende des pays – elle n'est plus nécessaire.

### Pour ajouter des étiquettes supplémentaires pour le nombre de cas sur les barres :

Glissez "Cases" vers Label.  
Cliquez sur Label → Text → cliquez sur "3 dots". Cela ouvre l'éditeur d'étiquettes.  
Organisez les étiquettes sur 1 ligne seulement.  
Soulignez <Countries And Territories>.  
Mettez <SUM(Cases)> en gras, et utilisez une police rouge.  
Cliquez sur "OK".

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_cQEuF4ppqaIqpHmvPvkWXQ.png)
_Éditeur d'étiquettes_

### Pour changer le nom de la feuille :

Double-cliquez sur "Sheet 1" et changez-le en "COVID-19 Daily Infected Cases".

### Pour changer les limites de l'axe X :

Double-cliquez sur l'axe X. Cela ouvre le menu Axis. Choisissez la Range pour être "Fixed" : Fixed start=0, Fixed end=40,000.

### Pour afficher uniquement les 15 premiers pays :

Glissez "Rank" vers Filters → cliquez sur "OK".  
Cliquez sur (Filters) Rank → menu déroulant → Compute Using → "Countries And Territories".  
Remplacez "206" par "15", et cliquez sur "OK".  
Changez la vue Standard en "Fit Height".

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_n_fm0Q4EtWUhpgi0eizV8A--1-.png)
_Afficher le graphique en utilisant 'Fit Height'_

### Pour augmenter la taille de la police des étiquettes :

Cliquez sur Label → Font → menu déroulant → changez la taille de la police en "15".

### Pour ajouter une étiquette de date au graphique :

Cliquez avec le bouton droit sur la zone vide du graphique → Annotate → Area.  
Cela ouvre l'éditeur d'annotations.  
Entrez <Page Name>, et augmentez la taille de la police à "20".  
Cliquez sur "OK".

Maintenant que l'étiquette de date a été créée, redimensionnez-la et déplacez-la en bas.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/1_YMbjCFpQJIgRUrb7oEbThg.png)
_Éditeur d'annotations_

## Publier la visualisation

Lorsque vous êtes satisfait de la personnalisation, la visualisation est alors prête à être publiée.

Cliquez sur File → Save to Tableau Public.

Le travail est maintenant [publié sur le serveur Tableau Public](https://public.tableau.com/profile/blackraven#!/vizhome/COVIT-19DailyInfectedCases/COVIT-19DailyInfectedCases). Vous pouvez ensuite le partager en utilisant le lien disponible.

Voici un tutoriel vidéo avec un guide étape par étape pour l'ensemble du processus :

%[https://youtu.be/ZnEuq6SHIUI]



Une course de graphiques à barres devient très simple à créer en utilisant la nouvelle fonctionnalité d'Animations dans Tableau Version 2020.1 et ultérieures. Vous pouvez maintenant l'essayer sur d'autres données de pays avec des séries temporelles : PIB, Population, Espérance de vie, etc.

Laissez libre cours à votre créativité !