---
title: Creative Coding — Comment créer un moteur VJ en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-21T09:37:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-vj-engine-in-javascript-b63b7fb1c87b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2SwNYMIzezIXuauBXdNbHg.png
tags:
- name: Art
  slug: art
- name: creative coding
  slug: creative-coding
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: technology
  slug: technology
seo_title: Creative Coding — Comment créer un moteur VJ en JavaScript
seo_desc: 'By George Gally

  Learn how to dynamically inject JavaScript into webpages

  For years I’ve been using the browser for my performances and installations using
  my own simple homegrown VJ engine. And now, after you learn a few simple tricks,
  you can too…

  A...'
---

Par George Gally

#### Apprenez à injecter dynamiquement du JavaScript dans des pages web

Depuis des années, j'utilise le navigateur pour mes performances et installations en utilisant mon propre moteur VJ simple fait maison. Et maintenant, après avoir appris quelques astuces simples, vous pouvez aussi le faire...

### Une rapide introduction

Tout d'abord, qu'est-ce qu'un moteur VJ ? vous pourriez demander. Et peut-être même : qu'est-ce qu'un VJ ? Voici une [définition de base](https://en.wikipedia.org/wiki/VJing) des caractéristiques du VJing :

> La création ou la manipulation d'images en temps réel par médiation technologique et pour un public, en synchronisation avec la musique.

Et un moteur VJ est simplement le logiciel utilisé pour le VJing.

Mais pourquoi construire le mien alors qu'il existe tant de moteurs VJ ?

Je n'ai jamais vraiment aimé les logiciels de VJ — ils m'ont toujours semblé surchargés et faisaient que tout le monde avait des trucs qui se ressemblaient. C'est un peu comme quand vous avez mis la main sur Photoshop pour la première fois, et que vous avez simplement mélangé un tas de trucs ensemble, ajouté quelques filtres, et c'était cool (parce que c'était les années 90). Mais surtout, je voulais une intégration plus étroite et meilleure entre le développement de contenu et les fréquences d'entrée sonore.

Je fais rarement du VJ ces jours-ci, mais cela anime toujours la plupart de mes installations et performances — partout où j'ai besoin de plusieurs visualisations, j'utilise _RBVJ_ (le _RB_ est pour _Radarboy_ — c'est moi) comme wrapper/lecteur.

_RBVJ_ a subi un certain nombre d'itérations au fil des ans, alors que je suis passé de Flash, à Processing, et enfin maintenant à JavaScript, tout en utilisant le même système simple.

J'avais précédemment ouvert le code source et mon contenu (avant l'ère de Git et sans vraiment savoir qu'il existait une chose appelée open-source). Il a remporté un tas de prix, et j'ai vu mon contenu être utilisé dans un tas d'endroits [ce qui était sympa](https://www.youtube.com/watch?v=XOhZgAPn_CU&ab_channel=CalumRodger). J'ai donc pensé qu'il était temps de le rendre à nouveau disponible pour les autres, avec un tas de contenu pour montrer comment je procède au creative coding.

![Image](https://cdn-media-1.freecodecamp.org/images/zXTWFCVzeLIVWd0XKR5aH03BI647fO5gKJwb)
_de [radarboy3000 sur Instagram](https://www.instagram.com/radarboy3000/" rel="noopener" target="_blank" title=")_

Ok, c'est une introduction assez longue. Montrez-moi le code, dites-vous !

### 1. Structurer le contenu

Essentiellement, un moteur VJ est juste un navigateur et un lecteur de contenu sophistiqués. Ce dont nous avons vraiment besoin, c'est d'un moyen de récupérer et de lire notre contenu.

Vous pourriez simplement déposer tout votre contenu dans un dossier, mais ce système est ce qui a le mieux fonctionné pour moi, permettant une structure simple pour le contrôle clavier :

* **Maj 0-9 pour changer les sets**
* **Touches 0-9 pour changer les banques**
* **Touches a-z pour choisir le contenu** dans la banque.

Cela vous donne 2 700 fichiers à utiliser. Si vous voulez vraiment (vraiment ?!) plus, vous pourriez aussi doubler cela en accédant à 26 fichiers supplémentaires par banque avec Maj A-Z).

Comme la plupart des projets HTML, j'ai une structure de haut niveau simple, et je garde le contenu VJ dans une structure numérotée à l'intérieur du dossier **art**, comme ceci :

```
index.html/css/js/art <- le contenu va ici
```

Mon dossier de contenu (/art) contient 10 dossiers numérotés, que j'appelle des **sets**. À l'intérieur de chaque set se trouvent 10 autres dossiers numérotés représentant des **banques**. Et à l'intérieur de chaque banque se trouvent 27 fichiers de contenu individuels numérotés, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/9SfMeEsL-OHXdShxWbJ3ZlihlxiYXlNw0Oqx)
_À l'intérieur de /art se trouvent 10 sets de dossiers. Chaque set contient 10 banques, à l'intérieur de chaque banque se trouvent 27 fichiers javascript. Les banques et les sets sont accessibles par les touches numériques et le contenu par les touches a-z_

### 2. Récupérer et lire le contenu

Maintenant, nous avons juste besoin d'un moyen d'accéder à nos fichiers, ce qui est fait en injectant du contenu dans notre page d'index.

Et c'est assez simple à faire.

La magie opère dans une fonction appelée **loadJS()**. Elle crée une balise de script dans l'en-tête de la page et y injecte du JavaScript (qui serait notre contenu). Nous déclenchons cette fonction via une pression de touche (mais cela pourrait aussi être un signal midi ou OSC) et passons le nom de fichier du contenu que nous voulons. Ensuite, le script est disponible sur la page.

```
// INJECTER JS DANS LA PAGE
```

```
var my_script;
```

```
function loadJS(filename) {
```

```
 // supprimer le JavaScript injecté s'il y en a eu chargé auparavant if (my_script != undefined)   document.getElementsByTagName("head")[0].removeChild(my_script); 
```

```
 // créer un élément de script my_script = document.createElement('script'); my_script.setAttribute("type", "text/javascript");
```

```
 // Charger le fichier et l'insérer dans la balise head de la page my_script.setAttribute("src", filename); document.getElementsByTagName("head")[0].appendChild(my_script);
```

```
}
```

Nous écoutons les pressions de touches avec un écouteur d'événements, qui appelle une fonction appelée **onKeyDown()**, comme ceci :

```
window.addEventListener( 'keydown', function( event ) {   onKeyDown( event ); });
```

L'écouteur passe l'objet événement à la fonction, qui contient un tas de choses utiles. Voici ce qui nous intéresse : le **event.keycode**. Appuyer sur la touche 'a' nous donne un **keycode** de 65, et appuyer sur 'z' nous donne un **keycode** de 90. Nous soustrayons donc simplement 65 du **keycode** pour obtenir le numéro de fichier requis et passons cette valeur à une fonction **changeFile()**, que je montrerai un peu plus tard.

De même, nous voulons que les touches 0-9 (keycodes 48 à 57, donc soustraire 48) changent les banques. Nous voulons aussi tester si la touche Maj a été pressée pour charger les sets. L'objet événement a une variable pratique **event.shiftKey** pour cela, donc notre fonction **onKeyDown** ressemblera à ceci :

```
// Gestion des pressions de touches
```

```
function onKeyDown( event ) {
```

```
    var keyCode = event.keyCode;
```

```
   // CHANGER LE FICHIER // touches a-z   if ( keyCode >= 65 && keyCode <= 90 ) {      changeFile(keyCode - 65);
```

```
   // CHANGER LE SET ET LA BANQUE // touches 0-9   } else if ( keyCode >= 48 && keyCode <= 57 ) {
```

```
      // Tester si la touche Maj est également pressée      if( event.shiftKey ) {       changeBank( keyCode-48 );      } else {       changeSet( keyCode-48 );      }
```

```
   }
```

```
}
```

La fonction **changeFile()** prend essentiellement la pression de touche et la convertit en une URL. Elle appelle notre fonction **loadJS()** pour injecter le contenu dans la page, et boom, nous y sommes...

![Image](https://cdn-media-1.freecodecamp.org/images/IzvgpLah3pAqNZ0KLPWx0rHgsqBWGLf916TP)
_de [radarboy3000 sur Instagram](https://www.instagram.com/radarboy3000/" rel="noopener" target="_blank" title=")_

Donc, notre fonction **changeFile()** ressemblerait à ceci :

```
var current_file = 0;var current_set = 0;var current_bank = 0;
```

```
var art_location = "art/";
```

```
// FONCTIONS DE CHARGEMENT DE FICHIERS
```

```
function changeFile(file) {
```

```
  current_file = file;  var loc = current_set + '/' + current_bank + '/' + current_file;  var filename = contentLocation + loc + '.js';  loadJS(filename);  document.location.hash = loc; //console.log("File: " + loc);
```

```
}
```

J'ai aussi une variable **art_location** au cas où je voudrais avoir différentes collections de visuels (pour pouvoir avoir différents dossiers pour différents spectacles et installations). J'ajoute aussi le nom de fichier comme un hash (https://127.0.0.1/#set/bank/file) à l'URL du navigateur pour faciliter la visualisation de l'endroit où je me trouve.

Nos fonctions **changeBank()** et **changeSet()** définissent les variables **current_bank** et **current_set**. Ensuite, elles appellent simplement la fonction **changeFile()** pour afficher le fichier correct.

Pour la gestion, je réinitialise aussi tous les compteurs — en remettant **current_file** à 0 lorsque je change de banque, et **current_bank** à 0 lorsque je change de set. Ainsi, je sais que lorsque je change de **banque**, le fichier joué sera le premier fichier de la banque. De même, lorsque je change de **set**, le fichier joué sera réinitialisé pour être le premier fichier de la première banque du set actuel (**current_set/0/0.js**).

Un peu long à expliquer, mais les fonctions sont en réalité super simples :

```
function changeSet(set) {
```

```
  current_set = set;  console.log("changeSet: " + current_set);
```

```
  // réinitialiser le numéro de banque  changeBank(0);
```

```
}
```

```
function changeBank(bank) {
```

```
current_bank = bank;  console.log("changeBank: " + current_bank);
```

```
  // réinitialiser le numéro de fichier et charger le nouveau fichier  changeFile(0);
```

```
}
```

Et ainsi, le code complet pour votre moteur VJ de base ressemble à ceci :

```
// FONCTIONS DE CHARGEMENT DE FICHIERS
```

```
var art_location = "/art";
```

```
var fileref;var current_file = 0;var current_set = 0;var current_bank = 0;
```

```
function changeFile( file ) {  reset()  current_file = file;  var loc = current_set + '/' + current_bank + '/' + current_file;  var filename = 'art/' + loc + '.js';  loadJS( filename );  document.location.hash = loc;  //console.log("File: " + loc);}
```

```
function changeSet( set ) {  current_set = set;  current_bank = 0;  console.log( "changeSet: " + current_bank );  // réinitialiser  changeFile( 0 );}
```

```
function changeBank( bank ) {  current_bank = bank;  console.log( "changeBank: " + current_bank );  changeFile( 0 );}
```

```
function reset(){  ctx.clearRect( 0, 0, w, h );  ctx2.clearRect( 0, 0, w, h );  ctx3.clearRect( 0, 0, w, h );  ctx.lineCap = "butt";}
```

```
// INJECTER JS DANS LA PAGE
```

```
function loadJS( filename ) {
```

```
if ( fileref != undefined ) document.getElementsByTagName( "head" )[ 0 ].removeChild( fileref );  fileref = document.createElement( 'script' );  fileref.setAttribute( "type", "text/javascript" );  fileref.setAttribute( "src", filename );  document.getElementsByTagName( "head" )[ 0 ].appendChild( fileref );
```

```
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/XnCcboR0KFixjweg9JBvoGifwsfXUZqyMcyT)
_de [radarboy3000 sur Instagram](https://www.instagram.com/radarboy3000/" rel="noopener" target="_blank" title=")_

Il ne reste plus qu'à vous montrer comment je structure les fichiers de contenu réels, qui utilisent une fonction encapsulée comme ceci :

```
// Art RBVJ
```

```
rbvj = function() {
```

```
  draw = function() {     // faire du creative coding ici  }
```

```
}();
```

La fonction **rbvj()** est ce qui est injecté dans la page. Elle est réutilisée, de sorte que chaque fois qu'un nouveau fichier est inséré dans ma page, la mémoire est vidée de tout le contenu précédent.

En encapsulant le code (voir le '()' après la fonction), tout code à l'intérieur de la fonction **rbvj()** s'exécutera automatiquement lorsque le fichier est injecté dans la page.

Vous remarquerez que dans le contenu, j'ai une fonction **draw()** (celle-ci provient de mon propre script utilitaire **creative_coding.js**). C'est juste une simple boucle qui utilise **requestAnimationFrame()** de JavaScript et est capable de faire varier le taux de rafraîchissement.

```
var frame_number = 0;var frame_rate = 60;var last_update = Date.now();
```

```
function loop() {
```

```
var now = Date.now();  var elapsed_mils = now - last_update;
```

```
if ((typeof window.draw == 'function') && (elapsed_mils >= (1000 / window.frame_rate))) {    window.draw();    frame_number++;    last_update = now - elapsed_mils % (1000 / window.frame_rate);  }  requestAnimationFrame(loop);
```

```
};
```

Et c'est à peu près tout. Vous avez maintenant un moteur VJ fonctionnel dans le navigateur.

### 3. Quelques autres choses à savoir qui pourraient être utiles

Normalement, je branche simplement l'entrée audio de mon ordinateur directement sur une entrée du mixer ou de l'ampli de la salle (j'utilise une version de mon fichier d'entrée microphone standard **mic.js**, que vous pouvez lire plus en détail [ici](https://hackernoon.com/creative-coding-using-the-microphone-to-make-sound-reactive-art-part1-164fd3d972f3)). Et j'ai des touches configurées (dans mon cas, les touches **plus** et **moins**) pour ajuster les niveaux d'entrée vers le haut ou vers le bas, afin de ne pas avoir à accéder constamment au mixer.

Notez également que pour l'entrée audio, vous aurez besoin d'une connexion sécurisée HTTPS — ou si vous utilisez quelque chose comme le Live Server d'Atom, cela est intégré.

J'ai aussi un tas d'autres touches configurées pour des filtres audio et visuels simples (voir comment créer un filtre de pixelisation [ici](https://hackernoon.com/creating-a-pixelation-filter-for-creative-coding-fc6dc1d728b2)).

Je n'utilise généralement pas d'écran/interface de prévisualisation, mais il est assez facile d'en construire un. Il suffit de créer une nouvelle page HTML et de laisser les pages communiquer entre elles via une socket.

Et enfin, un dernier conseil : lors du développement de contenu, créez simplement une fonction pour lire la valeur de hachage actuelle du navigateur, et appelez la fonction **loadFile()** au chargement de la page. Ainsi, lorsque vous travaillez sur un fichier et que vous rechargez la page, ce fichier est automatiquement affiché.

Et c'est à peu près tout. J'espère que cela vous aidera à vous lancer et à montrer plus de votre contenu. Comme je l'ai mentionné précédemment, j'ai inclus un tas de contenu pour que vous puissiez jouer et tester afin de vous faire une idée de la façon dont je crée mes trucs. Si vous utilisez ou modifiez l'un d'eux, j'adorerais voir comment, où et ce que vous en avez fait. Alors, s'il vous plaît, envoyez-moi un message.

**Bon codage. Et merci d'avoir lu !**

Comme d'habitude, le code complet est disponible [sur Github](https://github.com/GeorgeGally/rbvj).

_Cet article fait partie d'une série continue de tutoriels sur l'apprentissage du creative coding en JavaScript pur. Et oui, je devrais le faire en ES6, mais je voulais garder cela aussi simple que possible à comprendre._

Vous pouvez voir tous mes précédents tutoriels de creative coding [ici](https://medium.com/@radarboy3000).

**Et suivez-moi ici pour les mises à jour, les techniques et les bonbons pour les yeux :**

[**@radarboy3000 * Photos et vidéos Instagram**](https://www.instagram.com/radarboy3000/)  
[_3,960 abonnés, 843 abonnements, 1,082 publications - Voir les photos et vidéos Instagram de @radarboy3000_www.instagram.com](https://www.instagram.com/radarboy3000/)[**George Gally (@radarboy_japan) | Twitter**](https://twitter.com/radarboy_japan)  
[_Les derniers tweets de George Gally (@radarboy_japan). Artiste média, technologue, bricoleur, rêveur. Réaction au mouvement..._twitter.com](https://twitter.com/radarboy_japan)[**Radarboy**](https://www.facebook.com/radarboy3000)  
[_Radarboy. 130 mentions J'aime · 7 en parlent. Art, design, visualisation, hacks_www.facebook.com](https://www.facebook.com/radarboy3000)