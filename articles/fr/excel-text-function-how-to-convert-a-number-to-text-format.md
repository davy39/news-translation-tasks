---
title: Fonction Texte d'Excel – Comment convertir un nombre en format texte
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-07-30T22:22:23.000Z'
originalURL: https://freecodecamp.org/news/excel-text-function-how-to-convert-a-number-to-text-format
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/pexels-pixabay-534216.jpg
tags:
- name: excel
  slug: excel
- name: how-to
  slug: how-to
- name: Tutorial
  slug: tutorial
seo_title: Fonction Texte d'Excel – Comment convertir un nombre en format texte
seo_desc: "If you want to add a number to a text string, you can't do so directly\
  \ since the format isn't maintained. Also, a number added to a text string doesn't\
  \ have any formatting or all its decimal places. \nThe TEXT function comes in handy\
  \ here, as it allow..."
---

Si vous souhaitez ajouter un nombre à une chaîne de texte, vous ne pouvez pas le faire directement car le format n'est pas maintenu. De plus, un nombre ajouté à une chaîne de texte n'a aucun formatage ou toutes ses décimales. 

La fonction `TEXT` est utile ici, car elle vous permet de convertir un nombre en format texte avec un formatage spécifique. Ensuite, vous pouvez l'ajouter à une autre chaîne, et il sera dans le format que vous souhaitez.

## Comment utiliser la fonction `TEXT` dans Excel

Supposons que vous avez une série de nombres, et que vous voulez écrire un message incluant ces nombres. 

Voyons d'abord ce qui se passe sans utiliser la fonction TEXT. Tout d'abord, nous allons essayer d'utiliser la fonction `CONCAT` comme `=CONCAT("En ", A2, " il y avait un profit de ", B2)` puis remplir le reste de la colonne avec la même formule.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-108.png)

Ce n'est pas très beau, et les nombres sont tous différents les uns des autres. Cela est dû au fait que lorsque nous concaténons un nombre à une chaîne, le format est perdu.

Alors, utilisons plutôt `TEXT` pour faire une chaîne du nombre, puis l'ajouter à la chaîne.

`TEXT` prend deux arguments : le premier est le nombre que nous voulons convertir en chaîne, et le second est le format. Dans ce cas, le format que nous allons utiliser est `$##,##0.00` (nous verrons plus tard comment créer le format que nous voulons).

Supprimons tout le contenu de la colonne C et intitulons-la plutôt `Profit en format chaîne`. Nous allons écrire dans C2 `=TEXT(B2, "`$##,##0.00`")`, puis l'étendre au reste de la colonne.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-109.png)

Si vous créez à nouveau la chaîne en utilisant le nombre en format chaîne, cette fois les nombres restent dans le format que vous souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-110.png)

## Comment utiliser différents formats de nombres dans Excel

Nous venons de voir comment utiliser un format spécifique, `$##,##0.00`. Voyons maintenant ce que signifient les caractères afin que vous puissiez utiliser le format de nombre que vous souhaitez. Notez également que les nombres décimaux sont arrondis lorsque le format montre moins de décimales que ce que les nombres ont.

### Comment formater les nombres en décimaux

Le `0` est pour un nombre qui doit être présent – si le nombre converti n'a pas assez de chiffres, il y aura un `0`. Vous pouvez utiliser cela pour décider combien de décimales, de `0` finaux ou de `0` initiaux montrer. 

Par exemple, le nombre `12345.6` avec un format de `000000` sera affiché comme `012345` avec un `0` initial. Mais s'il est formaté comme `0.00`, il sera affiché comme `12345.60` avec un `0` final.

Le `#` est pour un nombre qui pourrait être présent mais aussi ne pas l'être. Vous pouvez l'utiliser, par exemple, pour montrer combien de nombres décimaux montrer au maximum. 

Par exemple, `12345.6` formaté comme `0.###` sera affiché comme `12345.6`. Mais `12345` sera affiché comme `12345.`, et `12345.6789` sera affiché comme `12345.679`, car le format est pour un maximum de 3 décimales.

Vous pouvez ajouter d'autres caractères au début, au milieu ou à la fin. Vous pouvez ajouter n'importe quels caractères sauf `,`, `.`, `?`, `0`, et `#`. La virgule agit comme séparateur de milliers, le point est un séparateur décimal, et les trois derniers symboles ont une signification spéciale dans le formatage (par exemple, le `?` est utilisé dans les fractions, voir ci-dessous).

Voici quelques exemples :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-119.png)

### Comment formater les nombres en fractions

Vous pouvez également formater les nombres en fractions. Dans le format de fraction, vous pouvez indiquer combien de chiffres le dénominateur doit avoir (ou spécifier un dénominateur). Vous pouvez également spécifier si la partie entière doit être écrite à l'intérieur de la fraction ou séparée.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-115.png)

Pour spécifier le nombre de chiffres dans le dénominateur de la fraction, vous pouvez utiliser le caractère `?`. Vous utilisez autant de `?` dans le dénominateur que le nombre de chiffres que vous voulez y avoir.

Ainsi, par exemple, `?/?` est pour un chiffre dans le dénominateur, `??/??` est pour deux chiffres, et ainsi de suite (notez que vous obtenez le même résultat avec `?/??` ou avec `??/??`).

Pour spécifier quel nombre doit être le dénominateur, vous pouvez l'écrire dans le format. Donc, si vous voulez une fraction en dix-neuvièmes, vous pouvez écrire `??/19`.

Pour séparer la partie entière de la fraction, vous pouvez écrire un `#` devant celle-ci, séparé par un espace, donc `# ??/19` ou `# ???/???`. Et si vous voulez que la partie entière soit toujours visible même si elle est nulle, vous pouvez écrire `0 ??/19` ou `0 ???/???` à la place.

## Conclusion

Ajouter des nombres à l'intérieur des chaînes est souvent utile pour écrire des rapports. Mais si vous voulez garder le nombre dans un format spécifique, vous devez utiliser la fonction `TEXT`. 

Dans cet article, vous avez appris comment formater un nombre en tant qu'entier, en tant que nombre avec des décimales, ou en tant que fraction.