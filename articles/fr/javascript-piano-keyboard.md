---
title: Comment construire un clavier de piano en utilisant JavaScript Vanilla
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-11T22:35:36.000Z'
originalURL: https://freecodecamp.org/news/javascript-piano-keyboard
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/twitterCard-piano.jpg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
- name: Tutorial
  slug: tutorial
seo_title: Comment construire un clavier de piano en utilisant JavaScript Vanilla
seo_desc: 'By Joe Liang

  Making a playable piano keyboard can be a great way to learn a programming language
  (besides being heaps of fun). This tutorial shows you how to code one using vanilla
  JavaScript without the need for any external libraries or frameworks....'
---

Par Joe Liang

Créer un clavier de piano jouable peut être un excellent moyen d'apprendre un langage de programmation (en plus d'être très amusant). Ce tutoriel vous montre comment en coder un en utilisant JavaScript Vanilla sans avoir besoin de bibliothèques ou de frameworks externes.

Voici le [clavier de piano JavaScript](http://1000mileworld.com/Portfolio/Piano/keyboard.html) que j'ai créé si vous voulez voir le produit final d'abord.

Ce tutoriel suppose que vous avez une compréhension de base de JavaScript, comme les fonctions et la gestion des événements, ainsi qu'une familiarité avec HTML et CSS. Sinon, il est totalement adapté aux débutants et destiné à ceux qui veulent améliorer leurs compétences en JavaScript par l'apprentissage basé sur des projets (ou qui veulent simplement réaliser un projet cool !).

Le clavier de piano que nous réalisons pour ce projet est basé sur le [clavier synthétique généré dynamiquement](https://keithwhor.com/music/) créé par Keith William Horwood. Nous allons étendre le nombre de touches disponibles à 4 octaves et définir de nouvelles associations de touches.

Bien que son clavier puisse jouer des sons d'autres instruments, nous allons garder les choses simples et nous en tenir au piano.

Voici les étapes que nous allons suivre pour réaliser ce projet :

1.      [Obtenir les fichiers de travail](#heading-1-obtenir-les-fichiers-de-travail)

2.      [Configurer les associations de touches](#heading-2-configurer-les-associations-de-touches)

3.      [Générer le clavier](#heading-3-generer-le-clavier)

4.      [Gérer les pressions de touches](#heading-4-gerer-les-pressions-de-touches)

Commençons !

<h2 id="step1">1. Obtenir les fichiers de travail</h2>

Ce tutoriel utilisera les fichiers suivants :

·        [audiosynth.js](https://keithwhor.github.io/audiosynth/)

·        [playKeyboard.js](https://github.com/1000mileworld/Piano-Keyboard/blob/master/playKeyboard.js)

Comme mentionné, nous allons baser notre clavier de piano sur celui créé par Keith. Naturellement, nous allons également emprunter une partie de son code, qu'il a aimablement autorisé avec audiosynth.js.

Nous incorporons audiosynth.js dans playKeyboard.js (ma version modifiée de certains codes de Keith) qui gère tout notre JavaScript. Ce tutoriel donne une explication détaillée dans les sections suivantes sur les points majeurs de la façon dont le code de ce fichier crée un clavier de piano entièrement fonctionnel.

Nous laissons le fichier audiosynth.js intact, car il est uniquement responsable de la génération des sons.

Le code de ce fichier distingue ce clavier de piano des autres trouvés en ligne en utilisant JavaScript pour générer dynamiquement le son approprié lorsque l'utilisateur appuie sur une touche. Ainsi, le code n'a pas besoin de charger de fichiers audio externes.

Keith fournit déjà une explication de la façon dont la génération de sons fonctionne sur son site Web, donc nous n'entrerons pas dans les détails ici.

En résumé, cela implique l'utilisation de la fonction `Math.sin()` en JS pour créer des formes d'onde sinusoïdales et les transformer pour qu'elles ressemblent davantage à des instruments réels grâce à des mathématiques sophistiquées.

Créez un fichier HTML index, et liez les fichiers JS dans l'en-tête :

```html
<script src="audiosynth.js"></script>
<script src="playKeyboard.js"></script>


Dans le corps, nous pouvons créer un élément `<div>` vide pour servir de "conteneur" pour notre clavier :

```html
<div id="keyboard"></div>

Nous lui donnons un nom d'identifiant afin de pouvoir y faire référence plus tard lorsque nous créerons le clavier en utilisant JS. Nous pouvons exécuter notre code JS en l'appelant dans le corps également :

```html
<script type="text/javascript">playKeyboard()</script>

Nous utilisons playKeyboard.js comme une grande fonction. Il s'exécutera dès que le navigateur atteindra cette ligne de code et générera un clavier entièrement fonctionnel dans l'élément `<div>` avec `id = "keyboard"`.

Les premières lignes de playKeyboard.js préparent la fonctionnalité pour les appareils mobiles (optionnel) et créent un nouvel objet `AudioSynth()`. Nous utilisons cet objet pour appeler les méthodes de audiosynth.js que nous avons liées précédemment. Nous utilisons l'une de ces méthodes au début pour définir un volume pour le son.

À la ligne 11, nous définissons la position du do central à la 4ème octave.

<h2 id="step2">2. Configurer les associations de touches</h2>

Avant de générer le clavier, nous devons configurer nos associations de touches, car elles déterminent combien de touches doivent être générées.

Je voulais initialement essayer de jouer les notes d'ouverture de "Für Elise" donc j'ai choisi une plage de 4 octaves pour un total de 48 touches noires et blanches. Cela a nécessité presque toutes les touches de mon clavier (PC) et vous pouvez inclure moins de touches si vous le souhaitez.

Un avertissement : je n'ai pas les meilleures associations de touches, donc elles peuvent sembler peu intuitives lorsque vous essayez réellement de jouer. Peut-être que c'est le prix à payer pour essayer de créer un clavier de 4 octaves.

Pour configurer les associations de touches, créez d'abord un objet qui utilisera le code de touche comme ses clés et la note à jouer comme ses valeurs (à partir de la ligne 15) :

```js
var keyboard = {
	/* ~ */
	192: 'C,-2',
	/* 1 */
	49: 'C#,-2',
	/* 2 */
	50: 'D,-2',
	/* 3 */
	51: 'D#,-2',
    //...et le reste des touches
}


Les commentaires désignent les touches qu'un utilisateur peut presser sur un clavier d'ordinateur. Si un utilisateur presse la touche tilde, alors le code de touche correspondant est 192. Vous pouvez obtenir le code de touche en utilisant un outil tel que keycode.info.

La valeur de la touche est la note à jouer et est écrite au format 'note, modificateur d'octave' où le modificateur d'octave représente la position relative de l'octave par rapport à l'octave contenant le do central. Par exemple, 'C, -2' est la note do 2 octaves en dessous du do central.

Notez qu'il n'y a pas de touches 'bémol'. Chaque note est représentée par un 'dièse'.

Pour rendre notre clavier de piano fonctionnel, nous devons préparer une table de recherche inverse où nous échangeons les paires `clé : valeur` de sorte que la note à jouer devienne la clé et le code de touche devienne la valeur.

Nous avons besoin d'une telle table car nous voulons itérer sur les notes musicales pour générer facilement notre clavier.

Voici où les choses peuvent devenir délicates : nous avons en fait besoin de 2 tables de recherche inverse.

Nous utilisons une table pour rechercher l'étiquette que nous voulons afficher pour la touche de l'ordinateur que nous pressons pour jouer une note (déclarée comme `reverseLookupText` à la ligne 164) et une seconde pour rechercher la touche réelle qui a été pressée (déclarée comme `reverseLookup` à la ligne 165).

Les plus perspicaces peuvent réaliser que les deux tables de recherche ont des codes de touche comme valeurs, donc quelle est la différence entre elles ?

Il s'avère que (pour des raisons qui m'échappent) lorsque vous obtenez un code de touche qui correspond à une touche et que vous essayez d'utiliser la méthode `String.fromCharCode()` sur ce code de touche, vous n'obtenez pas toujours la même chaîne représentant la touche pressée.

Par exemple, appuyer sur le crochet ouvert gauche donne le code de touche 219, mais lorsque vous essayez réellement de convertir le code de touche en une chaîne en utilisant `String.fromCharCode(219)`, il retourne "Û". Pour obtenir "[", vous devez utiliser le code de touche 91. Nous remplaçons les codes incorrects à partir de la ligne 168.

Obtenir le bon code de touche a initialement impliqué un peu d'essais et d'erreurs, mais plus tard, j'ai réalisé que vous pouvez simplement utiliser une autre fonction (`getDispStr()` à la ligne 318) pour forcer l'affichage de la bonne chaîne.

La majorité des touches se comportent correctement, mais vous pouvez choisir de commencer avec un clavier plus petit pour ne pas avoir à gérer les codes de touche incorrects.

<h2 id="step3">3. Générer le clavier</h2>

Nous commençons le processus de génération du clavier en sélectionnant notre élément `<div>` conteneur de clavier avec `document.getElementById('keyboard')` à la ligne 209.

À la ligne suivante, nous déclarons l'objet `selectSound` et définissons la propriété `value` à zéro pour que audioSynth.js charge le profil sonore pour le piano. Vous pouvez entrer une valeur différente (peut être 0-3) si vous voulez essayer d'autres instruments. Voir la ligne 233 de audioSynth.js avec `Synth.loadSoundProfile` pour plus de détails.

À la ligne 216 avec `var notes`, nous récupérons les notes disponibles pour une octave (C, C#, D...B) à partir de audioSynth.js.

Nous générons notre clavier en parcourant chaque octave et chaque note de cette octave. Pour chaque note, nous créons un élément `<div>` pour représenter la touche appropriée en utilisant `document.createElement('div')`.

Pour distinguer si nous devons créer une touche noire ou blanche, nous regardons la longueur du nom de la note. L'ajout d'un signe dièse rend la longueur de la chaîne supérieure à un (ex. 'C#') ce qui indique une touche noire et vice versa pour les touches blanches.

Pour chaque touche, nous pouvons définir une largeur, une hauteur et un décalage par rapport à la gauche en fonction de la position de la touche. Nous pouvons également définir des classes appropriées pour une utilisation ultérieure avec CSS.

Ensuite, nous étiquetons la touche avec la touche de l'ordinateur que nous devons presser pour jouer sa note et la stockons dans un autre élément `<div>`. C'est là que `reverseLookupText` est utile. À l'intérieur du même `<div>`, nous affichons également le nom de la note. Nous accomplissons tout cela en définissant la propriété innerHTML de l'étiquette et en ajoutant l'étiquette à la touche (lignes 240-242).

```js
label.innerHTML = '<b class="keyLabel">' + s + '</b>' + '<br /><br />' + n.substr(0,1) + 
'<span name="OCTAVE_LABEL" value="' + i + '">' + (__octave + parseInt(i)) + '</span>' + 
(n.substr(1,1)?n.substr(1,1):'');


De même, nous ajoutons un écouteur d'événement à la touche pour gérer les clics de souris (ligne 244) :

```js
thisKey.addEventListener(evtListener[0], (function(_temp) { return function() { fnPlayKeyboard({keyCode:_temp}); } })(reverseLookup[n + ',' + i]));

Le premier paramètre `evtListener[0]` est un événement `mousedown` déclaré beaucoup plus tôt à la ligne 7. Le deuxième paramètre est une fonction qui retourne une fonction. Nous avons besoin de `reverseLookup` pour obtenir le bon code de touche et nous passons cette valeur en tant que paramètre _temp à la fonction interne. Nous n'aurons pas besoin de reverseLookup pour gérer les événements `keydown` réels.

Ce code est pré-ES2015 (aka ES6) et l'équivalent mis à jour, espérons-le plus clair, est :

```js
const keyCode = reverseLookup[n + ',' + i];
thisKey.addEventListener('mousedown', () => {
  fnPlayKeyboard({ keyCode });
});


Après avoir créé et ajouté toutes les touches nécessaires à notre clavier, nous devons gérer la lecture réelle d'une note.

<h2 id="step4">4. Gérer les pressions de touches</h2>

Nous gérons les pressions de touches de la même manière, que l'utilisateur clique sur la touche ou presse la touche correspondante de l'ordinateur, en utilisant la fonction `fnPlayKeyboard` à la ligne 260. La seule différence est le type d'événement que nous utilisons dans `addEventListener` pour détecter la pression de touche.

Nous configurons un tableau appelé `keysPressed` à la ligne 206 pour détecter quelles touches sont pressées/cliquées. Pour simplifier, nous supposerons qu'une touche pressée peut inclure le fait qu'elle soit cliquée également.

Nous pouvons diviser le processus de gestion des pressions de touches en 3 étapes : ajouter le code de touche de la touche pressée à `keysPressed`, jouer la note appropriée et supprimer le code de touche de `keysPressed`.

La première étape consistant à ajouter un code de touche est facile :

```js
keysPressed.push(e.keyCode);

où `e` est l'événement détecté par `addEventListener`.

Si le code de touche ajouté est l'une des associations de touches que nous avons assignées, alors nous appelons `fnPlayNote()` à la ligne 304 pour jouer la note associée à cette touche.

Dans `fnPlayNote()`, nous créons d'abord un nouvel élément `Audio()` `container` pour notre note en utilisant la méthode `generate()` de audiosynth.js. Lorsque l'audio est chargé, nous pouvons alors jouer la note.

Les lignes 308-313 sont du code hérité et semblent pouvoir être simplement remplacées par `container.play()`, bien que je n'aie pas fait de tests approfondis pour voir quelle est la différence.

Supprimer une pression de touche est également assez simple, car vous pouvez simplement supprimer la touche du tableau `keysPressed` avec la méthode `splice` à la ligne 298. Pour plus de détails, voir la fonction appelée `fnRemoveKeyBinding()`.


La seule chose à laquelle nous devons faire attention est lorsque l'utilisateur maintient une touche ou plusieurs touches enfoncées. Nous devons nous assurer que la note ne joue qu'une seule fois pendant qu'une touche est maintenue enfoncée (lignes 262-267) :

```js
var i = keysPressed.length;
while(i--) {
	if(keysPressed[i]==e.keyCode) {
		return false;	
    }
}


Retourner `false` empêche le reste de `fnPlayKeyboard()` de s'exécuter.

<h2>Résumé</h2>

Nous avons créé un clavier de piano entièrement fonctionnel en utilisant JavaScript Vanilla !

Pour résumer, voici les étapes que nous avons suivies :

1.	Nous avons configuré notre fichier HTML index pour charger les fichiers JS appropriés et exécuter `playKeyboard()` dans `<body>` pour générer et rendre le clavier fonctionnel. Nous avons un élément `<div>` avec `id = "keyboard"` où le clavier sera affiché sur la page.
    
2.	Dans notre fichier JavaScript playKeyboard.js, nous avons configuré nos associations de touches avec des codes de touche comme clés et des notes musicales comme valeurs. Nous avons également créé deux tables de recherche inverse, dont l'une est responsable de la recherche de l'étiquette de touche appropriée en fonction de la note et l'autre de la recherche du bon code de touche.
    
3.	Nous générons dynamiquement le clavier en parcourant chaque note dans chaque plage d'octave. Chaque touche est créée en tant que son propre élément `<div>`. Nous utilisons les tables de recherche inverse pour générer l'étiquette de touche et le bon code de touche. Ensuite, un écouteur d'événement sur `mousedown` l'utilise pour appeler `fnPlayKeyboard()` pour jouer la note. L'événement `keydown` appelle la même fonction mais n'a pas besoin d'une table de recherche inverse pour obtenir le code de touche.
    
4.	Nous gérons les pressions de touches résultant de clics de souris ou de pressions de touches d'ordinateur en 3 étapes : ajouter le code de touche de la touche pressée à un tableau, jouer la note appropriée et supprimer le code de touche de ce tableau. Nous devons être prudents pour ne pas jouer répétitivement une note (à partir du début) pendant que l'utilisateur maintient une touche enfoncée.


Le clavier est maintenant entièrement fonctionnel mais peut sembler un peu terne. Je vous laisse la partie CSS ?

Encore une fois, voici le [clavier de piano JavaScript](http://1000mileworld.com/Portfolio/Piano/keyboard.html) que j'ai créé pour référence.

Si vous voulez en savoir plus sur le développement web et découvrir d'autres projets intéressants, visitez mon blog à [1000 Mile World](https://www.1000mileworld.com/).

Merci d'avoir lu et bon codage !