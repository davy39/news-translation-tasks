---
title: Comment analyser et visualiser de grands ensembles de données avec Microsoft
  Excel en utilisant les tableaux croisés dynamiques et les graphiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-05T17:40:39.000Z'
originalURL: https://freecodecamp.org/news/analyze-and-visualize-large-datasets-with-excel-pivot-tables-charts
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/all-charts-with-conditional-formatting-1.PNG
tags:
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
- name: excel
  slug: excel
seo_title: Comment analyser et visualiser de grands ensembles de données avec Microsoft
  Excel en utilisant les tableaux croisés dynamiques et les graphiques
seo_desc: "By Samuel A. Olubiyo\nMicrosoft Excel is a very powerful tool that you\
  \ can use to analyze and visualize data. \nIn this tutorial, you will learn how\
  \ to build a simple Excel Dashboard that visualizes important data from a large\
  \ dataset. \nThe dataset we'..."
---

Par Samuel A. Olubiyo

Microsoft Excel est un outil très puissant que vous pouvez utiliser pour analyser et visualiser des données. 

Dans ce tutoriel, vous apprendrez à créer un simple tableau de bord Excel qui visualise les données importantes d'un grand ensemble de données. 

L'ensemble de données avec lequel nous allons travailler est l'historique des transactions d'un supermarché sur une période de quatre ans. Notre objectif est d'obtenir des informations importantes à partir de cet ensemble de données et de visualiser ces informations graphiquement avec Microsoft Excel.

Ce tutoriel est conçu pour ceux qui sont déjà familiers avec Excel. Vous y apprendrez :

* Comment formater les dates dans Excel en utilisant la fonction TEXTE.
* Comment trier l'ensemble des données.
* Comment créer plusieurs tableaux croisés dynamiques sur la même feuille de calcul.
* Comment créer des graphiques basés sur le tableau croisé dynamique.
* Comment créer des segments pour filtrer les données, et enfin,
* Comment utiliser la mise en forme conditionnelle.

Afin de tirer le meilleur parti de ce tutoriel, j'ai fourni un ensemble de données que vous pouvez utiliser. Vous pouvez [le télécharger ici](https://github.com/Lordsamdev/superstoredata/blob/main/Super%20Store%20Dataset.xlsx).

Si vous êtes nouveau dans l'analyse et la visualisation de données avec Excel, le site web de freeCodeCamp contient de nombreux tutoriels pour débutants. [Voici un lien vers des articles sur Excel, du niveau débutant à avancé](https://www.freecodecamp.org/news/tag/excel/) si vous avez besoin de rafraîchir vos compétences.

## Notre ensemble de données

Après avoir téléchargé le fichier Excel et l'avoir ouvert, vous remarquerez une chose instantanément : les données sont énormes ! Il s'agit d'un ensemble de données contenant les transactions d'un supermarché sur une période de quatre ans (de 2014 à 2017). 

Ce fichier Excel est composé de 9995 lignes et 21 colonnes. Nous ne pouvons pas obtenir d'informations utiles à partir de cet ensemble de données simplement en le regardant, c'est pourquoi nous devons l'analyser et le visualiser.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Data-Overview.PNG)
_Capture d'écran de l'ensemble de données_

Le moyen le plus simple de le faire est d'utiliser les tableaux croisés dynamiques. Un tableau croisé dynamique est l'un des outils puissants de Microsoft Excel que vous pouvez utiliser pour calculer, analyser et résumer des données. Il vous aide à voir les comparaisons, les tendances et les motifs dans vos données et vous apprendrez à l'utiliser dans ce tutoriel.

Avant de continuer, examinons à nouveau l'ensemble de données : la colonne C contient les dates de commande pour chaque produit vendu. La colonne de date de commande est importante dans ce tutoriel, car nous devons trier l'ensemble des données en fonction des dates auxquelles chaque client a commandé un produit.

## Comment formater les dates dans Excel en utilisant la fonction TEXTE

Dans notre ensemble de données, les dates sont disposées de manière désordonnée et le formatage des dates rend difficile la détermination exacte de la date à laquelle chaque client a commandé un produit. Pour corriger cela, nous utiliserons la fonction TEXTE pour convertir les dates en texte.

Avant de faire cela, insérez une nouvelle colonne à côté de la colonne C. Ce sera votre nouvelle colonne D et c'est là que résideront les dates nouvellement formatées. Vous pouvez lui donner un nouveau nom – dans mon cas, je l'ai nommée « Dates formatées ».

Une fois cela fait, insérez la formule dans la capture d'écran ci-dessous et appuyez sur Entrée :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/formatting-a-date.PNG)
_Formule pour convertir les dates en texte_

Ou copiez et collez simplement la formule ci-dessous :

=TEXTE(C2; "j mmmm aaaa")

Bien sûr, la formule ne fonctionne que pour la première cellule de la colonne. Pour la répéter dans toute la colonne, double-cliquez simplement sur le petit nœud à l'extrémité droite de la cellule lorsqu'elle est mise en surbrillance (comme vous pouvez le voir dans la capture d'écran ci-dessous) :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/flash-fill-node.PNG)
_Cliquez sur le nœud pour remplir automatiquement les cellules restantes de la colonne_

Maintenant, vous devriez avoir des dates dans un format plus lisible dans la colonne D.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/formatted-date-column.PNG)
_Les dates dans un format plus lisible_

Pour les besoins de cette analyse, nous devons extraire les années des dates que nous venons de formater. Pour ce faire, créez une nouvelle colonne à côté de la colonne D, ce sera votre nouvelle colonne E. Nommez la colonne comme vous le souhaitez, mais dans mon cas, je l'ai nommée « Année ».

Utilisez maintenant la formule dans la capture d'écran ci-dessous et appuyez sur Entrée :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/getting-the-year.PNG)
_Formule pour obtenir l'année à partir de la date_

Ou copiez et collez simplement la formule ci-dessous :

=DROITE(D2;4)

Cela extraira l'année à la fin de la date. Double-cliquez sur le nœud à la fin de la cellule pour répéter cela dans toute la colonne. Vous devriez obtenir un résultat similaire à celui montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/The-year.PNG)
_Capture d'écran montrant l'année extraite_

## Comment trier l'ensemble des données

L'étape suivante de ce tutoriel consiste à trier l'ensemble des données en fonction de la colonne Année nouvellement extraite.

Mettez en surbrillance toute la colonne Année et allez dans l'onglet de tri, comme vous pouvez le voir dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/The-sort-tab.PNG)
_Tri de l'ensemble de données_

Laissez toutes les options par défaut et appuyez sur OK.

Maintenant, l'ensemble des données devrait être trié.

## Comment créer plusieurs tableaux croisés dynamiques sur la même feuille de calcul

L'étape suivante de ce tutoriel consiste à créer les tableaux croisés dynamiques que nous utiliserons pour donner un sens à ces données.

Allez dans l'onglet Insertion et cliquez sur Tableau croisé dynamique. Une boîte de dialogue devrait s'ouvrir vous demandant la plage des données à partir desquelles vous souhaitez créer le tableau croisé dynamique – qui par défaut est l'ensemble des données.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/pivot-table-creation.PNG)
_Création d'un tableau croisé dynamique_

Vous aurez également des options pour utiliser la feuille de calcul existante pour créer le tableau croisé dynamique ou une nouvelle feuille de calcul. Sélectionnez l'option _nouvelle feuille de calcul_ et appuyez sur OK.

Vous devriez avoir un résultat comme vous pouvez le voir dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/pivot-table-worksheet.PNG)
_La feuille de calcul du tableau croisé dynamique_

À partir de là, les choses commencent à devenir intéressantes.

Pour cet exercice, je ne m'intéresse qu'à trois choses : 

* La catégorie de produits avec les ventes les plus élevées pour chacune des quatre années (2014 à 2017)
* Quelle sous-catégorie a les ventes les plus élevées
* Quelle région génère le plus de ventes pour ce supermarché.

Je souhaite également visualiser ces informations à l'aide de graphiques et de tableaux. Heureusement, Excel dispose des outils dont nous avons besoin pour atteindre tous ces objectifs.

Au cas où vous ne sauriez pas comment créer un tableau croisé dynamique, voici un article complet de [freeCodeCamp](https://www.freecodecamp.org/news/how-to-create-a-pivot-table-in-excel/) qui vous apprend à le faire.

Nous devons donc créer trois tableaux croisés dynamiques, un pour les ventes par catégorie, un pour les ventes par sous-catégorie, et un pour les ventes par région.

Pour créer le premier tableau, sélectionnez simplement les ventes et la catégorie dans les champs du tableau croisé dynamique du côté droit de votre écran.

Après avoir créé le premier tableau croisé dynamique, pour ajouter un autre tableau sur la même feuille de calcul, allez simplement dans l'onglet Insertion et cliquez sur Tableau croisé dynamique, puis allez dans la feuille de calcul originale avec l'ensemble de données et mettez tout en surbrillance, cliquez sur OK.

Répétez l'étape pour créer le dernier tableau pour les ventes par région.

Vous devriez avoir trois tableaux comme montré dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/All-pivot-tables-1.PNG)
_Capture d'écran montrant les trois tableaux croisés dynamiques_

## Comment créer des graphiques basés sur le tableau croisé dynamique

L'étape suivante consiste à créer les graphiques pour visualiser ce qui est représenté dans les tableaux croisés dynamiques. Cela est assez simple – il suffit de mettre en surbrillance chaque tableau et de cliquer sur l'onglet Insertion pour insérer le graphique de votre choix.

J'ai utilisé un graphique en secteurs pour le tableau des ventes par catégorie, et des graphiques en colonnes pour les deux autres tableaux de la feuille de calcul. Mais vous pouvez utiliser le ou les graphiques que vous souhaitez.

Si vous suivez mes étapes exactement, vous devriez obtenir un résultat similaire à la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/All-charts-and-tables.PNG)
_Capture d'écran montrant tous les graphiques_

## Comment créer des segments pour filtrer les données

L'étape suivante consiste à utiliser des segments pour filtrer chaque tableau par année afin que nous puissions voir quelles sont les ventes totales pour chaque catégorie, sous-catégorie et région par année.

Pour ce faire, mettez en surbrillance chaque tableau et cliquez sur l'onglet Analyser, puis cliquez sur le bouton Segment comme montré dans cette capture d'écran :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/insert-slicer.PNG)
_Création d'un segment_

Vous verrez une liste d'options. Cherchez Année, et cliquez dessus.

Maintenant, vous devriez avoir un segment pour les années 2014 à 2017. En cliquant sur le bouton correspondant pour chaque année, vous filtrerez le tableau et afficherez les ventes pour cette année. Voici à quoi cela devrait ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/All-charts-with-slicers.PNG)
_Capture d'écran montrant tous les segments_

## Comment utiliser la mise en forme conditionnelle

Enfin, vous pouvez utiliser la mise en forme conditionnelle pour indiquer les valeurs les plus élevées et les plus basses de chaque tableau. Vous pouvez jouer avec cela comme vous le souhaitez.

Pour utiliser la mise en forme conditionnelle, cliquez sur l'onglet Mise en forme conditionnelle, et utilisez cette capture d'écran comme guide :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/conditional-formatting.PNG)
_Utilisation de la mise en forme conditionnelle_

Mettez en surbrillance les valeurs pour lesquelles vous souhaitez utiliser la mise en forme conditionnelle. J'ai utilisé l'option d'échelles de couleurs pour indiquer les valeurs les plus élevées et les plus basses par différentes couleurs, puis j'ai utilisé l'option de barres de données pour le tableau des ventes par sous-catégorie.

Si vous avez fait exactement ce que j'ai fait, vous devriez avoir quelque chose de proche de la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/all-charts-with-conditional-formatting.PNG)
_Le tableau de bord terminé_

## Conclusion

Ce petit projet que nous avons construit ensemble peut être étendu pour obtenir plus d'informations sur l'ensemble de données, ce qui peut s'avérer très utile lors de la prise de décisions commerciales. 

Ce tableau de bord que nous avons construit a révélé que la catégorie la plus vendue est l'électronique et la sous-catégorie la plus vendue est les téléphones. J'ai également appris que la plupart des ventes provenaient de la région ouest simplement en regardant ce tableau de bord.

J'espère que ce tutoriel a été utile. Voici [le lien](https://github.com/Lordsamdev/superstoredata/blob/main/Super%20Store%20Tutorial.xlsx) vers la version terminée de ce projet – vous pouvez la comparer avec ce que vous avez construit et voir comment vous vous en êtes sorti.

Si vous avez des questions, vous pouvez me contacter sur [X](https://twitter.com/thelordsamdev) et [LinkedIn](https://www.linkedin.com/in/lordsamdev/). Merci d'avoir lu.