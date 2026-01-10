---
title: Apprendre Google Apps Script – Créer une feuille de calcul Paint By Numbers
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-04-24T21:12:07.000Z'
originalURL: https://freecodecamp.org/news/learn-google-apps-script-build-a-paint-by-numbers-spreadsheet
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Google-Apps-Script-Paint-by-Numbers-Spreadsheet-final.jpg
tags:
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Apprendre Google Apps Script – Créer une feuille de calcul Paint By Numbers
seo_desc: "Spreadsheets are great for financial modeling, but they're also capable\
  \ of displaying pixel art. \nIn this Apps Script tutorial, we'll build a paint by\
  \ numbers spreadsheet using conditional formatting and a script that \"paints\"\
  \ a blank spreadsheet.\nYo..."
---

Les feuilles de calcul sont idéales pour la modélisation financière, mais elles peuvent également afficher de l'art pixelisé.

Dans ce tutoriel Apps Script, nous allons créer une feuille de calcul paint by numbers en utilisant la mise en forme conditionnelle et un script qui "peint" une feuille de calcul vierge.

Vous apprendrez à :

1. Importer des données
2. Appliquer un formatage de visualisation de données approprié
3. Coder quelques fonctions Apps Script pour la rendre interactive.

C'est parti 🎨

![Image](https://www.freecodecamp.org/news/content/images/2023/04/giphy.gif)
_Tenacious D en train de rocker_

## Vidéo de démonstration

Oui, j'ai une vidéo complète pour vous. Ouvrez-la pendant que vous lisez pour vous y référer et suivre 👇

%[https://youtu.be/zNqcLWGJlvQ]

Feuille de démonstration avec Pikachu : [https://docs.google.com/spreadsheets/d/1Zu0B0dE_N4UrgAAzlWKqbpmz2TL_qr9GYWS451O7UL0/edit#gid=0](https://docs.google.com/spreadsheets/d/1Zu0B0dE_N4UrgAAzlWKqbpmz2TL_qr9GYWS451O7UL0/edit#gid=0)

Feuille de démonstration avec Volcan : [https://docs.google.com/spreadsheets/d/11lOVseXtpB6xWxhrmZr1LfImI75TBDbof6mkFzz0ck4/edit#gid=0](https://docs.google.com/spreadsheets/d/11lOVseXtpB6xWxhrmZr1LfImI75TBDbof6mkFzz0ck4/edit#gid=0)

Vous pouvez créer une copie modifiable de l'une ou l'autre de ces feuilles en sélectionnant `Fichier -> Créer une copie`.

## Installation du projet

Tout ce que nous faisons aujourd'hui repose sur un formatage simple. Nous allons faire en sorte que les cellules prennent certaines couleurs en fonction du nombre qu'elles contiennent.

Voir l'image ci-dessous où toutes les cellules bleues contiennent le nombre 15. En définissant la couleur de la police et de l'arrière-plan sur bleu, nous pouvons créer l'effet de cellules de couleur unie.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-207.png)
_Image de l'art pixelisé de Pikachu_

Nous pouvons créer notre propre grille de nombres, mais il en existe une tonne disponibles. J'imprime celles-ci pour que mes enfants les colorient, et nous pouvons les importer dans notre feuille de calcul en quelques clics.

[Voici la grille du volcan](https://www.coloringsquared.com/worksheet/volcano-numbers-coloring-page/) que j'ai utilisée dans la vidéo de démonstration.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-226.png)
_Image de la grille de coloration par nombres du volcan_

Lorsque j'ai enregistré la vidéo de démonstration pour la première fois, je n'ai pas pu copier et coller depuis le PDF. Lorsque je l'ai fait, il a collé chaque nombre dans une seule cellule.

Au lieu de cela, en ouvrant d'abord dans Microsoft Word puis en copiant et collant depuis là, j'ai pu importer la grille de nombres dans la feuille Google.

Depuis, j'ai également découvert que lors de la copie et du collage depuis le PDF, parfois il importera les nombres dans la première cellule de chaque ligne :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-209.png)
_image de la grille de nombres dans Google Sheets_

Cela ne fonctionne pas non plus, car nous avons besoin de chaque nombre dans sa propre cellule. Mais, en appliquant la fonction `=SPLIT()`, nous pouvons y parvenir facilement.

`=SPLIT(A1," ")` séparera chaque valeur dans la cellule par les espaces vides. Ainsi, tous les nombres sont extraits dans leurs propres cellules dans la ligne.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-210.png)
_Image de la fonction Split dans Google Sheets_

Une fois que tous les nombres sont dans des cellules individuelles, appliquez un formatage à la feuille de calcul pour que chaque cellule soit un carré. Redimensionnez aussi grand ou aussi petit que vous le souhaitez. J'ai choisi une hauteur de ligne et de colonne de 30px.

Pour ce faire, sélectionnez les en-têtes de colonne en cliquant et en faisant glisser de A jusqu'à la fin des colonnes. Cliquez avec le bouton droit n'importe où dans la plage, et sélectionnez `Redimensionner les colonnes`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-211.png)
_Image du redimensionnement des colonnes dans Google Sheets_

Faites de même pour les lignes, en spécifiant 30px pour chacune.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-212.png)
_Image du redimensionnement des lignes dans Google Sheets_

Désactivez les lignes de grille en sélectionnant `Affichage -> Afficher -> Lignes de grille`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-213.png)
_Image des options d'affichage dans Google Sheets_

## Mise en forme conditionnelle

Sélectionnez toute la plage où se trouvent tous les nombres, puis cliquez sur `Format -> Mise en forme conditionnelle`.

Cliquez sur `Ajouter une nouvelle règle` et sous Règles de format, sélectionnez `Est égal à` dans le menu déroulant.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/equal.png)
_Image de la mise en forme conditionnelle dans Google Sheets_

Sous Style de formatage, suivez la légende des couleurs de la page de coloration que vous avez sélectionnée et ajustez les couleurs de police et d'arrière-plan selon chaque nombre.

Dans notre exemple, tous les nombres 10 doivent être bleus, donc nous entrons 10 puis nous avons le même bleu pour les couleurs d'arrière-plan et de police :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-215.png)
_Image des options de couleur dans Google Sheets_

### 🖠 Note importante

En raison du script que nous écrivons et de la manière dont nous le déclenchons, vous devez modifier le code HEX pour l'un de ces deux nombres. S'ils sont exactement les mêmes, cela provoquera une erreur plus tard.

Donc, entrez d'abord la même couleur pour les deux, puis ouvrez-en une et sélectionnez l'icône plus dans la palette de couleurs personnalisées.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/custom.png)
_Image des couleurs personnalisées dans Google Sheets_

Modifiez manuellement une valeur dans le code HEX d'un chiffre. Dans l'exemple, je l'ai changé de `#0b5294` à `#0b5394`. Visuellement, cela aura toujours la même apparence. Si cela est confus, assurez-vous de consulter la [vidéo de démonstration à 02:39](https://youtu.be/zNqcLWGJlvQ?t=159).

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-216.png)
_Image des couleurs personnalisées dans Google Sheets_

Faites cela pour chaque couleur dans votre œuvre d'art, et vous aurez une magnifique œuvre d'art pixelisé dans votre feuille de calcul. Cela seul est gratifiant ! 😀

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-217.png)
_Image de l'art pixelisé du volcan dans Google Sheets_

## Configuration d'Apps Script

Nommez la feuille sur laquelle nous nous trouvons en double-cliquant sur `Sheet1` en bas. Nous l'appellerons "art". Ensuite, créez une nouvelle feuille en cliquant sur l'icône plus dans la barre du bas. Nommez-la "canvas".

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-219.png)
_Image des noms de feuilles dans Google Sheets_

Configurez le canvas de la même manière que nous l'avons fait au début, mais sans la mise en forme conditionnelle. Faites en sorte que tout soit de la même taille, supprimez les lignes de grille et ajoutez une bordure autour de la plage `B2:T21` qui servira de cadre.

Maintenant, nous devons créer des boutons pour basculer dans chaque cellule. Dans Google Sheets, la façon de faire est d'ajouter des cases à cocher à toutes les cellules. Les cases à cocher contiendront soit une valeur `true`, soit `false`, et lorsque nous cliquerons dessus, elles changeront d'état.

Sélectionnez notre plage complète à nouveau, et sélectionnez `Données -> Validation des données`. Changez les critères en `Case à cocher` et sous Options avancées, sélectionnez `Rejeter la saisie`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-227.png)
_Image des règles de validation des données dans Google Sheets_

Cela donnera à notre script quelque chose à déclencher.

Formatez ces cases à cocher de la même manière que nous l'avons fait pour notre mise en forme conditionnelle : faites en sorte que l'arrière-plan soit blanc : `#ffffff`, et la couleur de la police légèrement différente : `#fffeff`. Ensuite, donnez-leur une taille de police énorme, comme 200. Cela nous permettra de cliquer n'importe où dans la cellule et de ne pas risquer de cliquer juste à l'extérieur de la bordure de la case elle-même.

Maintenant, ouvrons notre éditeur de code en sélectionnant `Extensions -> Apps Script`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-221.png)
_Image du menu Extensions dans Google Sheets_

## Logique du script

Nous devons copier et coller le formatage des cellules individuelles chaque fois que nous cliquons sur les cellules vides de notre canvas.

Pour ce faire, nous utiliserons une méthode de déclenchement `onEdit(e)` intégrée à Apps Script.

```javascript
function onEdit(e) {
  // obtenir la feuille active
  var sheet = SpreadsheetApp.getActiveSheet();

  // si nous ne sommes pas sur la feuille art...
  if(sheet.getName() != "art"){
```

Tout d'abord, nous allons récupérer la feuille active en tant que variable. Ensuite, en nous assurant que nous ne sommes pas sur la feuille "art", nous allons passer par les étapes pour récupérer et coller le formatage dont nous avons besoin...

```javascript
// obtenir la cellule active et sa référence de ligne, colonne
var activeRange = sheet.getActiveCell();
var row = activeRange.getRow();
var column = activeRange.getColumn();
```

Dans notre instruction conditionnelle if, nous allons créer trois variables supplémentaires afin que nous puissions récupérer la position de la cellule dans laquelle nous nous trouvons.

Ensuite, nous devons aller sur notre feuille "art" et récupérer le formatage de la cellule correspondante.

```javascript
var artRange = SpreadsheetApp.getActive().getSheetByName("art").getRange(row,column);
// obtenir la couleur d'arrière-plan de la même référence dans la feuille art
var backgroundColor = artRange.getBackground();
var fontColor = artRange.getFontColor();
```

Nous allons créer trois autres variables : une pour artRange qui récupère la plage de la feuille "art" en utilisant la `ligne` et la `colonne` sur lesquelles nous nous trouvons dans la feuille "canvas". Et puis deux variables pour les couleurs : une pour l'arrière-plan et une pour la police.

Maintenant, tout ce que nous devons faire est de définir la cellule de la feuille "canvas" avec les couleurs que nous venons de récupérer. J'ai également choisi de la faire basculer vers une cellule blanche vide si elle a déjà été colorée. Nous allons donc utiliser une autre instruction if pour gérer cela :

```javascript
trueFalse = activeRange.getValue();
if(trueFalse){
      // définir activeRange avec cette couleur d'arrière-plan
      activeRange.setBackground(backgroundColor);
      activeRange.setFontColor(fontColor);
    }
    else{
      activeRange.setBackground('#ffffff');
      activeRange.setFontColor('#fffeff');
    }
```

Tout d'abord, nous définissons une variable trueFalse égale à la valeur de activeRange. Cela est soit `true` soit `false` selon l'état de la case à cocher.

Si c'est false (la case à cocher n'est pas cochée), alors nous définissons les couleurs d'arrière-plan et de police en utilisant les variables que nous avons récupérées de notre feuille "art".

Voici le code complet de `onEdit(e)` :

```javascript
function onEdit(e) {
  // obtenir la feuille active
  var sheet = SpreadsheetApp.getActiveSheet();

  // si nous ne sommes pas sur la feuille art...
  if(sheet.getName() != "art"){

    // obtenir la cellule active et sa référence de ligne, colonne
    var activeRange = sheet.getActiveCell();
    var row = activeRange.getRow();
    var column = activeRange.getColumn();

    var artRange = SpreadsheetApp.getActive().getSheetByName("art").getRange(row,column);

    // obtenir la couleur d'arrière-plan de la même référence dans la feuille art
    var backgroundColor = artRange.getBackground();
    var fontColor = artRange.getFontColor();

    Logger.log(backgroundColor)
    Logger.log(fontColor)

    trueFalse = activeRange.getValue();

    if(trueFalse){
      // définir activeRange avec cette couleur d'arrière-plan
      activeRange.setBackground(backgroundColor);
      activeRange.setFontColor(fontColor);
    }
    else{
      activeRange.setBackground('#ffffff');
      activeRange.setFontColor('#fffeff');
    }
  }
}
```

## Fonction de réinitialisation

En tant que fonctionnalité supplémentaire, nous allons ajouter un bouton réel pour réinitialiser le canvas. Pour ce faire, nous allons créer une nouvelle fonction dans notre éditeur de code Apps Script.

Nous allons récupérer la feuille et toutes les cases à cocher en tant que variables. Pour obtenir les cases à cocher, nous allons utiliser la méthode `getRangebyName()` sur notre plage 'canvasArt'.

Ensuite, Apps Script rend cela assez facile avec des méthodes intégrées. Nous définissons la valeur de toutes les cases à cocher sur `false`, la couleur d'arrière-plan sur `#ffffff`, et la couleur de la police sur `#fffeff`.

Voici le code complet de `reset()` :

```javascript
function reset(){
  var sheet = SpreadsheetApp.getActive();
  var checkboxes = sheet.getRangeByName('canvasArt');
  checkboxes.setValue(false);
  checkboxes.setBackground("#ffffff");
  checkboxes.setFontColor("#fffeff");
}
```

## Déclenchement avec un bouton

Pour créer un bouton dans la feuille de calcul, sélectionnez `Insertion -> Dessin`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-222.png)
_Image du menu Insertion dans Google Sheets_

Sélectionnez la forme de rectangle arrondi et faites-la glisser sur la grille.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-223.png)
_Image du menu Formes dans Google Sheets_

Double-cliquez dans la forme pour écrire "EFFACER". Ajustez la police et les couleurs comme vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-224.png)
_Image du dessin du bouton dans Google Sheets_

Cliquez sur Enregistrer et Fermer, puis faites-le glisser pour le redimensionner et le repositionner sur votre feuille en bas du canvas.

Une fois que vous l'avez positionné, cliquez sur les trois cercles en haut à droite, sélectionnez `Attribuer un script`, et tapez le nom du script que vous souhaitez qu'il déclenche (dans notre cas, `reset`).

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-225.png)
_Image de l'attribution d'un script à un bouton dans Google Sheets_

Maintenant, lorsque vous cliquez sur ce bouton, ce script s'exécutera et effacera toute la toile d'art.

## Conclusion

J'espère que cela a été utile pour vous ! J'ai passé un excellent moment à faire cela, et j'ai d'autres contenus de feuilles de calcul de type jeu à venir bientôt.

Venez me suivre sur [YouTube](https://www.youtube.com/@eamonncottrell), et dites bonjour sur [LinkedIn](https://www.linkedin.com/in/eamonncottrell/).

Passez une excellente journée ! 👋