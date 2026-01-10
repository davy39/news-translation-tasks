---
title: Concaténer dans Excel – Comment combiner du texte et concaténer des chaînes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-26T16:55:39.000Z'
originalURL: https://freecodecamp.org/news/concatenate-in-excel-how-to-combine-text-and-concat-strings
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/mika-baumeister-Wpnoqo2plFA-unsplash.jpg
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: excel
  slug: excel
seo_title: Concaténer dans Excel – Comment combiner du texte et concaténer des chaînes
seo_desc: "By Gregory V. Chapman\nWhen dealing with Excel workbooks, data may be structured\
  \ in a way that doesn’t fit your needs and objectives. \nSometimes, you may need\
  \ to split the content of one cell into different cells. You may also need to do\
  \ the opposite,..."
---

Par Gregory V. Chapman

Lors de la manipulation de classeurs Excel, les données peuvent être structurées de manière à ne pas répondre à vos besoins et objectifs. 

Parfois, vous devrez peut-être diviser le contenu d'une cellule en différentes cellules. Vous devrez peut-être aussi faire l'inverse, en combinant des données de plusieurs colonnes en une seule. 

Le second processus est appelé concaténation. Le plus souvent, vous utilisez la concaténation dans Excel pour joindre des données telles que des noms et adresses, afficher l'heure et la date. 

Dans ce guide, nous examinerons en détail la concaténation et étudierons les techniques que vous pouvez utiliser dans différentes situations.

## Que signifie « Concaténer » ?

Généralement, Excel vous permet de combiner des données de deux manières : vous pouvez soit fusionner des cellules, soit concaténer leurs valeurs. 

La première option consiste à transformer plusieurs cellules en une seule. En résultat, vous obtenez une seule grande cellule qui s'affiche sur plusieurs colonnes ou lignes. 

Si vous choisissez de concaténer des cellules, vous ne fusionnerez pas les cellules elles-mêmes mais combinerez leur contenu. 

La concaténation n'impacte pas les cellules mais joint plusieurs valeurs. Par exemple, vous pouvez utiliser cette méthode pour combiner des morceaux de contenu textuel provenant de différentes cellules. Dans Excel, un tel contenu est appelé chaînes de texte. Vous pouvez également insérer un nombre obtenu à partir d'une formule entre du contenu textuel.

Par exemple, vous pouvez avoir les prénoms de vos clients dans la colonne B, et leurs noms de famille dans la colonne C. Vous souhaitez peut-être que la colonne D contienne à la fois leurs prénoms et noms de famille, mais retaper leurs noms manuellement est trop chronophage et inefficace. 

Dans ce cas, vous pouvez utiliser les fonctions de concaténation, comme « CONCATENATE », « CONCAT » et « &. » Examinons chacune de ces formules et découvrons les différences.

## Comment joindre des chaînes de texte dans Excel

### CONCATENATE

![Image](https://www.freecodecamp.org/news/content/images/2021/03/3-1.png)

Excel vous permet de joindre des chaînes de texte de différentes manières. Tout d'abord, vous pouvez utiliser la [fonction CONCATENATE](https://support.microsoft.com/en-us/office/concatenate-function-8f8ae884-2ca8-4f7a-b093-75d702bea31d). Dans ce cas, votre formule ressemblera à ceci :

=CONCATENATE(X1,X2,X3)

X1, X2 et X3 sont les cellules que vous souhaitez joindre.

Si vous souhaitez séparer les valeurs des cellules avec des espaces, vous pouvez les ajouter entre guillemets, séparés par des virgules :

=CONCATENATE(X1," ",X2)

### CONCAT

![Image](https://www.freecodecamp.org/news/content/images/2021/03/2-2.png)

CONCATENATE est la plus ancienne fonction de ce type et la seule fonction que vous pouvez utiliser pour joindre des chaînes de texte lorsque vous travaillez avec Excel 2013. 

Cependant, si vous utilisez une version plus récente d'Excel, vous pourriez envisager des fonctions mises à jour. La fonction CONCATENATE pourrait également ne pas être disponible dans les versions futures. La [fonction CONCAT](https://support.microsoft.com/en-us/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2) fonctionne avec Excel 2016 et Excel Mobile. 

Vous pouvez utiliser cette formule de la même manière que CONCATENATE, mais CONCAT est certainement plus facile à utiliser car elle est plus courte. 

Voici à quoi ressemblerait l'exemple ci-dessus avec la fonction CONCAT :

=CONCAT(X1,X2,X3)

### L'opérateur « & »

![Image](https://www.freecodecamp.org/news/content/images/2021/03/1-1.png)

Cependant, vous pouvez également choisir de ne pas utiliser l'une des formules ci-dessus et opter pour une option encore plus simple : l'opérateur esperluette (&). Cette méthode de jointure de cellules est recommandée par Microsoft, et elle est beaucoup plus facile à utiliser que les fonctions CONCAT et CONCATENATE. 

Voici un exemple de formule que vous pouvez utiliser :

=X1&X2&X3

Si vous souhaitez séparer les valeurs des cellules avec des espaces ou des virgules, voici à quoi ressembleront vos formules :

=X1&" "&X2

=X1&","&X2

L'utilisation de l'opérateur « & » est une option plus pratique. De plus, l'opérateur « & » n'a pas de limitations concernant le nombre de chaînes que vous pouvez joindre. 

En revanche, la fonction CONCATENATE est limitée à 8 192 caractères, ce qui signifie que vous ne pouvez l'utiliser que pour joindre jusqu'à 255 chaînes. Cependant, parfois vous pourriez vouloir utiliser la fonction CONCAT pour garder vos formules propres et les rendre plus faciles à lire.

### TEXTJOIN

Une autre fonction que vous pouvez utiliser lors de la combinaison de contenu textuel est [TEXTJOIN](https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c). Cette fonction ne fonctionne qu'avec les dernières versions de Microsoft Office, et elle offre quelques fonctionnalités intéressantes. 

Tout d'abord, vous pouvez choisir comment vous souhaitez séparer les valeurs de différentes cellules, sans avoir besoin de taper ces espaces, virgules ou autres symboles dans la formule. 

Deuxièmement, la fonction TEXTJOIN vous permet d'ignorer les cellules vides tout en incluant un tableau d'arguments.

Voici à quoi ressemble la fonction TEXTJOIN dans Excel :

=TEXTJOIN(délimiteur,ignorer_vide,texte1,[texte2],...)

« Délimiteur » est le séparateur que vous souhaitez utiliser entre différentes chaînes de texte, et « ignorer_vide » ne peut prendre que deux valeurs : VRAI ou FAUX. 

Lorsque vous utilisez TEXTJOIN, vous pouvez toujours ajouter des cellules manuellement, mais dans ce cas, l'opérateur « & » serait un meilleur choix. TEXTJOIN vous permet d'ajouter une plage entière de cellules. 

Par exemple, voici la fonction que vous pouvez utiliser pour joindre des chaînes de texte de la plage A1:A4, séparées par des virgules, en ignorant les valeurs vides :

=TEXTJOIN(",",VRAI,A1:A4)

Si vous souhaitez séparer les chaînes de texte avec des espaces et inclure les valeurs vides, la formule ressemblera à ceci :

=TEXTJOIN(" ",FAUX,A1:A4)

## Comment concaténer des chaînes de texte avec des sauts de ligne

Le plus souvent, les utilisateurs d'Excel ont besoin de séparer les chaînes de texte avec des espaces et des marques de ponctuation. Dans ce cas, vous pouvez utiliser les formules des sections précédentes, selon les fonctions ou opérateurs choisis. 

Cependant, parfois vous pourriez avoir besoin de séparer les chaînes de texte avec un retour à la ligne, ou saut de ligne. Par exemple, vous pourriez avoir besoin de fusionner des données et des adresses postales provenant de colonnes ou de lignes séparées.

Malheureusement, vous ne pouvez pas mettre de sauts de ligne dans les formules aussi facilement que vous le faites avec les marques de ponctuation car ils ne sont pas des caractères réguliers. La bonne nouvelle est que vous pouvez inclure pratiquement tous les caractères que vous souhaitez en utilisant les [codes ASCII](https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/). 

Dans ce cas, vous devez utiliser la [fonction CHAR](https://support.microsoft.com/en-us/office/char-function-bbd249c8-b36e-4a91-8017-1c133f9b837a). Pour inclure un saut de ligne sur Windows, vous devez utiliser CHAR(10), car 10 est le code ASCII pour un saut de ligne. Sur Mac, vous devez utiliser CHAR(13), puisque 13 est le code ASCII pour le retour chariot. 

Gardez à l'esprit que vous devez également activer l'option « Retour à la ligne » pour afficher correctement le résultat. Appuyez sur Ctrl+1, puis choisissez l'onglet « Alignement » dans le menu « Format de cellule » et cochez la case « Retour à la ligne ».

## Comment concaténer des colonnes

Pour concaténer plusieurs colonnes, vous pouvez écrire une formule de concaténation régulière dans la première cellule, puis faire glisser la poignée de recopie pour la copier dans d'autres cellules. 

Pour le faire rapidement, vous pouvez sélectionner la cellule qui contient la formule nécessaire, puis double-cliquer sur la poignée de recopie. Excel décide jusqu'où les cellules doivent être copiées après votre double-clic en fonction des cellules présentes dans votre formule. Par conséquent, si votre tableau contient des cellules vides, vous devrez peut-être faire glisser la poignée de recopie manuellement.

## Comment concaténer une plage de cellules

Étant donné que les fonctions CONCATENATE et CONCAT n'acceptent que des références de cellules uniques dans les arguments, la jointure de valeurs provenant de plusieurs cellules peut être un défi. 

Pour sélectionner rapidement plusieurs cellules, vous pouvez appuyer sur Ctrl et cliquer sur chacune des cellules que vous souhaitez combiner. 

Cependant, si vous traitez avec trop de cellules, cette méthode peut également être trop chronophage. Dans ce cas, vous pouvez utiliser la [fonction TRANSPOSE](https://support.microsoft.com/en-us/office/transpose-function-ed039415-ed8a-4a81-93e9-4b6dfac76027), qui ressemble à ceci :

=TRANSPOSE(X1:Xn)

Tapez la formule TRANSPOSE dans une cellule où vous souhaitez inclure la plage concaténée, cliquez sur la barre de formule, puis appuyez sur F9 pour remplacer votre formule par des valeurs concaténées. Après cela, vous devez supprimer les accolades autour des valeurs du tableau, taper =CONCAT( avant la première valeur, et ajouter une parenthèse fermante après la dernière valeur.

## Points à garder à l'esprit concernant la concaténation

N'oubliez pas de mettre des virgules entre les éléments concaténés. Par exemple, si vous souhaitez obtenir la phrase « [write my research paper](https://www.trustmypaper.com/write-my-research-paper) », votre formule doit être =CONCAT("write"," ","my"," ","research"," ","paper"). 

Dans cet exemple, tous les éléments sont également séparés par des espaces désignés. Vous pouvez également inclure des espaces supplémentaires après chaque chaîne de texte pour éviter de les taper séparément dans les formules.

Si vous tapez =CONCAT("Hi""there"), sans virgule, le résultat ressemblera à ceci : Hi"there. Une marque de guillemet supplémentaire apparaîtra car il n'y a pas de virgule entre les arguments. 

Si vous voyez l'erreur « #NAME? » au lieu du résultat souhaité, cela signifie probablement que vous avez oublié d'inclure certaines marques de guillemets. L'erreur « #VALUE! » signifie que certains des arguments sont invalides.

Vous devez également garder à l'esprit que les fonctions de concaténation retournent toujours une chaîne de texte, même si certaines cellules contiennent des valeurs numériques. Vous pouvez également convertir des nombres en texte en utilisant la [fonction TEXT](https://support.microsoft.com/en-us/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c) et utiliser différentes formules pour définir le format des nombres que vous souhaitez combiner avec du texte ou des symboles. 

Par exemple, si votre cellule A2 contient le nombre 13,6 et que vous souhaitez l'afficher comme un montant en dollars, votre formule doit être =TEXT(A2,"$0.00"). En résultat, vous obtiendrez $13.60.

## Conclusion

Excel vous permet de joindre des chaînes de texte en utilisant différentes fonctions, telles que CONCATENATE, CONCAT et l'opérateur « &. » 

Bien que vous ne puissiez utiliser la fonction CONCATENATE que dans Excel 2013, les versions plus récentes d'Excel supportent un simple opérateur « & » qui est beaucoup plus facile à utiliser. 

Lorsque vous concaténez des valeurs de différentes cellules, portez attention aux marques de guillemets et aux virgules car elles sont très importantes pour afficher correctement les résultats. 

J'espère que ce guide vous aidera à gagner beaucoup de temps et à rendre votre flux de travail aussi efficace que possible.