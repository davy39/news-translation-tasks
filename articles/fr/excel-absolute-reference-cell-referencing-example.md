---
title: Référence absolue Excel – Exemple de référence de cellule
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-05-16T17:29:50.000Z'
originalURL: https://freecodecamp.org/news/excel-absolute-reference-cell-referencing-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/spreadsheets-24956_1280.png
tags:
- name: data
  slug: data
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: Référence absolue Excel – Exemple de référence de cellule
seo_desc: 'In Excel, you can use both absolute and relative cell referencing to make
  calculations.

  Relative referencing is the default. So, for example, whenever you extend a formula
  down some cells, the cells change based on the relationships of the rows and c...'
---

Dans Excel, vous pouvez utiliser à la fois des références de cellule absolues et relatives pour effectuer des calculs.

La référence relative est celle par défaut. Ainsi, par exemple, chaque fois que vous étendez une formule vers le bas dans certaines cellules, les cellules changent en fonction des relations entre les lignes et les colonnes.

Que faire si vous souhaitez que chaque cellule soit verrouillée sur une certaine formule et ne change pas ? C'est là que vous devez utiliser la référence absolue.

Dans cet article, je vais vous montrer comment fonctionne la référence absolue dans Excel. Mais d'abord, vous devez savoir comment fonctionne la référence relative.

## Comment fonctionne la référence relative dans Excel

La référence relative est la référence par défaut dans Excel.

Lorsque vous entrez une formule dans une cellule et que vous l'étendez à d'autres cellules, ces autres cellules utilisent également la formule.

Dans l'illustration ci-dessous, j'ai calculé combien chaque footballeur gagne en un mois avec une référence relative :
![vid1](https://www.freecodecamp.org/news/content/images/2022/05/vid1.gif)

Si vous vérifiez la formule dans chaque cellule, vous découvrirez que la formule placée dans la cellule `D4` (`=D4*4`) a été étendue de manière relative à d'autres cellules (`D5` à `D14`).

Ainsi, la cellule `D5` utilise maintenant `D5*4`, `D6` utilise maintenant `D6*4`, et ainsi de suite.

Pour afficher les formules dans Excel, basculez vers le menu des formules, puis cliquez sur "afficher les formules" :
![ss1-2](https://www.freecodecamp.org/news/content/images/2022/05/ss1-2.png)

C'est ainsi que fonctionne la référence relative dans Excel.

## Référence absolue dans Excel

Si vous ne voulez pas que la formule change lorsque vous l'étendez vers le bas à travers diverses cellules, vous devrez utiliser la référence absolue.

La référence absolue est effectuée en préfixant les lignes et les colonnes avec un signe dollar. Par exemple, `$D$4`.

Si vous voulez seulement que la ligne soit fixe, faites-le comme ceci : `$D4`.

Si vous voulez seulement que la colonne soit fixe, faites-le comme ceci : `D$4`.

Rappelez-vous que si vous voulez faire une référence relative, vous tapez la formule `=D4*4` dans la cellule `E4` et vous l'étendez à la cellule `E5`. Ainsi, la formule devient `=D5*4`.

Mais si vous entrez la formule comme une référence absolue comme `=$D$5*4`, elle reste `=$D$5*4`.

Dans l'exemple ci-dessous, j'ai essayé de calculer les salaires payés avec les taxes en multipliant les salaires par le multiplicateur de taxe, mais je n'ai pas obtenu ce que je voulais :
![vid2](https://www.freecodecamp.org/news/content/images/2022/05/vid2.gif)

C'est parce que la référence relative est utilisée. Vous pouvez le confirmer à nouveau en vérifiant les formules :
![ss2-2](https://www.freecodecamp.org/news/content/images/2022/05/ss2-2.png)

Vous pouvez voir que la formule a changé vers le bas à partir de G8, et tout ce qui est en dessous de G8 n'existe pas dans la feuille.

Pour corriger cela, nous devons verrouiller la formule sur G8 en préfixant la ligne (G) et la colonne (8) avec des signes dollar. Ainsi, la formule devient `E4*$G$8`, `E5*$G$8`, `E6*$G$8`, et ainsi de suite.

Maintenant, cela fonctionne comme prévu :
![vid3](https://www.freecodecamp.org/news/content/images/2022/05/vid3.gif)

Si vous vérifiez les formules, elles restent toutes fixes sur `$G$8` :
![ss3-2](https://www.freecodecamp.org/news/content/images/2022/05/ss3-2.png)

## Conclusion

Cet article vous a montré comment la référence absolue est utilisée dans Excel et l'a comparée à un autre type de référence – la référence relative – afin que vous puissiez mieux la comprendre.

Si vous ne voulez pas que vos formules soient copiées dans d'autres cellules lorsque vous les étendez, alors vous devriez envisager d'utiliser la référence absolue.

Merci d'avoir lu.