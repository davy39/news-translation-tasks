---
title: Tutoriel Google Sheets – Comment utiliser Regex et VLOOKUP pour afficher des
  images depuis Google Drive
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2022-08-03T17:03:25.000Z'
originalURL: https://freecodecamp.org/news/google-sheets-use-regex-and-vlookup-to-display-images-from-google-drive
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/google-sheets-regex.jpg
tags:
- name: google sheets
  slug: google-sheets
- name: image
  slug: image
- name: Regex
  slug: regex
- name: Regular Expressions
  slug: regular-expressions
seo_title: Tutoriel Google Sheets – Comment utiliser Regex et VLOOKUP pour afficher
  des images depuis Google Drive
seo_desc: "Images make many things better. And Google Sheets is one of those things.\
  \ \nThe easiest way to add an image to Google Sheets is to simply insert one into\
  \ your sheet. \nBut if you have added many images this way, you'll quickly tire\
  \ of the multiple clic..."
---

Les images améliorent beaucoup de choses. Et Google Sheets en fait partie. 

La manière la plus simple d'ajouter une image à Google Sheets est de simplement en insérer une dans votre feuille. 

Mais si vous avez ajouté beaucoup d'images de cette manière, vous vous lasserez rapidement des multiples clics nécessaires pour le faire. Surtout si vous devez ajouter des images souvent, ou si vous devez ajouter les mêmes images à plusieurs feuilles.

Dans cet article, vous apprendrez à ajouter plusieurs images à partir de leurs URLs que vous pourrez basculer dynamiquement dans une liste déroulante. Nous aborderons :

* La validation des données pour créer une liste déroulante
* Les plages nommées pour rendre les références de formules plus faciles et plus propres
* La fonction VLOOKUP pour afficher la bonne image à partir de la liste déroulante
* La fonction REGEXEXTRACT pour extraire une chaîne d'une URL (ne vous inquiétez pas, cela aura du sens 😉)
* La fonction IMAGE pour afficher l'image à partir d'une adresse URL
* Nous utiliserons l'opérateur esperluette (&) ainsi que les expressions régulières (Regex)
* Nous rendrons également notre feuille plus attrayante en supprimant les lignes de grille, en changeant la police, en ajoutant des bordures, des couleurs et un effet d'ombre portée derrière les tableaux

## Comment installer le projet 📰

Vous pouvez suivre avec la feuille que j'utilise pour tout ce dont nous allons discuter :

[https://docs.google.com/spreadsheets/d/1rFU2gPy6rU8IKFDmsxKHYCf0KGVHkcumQ5O5QCf156M/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1rFU2gPy6rU8IKFDmsxKHYCf0KGVHkcumQ5O5QCf156M/edit?usp=sharing)

Faites une copie si vous souhaitez l'éditer vous-même.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/copy.png)
_Faites une copie pour l'éditer vous-même_

Toutes les références de cellules et de plages ci-dessous proviendront de cette feuille afin que vous puissiez facilement voir de quoi je parle.

J'ai également créé un dossier d'images [ici](https://drive.google.com/drive/folders/1na_BdarFXheF5t6YssKY2qPfTEDLYlSF?usp=sharing) qui est partagé publiquement pour que tout cela fonctionne. Vous n'avez pas besoin de faire une copie de cela sauf si vous le souhaitez vraiment 😀.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/visible.png)

## Comment utiliser les plages nommées dans Google Sheets 📝

Les plages nommées facilitent la vie. 

Vous n'êtes pas obligé de les utiliser, mais cela rend les références dans les fonctions plus faciles puisque vous écrirez le nom de quelque chose au lieu d'une référence de cellule stérile.

Nous en utiliserons trois :

1. `B4` = `itemSelect` C'est la cellule où notre liste déroulante résidera.
2. `B8:G13` = `pictureMatch` C'est la plage pour notre fonction VLOOKUP. Elle contient les noms des images que nous afficherons suivis de leurs URLs respectives.
3. `B8:B16` = `pictureName` C'est la première colonne de la plage `pictureMatch` pour référencer uniquement les noms dans notre cellule de validation des données.

Pour créer une plage nommée, il suffit de surligner la plage, de sélectionner Données -> Plages nommées dans la barre d'outils, et de la nommer.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/named.png)

## Comment effectuer la validation des données 📋

Nous utiliserons la validation des données pour créer une liste déroulante dans B4. Même principe ici – il suffit de surligner la cellule (ou la plage) et de sélectionner Données -> Validation des données dans la barre d'outils :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/validation.png)

Sélectionnez Liste à partir d'une plage, puis `=pictureName` (parce que nous avons nommé cette plage) pour la plage. Alternativement, vous pouvez déclarer la plage explicitement.

Il y a des options supplémentaires à configurer si vous souhaitez changer quelque chose :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-8.png)

Si vous sélectionnez rejeter l'entrée, vous pouvez faire apparaître un message personnalisé chaque fois qu'un choix invalide est saisi :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-7.png)
_Vous pourriez vouloir rendre votre message plus utile que celui-ci._

## Comment utiliser VLOOKUP 📊

VLOOKUP est une fonction incroyablement utile. Elle prend quatre arguments : 

```
=VLOOKUP(search_key, range, index, [is_sorted])

=VLOOKUP(itemSelect,pictureMatch,3,0)

```

Nous utiliserons `itemSelect` pour notre `search_key` et `pictureMatch` pour la plage parce que nous voulons trouver `itemSelect` dans cette plage. Ensuite, le 3 pour index obtient la valeur dans la troisième colonne de cette plage. 

(C'est 3 dans notre exemple parce que nous avons fusionné les cellules des colonnes B & C pour notre mise en forme, mais VLOOKUP les compte toujours toutes les deux).

Enfin, le zéro définit `is_sorted` sur `FALSE`. Nos données ne sont pas triées, et nous voulons une correspondance exacte.

## Comment utiliser REGEXEXTRACT 📋

C'est arrivé : j'ai trouvé une utilisation réelle des expressions régulières. 😳

[Cette section de la certification Javascript de freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/regular-expressions/) était particulièrement confuse pour moi, et il était bon de revisiter une petite partie ici dans la nature.

Parce que Google Drive est capricieux, et que nous bricolons une option gratuite ici, nous devons modifier les URLs de nos images pour que la fonction IMAGE fonctionne correctement.

[Cette](https://stackoverflow.com/questions/60287504/how-display-images-from-google-drive-on-gsheet-cell) réponse Stack Overflow m'a été utile.

Nous devons construire une URL en prenant ceci :

```javascript
https://drive.google.com/uc?export=download&id=###
```

et en remplaçant la partie ### à la fin par l'ID que nous extrayons avec la fonction `REGEXEXTRACT`.

En regardant les URLs que nous avons copiées, nous pouvons voir un motif. Tout ce qui suit le `/d/` et avant le `/` suivant est l'ID. 

Voici un exemple de l'une de nos URLs d'image : [`https://drive.google.com/file/d/1IaO08gj3GWIUQDAnzKEob62Gcl87ufuN/view?usp=sharing`](https://drive.google.com/file/d/1IaO08gj3GWIUQDAnzKEob62Gcl87ufuN/view?usp=sharing)

Vous pouvez voir cela en action seul dans `B26` de la feuille de calcul d'exemple alors que la fonction extrait tout entre ces deux marqueurs :

`=REGEXEXTRACT(D9,".*/d/(.*)/")`

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-9.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-10.png)
_Cela extrait tout entre le /d/ et le /_

## Comment utiliser la fonction IMAGE 📷

D'accord. Nous avons compris les pièces disparates. Je sais que les pièces s'emboîtent. 🎵 

Mettons-les ensemble.

Tout notre travail était de faire en sorte qu'une cellule ( `B4` ) fournisse des données à la fonction `IMAGE`.

Image prend un argument et trois autres optionnels : 

```javascript
 IMAGE(url, [mode], [height], [width])
```

Nous construisons l'URL en combinant le début requis de l'URL que j'ai dans `J17` en utilisant l'opérateur esperluette (&) avec notre fonction `REGEXEXTRACT`. Et dans notre fonction `REGEXEXTRACT`, nous utilisons notre fonction `VLOOKUP` pour obtenir l'URL de l'image que nous avons sélectionnée dans la cellule `itemSelect`.

Ouf. 

Mais c'est cool, non ?!

![Image](https://www.freecodecamp.org/news/content/images/2022/08/giphy-1.gif)

Si vous vous sentez perdu dans un cauchemar récursif, je vous encourage à ouvrir la [**feuille de calcul d'exemple**](https://docs.google.com/spreadsheets/d/1rFU2gPy6rU8IKFDmsxKHYCf0KGVHkcumQ5O5QCf156M/edit?usp=sharing) et à examiner les parties de la fonction dans `F4` pièce par pièce. 👍

## Comment formater votre feuille FTW 🎯

Ces quelques détails peuvent **augmenter le volume 📛** sur une feuille de calcul autrement banale.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/nin2.gif)
_C'est probablement le seul endroit où vous trouverez un gif de NIN dans un article sur les feuilles de calcul aujourd'hui._

J'adore une ombre portée dure, et nous pouvons l'obtenir en manipulant les tailles de lignes et de colonnes autour d'une cellule ou d'une plage particulière, en utilisant l'option de fusion de cellules pour notre plage principale, puis en utilisant une couleur de remplissage autour du côté droit et du bas.

Cliquez sur les lignes entre les en-têtes de colonne pour faire glisser et ajuster les largeurs et hauteurs des colonnes et des lignes.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/width.png)

Les cellules sont le principal attrait des feuilles de calcul, mais dans certains cas, masquer les lignes de grille peut faire ressortir votre feuille. J'ai opté pour cette approche dans ce projet. 

Sélectionnez Affichage->Afficher->Lignes de grille.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/gridlines.png)

Autant j'apprécie Arial, je choisis généralement une autre police que celle par défaut immédiatement. 

Cliquez sur le menu déroulant Police dans la barre d'outils. Il est généralement en plein milieu :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/fonts.png)

Et choisissez simplement la police que vous souhaitez.

Voilà !

## Merci d'avoir lu ! 👋

Suivez-moi sur Twitter pour voir plus de contenu comme celui-ci : [https://twitter.com/EamonnCottrell](https://twitter.com/EamonnCottrell)

Merci !

![Image](https://www.freecodecamp.org/news/content/images/2022/08/thankyou.gif)