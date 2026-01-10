---
title: Pirater G Suite en utilisant Apps Scripts — en moins d'une heure.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-21T05:42:15.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-hack-using-apps-scripts-in-under-an-hour-8442a1495dce
coverImage: https://cdn-media-1.freecodecamp.org/images/0*nVQ-TOygSLHF9ucy
tags:
- name: Google
  slug: google
- name: google apps script
  slug: google-apps-script
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Pirater G Suite en utilisant Apps Scripts — en moins d'une heure.
seo_desc: 'By Supriya Shashivasan

  Have you heard of Google Apps Script? I was introduced to it for the first time
  at a Google Developer Group meetup held in Bangalore.

  Apps Script helps you use Google’s G Suite products, by running a script similar
  to JavaScrip...'
---

Par Supriya Shashivasan

Avez-vous entendu parler de [Google Apps Script](https://developers.google.com/apps-script/) ? Je l'ai découvert pour la première fois lors d'une rencontre du [Google Developer Group](https://www.meetup.com/GDGBangalore/) organisée à Bangalore.

Apps Script vous aide à utiliser les produits G Suite de Google en exécutant un script similaire à JavaScript. Avec seulement quelques lignes de code, les utilisateurs peuvent accomplir des tâches en un clic, ce qui prendrait autrement beaucoup plus de temps.

Google Apps Scripts est très facile à apprendre et vous aide à construire des systèmes complexes en utilisant G Suite. Les utilisateurs peuvent publier des applications web et créer des fonctions personnalisées pour Google Slides, Sheets et Forms.

Dans cet article, je vais vous guider à travers la création d'une petite application qui utilise Google Sheets, Google Slides et Google Translate.

J'ai construit cette application pour les voyageurs. Lorsque nous visitons des pays étrangers, la communication devient un problème en raison des barrières linguistiques. Les gens prennent souvent des cartes éclair avec eux pour aider à communiquer avec les locaux.

![Image](https://cdn-media-1.freecodecamp.org/images/NNMmCE6qcHtQ1kn3fi6AGLQI-UK81XER9XUe)
_Photo par [Unsplash](https://unsplash.com/@sonereker?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Soner Eker</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Nous allons construire exactement cela. Les questions et phrases sont mises dans Google Sheets. Ensuite, un script traduit les lignes et les écrit sur Google Slides. Voici ! Les cartes éclair traduites sont prêtes à l'emploi.

Maintenant, _PRÊT.PARTI.CODEZ_

![Image](https://cdn-media-1.freecodecamp.org/images/wnoNxBiBIyjAcxeQAoR85BqnqU3TAdZH4egu)

### Stocker les données

Les données ici sont des phrases/mots que vous voulez traduire. Elles sont stockées dans les lignes de la feuille Google.

Donc, la structure de la feuille de calcul sera :

* Chaque ligne sera remplie avec des phrases que vous voulez traduire.
* La deuxième colonne contiendra la valeur pour nous indiquer la langue dans laquelle les phrases doivent être traduites. La valeur ici est le [code de langue de Google Translate](https://ctrlq.org/code/19899-google-translate-languages). Si je veux que les phrases soient traduites en espagnol, le code sera "es".

![Image](https://cdn-media-1.freecodecamp.org/images/-CaL-t-tLtaweljpuILtIsX4xcV04CkZijiO)
_Feuille Google remplie_

### Accéder à l'éditeur de script

Le script pour accomplir la tâche souhaitée est écrit dans l'éditeur de script. Pour y accéder, allez dans **Outils > Éditeur de script**. Une autre façon d'accéder à l'éditeur de script est de visiter le [tableau de bord des scripts d'application](https://script.google.com/home) et de créer un nouveau script Apps. Tous les scripts que les utilisateurs écrivent peuvent être gérés par ce tableau de bord.

L'éditeur de script contient un fichier vide appelé **Code.gs**. Nous allons écrire le code ici en un seul script.

### Fonction principale

Nous écrivons une fonction principale `sheetToSlide()` dans laquelle la feuille et la diapositive actives sont initialisées. Une autre fonction `translate()` est appelée dans la fonction principale. C'est ici que la logique réelle prend place.

```
function sheetToSlide() {  var sheet =   SpreadsheetApp.getActiveSheet();  var slide = SlidesApp.create('TranslateApp');  var data = sheet.getDataRange().getValues();  var lan= data[0][1];  Logger.log(lan);  for (var i=0; i<data.length; i++){     translate(i,data[i][0],lan,slide);  }}
```

Dans la variable `data`, le contenu de la feuille de calcul est stocké sous forme de tableau multidimensionnel. Ces valeurs peuvent être accessibles par `data[Row][Column]`.

Elles sont transmises à la fonction `translate` pour un traitement ultérieur, ainsi qu'à la variable `slide` et à la `language` dans laquelle la traduction est requise.

`Logger` est une classe utilisée pour écrire du texte dans la console de journalisation. Cela aide beaucoup dans le processus de développement d'un code. La sortie du code peut être imprimée dans les journaux de débogage. Pour voir les journaux, allez dans **Affichage > J**ournaux dans la fenêtre de l'éditeur de script.

### Fonction de traduction

Dans cette fonction, de nouvelles diapositives sont ajoutées à la présentation qui contiennent à la fois les phrases originales et traduites. Chaque phrase est insérée dans une nouvelle diapositive dans une zone de texte.

```
function translate(num,data,language,slide){  var translate_lang = LanguageApp.translate(data, 'en', language);  var card= slide.insertSlide(num);  var shapeEnglish = card.insertShape(SlidesApp.ShapeType.TEXT_BOX, 150,100,300,60);  var textEnglish = shapeEnglish.getText();    textEnglish.setText(data);  textEnglish.getTextStyle().setBold(true);  card.insertLine(SlidesApp.LineCategory.STRAIGHT, 200,175,300,175)      var shapeTranslated = card.insertShape(SlidesApp.ShapeType.TEXT_BOX, 150,200,300,60);  var textTranslated = shapeTranslated.getText();  textTranslated.setText(translate_lang);  textTranslated.getTextStyle().setBold(true);  }
```

La phrase obtenue est d'abord traduite en utilisant Google Translate qui fait partie de G Suite.

Une nouvelle diapositive est insérée pour contenir les phrases. Dans la diapositive, une zone de texte est placée à une position particulière. Vous pouvez la modifier en consultant la documentation [ici](https://developers.google.com/apps-script/reference/slides/).

Le texte qui doit être affiché dans la zone de texte est fait en utilisant les méthodes `getText()` et `setText()`. Ce sont toutes des propriétés de Google Slides que vous pouvez manipuler et personnaliser selon vos souhaits.

Le design ici est fait très simple. Une ligne horizontale est placée au milieu en utilisant la méthode `insertLine()` pour séparer le texte original et traduit. Les propriétés et variables de toutes ces méthodes utilisées sont données en détail dans la documentation fournie par Google.

![Image](https://cdn-media-1.freecodecamp.org/images/bw5GvkzBf8xM-B66nc1XsQBoSYKyoT5AcSMM)

Pour exécuter le script, cliquez sur le bouton d'exécution à côté de l'icône de temps. Le script ouvrira une fenêtre qui demandera la permission d'accéder aux feuilles et diapositives, autorisez-la simplement. Ensuite, allez dans votre drive et une nouvelle présentation sera prête avec des phrases traduites dans les cartes.

C'est à quel point Apps Script est utile et facile. Vous pouvez également remplir une base de données Firebase Realtime en utilisant simplement Google Sheets. En écrivant simplement des scripts simples en quelques lignes, vous pouvez automatiser beaucoup de choses et également construire des applications web qui peuvent être hébergées.

App Scripts est vraiment puissant et vise à permettre aux utilisateurs de rendre leurs services automatisés. La prochaine fois que vous voulez envoyer un email à un groupe de personnes, essayez d'utiliser App Scripts. Une fois que vous en aurez le coup, vous pourrez construire des choses merveilleuses, comme des feuilles vers un site web, votre propre blog, des feuilles vers des diapositives et bien plus encore.

J'espère que cela vous a aidé. Santé !!

N'hésitez pas à me contacter !

**Twitter** : [https://twitter.com/@s_omeal](https://twitter.com/@s_omeal)

**Paybackhub** : paybackhub.com et **Certhive** : certhive.com