---
title: Comment créer des fonctions nommées personnalisées dans Google Sheets
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-03-13T17:56:24.000Z'
originalURL: https://freecodecamp.org/news/google-sheets-how-to-create-custom-named-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/fCC-thumbp.jpg
tags:
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment créer des fonctions nommées personnalisées dans Google Sheets
seo_desc: "There are 513 built-in functions in Google Sheets at the time of this writing.\
  \ But what if you needed a custom function that wasn't included? \nIn this tutorial,\
  \ I'll show you how to create and use your own custom function in Google Sheets.\n\
  Why would ..."
---

Au moment où j'écris ces lignes, il existe 513 fonctions intégrées dans Google Sheets. Mais que faire si vous aviez besoin d'une fonction personnalisée qui n'est pas incluse ?

Dans ce tutoriel, je vais vous montrer comment créer et utiliser votre propre fonction personnalisée dans Google Sheets.

Pourquoi auriez-vous besoin d'une fonction personnalisée ? Il peut y avoir de nombreuses raisons. Cela peut minimiser la saisie si vous avez de nombreux cas où vous devez calculer certains éléments. Cela peut simplifier un agencement autrement complexe de formules saisies manuellement. Vous pourriez simplement vouloir montrer vos talents sur les feuilles de calcul.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/custom.gif)
_gif d'une femme disant "c'est personnalisé"_

Je vais détailler un exemple simple ci-dessous où nous trouvons la variation en pourcentage entre deux nombres. J'ai écrit abondamment sur 5 façons de réaliser cet exercice particulier dans un autre article [ici](https://www.freecodecamp.org/news/how-to-calculate-percentage-differences-between-two-numbers-in-excel-cell-percentage-change-tutorial/).

## Exemple de variation en pourcentage

Tout d'abord, voici une démonstration vidéo de la création de fonctions nommées personnalisées si vous souhaitez voir une démonstration en direct.

[Voici la feuille de calcul de démonstration](https://docs.google.com/spreadsheets/d/1pubmIp-4VmcHpQJXibxU1Astl6lgH2qZEN3Ry1S7i6Q/edit#gid=337119202).

%[https://youtu.be/UmzAdZnVRy0]

Pour trouver la variation en pourcentage entre deux nombres, nous devons effectuer un calcul simple en divisant la différence entre eux par le premier nombre.

Si nous avons le tableau de données de ventes suivant dans les colonnes E, F et G, nous pouvons trouver la variation en pourcentage entre les années 1 et 2 en écrivant manuellement la formule `(F7-E7)/E7`. Et de la même manière pour les années 2 à 3 en écrivant `(G7-F7)/F7`.

<table><tbody><tr><td>année 1 </td><td>année 2</td><td>                  année 3</td></tr><tr><td>180 000,00 $</td><td>200 088,00 $</td><td>340 000,00 $</td></tr><tr><td>180 000,00 $</td><td>200 088,00 $</td><td>340 000,00 $</td></tr></tbody></table>

C'est très bien. Mais Google Sheets permet d'utiliser des fonctions personnalisées que nous pouvons définir une seule fois, puis utiliser sans avoir à taper autant manuellement. Pour cet exemple, c'est assez simple, mais pour des formules plus complexes, cela peut faire gagner beaucoup de temps et éviter des erreurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-97.png)
_Capture d'écran de Google Sheets_

## Comment créer une fonction nommée personnalisée

Pour accéder aux fonctions nommées, cliquez sur `Données, Fonctions nommées` dans la barre d'outils.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.51.03-PM.png)
_capture d'écran du menu données et de l'option fonctions nommées_

Sélectionnez `Ajouter une nouvelle fonction` en bas :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.52.24-PM.png)
_Capture d'écran de l'ajout d'une nouvelle fonction_

Et à partir de là, nous pouvons remplir les détails de notre nouvelle fonction en commençant par le nom et la description :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.53.03-PM-1.png)
_Capture d'écran du nom de la fonction nommée_

Ensuite, nous avons des espaces réservés d'arguments optionnels. Pour notre fonction, nous en avons besoin de deux : un pour chaque année.

Ensuite, nous remplissons la définition réelle de la formule. C'est ici que nous décrivons ce que nous voulons que la formule fasse. Nous utilisons les espaces réservés d'arguments comme des variables au lieu des références de cellules spécifiques :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.53.14-PM.png)
_capture d'écran des arguments et de la définition de la formule_

Et dans le dernier menu, nous pouvons ajouter des détails supplémentaires décrivant et donnant des exemples de nos arguments. Cela peut être aussi détaillé ou succinct que nécessaire. Dans notre cas, je n'ai rempli que le strict minimum :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.53.34-PM.png)
_Capture d'écran des détails de l'argument dans la fonction nommée personnalisée_

Regardez ça ! Nous avons maintenant une fonction nommée personnalisée opérationnelle pour trouver la variation en pourcentage entre deux nombres. Au lieu de devoir saisir toute la formule, il nous suffit maintenant de saisir les cellules pour `annee1` et `annee2` :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-8.16.52-PM.png)
_Capture d'écran de la fonction nommée personnalisée_

## Résumé

Les fonctions intégrées de Google Sheets peuvent vous mener loin, mais si jamais vous avez besoin de définir votre propre fonction unique, vous le pouvez désormais.

J'espère que cela vous a été utile !

N'hésitez pas à consulter ma [chaîne YouTube ici](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) et ma [page LinkedIn ici](https://www.linkedin.com/in/eamonncottrell/).

Passez une excellente journée !