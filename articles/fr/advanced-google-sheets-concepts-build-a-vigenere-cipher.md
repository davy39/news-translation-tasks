---
title: Concepts avancés de Google Sheets – Comment construire un chiffrement Vigenère
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-12-13T18:13:22.000Z'
originalURL: https://freecodecamp.org/news/advanced-google-sheets-concepts-build-a-vigenere-cipher
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/2cipher.png
tags:
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Concepts avancés de Google Sheets – Comment construire un chiffrement Vigenère
seo_desc: "A Vigenère Cipher encrypts and decrypts text using a different alphabet\
  \ for each letter. It consists of text to encrypt and a key with a different letter\
  \ corresponding to each letter in the text. \nCreating a grid of alphabets helps\
  \ illustrate this pr..."
---

Un chiffrement Vigenère crypte et décrypte du texte en utilisant un alphabet différent pour chaque lettre. Il se compose d'un texte à crypter et d'une clé avec une lettre différente correspondant à chaque lettre du texte. 

Créer une grille d'alphabets aide à illustrer cette pratique. Si la première lettre de votre texte est `A` et la première lettre de votre clé est `L`, vous trouverez la lettre cryptée, `L`, là où le texte en clair et la clé se croisent :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/cipher2.png)
_capture d'écran d'une grille d'alphabets_

Ainsi, votre texte à crypter pourrait ressembler à ceci : `attackatdawn`, votre clé pourrait être celle-ci : `LEMONLEMONLE`, et le texte crypté serait celui-ci : `LXFOPVEFRNHR`.

C'est le même exemple utilisé sur la [page Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) que je vais vous expliquer dans cet article.

Vous pourriez créer un encodeur/décodeur de chiffrement avec n'importe quel langage de programmation. Mais les tableurs sont un bon outil à utiliser pour ce type de projet car ils disposent de fonctions intégrées assez robustes qui nous aideront à disséquer le chiffrement. 

J'ai choisi Google Sheets car il est un peu plus simple à utiliser, surtout si vous avez déjà un compte Gmail. Mais vous pouvez faire toutes les mêmes choses dans Microsoft Excel.

Voici le [Google Sheet que j'ai utilisé](https://docs.google.com/spreadsheets/d/1i_auliGPhTOIOk3WrsIRuHveXyEdQxi16BcvSBo6MTA/edit#gid=1257498594).

Si vous souhaitez consulter un tutoriel vidéo, le voici 👇

%[https://youtu.be/dM_Ims4KnVc]

## Préparation du tableur

Ce n'est pas trop compliqué. Nous avons besoin d'une grille d'alphabets. Non, vous n'avez pas à les taper encore et encore.

En fait, vous n'avez même pas à taper tout le premier alphabet. Utilisons des caractères Unicode. Pour les lettres majuscules, l'Unicode de l'alphabet commence à 65. 

La fonction `CHAR()` dans les tableurs convertit un nombre en caractère selon la table Unicode actuelle.

La fonction `COLUMN()` retourne un nombre correspondant à la colonne actuelle où la colonne A retourne 1, la colonne B retourne 2, et ainsi de suite. 

Ainsi, si nous commençons notre alphabet dans la colonne B, nous pouvons accéder à chaque lettre en ajoutant 63 à la fonction `COLUMN()` et en l'enveloppant dans la fonction `CHAR()` :

```
=CHAR(COLUMN()+63)
```

Ensuite, nous pouvons faire glisser cela vers la droite jusqu'à ce que nous ayons l'alphabet complet.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-41.png)
_capture d'écran des fonctions CHAR et COLUMN_

La même chose s'applique en descendant. Nous allons simplement utiliser la fonction `ROW()` à la place :

```
=CHAR(ROW()+63)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-42.png)
_capture d'écran des fonctions CHAR et ROW_

Ensuite, nous pouvons référencer la cellule au-dessus et à droite pour chaque cellule en dessous pour remplir la grille complète de l'alphabet :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-43.png)
_capture d'écran d'une cellule de tableur_

La seule qui sera différente sera dans la dernière colonne où nous devrons référencer la première colonne pour que l'alphabet s'enroule :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-44.png)
_capture d'écran d'une cellule de tableur_

Nous n'avons à faire cela que sur la deuxième ligne. Ensuite, sélectionnez la deuxième ligne complète et faites glisser les formules vers le bas pour remplir la grille :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/drag.png)
_capture d'écran de la grille de tableur_

À ce stade, vous pouvez copier `CTRL + C` et coller uniquement les valeurs `CTRL + SHIFT + V` pour tout l'alphabet. Si vous ajoutez ou déplacez des lignes, les alphabets peuvent être déformés puisque leurs formules référencent des colonnes fixes.

## Le plan de jeu

Maintenant, le plus amusant. Nous voulons que notre texte soit crypté automatiquement. Mettons en évidence trois cellules : une pour le texte à crypter, une pour une clé, et ensuite une cellule vide pour notre texte crypté :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-46.png)
_capture d'écran du texte à crypter_

Remarque : la clé doit être de la même longueur que le texte à crypter/décrypter. Dans cet exemple, la clé est le mot LEMON, mais nous l'étendons en la répétant pour chaque caractère que nous devons crypter.

Maintenant, nous devons faire trois choses : 

1. Séparer chaque caractère de notre texte dans sa propre cellule
2. Parcourir chaque caractère et le crypter en fonction du caractère de clé correspondant.
3. Joindre tous ces caractères ensemble et placer le résultat dans notre cellule de texte crypté.

## Diviser le texte pour l'installation

Intéressamment, nous ne pouvons pas utiliser la fonction `SPLIT()` - ou si vous êtes dans Excel, la fonction `TEXTSPLIT()` - sans délimiteur. C'est-à-dire que nous ne pouvons pas simplement lui dire de diviser chaque caractère sans qu'il y ait quelque chose entre les caractères.

Nous devons donc être astucieux. Dans le tutoriel vidéo, j'explore une approche spécifique à Google Sheets utilisant des expressions régulières... qui sont un défi amusant.

Voici à quoi cela ressemble, et cela implique de créer des groupes de caractères, d'insérer quelque chose entre chacun d'eux, puis de diviser en utilisant cette même chose comme délimiteur. J'ai utilisé un espace vide comme la chose que j'ai insérée puis divisée par :

```
=SPLIT(REGEXREPLACE(AG6,"(.)","$1 ")," ")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/hard.gif)
_gif d'une femme disant, c'est juste difficile_

Utilisateurs d'Excel et mortels, ne craignez rien – il existe une méthode plus élégante que je vais vous montrer ici et qui peut être réalisée dans les deux programmes en utilisant les fonctions `MID()` et `COLUMNS()`.

La fonction `MID()` extrait un segment d'une chaîne, et `COLUMNS()` retourne le nombre de colonnes dans un tableau. En imbriquant `COLUMNS()` à l'intérieur de `MID()`, nous pouvons extraire un par un chaque caractère de la chaîne :

```
=MID($AG$6,COLUMNS($AG6:AG6),1)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-47.png)
_capture d'écran des fonctions MID et COLUMNS_

En verrouillant `$AG6` comme première partie du tableau référencé dans la fonction `COLUMNS()`, ce nombre ajoute un pour chaque colonne sur laquelle nous faisons glisser notre formule.

Faites glisser cela jusqu'à ce que vous atteigniez la fin du texte à crypter. Chaque caractère devrait maintenant être dans sa propre cellule. Faites de même pour la clé.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-48.png)
_capture d'écran des cellules de tableur_

## Comment utiliser `XLOOKUP()` pour crypter

Sous chaque paire de texte en clair et de texte de clé, nous allons maintenant faire un double `XLOOKUP()`. 

Oui, c'est aussi génial que cela en a l'air.

Voici à quoi cela ressemble, et passons en revue ce qui se passe :

```
=XLOOKUP(AD9,$B$2:$B$27,XLOOKUP(AD10,$B$2:$AA$2,$B$2:$AA$27))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-49.png)
_capture d'écran des fonctions double XLOOKUP_

Pour le premier `XLOOKUP()`, nous recherchons le texte en clair et nous référençons le premier alphabet en clair pour notre plage de recherche. Mais ensuite, pour notre plage de résultats, nous ouvrons un autre `XLOOKUP()`...

C'est parce que nous devons encore utiliser l'alphabet de clé correct pour retourner une valeur cryptée.

Nous avons donc besoin du deuxième `XLOOKUP()` pour retourner un alphabet complet basé sur la position du caractère de la clé.

Nous utilisons le caractère de la clé comme notre valeur de recherche, nous utilisons le premier alphabet le long de la ligne de clé supérieure pour notre plage de recherche, puis nous retournons toute la grille comme notre plage de résultats. Cela nous permettra de retourner un alphabet complet qui est à son tour référencé comme la plage de résultats pour notre premier `XLOOKUP()`.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/cipher3.png)
_capture d'écran de la grille d'alphabet et exemple de XLOOKUP_

Vous pouvez voir le deuxième `XLOOKUP()` seul dans l'image ci-dessus. La formule est en haut à gauche. Nous utilisons la première lettre du texte de la clé comme valeur de recherche. La plage de recherche est l'alphabet supérieur dans la boîte violette. La plage de résultats est toute la grille dans la boîte bleue. Et l'alphabet retourné est celui qui commence par L dans la boîte rouge.

Vous pouvez le voir retourné sous la formule où il y a une flèche dans l'image.

Faites glisser la fonction double `XLOOKUP()` pour crypter chaque caractère du texte en clair avec le texte de la clé.

## Joindre le texte pour la solution finale

Maintenant que nous avons crypté chaque lettre, nous voulons qu'elles soient jointes en une seule chaîne et retournées dans notre cellule de texte crypté.

Pour ce faire, nous pouvons utiliser la fonction `JOIN()` - ou `TEXTJOIN()` pour Excel - avec une citation vide comme délimiteur. 

```
=JOIN("",AD11:AO11)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-50.png)
_capture d'écran de la fonction JOIN_

Et voilà ! Nous venons de crypter une chaîne en utilisant un double `XLOOKUP()`.

## Comment décrypter le texte

Le décryptage fonctionne exactement de la même manière. La seule différence est le placement du deuxième `XLOOKUP()`. Au lieu de l'utiliser comme plage de résultats, nous l'utilisons comme plage de recherche :

```
=XLOOKUP(AD20,XLOOKUP(AD21,$B$2:$AA$2,$B$2:$AA$27),$B$2:$B$27)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-51.png)
_capture d'écran de l'exemple de double XLOOKUP pour le décryptage_

## Merci d'avoir lu

J'espère que cela vous a été utile et que vous avez appris quelque chose de nouveau !

Vous pouvez trouver plus de mes tutoriels sur [YouTube](https://www.youtube.com/@eamonncottrell), et veuillez vous inscrire à ma newsletter sur [le codage et les tableurs ici](https://got-sheet.beehiiv.com/).