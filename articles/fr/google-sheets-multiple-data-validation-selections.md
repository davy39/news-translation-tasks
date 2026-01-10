---
title: Tutoriel Google Sheets – Comment activer la validation de données à sélection
  multiple à l'aide d'Apps Script
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-01-30T17:30:58.000Z'
originalURL: https://freecodecamp.org/news/google-sheets-multiple-data-validation-selections
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/multiple-selection-data-validation.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Tutoriel Google Sheets – Comment activer la validation de données à sélection
  multiple à l'aide d'Apps Script
seo_desc: 'In this article I will show you how to allow for multiple items to be selected
  using the drop-down data validation feature in Google Sheets.

  Here''s the Google Sheet we''ll use for the example. You can make a copy of this
  to edit yourself by clicking F...'
---

Dans cet article, je vais vous montrer comment permettre la sélection de plusieurs éléments à l'aide de la fonctionnalité de validation de données par liste déroulante dans Google Sheets.

[Voici la feuille Google](https://docs.google.com/spreadsheets/d/1yxc4k1x5idcS_moQ1Bq8LnHGZF2nm9dpARglY7Rv0UI/edit#gid=390071620) que nous utiliserons pour l'exemple. Vous pouvez en faire une copie pour l'éditer vous-même en cliquant sur `Fichier -> Créer une copie`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-13.png)

À la fin de l'article, vous trouverez une vidéo explicative que j'ai enregistrée pour cette solution. 👋

## Le Problème 🤔

Mon fils de cinq ans a posé une question qui m'a plongé dans une exploration approfondie de Google Apps Script. Il voulait pouvoir sélectionner plusieurs éléments à partir d'une liste déroulante de validation de données.

Laissez un enfant de cinq ans vous envoyer sur Google, YouTube et au-delà à la recherche d'une solution pour une feuille de calcul ! 😅

![Image](https://www.freecodecamp.org/news/content/images/2023/01/michelangelo.gif)
_Gif de Michelangelo des Tortues Ninja_

Nous avions créé une feuille de calcul qui affichait des informations sur les Tortues Ninja. Noms, anniversaires, âges, couleurs préférées...

Je mettais en avant le pouvoir incroyable des feuilles de calcul pour organiser, calculer et visualiser des informations. Des trucs typiques de parent d'un enfant de cinq ans.

Pour la colonne des couleurs préférées, nous avons utilisé une liste déroulante pour sélectionner parmi une liste de couleurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-3.png)

C'est une fonctionnalité assez simple à utiliser dans Google Sheets. Pour créer une liste déroulante, sélectionnez `Données -> Validation des données` dans le menu :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-4.png)
_Capture d'écran du menu de données de Google Sheets_

Mise à jour : la même fonctionnalité est désormais également disponible lorsque vous faites un clic droit sur une cellule :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-5.png)
_Capture d'écran du menu de clic droit dans Google Sheets_

Dans les deux cas, un menu de validation des données apparaîtra où vous pourrez définir vos conditions.

Nous avions notre liste de couleurs dans les cellules `H2:H9`, donc nous avons sélectionné `Liste déroulante (à partir d'une plage)` dans la section Critères et avons ensuite entré cette plage.

Nous voulions que cela soit copié dans d'autres cellules sans affecter cette plage, donc nous l'avons verrouillée en place, en utilisant les signes $ : `=$H$2:$H$9`.

Cela permet à la validation d'être copiée dans d'autres cellules tout en conservant ces références de cellules pour la liste des valeurs de couleurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-7.png)
_Capture d'écran du menu des options de validation des données de Google Sheets_

## Google Sheets permet une seule sélection 🚫

Le problème est que Google Sheets ne permet qu'une seule sélection. Nous voulions que Léonard ait plusieurs couleurs préférées !

Heureusement, Google Apps Script permet d'écrire du code personnalisé dans Google Sheets, et nous avons utilisé cela pour résoudre notre problème.

Je suis tombé sur le code pour cela à partir d'une vidéo [YouTube](https://www.youtube.com/watch?v=dm4z9l26O0I) d'Alexander Ivanov et j'ai entrepris de mettre à jour les informations avec une vidéo et une explication plus claires de ma part.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/problem-solved.gif)
_Gif Problème résolu_

## Comment utiliser Apps Script👨‍💻

Ouvrez l'écran Apps Script en sélectionnant `Extensions -> Apps Script` dans la barre de menu.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-9.png)

Vous pourrez créer des fichiers en utilisant l'icône plus `+`. Pour ce projet, nous avons besoin d'un fichier `Code.gs` et d'un fichier `Page.html`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-8.png)

## Le fichier Code.gs

Commencez dans le fichier Code.gs.

La première chose que nous voulons est une liste déroulante à partir de la barre d'outils de Google Sheets pour exécuter notre code.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-14.png)
_Capture d'écran de la barre d'outils personnalisée de Google Sheets_

Pour ce faire, nous utilisons le code suivant pour ajouter l'option d'interface utilisateur `Afficher la boîte de dialogue` à la barre de menu. En cliquant dessus, cela exécutera la fonction `showDialog`. En enveloppant ces méthodes dans la fonction intégrée `onOpen`, ce menu dans la barre d'outils est ajouté dès que nous ouvrons la feuille de calcul.

```javascript
function onOpen(e) {								
	SpreadsheetApp.getUi()								
	.createMenu('Validation de données à sélection multiple')
	.addItem('Afficher la boîte de dialogue', 'showDialog')								
	.addToUi();								
}	
```

Il y a souvent un court délai de quelques secondes avant que les menus personnalisés ne soient visibles dans le menu. Donnez-lui quelques secondes et il apparaîtra.

La fonction `showDialog` créera une variable HTML à partir d'un modèle que nous allons créer dans un instant. Elle utilise ensuite la méthode intégrée `.showSidebar` pour créer une barre latérale avec ce HTML.

```javascript
function showDialog() {								
	var html = HtmlService.createTemplateFromFile('Page').evaluate();
	SpreadsheetApp.getUi().showSidebar(html);								
}
```

Ensuite, nous avons une autre fonction, `valid`, qui vérifie la cellule actuelle pour tout critère de validation de données et renvoie ces valeurs dans un tableau à deux dimensions.

```javascript
var valid = function(){								
	try{								
		return SpreadsheetApp.getActiveRange().getDataValidation().getCriteriaValues()[0].getValues();								
    }catch(e){								
        return null								
    }								
}	
```

Et notre fonction finale, `fillCell`, créera un tableau pour contenir la liste résultante des valeurs que nous voulons que la cellule contienne. Elle pousse ensuite ces chaînes dans le tableau et les sépare par des virgules.

Enfin, elle utilise la méthode intégrée, `setValue`, pour remplir la cellule actuelle avec les valeurs séparées par des virgules (nos couleurs préférées).

(`fillCell` et `valid` sont appelés dans le code Page.html que nous allons passer en revue.)

```javascript
function fillCell(e){								
	var s = [];								
	for(var i in e){								
		if(i.substr(0, 2) == 'ch') s.push(e[i]);								
}								
    if(s.length) SpreadsheetApp.getActiveRange().setValue(s.join(', '));
}
```

Voici le code complet pour le fichier `Code.gs` :

```javascript
function onOpen(e) {								
	SpreadsheetApp.getUi()								
	.createMenu('Validation de données à sélection multiple')
	.addItem('Afficher la boîte de dialogue', 'showDialog')								
	.addToUi();								
}								
function showDialog() {								
	var html = HtmlService.createTemplateFromFile('Page').evaluate();
	SpreadsheetApp.getUi().showSidebar(html);								
}								
var valid = function(){								
	try{								
		return SpreadsheetApp.getActiveRange().getDataValidation().getCriteriaValues()[0].getValues();								
    }catch(e){								
        return null								
    }								
}								
function fillCell(e){								
	var s = [];								
	for(var i in e){								
		if(i.substr(0, 2) == 'ch') s.push(e[i]);								
}								
    if(s.length) SpreadsheetApp.getActiveRange().setValue(s.join(', '));
}
```

## Le fichier Page.html

Maintenant, créez et ouvrez un fichier appelé `Page.html`.

Cela contrôlera une barre latérale contextuelle où nous gérerons nos sélections multiples, et contiendra :

1. un formulaire avec des cases à cocher à côté de chaque option
2. un bouton pour remplir la cellule actuelle
3. un bouton pour obtenir la validation de la cellule actuelle

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-10.png)
_Capture d'écran de notre barre latérale HTML personnalisée de Google Sheets_

Nous utiliserons du HTML modélisé pour notre exemple. Tout d'abord, créez une variable, `data`, en appelant la fonction `valid()` que nous avons créée ci-dessus. Nous utilisons la syntaxe `<? CODE_GOES_HERE ?>` pour écrire du code dans le modèle HTML.

```javascript
<? var data = valid(); ?>
```

Ensuite, nous créons un formulaire pour héberger toutes les données extraites de la fonction `valid()` :

```html
<form id="form" name="form">
</form>
    
```

Et nous exécuterons un peu de code pour construire notre liste de cases à cocher dans ce formulaire. Tout d'abord, nous vérifions si les données dans la cellule sont de type `[object Array]`.

```javascript
<? if(Object.prototype.toString.call(data) === '[object Array]') { ?>
```

`valid()` renvoie un tableau à deux dimensions car il utilise la méthode intégrée `getValues()`. Donc, vous pouvez imaginer que cela est renvoyé comme un tableau de tableaux, chacun étant l'une des couleurs préférées :

```javascript
//pour illustration seulement ; c'est le type de tableau 2D que valid() renverra

favoriteColors = [
    ["purple"],
    ["red"],
    ["white"],
    ["black"]
]
```

Cela aidera lorsque nous examinerons le prochain morceau de code qui peut sembler écrasant.

Nous devons accéder à chaque couleur – les chaînes. Nous faisons cela en imbriquant des boucles `for`. La première boucle itère à travers chaque position dans le tableau des couleurs préférées.

```javascript
<? for (var i = 0; i < data.length; i++) { ?>
```

La deuxième boucle itère à travers chaque élément dans les tableaux intérieurs. Dans notre cas, cela sera toujours un élément puisque chacun de ces tableaux a une longueur de 1.

```javascript
<? for (var j = 0; j < data[i].length; j++) { ?>
```

Rappelez-vous, `["purple"]` est un tableau de longueur 1. La boucle `j` ne compte pas les lettres dans la chaîne _à l'intérieur_ du tableau – nous comptons simplement la longueur _du_ tableau.

Donc, nous parcourons chaque élément dans le tableau 2D et créons une entrée de case à cocher pour chacun :

```javascript
<input type="checkbox" id="ch<?= '' + i + j ?>" name="ch<?= '' + i + j ?>" value="<?= data[i][j] ?>"><?= data[i][j] ?><br>
```

Cela ajoute un `id` et un `name` qui commencent par "ch" puis ajoute la position du tableau de l'élément. Il extrait également la valeur (la couleur) elle-même en tant que `value` en plus du texte affiché.

Ces captures d'écran peuvent aider à connecter les points mentaux :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-11.png)
_capture d'écran de l'élément inspecté : l'entrée avec un id_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-12.png)
_capture d'écran de l'élément inspecté : le formulaire et les éléments d'entrée_

Si notre instruction `if` initiale échoue, nous afficherons un `<p>` indiquant qu'il n'y a peut-être pas de règles de validation de données dans cette cellule tout en liant à un article de support montrant comment créer une liste déroulante dans la cellule.

```javascript
else { ?>								
	<p>Peut-être que la cellule actuelle n'a pas de <a href="https://support.google.com/drive/answer/139705?hl=en">validation de données...</a></p>								
<? } ?>
```

### Comment coder les boutons

Ensuite, nous avons besoin de nos deux boutons.

Le premier bouton extrait la validation de données de la cellule. Il exécute la fonction `showDialog()` que nous avons créée dans `Code.gs` et construit le formulaire des entrées de cases à cocher s'il existe des valeurs de validation de données.

```javascript
// obtenir la validation de la cellule actuelle
<input type="button" value="obtenir la validation de la cellule actuelle" onclick="google.script.run.showDialog()" />
```

Le deuxième bouton remplit les valeurs sélectionnées dans la cellule actuelle. **C'est ce que nous voulions depuis le début !** Cela exécute la fonction `fillCell` dans `Code.gs`.

```javascript
// remplit les valeurs dans la cellule actuelle
<input type="button" value="remplir la cellule actuelle" onclick="google.script.run.fillCell(this.parentNode)" />
```

Voici le code complet pour `Page.html` :

```javascript
<div>								
<? var data = valid(); ?>								
<form id="form" name="form">								
<? if(Object.prototype.toString.call(data) === '[object Array]') { ?>								
<? for (var i = 0; i < data.length; i++) { ?>								
    <? for (var j = 0; j < data[i].length; j++) { ?>								
        <input type="checkbox" id="ch<?= '' + i + j ?>" name="ch<?= '' + i + j ?>" value="<?= data[i][j] ?>"><?= data[i][j] ?><br>								
    <? } ?>								
<? } ?>								
<? } else { ?>								
        <p>Peut-être que la cellule actuelle n'a pas de <a href="https://support.google.com/drive/answer/139705?hl=en">validation de données...</a></p>								
<? } ?>								
    <input type="button" value="remplir la cellule actuelle" onclick="google.script.run.fillCell(this.parentNode)" />								
    <input type="button" value="obtenir la validation de la cellule actuelle" onclick="google.script.run.showDialog()" />								
</form>								
</div>	
```

## Résumé

Oui, c'est une solution assez lourde pour quelque chose de relativement simple. Peut-être que Google ajoutera cela à la fonctionnalité native à un moment donné. Ils ont récemment mis à jour la validation des données pour inclure des fonctionnalités plus modernes et faciles à utiliser, donc ce n'est pas hors de question.

En attendant, cela a été une excellente solution pour moi, et je suis reconnaissant à [Alexander](https://www.youtube.com/watch?v=dm4z9l26O0I) pour son code initial.

J'espère que cet article vous a aidé à mieux comprendre le code et qu'il vous donne les moyens de créer vos propres solutions personnalisées pour Google Sheets !

Comme promis, voici ma vidéo explicative :

## Vidéo explicative 📹️

%[https://youtu.be/41ydIPKZezE]

## Merci !

Merci d'avoir lu ! Si vous avez trouvé cela utile, j'adorerais que vous me suiviez et que vous disiez bonjour 👋 sur [LinkedIn](https://www.linkedin.com/in/eamonncottrell/) et [YouTube](https://www.youtube.com/@eamonncottrell) où vous pouvez trouver plus de contenu comme celui-ci.

Passez une excellente journée !