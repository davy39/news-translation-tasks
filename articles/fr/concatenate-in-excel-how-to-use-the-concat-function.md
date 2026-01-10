---
title: Concaténer dans Excel – Comment utiliser la fonction Concat
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-05-12T19:26:13.000Z'
originalURL: https://freecodecamp.org/news/concatenate-in-excel-how-to-use-the-concat-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-yan-krukov-7693224.jpg
tags:
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: Concaténer dans Excel – Comment utiliser la fonction Concat
seo_desc: 'Excel has many useful functions that you can use to work with your data.

  In this guide you will learn about the CONCAT function and how to use it.

  Concatenation just means to join two things together. And in Excel, you can use
  the CONCAT function to ...'
---

Excel dispose de nombreuses fonctions utiles que vous pouvez utiliser pour travailler avec vos données.

Dans ce guide, vous apprendrez à connaître la fonction `CONCAT` et comment l'utiliser.

La concaténation signifie simplement joindre deux choses ensemble. Et dans Excel, vous pouvez utiliser la fonction `CONCAT` pour joindre des données de plusieurs cellules en une seule cellule. Voyons comment cela fonctionne.

## Syntaxe de la fonction CONCAT

La syntaxe générale de la fonction CONCAT est :

```text
=CONCAT(texte1; [texte2; ...])
```

Où les arguments sont :

* `texte1` est un argument requis qui peut être une chaîne ou un tableau de chaînes (comme une plage de cellules).
* `[texte2, ...]` identifie les arguments facultatifs qui suivent. Il peut y avoir jusqu'à 253 arguments de texte, et chacun peut également être une chaîne ou un tableau de chaînes (comme une plage de cellules).

## Comment utiliser la fonction CONCAT dans Excel

Pour utiliser la fonction CONCAT, vous devrez cliquer sur la cellule dans laquelle vous souhaitez que le résultat apparaisse, et taper `=CONCAT(` là.

Après cela, vous pouvez cliquer sur les cellules, ou la plage de cellules, que vous souhaitez concaténer (ou joindre) ensemble – vous devrez garder le bouton Ctrl enfoncé pour ajouter plusieurs arguments.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-67.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-68.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-69.png)

Comme vous pouvez le voir dans ces captures d'écran, nous écrivons `=CONCAT(` dans la cellule D1 puis nous cliquons sur les cellules A1 et B1 tout en gardant Ctrl enfoncé. Après cela, appuyer sur Entrée donnera le résultat dans la cellule D1.

Si vous souhaitez ajouter du texte entre le contenu des différentes cellules, par exemple un espace, vous pouvez cliquer sur une cellule, puis taper un point-virgule et le texte que vous souhaitez ajouter entre guillemets, puis un autre point-virgule, et enfin cliquer sur la cellule suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-70.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-71.png)

Dans ce cas, vous écriviez `=CONCAT(` dans la cellule D1, puis vous cliquez sur la cellule A1, tapez un point-virgule, puis tapez l'espace entouré de chaînes, `" "`, suivi d'un autre point-virgule, et enfin cliquez sur la cellule B1. Cela donnera "Leonardo da Vinci" dans la cellule D1.

**Note :** Vous pouvez concaténer jusqu'à 32 767 caractères, ce qui est la limite de la cellule. Si la chaîne résultante est plus longue que 32 767 caractères, la fonction renverra une erreur `#VALUE!`.

## Exemples

La [documentation officielle de Microsoft](https://support.microsoft.com/en-us/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2) propose trois exemples utiles sur l'utilisation de la fonction `CONCAT`. Examinons-les.

### Exemple 1 de CONCAT :

| =CONCAT(B:B; C:C) | A's | B's |
| ---  | --- | --- |
| | a1 | b1 |
| | a2 | b2 |
| | a4 | b4 |
| | a5 | b5 |
| | a6 | b6 |
| | a7 | b7 |

Si vous souhaitez suivre, copiez ce tableau et collez ses données dans la cellule A1 d'une nouvelle feuille Excel.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-75.png)

Cette fonction permet de faire référence à une colonne entière, donc dans la formule `=CONCAT(B:B; C:C)` vous concaténez toute la colonne B (`B:B`) suivie de toute la colonne C (`C:C`), donc le résultat est `A'sa1a2a4a5a6a7B'sb1b2b4b5b6b7` – les cellules vides ne contribuent pas au résultat final.

### Exemple 2 de CONCAT :

| =CONCAT(B2:C8)	| A's	| B's |
| --- | --- | --- |
| |a1|	b1|
||	a2|	b2|
||	a4|	b4|
||a5|	b5|
||	a6|	b6|
||a7|	b7|


Pour suivre, copiez ce tableau et collez-le dans la cellule A1 d'une feuille Excel vide.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-76.png)

Dans ce cas, ce sont les cellules de la plage `B2:C8` (la plage mise en évidence dans l'image) qui sont concaténées ensemble, et la formule dans la cellule A1 donnera `a1b1a2b2a4b4a5b5a6b6a7b7`. Ici aussi, les cellules vides ne contribuent pas au résultat.

**Note :** Les cellules d'une plage sont lues ligne par ligne, donc les cellules sont concaténées dans l'ordre : `B2;C2;B3;C3;B4;C4;B5;C5;B6;C6;B7;C7;B8;C8` (avec B8 et C8 étant vides, donc ne contribuant pas au résultat final).

### Exemple 3 de CONCAT

Cet exemple contient divers exemples, tous avec le thème général de joindre des cellules avec d'autres textes. Cet exemple illustre bien comment vous pouvez faire beaucoup de choses avec la fonction Concat.

Examinons cela.

| Données | Prénom | Nom |
| --- | --- | --- |
| truite de ruisseau | Andreas | Hauser |
| espèce | Fourth | Pine |
| 32 | | |	
| **Formule** | **Description** | **Résultat** |
| `=CONCAT("Population de ruisseau pour "; A2;" "; A3; " est "; A4; "/mile.")` | Crée une phrase en joignant les données de la colonne A avec d'autres textes. | Population de ruisseau pour l'espèce truite de ruisseau est 32/mile. |
| `=CONCAT(B2;" "; C2)` | Joint trois choses : la chaîne dans la cellule B2, un caractère d'espace, et la valeur dans la cellule C2. | Andreas Hauser |
| `=CONCAT(C2; ", "; B2)` | Joint trois choses : la chaîne dans la cellule C2, une chaîne avec une virgule et un caractère d'espace, et la valeur dans la cellule B2. | Hauser, Andreas |
| `=CONCAT(B3; " & "; C3)` | Joint trois choses : la chaîne dans la cellule B3, une chaîne composée d'un espace avec un esperluette et un autre espace, et la valeur dans la cellule C3. | Fourth & Pine |
| `=B3 & " & " & C3` | Joint les mêmes éléments que l'exemple précédent, mais en utilisant l'opérateur de calcul esperluette (&) au lieu de la fonction CONCAT. | Fourth & Pine |


Pour suivre, vous pouvez également copier ce tableau dans la cellule A1 d'une feuille Excel vide.

#### Population de ruisseau pour l'espèce truite de ruisseau est 32/mile.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-77.png)

La première formule montrée dans cet exemple joint le texte de trois cellules (A2, A3 et A4) avec quelques chaînes pour former une phrase plus longue.

Ainsi, le résultat est donné par la combinaison de la chaîne `"Population de ruisseau pour "` avec le contenu de la cellule A2, donc `"truite de ruisseau"`, qui est ensuite suivi d'un espace (`" "`), le contenu de la cellule A3 (`"espèce"`), la chaîne `" est "`, le contenu de la cellule A4 (`32`), et enfin, la chaîne `"/mile."`. 

Ensemble, cela donne la chaîne `"Population de ruisseau pour l'espèce truite de ruisseau est 32/mile."`.

(Pour les captures d'écran suivantes, j'ai masqué les lignes des formules dont j'ai déjà parlé).

#### Andreas Hauser

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-78.png)

Dans cet exemple, la formule `=CONCAT(B2; " "; C2)` joint la chaîne de la cellule B2, un espace `" "` et la chaîne de la cellule C2, donnant `"Andreas Hauser"`.

#### Hauser, Andreas

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-79.png)

Dans cet exemple, vous pouvez voir que l'ordre dans lequel les cellules sont écrites dans les arguments de la fonction `CONCAT` compte. La formule `=CONCAT(C2; ", "; B2)` joint les chaînes de la cellule C2, une virgule et un espace `", "` et de la cellule B2, donnant `"Hauser, Andreas"`. 

Les chaînes des cellules C2 et B2 ont été jointes dans un ordre différent car elles ont été écrites dans un ordre différent dans les arguments de la méthode.

#### Fourth & Pine

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-80.png)

Vous pouvez joindre n'importe quel type d'écran. Voyez ici où la formule `=CONCAT(B3; " & "; C3)` joint la chaîne de la cellule B3 avec la chaîne de la cellule C3 en mettant au milieu des deux la chaîne avec un espace, un esperluette et un autre espace, `" & "` donnant `"Fourth & Pine"`. 

#### Fourth & Pine (II)

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-81.png)

Cet exemple montre une méthode alternative de concaténation de chaînes : en utilisant l'opérateur `&` vous pouvez écrire la liste des chaînes que vous souhaitez joindre séparées par un esperluette (`&`). Donc `=B3 & " & " & C3` donne le même résultat que `=CONCAT(B3; " & "; C3)`.

**Note :** Vous pouvez utiliser l'opérateur `&` uniquement pour des cellules individuelles, il ne fonctionne pas pour les plages.

Et c'est tout ! Maintenant vous savez comment utiliser la fonction `CONCAT` dans Excel. Merci d'avoir lu !