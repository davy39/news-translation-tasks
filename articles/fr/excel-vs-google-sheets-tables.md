---
title: Comment travailler avec les tableaux dans Excel vs Google Sheets
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2024-07-02T17:27:11.000Z'
originalURL: https://freecodecamp.org/news/excel-vs-google-sheets-tables
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/4.jpg
tags:
- name: excel
  slug: excel
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment travailler avec les tableaux dans Excel vs Google Sheets
seo_desc: 'Google Sheets recently released an all new feature: tables.

  Well, new is a bit of an overstatement. Excel has had proper tables for many, many
  years, and it''s been a point of contention in the spreadsheet community.

  In this article, I''ll break down w...'
---

Google Sheets a récemment lancé une toute nouvelle fonctionnalité : les tableaux.

Eh bien, _nouveau_ est un peu exagéré. Excel dispose de vrais tableaux depuis de nombreuses années, et cela a été un point de discorde dans la communauté des tableurs.

Dans cet article, je vais décomposer ce que sont exactement les tableaux, pourquoi ils sont importants, puis voir comment les nouveaux tableaux de Google Sheets se comparent à ceux de Microsoft Excel.

Voici une vidéo qui couvre tout ce que nous allons aborder :

%[https://youtu.be/vBp5mveYZZ4]

## Qu'est-ce qu'un tableau ?

Un tableau est une manière de structurer et de formater des données dans une feuille de calcul. Il regroupe des lignes et des colonnes de données afin qu'elles puissent être plus facilement filtrées, groupées et analysées.

Beaucoup de gens regarderaient les données suivantes et penseraient à tort qu'elles sont déjà dans un tableau.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-103.png)
_Données dans Excel_

Ce ne sont que des lignes et des colonnes bien organisées dans Excel. Chaque colonne est une catégorie distincte d'informations, à savoir les identifiants, les noms, les emails, les titres de poste et les salaires.

Chaque ligne représente une entrée de ces données. Ainsi, vous placerez votre identifiant, votre nom, votre email, votre titre de poste et votre salaire de gauche à droite dans une ligne.

Simple, n'est-ce pas ?

Un tableau contient toutes les mêmes données, mais en le formatant comme un tableau, nous pouvons débloquer beaucoup de fonctionnalités supplémentaires.

La première est l'apparence elle-même. Lorsque nous créons un tableau, Excel colore immédiatement nos données avec une ligne d'en-tête sombre et des bandes de couleurs alternées.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-104.png)
_Tableau dans Excel_

Sheets fait de même, comme nous pouvons le voir ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-105.png)
_Tableau dans Google Sheets_

Ainsi, un tableau est simplement une manière de gérer et de regrouper des données plus facilement. Mais cela va bien au-delà du simple formatage, comme nous allons le voir.

## Pourquoi les tableaux sont-ils importants ?

Les tableaux aident à réduire les erreurs. Lorsque nous traitons des données, nous veillons toujours à ce que les données soient propres et à ce que nous n'ayons pas d'erreurs dans nos formules.

Les tableaux aident à garder les choses en ordre simplement en étant structurés et bien formatés. Mais comme nous allons le voir dans la section sur les formules dans un instant, ils nous permettent également de réduire les erreurs dans les formules en calculant dynamiquement les choses pour nous.

## Comment créer un tableau dans Excel et Sheets

Dans Microsoft Excel, créer un tableau est aussi simple que de cliquer n'importe où dans la plage de données et d'appuyer sur `CTRL + T`. Immédiatement, Excel prédira la plage de données pour le tableau et vous demandera de confirmer cela.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-106.png)
_Plage de données du tableau Excel_

Alternativement, vous pouvez trouver la même option de création de tableau dans le menu Insertion dans le Ruban en haut.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/table.png)
_Menu d'insertion Excel_

Dans Sheets, vous devrez soit faire un clic droit dans une cellule de la plage de données, soit sélectionner l'option dans le menu Format pour Convertir en tableau.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sheets.png)
_Options de conversion en tableau dans Google Sheets_

Un avertissement dans Sheets : si vous faites un clic droit dans une cellule, vous devez sélectionner toute la plage de données pour qu'elle soit convertie en tableau. Alors que si vous sélectionnez Format - Convertir en tableau depuis le menu, il est (comme Excel) assez intelligent pour prédire toute la plage de données.

Une petite chose. Mais Excel remporte le prix pour la facilité de création.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/right-click.png)
_Convertir en tableau dans Google Sheets_

**🔅Gagnant : EXCEL**

## Comment formater les tableaux dans Excel et Sheets

Comme nous l'avons vu initialement, un certain formatage est effectué dès que nous créons un tableau.

À partir de là, cependant, les deux programmes permettent une personnalisation supplémentaire.

Dans Sheets, nous pouvons sélectionner la liste déroulante en haut à gauche à côté du nom du tableau pour accéder à quelques options immédiatement. Pour la plupart, nous pouvons simplement changer les couleurs alternées du tableau.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sheets-format.png)
_Options de formatage dans Google Sheets_

Si nous sélectionnons Personnalisé, cela ouvre le menu complet des couleurs alternées qui est également accessible via le menu Format. Cela nous donne plus de contrôle sur les couleurs, mais c'est tout esthétique.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-110.png)
_Menu des couleurs alternées dans Google Sheets_

Pendant ce temps, dans Excel, nous avons les mêmes options avec quelques sélections de bascule supplémentaires pour le style. Par exemple, nous pouvons cocher la première colonne pour mettre en gras le texte dans la colonne des identifiants ou nous basculer entre les colonnes et/ou les lignes en bandes.

Et à l'extrême droite de l'onglet Conception de tableau dans le Ruban, il y a une tonne de styles préconstruits que nous pouvons activer et désactiver.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/format-excel.png)
_Conception de tableau dans Excel_

Les deux programmes offrent de nombreuses options ici, et cela sert principalement à rendre les tableaux esthétiques. Mais Excel se distingue avec plus d'options.

**🔅Gagnant : EXCEL**

## Comment trier les tableaux dans Excel et Google Sheets

Dans les deux programmes, il y a un bouton de bascule déroulant dans chacune des cellules de la ligne d'en-tête. Sélectionner cela dans Excel nous permet de trier par ordre croissant ou décroissant... ou même par couleur.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sort.png)
_Tri dans Excel_

Par exemple, si certaines de nos données utilisent une couleur de police bleue, nous pouvons effectivement les trier par cette couleur :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sort-color.png)
_Tri par couleur dans Excel_

Et Google Sheets ? Oui, même chose. Il détectera également lorsque différentes couleurs sont utilisées et vous permettra de faire le même type de tri.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/sheets-sorting-options-1.png)
_Tri par couleur dans Sheets_

Excel dispose d'une boîte de dialogue de tri personnalisé qui peut approfondir davantage. Par exemple, vous pouvez ajouter des niveaux de tri.

En utilisant notre exemple de couleur, nous pouvons d'abord trier par les couleurs de police bleue dans la couleur de l'email, puis par les couleurs de police rouge dans la colonne du titre de poste.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/double-sort.png)
_Tri multi-colonnes dans Excel_

Google Sheets peut faire la même chose, mais pas depuis les listes déroulantes d'en-tête. Le tri par liste déroulante d'en-tête est limité à une ligne à la fois dans Sheets.

Mais, si vous sélectionnez toute la plage de données du tableau, puis `Données - Plage de tri - Options de tri de plage avancées`, vous pouvez trier par plusieurs colonnes dans Google Sheets.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/advanced-sort-google-sheets.png)
_Tri avancé dans Google Sheets_

Le tri avancé de Sheets n'est pas aussi puissant que celui d'Excel, cependant. Vous ne pouvez trier que par ordre croissant ou décroissant par valeur. Excel remporte la palme sur ce point de justesse.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/google-sheets-muiltiple-row-sorting.png)

**🔅Gagnant : EXCEL**

## Comment filtrer les tableaux dans Excel et Google Sheets

Le filtrage fonctionne exactement de la même manière que le tri. Dans les deux programmes, cliquez sur le sélecteur déroulant dans la ligne d'en-tête pour voir les options de filtrage.

Dans les deux programmes, nous avons les mêmes options. Nous pouvons filtrer par couleur comme dans notre tri. Nous pouvons filtrer par valeurs en sélectionnant toutes, aucune ou des valeurs individuelles. Et nous pouvons filtrer par condition.

Voici le menu de Google Sheets :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-113.png)
_Filtrage dans Google Sheets_

Et voici le menu d'Excel. Toutes les mêmes options sont disponibles. Les deux programmes permettent également de saisir des formules de filtre personnalisées.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-112.png)
_Filtrage dans Excel_

**🔅Gagnant : ÉGALITÉ**

## Comment utiliser les tableaux dans les formules dans Excel et Google Sheets

L'une des principales raisons d'utiliser des tableaux réside dans les formules. Que vous utilisiez Excel ou Sheets, vous tirez probablement parti des fonctions intégrées et de la possibilité de créer des formules personnalisées pour analyser vos données.

En plaçant vos données dans un tableau, vos formules peuvent référencer ces données dynamiquement.

Cela signifie que si vous ajoutez des lignes de données à votre tableau, toutes les formules référençant ces valeurs de tableau seront mises à jour automatiquement.

Le risque de casser des choses en ajoutant des données diminue considérablement avec l'utilisation de tableaux.

Voici un exemple simple. Si nous voulions combiner les prénoms et les noms de famille dans une seule cellule, nous pourrions les concaténer avec cette formule `=Salaire[prenom]&" "&Salaire[nom]`.

Dans Excel, nous référençons un tableau par son nom, dans ce cas, `Salaire`. Ensuite, entre crochets, nous référençons un nom de colonne, `[nom]`.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-115.png)
_Formule de déversement dans Excel_

Nous pouvons faire exactement la même chose dans Sheets.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-116.png)
_Référencement de formule dans Sheets_

Il y a une différence puissante, cependant. Dans Excel, la formule se déversera vers le bas. Cela signifie que nous n'avons à l'écrire qu'une seule fois tout en haut, mais parce qu'il voit que nous référençons des valeurs dans un tableau, il se déversera vers chaque ligne du tableau.

Dans Google Sheets, nous devons toujours faire glisser la formule vers le bas.

Parfois, nous ne voulons peut-être pas que les choses se déversent vers le bas. Dans ce cas, nous pouvons utiliser une syntaxe différente dans Excel. Au lieu du nom de la colonne entre crochets, nous pouvons ajouter un signe @ et un autre ensemble de crochets. Cela indique à Excel de ne faire le calcul que sur une ligne :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-117.png)
_Référencement de formule dans Excel_

Excel se distingue sur ce point. Il est beaucoup plus puissant d'utiliser des tableaux dans les formules dans Excel que dans Sheets.

**🔅Gagnant : EXCEL**

## Comment changer la plage de tableau dans Excel et Google Sheets

Que faire si nous voulons étendre notre tableau ou en supprimer des données ? Google Sheets et Excel nous permettent de le faire facilement.

Supposons que nous voulons ajouter une colonne pour le nom complet d'une personne. Dans les deux programmes, si nous tapons simplement `nom_complet` dans G1 à droite de notre dernière colonne, cette colonne fera partie de la plage de données du tableau.

Chaque fois que nous tapons dans une colonne ou une ligne adjacente à nos données de tableau, les programmes supposeront que le tableau doit s'étendre pour l'inclure.

Ensuite, nous pouvons utiliser une version de la formule de notre exemple précédent pour insérer les noms complets. Maintenant que nous sommes à l'intérieur du tableau, cependant, il n'est pas nécessaire d'inclure le titre du tableau dans notre formule.

Maintenant, tout ce qui est nécessaire dans Excel est `=[@[prenom]]&" "&[@[nom]]`.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-119.png)
_Référencer les colonnes de tableau dans Excel_

Pour Google Sheets, c'est la même chose à l'intérieur du tableau qu'à l'extérieur : `=Tableau2[prenom]&" "&Tableau2[nom]`. Sheets nécessite également que nous fassions glisser la formule vers le bas. Il ne gère pas le déversement comme Excel (pour l'instant).

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-118.png)
_Référencer les colonnes de tableau dans Sheets_

Pour ajouter des colonnes dans un tableau, nous pouvons faire un clic droit sur le nom de la colonne et sélectionner insérer.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-120.png)
_Insérer une colonne dans Excel_

Google a un léger avantage ici en ce sens que vous pouvez choisir d'insérer à gauche ou à droite, alors qu'Excel n'insère qu'à gauche.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-121.png)
_Insérer une colonne dans Google Sheets_

L'insertion de lignes est exactement la même. Excel permet d'insérer des lignes au-dessus, tandis que Sheets vous permet de sélectionner au-dessus ou en dessous.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-122.png)
_Insertion de lignes dans Google Sheets_

Dans les deux programmes, la suppression de lignes et de colonnes est aussi simple que de sélectionner la ou les lignes ou colonnes, de faire un clic droit et de sélectionner supprimer.

Dans Excel, vous avez l'avantage supplémentaire d'un raccourci clavier. `CTRL + -` supprimera les lignes ou colonnes sélectionnées.

Les deux programmes vous permettront également de convertir un tableau en une plage de données régulière. Dans Excel, c'est le bouton `Convertir en plage` dans l'onglet `Conception de tableau` du menu.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/convert.png)
_Option Convertir en plage dans Excel_

Et dans Google Sheets, c'est l'option `Revenir aux données non formatées` dans le menu déroulant du tableau.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/revert.png)
_Option Revenir aux données non formatées dans Sheets_

**🔅Gagnant : ÉGALITÉ**

## Comment ajouter une ligne de total dans un tableau

Il y a de fortes chances que vous souhaitiez totaliser les montants dans une colonne. À quel point est-ce facile à ajouter dans un tableau ?

Vous pouvez le faire dans les deux programmes, mais...

Excel le rend incroyablement facile. Il y a une option de bascule pour cela dans le menu Conception de tableau dans le Ruban. Activez cette option, et une ligne de total est automatiquement incluse et calculée en bas.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/total-row.png)
_Ligne de total dans Excel_

Pouvez-vous faire de même dans Sheets ?

Oui, vous devez simplement le faire vous-même.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-124.png)
_Ligne de total dans Sheets_

**🔅Gagnant : EXCEL**

## Qui gagne ?

Eh bien, il n'est pas surprenant qu'Excel sorte vainqueur. Les utilisateurs de Sheets (moi y compris) ont beaucoup de raisons d'être enthousiastes avec la possibilité de enfin créer des tableaux appropriés. Dans l'ensemble, la fonctionnalité est tout aussi puissante qu'Excel.

Et comme pour de nombreuses fonctionnalités comparées entre les deux programmes, Sheets peut probablement faire le travail pour la plupart des cas d'utilisation.

Excel, comme d'habitude, fait simplement plus et un peu mieux.

Je suis Eamonn, et je vais vous aider à **devenir bon avec les tableurs**. Rejoignez ma newsletter gratuite, [Got Sheet, ici](https://www.gotsheet.xyz/subscribe).