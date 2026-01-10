---
title: Donnez des super-pouvoirs à votre journée de travail avec Google Apps Script
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-08T17:59:09.000Z'
originalURL: https://freecodecamp.org/news/automate-your-workday-with-google-app-script
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca228740569d1a4ca52e9.jpg
tags:
- name: automation
  slug: automation
- name: google apps script
  slug: google-apps-script
- name: JavaScript
  slug: javascript
- name: work life balance
  slug: work-life-balance
seo_title: Donnez des super-pouvoirs à votre journée de travail avec Google Apps Script
seo_desc: 'By Peter Gleeson

  The best learn-to-code projects are often those which solve a real world problem.

  These projects can provide that extra dose of motivation so essential to finishing
  any project. They encourage you to actively explore and discover new...'
---

Par Peter Gleeson

Les meilleurs projets pour apprendre à coder sont souvent ceux qui résolvent un problème réel.

Ces projets peuvent fournir cette dose supplémentaire de motivation si essentielle pour terminer un projet. Ils vous encouragent à explorer et à découvrir activement de nouveaux concepts, plutôt qu'à imiter des exemples que vous avez vus auparavant.

Il y a aussi quelque chose de particulièrement satisfaisant à résoudre un problème auquel vous êtes confronté au quotidien.

Un moyen facile de commencer est avec [Google Apps Script](https://developers.google.com/apps-script/).

Il s'agit d'un langage de script pour une gamme d'applications Google. Le langage lui-même est en fait JavaScript.

Ce que Google Apps Script fournit, ce sont des bibliothèques et des classes qui vous permettent de travailler avec des objets tels que des feuilles de calcul, des emails, des calendriers, des diapositives, et plus encore.

Si vous voulez plonger directement, la documentation est disponible [ici](https://developers.google.com/apps-script/reference/).

Voici trois exemples qui montreront comment commencer avec Google Apps Script. Espérons que cela vous donnera quelques idées pour vos propres projets !

### Lancer Google Apps Script

Vous aurez besoin d'un compte Google pour commencer à développer des projets Apps Script. Pour démarrer un nouveau projet, il suffit de naviguer vers [script.google.com/home](https://script.google.com/home) et de cliquer sur 'Nouveau Script'.

Vous serez redirigé vers un IDE dans le navigateur qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-18.40.56.png)

Donnez un nom à votre projet en changeant le titre dans le coin supérieur gauche.

Notez que chaque fois que vous avez besoin que Apps Script accède à différentes applications Google, vous devrez donner les permissions nécessaires.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-17.34.16.png)

Cela peut sembler un peu intimidant, mais si vous exécutez votre propre projet avec soin, il n'y aura aucun problème. Cliquez sur "Avancé" et autorisez votre projet à s'exécuter.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-17.34.42.png)

Regardons quelques exemples.

### Calculez votre impôt sur le revenu

Cet exemple simple vous montrera comment étendre [Google Sheets](https://www.google.com/sheets/about/) en ajoutant vos propres formules personnalisées. Dans cet exemple, la formule sera utilisée pour calculer l'impôt sur le revenu au Royaume-Uni.

Au Royaume-Uni, [différents taux d'imposition](https://www.gov.uk/income-tax-rates) sont appliqués à différentes catégories de revenus. Par conséquent, le montant de l'impôt sur le revenu dû varie en fonction du revenu.

Tout d'abord, créez une nouvelle [feuille Google](https://docs.google.com/spreadsheets/u/0/). Ensuite, dans le ruban de menu, sélectionnez Outils > Éditeur de script. Vous serez redirigé vers l'IDE Apps Script.

Le bloc de code ci-dessous utilise une [instruction switch](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-javascript/selecting-from-many-options-with-switch-statements/) pour calculer le bon montant d'impôt pour un argument numérique `income`. Si vous êtes familier avec JavaScript, vous reconnaîtrez la syntaxe.

```javascript
function TAX(income) {
  
  switch (true) {
      
    case income <= 12500:
      var tax = 0;
      break;
    case income <= 50000:
      var tax = 0.2 * (income - 12500);
      break;
    case income <= 150000:
      var tax = 7500 + (0.4 * (income - 50000));
      break;
    case income > 150000:
      var tax = 47500 + (0.45 * (income - 150000));
      break;
    default:
      var tax = "ERROR";
  }
  
  return tax;
  
}
```

Enregistrez votre projet si vous ne l'avez pas déjà fait.

Maintenant, de retour dans la feuille, entrez votre salaire choisi dans, par exemple, la cellule A1. Vous pouvez maintenant appeler la nouvelle formule avec `=TAX(A1)`.

Vous pourriez écrire une fonction similaire pour calculer les [cotisations d'assurance nationale du Royaume-Uni](https://www.which.co.uk/money/tax/national-insurance/national-insurance-rates-ajg9u9p48f2f#headline_3).

Quelles autres fonctions Sheets pourriez-vous écrire ?

### N'oubliez pas de vérifier vos emails

Il peut être difficile de trouver le temps de répondre aux emails importants. Cet exemple réunira [Gmail](https://www.google.com/gmail/) et [Google Calendar](https://calendar.google.com/calendar/r) en une seule courte application.

L'idée est simple. Vous fournissez une liste de contacts email importants et/ou de mots-clés. L'application vérifie votre boîte de réception toutes les six heures. Si elle trouve de nouveaux emails de ces contacts (avec l'un des mots-clés dans la ligne d'objet), elle crée un événement de calendrier vous rappelant de répondre plus tard dans la journée.

Vous pouvez créer un nouveau projet à partir de [script.google.com/home](https://script.google.com/home).

Consultez le code ci-dessous :

```javascript
function reminder() {
  /* créer une liste d'expéditeurs et de mots-clés de sujet */
  senders = ["freecodecamp", "codecademy", "meetup"];
  subjects = ["javascript", "python", "data science"];

  /* construire la requête de recherche */
  var searchString = "is:unread newer_than:1d from: { " +
    senders.join(" ") + "} subject: { " + 
    subjects.join(" ") + " }"

  /* récupérer les messages correspondants */
  threads = GmailApp.search(searchString);

  /* s'il y a des résultats, créer un événement de calendrier */
  if (threads.length > 0) {
    var event = CalendarApp.getDefaultCalendar();
    event.createEventFromDescription('Revoir les emails à 18h aujourd\'hui');
  }

}

```

Pour exécuter cette fonction à intervalles réguliers, vous pouvez configurer un déclencheur. Dans le ruban de menu, choisissez Édition > Déclencheurs du projet actuel.

Cela vous mènera à un nouvel onglet où vous pourrez ajouter un nouveau déclencheur pour le projet actuel. Cliquez sur 'Ajouter un nouveau déclencheur' et choisissez les paramètres que vous souhaitez utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-16.30.47.png)

Maintenant, votre script s'exécutera toutes les 6 heures et créera un événement de calendrier si vous avez des emails à réviser.

Une extension utile pourrait être de créer une feuille de calcul ou un formulaire Google qui vous permet d'ajouter facilement des contacts et des mots-clés.

Comment pourriez-vous intégrer votre boîte de réception et votre calendrier ?

### Mise à jour des diapositives

Garder les présentations et les diapositives à jour peut être une tâche fastidieuse. Heureusement, vous pouvez utiliser Google Apps Script pour automatiser le processus.

Pour cet exemple, nous utiliserons une application mobile fictive. Le but est de produire un diaporama avec des métriques à jour telles que les téléchargements d'applications, les utilisateurs actifs et les revenus.

L'astuce consistera à remplacer un certain nombre de `<tags>` dans le diaporama par des données contenues dans une feuille Google.

Dans Slides, créez une nouvelle présentation. Donnez-lui un nom tel que "Modèle de mise à jour de l'application".

Créez une nouvelle diapositive. Donnez-lui un titre tel que "Métriques clés".

Dans une zone de texte, ajoutez un contenu tel que ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-18.55.18.png)

Remarquez les tags inclus dans chaque ligne. Ceux-ci seront remplacés par des chiffres à jour chaque fois que le script sera exécuté.

Ensuite, créez une nouvelle feuille et ajoutez des données à utiliser dans le diaporama. Dans une colonne, faites référence aux tags dans le diaporama. Dans l'autre, ajoutez les dernières données.

Dans un exemple réel, cela serait calculé à partir de données brutes ailleurs dans la feuille de calcul. Les données brutes pourraient provenir de Google Analytics, ou être exportées d'un entrepôt de données, ou d'une autre source.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-18.53.00.png)

De retour dans Slides, sélectionnez Outils > Éditeur de script dans le ruban de menu. Cela ouvrira un nouveau projet Apps Script.

Maintenant, vous pouvez commencer à écrire du code. La fonction prend deux identifiants de fichiers comme arguments - un pour le modèle Slides, un pour la feuille. L'identifiant de fichier est la chaîne de lettres et de chiffres que vous pouvez trouver dans l'URL du fichier.

```javascript
function updateSlides(templateId, sheetId) {
  
  /* Faire une copie récente du modèle de diaporama */
  var template = DriveApp.getFileById(templateId);
  var today = Date();
  var copyName = "Mise à jour de l'application " + today;
  var templateCopy = template.makeCopy(copyName);
  
  /* Ouvrir la feuille de calcul et les diapositives par leur identifiant */
  var sheet = SpreadsheetApp.openById(sheetId);
  var slides = SlidesApp.openById(templateCopy.getId());
  
  /* Obtenir les données de la feuille */
  var data = sheet.getRange("A1:B5").getValues();
  
  /* remplacer toutes les tags dans le diaporama par leurs dernières valeurs */
  for(var i=0; i <data.length; i++){
    var tag = "<"+data[i][0]+">";
    var value = data[i][1].toString();
    
    slides.replaceAllText(tag, value);
    
  }
}


```

Si vous exécutez ce script, une nouvelle présentation sera créée avec les dernières données à la place de chacune des tags.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-18.56.23.png)

Vous pourriez planifier ce script pour qu'il s'exécute à intervalles réguliers, par exemple à la fin de chaque mois. Si vous vouliez développer davantage l'idée, vous pourriez utiliser Apps Script pour envoyer automatiquement le nouveau diaporama à une liste de contacts.

### À vous de jouer

Google Apps Script est un excellent moyen de commencer à écrire du vrai JavaScript de manière immédiatement pratique. Espérons que vous avez trouvé ces trois exemples utiles.

Peut-être que cette introduction vous a donné des idées pour des projets que vous pourriez développer ?

Rappelez-vous, le codage est un outil puissant - ne faites rien avec Apps Script que vous ne feriez pas manuellement. Mieux vaut ne pas effacer toute votre boîte de réception ou écraser un fichier important avec des memes.

Merci d'avoir lu !