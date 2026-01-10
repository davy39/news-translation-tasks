---
title: AutoSum Excel – Comment additionner des nombres avec la formule Sum
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-03-02T23:48:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-numbers-in-excel-with-the-excel-sum-formula
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6037ad25a675540a229236b5.jpg
tags:
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
- name: spreadsheets
  slug: spreadsheets
seo_title: AutoSum Excel – Comment additionner des nombres avec la formule Sum
seo_desc: 'The SUM() formula in Excel is used to add together the content of two or
  more cells. It takes the cell names and gives back the result of the sum.

  Let''s apply the SUM formula so we can see it in action. Say that you''re organizing
  a party, and differe...'
---

La formule `SUM()` dans Excel est utilisée pour additionner le contenu de deux cellules ou plus. Elle prend les noms des cellules et retourne le résultat de la somme.

Appliquons la formule `SUM` pour la voir en action. Supposons que vous organisez une fête et que différentes personnes apportent des ballons de différentes couleurs. Vous enregistrerez dans un tableau combien de ballons de chaque couleur chaque personne apporte.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-181.png)

## Comment additionner les cellules d'une colonne

Tout d'abord, nous voulons savoir combien de ballons de chaque couleur les gens ont apportés à la fête.

Ainsi, sur la base du tableau ci-dessus, pour savoir combien de ballons bleus nous avons, nous pouvons écrire la formule `SUM` dans la cellule `C6`. Ensuite, nous écrivons les cellules que nous voulons additionner comme `C3:C5`, ce qui sera interprété comme "toutes les cellules de `C3` à `C5`". Nous aurons donc `=SUM(C3:C5)`.

Nous pouvons faire la même chose pour les ballons verts et blancs également - nous écrivons les cellules `D3:D5` pour les verts et `E3:E5` pour les blancs.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sum-columns-colored.png)

## Comment additionner les cellules d'une ligne

Ensuite, nous voulons savoir combien de ballons chaque personne a apportés. Pour savoir combien de ballons Marisa a apportés, nous pouvons écrire la formule `SUM` dans la cellule `F3`, et écrire les cellules que nous voulons additionner comme `C3:E3`. Cela sera interprété comme "toutes les cellules de `C3` à `E3`", ce qui nous donne `=SUM(C3:E3)`.

De même, pour les ballons d'Oliver, nous écrivons les cellules `C4:E4` et pour les ballons d'Alex `C5:E5`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sum-rows-colored.png)

## Comment additionner les cellules d'un bloc

La dernière chose que nous voulons apprendre à faire est de déterminer combien de ballons nous avons au total.

Pour cela, nous devons additionner tous les ballons que nous avons. Nous écrivons le bloc de cellules comme `C3:E5`, ce qui sélectionnera toutes les cellules dans le rectangle avec `C3` dans le coin supérieur gauche et `E5` dans le coin inférieur droit.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sum-block-coloured.png)

## Comment additionner les cellules dans différents intervalles

Si nous voulons connaître la somme de différents intervalles de données qui ne sont pas proches les uns des autres (par exemple, combien de ballons bleus et blancs nous avons au total), nous pouvons utiliser la formule `SUM` en séparant les intervalles de données par des virgules.

Ainsi, puisque `C3:C5` est l'intervalle pour les ballons bleus, et `E3:E5` est l'intervalle pour les ballons blancs, nous pouvons écrire `=SUM(C3:C5,E3:E5)`. De plus, comme nous savons déjà combien de ballons bleus nous avons au total et combien de ballons blancs nous avons au total, nous pouvons additionner les deux totaux avec `=SUM(C6,E6)`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/sum-intervals-colored.png)

## Comment additionner des cellules en sélectionnant les données avec la souris

Jusqu'à présent, nous avons tapé les noms des cellules pour les sélectionner. Mais Excel permet également de sélectionner les cellules à utiliser dans la formule avec la souris.

Une fois que vous avez écrit `=SUM(`, vous pouvez sélectionner les cellules - si vous souhaitez sélectionner plusieurs intervalles, vous pouvez simplement maintenir la touche `Ctrl` enfoncée. Une fois que vous avez terminé, vous pouvez appuyer sur `Entrée` et la somme des cellules sélectionnées sera calculée.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-182.png)

## Comment additionner des cellules en utilisant AutoSum

Il existe un outil dans Excel qui permet de faire des sommes simples avec un clic, appelé AutoSum. Vous pouvez le trouver dans le menu Accueil, et il a le symbole de la lettre grecque sigma majuscule (Σ).

Avec cet outil, vous pouvez, à partir de la situation de la première image avant qu'aucun calcul n'ait été effectué, sélectionner les trois cellules `F3`, `F4` et `F5`, appuyer sur le bouton AutoSum, et il remplira immédiatement les cellules avec les sommes des cellules à gauche (le même résultat que nous avons obtenu lorsque nous avons additionné les cellules d'une ligne).

Vous pouvez également sélectionner les trois cellules `C6`, `D6` et `E6` et appuyer sur AutoSum pour obtenir les sommes des cellules au-dessus (le même résultat que lorsque nous avons additionné les cellules d'une colonne).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/autosum.png)

Alternativement, l'outil AutoSum peut être utilisé comme un raccourci pour écrire la formule `SUM` : lorsque vous sélectionnez une seule cellule et appuyez sur le bouton AutoSum, la cellule est remplie avec la formule `SUM`. Ensuite, vous pouvez sélectionner les cellules à additionner avec la souris ou écrire l'intervalle des cellules à additionner à l'intérieur des parenthèses de la formule.

Si la cellule sélectionnée est proche d'autres cellules remplies, la formule `SUM` peut être pré-remplie avec une suggestion de cellules à additionner.

## Conclusion

La formule `SUM()` permet d'additionner des cellules. Pour déterminer quelles cellules additionner, vous pouvez taper leurs noms en tant qu'argument de la formule `SUM()`, ou vous pouvez les sélectionner avec votre souris après avoir tapé le nom de la formule et la parenthèse ouvrante. La formule peut également être utilisée avec l'outil AutoSum.