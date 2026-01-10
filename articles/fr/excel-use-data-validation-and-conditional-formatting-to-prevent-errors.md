---
title: Microsoft Excel – Comment utiliser la validation des données et la mise en
  forme conditionnelle pour prévenir les erreurs
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-03-06T16:41:05.000Z'
originalURL: https://freecodecamp.org/news/excel-use-data-validation-and-conditional-formatting-to-prevent-errors
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/fcc.jpg
tags:
- name: error
  slug: error
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: Microsoft Excel – Comment utiliser la validation des données et la mise
  en forme conditionnelle pour prévenir les erreurs
seo_desc: 'I''ve been using Microsoft Excel and Google Sheets in my business for over
  a decade. And as I''ve learned better ways to clean and validate data, it''s increased
  productivity, decreased human errors, and generally caused a lot of joy! 🥳

  In this article...'
---

J'utilise Microsoft Excel et Google Sheets dans mon entreprise depuis plus d'une décennie. Et à mesure que j'ai appris de meilleures façons de nettoyer et de valider les données, cela a augmenté la productivité, diminué les erreurs humaines et généralement causé beaucoup de joie ! 🥳

Dans cet article, nous examinerons deux façons de valider et/ou d'appliquer une mise en forme conditionnelle à un formulaire de commande exemple pour prévenir les erreurs et accélérer la préparation des commandes.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/no-error.gif)
_gif d'un homme disant, "il n'y a pas de place pour l'erreur"_

Vous pouvez trouver la feuille Excel que nous utilisons pour ce tutoriel [ici](https://onedrive.live.com/edit.aspx?resid=FE6EDAF51E9AF322!1141&ithint=file%2Cxlsx&authkey=!ANRcKMn_p25YVyo). 

Vous pouvez télécharger une copie locale pour l'explorer en sélectionnant `Fichier, Enregistrer sous, Télécharger une copie` :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-21.png)
_Télécharger une copie du classeur Excel_

Vous pouvez trouver une version Google Sheets de la même chose [ici](https://docs.google.com/spreadsheets/d/1gnacOaU_TCX_I7wGxHWWriyej4kI7t9AzM_nLybv9Cs/edit?usp=sharing).

Vous pouvez télécharger ou faire une copie en ligne en sélectionnant `Fichier, Télécharger` ou `Fichier, Faire une copie`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-22.png)
_Télécharger ou faire une copie de la feuille Google Sheet_

Je vais discuter de la version Excel à partir de maintenant, en faisant référence lorsque quelque chose diffère dans Google Sheets.

## Vidéo explicative

Oh, et voici une vidéo explicative agréable si vous en avez envie. 😁😁

%[https://youtu.be/vMyBjyHGQ-U]

## Installation

J'ai créé un formulaire de commande à trois colonnes où un magasin peut inventorier ses produits et entrer une quantité à commander. La troisième colonne est utilisée par l'entrepôt pour entrer combien ont été réellement livrés. Il s'agit d'une configuration réelle que nous utiliserons sous une forme simplifiée pour ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-23.png)
_Formulaire de commande exemple dans Excel_

Il peut être difficile pour la préparation des commandes s'il y a des zéros saisis dans la colonne de commande. Au lieu de permettre cela, nous allons utiliser quelques outils pour montrer comment contrôler les valeurs dans une cellule. Peu importe à quel point les instructions sont claires, quelqu'un oubliera toujours et saisira un zéro.

## Mise en forme conditionnelle

En appliquant une mise en forme conditionnelle, nous pouvons effectivement masquer les cellules qui contiennent des zéros (ou toute valeur négative).

À partir du ruban Accueil dans Excel et du menu Format dans Google Sheets, sélectionnez `Mise en forme conditionnelle`. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/conditional-on-classic-ribbon.png)

Si vous ne voyez pas la mise en forme conditionnelle comme une option, elle se trouvera dans le menu déroulant des styles ou à l'extrême droite dans un menu déroulant à trois points, selon que vous avez le style classique ou le nouveau style de ruban affiché.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/differnt-ribbon.png)
_Menu de mise en forme conditionnelle dans les rubans Excel_

Si vous souhaitez changer la disposition de votre ruban, sélectionnez cette flèche déroulante à l'extrême droite du ruban :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/ribbon.png)
_Changer la disposition du ruban Excel_

Une fois que vous êtes dans le menu de format conditionnel, cliquez sur `Gérer les règles`. Cela vous permettra de spécifier le formatage en fonction d'une multitude d'options. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/manage-rules.png)
_Gérer les règles de mise en forme conditionnelle dans Excel_

C'est là que Microsoft Excel a un avantage sur Google Sheets. Excel a plus d'options disposées de manière plus intuitive. Vous pouvez faire les mêmes choses dans chaque programme, mais Excel a organisé les siennes un peu mieux à mon avis.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-26.png)
_Organisation du menu de mise en forme conditionnelle dans Excel_

Nous allons sélectionner la colonne Commande comme notre plage, puis mettre en surbrillance les cellules avec des valeurs de cellule inférieures ou égales à zéro. 

À d'autres moments, vous utiliserez la mise en forme conditionnelle pour faire de la visualisation de données en utilisant des couleurs et des échelles de couleurs, mais dans notre cas, nous voulons masquer la valeur zéro. 

Pour ce faire, j'ai simplement sélectionné une couleur de remplissage blanche et une couleur de texte blanche. 🤔

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-25.png)
_Menu de mise en forme conditionnelle_

Et maintenant, voilà ! Si un montant de zéro est saisi, il sera simplement masqué pour ne pas distraire du centre de préparation des commandes :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/zero.png)
_Valeur zéro saisie et mise en forme conditionnelle appliquée_

## Validation des données

La deuxième option à notre disposition est la validation des données. Vous pouvez trouver cela dans l'onglet données du ruban, et si vous ne le voyez pas, vous pouvez le trouver en explorant les mêmes options de ruban que j'ai détaillées ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/validation-1.png)
_Menu de validation des données dans le ruban_

Cela nous donnera une multitude d'options à sélectionner pour valider les données entrant dans une plage spécifiée. Il y a de nombreuses options à choisir pour nos données.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-30.png)

Dans notre cas, nous voulons nous assurer qu'ils sont des nombres entiers supérieurs à zéro. Un peu l'inverse de la mise en forme conditionnelle que nous avons faite ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-29.png)
_Validation des données_

Une autre fonctionnalité Excel agréable qui manque au moment de la rédaction de cet article dans Google Sheets est la possibilité de mettre un message d'entrée dans la validation des données.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-31.png)
_Message d'entrée dans la validation des données_

Maintenant, chaque fois que vous êtes sur une cellule dans la plage de validation des données, une boîte amicale apparaîtra avec des instructions vous rappelant de ne pas commander une quantité de zéro. 😀

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-32.png)
_Exemple de texte d'entrée dans la feuille de calcul_

La validation des données dans Excel bloque par défaut toute entrée qui ne respecte pas les conditions définies. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-33.png)

Ainsi, vous recevrez une fenêtre contextuelle disgraciée vous empêchant de saisir un zéro.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-34.png)
_avertissement de validation des données_

Nous pouvons améliorer cela en définissant un message personnalisé ici aussi, cependant. Et nous pouvons choisir de le bloquer complètement ou de permettre à un zéro d'être saisi après l'apparition de l'avertissement. Permettant effectivement à l'avertissement d'être ignoré dans le cas où il y a une raison de le faire.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-35.png)
_message d'avertissement personnalisé de validation des données_

Et enfin, nous pouvons coupler l'une de ces options avec notre mise en forme conditionnelle afin que si nous ne faisons qu'avertir contre l'entrée, nous la masquons toujours avec le texte blanc et la couleur de remplissage blanche.

La [feuille Excel](https://onedrive.live.com/edit.aspx?resid=FE6EDAF51E9AF322!1141&ithint=file%2cxlsx&authkey=!ANRcKMn_p25YVyo) et la [feuille Google](https://docs.google.com/spreadsheets/d/1gnacOaU_TCX_I7wGxHWWriyej4kI7t9AzM_nLybv9Cs/edit#gid=1341856047) accompagnantes contiennent quatre colonnes de chacun des exemples ci-dessus pour que vous puissiez les voir en action.

J'espère que cela vous a été utile ! 

Venez voir mes [tutoriels vidéo sur YouTube](https://www.youtube.com/@eamonncottrell?sub_confirmation=1). J'apprécierais un like et un abonnement car je développe ma chaîne d'éducation technologique là-bas !

Passez une excellente journée !