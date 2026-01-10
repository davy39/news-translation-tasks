---
title: Comment déboguer JavaScript avec les outils de développement de votre navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T22:14:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-javascript-with-your-browsers-devtools
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cb5740569d1a4ca33be.jpg
tags:
- name: Browsers
  slug: browsers
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Comment déboguer JavaScript avec les outils de développement de votre navigateur
seo_desc: 'As a developer you will often want to debug code. You might have already
  used console.log in some of the challenges, which is the simplest way to debug.

  In this article we will tell you some of the coolest tricks, to debug using the
  native debug-tool...'
---

En tant que développeur, vous voudrez souvent déboguer du code. Vous avez peut-être déjà utilisé `console.log` dans certains des défis, ce qui est la manière la plus simple de déboguer.

Dans cet article, nous allons vous montrer quelques-uns des trucs les plus cool pour déboguer en utilisant les outils de débogage natifs des navigateurs.

## **Un bref aperçu de l'éditeur de code FreeCodeCamp :**

Avant de plonger dans le débogage, laissons fuir quelques faits secrets sur ce _moteur de vérification de code génial_ chez FCC.

Nous utilisons un [CodeMirror](http://codemirror.net/mode/javascript/index.html) personnalisé, comme éditeur de code. Une fonction [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) est utilisée pour évaluer le code JavaScript représenté sous forme de chaîne de caractères depuis l'éditeur. Lorsque `eval()` est appelée, les navigateurs exécuteront nativement votre code. Nous apprendrons plus tard dans cet article pourquoi ce secret est important.

## **Passons maintenant aux astuces :**

## **Outils de développement Google Chrome**

Google Chrome est l'un des navigateurs les plus populaires avec un moteur JavaScript intégré appelé [V8](https://developers.google.com/v8/), et offre un excellent ensemble d'outils pour les développeurs appelé [Chrome DevTools](https://developer.chrome.com/devtools). Visiter leur [Guide complet de débogage JavaScript](https://developer.chrome.com/devtools/docs/javascript-debugging) est fortement recommandé.

### **1 : Les bases des DevTools**

#### **Lancement des Chrome DevTools**

Appuyez sur `F12`. Alternativement, vous pouvez presser

`Ctrl` + `Shift` + `I`

sur Windows et Linux ou

`Cmd` + `Shift` + `I`

sur Mac, ou si vous aimez simplement votre souris, allez dans `Menu > Plus d'outils > Outils de développement`.

#### **Découverte des onglets `Sources` et `console`.**

Ces deux onglets seront probablement vos meilleurs amis lors du débogage. L'onglet `Sources` peut être utilisé pour visualiser tous les scripts présents sur la page web que vous visitez. Cet onglet contient des sections pour la fenêtre de code, l'arborescence des fichiers, la pile d'appels et les fenêtres de surveillance, etc.

L'onglet `console` est l'endroit où toutes les sorties de journalisation sont affichées. De plus, vous pouvez utiliser l'invite de l'onglet console pour exécuter du code JavaScript. C'est un peu synonyme de l'invite de commande sur Windows, ou du terminal sur Linux.

_Astuce : Basculer vers la console à tout moment dans les DevTools en utilisant la touche `Esc`._

### **2 : Raccourcis courants et fonctionnalités**

Bien que vous puissiez consulter la [liste complète des raccourcis](https://developers.google.com/web/tools/chrome-devtools/iterate/inspect-styles/shortcuts), voici quelques-uns des plus utilisés :

Fonctionnalité Windows, Linux Mac  
Rechercher un mot-clé, les regex sont supportées. `Ctrl`+`F``Cmd`+`F`  
Rechercher et ouvrir un fichier `Ctrl`+`P``Cmd`+`P`  
Aller à la ligne `Ctrl`+`G`+`:line_no``Cmd`+`G`+`:line_no`  
Ajouter un point d'arrêt `Ctrl`+`B`, ou cliquer sur le numéro de ligne`Cmd`+`B`, ou cliquer sur le numéro de ligne  
Mettre en pause / reprendre l'exécution du script `F8` `F8`  
Passer à l'appel de fonction suivant `F10` `F10`  
Entrer dans l'appel de fonction suivant `F11` `F11`

### **3 : Utilisation d'une Source Map pour notre code**

L'une des fonctionnalités les plus cool que vous allez adorer est le [débogage de script dynamique](https://developer.chrome.com/devtools/docs/javascript-debugging#breakpoints-dynamic-javascript), à la volée, via les [Source Maps](https://developer.chrome.com/devtools/docs/javascript-debugging#source-maps).

Chaque script peut être visualisé dans l'onglet Source des DevTools. L'onglet source contient tous les fichiers sources JavaScript. Mais le code de l'éditeur de code est exécuté via `eval()` dans un conteneur simplement appelé une machine virtuelle (VM) au sein du processus du navigateur.

Comme vous l'avez peut-être deviné maintenant, notre code est en fait un script qui n'a pas de nom de fichier. Nous ne le voyons donc pas dans l'onglet Source.

![:sparkles:](https://forum.freecodecamp.com/images/emoji/emoji_one/sparkles.png?v=2)

**_Voici l'astuce !_**

![:sparkles:](https://forum.freecodecamp.com/images/emoji/emoji_one/sparkles.png?v=2)

Nous devons utiliser les `Source Maps` pour attribuer un nom au JavaScript de notre éditeur. C'est assez simple :

Supposons que nous sommes sur le défi [Factorialize](https://www.freecodecamp.com/challenges/factorialize-a-number), et que notre code ressemble à ceci :

```text
function factorialize(num) {
  if(num <= 1){
  ...
}
factorialize(5);
```

Tout ce que nous devons faire est d'ajouter `//# sourceURL=factorialize.js` en haut du code, c'est-à-dire la première ligne :

```text
//# sourceURL=factorialize.js

function factorialize(num) {
  if(num <= 1){
  ...
```

![:sparkles:](https://forum.freecodecamp.com/images/emoji/emoji_one/sparkles.png?v=2)

**_Et Eurêka, c'est tout !_**

![:sparkles:](https://forum.freecodecamp.com/images/emoji/emoji_one/sparkles.png?v=2)

Maintenant, ouvrez les DevTools et recherchez le nom du fichier. Ajoutez des points d'arrêt, déboguez et amusez-vous !

## Plus d'informations sur le débogage :

* [Guide du débutant pour écraser les bugs](https://www.freecodecamp.org/news/the-beginner-bug-squashing-guide/)
* [Conseils et astuces de débogage pour débutants](https://www.freecodecamp.org/news/debugging-javascript-for-beginners-5d4ac15dd1cd/)
* [Comment tirer le meilleur parti de la console de débogage de votre navigateur](https://www.freecodecamp.org/news/how-to-go-beyond-console-log-and-get-the-most-out-of-your-browsers-debugging-console-e185256a1115/)