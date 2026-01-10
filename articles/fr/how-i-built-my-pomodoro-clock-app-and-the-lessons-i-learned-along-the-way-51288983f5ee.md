---
title: Comment j'ai construit mon application Pomodoro Clock, et les leçons que j'ai
  apprises en cours de route
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-09T04:31:16.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-my-pomodoro-clock-app-and-the-lessons-i-learned-along-the-way-51288983f5ee
coverImage: https://cdn-media-1.freecodecamp.org/images/0*NTDCi8iO84iyCE8U.
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit mon application Pomodoro Clock, et les leçons que
  j'ai apprises en cours de route
seo_desc: 'By Cynthia Lee

  I embarked on my freeCodeCamp journey in Dec 2017, and am two projects shy of completing
  the Front-End Development Certificate. This post documents my process of completing
  the Pomodoro Clock project.

  What is a Pomodoro Clock?

  The Pomo...'
---

Par Cynthia Lee

J'ai commencé mon parcours [freeCodeCamp](https://www.freecodecamp.org) en décembre 2017, et il me reste deux projets à compléter pour obtenir le Certificat de Développement Front-End. Cet article documente mon processus de réalisation du projet Pomodoro Clock.

### Qu'est-ce qu'une Pomodoro Clock ?

La [Technique Pomodoro](https://francescocirillo.com/pages/pomodoro-technique/?utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier) est un cadre de gestion du temps qui est aussi simple qu'efficace - vous utilisez un minuteur pour diviser votre travail en blocs de temps (généralement 25 minutes), séparés par une pause de 5 minutes. Après chaque série de 4 pomodoros, vous pouvez prendre une pause plus longue.

Je devais satisfaire les histoires utilisateur suivantes :

* Je peux démarrer un pomodoro de 25 minutes, et le minuteur sonnera une fois les 25 minutes écoulées.
* Je peux réinitialiser le minuteur pour mon prochain pomodoro.
* Je peux personnaliser la durée de chaque pomodoro.

### Conception / disposition

![Image](https://cdn-media-1.freecodecamp.org/images/1*usZAFrV70goblyvT6zfFcA.jpeg)

Mon principe de conception est de garder l'interface utilisateur propre et simple. J'ai adoré l'idée d'utiliser une tomate comme minuteur. Il y a un affichage travail/pause, un compte à rebours du minuteur, et un bouton lecture/pause.

Sous le minuteur, j'avais des paramètres pour modifier la durée du travail et de la pause, et un bouton de réinitialisation.

### Problèmes de disposition rencontrés

J'ai eu des problèmes majeurs pour positionner l'image de la tomate en arrière-plan sous les autres éléments. Comme je souhaiterais qu'il y ait une option de disposition que je pourrais sélectionner ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*ANAEwK4kQz5UaGlDIGBW1A.png)
_Les bonnes vieilles options de disposition d'image de Microsoft Word_

Une suggestion que j'ai trouvée était d'enregistrer l'image de la tomate sur ma couleur d'arrière-plan préférée en tant que nouvelle image, puis d'utiliser cette image en arrière-plan. L'inconvénient était que cela commençait à avoir l'air bizarre une fois que j'ai testé la réactivité de la disposition.

Finalement, j'ai réussi à le faire correctement avec une combinaison de `positionnement absolu`, en modifiant les pourcentages `top` et `left`, et `transform`.

```
#status {  position: absolute;  top: 45%;  left:50%;  transform: translate(-50%, -50%);}
```

```
.timerDisplay {  position: absolute;  top: 60%;  left: 50%;  transform: translate(-50%, -50%);}
```

```
#start-btn {  position: absolute;  bottom: 8%;  left: 48%;  transform: translate(-50%, -50%);}
```

Les paramètres du bas étaient assez simples. J'ai utilisé CSS Grid pour séparer les composants en trois colonnes, la colonne du milieu faisant la moitié de la largeur des colonnes extérieures.

```
.settings {  margin: auto;  width: 80%;  display: grid;  grid-template-columns: 2fr 1fr 2fr;  align-items: center;}
```

Une fois de plus, j'ai utilisé `transform` pour décaler le bouton de réinitialisation pour un meilleur alignement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g8a8NTOJi_tkSlmLzCckWA.jpeg)

### Structuration de mon code - et puis le démanteler

Je trouve utile de définir la structure de mon code si je décompose les exigences :

* Le minuteur basculera entre le démarrage et la pause lorsque je cliquerai sur le bouton 'start'.
* Une fois que le minuteur atteint zéro, une alarme se déclenche.
* Une session de travail est toujours suivie d'une session de pause.
* Les durées de travail et de pause peuvent être modifiées.
* Le bouton 'reset' réinitialisera le minuteur.

J'avais précédemment complété un compte à rebours dans le cours [JavaScript30](https://javascript30.com/) de Wes Bos, donc je savais que je pouvais utiliser la méthode `setInterval`. J'ai également décidé de me challenger en restant sur du JavaScript vanilla, et d'éviter de dépendre de jQuery.

Et ainsi j'ai commencé à écrire mon code JavaScript. Bien que j'ai réussi à créer une horloge pomodoro fonctionnelle, je ne vais pas passer en revue la première version de mon code ici. Cela est dû au fait que j'ai apporté des modifications significatives après avoir reçu des commentaires constructifs d'un amazing stranger sur Reddit. ?

Oui, de bonnes choses arrivent sur Reddit !

Les points principaux des commentaires étaient :

* `setInterval(timer, 1000)` prend au moins 1000 ms pour se déclencher, mais peut prendre plus de temps. Vous devriez donc vérifier combien de temps s'est réellement écoulé, ou votre horloge peut être inexacte.
* Regroupez toutes les mises à jour HTML dans une seule section, car cela rend votre code plus facile à mettre à jour et à déboguer.
* Il est généralement bon de faire le code sans penser à la représentation.
* Soyez sûr de la logique du minuteur, et supprimez le code inutile.
* Assurez-vous que les noms des variables sont descriptifs. Laissez des commentaires lorsque cela est nécessaire.

Vous pouvez voir mon premier commit sur [GitHub](https://github.com/CynthiaLixinLee/pomodoro-timer/commit/dbf2d9f0afb4a7ad208a3326f520e1e5ab40e422#diff-42f69825340f0b5fa628d80900a46daa).

### Refactorisation de mon code

Après avoir reçu tous ces commentaires précieux, j'ai refactorisé mon code plusieurs fois jusqu'à ce que j'en sois satisfaite.

Tout d'abord, j'ai défini toutes les variables. Comme je n'utilisais pas jQuery, j'ai veillé à capturer tous mes éléments en utilisant `document.querySelector`.

```
let countdown = 0; // variable pour définir/effacer les intervalleslet seconds = 1500; // secondes restantes sur l'horlogelett workTime = 25;let breakTime = 5;let isBreak = true;let isPaused = true;
```

```
const status = document.querySelector("#status");const timerDisplay = document.querySelector(".timerDisplay");const startBtn = document.querySelector("#start-btn");const resetBtn = document.querySelector("#reset");const workMin = document.querySelector("#work-min");const breakMin = document.querySelector("#break-min");
```

Ensuite, j'ai créé l'élément audio.

```
const alarm = document.createElement('audio'); alarm.setAttribute("src", "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3");
```

Lorsque le bouton 'start' est cliqué, l'intervalle est effacé. Un nouvel intervalle est défini si `isPaused` passe de _true_ à _false_.

Le bouton 'reset' efface l'intervalle et réinitialise les variables.

```
startBtn.addEventListener('click', () => {  clearInterval(countdown);  isPaused = !isPaused;  if (!isPaused) {    countdown = setInterval(timer, 1000);  }})
```

```
resetBtn.addEventListener('click', () => {  clearInterval(countdown);  seconds = workTime * 60;  countdown = 0;  isPaused = true;  isBreak = true;})
```

La **fonction timer** est là où la magie du compte à rebours se produit. Elle soustrait une seconde de **seconds**. Si **seconds <**; 0, l'alarme est jouée, et la fonction détermine si le prochain compte à rebours doit être une session de travail ou une session de pause.

```
function timer() {  seconds --;  if (seconds < 0) {    clearInterval(countdown);    alarm.currentTime = 0;    alarm.play();    seconds = (isBreak ? breakTime : workTime) * 60;    isBreak = !isBreak;  }}
```

Maintenant, il est temps de travailler sur les boutons +/- pour les durées de travail et de pause. Initialement, j'ai créé une fonction `onclick` pour chaque bouton. Bien que cela fonctionnait, il y avait définitivement de la place pour l'amélioration.

```
document.querySelector("#work-plus").onclick = function() {         workDuration < 60 ? workDuration += increment : workDuration;                   }document.querySelector("#work-minus").onclick = function() {         workDuration > 5 ? workDuration -= increment : workDuration;              }document.querySelector("#break-plus").onclick = function() {     breakDuration < 60 ? breakDuration += increment : breakDuration;                     }document.querySelector("#break-minus").onclick = function() {        breakDuration > 5 ? breakDuration -= increment : breakDuration;                  }
```

Ce même Redditor sympathique a suggéré que j'utilise un [tableau associatif](http://www.i-programmer.info/programming/javascript/1441-javascript-data-structures-the-associative-array.html), qui est essentiellement un ensemble de paires clé-valeur.

```
let incrementFunctions =    {"#work-plus": function () { workTime = Math.min(workTime + increment, 60)},     "#work-minus": function () { workTime = Math.max(workTime - increment, 5)},     "#break-plus": function () { breakTime = Math.min(breakTime + increment, 60)},     "#break-minus": function () { breakTime = Math.max(breakTime - increment, 5)}};
```

```
for (var key in incrementFunctions) {    if (incrementFunctions.hasOwnProperty(key)) {      document.querySelector(key).onclick = incrementFunctions[key];    }}
```

Il est temps de mettre à jour le HTML !

J'ai créé des fonctions pour mettre à jour l'affichage du compte à rebours et l'affichage du bouton, et j'ai incorporé ces fonctions dans une fonction globale qui mettait également à jour le statut Travail/Pause et les durées.

Enfin, j'ai utilisé `document.onclick` pour exécuter la **fonction updateHTML** chaque fois que l'utilisateur clique sur la page. J'ai également utilisé `window.setInterval` pour exécuter la fonction 10 fois par seconde pour bonne mesure.

```
function countdownDisplay() {  let minutes = Math.floor(seconds / 60);  let remainderSeconds = seconds % 60;  timerDisplay.textContent = `${minutes}:${remainderSeconds < 10 ? '0' : ''}${remainderSeconds}`;}
```

```
function buttonDisplay() {  if (isPaused && countdown === 0) {    startBtn.textContent = "START";  } else if (isPaused && countdown !== 0) {    startBtn.textContent = "Continue";   } else {    startBtn.textContent = "Pause";  }}
```

```
function updateHTML() {  countdownDisplay();  buttonDisplay();  isBreak ? status.textContent = "Keep Working" : status.textContent = "Take a Break!";  workMin.textContent = workTime;  breakMin.textContent = breakTime;}
```

```
window.setInterval(updateHTML, 100);
```

```
document.onclick = updateHTML;
```

Et c'est le résumé de mon projet !

Vous pouvez voir mon projet final [ici](https://codepen.io/cynthiaLixinLee/full/xWzdRK/).

### Réflexions finales

Ma plus grande leçon de ce projet est que je devrais viser la simplicité en termes de conception de code, car c'est un prérequis pour la fiabilité. Cela rendra mon code facile à comprendre, facile à déboguer et facile à mettre à jour.

Je suis également rappelée des avantages de la programmation en binôme et des revues de code, surtout lorsque l'on est nouveau dans le codage.

Il y a encore tant à apprendre. Mais pour l'instant, laissez-moi me récompenser avec une assiette de Pasta al pomodoro.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OnSu8IZp3yv85Qe_.)
_Photo par [Unsplash](https://unsplash.com/@olamishchenko?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">OLA Mishchenko</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_