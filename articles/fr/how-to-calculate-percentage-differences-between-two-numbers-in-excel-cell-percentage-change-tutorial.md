---
title: Comment calculer les différences de pourcentage entre deux nombres dans Excel
  - Tutoriel sur le changement de pourcentage des cellules
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2022-12-13T21:49:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-calculate-percentage-differences-between-two-numbers-in-excel-cell-percentage-change-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/12.13.22-Percent-Change2.jpg
tags:
- name: data
  slug: data
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment calculer les différences de pourcentage entre deux nombres dans
  Excel - Tutoriel sur le changement de pourcentage des cellules
seo_desc: "Spreadsheets are powerful and awesome. \U0001F4AA \nIn this tutorial I\
  \ will show you four ways to find the percentage difference between two numbers\
  \ in Excel. I'll also show you how to use custom functions in Google Sheets. \U0001F44D\
  \nThe four techniques (and one bon..."
---

Les feuilles de calcul sont puissantes et géniales. 4ca

Dans ce tutoriel, je vais vous montrer quatre façons de trouver la différence de pourcentage entre deux nombres dans Excel. Je vais également vous montrer comment utiliser des fonctions personnalisées dans Google Sheets. 44d

Les quatre techniques (et un bonus) que nous allons utiliser sont :

1. Utilisation d'une formule (niveau 13a3 facile)
2. Utilisation de la fonction LAMBDA + Gestionnaire de noms (niveau 23a3 mode normal)
3. Utilisation de Visual Basic pour Applications (VBA) (niveau 33a3 mode difficile)
4. Utilisation de l'API JavaScript Office (niveau 43a3 mode ultra)
5. Utilisation de fonctions personnalisées avec Google Sheets (4e5 niveau bonus)

## Formule pour le changement de pourcentage entre deux nombres dans Excel

La formule est la première chose à laquelle la plupart des gens auront recours lorsqu'ils effectuent un calcul dans Excel. Elle nous permet de faire des calculs explicites en utilisant les données des cellules.

Supposons que nous avons des données de ventes pour une année dans la cellule `B3` et des données de ventes pour la deuxième année dans la cellule `C3`. En tapant la formule ci-dessous, nous pouvons calculer la différence de pourcentage de la première année à la deuxième :

```excel
=(C3-B3)/B3
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-62.png)
_formule pour le changement de pourcentage entre deux nombres dans Excel_

Taper une formule personnalisée a l'avantage d'être rapide et simple, surtout pour des calculs simples.

De plus, les formules peuvent être copiées vers le bas et/ou à travers des plages de cellules pour une réutilisation rapide. Et les formules sont utilisées de la même manière dans Google Sheets que dans Microsoft Excel.

Cependant, lorsque les calculs deviennent longs et/ou complexes, il peut être utile de connaître certaines méthodes alternatives.

## Comment utiliser une fonction LAMBDA et le gestionnaire de noms

En nous basant sur notre premier exemple, la fonction LAMBDA nous permet de prendre une opération personnalisée et de la codifier pour une réutilisation dans toute notre feuille de calcul.

En utilisant les mêmes données que précédemment (cette fois dans les cellules `B4` et `C4`), nous écrivons la fonction LAMBDA comme suit :

```excel
=LAMBDA(annee1,annee2,(annee2-annee1)/annee1)(B4,C4)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-63.png)
_Capture d'écran de la fonction Lambda Excel_

Au premier abord, vous pourriez vous demander pourquoi diantre nous devrions taper ce désordre interminable, mais restez avec moi et vous verrez qu'il est probablement plus propre pour une réutilisation que de simplement définir une fonction.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/confused.gif)
_Gif d'une femme se grattant la tête et ayant l'air confuse_

Voici ce qui se passe :

La première chose que nous faisons est de définir les paramètres de notre fonction et de les séparer par des virgules. Vous pouvez définir autant de paramètres que vous le souhaitez (eh bien, jusqu'à 253, cela dit 913). Nous n'en avons que deux : `annee1` et `annee2`.

Après avoir listé les paramètres, nous écrivons la formule que nous voulons que Excel calcule. C'est la même chose que nous avons faite dans la première section Formule, sauf que cette fois nous utilisons les noms de nos paramètres au lieu des noms de cellules explicites : `(annee1-annee2)/annee1`.

Enfin, nous fermons la parenthèse de la fonction LAMBDA puis nous l'appelons en écrivant les cellules réelles utilisées : `B4,C4`. Cela indique à la fonction qu'elle doit utiliser la valeur dans la cellule `B4` pour le paramètre `annee1` et la valeur dans la cellule `C4` pour le paramètre `annee2`.

Quel désordre, n'est-ce pas ? Oui, et techniquement, écrire toute la fonction LAMBDA ici est simplement une bonne pratique pour s'assurer que la chose fonctionne avant de passer à l'étape suivante...

C'est la partie cool. Cliquez sur l'onglet Formule dans le Ruban en haut et sélectionnez Gestionnaire de noms.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/name-manager.png)
_Ruban Excel accédant au Gestionnaire de noms dans l'onglet Formule_

Sélectionnez Nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/name-manager-new.png)
_Capture d'écran du Gestionnaire de noms dans Excel_

Ensuite, entrez le Nom de votre formule et écrivez une description facultative dans les Commentaires. Dans la ligne Fait référence à, vous copierez la fonction LAMBDA.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/name-manager2.png)
_Capture d'écran de la Fonction nommée dans Excel_

Vous pourrez l'utiliser de la même manière que vous utiliseriez une fonction intégrée en tapant ce qui suit dans une cellule :

```excel
=Pourcentage_Variation(B5,C5)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/percentage-change-lambda.png)
_Capture d'écran de la formule Excel_

Maintenant, nous avons toute la facilité d'une fonction intégrée régulière à notre disposition. Google Sheets a une fonctionnalité similaire, que nous aborderons à la fin de cet article.

## Comment utiliser Visual Basic pour Applications

Si vous utilisez la version de bureau d'Excel, vous avez accès à Visual Basic pour Applications. Il s'agit d'un langage de programmation orienté événement de Microsoft et vous pouvez l'utiliser pour faire presque tout ce que vous pouvez imaginer (et coder).

Si vous vouliez trouver la différence de pourcentage entre deux nombres en utilisant VBA, vous iriez dans l'onglet Développeur du Ruban (ou appuierez sur `alt + F11`).

![Image](https://www.freecodecamp.org/news/content/images/2022/12/vba1.png)
_Capture d'écran de l'onglet Développeur dans Excel_

Si vous ne voyez pas l'onglet Développeur, vous devrez peut-être l'activer en sélectionnant Fichier -> Options. Ensuite, cherchez Personnaliser le Ruban. À partir de là, vous pouvez sélectionner la case à côté de Développeur.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/vba3.png)
_Capture d'écran des Options Excel_

Bonus : Si `ALT + F11` ne fonctionne pas, GeForce Experience peut interférer avec les raccourcis intégrés. Changez le raccourci pour ce qui utilise `ALT + F11` dans les paramètres. Pour moi, c'était le paramètre Activer/désactiver les commentaires lors de la diffusion sur Facebook.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/vba2.png)
_capture d'écran des paramètres GeForce Experience_

Une fois que vous avez ouvert la fenêtre VBA, sélectionnez Insertion -> Module dans le menu. Cela ouvrira une fenêtre vide où nous écrirons notre programme. Pensez à cela comme un IDE à l'intérieur d'Excel. Nous programmerons ici puis utiliserons ce programme dans notre feuille de calcul.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/vba4.png)
_Capture d'écran du menu VBA_

Ici, nous pouvons entrer le même type de commandes que nous avons utilisées avec la fonction LAMBDA nommée ci-dessus.

```excel
Function FONCTIONPOURCENT(annee1, annee2)
    FONCTIONPOURCENT = (annee2 - annee1) / annee1
End Function
```

Et voilà ! Nous pouvons maintenant utiliser `FONCTIONPOURCENT` dans notre feuille Excel de la même manière que nous avons utilisé la fonction nommée `Pourcentage_Variation`.

VBA est utile pour des programmes plus compliqués et serait excessif pour notre exemple. Accessoirement, Google Sheets n'a pas de fonctionnalité VBA.

## Comment utiliser l'API JavaScript Office

Maintenant, le vrai bon truc ! Saviez-vous que vous pouvez écrire du JavaScript et du TypeScript dans Excel ? Moi non plus. Mais vous pouvez.

Script Lab est un module complémentaire de Microsoft qui nous permet d'explorer l'API JavaScript dans les applications Office ainsi que de déclarer des fonctions personnalisées en les écrivant sous forme de scripts.

Vous pouvez l'ajouter à Excel [ici](https://learn.microsoft.com/en-us/office/dev/add-ins/overview/explore-with-script-lab). Et en lire plus à ce sujet [ici](https://learn.microsoft.com/en-us/office/dev/add-ins/overview/explore-with-script-lab).

Contrairement à VBA, cela est utilisable sur la version web d'Excel également.

Une fois installé, sélectionnez-le dans le Ruban et cliquez sur Code.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/script1.png)
_Capture d'écran de Script Lab dans le Ruban Excel_

Cela fera apparaître un véritable éditeur de code dans la barre latérale.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-66.png)
_Capture d'écran de l'éditeur de code Script Labs dans Excel_

Nous pouvons créer une fonction personnalisée en utilisant JavaScript en sélectionnant un Nouveau Snippet dans le menu Hamburger en haut à gauche de la fenêtre Scripts Lab.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-67.png)
_Capture d'écran du menu Nouveau Snippet_

En tapant la fonction suivante, nous pouvons à nouveau définir une fonction de différence de pourcentage, mais cette fois en utilisant JavaScript.

```javascript
/** @CustomFunction */
function pourcentage_variation_javascript(annee1, annee2) {
  return (annee2 - annee1) / annee1;
}

```

Pour utiliser cette fonction, sélectionnez Script Lab -> Fonctions dans le Ruban :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/script2.png)
_Capture d'écran du menu Script Lab dans le Ruban_

Cela ouvrira un autre onglet de barre latérale et grâce à la première ligne du snippet : `/** @CustomFunction */`, il enregistrera cette fonction personnalisée.

Dans la feuille de calcul, vous pourrez l'utiliser exactement comme nous avons utilisé les fonctions définies personnalisées. Cette fois, cependant, lorsque vous commencez à taper le titre, vous verrez qu'elle est enregistrée avec un préfixe scriptlab sur le nom. Sélectionnez ceci, et il retournera le changement de pourcentage tout comme les autres méthodes.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/script3.png)
_Capture d'écran de la fonction personnalisée Script Lab dans Excel_

Une fois de plus, cela est un peu excessif pour une simple fonction, mais assez pratique à mettre dans votre ceinture à outils néanmoins ! 44d

## Comment utiliser des fonctions personnalisées avec Google Sheets

Comme promis, voici un bonus sur la façon de créer une fonction nommée dans Google Sheets. Cela est très similaire à l'utilisation du Gestionnaire de noms dans Excel.

Sélectionnez Données -> Fonctions nommées dans Google Sheets.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/sheets1.png)
_Capture d'écran du menu Données de Google Sheets_

Cela vous invitera à nommer et décrire votre fonction ainsi qu'à fournir des arguments, si applicable.

Enfin, vous définirez l'opération de la fonction.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/sheets2.png)
_Capture d'écran du nommage d'une fonction personnalisée dans Google Sheets_

L'écran suivant vous invite à ajouter des descriptions et des exemples d'arguments si vous le souhaitez. Cela est facultatif, mais sera inclus dans le menu d'aide déroulant lorsque vous utiliserez la fonction dans votre feuille.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/sheets4.png)
_Capture d'écran des descriptions d'arguments de fonction personnalisée dans Google Sheets_

Ensuite, il est aussi simple que de taper votre fonction personnalisée et de sélectionner les cellules. Vous pouvez voir ci-dessous comment le menu d'aide est affiché avec les informations que vous avez fournies.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/sheets5.png)
_Capture d'écran de l'utilisation d'une fonction personnalisée dans Google Sheets_

## Conclusion

Oui, souvent vous opterez pour la simplicité en utilisant une formule rapide dans Excel ou Google Sheets. Mais maintenant vous connaissez plusieurs autres façons de trouver le changement de pourcentage entre deux nombres.

J'espère que vous avez trouvé cela utile, et bonne chance dans vos propres aventures de feuilles de calcul !

Vous pouvez me trouver et me suivre sur [LinkedIn](https://www.linkedin.com/in/eamonncottrell/). J'adorerais que vous disiez bonjour. 44b

![Image](https://www.freecodecamp.org/news/content/images/2022/12/hey.gif)
_Jimmy Fallon disant haaaaay et tenant du foin_