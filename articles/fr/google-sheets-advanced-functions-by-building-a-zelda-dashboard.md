---
title: Google Sheets – Apprendre les fonctions avancées en créant un tableau de bord
  Zelda
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-04-13T17:31:52.000Z'
originalURL: https://freecodecamp.org/news/google-sheets-advanced-functions-by-building-a-zelda-dashboard
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Zelda-Walkthrough.jpg
tags:
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Google Sheets – Apprendre les fonctions avancées en créant un tableau de
  bord Zelda
seo_desc: "In this article we'll build a dashboard inspired by the recipes in Zelda:\
  \ Breath of the Wild. \nOur dashboard will have multiple data validation dropdown\
  \ selections for us to choose ingredients. By using a =Query() function, we'll then\
  \ display the rec..."
---

Dans cet article, nous allons créer un tableau de bord inspiré des recettes de Zelda : Breath of the Wild. 

Notre tableau de bord aura plusieurs sélections de menus déroulants de validation de données pour choisir les ingrédients. En utilisant une fonction `=Query()`, nous afficherons ensuite les recettes qui contiennent toute combinaison des ingrédients sélectionnés.

C'est parti !

![Image](https://www.freecodecamp.org/news/content/images/2023/04/letsgo.gif)
_gif d'un homme disant, "c'est parti !"_

## Produit final

Voici à quoi ressemblera le tableau de bord terminé. Ce n'est pas trop compliqué, et les outils et techniques que nous utiliserons pour obtenir les données, les nettoyer et les afficher dynamiquement sont assez précieux.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-7.28.35-PM.png)
_photo du tableau de bord Zelda_

**[Voici le code source de la feuille Google](https://docs.google.com/spreadsheets/d/1S_oWlUdbMCEm5B12oYoUDvdMwKLZ5oFr4XqxQ_9rVo4/edit?usp=sharing).** Ouvrez-le pour suivre et vérifier certains codes au fur et à mesure que vous lisez l'article.

Vous pouvez en faire une copie modifiable en sélectionnant `Fichier -> Créer une copie`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-7.36.29-PM.png)

### Vidéo de démonstration

Si vous souhaitez voir une vidéo de moi construisant cela à partir de zéro, voici une vidéo en accéléré de 14 minutes avec moi narrant les étapes :

%[https://youtu.be/EUBpyTiaCV0]

## Installation du projet

La première chose dont nous avons besoin est des données. Dans notre cas, nous allons utiliser la fonction `IMPORTHTML()` pour obtenir des données à partir d'IGN. `IMPORTHTML()` nous permet de référencer une URL, de spécifier si nous recherchons des "tables" ou des "listes" dans l'URL, puis, en fournissant un numéro d'index, d'importer la table ou la liste à partir de l'URL.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-129.png)
_capture d'écran de la documentation importhtml_

IGN a un livre de recettes pratique [ici](https://www.ign.com/wikis/the-legend-of-zelda-breath-of-the-wild/All_Recipes_and_Cookbook).

Nous placerons l'URL dans une cellule de notre feuille Google car, après avoir inspecté la page, nous voyons que les recettes sont contenues dans plusieurs tables, nous devrons donc utiliser plusieurs instructions d'importation.

J'ai mis l'URL dans `D3` et nous sommes prêts à importer toutes les tables. Pour le faire en une seule fois, nous pouvons utiliser des accolades. Dans Google Sheets, les accolades créent des tableaux.

En enveloppant plusieurs instructions `IMPORTHTML()` dans des accolades, nous créons un tableau de toutes ces importations. En guise de touche finale, nous pouvons envelopper le tout dans une fonction `UNIQUE()` pour nous assurer qu'aucune recette en double (ou dans notre cas, en-têtes de table) ne soit transférée dans notre onglet de données.

Voici le code :

```google sheets
=UNIQUE({IMPORTHTML(D3,"table",3);
IMPORTHTML(D3,"table",4);
IMPORTHTML(D3,"table",5);
IMPORTHTML(D3,"table",6);
IMPORTHTML(D3,"table",7);
IMPORTHTML(D3,"table",8);
IMPORTHTML(D3,"table",9)})
```

Cela nous donne les données, mais nous devons les nettoyer. Plus précisément, nous devons nous débarrasser des astérisques dans les titres des repas et des tirets, des espaces supplémentaires et des sauts de ligne dans les listes d'ingrédients.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-7.46.34-PM.png)
_photo des données importées non nettoyées_

## Comment nettoyer les données

Pour les titres, nous utiliserons les fonctions `MID()` et `LEN()`.

```google sheets
//Pour la première ligne des titres de repas
=MID(A6,2,LEN(A6)-2)
```

`MID()` retourne une section du contenu de la cellule en commençant à un index et en terminant à un autre. Nous voulons saisir le contenu après le premier astérisque, nous utiliserons donc 2 comme premier index. Ensuite, nous utiliserons `LEN()-2` pour trouver la longueur du contenu de la cellule moins 2 pour l'index de fin.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.09.57-PM.png)
_Capture d'écran du nettoyage des données dans Google Sheet_

Pour les ingrédients, nous utiliserons d'abord `TRIM(CLEAN())` pour supprimer les caractères non imprimables et les espaces supplémentaires. Ensuite, nous utiliserons `ARRAYFORMULA(TRIM(SPLIT()))` pour obtenir chaque ingrédient restant dans sa propre cellule.

```google sheets
//Pour la première ligne des ingrédients
=ARRAYFORMULA(TRIM(SPLIT(C6,"-")))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.15.06-PM.png)
_Capture d'écran de TRIM, SPLIT et ARRAY FORMULA_

Maintenant que nous avons nos ingrédients divisés en cellules séparées, nommons quelques plages. Cela facilitera la vie lorsque nous construirons le tableau de bord dans un instant. 😀

En sélectionnant chaque colonne des ingrédients, allez dans `Données -> plages nommées` et nommez-les `Ingredient1`, `Ingredient2`, `Ingredient3`, `Ingredient4` et `Ingredient5`. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.20.43-PM.png)
_capture d'écran du menu des plages nommées_

De plus, sélectionnez toute la plage de données nettoyées : nos titres de repas et nos colonnes d'ingrédients individuels, et nommez cette plage `RecipeList`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.24.40-PM.png)
_Capture d'écran de la liste complète des recettes nettoyées_

## Comment obtenir tous les ingrédients uniques

Créez une nouvelle feuille en cliquant sur le bouton `+` en bas à gauche de la fenêtre et nommez cette feuille `Ingredients`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.26.05-PM.png)
_Capture d'écran du bouton ajouter une nouvelle feuille_

Nous avons maintenant besoin de tous les ingrédients uniques extraits dans une plage que nous nommerons `allIngredients`.

Pour ce faire, nous utiliserons la fonction `UNIQUE()` et toutes les plages nommées d'ingrédients enveloppées dans des accolades.

```appscript
=UNIQUE({Ingredient1;
Ingredient2;
Ingredient3;
Ingredient4;
Ingredient5})
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.28.41-PM.png)

Cela nous donne une liste unique d'ingrédients que nous utiliserons pour construire les menus déroulants dans notre tableau de bord.

## Comment créer le tableau de bord

Créez une autre nouvelle feuille et nommez-la `Dashboard`. C'est ici que le plaisir commence. 🔥

![Image](https://www.freecodecamp.org/news/content/images/2023/04/fun.gif)
_gif d'une femme disant, le plaisir va maintenant commencer._

La première chose dont nous avons besoin est quelques menus déroulants contenant tous les ingrédients possibles.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.32.55-PM.png)
_capture d'écran du menu déroulant_

Vous pouvez soit faire un clic droit dans une cellule et sélectionner Dropdown, soit sélectionner `Données -> Validation des données` dans la barre d'outils.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.33.35-PM.png)
_Capture d'écran de l'option Dropdown dans Google Sheets_

Sous critères, sélectionnez `Dropdown (à partir d'une plage)`. Et dans la plage, nous pouvons entrer la plage nommée que nous venons de créer à partir de notre feuille Ingredients : `=allIngredients`.

Cela remplira tous les ingrédients sous la sélection. Si vous le souhaitez, vous pouvez même personnaliser les options de couleur et d'apparence pour ceux-ci. Comme il y en a tellement, je les ai laissés par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.34.46-PM.png)
_Capture d'écran des règles de validation des données._

Il suffit de copier et coller cette cellule deux fois de plus et nous avons nos trois menus déroulants identiques.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.37.19-PM.png)
_Capture d'écran de 3 menus déroulants_

### Logique

Nous voulons gérer quelques cas différents dans notre tableau de bord. Pour tout ingrédient sélectionné ou combinaison d'ingrédients, nous voulons interroger notre plage nommée `RecipeList` pour ces ingrédients et retourner la recette complète correspondante.

Il y a huit combinaisons possibles pour les menus déroulants étant remplis : 

1. aucun
2. tous
3. seulement le premier
4. seulement le deuxième
5. seulement le troisième
6. premier et deuxième
7. premier et troisième
8. deuxième et troisième.

Nous devons alimenter une instruction de requête avec différentes valeurs selon lequel des états ci-dessus est vrai.

Créons une autre nouvelle feuille et nommons-la `Formula` pour épeler et suivre cette logique.

Nous avons besoin d'un simple test pour VRAI ou FAUX pour chacune des possibilités. Et pour ce faire, nous testerons simplement si chacun des menus déroulants est vide ou contient du texte. 

Heureusement, Google Sheets a deux fonctions qui font exactement cela : `ISBLANK()` et `ISTEXT()`.

Nous ferons un peu plus de nommage de plages pour rendre les choses plus lisibles, puis nous testerons chaque condition.

J'ai nommé les trois plages de menus déroulants sur le Dashboard `Dash9`, `Dash10` et `Dash11`.

Voici le code pour tester lorsque les premier et troisième menus déroulants sont remplis :

```google sheets
=IF(AND(ISTEXT(Dash9),ISTEXT(Dash10),ISBLANK(Dash11)),true,false)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.44.27-PM.png)
_Capture d'écran des tests logiques_

L'instruction `IF` retourne vrai ou faux en fonction de l'instruction `AND` imbriquée qui combine les instructions `ISTEXT` et `ISBLANK` pour chaque menu déroulant.

> Restez avec moi ! Tout est sur le point de s'assembler ! 👊

Maintenant, afin d'alimenter les options de menu déroulant dans notre instruction de requête (que je promets que nous allons écrire !), nous devons les concaténer avec des barres verticales qui fonctionneront comme l'opérateur `OR` dans la requête.

Donc...dans `A1` de notre feuille `Formula`, nous utiliserons une fonction `IFS()` pour afficher le contenu d'une ou plusieurs des plages `Dash9`, `Dash10` et `Dash11`. 

Pour y parvenir lorsqu'il y en a plus d'un avec des valeurs, nous utilisons l'opérateur `&` qui concatène la valeur dans la cellule `Dash` avec une barre verticale entre guillemets ("|"). Et le résultat est montré ci-dessous. 

```google sheets
=IFS(B2,"",
B3,Dash9,
B4,Dash10,
B5,Dash11,
B6,Dash9&"|"&Dash10,
B7,Dash9&"|"&Dash11,
B8,Dash10&"|"&Dash11,
B9,Dash9&"|"&Dash10&"|"&Dash11)
```

Nous avons notre valeur de requête construite. Et elle changera dynamiquement en fonction des menus déroulants qui contiennent du texte.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-12-at-8.55.39-PM.png)
_Capture d'écran de l'instruction IFS_

## Instruction de requête

Maintenant, le travail difficile est terminé. Intégrons ce que nous avons créé dans une instruction de requête sur le Dashboard pour que tout cela fonctionne !

La requête examinera une plage, dans notre cas la plage nommée `RecipeList` avec tous nos noms de repas et ingrédients, et retournera tout ce qui correspond aux critères que nous lui fournissons. 

Nous voulons retourner une recette complète lorsque notre plage nommée `Query` est appariée à un ingrédient dans l'une des cinq plages nommées d'ingrédients. 

Voici le code complet, et je l'expliquerai ci-dessous.

```google sheets
=if(Query="","",
QUERY(RecipeList,
"Select * 
WHERE E matches'"&Query&"' 
OR F matches '"&Query&"' 
OR G matches '"&Query&"' 
OR H matches '"&Query&"' 
OR I matches '"&Query&"'"))
```

Tout d'abord, si notre `Query` est une chaîne vide, nous ne voulons rien retourner...c'est lorsque aucun des menus déroulants n'est rempli et le résultat sera un tableau vide sur le tableau de bord.

`Select *` : cela signifie sélectionner tout, ou retourner toutes les valeurs dans la plage de requête. 

`WHERE E matches '"&Query&"'` : ceci est le début des critères. `E` est littéralement la colonne E de notre feuille `Data`. C'est là que se trouve la plage nommée `Ingredient1`. `F` est où se trouve `Ingredient2`...et ainsi de suite.

En utilisant `matches`, nous disons à la requête de voir si une valeur dans la plage nommée `Query` correspond à une valeur dans chacune des colonnes d'ingrédients spécifiées. Nous devons utiliser la syntaxe étrange de guillemets simples et doubles pour faire comprendre à la fonction de requête que nous utilisons cette plage nommée `Query` et non le mot ou la chaîne, "Query".

Les barres verticales dans notre plage nommée `Query` fonctionnent comme l'opérateur OR, donc lorsque plusieurs ingrédients sont dans la liste déroulante, l'instruction de requête recherche dans chaque colonne l'un **ou** l'autre ingrédient.

## Conclusion

C'était très amusant à faire, et j'espère que vous avez pu apprendre des compétences précieuses en suivant. 

Nous avons importé des données, les avons nettoyées, créé des plages nommées, des menus déroulants et des tests logiques changeant dynamiquement...tout cela pour une instruction de requête qui retourne les recettes dont nous avons besoin en fonction des ingrédients que nous lui donnons.

[Venez me suivre sur YouTube](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) où je crée plus de contenu comme celui-ci chaque semaine. 👋

Passez une excellente journée !