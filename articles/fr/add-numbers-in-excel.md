---
title: Comment additionner des nombres dans Excel
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-10-12T21:02:58.000Z'
originalURL: https://freecodecamp.org/news/add-numbers-in-excel
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/add-numbers-thumb-2.png
tags:
- name: excel
  slug: excel
- name: Math
  slug: math
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment additionner des nombres dans Excel
seo_desc: 'Did you know you can write Python code in a spreadsheet?

  You''d be surprised how many different ways there are to do things in Excel. Below,
  I''ll show you 9 ways to add two or more numbers. You can skip to a certain section
  if you''d like to see that m...'
---

Saviez-vous que vous pouvez écrire du code Python dans une feuille de calcul ?

Vous seriez surpris du nombre de façons différentes d'effectuer des tâches dans Excel. Ci-dessous, je vais vous montrer 9 façons d'additionner deux nombres ou plus. Vous pouvez sauter à une section spécifique si vous souhaitez voir cette méthode :

1. [Manuel](#manuel)
2. [Références](#references)
3. [SOMME()](#somme)
4. [SOMME.SI()](#somme-si)
5. [SOUS.TOTAL()](#sous-total)
6. [AGREGAT()](#agregat)
7. [VBA](#vba)
8. [Python](#python)
9. [Surligner](#surligner)

## Vidéo de démonstration

Si vous préférez me regarder passer en revue chacune de ces méthodes dans un classeur de démonstration, voici une vidéo pour cela :

%[https://youtu.be/xe5Ohlgizi8]

Pour écrire une formule ou une fonction dans Excel (ce que nous ferons dans les exemples ci-dessous), commencez simplement par taper un signe égal dans une cellule.

`=`

Cela indique à Excel que ce qui suit sera une formule ou une fonction intégrée.

<a id="manuel"></a>

## Manuel

Il s'agit de la version la plus simple d'une formule dans Excel. Commencez par le signe égal, puis tapez les nombres et l'opération que vous souhaitez effectuer. Comme avec une calculatrice :

`=6+102`

Appuyer sur Entrée affichera `108` dans la cellule.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-30.png)
_capture d'écran de l'addition manuelle dans Excel_

<a id="references"></a>

## Références

L'étape suivante dans Excel consiste à commencer à utiliser des références de cellules. Remarquez qu'en haut et sur le côté gauche de la zone principale de la feuille de calcul, il y a des colonnes désignées par des lettres et des lignes désignées par des nombres.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/rowscolumns.png)
_capture d'écran des lignes et colonnes_

Nous pouvons nous référer à des cellules spécifiques en utilisant la notation "A1". Comme un ensemble de coordonnées (x,y) sur un graphique, cela signifie simplement qu'en nous référant à C4, par exemple, nous nous référons à la cellule trouvée dans la colonne C, ligne 4.

Pour additionner des nombres en utilisant des références, nous commençons à nouveau par le signe égal et nous nous référons directement aux valeurs dans des cellules spécifiques.

Cela a l'avantage supplémentaire d'être dynamique. Si une valeur est modifiée dans l'une des cellules, le résultat de la somme est automatiquement mis à jour.

`=SOMME(A1+A3)` nous donne la valeur des nombres dans `A1` et `A3`.

<a id="somme"></a>

## SOMME()

Les deux premières méthodes sont des exemples d'utilisation de formules. Nous donnons manuellement à Excel une série d'instructions qu'il exécute.

Excel dispose également de fonctions intégrées que nous pouvons utiliser en commençant par le signe égal, puis en nous référant à la fonction par son nom. Les fonctions prennent également des variables que nous leur passons en utilisant une série de parenthèses après le nom de la fonction.

La fonction `SOMME()` prend soit une plage, soit une liste séparée par des virgules de références de cellules. Elle retourne ensuite la somme de tous les nombres dans la plage.

Vous pouvez sélectionner une plage soit en cliquant et en faisant glisser, soit en déclarant une plage en tapant la notation A1 avec un deux-points entre la cellule en haut à gauche et la cellule en bas à droite de la plage.

`SOMME(A5:A11)` additionne tous les nombres dans les cellules `A5, A6, A7, A8, A9, A10, A11`

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-31.png)
_capture d'écran de la fonction SOMME()_

<a id="somme-si"></a>

## SOMME.SI()

Une version plus puissante de `SOMME()` est la fonction `SOMME.SI()`. Celle-ci ajoute une logique conditionnelle. Elle nécessite au moins deux variables : une plage et une condition. Nous pourrions lui donner la même plage que ci-dessus et avoir une condition selon laquelle elle n'additionne que les nombres supérieurs à zéro.

Une troisième variable, optionnelle, est une `plage_somme`. Cela nous permet de faire correspondre une condition dans une plage avec la somme des valeurs dans une autre plage.

Dans la feuille d'exemple, j'ai inséré des cases à cocher dans la colonne C. Les cases à cocher dans Excel sont [une nouvelle fonctionnalité](https://youtu.be/hROvLovbl8E). Il s'agit de la plage que je vérifie pour une condition. La condition est VRAI. Maintenant, j'entre la plage que je veux additionner si la condition dans la ligne correspondante de la première plage est effectivement VRAI.

Lorsque vous utilisez une plage et une plage_somme séparément comme ceci, elles doivent avoir la même taille, sinon cela ne se comportera pas comme vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-32.png)
_capture d'écran de la fonction SOMME.SI() dans Excel_

<a id="sous-total"></a>

## SOUS.TOTAL()

D'accord, voici où les choses commencent à devenir intéressantes.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/butts.gif)

La fonction `SOUS.TOTAL()` nous permet de faire un tas de choses différentes. En fin de compte, elle retourne un sous-total d'une liste ou d'une base de données. Mais à l'intérieur de `SOUS.TOTAL()`, il y a d'autres fonctions. Le premier argument que nous donnons à `SOUS.TOTAL()` est un nombre correspondant à l'une de ces fonctions :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-33.png)
_capture d'écran des fonctions dans SOUS.TOTAL de Microsoft Excel_

En regardant la liste des fonctions, nous voyons que 9 ou 109 correspondent tous deux à la fonction `SOMME()` que nous voulons utiliser. Si nous avons des lignes cachées dans notre plage que nous ne voulons pas inclure dans la somme, nous utilisons 109 pour les ignorer – sinon, simplement 9.

Ainsi, la fonction ressemble à ceci : `SOUS.TOTAL(9,B3:B12)`. Cela fait la somme de `B3:B12` même si une ou plusieurs de ces lignes sont cachées.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-34.png)
_capture d'écran de SOUS.TOTAL dans Excel_

<a id="agregat"></a>

## AGREGAT()

Nous pouvons considérer `AGREGAT()` comme une version améliorée de `SOUS.TOTAL()`. Elle fonctionne de la même manière mais dispose de beaucoup plus de fonctions intégrées (19 au total) et permet une spécificité détaillée sur les valeurs à ignorer dans le calcul, le cas échéant.

`AGREGAT(num_fonction, options, ref1, [ref2], …)` est la formule de référence complète. Encore une fois, nous lui passons un nombre correspondant à l'une des 19 fonctions intégrées, puis un argument optionnel pour le type de valeurs à ignorer, suivi du tableau de référence et d'un tableau de référence secondaire optionnel.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-35.png)
_capture d'écran des options pour la fonction Agregat de Microsoft Excel_

Pour notre exemple, nous utilisons à nouveau 9 comme numéro de fonction, mais nous pouvons utiliser l'option 5 pour exclure explicitement les lignes cachées :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-36.png)
_capture d'écran de la fonction Agregat dans Excel_

<a id="vba"></a>

## VBA

Maintenant, nous sommes échauffés. Passons à quelque chose de trop compliqué.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/complicated.gif)
_gif de non-sens compliqué_

Visual Basic for Applications est le langage de programmation intégré de Microsoft dans les applications Microsoft Office.

Ouvrez-le en sélectionnant Visual Basic dans l'onglet Développeur.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/vba.png)
_capture d'écran de VBA dans l'onglet Développeur dans Excel_

Si vous ne voyez pas l'onglet Développeur, allez dans Fichier - Options - Personnaliser le ruban et ajoutez-le.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/developer-tab.png)
_capture d'écran de la personnalisation du ruban dans Excel_

De plus, `Alt + 11` est le raccourci clavier pour ouvrir VBA.

Une fois ici, nous pouvons écrire du code pour faire toutes sortes de choses. Notre exemple n'est pas très pratique puisque une fonction le fera plus rapidement, mais le code suivant additionnera la plage `A1:A11`, placera le résultat dans `F11` et affichera un message pop-up avec le résultat :

```vba
Sub AssignSumVariable()
   Dim result As Double
   'Assigner la variable
   result = WorksheetFunction.Sum(Range("B1:B11"))
   'Afficher le résultat
   MsgBox "Le total des plages est " & result
   'Placer le résultat dans la cellule F9
  Range("F9") = result
End Sub
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-37.png)
_capture d'écran de VBA dans Excel_

<a id="python"></a>

## Python

Oui, cela devient maintenant ridicule. Mais il est bon de savoir ce qu'Excel peut faire lorsque vous avez des tâches plus compliquées qui nécessitent des outils comme VBA ou Python. Au moment de la rédaction de cet article, Python est disponible dans Excel pour les personnes utilisant le canal Beta d'Excel.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/overkill.gif)
_gif d'une femme disant "semble excessif"_

Vous pouvez vérifier votre éligibilité et rejoindre Microsoft 365 Insider si vous souhaitez tester de nouvelles fonctionnalités comme celle-ci à l'avenir.

Allez dans Fichier - Compte, puis sélectionnez le bouton du canal Microsoft 365 Insider pour plus d'informations.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-38.png)
_capture d'écran des options Microsoft 365 Insider_

Une fois que Python est utilisable dans Excel, vous l'activez en tapant `=py` puis la touche `tab`. Cela transforme la cellule en une ligne de commande Python.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-39.png)
_capture d'écran de la ligne de commande Python dans Excel_

À partir de là, nous pouvons écrire du code Python directement dans la cellule. Le code suivant utilise la fonction personnalisée xl() pour Python afin d'utiliser une plage. Nous conservons la plage dans la variable numbers, puis, en utilisant la notation par points, nous faisons la somme de cette plage avec la ligne `numbers.sum()` :

```python
numbers = xl("'Sum795'!$B$3:$B$12")
numbers.sum()
```

Maintenant, pour exécuter le code Python, cliquez sur `CTRL + ENTRÉE`.

Ce que nous voyons maintenant, c'est que nous avons une série Python dans la cellule :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-40.png)

Afin d'afficher simplement la réponse, nous pouvons cliquer sur le sélecteur de sortie Python juste à gauche de la barre de formule et sélectionner `Valeur Excel` :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/python-object.png)
_capture d'écran de la sortie Python dans Excel_

Maintenant, notre cellule est mise à jour avec la valeur correcte.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-42.png)
_capture d'écran des cellules dans Excel_

La vraie valeur de Python dans Excel réside dans la manipulation des dataframes en utilisant des bibliothèques intégrées comme Matplotlib, NumPy ou Pandas.

D'accord, prenez une respiration, nous allons terminer avec quelque chose de simple et facile...👇

<a id="surligner"></a>

## Surligner

Temps bonus. Si vous surlignez des cellules dans Excel en cliquant et en faisant glisser la souris sur une plage, ou en appuyant sur `CTRL` + `Clic gauche` sur des cellules individuelles, certains calculs automatiques sont visibles en bas à droite de la fenêtre, y compris la Moyenne, le Compte et la Somme :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/highlight.png)

Si la somme n'est pas immédiatement visible, un clic droit fera apparaître des calculs automatiques que vous pouvez activer ou désactiver :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-29.png)
_capture d'écran des options de calcul automatique dans Excel_

## Merci d'avoir lu !

J'espère que cela vous est utile !

Suivez-moi sur LinkedIn : [https://www.linkedin.com/in/eamonncottrell/](https://www.linkedin.com/in/eamonncottrell/)

Et sur YouTube : [https://www.youtube.com/@eamonncottrell](https://www.youtube.com/@eamonncottrell)

Passez une excellente journée ! 👋