---
title: Méthodes de la fenêtre JavaScript expliquées avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-window-methods-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d1d740569d1a4ca35fa.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Méthodes de la fenêtre JavaScript expliquées avec des exemples
seo_desc: 'Window location Method

  The window.location object can be used to get information on the current page address
  (URL) and to redirect the browser to a new page.

  The window.location object can be written without the window prefix, as just location.

  Some ...'
---

## **Méthode window.location**

L'objet `window.location` peut être utilisé pour obtenir des informations sur l'adresse de la page actuelle (URL) et pour rediriger le navigateur vers une nouvelle page.

L'objet `window.location` peut être écrit sans le préfixe `window`, simplement `location`.

## Quelques exemples :

* `window.location.href` retourne l'URL de la page actuelle
* `window.location.hostname` retourne le nom de domaine de l'hôte web
* `window.location.host` retourne à la fois le nom de l'hôte et tout port associé
* `window.location.pathname` retourne le chemin et le nom de fichier de la page actuelle
* `window.location.protocol` retourne le protocole web utilisé (http: ou https:)
* `window.location.assign()` charge un nouveau document

### Plus d'informations :

[MDN](https://developer.mozilla.org/docs/Web/API/Window/location)

## **Méthode window.setInterval**

La méthode `setInterval()` appelle une fonction ou évalue une expression à des intervalles spécifiés (en millisecondes).

```js
setInterval(function(){ 
  alert("Bonjour");
}, 3000); 
```

La méthode `setInterval()` continuera à appeler la fonction jusqu'à ce que `clearInterval()` soit appelée, ou que la fenêtre soit fermée.

La méthode `setInterval()` peut passer des paramètres supplémentaires à la fonction, comme le montre l'exemple ci-dessous.

```js
setInterval(function, milliseconds, parameter1, parameter2, parameter3); 
```

La valeur d'ID retournée par `setInterval()` est utilisée comme paramètre pour la méthode `clearInterval()`.

Conseils :

* 1000 ms = 1 seconde.
* Pour exécuter une fonction une seule fois, après un nombre spécifié de millisecondes, utilisez la méthode `setTimeout()`.

## Méthode window.setTimeout

La méthode `setTimeout()` définit un minuteur en millisecondes, puis appelle une fonction ou évalue une expression lorsque le minuteur expire.

Notes :

* `setTimeout()` utilise des millisecondes, et 1000 ms est égal à 1 seconde
* Cette méthode n'exécute la fonction ou l'expression que vous lui passez qu'une seule fois. Utilisez la méthode `setInterval()` si vous devez répéter l'exécution plusieurs fois
* Pour arrêter la fonction ou l'expression qui lui est passée, utilisez la méthode `clearTimeout()`

La syntaxe de la méthode `setTimeout()` est la suivante :

```js
setTimeout(function, milliseconds, param1, param2, ...);
```

Par exemple :

```js
setTimeout(function() { 
  alert("Bonjour");
}, 3000);
```

Une chose très importante à retenir à propos de `setTimeout()` est qu'il est exécuté de manière asynchrone :

```js
console.log("A");
setTimeout(function() { console.log("B"); }, 0);
console.log("C");

// L'ordre dans la console sera
// A
// C
// B
```

L'ordre des logs dans la console n'est probablement pas celui auquel vous vous attendiez. Pour résoudre ce problème et vous assurer que votre code est exécuté de manière synchrone, il vous suffit d'imbriquer la dernière instruction `console.log` dans la fonction :

```js
console.log("A");
setTimeout(function() {
    console.log("B");
    console.log("C");
}, 0);

// L'ordre dans la console sera
// A
// B
// C
```

## **Méthode window.clearTimeout**

La méthode `clearTimeout()` est utilisée pour arrêter un minuteur défini avec la méthode `setTimeout()`.

```js
    clearTimeout(setTimeout_ID); 
```

Pour pouvoir utiliser la méthode `clearTimeout()`, vous devez utiliser une variable globale. Voir l'exemple ci-dessous

La méthode `clearTimeout()` fonctionne en utilisant l'ID retourné par `setTimeout()`. Pour cette raison, il est souvent judicieux d'utiliser une variable globale pour stocker `setTimeout()`, puis de l'effacer lorsque cela est nécessaire :

```js
const myTimeout = setTimeout(function, milliseconds);

...

// Plus tard, pour effacer le timeout
clearTimeout(myTimeout);
```

## **Méthode window.clearInterval**

La méthode `clearInterval()` est utilisée pour effacer un minuteur défini avec la méthode `setInterval()`.

```js
clearInterval(setInterval_ID); 
```

La méthode `clearInterval()` fonctionne en utilisant l'ID retourné par `setInterval()`. Pour cette raison, il est souvent judicieux d'utiliser une variable globale pour stocker `setInterval()`, puis de l'effacer lorsque cela est nécessaire :

```js
const myInterval = setInterval(function, milliseconds);

...

// Plus tard, pour effacer le timeout
clearInterval(myInterval);
```

## Méthode window.localStorage

`localStorage` fournit un moyen pour vos applications web de stocker des paires clé/valeur localement dans le navigateur de l'utilisateur.

Avant HTML5 et `localStorage`, les données des applications web devaient être stockées dans des cookies. Chaque requête HTTP inclut des cookies, et ceux-ci étaient autrefois une méthode légitime pour stocker des données d'application localement sur les appareils clients. Cependant, beaucoup des mêmes données étaient transmises avec les cookies, et comme ils étaient limités à environ 4 Ko de données, il était difficile de stocker tout ce dont votre application avait besoin.

La limite de stockage pour `localStorage` est de 10 Mo de données par domaine, et il est considéré comme plus efficace car les informations qui y sont stockées ne sont jamais transférées au serveur avec chaque requête.

### **Types de stockage web**

`localStorage` est l'une des deux méthodes modernes pour que les navigateurs stockent des données localement :

* `localStorage` : stocke les données sans date d'expiration. Les données dans `localStorage` persistent même lorsque le navigateur de l'utilisateur est fermé et rouvert.
* `sessionStorage` : similaire à `localStorage`, sauf qu'il stocke les données pour une seule session. Ces données sont supprimées une fois que l'utilisateur ferme son navigateur.

### **Méthodes HTML5 localStorage**

`localStorage` est livré avec quelques méthodes JavaScript différentes qui le rendent très facile à utiliser.

Pour définir des données :

```javascript
localStorage.setItem('Nom', 'unevaleur');
```

Pour récupérer des données du stockage :

```javascript
localStorage.getItem('Nom');
```

Pour supprimer des données :

```javascript
localStorage.removeItem('Nom');
```

Pour tout effacer dans le stockage (pas seulement un élément individuel) :

```javascript
localStorage.clear();
```

Pour obtenir le nombre de propriétés dans le stockage :

```javascript
localStorage.length;
```

Note : Toutes les méthodes ci-dessus fonctionnent également avec `sessionStorage`. Il suffit de remplacer `localStorage` par `sessionStorage`.

## Méthode window.open

La méthode Window `open()` est utilisée pour ouvrir une nouvelle fenêtre ou un nouvel onglet de navigateur, selon les paramètres et les préférences de l'utilisateur. Cette méthode est généralement utilisée pour les popups, et est bloquée par défaut dans de nombreux navigateurs modernes.

La syntaxe de la méthode `open()` est :

```js
const window =  window.open(url, windowName, windowFeatures);
```

### Paramètres

* `url` : Une chaîne pour la ressource que vous souhaitez charger.
* `windowName` : Une chaîne indiquant le nom de la cible de la nouvelle fenêtre ou de l'onglet. Notez que cela ne sera pas utilisé comme titre pour la nouvelle fenêtre/onglet.
* `windowFeatures` : Une liste facultative séparée par des virgules de chaînes de fonctionnalités telles que la taille de la nouvelle fenêtre, sa position, si la barre de menu doit être affichée, etc.

### Exemple

```javascript
let windowObjectReference;
const strWindowFeatures = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

function openRequestedPopup() {
  windowObjectReference = window.open("https://www.freecodecamp.org/", "fCC_WindowName", strWindowFeatures);
}

openRequestedPopup();
```

Le code ci-dessus tentera d'ouvrir une popup vers la page d'accueil de freeCodeCamp.

## **Méthode window.confirm**

Vous pouvez utiliser la méthode `confirm` pour demander à un utilisateur de confirmer une décision sur une page web. Lorsque vous appelez cette méthode, le navigateur affichera une boîte de dialogue avec deux choix du type « OK » et « Annuler ».

Par exemple, supposons que quelqu'un vient de cliquer sur un bouton Supprimer. Vous pourriez exécuter le code suivant :

```javascript
if (window.confirm("Êtes-vous sûr de vouloir supprimer cet élément ?")) {
  // Supprimer l'élément
}
```

Le message « Êtes-vous sûr de vouloir supprimer cet élément ? » apparaîtra dans la boîte de dialogue. Si l'utilisateur clique sur OK, la méthode confirm retournera `true` et le navigateur exécutera le code à l'intérieur de l'instruction if. S'il clique sur Annuler, la méthode retournera `false` et rien d'autre ne se produira. Cela offre une certaine protection contre un clic accidentel sur Supprimer.