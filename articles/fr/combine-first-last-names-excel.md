---
title: Comment combiner prénom et nom de famille dans Excel
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-04-21T19:16:31.000Z'
originalURL: https://freecodecamp.org/news/combine-first-last-names-excel
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/article-iamge-combine-first-last-name.png
tags:
- name: excel
  slug: excel
- name: how-to
  slug: how-to
seo_title: Comment combiner prénom et nom de famille dans Excel
seo_desc: 'In Excel, you might have a column with first names and a column with last
  names that you want to join. In this tutorial I will explain how you can easily
  accomplish this.

  Let''s say we have the list of first names in column A and the list of last name...'
---

Dans Excel, vous pouvez avoir une colonne avec des prénoms et une colonne avec des noms de famille que vous souhaitez joindre. Dans ce tutoriel, je vais expliquer comment vous pouvez facilement accomplir cela.

Supposons que nous avons la liste des prénoms dans la colonne A et la liste des noms de famille dans la colonne B, et que nous voulons les joindre dans la colonne D. Nous devrons utiliser la fonction `CONCAT` d'Excel pour cela.

La fonction `CONCAT` accepte une liste ou une plage de chaînes de texte et les concatène (ou les combine) pour créer une nouvelle valeur continue. Ainsi, elle vous permet de combiner les informations des deux colonnes en une nouvelle colonne.

## Comment utiliser CONCAT dans Excel

Dans la première cellule de la colonne D, nous écrivons `=CONCAT(A1, " ", B1)`. Il s'agit de la syntaxe pour créer la nouvelle chaîne composée du prénom (`A1`), puis d'un espace (`" "`), puis du nom de famille (`B1`).

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-84.png)

Ainsi, au lieu d'avoir "Harry" et "Potter" dans deux cellules différentes, Excel nous donnera une nouvelle colonne avec "Harry Potter" comme nous le voulions.

Si vous souhaitez appliquer cela à plus d'une ligne, vous pouvez copier cette formule et la coller dans toutes les cellules en dessous. Ou vous pouvez cliquer sur la poignée verte dans le coin inférieur droit de la cellule et la faire glisser pour que la bordure verte entoure toutes les cellules dans lesquelles nous voulons appliquer cette formule. Lorsque vous relâchez, Excel appliquera `CONCAT` à toutes les cellules que vous avez surlignées.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-87.png)

### Problèmes de compatibilité avec CONCAT

La fonction `CONCAT` a été ajoutée dans Excel 2016. Donc, si vous utilisez une version antérieure d'Excel, vous devez utiliser `CONCATENATE` à la place.

Elle présente quelques légères différences, mais pour cette situation, vous pouvez suivre les instructions ci-dessus et simplement substituer `CONCATENATE` directement chaque fois que `CONCAT` était utilisé et cela vous donnera les mêmes résultats.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-88.png)

## Conclusion

Dans ce tutoriel, nous avons appris à utiliser la fonction `CONCAT` d'Excel ainsi que son prédécesseur, `CONCATENATE`. Nous avons utilisé cette fonction pour joindre une liste de prénoms et de noms de famille afin d'obtenir une liste de noms complets.