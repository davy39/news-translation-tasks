---
title: Comment utiliser le code Google Apps Script pour effacer des plages de données
  dans Google Sheets
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-03-29T19:55:52.000Z'
originalURL: https://freecodecamp.org/news/use-apps-script-to-clear-data-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/fcc-1.jpg
tags:
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment utiliser le code Google Apps Script pour effacer des plages de
  données dans Google Sheets
seo_desc: 'Google Apps Script allows you to write code in your spreadsheet. It functions
  like Visual Basic for Applications (VBA) does in Excel. They''re both incredibly
  useful for executing more complicated actions or for automating repetitive tasks.

  In this ar...'
---

Google Apps Script vous permet d'écrire du code dans votre feuille de calcul. Il fonctionne de la même manière que Visual Basic for Applications (VBA) dans Excel. Les deux sont incroyablement utiles pour exécuter des actions plus complexes ou pour automatiser des tâches répétitives.

Dans cet article, je vais vous donner un bref aperçu de Google Apps Script en vous montrant comment faire quelque chose de très simple : effacer un ensemble de données dans votre feuille de calcul.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/homer-simple.gif)
_gif d'Homer Simpson disant, bien sûr, c'est si simple._

## Qu'est-ce qu'Apps Script ?

Bonne question. Bien que vous soyez peut-être familier avec la grille carrée qui constitue l'interface de la plupart des feuilles de calcul, vous ne savez peut-être pas qu'en coulisses, se trouve une puissante plateforme JavaScript basée sur le cloud.

Apps Script vous permet d'écrire des fonctions personnalisées, des automatisations, des modules complémentaires et plus encore. La capture d'écran ci-dessous provient de la [documentation Google Workspace](https://developers.google.com/apps-script#:~:text=Apps%20Script%20is%20a%20cloud,automate%20tasks%20across%20Google%20products.) :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-213.png)
_Documentation Google Workspace_

## Ouvrir Apps Script

[Voici le lien vers la feuille de démonstration](https://docs.google.com/spreadsheets/d/1wmiSt2KnwTOX7wQZZaLnHXYIN9NBk_B487JJ4EHbnlc/edit?usp=sharing) si vous souhaitez suivre et/ou en faire une copie.

Vous pouvez également en créer une avec moi en ouvrant une nouvelle feuille : [https://sheets.new](https://sheets.new).

Et voici une vidéo de présentation détaillant tout ce que nous allons faire :

%[https://youtu.be/PVoa7dp6pr0]

Pour notre exemple, nous avons simplement besoin de quelques données à effacer. Dans mon entreprise, nous utilisons cet Apps Script pour vider une fois par mois des modèles que nous utilisons chaque semaine pour l'inventaire.

Nous allons construire une version miniature de cela pour nous entraîner, mais les principes que nous abordons peuvent être utilisés à des échelles beaucoup plus vastes où Apps Script peut faire gagner énormément de temps et d'efforts.

Voici à quoi ressemblera notre feuille : quatre semaines d'inventaire et de montants de commandes.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-209.png)
_capture d'écran du formulaire de commande dans Google Sheets_

Nous voulons un moyen automatisé d'effacer les données dans les colonnes d'inventaire et de commande.

Oui, vous pourriez simplement sélectionner cette plage et appuyer sur supprimer ou retour arrière. Mais si votre feuille de calcul est plus grande et plus nuancée, il peut y avoir des dizaines ou des centaines de plages à sélectionner.

C'est là qu'Apps Script devient super pratique.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/assist.gif)
_gif de Bill Murray_

Pour ouvrir Apps Script, allez dans `Extensions -> Apps Script`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/open.png)
_Capture d'écran de la barre d'outils Extensions_

🤔 Maintenant, qu'y a-t-il de mieux que de travailler dans une feuille de calcul élégante ?

Pouvoir écrire du code personnalisé pour celle-ci !

À partir de là, nous sommes accueillis par notre vieil ami, l'éditeur de code.

Nous donnerons à ce projet le nom de `Clear Range` en haut, puis en nous assurant que l'éditeur de code est sélectionné dans la barre latérale gauche, nous commencerons à écrire notre première fonction, également nommée `clearRange` :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/editor.png)

Nous pouvons enregistrer notre progression au fur et à mesure de l'écriture en appuyant sur `CTRL + S` ou en cliquant sur l'icône de disquette dans la barre d'outils.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/save.png)
_capture d'écran de l'éditeur de code Apps Script_

Ce ne serait pas de la programmation sans une console pour déboguer, et bien sûr, il existe une méthode `Logger.log()` intégrée à Apps Script. Écrivons notre premier script Apps Script 😀 pour journaliser le message, `Bonjour la console ! :)` :

```javascript
function clearRange() {
  Logger.log('Bonjour la console ! :)')
}
```

Et voici ce que vous devriez voir lorsque vous appuyez sur le bouton Exécuter dans la barre d'outils :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/console.log.png)
_Capture d'écran de Logger.log() dans Apps Script_

Ok, donc les choses fonctionnent effectivement. Passons aux choses sérieuses avec notre script réel...

## Comment ajouter un menu personnalisé

Nous pouvons exécuter notre code dans l'éditeur de code en cliquant sur `Exécuter`, mais nous ne voulons pas l'ouvrir à chaque fois que nous utilisons le code. Alors, ajoutons un menu personnalisé à la barre d'outils à l'intérieur de notre feuille de calcul.

Nous avons deux options ici : créer un menu personnalisé ou créer un menu d'extension (add-on). Le menu personnalisé fonctionnera comme un menu déroulant directement sur la barre d'outils à droite du menu `Aide`. Le menu d'extension s'affichera dans le menu déroulant habituel `Extensions`.

Ajoutons le menu personnalisé. Il peut être utile de copier des méthodes de la [documentation Apps Script](https://developers.google.com/apps-script/reference/base/ui#createMenu(String)) et de les adapter à nos besoins. C'est ce que j'ai fait ci-dessous à partir de la méthode createMenu() ici :

```javascript
function onOpen(e) {
  SpreadsheetApp.getUi()
      .createMenu('Effacer les entrées')
      .addItem('Tout effacer !', 'clearRange')
      .addSeparator()
      .addToUi();
}
```

Cela crée un menu nommé "Effacer les entrées" lorsque la feuille de calcul est ouverte. Dans le menu, il y a un élément cliquable nommé "Tout effacer !" qui appelle la fonction `clearRange`.

## Comment ajouter la fonction

Maintenant, nous avons besoin que la fonction fasse plus que journaliser un message dans la console.

Nous pouvons effacer le contenu d'une plage ou de plusieurs plages de différentes manières. Nous allons le faire ici en nommant les plages que nous voulons effacer. Cela nous évitera d'avoir à coder en dur des références de cellules au cas où celles-ci changeraient plus tard si nous modifions la feuille de calcul.

J'ai nommé les colonnes d'inventaire et de commande de chaque semaine comme des plages nommées :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-255.png)
_capture d'écran des plages nommées_

Ensuite, dans notre fonction, nous créons une variable pour contenir un tableau de toutes les plages nommées, nous itérons sur chacune d'elles dans une boucle `forEach()`, et nous effaçons le contenu de chaque plage en utilisant la méthode `clearContent()`.

Très simple, et cela ne prend que quelques lignes de code :

```javascript
function clearRange(){
  var ss = SpreadsheetApp.getActive();
  var ranges = ss.getNamedRanges();
  // Parcourir chaque plage et effacer son contenu
  ranges.forEach(range => range.getRange().clearContent());
}
```

Dans la [feuille Google Sheet de démonstration](https://docs.google.com/spreadsheets/d/1wmiSt2KnwTOX7wQZZaLnHXYIN9NBk_B487JJ4EHbnlc/edit?usp=sharing), j'ai inclus l'autre façon d'écrire ceci avec la notation A1 si vous aviez besoin de ne pas utiliser les plages nommées.

## Comment exécuter la fonction

Lorsque vous exécutez pour la première fois une fonction qui nécessite l'accès à vos données, vous serez accueilli par cet écran d'autorisation.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-251.png)
_capture d'écran d'autorisation_

Choisissez votre compte Google, cliquez sur Paramètres avancés lorsque vous voyez l'écran "Google n'a pas validé cette application" :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/verify.png)
_écran de vérification Google_

Il décrira à quoi la fonction qui tente de s'exécuter va avoir la permission d'accéder. Cliquez sur Autoriser :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/sign.png)
_capture d'écran autorisant la permission d'utiliser notre nouvelle fonction_

Une fois que vous avez accordé les permissions, vous devrez exécuter à nouveau la fonction pour qu'elle s'exécute réellement cette fois-ci. Vous verrez cette boîte de dialogue de script en cours d'exécution apparaître en haut :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-256.png)
_capture d'écran de la boîte de dialogue de script en cours d'exécution_

Et voilà !

Nous avons effacé notre plage :)

![Image](https://www.freecodecamp.org/news/content/images/2023/03/clear-script_1.gif)
_gif de l'effacement de la plage de la feuille de calcul_

## Résumé

J'espère que ce guide vous a été utile et que vous avez appris quelque chose de nouveau. J'utilise régulièrement une version de ce script même dans le monde réel. C'est un exemple d'une toute petite chose qui permet de gagner énormément de temps et d'éviter des erreurs.

Venez me dire bonjour et abonnez-vous à ma [chaîne YouTube par ici](https://www.youtube.com/@eamonncottrell). Je crée des tutoriels et du contenu technique chaque semaine.

Passez une excellente journée ! 👋