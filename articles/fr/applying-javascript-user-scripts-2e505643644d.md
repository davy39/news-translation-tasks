---
title: 'Application de JavaScript : Scripts Utilisateur'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-01T17:04:17.000Z'
originalURL: https://freecodecamp.org/news/applying-javascript-user-scripts-2e505643644d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ec0HoiWFiji_XNA4OXk29w.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Application de JavaScript : Scripts Utilisateur'
seo_desc: 'By Thomas Noe

  Writing a Userscript is a fun way to use your JavaScript skills. It takes you out
  of the editor into the browser with real time feedback and validation.

  What is a user script?


  Userscripts (a.k.a User Scripts, User scripts, or .user.js)...'
---

Par Thomas Noe

Écrire un Userscript est une manière amusante d'utiliser vos compétences en JavaScript. Cela vous sort de l'éditeur pour vous plonger dans le navigateur avec des retours et une validation en temps réel.

#### Qu'est-ce qu'un script utilisateur ?

> Les Userscripts _(également appelés User Scripts, User scripts, ou .user.js)_ sont des extensions open-source pour les navigateurs web qui modifient les pages web au moment de leur chargement. Ils donnent aux utilisateurs le pouvoir de faire faire aux sites web ce qu'ils veulent, plutôt que ce qui était initialement prévu.

Les scripts utilisateur sont écrits en JavaScript et vous permettent de modifier l'apparence d'une page web dans votre navigateur. Les scripts n'affectent que votre navigateur, pas la page web elle-même.

#### Un petit avertissement

> Vous devez être conscient des problèmes de confidentialité lors de l'utilisation de userscripts et ne pas les installer à partir de sources non fiables. Les userscripts peuvent effectuer des actions en votre nom et peuvent potentiellement accéder à toute information sur un site web auquel vous avez accès, ou que vous entrez dans un site web. Ils sont souvent autorisés à effectuer des fonctions que les scripts sur les sites web normaux ne peuvent pas, comme stocker des informations sur votre ordinateur et les partager entre les sites web. Des userscripts mal écrits pourraient également être exploités par des sites web malveillants.

_explications tirées de_ [https://github.com/OpenUserJs/OpenUserJS.org/wiki/Userscript-Beginners-HOWTO](https://github.com/OpenUserJs/OpenUserJS.org/wiki/Userscript-Beginners-HOWTO)

#### Pourquoi les scripts utilisateur ?

Free Code Camp propose de nombreux projets concrets qui enrichiront votre ensemble de compétences et votre portfolio. Personnellement, j'aime utiliser les compétences que j'ai apprises en JavaScript, jQuery et CSS pour modifier ma navigation quotidienne.

Certains scripts utilisateur ont été extrêmement populaires et ont été transformés en extensions de navigateur. Un exemple en est le Reddit Enhancement Suite disponible à l'adresse [http://redditenhancementsuite.com/](http://redditenhancementsuite.com/).

Vous aussi, vous pourriez utiliser votre script utilisateur comme base pour une extension de navigateur !

### Pour commencer

Les scripts utilisateur sont exécutés à partir d'extensions de navigateur. Grease Monkey (FireFox) a été l'extension pionnière permettant aux utilisateurs de personnaliser leur expérience de navigation. Installez le plugin approprié pour votre navigateur.

Pour FireFox : **_Grease Monkey_**

[**Greasemonkey**](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/)  
[_Le canal de développement vous permet de tester une nouvelle version expérimentale de cette extension avant sa sortie pour le grand public..._addons.mozilla.org](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/)

Pour Chrome : **_Tamper Monkey_**

[**Tampermonkey**](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en)  
[_Le gestionnaire de userscripts le plus populaire pour les navigateurs basés sur Blink_chrome.google.com](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en)

Pour ce tutoriel, j'utiliserai Chrome avec Tamper Monkey.

Il ne devrait pas y avoir de différences significatives dans le processus après l'installation de Grease Monkey ou Tamper Monkey.

Au cas où, voici un lien rapide pour installer Grease Monkey (ainsi que pour faire quelques choses avec).

[**Tutoriel Greasemonkey pour débutants**](http://hayageek.com/greasemonkey-tutorial/#install-greasemonkey)  
[_Dans ce tutoriel Greasemonkey, j'ai couvert comment écrire des scripts utilisateur Greasemonkey. Après ce tutoriel, vous serez capable de..._hayageek.com](http://hayageek.com/greasemonkey-tutorial/#install-greasemonkey)

### Le projet

Nous allons apporter une légère modification à la page d'accueil de Hacker News [http://news.ycombinator.com](http://news.ycombinator.com).

![Image](https://cdn-media-1.freecodecamp.org/images/6ICv092GpRSQFSCbogHBMCj3IBqWVqV0d7il)
_Page d'accueil de HackerNews_

Nous allons utiliser jQuery pour rendre les couleurs de fond des liens alternés légèrement différentes afin d'améliorer la lisibilité.

#### Démarrer un nouveau script

Cliquez sur l'icône Tamper Monkey en haut à droite et sélectionnez « Ajouter un nouveau script » dans la boîte de dialogue.

Vous devriez être redirigé vers un nouvel onglet qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/MnG62eij5rouor9HWsShflip5d1uJAH7bGGf)
_page de nouveau script_

#### Remplir les informations

Après avoir démarré un nouveau script, la première chose à faire est de remplir les informations du script en haut. Allez-y et remplissez les attributs suivants comme vous le souhaitez :

* nom
* description
* auteur

Je vais vous montrer à quoi ressemble le mien.

#### Ajouter jQuery

Juste avant la ligne

```
// ==/UserScript==
```

ajoutez une ligne avec le texte suivant :

```
// @require http://code.jquery.com/jquery-latest.js
```

Considérez cela comme l'importation/le requêtage de jQuery pour un projet JS.

#### Voici le mien

![Image](https://cdn-media-1.freecodecamp.org/images/9BlQRN0ORWp6K2ak0A-f6UD71dWwN4bTrDYp)
_informations du script remplies_

### Bonjour script.js !

Voyons si notre script se charge sur [http://news.ycombinator.com](http://news.ycombinator.com) et si jQuery est prêt à l'emploi.

Après la ligne // _votre code ici_, ajoutez le code suivant :

```
$(document).ready(function() {  alert('GAGNÉ');});
```

et appuyez sur **Ctrl + s** ou cliquez sur le bouton de sauvegarde à gauche.

Vous pourriez être redirigé vers la page suivante. Sinon, cliquez sur l'onglet « Userscripts installés ».

![Image](https://cdn-media-1.freecodecamp.org/images/RwzBGDralHUJYCaJUxb6ZFE1J-fo-IKkp1RT)
_page des userscripts installés_

Super ! Notre script est chargé dans Tamper Monkey. Le point vert à gauche signifie que le script est activé. Vous pouvez même voir le logo de Hacker News dans la capture d'écran.

#### Exécuter le script

Visitez [Hacker News](http://news.ycombinator.com) dans votre navigateur et, si vous avez suivi les instructions et que tout s'est bien passé, vous devriez voir :

![Image](https://cdn-media-1.freecodecamp.org/images/kjO1MKNyMj0C1jza9KjXNqozJbJVwQJNjAJ2)
_boîte de dialogue d'alerte fonctionnelle_

### Lancer le débogueur

Il est temps de trouver les éléments de publication que nous voulons modifier. Appuyez sur **Ctrl + Shift + i** pour ouvrir le débogueur du navigateur.

Maintenant, nous voulons sélectionner un élément pour l'examiner de plus près. Cliquer sur le carré bleu avec la souris en haut à gauche du débogueur ouvrira le sélecteur d'éléments. Vous pouvez également utiliser la commande **Ctrl + Shift + c**.

![Image](https://cdn-media-1.freecodecamp.org/images/K57nqIwcj2tQz8CqY31YuHLVdClePaxYqHFX)
_sélecteur d'éléments_

Comme vous pouvez le voir, j'ai trouvé un élément appelé _td.title_. Après avoir cliqué dessus, l'élément est mis en surbrillance dans l'onglet des éléments du débogueur (également montré ci-dessus).

En surbrillant l'élément au-dessus de notre titre appelé

```
<tr class="athing">
```

sélectionne ceci dans le navigateur

![Image](https://cdn-media-1.freecodecamp.org/images/3jTJbC0gL7Irgh-qfpzNbW5hksEdjfTKC6O5)
_BINGO_

Bingo. Il semble que nous ayons trouvé l'élément que nous voulons. Hacker News a une structure HTML propre, donc ce n'était pas trop difficile de trouver notre élément cible.

Si vous vous souvenez de votre jQuery, tout ce que vous avez à faire pour trouver tous les éléments de publication est d'utiliser le sélecteur

```
$('.athing')
```

#### Faire quelque chose avec notre élément de publication

Maintenant que nous avons un moyen de sélectionner notre élément avec jQuery, nous pouvons modifier notre élément. Changeons la couleur de fond des publications en utilisant le code suivant. Changez le code $(document).ready() en ceci :

```
$(document).ready(function() {  $('.athing').css('background-color', '#DDD');});
```

_note : #DDD est une abréviation pour #DDDDDD ;_

Regardons la page résultante. N'oubliez pas de sauvegarder votre userscript, puis d'actualiser la page HackerNews. Vous devrez peut-être fermer votre débogueur pour voir toute la page.

![Image](https://cdn-media-1.freecodecamp.org/images/vkeMepNz7Ixs6vh5lBbQqqBrtqwSaqnKK4TG)
_page d'accueil de Hacker News modifiée_

Avons-nous terminé ? Pas tout à fait. Nous avons modifié tous nos éléments de publication au lieu de les alterner. Cela peut ressembler à l'effet zébré que nous voulions, mais c'est seulement parce que l'élément score/subinfo n'est pas affecté. _Si vous souhaitez également modifier cet élément, n'hésitez pas et partagez votre méthode dans les commentaires. Cela dépasse le cadre de ce guide._

_Oh non ?! Que faisons-nous... Je ne veux pas écrire de boucles !_

#### jQuery à la rescousse

N'ayez crainte, chers Campeurs. jQuery est encore une fois à la rescousse.

jQuery fournit des sélecteurs spéciaux pour une occasion comme celle-ci.

Voici **:odd**

[**:odd Selector**](https://api.jquery.com/odd-selector/)  
[_Description : Sélectionne les éléments impairs, indexés à partir de zéro. Voir aussi even. En particulier, notez que l'indexation basée sur 0 signifie..._api.jquery.com](https://api.jquery.com/odd-selector/)

Tout ce que nous avons à faire est d'ajouter **:odd** à la fin de notre sélecteur pour que la ligne ressemble à ceci. _note : J'ai également changé la couleur en #EEE ; pour mieux s'intégrer._

```
    $(' .athing:odd ').css('background-color', '#EEE');
```

Enregistrez votre script, actualisez HackerNews et vous devriez voir ce produit final

![Image](https://cdn-media-1.freecodecamp.org/images/U2VcB-db2IvtuKrjzSfEfcKxU3jYxARMG1rV)
_produit final_

### Conclusion

Voilà. Vous avez maintenant un autre exutoire créatif pour libérer votre magie de codage naissante ! Les scripts utilisateur peuvent être utilisés pour ajuster la fonctionnalité ou l'apparence d'un site, pour ajouter une fonctionnalité que vous avez toujours voulue, et bien plus encore.

#### Devoirs

Écrivez votre propre script utilisateur pour ajouter quelque chose à un site web que vous utilisez souvent. Qu'il s'agisse de style ou d'un bouton qui peut basculer la visibilité de certains éléments, tout dépend de vous. Partagez votre produit dans les commentaires ici !

Allez de l'avant et conquérez, Campeurs !

#### Plus de lectures

[**Tampermonkey**](https://tampermonkey.net/documentation.php)  
[_Tampermonkey est une extension de navigateur gratuite et le gestionnaire de userscripts le plus populaire pour les navigateurs basés sur Blink comme Chrome..._tampermonkey.net](https://tampermonkey.net/documentation.php)[**GreaseSpot Wiki**](http://wiki.greasespot.net/Main_Page)  
[_GreaseSpot est une documentation communautaire pour le scripting utilisateur avec Greasemonkey._wiki.greasespot.net](http://wiki.greasespot.net/Main_Page)[**Greasy Fork - scripts utilisateur sûrs et utiles**](https://greasyfork.org/en)  
[_Les scripts utilisateur vous donnent le contrôle de votre expérience de navigation. Une fois installés, ils modifient automatiquement les sites que vous..._greasyfork.org](https://greasyfork.org/en)[**Commencer : Construire une extension Chrome**](https://developer.chrome.com/extensions/getstarted)  
[_Les extensions vous permettent d'ajouter des fonctionnalités à Chrome sans plonger profondément dans le code natif. Vous pouvez créer de nouvelles..._developer.chrome.com](https://developer.chrome.com/extensions/getstarted)[**Comment développer une extension Firefox**](https://blog.mozilla.org/addons/2009/01/28/how-to-develop-a-firefox-extension/)  
[_Cet article de blog est très obsolète. Si vous voulez un guide plus récent pour le développement d'extensions, veuillez lire le nouveau Comment..._blog.mozilla.org](https://blog.mozilla.org/addons/2009/01/28/how-to-develop-a-firefox-extension/)