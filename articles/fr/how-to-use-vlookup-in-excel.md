---
title: Comment utiliser VLOOKUP dans Excel
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-07-01T16:47:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-vlookup-in-excel
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/scott-graham-5fNmWej4tAA-unsplash.jpg
tags:
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment utiliser VLOOKUP dans Excel
seo_desc: 'When you''re working in Excel, the VLOOKUP function makes looking up information
  less time-consuming. This is particularly true when you''re using more than one
  Excel sheet.

  In this article, you will learn what the VLOOKUP function does, as well as und...'
---

Lorsque vous travaillez dans Excel, la fonction VLOOKUP rend la recherche d'informations moins chronophage. Cela est particulièrement vrai lorsque vous utilisez plus d'une feuille Excel.

Dans cet article, vous apprendrez ce que fait la fonction VLOOKUP, ainsi que la syntaxe qui la sous-tend. Vous apprendrez également comment utiliser la fonction VLOOKUP d'Excel pour rechercher une valeur à l'aide d'un exemple simple.

Commençons !

## Qu'est-ce que VLOOKUP dans Excel ? Définition de VLOOKUP

VLOOKUP est une fonction puissante de Microsoft Excel qui recherche et récupère des informations dans un tableau de données.

VLOOKUP signifie **Recherche Verticale**, donc le V dans VLOOKUP est l'abréviation de Vertical. 

Vertical dans Excel fait référence aux **colonnes** et, dans ce cas, à la recherche de données verticalement dans la feuille de calcul. 

Plus précisément, VLOOKUP recherche une valeur spécifique dans une colonne.

VLOOKUP recherche une information spécifique dans un ensemble de données et retourne des données supplémentaires liées à cette information initiale mais provenant d'une colonne différente dans la même ligne.

Par exemple, si vous avez une liste de noms et d'emails, VLOOKUP recherchera le nom d'une personne dans un tableau et récupérera son email. Ce sera l'entrée email associée à son nom.

Il est important de noter que VLOOKUP ne doit pas être confondu avec HLOOKUP - HLOOKUP est une fonction entièrement différente. 

HLOOKUP signifie Recherche Horizontale, et le H est l'abréviation de Horizontal. Horizontal dans Excel fait référence aux **lignes** et à la recherche de données horizontalement dans la feuille de calcul.

Pour en savoir plus sur les lignes et les colonnes dans Excel, lisez [ce guide rapide](https://www.freecodecamp.org/news/row-vs-column-in-excel-what-is-the-difference/) qui explique la différence entre les deux.

### Analyse de la syntaxe de la fonction VLOOKUP

La syntaxe générale de la fonction VLOOKUP est la suivante :

```
=VLOOKUP(valeur_recherche, tableau_matrice, numéro_colonne, [recherche_plage])
```

Vous commencez par écrire un signe égal, `=`, puis vous tapez la fonction `VLOOKUP()`.

La fonction VLOOKUP prend quatre arguments, et chaque argument est séparé par une virgule, `,`. 

Expliquons ce que signifie chaque argument :

- **valeur_recherche** : Cet argument est obligatoire et spécifie la valeur que vous souhaitez rechercher et localiser. Cette valeur se trouve dans le coin le plus à gauche et dans la première colonne du tableau. VLOOKUP recherchera toujours des informations à droite de cette `valeur_recherche`.
- **tableau_matrice** : Cet argument est obligatoire et représente la plage de données dans le tableau que vous souhaitez parcourir. La `valeur_recherche`, le `numéro_colonne` et la valeur de retour que vous souhaitez obtenir sont tous inclus dans cette plage.
- **numéro_colonne** : Cet argument est obligatoire. Il s'agit d'un nombre entier qui spécifie le numéro de colonne dans le `tableau_matrice` à partir duquel vous souhaitez récupérer la valeur de retour.
- **recherche_plage** : Cet argument est facultatif et peut être soit `VRAI` soit `FAUX`. `VRAI` spécifie que la fonction doit retourner une correspondance approximative, ce qui signifie que s'il n'y a pas de correspondance exacte, elle doit retourner la correspondance la plus proche possible. Et `FAUX` spécifie que la fonction doit retourner une correspondance exacte pour ce que vous recherchez, et si ce n'est pas le cas, cela entraînera une erreur. 

## Comment utiliser VLOOKUP dans Excel

Ci-dessous, j'ai un exemple d'un ensemble de données simple. 

Cet exemple vous donnera une idée de la manière dont vous pouvez utiliser la fonction VLOOKUP. Vous pouvez également appliquer les techniques utilisées ici à des tableaux plus grands et plus complexes.

![Screenshot-2022-06-29-at-10.06.00-AM](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-29-at-10.06.00-AM.png)

Je vais utiliser VLOOKUP pour rechercher dans un tableau de données d'employés. Ce tableau stocke le nom d'un employé, son numéro d'identification, le département dans lequel il travaille et son salaire. 

Je souhaite utiliser VLOOKUP pour rechercher un employé spécifique et obtenir son salaire correspondant.

Je veux que, chaque fois que je recherche le nom d'un employé dans la cellule `F2`, son salaire correspondant soit retourné.

Ainsi, si je voulais localiser l'employé `John Doe` et retourner son salaire, dans la colonne `F2`, j'écrirais :

```
=VLOOKUP(A3, A2:D5, 4, FAUX)
```

Décomposons cela :

- La cellule `A3` contient la valeur que je souhaite rechercher. L'employé nommé `John Doe` se trouve dans la cellule `A3`. Ce sera la valeur de recherche et le premier argument de la fonction.
- La plage de cellules `A2:D5` contient les données que je souhaite parcourir. C'est la source de données que VLOOKUP utilisera. Cette plage doit inclure la première colonne, qui stocke le premier argument, et elle doit également inclure la colonne où je souhaite que la valeur de retour soit stockée.
- Ensuite, j'inclus le numéro de colonne où la valeur de retour peut être trouvée. Gardez à l'esprit que vous devez commencer à compter où le tableau commence. Dans ce cas, il s'agit de la 4ème colonne du tableau.
- Enfin, je veux que VLOOKUP retourne une correspondance exacte, donc le dernier argument est `FAUX`.

Je vois ensuite le résultat dans la cellule `F2` :

![Screenshot-2022-07-01-at-5.13.50-PM](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-01-at-5.13.50-PM.png)


## Conclusion

Dans cet article, vous avez appris les bases de l'utilisation de la fonction VLOOKUP dans Excel.

Pour en savoir plus sur Excel, consultez les ressources suivantes :

- [Apprendre Microsoft Excel - Cours vidéo complet](https://www.freecodecamp.org/news/learn-microsoft-excel/)
- [Cours Excel en ligne – 11 cours de formation Excel gratuits](https://www.freecodecamp.org/news/excel-classes-online-free-excel-training-courses/)

Merci d'avoir lu !