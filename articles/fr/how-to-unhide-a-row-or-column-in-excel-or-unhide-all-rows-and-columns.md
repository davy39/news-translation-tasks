---
title: Comment afficher une ligne ou une colonne dans Excel – Ou tout afficher
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-02-23T22:45:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-unhide-a-row-or-column-in-excel-or-unhide-all-rows-and-columns
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/unhideExcel.png
tags:
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
- name: VBA
  slug: vba
seo_title: Comment afficher une ligne ou une colonne dans Excel – Ou tout afficher
seo_desc: "If you’re working with a spreadsheet that contains sensitive or private\
  \ data, then some rows and columns might be hidden. You might also need to hide\
  \ unimportant information or data you don’t want others to see in your own spreadsheet.\
  \ \nIn these case..."
---

Si vous travaillez avec une feuille de calcul contenant des données sensibles ou privées, certaines lignes et colonnes peuvent être masquées. Vous pourriez également avoir besoin de masquer des informations ou des données non importantes que vous ne souhaitez pas que d'autres voient dans votre propre feuille de calcul. 

Dans ces cas, vous devrez peut-être afficher ces lignes et colonnes masquées avant de commencer à mettre à jour la feuille de calcul et d'examiner les données qu'elle contient.

Dans cet article, vous apprendrez comment afficher des lignes et des colonnes dans Excel. Vous apprendrez également comment afficher toutes les lignes et colonnes au cas où elles seraient toutes masquées.

Ce tutoriel est applicable à Excel 2007 à 2016, mais il peut également vous guider pour le faire dans d'autres versions d'Excel.

## Ce que nous allons couvrir
- [Comment trouver les lignes et colonnes masquées](#heading-comment-trouver-les-lignes-et-colonnes-masquees)
- [Comment afficher une colonne dans Excel](#heading-comment-afficher-une-colonne-dans-excel)
- [Comment afficher une ligne dans Excel](#heading-comment-afficher-une-ligne-dans-excel)
- [Comment afficher toutes les lignes et colonnes masquées dans l'onglet Accueil](#heading-comment-afficher-toutes-les-lignes-et-colonnes-masquees-dans-longlet-accueil)
- [Comment afficher toutes les lignes et colonnes en une fois avec une macro VBA](#heading-comment-afficher-toutes-les-lignes-et-colonnes-en-une-fois-avec-une-macro-vba)
- [Conclusion](#heading-conclusion)

Avant de plonger dans la façon d'afficher des lignes et des colonnes dans Excel, voyons comment trouver les lignes et colonnes masquées.


## Comment trouver les lignes et colonnes masquées
Vous pouvez détecter une ligne ou une colonne masquée en regardant les lignes qui séparent chaque ligne et chaque colonne. Si les lignes sont doubles ou vertes, cela signifie qu'il y a une ligne ou une colonne masquée.

![Screenshot-2023-02-23-at-11.49.19](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-11.49.19.png)

De plus, en regardant la feuille de calcul, si des lettres sont manquantes pour les colonnes ou des numéros pour les lignes, il est possible qu'il y ait des lignes et colonnes masquées dans la feuille de calcul.

![Screenshot-2023-02-23-at-11.49.43](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-11.49.43.png) 


## Comment afficher une colonne dans Excel
Vous pouvez afficher une certaine colonne en faisant un clic droit sur la double ligne qui indique la colonne masquée et en sélectionnant « afficher »:

![Screenshot-2023-02-23-at-11.56.27](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-11.56.27.png) 

![Screenshot-2023-02-23-at-13.04.02](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-13.04.02.png)


## Comment afficher une ligne dans Excel
Si vous souhaitez afficher une ligne, faites un clic droit sur la double ligne indiquée en vert (ou, si possible, une autre couleur selon les paramètres de l'utilisateur), puis sélectionnez « afficher »:

![Screenshot-2023-02-23-at-12.01.11](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-12.01.11.png)

![Screenshot-2023-02-23-at-13.08.06](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-13.08.06.png) 


## Comment afficher toutes les lignes et colonnes masquées dans l'onglet Accueil
Pour afficher toutes les lignes, sélectionnez toutes les lignes et colonnes en appuyant sur CTRL + A, allez dans l'onglet `Accueil`, localisez les cellules et cliquez sur la flèche de "Format" :

![Screenshot-2023-02-23-at-12.07.16](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-12.07.16.png)

Sous visibilité, survolez "Masquer et afficher", puis sélectionnez "Afficher les lignes" :

![Screenshot-2023-02-23-at-12.08.14](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-12.08.14.png)

Pour afficher toutes les colonnes masquées, vous devez suivre le même processus, mais cette fois-ci, vous devez sélectionner "Afficher les colonnes".


## Comment afficher toutes les lignes et colonnes en une fois avec une macro VBA
Si vous travaillez avec une grande feuille de calcul, les processus que nous venons de discuter peuvent être fastidieux pour vous. 

Au lieu d'afficher les lignes et colonnes une par une ou d'afficher les lignes et d'afficher les colonnes, vous pouvez exécuter un code VBA (Visual Basic for Applications) pour le faire.

Voici comment exécuter du code VBA dans Excel :

Appuyez sur ALT + F11 (ou Option + F11 sur Mac) pour ouvrir le VBE (Visual Basic Editor) :

![Screenshot-2023-02-23-at-12.31.01](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-12.31.01.png)

Faites un clic droit sur votre classeur actuel, survolez "Insérer" et sélectionnez "Module" :

![Screenshot-2023-02-23-at-12.32.53](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-12.32.53.png)

Collez ce code dans l'éditeur :

```bas
Sub UnhideAllRowsAndColumns()
  Cells.EntireColumn.Hidden = False
  Cells.EntireRow.Hidden = False
End Sub
```

Fermez la boîte de dialogue et retournez à votre feuille de calcul. 

Ensuite, vous devez exécuter la macro VBA. Appuyez sur ALT + F8 et vous verrez quelque chose comme ceci :

![Screenshot-2023-02-23-at-12.38.39](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-12.38.39.png)

Développez-le et cliquez sur "Exécuter" :

![Screenshot-2023-02-23-at-12.40.04](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-12.40.04.png)

Toutes les lignes et colonnes devraient maintenant s'afficher :

![Screenshot-2023-02-23-at-13.03.28](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-23-at-13.03.28.png) 


## Conclusion
Cet article vous a montré comment afficher une ligne ou une colonne dans Excel. 

Les exemples que nous avons examinés vous ont montré comment afficher des lignes et colonnes individuelles, afficher toutes les colonnes et afficher toutes les lignes. 

Nous avons également vu comment vous pouvez afficher les lignes et colonnes ensemble avec l'éditeur VBA (Visual Basic Editor) d'Excel.

Si vous trouvez cet article utile, partagez-le avec vos amis et votre famille.