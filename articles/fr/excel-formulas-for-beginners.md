---
title: Formules Excel – Fonctions de base pour débutants
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-05-12T15:44:00.000Z'
originalURL: https://freecodecamp.org/news/excel-formulas-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/einstein-153422_1280.png
tags:
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
seo_title: Formules Excel – Fonctions de base pour débutants
seo_desc: 'Microsoft Excel lets you use formulas and functions to perform basic and
  advanced numerical calculations. You can do addition, subtraction, multiplication,
  division, mean, worke with strings, and many others.

  In Excel, the difference between a formul...'
---

Microsoft Excel vous permet d'utiliser des formules et des fonctions pour effectuer des calculs numériques de base et avancés. Vous pouvez faire des additions, des soustractions, des multiplications, des divisions, des moyennes, travailler avec des chaînes de caractères, et bien plus encore.

Dans Excel, la différence entre une formule et une fonction est qu'une fonction est un calcul prédéfinis tandis qu'une formule est un calcul défini par l'utilisateur. 

Par exemple, `SUM` est une fonction tandis que `=SUM(E1:E9)` est une formule utilisant la fonction `SUM`. 

Dans cet article, je vais vous montrer des formules et fonctions Excel qui vous faciliteront la vie chaque fois que vous travaillez avec Excel. Vous apprendrez également comment utiliser chacune des formules. 
 
| Fonction      | Description | Utilisation |
| ----------- | ----------- |----------|
|**Formules Excel pour travailler avec des nombres**|
| SUM      | Pour additionner des nombres dans une cellule       | =SUM(D2:D10)   |
| AVERAGE   | Pour trouver la moyenne de certains nombres dans une cellule      |  =AVERAGE(E6:E8)  |
|MIN| Pour trouver le nombre minimum parmi les nombres dans les cellules| MIN(C1:C10)|
|MAX| Pour trouver le nombre maximum parmi les nombres dans les cellules | =MAX(C1:C10)|
|SUMIF| Additionne tous les nombres dans certaines cellules qui répondent à certains critères| =SUMIF(B7:B9, ">2000",E2:E6)|
|ISNUMBER| Retourne vrai si une valeur est un nombre et faux si ce n'est pas un nombre| ISNUMBER(E7)|
|ISEVEN| Retourne vrai si un nombre est un nombre pair et faux si ce n'est pas le cas |ISEVEN(D3)|
|ISODD | Retourne vrai si un nombre est un nombre impair et faux si ce n'est pas le cas |=ISODD(D10)|
| ISERROR | Retourne vrai si une valeur est une erreur et faux si ce n'est pas le cas | =ISERROR(D9) |
|MEDIAN | Retourne le nombre au milieu de certains nombres | =MEDIAN(D2:D10) | 
|PI | Retourne la valeur de Pi à 15 chiffres | =Pi() |
| CODE | Retourne un code numérique pour le premier caractère d'une chaîne dans le jeu de caractères utilisé par votre ordinateur | =CODE(free) |
|RAND | Génère un nombre aléatoire entre 0 et 1 | RAND()|
|POWER | Retourne le résultat d'un nombre élevé à une puissance | =POWER(3,9)|
|ROUND | Arrondit un nombre au nombre spécifié de décimales | =ROUND(D10,3) | 
|ROMAN | Convertit un nombre en chiffres romains | =ROMAN(2022) |
|MOD | Retourne le reste d'un nombre lorsqu'il est divisé par un autre nombre | =MOD(123 ,3) |
|BASE | Convertit un nombre en une représentation textuelle avec le nombre de base donné | =BASE(2,32,1)|
|CEILING | Arrondit un nombre à l'entier supérieur ou au multiple de signification le plus proche | =CEILING(D6, 2)|
|CELL | Retourne des informations sur une cellule | =CELL(D9)|
|CHAR | Retourne le caractère spécifié par le numéro de code du jeu de caractères de votre ordinateur | =CHAR(D4)|
|COUNT | Compte combien de nombres se trouvent dans la liste de certains arguments | =COUNT(D2:D10)| 
| DOLLAR | Convertit un nombre au format devise à un nombre spécifié de décimales | =DOLLAR(4000,4)|
| COS | Retourne le cosinus d'un angle | =COS(60)|
| SIN | Retourne le sinus d'un angle | =SIN(30)|
| TAN | Retourne la tangente d'un angle | =TAN(45)|
|**Formules Excel pour travailler avec des dates**|
|TIME | Convertit l'heure, les minutes et les secondes en un numéro de série Excel au format heure | =TIME(9,20,40|
|DATE | Retourne le numéro qui représente le jour dans le code date-heure Excel | =DATE(2022,5,12)|
|DAY | Convertit un nombre en une date du mois | =DAY(243)|
|HOUR| Retourne le nombre en tant qu'heure entre 0 et 23| =HOUR(34)|
|MINUTE| Retourne la minute, un nombre entre 0 et 59 | =MINUTE(59)|
|SECOND| Retourne la seconde, un nombre entre 0 et 59 | =SECOND(48)|
|TODAY| Retourne la date actuelle formatée en tant que date | =TODAY()|
|WEEKDAY| Retourne le jour de la semaine, un nombre entre 1 et 7 | =WEEKDAY(12,4)|
| MONTH | Retourne le mois, un nombre entre 1 et 12 |=MONTH(9)|
|YEAR | Retourne l'année, une date entre 1900 et 9999 |=YEAR(12) |
|**Formules Excel pour travailler avec du texte et des chaînes de caractères**|
|Concatenate | Combine divers textes ensemble | =CONCATENATE("free","Code","Camp")|
|LEN| Retourne la longueur d'une chaîne| =LEN(C1)|
|LEFT | Retourne le nombre de chaînes spécifiées du côté gauche d'une chaîne | =LEFT(C6,5) |
| RIGHT | Retourne le nombre de chaînes spécifiées du côté droit d'une chaîne | =RIGHT(C6,5) |
|MID | Retourne le nombre au milieu d'une chaîne à partir d'une position de départ et de longueur spécifiées| =MID(C7,3,5) |
|REPLACE | Remplace des parties d'une chaîne par une autre chaîne spécifiée | =REPLACE("Coding",2,2,"og")|
|FIND | Retourne la position de départ d'une chaîne avec une autre chaîne | =FIND("od","Coding",1) |
|ISTEXT| Retourne vrai si une valeur est une chaîne et faux si ce n'est pas le cas | =ISTEXT(D9)|
|LOWER | Convertit le texte en minuscules | =LOWER("FREECODECAMP")|
|UPPER | convertit le texte en majuscules | =UPPER("freecodecamp")|
|TRIM | Supprime tous les espaces d'un texte sauf les espaces simples entre les mots | =TRIM("free  code    camp")|
| EXACT | Retourne vrai si deux textes sont égaux et faux s'ils ne le sont pas| =EXACT("free","FREE"|
| PROPER | Convertit la première lettre d'un mot en majuscule| =PROPER("javascript")|
| **Logique** |
|AND | Retourne vrai si tous les arguments sont vrais et faux s'ils ne le sont pas | =AND(12,34)|
|NOT| Change faux en vrai et vrai en faux | =NOT(TRUE)|
|OR | Retourne faux uniquement si tous les arguments sont faux | =OR(12,12)|

## Conclusion

Excel fournit diverses fonctions qui vous permettent de manipuler vos données.

Pour découvrir plus de ces fonctions, cliquez sur l'onglet Formule
![formulas](https://www.freecodecamp.org/news/content/images/2022/05/formulas.png)