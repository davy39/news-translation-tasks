---
title: Comment créer une image pop-up dans votre feuille de calcul
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2024-05-16T10:17:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-image-lightbox
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Lightbox-2-1.jpg
tags:
- name: google apps script
  slug: google-apps-script
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment créer une image pop-up dans votre feuille de calcul
seo_desc: 'In this article, I''ll show you two ways to create a lightbox effect in
  a spreadsheet. The first will trigger the image to be displayed in a large area
  in the sheet. The second will be an actual HTML popup on top of the sheet.

  If you want to follow al...'
---

Dans cet article, je vais vous montrer deux façons de créer un effet lightbox dans une feuille de calcul. La première déclenchera l'affichage de l'image dans une grande zone de la feuille. La seconde sera une véritable fenêtre contextuelle HTML au-dessus de la feuille.

Si vous souhaitez suivre avec la feuille que j'ai utilisée, vous pouvez y accéder [ici](https://docs.google.com/spreadsheets/d/1Uz9sZJW1ts_YZc2-Ifd-UAQ8Pkgn23XLzmNdE_sDYrg/copy). Le lien vous invitera à créer une copie de la feuille de calcul et du fichier Apps Script associé.

## Qu'est-ce qu'une Lightbox d'image ?

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-35.png)
_miniatures d'images dans une feuille de calcul_

Une lightbox d'image est ce que nous appelons lorsque nous survolons ou cliquons sur une image et qu'elle s'affiche en version agrandie à l'écran.

C'est quelque chose que nous avons l'habitude de voir sur les sites web, et cela donne une touche agréable et professionnelle lorsque c'est bien fait.

Mais qu'en est-il dans une feuille de calcul ? 🤔

Eh bien, nous avons deux versions de solution :

1. Utiliser des fonctions intégrées pour afficher une version plus grande dans une cellule plus grande.
2. Utiliser Apps Script pour créer une boîte de dialogue contextuelle au-dessus de notre feuille de calcul.

En bonus à la première solution, nous inclurons également un Apps Script optionnel pour rendre les choses un peu plus fluides. Plus d'informations à ce sujet ci-dessous 😉.

Comme d'habitude, voici une vidéo de démonstration où je passe par tout le processus :

%[https://youtu.be/J39nMbuycEk]

## Image Popup avec des fonctions intégrées

Tout d'abord, nous avons besoin d'images dans des cellules. Dans le menu supérieur, `Insertion - Image - Insérer une image dans une cellule` fera l'affaire.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-37.png)
_insertion d'une image dans une cellule de feuille de calcul_

Ensuite, nous devons fusionner certaines cellules ensemble afin qu'il y ait un conteneur plus grand qui contiendra notre image plus grande après l'étape suivante.

Vous pouvez utiliser une seule cellule et changer sa largeur et sa hauteur, mais dans ma [feuille d'exemple](https://docs.google.com/spreadsheets/d/1Uz9sZJW1ts_YZc2-Ifd-UAQ8Pkgn23XLzmNdE_sDYrg/copy), la zone "lightbox" partage des lignes avec le reste des données, donc je ne voulais pas faire cela.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-38.png)
_une grande plage de cellules fusionnées_

Dans la colonne à côté de mes miniatures d'images, j'ai mis des cases à cocher en sélectionnant `Données - Validation des données - Critères : Cases à cocher` dans le menu supérieur.

Cela nous permettra de sélectionner quelle image afficher en grand dans notre zone lightbox.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-39.png)
_validation des données dans google sheets_

J'ai nommé la plage `A2:A11` comme `pics` et la plage `B2:B11` comme `checkboxes` pour permettre une meilleure lisibilité dans la fonction que nous allons écrire ensuite.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-41.png)
_plages nommées dans google sheets_

Il ne reste plus qu'une fonction `XLOOKUP()` à mettre dans notre plage lightbox.

`=XLOOKUP(TRUE,checkboxes,pics,"")` est la fonction qui recherche une case cochée puis affiche l'image correspondante. En mettant cela dans une grande cellule ou une plage de cellules fusionnées, nous pouvons afficher n'importe quelle petite image que nous sélectionnons dans la zone plus grande.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-40.png)
_fonction xlookup dans google sheets_

Rappelez-vous, une case à cocher ne fait que stocker une valeur `TRUE` (cochée) ou `FALSE` (non cochée).

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-42.png)
_cases à cocher et miniatures d'images dans google sheets_

## 🚨🸏AVERTISSEMENT🚨🸏

Cela pose cependant un problème. Savez-vous lequel ?

`XLOOKUP()` va retourner la première case cochée qu'elle rencontre avec une valeur TRUE. Donc si vous avez plusieurs images cochées, elle ne va afficher que _la première qu'elle rencontre_, pas la plus _récemment cliquée_.

Pour contourner cela, écrivons un peu de code.

## Amélioration avec Apps Script

Ouvrez Apps Script en sélectionnant `Extensions - Apps Script` dans le menu supérieur.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-46.png)
_ouverture d'apps script dans google sheets_

Supprimez la fonction intégrée dans l'éditeur de code qui s'ouvre. Nous allons commencer à partir de zéro avec une fonction `onEdit` :

```javascript
function onEdit(e) {
```

Nous devons récupérer la plage que nous sommes en train d'éditer.

```javascript
var range = e.range
```

Ensuite, la plage des cases à cocher.

```javascript
var checkboxes = SpreadsheetApp.getActive().getRangeByName("checkboxes")
```

Ensuite, nous devons vérifier si ce que nous venons d'éditer est dans cette plage de cases à cocher.

```javascript
if (range.getColumn() == 2 && range.getRow() >= 2 && range.getRow() <= 10)
```

Si c'était une case à cocher, alors nous voulons décocher toutes les cases à cocher et recocher celle que nous venons de cocher.

```javascript
// Décocher toutes les autres cases à cocher dans la plage
checkboxes.uncheck();
// Cocher la cellule éditée
range.check();
```

Maintenant, il y a un léger délai lorsque vous exécutez le code. Après avoir cliqué sur une case à cocher, toutes les cases sont effacées juste avant que celle que vous avez cochée soit cochée à nouveau.

Voici à quoi ressemble le code complet :

```javascript
function onEdit(e) {
  var range = e.range;
  var checkboxes = SpreadsheetApp.getActive().getRangeByName("checkboxes")

  // Vérifier si la cellule éditée est une case à cocher dans la plage souhaitée
  if (range.getColumn() == 2 && range.getRow() >= 2 && range.getRow() <= 10) {
    // Décocher toutes les autres cases à cocher dans la plage
    checkboxes.uncheck();
    // Cocher la cellule éditée
    range.check();
  }
}
```

## Une vraie boîte de dialogue contextuelle avec HTML

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-43.png)
_boîte de dialogue modale dans google sheets_

D'accord, c'est bien. Mais qu'en est-il de la vraie chose ?

Cela nécessite plus d'Apps Script, mais c'est réalisable grâce à la méthode intégrée `showModalDialog`.

C'est essentiellement une fenêtre contextuelle qui peut contenir du HTML. Et comme l'internet est construit avec HTML, tout ce que nous avons à faire est d'utiliser un peu de HTML pour insérer une image.

Cette méthode nécessite une image disponible sur internet quelque part. Donc, nous ne pouvons pas référencer l'image que nous avons intégrée dans notre feuille et l'utiliser dans le HTML que nous allons écrire.

Bizarre, je sais.

Trouvons une URL d'image que nous pouvons utiliser. J'ai pris un aigle sur [unsplash](https://unsplash.com/).

Nous allons stocker cela dans une variable.

```javascript
var imageURL = "https://images.unsplash.com/photo-1715002383611-63488b956401?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
```

Ensuite, nous devons construire notre HTML. Dans notre cas, tout ce que nous voulons est un élément, donc nous ne nous soucierons pas de construire une page complète et sémantiquement correcte (bien que nous pourrions certainement 😉)

Une autre variable contiendra cet élément `img` :

```javascript
var html = '<img src="' + imageURL + '" style="max-width: 100%; max-height: 100%;">';
```

Nous avons accès à [Class Ui](https://developers.google.com/apps-script/reference/base/ui) dans Apps Script où nous pouvons "...ajouter des fonctionnalités comme des menus, des dialogues et des barres latérales."

```javascript
  var ui = SpreadsheetApp.getUi();
```

Et enfin, en appelant la méthode `showModalDialog()`, nous pouvons générer du HTML à partir de notre variable `html` en utilisant [Class HtmlService](https://developers.google.com/apps-script/reference/html/html-service).

```javascript
ui.showModalDialog(HtmlService.createHtmlOutput(html).setWidth(700).setHeight(1000), 'Aigle 🦅');
```

Une dernière touche consiste à ajouter une version miniature de notre image d'aigle dans notre feuille de calcul afin qu'elle soit insérée au-dessus de nos cellules (ce qui suit ne fonctionnera pas si elle est intégrée dans une cellule elle-même).

Une fois qu'elle est dans notre feuille, nous pouvons cliquer sur les trois points noirs dans le coin supérieur droit et assigner un script directement à l'image.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-44.png)
_assigner un script à une image dans google sheets_

Nous avons nommé notre script `displayImagePopup`, donc c'est ce que nous entrons. Assurez-vous de ne pas mettre les parenthèses lorsque vous le tapez dans le formulaire de script de l'image.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-45.png)
_assigner un script_

Maintenant, chaque fois que nous cliquons sur la petite image de l'aigle, une boîte de dialogue contextuelle s'ouvre avec l'image complète.

Voici à quoi ressemble le code complet :

```javascript
function displayImagePopup() {
  // Obtenir la feuille active
  var sheet = SpreadsheetApp.getActiveSheet();
  var imageURL = "https://images.unsplash.com/photo-1715002383611-63488b956401?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
  // Créer une chaîne HTML pour la fenêtre contextuelle
  var html = '<img src="' + imageURL + '" style="max-width: 100%; max-height: 100%;">';
  
  // Afficher la boîte de dialogue
  var ui = SpreadsheetApp.getUi();
  ui.showModalDialog(HtmlService.createHtmlOutput(html).setWidth(700).setHeight(1000), 'Aigle 🦅');
}
```

## Merci beaucoup !

J'espère que cela vous a été utile. 

Consultez ma [chaîne YouTube](https://www.youtube.com/@eamonncottrell) et mon [bulletin d'information gratuit](https://www.gotsheet.xyz/subscribe) pour devenir bon avec les feuilles de calcul !