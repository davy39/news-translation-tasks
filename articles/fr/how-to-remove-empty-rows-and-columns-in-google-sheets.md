---
title: Comment supprimer les lignes et colonnes vides dans Google Sheets
subtitle: ''
author: Nibesh Khadka
co_authors: []
series: null
date: '2023-09-07T07:10:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-empty-rows-and-columns-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/delete-empty-rows-and-columns-in-google-sheets.png
tags:
- name: automation
  slug: automation
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
seo_title: Comment supprimer les lignes et colonnes vides dans Google Sheets
seo_desc: "In this tutorial, you will learn how to remove empty rows and columns from\
  \ Google Sheets using Google Apps Script.\nA while ago I wrote an article on how\
  \ to remove empty rows and columns from Google Sheets. \nI recently revisited that\
  \ article and I now..."
---

Dans ce tutoriel, vous apprendrez à supprimer les lignes et colonnes vides de Google Sheets en utilisant Google Apps Script.

Il y a quelque temps, j'ai écrit un article sur [comment supprimer les lignes et colonnes vides de Google Sheets](https://kcl.hashnode.dev/how-to-delete-empty-rows-and-columns-in-google-sheets).

J'ai récemment revisité cet article et je vous présente maintenant cette version révisée.

J'ai également une version vidéo de ce sujet que vous pouvez consulter ci-dessous :

%[https://youtu.be/Eiqa5ST9DYM]

## Ce que nous allons couvrir

Vous allez créer deux fonctions : `deleteExternalEmptyRowsNColumns()` et `deleteInternalEmptyRowsNColumns()`.

La première fonction supprimera les lignes et colonnes vides de la plage qui sont à l'extérieur de la plage retournée par la méthode [`getDataRange()`](https://developers.google.com/apps-script/reference/spreadsheet/sheet#getdatarange).

La deuxième fonction supprimera les lignes et colonnes qui sont vides et qui sont à l'intérieur de la plage retournée par `getDataRange()`.

Nous allons également créer un menu afin que nous puissions exécuter ces fonctions depuis la feuille de calcul elle-même.

## Comment préparer la feuille

Ma feuille de calcul ressemble actuellement à l'image ci-dessous :

![Sheets Sample](https://cdn.hashnode.com/res/hashnode/image/upload/v1693110060718/c5e5f9e6-2ddf-4ee1-a08c-3a0a8ba4de87.png)
_Feille de calcul avec beaucoup de lignes et colonnes vides_

Elle a quelques colonnes et lignes avec des données, avec beaucoup de lignes et colonnes vides.

Rendons les feuilles de calcul plus présentables comme dans l'image suivante :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693110269477/fd55cbfd-88f8-47b2-b0d1-69d1ced421b0.png)
_Version finale propre de la feuille de calcul_

## Comment ouvrir le projet Apps Script

Ensuite, ouvrons notre projet Apps Script à partir de l'onglet Extensions dans la feuille de calcul :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/open_apps_script-2.png)
_Ouvrir le projet Apps Script à partir de l'onglet de la feuille de calcul_

## Comment créer une fonction pour supprimer les lignes et colonnes vides en dehors de DataRange

Nous allons créer une fonction nommée `deleteExternalEmptyRowsNColumns()`.

Cette fonction sera responsable de la suppression de toutes les lignes et colonnes vides qui sont à l'extérieur de la plage de `getDataRange()` :

```javascript
/**
 * Supprime les lignes et colonnes vides en dehors de DataRange()
 */
function deleteExternalEmptyRowsNColumns() {
  // obtenir les feuilles et les données
  const ss = SpreadsheetApp.getActiveSheet();
  const data = ss.getDataRange().getValues();

  //console.log(data);

  // déterminer la dernière ligne et colonne
  const lastRow = data.length;
  const lastCol = data[0].length;

  // obtenir le nombre maximum de lignes et de colonnes
  const maxRows = ss.getMaxRows();
  const maxCols = ss.getMaxColumns();

  // supprimer les lignes et colonnes uniquement s'il y a des lignes ou colonnes vides au-delà de la dernière ligne et colonne
  if (maxRows > lastRow) {
    ss.deleteRows(lastRow + 1, maxRows - lastRow);
  }
  if (maxCols > lastCol) {
    ss.deleteColumns(lastCol + 1, maxCols - lastCol);
  }

}
```

Nous utilisons le nombre maximum de lignes et de colonnes car ces valeurs retourneront la dernière ligne et la dernière colonne de la feuille de calcul, indépendamment du contenu.

Cela signifie qu'elles incluent également les lignes vides et les colonnes vides au-delà de la plage de données.

Ensuite, nous ne supprimons les colonnes et les lignes que si elles sont à l'extérieur de la plage.

Cela signifie que si la ligne maximale est supérieure à la dernière ligne, alors nous supprimerons les lignes. Il en va de même pour les colonnes.

Nous utilisons la méthode [`deleteRows()`](https://developers.google.com/apps-script/reference/spreadsheet/sheet#deleterowsrowposition,-howmany) pour supprimer ces lignes, qui prend deux paramètres.

Le premier est l'index de la ligne à partir de laquelle les lignes doivent être supprimées, `lastRow + 1` dans notre cas.

Le deuxième paramètre est le nombre de lignes que nous devons supprimer, qui est `maxRows - lastRow` dans notre cas.

Pour les colonnes, nous utiliserons la méthode [`deleteColumns()`](https://developers.google.com/apps-script/reference/spreadsheet/sheet#deletecolumnscolumnposition,-howmany). Le fonctionnement de cette méthode est le même que celui de `deleteRows()` mais pour les colonnes.

Si vous exécutez cette fonction, votre feuille de calcul ressemblera à l'image suivante :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693112111932/eb0387b4-9b5a-49b3-9e9a-6b572d75be1e.png)
_Feille de calcul avec les colonnes et lignes hors limites supprimées_

Vous verrez que les colonnes et lignes qui étaient à l'extérieur de la plage retournée par `getDataRange()` ont maintenant été supprimées par la fonction.

## Comment créer une fonction pour supprimer les lignes et colonnes vides à l'intérieur de DataRange

Maintenant, nous allons créer une autre fonction : `deleteInternalEmptyRowsNColumns()`.

Celle-ci sera responsable de la suppression des lignes et colonnes vides qui sont incluses dans la méthode `getDataRange()`, avec cette fonction ci-dessous :

```javascript
/**
 * Supprime les lignes et colonnes vides à l'intérieur de DataRange()
 */
function deleteInternalEmptyRowsNColumns() {
  // obtenir les feuilles et les données
  const ss = SpreadsheetApp.getActiveSheet();
  const data = ss.getDataRange().getValues();

  const lastRow = data.length;
  const lastCol = data[0].length;

  // vérifions s'il y a des colonnes vides au début qui sont incluses dans les données
  const emptyColumnIndexes = [];
  for (let i = 1; i <= lastCol; i++) {
    if (ss.getRange(1, i, lastRow, 1).getValues().flat().join("") === "") {
      // soustraire la longueur avant de pousser la valeur avec moins de 1 de l'index original
      // car plus tard, lorsque nous supprimons les colonnes une par une, les index
      // seront hors limites/incorrects en raison de la mise à jour de la feuille avec de nouveaux index
      emptyColumnIndexes.push(i - emptyColumnIndexes.length);

    }

  }

  // supprimons ces colonnes
  if (emptyColumnIndexes.length > 0) {
    // supprimer la colonne
    emptyColumnIndexes.forEach(ind => ss.deleteColumn(ind));

  }

  //***************Supprimer les lignes vides internes */
  // convertir les tableaux imbriqués en chaîne et supprimer les chaînes vides avec filter
  const newData = ss.getDataRange().getValues().filter((arr) => arr.join("") !== "")

  const newLastRow = newData.length;
  const newLastCol = newData[0].length;

  // effacer les valeurs précédentes
  ss.clearContents();

  // définir les nouvelles valeurs
  ss.getRange(1, 1, newLastRow, newLastCol).setValues(newData);

// maintenant supprimer les lignes et colonnes vides
 deleteExternalEmptyRowsNColumns();
}
```

Expliquons ce que fait la fonction dans les sections suivantes.

### Comment supprimer les colonnes vides

Tout d'abord, nous allons travailler sur les colonnes vides. Après cela, nous supprimerons les lignes vides.

```javascript
 const emptyColumnIndexes = [];
  for (let i = 1; i <= lastCol; i++) {
    if (ss.getRange(1, i, lastRow, 1).getValues().flat().join("") === "") {
      // soustraire la longueur avant de pousser la valeur avec moins de 1 de l'index original
      // car plus tard, lorsque nous supprimons les colonnes une par une, les index
      // seront hors limites/incorrects en raison de la mise à jour de la feuille avec de nouveaux index
      emptyColumnIndexes.push(i - emptyColumnIndexes.length);

    }

  }

  // supprimons ces colonnes
  if (emptyColumnIndexes.length > 0) {
    // supprimer la colonne
    emptyColumnIndexes.forEach(ind => ss.deleteColumn(ind));

  }
```

Créons un tableau nommé `emptyColumnIndexes`. Il contiendra tous les index des colonnes qui sont vides.

Pour vérifier si les colonnes sont vides ou non, nous allons parcourir chaque colonne avec une boucle `for` en commençant par la première colonne.

Ensuite, nous allons récupérer les valeurs d'une colonne. À chaque boucle, elle retournera un tableau imbriqué et nous allons aplatir le tableau.

Après cela, nous allons joindre le tableau avec une chaîne vide ("").

Si la chaîne jointe est effectivement vide, nous savons que c'est une colonne vide, donc nous allons pousser cet index dans le tableau des index des colonnes vides avec le code suivant : `ss.getRange(1, i, lastRow, 1).getValues().flat().join("") === ""`.

Mais avant de pousser l'index, nous allons soustraire la longueur du tableau `emptyColumnIndexes` de l'index lui-même à chaque fois.

C'est parce que plus tard, lorsque nous supprimerons cette colonne, nous devons supprimer chaque colonne une par une.

En faisant cela, nous allons découvrir que si nous supprimons la première colonne, la structure de la feuille de calcul change, et les colonnes qui viennent après la colonne supprimée auront leur index changé.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693111825663/d8e82618-0404-4b89-89be-f22c33ed2d23.png)
_Feille de calcul avec colonnes et lignes vides internes_

Par exemple, à partir de l'image précédente, après avoir supprimé la colonne "A", l'index de la colonne "F" sera changé en "E".

Après cela, si `emptyColumnIndexes` n'est pas vide, nous allons parcourir chaque valeur en utilisant [forEach()](https://www.w3schools.com/jsref/jsref_foreach.asp).

Ensuite, nous allons supprimer la colonne avec la méthode [deleteColumn()](https://developers.google.com/apps-script/reference/spreadsheet/sheet#deletecolumncolumnposition).

Maintenant, exécutez cette fonction et vous verrez un résultat similaire à l'image suivante, où toutes les colonnes vides ont été supprimées :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693112373678/58a09e91-924f-4cef-a5ec-e437fcf1a597.png)
_Feille de calcul avec colonnes vides internes supprimées_

### Comment supprimer les lignes vides

Maintenant, nous allons travailler sur la suppression des lignes vides de notre feuille de calcul.

Pour ce faire, nous allons filtrer toutes les lignes non vides en utilisant le même processus que nous avons utilisé précédemment en les joignant avec une chaîne vide.

Si elles ne sont pas juste une citation vide (""), nous les retournerons comme les éléments du tableau dans `newData` avec `const newData = ss.getDataRange().getValues().filter((arr) => arr.join("") !== "")`.

Maintenant, nous allons sauvegarder ces valeurs dans notre feuille de calcul après avoir effacé le contenu précédent.

Mais si vous exécutez cette fonction maintenant, vous découvrirez que cela seul ne supprimera pas les colonnes vides mais accumulera les lignes en un seul endroit comme dans l'image ci-dessous :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693114104374/502bba63-dd4d-4d67-9635-0f2b2fc75358.png)
_Feille de calcul avec lignes vides externes_

Ce n'est pas ce que nous voulons.

Donc, pour supprimer ces lignes supplémentaires, nous allons simplement appeler la fonction `deleteExternalEmptyRowsNColumns()` que nous avons créée précédemment, car maintenant ces espaces supplémentaires sont à l'extérieur de la plage de `getDataRange()`.

Exécutons à nouveau la fonction, et maintenant nous serons en mesure d'accomplir ce que nous voulions initialement :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693114340988/7f0bf2d5-8f24-4e83-9389-ad6e833c2c4b.png)
_Feille de calcul propre_

## Comment créer un menu personnalisé pour la feuille de calcul

Enfin, nous allons créer un menu afin que nous puissions exécuter ces fonctions depuis la feuille de calcul elle-même.

Pour cela, créez un nouveau fichier de script dans votre projet nommé menu :

```javascript
/**
 * Le menu crée une interface de menu dans la feuille de calcul.
 */
function createCustomMenu() {
  let menu = SpreadsheetApp.getUi().createMenu("Supprimer les lignes et colonnes vides");

  menu.addItem("Supprimer les lignes et colonnes vides externes", "deleteExternalEmptyRowsNColumns");
  menu.addItem("Supprimer les lignes vides internes", "deleteInternalEmptyRowsNColumns");
  menu.addToUi();
}

/**
 * Déclencheur OnOpen qui crée le menu
 * @param {Dictionary} e
 */
function onOpen() {
  createCustomMenu();
}
```

Après avoir sauvegardé le script, nous allons retourner à la feuille de calcul et la recharger.

Après un moment, vous pourrez voir un menu dans l'onglet de la feuille de calcul comme dans l'image ci-dessous :

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1693114629659/3fc2f151-12c9-47d7-abc8-549b2937d9e7.png)
_Menu de la feuille de calcul_

Félicitations !

Maintenant, vous n'avez qu'à copier et coller le script de ce tutoriel ou de [ce](https://github.com/nibukdk/detete_empty_rows_n_columns_in_spreadsheet) dépôt GitHub et vous pourrez nettoyer vos feuilles instantanément.

## Conclusion

Dans ce tutoriel, nous avons créé deux fonctions : `deleteExternalEmptyRowsNColumns()` et `deleteInternalEmptyRowsNColumns()`.

Nous avons supprimé les lignes et colonnes vides qui étaient hors limites et avons ensuite supprimé les lignes et colonnes vides qui étaient dans les limites des données.

Ensuite, nous avons créé un menu qui offre un accès facile même aux non-codeurs pour exécuter les fonctions mentionnées ci-dessus à partir de l'onglet de la feuille de calcul.

Maintenant, il ne vous reste plus qu'à partager cet article. Si vous regardez également la version vidéo, j'espère que vous vous abonnerez à ma [chaîne](https://youtube.com/@codingWithNibesh) également.

Je suis Nibesh Khadka, un freelance spécialisé dans l'automatisation des produits Google avec Apps Script. Contactez-moi si vous avez besoin de mes services à me@nibeshkhadka.com.