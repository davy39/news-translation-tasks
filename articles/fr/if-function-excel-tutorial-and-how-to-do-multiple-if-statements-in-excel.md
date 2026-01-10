---
title: Tutoriel sur la fonction SI d'Excel – Et comment faire des instructions SI
  multiples dans Excel
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-03-26T17:34:46.000Z'
originalURL: https://freecodecamp.org/news/if-function-excel-tutorial-and-how-to-do-multiple-if-statements-in-excel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604b8922a7946308b768766f.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: excel
  slug: excel
seo_title: Tutoriel sur la fonction SI d'Excel – Et comment faire des instructions
  SI multiples dans Excel
seo_desc: 'The IF function in Excel is an inestimable ally when we need to implement
  conditional logic, that is when we need different results depending on a condition.

  The syntax is IF(logical_test, [value_if_true], [value_if_false]), where


  logical_test is an...'
---

La fonction `SI` dans Excel est une alliée inestimable lorsque nous devons implémenter une logique conditionnelle, c'est-à-dire lorsque nous avons besoin de résultats différents en fonction d'une condition.

La syntaxe est `SI(test_logique, [valeur_si_vrai], [valeur_si_faux])`, où

* `test_logique` est une expression qui évalue à `VRAI` ou `FAUX`,
* `valeur_si_vrai` est un argument optionnel, et c'est ce à quoi l'expression évalue si `test_logique` est vrai, et 
* `valeur_si_faux` est un argument optionnel qui détermine la valeur dans le cas où `test_logique` est faux.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-39.png)

## Comment définir conditionnellement la valeur d'une cellule dans Excel

Voyons l'instruction si en action dans le cas d'utilisation le plus simple, lorsque la valeur d'une cellule est déterminée entre deux options en fonction de la valeur d'une autre cellule.

Par exemple, supposons que nous avons une liste de projets, le pourcentage de progression de chacun d'eux, et nous voulons définir automatiquement la chaîne à "En cours" ou "Terminé". Alors nous pouvons écrire `SI(B2=100, "Terminé", "En cours")` (où `B2` est la première cellule avec la progression).

Après avoir écrit la formule dans la première cellule, nous pouvons simplement double-cliquer sur la poignée verte qui apparaît lorsque la cellule est sélectionnée et la formule se propagera à toutes les autres cellules de la colonne.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/single-if.png)

## Comment utiliser une instruction si imbriquée pour définir conditionnellement la valeur d'une cellule avec plus d'options dans Excel

En continuant à partir de l'exemple ci-dessus, nous pouvons vouloir décomposer le statut de progression encore plus. Cette fois, nous voulons avoir 7 chaînes de statut différentes en fonction de la progression du projet.

Nous devons utiliser des instructions si imbriquées, en écrivant une instruction si à la place de `valeur_si_faux` (elle peut être utilisée également à la place de `valeur_si_vrai` mais cela devient plus compliqué).

Essayons de construire une formule dans le cas où nous voulons avoir tous ces statuts de progression : Non commencé, Commencé, Première moitié, À mi-chemin, Deuxième moitié, Presque terminé, Terminé.

Dans ce cas, nous avons besoin d'un total de 6 instructions si, donc nous pourrions écrire quelque chose comme ceci :

```
=SI(B2=0, "Non commencé", SI(B2<10, "Commencé", SI(B2<50, "Première moitié", SI(B2=50, "À mi-chemin", SI(B2<90, "Deuxième moitié", SI(B2<100, "Presque terminé", "Terminé"))))))
```

Excel permet un maximum de 7 instructions si imbriquées. Si nous voulions étendre notre liste de statuts possibles, nous pourrions ajouter seulement une condition de plus et un statut de plus. Mais heureusement, nous pouvons en ajouter plus en utilisant une fonction différente.

## Comment utiliser `SI.CONDITIONS()` pour plus de 7 conditions dans Excel

La fonction `SI.CONDITIONS()` a été introduite dans Excel 2016, et elle permet jusqu'à 127 conditions. La syntaxe est `SI.CONDITIONS(test_logique1, valeur_si_vrai1, [test_logique2, valeur_si_vrai2] ... [test_logique127, valeur_si_vrai127])`.

Les expressions de test logique sont évaluées consécutivement. Lorsque la première qui retourne VRAI est trouvée, la `valeur_si_vrai` correspondante est donnée comme sortie.

L'expression précédente que nous avons écrite avec des instructions si imbriquées peut être écrite comme ceci :

```
=SI.CONDITIONS(B2=0, "Non commencé", B2<10, "Commencé", B2<50, "Première moitié", B2=50, "À mi-chemin", B2<90, "Deuxième moitié", B2<100, "Presque terminé", B2=100, "Terminé")
```

## Conclusion

Lorsque vous devez définir conditionnellement, vous utiliserez souvent `SI()`. Vous pouvez imbriquer plusieurs instructions `SI()` pour avoir des chaînes logiques complexes.

Mais si vous devez utiliser plus de 7 instructions `SI()` imbriquées, alors vous pouvez utiliser `SI.CONDITIONS()` à la place.