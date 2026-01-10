---
title: RECHERCHEV dans Excel – Formule et exemple de fonction
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-05T16:26:42.000Z'
originalURL: https://freecodecamp.org/news/vlookup-in-excel-formula-and-example-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/vlookup.png
tags:
- name: data analysis
  slug: data-analysis
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: RECHERCHEV dans Excel – Formule et exemple de fonction
seo_desc: "In Excel, VLOOKUP() means vertical lookup. It is a powerful built-in function\
  \ you can use to quickly search for a value in a spreadsheet. \nVLOOKUP() searches\
  \ for a value in a vertical manner across the sheet – unlike the HLOOKUP() function\
  \ which does..."
---

Dans Excel, `RECHERCHEV()` signifie recherche verticale. C'est une fonction intégrée puissante que vous pouvez utiliser pour rechercher rapidement une valeur dans une feuille de calcul. 

`RECHERCHEV()` recherche une valeur de manière verticale à travers la feuille – contrairement à la fonction `RECHERCHEH()` qui le fait horizontalement.

Avant d'utiliser `RECHERCHEV()`, assurez-vous que chaque ligne de votre feuille de calcul possède un identifiant (ID). Les ID doivent également être classés par ordre croissant. Cela permet de s'assurer qu'Excel ne s'embrouille pas lors du processus de renvoi d'une valeur à partir d'une recherche.

Dans cet article, je vais vous montrer comment utiliser la fonction `RECHERCHEV()` en expliquant les valeurs que vous devez saisir dans la fonction. Nous examinerons également deux exemples différents.	

## La formule `RECHERCHEV()` et ses valeurs
Dans Excel, vous faites presque tout avec une formule – et `RECHERCHEV()` ne fait pas exception. 

Voici les valeurs que prend la fonction `RECHERCHEV()` :

`RECHERCHEV(valeur_cherchée, table_matrice, no_index_col, [valeur_proche])`

- valeur_cherchée : la cellule qui contient la valeur que vous souhaitez rechercher. Elle se trouve toujours à gauche. Par exemple, A5.
- table_matrice : l'emplacement où vous pensez que la valeur se trouve et où vous voulez qu'Excel effectue la recherche. Par exemple, A1:D10
- no_index_col : la colonne où se trouve la valeur. Par exemple, 4
- [valeur_proche] : Vous pouvez seulement spécifier VRAI (TRUE) ou FAUX (FALSE) pour cela. VRAI signifie une correspondance approximative et FAUX signifie une correspondance exacte.

## Comment utiliser `RECHERCHEV()` dans Excel
Pour utiliser `RECHERCHEV()` afin de rechercher une valeur dans Excel, vous devez utiliser la formule et saisir les valeurs individuelles discutées dans la section précédente.

Pour vous montrer comment utiliser `RECHERCHEV`, j'utiliserai le tableau ci-dessous. C'est un tableau montrant quelques footballeurs fictifs, leurs âges, leurs clubs et le nombre de buts marqués au cours de leur carrière.

![ss1-1](https://www.freecodecamp.org/news/content/images/2022/10/ss1-1.png) 

### Exemple 1 de `RECHERCHEV()`
Dans le tableau, je veux voir le nombre de buts marqués en carrière par Kat Katongo (`A5`). Nous pouvons utiliser RECHERCHEV() dans ce cas. Cet exemple ne nécessite pas d'ID pour toutes les entrées.

**Étape 1** : Tapez un nom représentatif dans une cellule vide :
![ss2-1](https://www.freecodecamp.org/news/content/images/2022/10/ss2-1.png) 

**Étape 2** : Il est logique de placer les buts en carrière juste en face de la cellule de référence, je vais donc mettre la cellule en surbrillance :
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/10/ss3-1.png) 

**Étape 3** : Saisissez la formule dans la barre de formule :
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/10/ss4-1.png)

La formule que j'utilise est `=RECHERCHEV(A5, A1:D10, 4, FAUX)` :
![ss5-1](https://www.freecodecamp.org/news/content/images/2022/10/ss5-1.png) 

- A5 est la valeur_cherchée
- A1:D10 est la table_matrice
- 4 est le no_index_col – parce que c'est la colonne pour les buts en carrière 
- FAUX est la [valeur_proche] parce que je veux une correspondance exacte.

Et voilà ! 180 apparaît dans la cellule :
![ss6-1](https://www.freecodecamp.org/news/content/images/2022/10/ss6-1.png) 

Pour rendre les choses plus claires pour vous, le GIF ci-dessous montre comment j'ai saisi la formule :
![vlookup1](https://www.freecodecamp.org/news/content/images/2022/10/vlookup1.gif) 

### Exemple 2 de `RECHERCHEV()`

Dans cet exemple, je veux simplement saisir un ID et voir les buts en carrière du joueur. Cela signifie que je dois attribuer un ID à chaque footballeur.
![ss7](https://www.freecodecamp.org/news/content/images/2022/10/ss7.png) 

**Étape 1** : Maintenant, je veux commencer par rechercher les buts en carrière du joueur ayant l'ID 9. Je prépare donc quelques entrées supplémentaires sur la droite.
![ss8](https://www.freecodecamp.org/news/content/images/2022/10/ss8.png) 

**Étape 2** : Pour rechercher les buts en carrière du joueur avec l'ID 9 (Baba Ali), je vais sélectionner la cellule dans laquelle je veux qu'ils s'affichent et cliquer sur l'onglet formule. Une fois cela fait, une invite apparaîtra.
![ss9](https://www.freecodecamp.org/news/content/images/2022/10/ss9.png) 

**Étape 3** : Sélectionnez `RECHERCHEV` et cliquez sur OK. Si vous ne voyez pas `RECHERCHEV()` à cet endroit, recherchez-la et sélectionnez-la.
![ss10](https://www.freecodecamp.org/news/content/images/2022/10/ss10.png)

**Étape 4** : Une autre fenêtre contextuelle affichant les champs pour saisir les valeurs de la formule apparaîtra :
![ss11](https://www.freecodecamp.org/news/content/images/2022/10/ss11.png)

**Étape 5** : Saisissez les valeurs une par une :
![ss12](https://www.freecodecamp.org/news/content/images/2022/10/ss12.png) 

- J'ai saisi `I3` pour la valeur cherchée car c'est là que j'ai mis l'ID 9
- `A1:E10` pour la table matrice car c'est la zone dans laquelle je veux effectuer la recherche
- `5` pour l'index de colonne car c'est la colonne contenant les buts en carrière des joueurs
- et `FAUX` comme valeur_proche car je veux une correspondance exacte

Lorsque j'ai appuyé sur `OK`, les buts en carrière de Baba Ali (le joueur avec l'ID 9) se sont affichés :
![ss13](https://www.freecodecamp.org/news/content/images/2022/10/ss13.png) 

Pour rendre les choses plus claires pour vous, voici comment j'ai saisi la formule :
![vlookup2](https://www.freecodecamp.org/news/content/images/2022/10/vlookup2.gif) 

Chaque fois que je change l'ID et que j'appuie sur `ENTRÉE`, les buts en carrière du joueur correspondant à cet ID s'affichent :
![vlookup3](https://www.freecodecamp.org/news/content/images/2022/10/vlookup3.gif) 

## Conclusion
`RECHERCHEV()` est une fonction Excel puissante qui peut vous aider à rechercher n'importe quelle valeur dans une feuille de calcul – qu'elle soit petite ou grande. C'est pourquoi j'ai écrit cet article pour vous aider à démarrer avec elle.

Si vous trouvez cet article utile, n'hésitez pas à le partager afin qu'il puisse profiter à d'autres.

Merci de m'avoir lu.