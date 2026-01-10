---
title: Comment coder le mode sombre pour Google Sheets avec Apps Script et JavaScript
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-09-20T22:23:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-dark-mode-for-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/code-your-own-dark-mode.png
tags:
- name: dark mode
  slug: dark-mode
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
- name: JavaScript
  slug: javascript
seo_title: Comment coder le mode sombre pour Google Sheets avec Apps Script et JavaScript
seo_desc: "Google Sheets is a great tool for working and collaborating on spreadsheets,\
  \ but it doesn't have native support for dark mode. \nIn this article, we'll create\
  \ our own dark mode. One way to do that would be by selecting all the cells and\
  \ manually chang..."
---

Google Sheets est un excellent outil pour travailler et collaborer sur des feuilles de calcul, mais il ne prend pas en charge nativement le mode sombre. 

Dans cet article, nous allons créer notre propre mode sombre. Une façon de le faire serait de sélectionner toutes les cellules et de changer manuellement leur couleur de fond et leur couleur de police. Cela fera le travail, mais nous pouvons automatiser le processus et ajouter plus d'options de style parmi lesquelles choisir.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/automate-2.gif)
_gif d'un personnage de dessin animé attrapant un ordinateur_

Voici ce que nous allons construire : un sélecteur de style qui propose quatre styles différents, déclenchés soit par un nouveau menu déroulant, soit en cliquant sur une icône de bouton personnalisée.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-12.png)
_capture d'écran de Google Sheets avec différents modes de fond_

Et voici la vidéo de présentation si vous préférez suivre celle-ci : 

%[https://youtu.be/TxSGuXPav70]

## Comment créer un mode sombre dans Apps Script

Nous allons créer quatre fonctions, une pour chaque mode de style. Chacune de nos fonctions effectuera les actions suivantes :

1. Définir la couleur de fond
2. Définir la couleur de la police
3. Définir la famille de polices
4. Définir la couleur et le style de la bordure

Examinons comment créer une fonction `darkMode` dans [Apps Script](https://script.google.com/home/start). Nous définirons chaque fonction avec le mot-clé `function`, suivi du nom que nous lui donnerons.

Puisque les fonctions ne prennent aucun argument (elles s'exécutent sans avoir besoin de plus d'informations de notre part), nous avons des parenthèses ouvertes et fermées sans rien à l'intérieur, suivies d'une accolade ouverte.

Tout notre code pour la fonction se trouve entre les accolades de la fonction `darkMode` :

```javascript
function darkMode() {
  SpreadsheetApp.getActive().getRange('A1:Z')
    .setBackground("#333333")
    .setFontColor("white")
    .setFontFamily("Google Sans")
    .setBorder(false,false,false,false,true,
     true,"#444444",SpreadsheetApp.BorderStyle.SOLID)
}
```

Pour sélectionner toutes les cellules, nous avons utilisé les méthodes intégrées de la classe `SpreadsheetApp` : `getActive()` et `getRange()`. Celles-ci sélectionnent la feuille active ainsi qu'une plage donnée.

Dans notre cas, nous allons utiliser `A1:Z` comme plage, mais vous pouvez l'étendre davantage si vous le souhaitez. Par exemple, `A1:AZ` ajouterait les colonnes `AA:AZ` et appliquerait ensuite notre style à celles-ci.

Les quatre lignes qui suivent sont simplement des extensions de notation par points indiquant les styles à appliquer. Vous pouvez écrire cela sur une seule ligne si vous le souhaitez, mais il est bon de faire des sauts de ligne pour rendre le code facile à lire.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/clever.gif)
_gif d'un homme disant, c'est malin_

## Comment définir les couleurs et les polices

Vous remarquerez que nous avons utilisé à la fois `setBackground(#333333)` et `setFontColor("white")` dans le code. Cela est dû au fait que nous pouvons utiliser des couleurs en notation CSS soit au format hexadécimal, soit en utilisant le nom de la couleur.

En utilisant `setFontFamily("Google Sans")`, nous lui avons donné le nom de la famille de polices entre guillemets. Étant un produit Google, vous pouvez utiliser n'importe laquelle des [Google Fonts](https://fonts.google.com/) ainsi que la police Google Sans de Google, comme je l'ai découvert en réalisant ce projet.

## Comment définir la bordure

La fonction `setBorder(false,false,false,false,true, true,"#444444",SpreadsheetApp.BorderStyle.SOLID)` vous permet d'entrer des valeurs `true` ou `false` pour les bordures supérieure, gauche, inférieure, droite, verticale ou horizontale, dans cet ordre, suivies de la couleur et du style.

Pour définir le style, nous avons dû invoquer un attribut Enum intégré — `BorderStyle` — pour changer le style de la bordure.

## Comment créer le menu de style

Pour pouvoir sélectionner l'un des styles que nous créons à partir de la feuille de calcul elle-même, nous avons besoin d'un menu.

Pour ajouter le menu, nous allons créer une nouvelle fonction appelée `onOpen()` qui s'exécute dès que la feuille de calcul s'ouvre, puis utiliser les méthodes intégrées de `getUi()` pour construire notre menu personnalisé.

Nous pouvons créer le menu avec `.createMenu()` puis ajouter chacune de nos fonctions au menu avec la fonction `addItem()`.

Voici le code :

```javascript
function onOpen(){
  SpreadsheetApp.getUi()
    .createMenu('Style')
    .addItem("Sombre","darkMode")
    .addItem("Papyrus","papyrusMode")
    .addItem("Clair","lightMode")
    .addItem("Synth","synthMode")
    .addToUi();
}
```

Google Apps Script s'intègre automatiquement avec les applications Google Workspace (comme Google Sheets), donc les fonctions que nous avons ajoutées dans le code rendront les fonctionnalités accessibles dans vos Google Sheets.

## Comment ajouter des boutons d'icônes

En bonus, j'ai ajouté quatre images d'icônes à la feuille, et en sélectionnant `Assign script`, nous pouvons faire en sorte que ces icônes agissent comme des boutons pour déclencher l'un des quatre styles que nous avons créés :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2.png)
_capture d'écran des icônes dans la feuille de calcul_

Lorsque vous tapez le nom de la fonction dans la boîte de dialogue Assign script, assurez-vous de ne pas utiliser de parenthèses. Vous devez uniquement entrer le nom de la fonction lui-même :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/3.png)
_capture d'écran de l'assignation de script à une image_

Et voilà ! Nous avons un sélecteur de style. Vous pouvez ajouter ou modifier ceux-ci pour créer n'importe quel nombre de combinaisons que vous pouvez facilement activer et désactiver dans votre propre Google Sheet !

![Image](https://www.freecodecamp.org/news/content/images/2023/09/4.png)
_capture d'écran du style Synth Mode_

## Conclusion

Cet article montre comment vous pouvez créer et coder des modes sombres et d'autres modes de fond pour vos Google Sheets en utilisant Apps Script et JavaScript.

J'espère que cela a été utile pour vous !

## Plus de ressources
d83dude04

25b6 Trouvez tous mes tutoriels vidéo et mes présentations sur YouTube : [https://www.youtube.com/@eamonncottrell?sub_confirmation=1](https://www.youtube.com/@eamonncottrell?sub_confirmation=1)

25b6 Connectez-vous avec moi sur LinkedIn où je partage des conseils quotidiens : [https://www.linkedin.com/in/eamonncottrell/](https://www.linkedin.com/in/eamonncottrell/)