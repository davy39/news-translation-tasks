---
title: Numérotation automatique dans Excel – Comment numéroter les cellules automatiquement
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-03-01T15:59:33.000Z'
originalURL: https://freecodecamp.org/news/auto-numbering-in-excel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6037a8a2a675540a2292367b.jpg
tags:
- name: excel
  slug: excel
- name: how-to
  slug: how-to
- name: Productivity
  slug: productivity
seo_title: Numérotation automatique dans Excel – Comment numéroter les cellules automatiquement
seo_desc: "Numbering cells is a task often you'll often perform in Excel. But writing\
  \ the number manually in each cell takes a lot of time. \nFortunately, there are\
  \ methods that help you add numbers automatically. And in this article, I'll show\
  \ you two methods o..."
---

Numéroter les cellules est une tâche que vous effectuerez souvent dans Excel. Mais écrire le numéro manuellement dans chaque cellule prend beaucoup de temps. 

Heureusement, il existe des méthodes qui vous aident à ajouter des numéros automatiquement. Et dans cet article, je vais vous montrer deux méthodes pour le faire : la première est une méthode simple, et la seconde vous permet d'avoir des cellules numérotées dynamiquement. Alors, commençons.

# Comment numéroter automatiquement les cellules avec un motif régulier

Pour cette méthode, vous définissez votre numéro de départ dans une cellule et le numéro suivant de la série dans la cellule suivante.

Une fois que vous avez deux cellules adjacentes remplies avec vos deux numéros de départ, vous pouvez sélectionner ces deux cellules, cliquer sur la poignée dans le coin inférieur droit du contour vert, et faire glisser pour sélectionner toutes les cellules que vous souhaitez suivre votre motif. 

Une info-bulle utile apparaît près du coin inférieur droit du contour vert pour montrer quel serait le dernier numéro de la série si vous relâchiez à ce moment-là.

Ainsi, si vous souhaitez commencer par le numéro 5 et incrémenter de 3 jusqu'à 38, vous écriviez 5 dans votre première cellule, et 8 dans la cellule suivante. Vous sélectionneriez ensuite les cellules contenant le 5 et le 8, cliqueriez sur la poignée, et feriez glisser pour sélectionner les autres cellules jusqu'à ce que vous voyiez `38` apparaître dans l'info-bulle. Ensuite, vous pouvez relâcher, et les numéros seront remplis automatiquement. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/excel-autonumbering.png)
_1) Sélectionnez les cellules. 2) Faites glisser la poignée sur le contour (vous pouvez également voir l'info-bulle avec le dernier numéro de la série) 3) Relâchez_

Les numéros peuvent également être formatés dans l'ordre décroissant : si vous commencez par 7 puis entrez 5, le motif continuera avec 3, 1, -1, et ainsi de suite.

Vous pouvez également faire de même avec des lignes au lieu de colonnes. Remplissez deux cellules consécutives dans une ligne avec le début de votre motif, puis sélectionnez-les et faites glisser le contour horizontalement sur les cellules que vous souhaitez continuer ce motif. Il remplira automatiquement ces numéros.

Vous pouvez également faire de même en remontant – remplissez deux cellules, sélectionnez-les, cliquez sur la poignée et faites glisser vers le haut pour remplir les cellules au-dessus de vos deux cellules de départ.

Note : cela ajoutera toujours des numéros qui sont régulièrement espacés dans le motif que vous avez commencé. Cela ne fonctionnera pas avec d'autres types de progressions numériques.

# Comment numéroter automatiquement les cellules en utilisant la fonction ROW()

Si vous avez des données qui peuvent être triées de différentes manières (par exemple, une liste de noms - par ordre alphabétique, etc.), il est ennuyeux si la numérotation de vos lignes se mélange lorsque vous triez d'autres données. 

Pour éviter cela, vous pouvez numéroter dynamiquement vos lignes en utilisant la fonction `ROW()`.

Dans la cellule où vous souhaitez que la numérotation commence, écrivez `=ROW(A1)`. Cela produira le numéro 1 dans la cellule. 

Sélectionnez la cellule et faites glisser le contour à partir de la poignée dans le coin pour remplir la même formule dans le reste des cellules (ou, si vous ajoutez les numéros de ligne près d'un bloc de données déjà présent, vous pouvez simplement double-cliquer sur la poignée dans le coin de la sélection).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/auto-number-row-function.png)
_1) Écrivez `=ROW(A1)` dans votre première cellule, 2) Cela apparaîtra comme le numéro `1`, 3) Cliquez et faites glisser ou double-cliquez pour remplir toutes les autres cellules. 4) Maintenant, si vous triez les données, les numéros de ligne resteront dans l'ordre._

Si vous souhaitez avoir un motif régulier différent, vous pouvez utiliser un peu de mathématiques : pour avoir des numéros espacés de 2, vous pouvez écrire `=ROW(A1) * 2` dans la première cellule, puis procéder aux mêmes étapes que ci-dessus. Cela produira les numéros 2, 4, 6... et ainsi de suite.

Si vous souhaitez changer le point de départ du motif – pour peut-être avoir uniquement des numéros impairs, par exemple – vous pouvez soustraire un : `=ROW(A1) * 2 - 1`, cela produira les numéros 1, 3, 5, 7...

En tant que formule générale, pour obtenir n'importe quel motif, vous pouvez écrire `=ROW(A1) * a + b`. `a` est utilisé pour déterminer le pas, et `b` (il peut s'agir d'un nombre positif ou négatif) est utilisé pour changer le point de départ du motif.

Si vous souhaitez numéroter vos colonnes, vous pouvez utiliser la fonction `COLUMN()` de la même manière que la fonction `ROW()`. Il suffit de remplir votre première cellule avec `=COLUMN(A1)`, de sélectionner la cellule, puis d'étendre la sélection au reste des cellules où vous souhaitez que vos numéros soient.

**Note** : si vous ajoutez ou supprimez des lignes, vous devrez réinitialiser la numérotation automatique en sélectionnant la première cellule et en faisant glisser ou en double-cliquant à nouveau pour restaurer le motif.

# Conclusion

Écrire des numéros dans des cellules est une tâche souvent effectuée dans Excel, et ici nous avons vu deux méthodes simples qui nous permettent de gagner du temps. La première méthode consiste simplement à écrire des numéros dans deux cellules, puis à effectuer quelques clics. Et l'autre nécessite simplement d'écrire une formule dans une cellule, puis quelques clics.

Il existe quelques autres méthodes pour numéroter des cellules dans Excel, mais ce sont les plus simples.