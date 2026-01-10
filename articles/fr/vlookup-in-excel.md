---
title: Exemple de VLOOKUP – Comment faire une recherche VLOOKUP dans Excel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-11T18:06:38.000Z'
originalURL: https://freecodecamp.org/news/vlookup-in-excel
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/pexels-photo-4050320-1.jpeg
tags:
- name: excel
  slug: excel
- name: Microsoft
  slug: microsoft
seo_title: Exemple de VLOOKUP – Comment faire une recherche VLOOKUP dans Excel
seo_desc: 'By Gregory V. Chapman

  Microsoft Excel includes a variety of different functions that help users with calculations
  of any kind. The functionality of Excel is so comprehensive that average users don''t
  even take advantage of most utilities.

  However, if ...'
---

Par Gregory V. Chapman

Microsoft Excel inclut une variété de fonctions différentes qui aident les utilisateurs avec des calculs de tout type. La fonctionnalité d'Excel est si complète que les utilisateurs moyens ne profitent même pas de la plupart des utilitaires.

Cependant, si vous faites souvent défiler des colonnes et des lignes à la recherche des mêmes informations, il est probable que vous apprécierez la fonction VLOOKUP. VLOOKUP, qui signifie « recherche verticale », peut vous aider à trouver rapidement les données associées à une certaine valeur que vous entrez.

Par exemple, vous pouvez avoir un tableau qui contient des produits avec des identifiants uniques et des prix. VLOOKUP peut vous montrer le prix d'un certain produit si vous entrez son identifiant. 

Vous pouvez utiliser VLOOKUP de nombreuses manières différentes et cela simplifiera considérablement votre travail, surtout lorsque vous traitez avec de grands tableaux.

Vous n'avez pas besoin de passer beaucoup de temps à chercher une certaine cellule car cette fonction la trouvera pour vous. Cependant, les utilisateurs débutants trouvent souvent difficile de configurer VLOOKUP. Par conséquent, j'ai décidé de vous aider en préparant ce guide détaillé.

## Qu'est-ce que VLOOKUP ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/m-b-m-ZzOa5G8hSPI-unsplash.jpg)

Tout d'abord, VLOOKUP est une fonction. Par conséquent, si vous êtes nouveau dans Excel, vous pouvez vouloir vous familiariser avec certaines fonctions de base, comme MOYENNE, SOMME, ou AUJOURDHUI. De cette façon, il vous sera facile de comprendre comment cette fonction fonctionne.

VLOOKUP est une fonction de base de données, donc elle est destinée aux tableaux de bases de données. Ces tableaux sont essentiellement des listes de différents éléments. Par exemple, vous pouvez utiliser cette fonction lorsque vous travaillez avec des listes de produits, d'employés, de clients, etc.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/photo_2020-06-11_20-26-54.jpg)

Disons que vous avez une liste de produits qui se compose de quatre colonnes. Elle peut inclure le code de l'article dans la première colonne, le nom ou la description du produit dans la deuxième colonne, et le prix et le nombre d'articles disponibles en stock dans les troisième et quatrième colonnes, respectivement.

Les tableaux de bases de données ont généralement une sorte d'identifiant unique pour chaque élément. Dans ce cas, c'est le code de l'article. Cette colonne est nécessaire pour que la fonction VLOOKUP fonctionne, et elle doit être la première colonne de votre tableau.

Si vous êtes débutant, la première chose que vous devriez faire est de comprendre ce que VLOOKUP fait exactement. Simplement dit, il affiche des informations à partir d'une liste ou d'une base de données en fonction de l'identifiant unique entré par l'utilisateur.

Si nous considérons l'exemple ci-dessus, cette fonction pourrait afficher le prix, la description ou la disponibilité d'un produit en fonction de son code d'article. Ce qu'elle affichera exactement dépend de la formule que vous écrivez. VLOOKUP prend en charge à la fois la correspondance exacte et approximative, ainsi que les caractères génériques pour les correspondances partielles.

## Comment fonctionne VLOOKUP

Voici la syntaxe des formules qui décrivent la fonction VLOOKUP :

`=VLOOKUP(valeur, tableau, indice_colonne, [plage])`

* `valeur` est ce que cette fonction recherchera dans la première colonne
* `tableau` est le tableau à partir duquel la fonction récupérera les informations nécessaires
* `indice_colonne` est le numéro de la colonne à partir de laquelle la fonction récupérera les informations
* `plage` est un paramètre booléen qui peut être soit VRAI soit FAUX. VRAI est la valeur par défaut, et elle correspond à la correspondance approximative. FAUX vous montrera uniquement les correspondances exactes.

Même le nom de cette fonction inclut « vertical », et VLOOKUP est uniquement destiné aux tableaux où les données sont organisées en colonnes verticales. Par conséquent, si vous organisez vos données horizontalement, cette fonction sera inutile. Dans ce cas, vous pouvez utiliser une fonction similaire pour la recherche horizontale — [HLOOKUP](https://support.office.com/en-us/article/hlookup-function-a3034eec-b719-4ba3-bb65-e1ad662ed95f).

Vous devez également garder à l'esprit que cette fonction ne fonctionne que de gauche à droite. En d'autres termes, si l'identifiant unique n'est pas dans la première colonne de votre tableau, la fonction ne pourra pas récupérer les informations des colonnes à gauche de l'identifiant.

Chaque colonne a son numéro, et toutes les colonnes sont numérotées de gauche à droite. Si vous voulez obtenir une valeur d'une certaine colonne, vous devez spécifier son numéro dans votre formule. Dans le modèle de formule ci-dessus, ce numéro est appelé `indice_colonne`. 

Par exemple, si vous voulez récupérer le nom du produit de l'exemple ci-dessus, l'indice de colonne doit être 2.

Comme je l'ai déjà mentionné ci-dessus, la fonction VLOOKUP prend en charge deux modes de correspondance : approximatif et exact. Ce paramètre est le quatrième argument de la formule. La correspondance approximative est définie par défaut. Si vous voulez choisir la correspondance exacte, vous devez définir la plage de recherche sur `FAUX`.

Par conséquent, les deux formules ci-dessous récupéreront les données en utilisant la correspondance approximative :

`=VLOOKUP(valeur, tableau, indice_colonne)`

`=VLOOKUP(valeur, tableau, indice_colonne, VRAI)`

Comme vous pouvez le voir, si vous voulez utiliser le mode de correspondance exacte, vous devez être prudent. Si vous ne fournissez aucune valeur de plage de recherche, la fonction utilisera toujours le mode de correspondance approximative.

La formule suivante forcerait le mode de correspondance exacte :

`=VLOOKUP(valeur, tableau, indice_colonne, FAUX)`

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mika-baumeister-Wpnoqo2plFA-unsplash.jpg)

Assurez-vous de définir la valeur sur `FAUX` si vous allez utiliser le mode de correspondance exacte. Il est probable que vous aurez besoin de la correspondance exacte dans la plupart des cas, donc si vous êtes nouveau dans Excel, n'oubliez pas ce détail. 

La correspondance exacte est le bon choix si vous avez une colonne avec l'identifiant de l'article. Cela peut également être une valeur unique qui peut être utilisée pour une recherche exacte. Par exemple, cela peut être un titre unique d'un livre ou d'un film, ainsi que tout autre mot-clé unique. Gardez à l'esprit que VLOOKUP n'est pas sensible à la casse.

Cependant, parfois vous pouvez avoir besoin non pas de la correspondance exacte, mais de la meilleure correspondance possible. Dans ce cas, vous pouvez utiliser le mode de correspondance approximative. 

Par exemple, vous pouvez utiliser ce mode lorsque vous traitez avec des tableaux de données où les informations nécessaires correspondent à certaines valeurs numériques, et vous voulez récupérer des résultats pour une valeur qui n'est pas incluse dans le tableau.

Vous pouvez utiliser cette approche lorsque vous effectuez des calculs basés sur les données existantes. Si vous entrez une valeur et que la fonction trouve la correspondance exacte, elle récupérera les informations de la ligne correspondante. Cependant, s'il n'y a pas de correspondance exacte dans le tableau, la fonction correspondra à la ligne précédente.

Pourquoi correspondrait-elle à la ligne précédente, et non à une autre ? Eh bien, elle ne le fera pas si vous n'organisez pas votre tableau de la bonne manière. Pour permettre à VLOOKUP de rechercher la meilleure valeur approximative, vous devez vous assurer que toutes les valeurs de cette colonne sont triées par ordre croissant. Dans ce cas, la fonction reculera simplement et récupérera la valeur la plus proche.

## Erreurs #N/A

Lorsque vous utilisez la fonction VLOOKUP, ainsi que de nombreuses autres fonctions dans Excel, vous pouvez souvent obtenir des erreurs #N/A. Cette erreur signifie que la valeur n'a pas été trouvée. 

Vous pouvez obtenir cette erreur pour plusieurs raisons. Voici quelques-uns des cas les plus courants :

* vous avez mal orthographié la valeur ou ajouté un espace supplémentaire
* la valeur nécessaire n'existe pas dans le tableau
* vous utilisez le mode de correspondance exacte lorsque vous recherchez une valeur approximative
* vous n'avez pas entré la plage de tableau correcte
* vous avez copié VLOOKUP alors que la référence de tableau n'est pas verrouillée.

Si votre tableau a une référence absolue, cela signifie que les lignes et les colonnes ne changeront pas si elles sont copiées. Cependant, ce n'est pas le cas avec une référence relative. Dans ce cas, vous devrez [passer à la référence absolue](https://support.office.com/en-us/article/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9).

Vous pouvez personnaliser le texte de l'erreur #N/A en utilisant la [fonction SIERREUR](https://support.office.com/en-ie/article/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461). Dans ce cas, vous devez écrire une formule plus longue avec SIERREUR qui inclut VLOOKUP. 

Voici un exemple de formule qui retournera « non trouvé » au lieu de #N/A :

`=SIERREUR(VLOOKUP(valeur, tableau, indice_colonne, FAUX), "non trouvé")`

Et voici une formule qui retournera un résultat vide :

`=SIERREUR(VLOOKUP(valeur, tableau, indice_colonne, FAUX), "")`

Bien que vous puissiez personnaliser le message, vous pouvez envisager d'utiliser l'erreur #N/A car elle attirera immédiatement votre attention et vous fera savoir si quelque chose ne va pas.

## Comment utiliser VLOOKUP

Vous pouvez écrire des formules à partir de zéro, ou vous pouvez également utiliser le menu Excel. Sélectionnez la cellule où vous voulez afficher le résultat, puis sélectionnez l'onglet « Formules ». 

Après cela, cliquez sur « Insérer une fonction ». Vous verrez une boîte où vous pouvez sélectionner des catégories de fonctions et choisir la fonction VLOOKUP. Vous pouvez également utiliser la boîte « Rechercher une fonction », et entrer « vlookup ».

Sélectionnez la fonction, et la boîte « Arguments de la fonction » apparaîtra. Ici, vous pouvez entrer les paramètres nécessaires de la fonction. Dans cette fenêtre, vous devez spécifier l'identifiant unique que vous recherchez, l'emplacement de la base de données et les informations qui correspondent à l'identifiant que vous voulez récupérer.

Ces arguments sont « Valeur_recherchée », « Tableau », et « Numéro_indice_colonne ». Ces champs sont écrits en gras car ces arguments sont obligatoires. 

Le quatrième argument est pour le mode de recherche, et vous pouvez ou non le spécifier. Le mode approximatif est défini par défaut.

Pour entrer le premier argument, qui est l'identifiant unique, vous pouvez sélectionner la cellule nécessaire et appuyer sur Entrée. Dans ce cas, la valeur de cette cellule sera automatiquement entrée comme premier argument de la fonction VLOOKUP.

Maintenant, vous devez entrer le deuxième argument. La base de données n'a pas nécessairement besoin de commencer dans le coin supérieur gauche. Par exemple, vous pouvez également avoir une ligne qui décrit les colonnes, qui sert d'en-tête. 

« L'une des meilleures choses à propos de la fonction VLOOKUP est que l'emplacement de la base de données peut également être personnalisé », note Bridget Allen, comptable chez [Best Writers Online](http://bestwritersonline.com/).

Étant donné que VLOOKUP ne fonctionne qu'avec les numéros de colonnes, vous devez spécifier quelle zone de votre tableau vous voulez utiliser pour la recherche. C'est à cela que sert la boîte « Tableau ». 

Par exemple, si votre tableau commence dans le coin supérieur gauche, et que sa première ligne est un en-tête, vous pouvez sélectionner toute la base de données sans la première ligne. Si votre base de données a quatre colonnes (A-D) et cinq éléments, le tableau sera A2:D6, car les cellules A1-D1 contiendront l'en-tête.

Vous pouvez cliquer sur l'onglet de la feuille de calcul nécessaire et sélectionner la zone avec la base de données. Appuyez sur Entrée et la plage de cellules sélectionnée sera automatiquement ajoutée au deuxième argument de la fonction VLOOKUP. Voici un exemple d'argument de fonction :

`'nom_base_de_données'!A2:D6`

Dans ce cas, « nom_base_de_données » est le nom de l'onglet de la feuille de calcul.

Maintenant, vous devez simplement spécifier quelles informations vous voulez récupérer et fournir le numéro de la colonne nécessaire. 

Par exemple, si vous voulez récupérer le prix d'un article du tableau au début de cet article, vous devez utiliser la troisième ligne, et la valeur « Numéro_indice_colonne » sera 3.

## Conclusion

Microsoft Excel dispose d'une grande variété de fonctions qui peuvent aider les utilisateurs à traiter différents calculs et autres tâches. VLOOKUP est une fonction très utile qui peut récupérer des informations correspondant à une certaine valeur d'un tableau de base de données. 

Si vous êtes nouveau dans Excel, vous pouvez rencontrer des difficultés avec cette fonction car elle a quatre arguments.

Cependant, si vous suivez notre guide, vous serez en mesure de sélectionner les bons arguments et d'utiliser les bonnes formules. Si vous utilisez cette fonction quelques fois en pratique, vous comprendrez rapidement comment elle fonctionne afin de pouvoir utiliser VLOOKUP chaque fois que vous en avez besoin.