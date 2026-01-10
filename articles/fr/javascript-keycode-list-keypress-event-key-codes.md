---
title: Liste des codes clés JavaScript – Codes clés pour Entrée, Espace, Retour arrière
  et plus
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-01-08T19:15:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-keycode-list-keypress-event-key-codes
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/freeCodeCamp-Cover.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Liste des codes clés JavaScript – Codes clés pour Entrée, Espace, Retour
  arrière et plus
seo_desc: "JavaScript keyboard events help you capture user interactions with the\
  \ keyboard. \nLike many other JavaScript events, the KeyboardEvent interface provides\
  \ all the required properties and methods for handling every keystroke a user makes\
  \ using the keyb..."
---

Les événements clavier JavaScript vous aident à capturer les interactions utilisateur avec le clavier. 

Comme de nombreux autres événements JavaScript, l'interface `KeyboardEvent` fournit toutes les propriétés et méthodes requises pour gérer chaque frappe effectuée par l'utilisateur avec le clavier.

De nombreux articles ont été écrits sur leur fonctionnement et leur utilisation. En même temps, [W3.org](https://www.w3.org/TR/uievents/#events-keyboardevents) continue de mettre à jour la spécification en introduisant de nouvelles propriétés, en dépréciant les propriétés existantes et en marquant certains codes comme hérités. 

Pour cette raison, il est essentiel pour les développeurs web de continuer à apprendre sur l'interface `KeyboardEvent` pour savoir exactement ce qu'ils doivent utiliser et ce qui n'est plus pertinent.

Dans cet article, nous allons apprendre sur :

* L'interface KeyboardEvent.
* Les types d'événements clavier sur lesquels nous devons nous concentrer.
* Les types d'événements clavier dont nous n'aurons peut-être jamais besoin.
* Les propriétés dont vous avez besoin en pratique et comment les différents navigateurs les gèrent.
* Ce qui est déprécié et ce qui est en usage.
* Un terrain de jeu pour essayer des choses pendant que nous apprenons.
* Enfin, la liste actuelle des codes clés pour référence et usage futur.

J'espère que vous allez l'apprécier.

# L'interface KeyboardEvent et les types d'événements

L'interface KeyboardEvent fournit des informations en utilisant les constantes définies, les propriétés et une seule méthode (en janvier 2021). Elle étend l'interface `UIEvent` qui étend finalement l'interface `Event`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/keyboardevent_hierarchy.png)
_Hiérarchie de KeyboardEvent_

Il existe principalement trois types d'événements clavier, `keydown`, `keypress` et `keyup`. Nous pouvons obtenir des informations contextuelles sur ces événements à partir des propriétés et méthodes de l'interface `KeyboardEvent`. 

Vous pouvez ajouter chacun de ces types d'événements à un élément HTML ou à un objet `document` en utilisant la méthode `addEventListener`. Voici un exemple d'écoute d'un événement `keydown` sur un élément dont l'id est 'type-here' :

```js
let elem = document.getElementById('type-here');

elem.addEventListener("keydown", function (event) {
    // Le paramètre event est de type KeyboardEvent
  	addRow(event);
});
```

Alternativement, vous pouvez utiliser les méthodes de gestion comme `onKeydown(event)`, `onKeyup(event)`, `onKeypress(event)` avec l'élément pour gérer les événements clavier. Voici un exemple de gestion d'un événement `keyup` sur un élément d'entrée :

```html
<input type="text" id="type-here" onkeyup="doSomething(event)">
```

Si vous affichez l'objet `event` dans la console du navigateur, vous verrez toutes ses propriétés et méthodes ainsi que celles qu'il hérite des interfaces `UIEvent` et `Event`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/event_info.png)
_J'ai pressé la touche `a` en gérant l'événement `keyup`_

# Essayez ce terrain de jeu interactif pour les événements clavier

Avant d'aller plus loin, que diriez-vous d'un terrain de jeu pour explorer tous les événements clavier, leurs propriétés, caractéristiques, et ainsi de suite ? Je pense que ce serait génial de l'utiliser en parallèle avec cet article et au-delà. 

Concentrez simplement votre curseur n'importe où dans l'application intégrée ci-dessous et tapez n'importe quelle touche pour voir les informations contextuelles à ce sujet. 

Vous pouvez également filtrer les événements que vous souhaitez en décochant les cases à cocher en haut. Alors essayez-le :

%[https://stackblitz.com/edit/js-keycodes?embed=1&file=index.html&hideExplorer=1&hideNavigation=1&view=preview]

> Si vous avez des problèmes pour accéder au terrain de jeu ci-dessus, vous pouvez accéder directement à cet outil ici : [https://keyevents.netlify.app/](https://keyevents.netlify.app/)  
>   
> Et vous pouvez trouver le code source de la démonstration ici : [https://github.com/atapas/js-keyevents-demo](https://github.com/atapas/js-keyevents-demo)

# keydown, keypress, keyup - lequel devriez-vous utiliser ?

Les événements clavier sont :

* `keydown` : Il se déclenche lorsqu'une touche est enfoncée.
* `keypress` : Il se déclenche uniquement lorsqu'une touche qui produit une [valeur de caractère](https://www.w3.org/TR/uievents/#character-value) est enfoncée. Par exemple, si vous appuyez sur la touche `a`, cet événement se déclenchera car la touche `a` produit une valeur de caractère de `97`. En revanche, cet événement ne se déclenchera pas lorsque vous appuyez sur la touche `shift` car elle ne produit pas de valeur de caractère. 
* `keyup` : Il se déclenche lorsqu'une touche est relâchée.

Si les trois événements sont attachés à un élément DOM, l'ordre de déclenchement serait :

1. D'abord, keydown
2. Ensuite, keypress (avec la condition indiquée ci-dessus)
3. Enfin, keyup

Parmi ces événements, l'événement clavier le plus utilisé (ou devrait l'être) est `keydown` car :

* L'événement `keydown` a la couverture maximale des touches pour produire les informations contextuelles. L'événement `keypress` fonctionne uniquement pour un sous-ensemble des touches. Vous ne pouvez pas capturer les événements des touches Alt, Ctrl, Shift, Meta et autres similaires avec un keypress. Cela signifie également que nous ne pouvons pas déclencher l'événement keypress avec des combinaisons de touches comme `Ctrl Z`, `Shift Tab`, etc.
* De plus, [l'événement `keypress`](https://www.w3.org/TR/uievents/#event-type-keypress) a été déprécié. C'est une raison suffisamment importante pour l'éviter.
* Bien que les événements `keydown` et `keyup` couvrent toutes les touches et soient bien supportés par la plupart des navigateurs, il existe quelques différences qui poussent `keydown` devant `keyup`. L'événement keydown se déclenche avant que le navigateur ne traite la touche, tandis que l'événement keyup se déclenche après que le navigateur a traité la touche. Si vous annulez un événement keydown (par exemple, en utilisant `event.preventDefault()`), l'action du navigateur sera également annulée. Dans le cas de l'événement keyup, l'action du navigateur ne sera pas annulée même si vous avez annulé l'événement.

Dans l'exemple ci-dessous, nous utilisons `event.preventDefault()` lorsqu'un événement `keydown` ou `keyup` se déclenche. L'action du navigateur pour écrire les caractères de la touche dans la zone de texte ne sera pas effectuée dans le cas de `keydown`, mais elle continuera à se produire pour `keyup`.

%[https://stackblitz.com/edit/js-key-down-up-test?devtoolsheight=33&embed=1&file=index.html]

Avec toutes ces explications, l'événement `keydown` est clairement le gagnant et devrait devenir le type d'événement clé le plus populaire (utilisé). 

# Comment utiliser les propriétés de KeyboardEvent en pratique

C'est la question à un milliard de dollars ! La réponse la plus courte est : cela dépend. Mais de quoi ? Cela dépend de :

* La prise en charge du navigateur pour votre application
* À quel point le code de votre application est hérité et combien êtes-vous prêt à refactoriser ?

Mais avant d'aller plus loin, voyons un aperçu de certaines des propriétés et méthodes utiles de l'interface `KeyboardEvent`.

| Propriété/Méthode | Description | Dépréciée/Obsolète | 
|------------------|-------------|--------------------|
| altKey           | Retourne un booléen (vrai/faux). La valeur est `true` lorsque la touche `Alt` est enfoncée.                   | Non |
| ctrlKey          | Retourne un booléen (vrai/faux). La valeur est `true` lorsque la touche `Control` est enfoncée.                   | Non |
| shiftKey         | Retourne un booléen (vrai/faux). La valeur est `true` lorsque la touche `Shift` est enfoncée.                   | Non |
| metaKey          | Retourne un booléen (vrai/faux). La valeur est `true` lorsque l'une des touches `Meta` est enfoncée.                   | Non |
| code             | Valeur de code de la touche physique. | Non |
| key              | La valeur réelle de la touche enfoncée. | Non |
| getModifierState() méthode | Retourne un booléen (vrai/faux). La valeur `true` indique l'état `on` de ces touches, `CapsLock`, `NumLock`, `Alt`, `Control`, `Shift`, `Meta`, etc.| Non |
| charCode         | Retourne la valeur Unicode. Cela a été déprécié et nous devrions utiliser la propriété `key` à la place. | Oui |
| keyCode          | Retourne le code numérique de la valeur enfoncée. Cela a été déprécié et nous devrions utiliser la propriété `key` à la place. | Oui |
| which            | Retourne le code numérique de la valeur enfoncée. Cela a été déprécié et nous devrions utiliser la propriété `key` à la place. | Oui |

Les trois dernières propriétés sont dépréciées et vous devriez utiliser la propriété `key` à la place. La propriété `key` a le [support navigateur le plus large](https://caniuse.com/?search=Keyboardevent.key). 

Elle est supportée sur :

* Microsoft Edge : Version >= 79
* Firefox : Version >= 29
* Google Chrome : Version >= 51
* Safari : Version >= 10.1

Ainsi, tant que vous n'utilisez pas de navigateurs plus anciens, la propriété `event.key` devrait suffire pour identifier une touche. Dans le cas où vous devez supporter un navigateur plus ancien, une meilleure solution de repli serait la propriété `event.which`.

```js
window.addEventListener("keydown", function (event) {
  
  if (event.key !== undefined) {
    // Gérer l'événement avec KeyboardEvent.key
  } else if (event.which !== undefined) {
    // Gérer l'événement avec KeyboardEvent.which
  }
});
```

Si votre code utilise l'une des propriétés dépréciées et que vous avez l'opportunité de refactoriser ce code, il est toujours préférable de le faire.

## Touches de modification

Les touches de modification sont les touches spéciales de votre clavier qui modifient le comportement par défaut des autres touches. `Control`, `Shift` et `Alt` sont des touches de modification. Lorsqu'une touche de modification est combinée avec une autre touche, vous pouvez vous attendre à ce qu'une action différente se produise. 

Par exemple, si vous appuyez sur la touche `z`, elle doit retourner la touche et le code pour la lettre z. Si vous la combinez avec la touche de modification `Control` et appuyez sur `Control z`, vous obtiendrez probablement une opération `Annuler`. Voyons cela avec quelques exemples supplémentaires dans la section suivante.

Les propriétés `event.altKey`, `event.ctrlKey`, `event.shiftKey`, etc., aident à détecter si une touche de modification a été enfoncée.

## Combinaisons de touches

Nous pouvons combiner plusieurs touches et effectuer des actions basées sur les combinaisons de touches. L'extrait de code ci-dessous montre comment combiner les touches `Control` et `z` pour définir une action :

```js
document
  .getElementById("to_focus")
  .addEventListener("keydown", function(event) {
    if (event.ctrlKey && event.key === "z") {
      // Faire quelque chose, peut-être une opération 'Annuler'
    }
});
```

Voici un autre exemple qui démontre quelques combinaisons de touches supplémentaires. Veuillez l'essayer :

%[https://stackblitz.com/edit/js-key-combinations?embed=1&file=index.js&hideExplorer=1&view=preview]

# Une liste complète des valeurs d'événements clés

Le tableau ci-dessous montre une liste de touches avec les valeurs `event.which`, `event.key` et `event.code`.

| Nom de la touche | event.which | event.key | event.code | Notes 
|-----------------|-------------|-----------|------------|------|
| backspace       | 8           | Backspace | Backspace |
| tab             | 9           | Tab       | Tab |
| enter           | 13          | Enter     | Enter |
| shift(gauche)   | 16          | Shift     | ShiftLeft | `event.shiftKey` est vrai |
| shift(droite)   | 16          | Shift     | ShiftRight | `event.shiftKey` est vrai |
| ctrl(gauche)    | 17          | Control   | ControlLeft | `event.ctrlKey` est vrai |
| ctrl(droite)    | 17          | Control   | ControlRight | `event.ctrlKey` est vrai |
| alt(gauche)     | 18          | Alt       | AltLeft | `event.altKey` est vrai |
| alt(droite)     | 18          | Alt       | AltRight | `event.altKey` est vrai |
| pause/break     | 19          | Pause     | Pause |
| caps lock       | 20          | CapsLock  | CapsLock |
| escape          | 27          | Escape    | Escape |
| space           | 32          |           | Space   | La valeur `event.key` est un espace unique.
| page up         | 33          | PageUp    | PageUp |
| page down       | 34          | PageDown  | PageDown |
| end             | 35          | End       | End |
| home            | 36          | Home      | Home |
| flèche gauche   | 37          | ArrowLeft | ArrowLeft |
| flèche haut     | 38          | ArrowUp   | ArrowUp |
| flèche droite   | 39          | ArrowRight | ArrowRight |
| flèche bas      | 40          | ArrowDown  | ArrowDown |
| print screen    | 44          | PrintScreen  | PrintScreen |
| insert          | 45          | Insert    | Insert |
| delete          | 46          | Delete    | Delete |
| 0               | 48          | 0         | Digit0 | 
| 1               | 49          | 1         | Digit1 |
| 2               | 50          | 2         | Digit2 |
| 3               | 51          | 3         | Digit3 |
| 4               | 52          | 4         | Digit4 |
| 5               | 53          | 5         | Digit5 |
| 6               | 54          | 6         | Digit6 |
| 7               | 55          | 7         | Digit7 |
| 8               | 56          | 8         | Digit8 |
| 9               | 57          | 9         | Digit9 |
| a               | 65          | a         | KeyA |
| b               | 66          | b         | KeyB |
| c               | 67          | c         | KeyC |
| d               | 68          | d         | KeyD |
| e               | 69          | e         | KeyE |
| f               | 70          | f         | KeyF |
| g               | 71          | g         | KeyG |
| h               | 72          | h         | KeyH |
| i               | 73          | i         | KeyI |
| j               | 74          | j         | KeyJ |
| k               | 75          | k         | KeyK |
| l               | 76          | l         | KeyL |
| m               | 77          | m         | KeyM |
| n               | 78          | n         | KeyN |
| o               | 79          | o         | KeyO |
| p               | 80          | p         | KeyP |
| q               | 81          | q         | KeyQ |
| r               | 82          | r         | KeyR |
| s               | 83          | s         | KeyS |
| t               | 84          | t         | KeyT |
| u               | 85          | u         | KeyU |
| v               | 86          | v         | KeyV |
| w               | 87          | w         | KeyW |
| x               | 88          | x         | KeyX |
| y               | 89          | y         | KeyY |
| z               | 90          | z         | KeyZ |
| touche windows gauche  | 91  | Meta | MetaLeft | `event.metaKey` est vrai |
| touche windows droite | 92  | Meta | MetaRight | `event.metaKey` est vrai |
| touche select (Menu contextuel) | 93 | ContextMenu | ContextMenu |
| pavé numérique 0         | 96  | 0 | Numpad0 |
| pavé numérique 1         | 97  | 1 | Numpad1 |
| pavé numérique 2         | 98  | 2 | Numpad2 |
| pavé numérique 3         | 99  | 3 | Numpad3 |
| pavé numérique 4         | 100 | 4 | Numpad4 |
| pavé numérique 5         | 101 | 5 | Numpad5 |
| pavé numérique 6         | 102 | 6 | Numpad6 |
| pavé numérique 7         | 103 | 7 | Numpad7 |
| pavé numérique 8      | 104 | 8 | Numpad8 |
| pavé numérique 9      | 105 | 9 | Numpad9 |
| multiplier      | 106 | * | NumpadMultiply |
| addition           | 107 | + | NumpadAdd |
| soustraction      | 109 | - | NumpadSubtract |
| point décimal | 110 | . | NumpadDecimal |
| division        | 111 | / | NumpadDivide |
| f1            | 112 | F1 | F1 |
| f2            | 113 | F2 | F2 |
| f3            | 114 | F3 | F3 |
| f4            | 115 | F4 | F4 |
| f5            | 116 | F5 | F5 |
| f6            | 117 | F6 | F6 |
| f7            | 118 | F7 | F7 |
| f8            | 119 | F8 | F8 |
| f9            | 120 | F9 | F9 |
| f10           | 121 | F10 | F10 |
| f11           | 122 | F11 | F11 |
| f12           | 123 | F12 | F12 |
| verrouillage numérique      | 144 | NumLock | NumLock |
| verrouillage défilement   | 145 | ScrollLock | ScrollLock |
| volume audio muet   | 173 | AudioVolumeMute |  | ⚠️ La valeur `event.which` est 181 dans Firefox. De plus, FF fournit la valeur de code comme `VolumeMute` |
| volume audio bas   | 174 | AudioVolumeDown |  | ⚠️ La valeur `event.which` est 182 dans Firefox. De plus, FF fournit la valeur de code comme `VolumeDown` |
| volume audio haut   | 175 | AudioVolumeUp |  | ⚠️ La valeur `event.which` est 183 dans Firefox. De plus, FF fournit la valeur de code comme `VolumeUp` |
| lecteur multimédia   | 181 | LaunchMediaPlayer |  | ⚠️ La valeur `event.which` est 0 (aucune valeur) dans Firefox. De plus, FF fournit la valeur de code comme `MediaSelect` |
| lancer application 1 | 182 | LaunchApplication1 |  | ⚠️ La valeur `event.which` est 0 (aucune valeur) dans Firefox. De plus, FF fournit la valeur de code comme `LaunchApp1` |
| lancer application 2 | 183 | LaunchApplication2 | | ⚠️ La valeur `event.which` est 0 (aucune valeur) dans Firefox. De plus, FF fournit la valeur de code comme `LaunchApp2` |
| point-virgule    | 186 | ; | Semicolon | ⚠️ La valeur `event.which` est 59 dans Firefox |
| signe égal    | 187 | = | Equal | ⚠️ La valeur `event.which` est 61 dans Firefox |
| virgule         | 188 | , | Comma |
| trait d'union          | 189 | - | Minus | ⚠️ La valeur `event.which` est 173 dans Firefox |
| point        | 190 | . | Period |
| barre oblique avant | 191 | / | Slash |
| Backquote/Accent grave  | 192 | ` | Backquote |
| parenthèse ouvrante  | 219 | [ | BracketLeft |
| barre oblique inverse    | 220 | \ | Backslash |
| parenthèse fermante | 221 | ] | BracketRight |
| guillemet simple  | 222 | ' | Quote |


Veuillez noter :

- `event.which` a été déprécié (ou est obsolète)
- La valeur `event.code` est la même pour les lettres minuscules (a) et majuscules (A). Cependant, la valeur `event.key` représente la lettre réelle.
- La valeur `event.which` est différente dans Firefox (FF) et les autres navigateurs pour les touches `égal (=)`, `point-virgule (;)` et `trait d'union/moins (-)`

# Et le clavier virtuel ?

Alors, qu'en est-il des claviers virtuels, comme l'utilisation de nos téléphones mobiles ou tablettes ou tout autre dispositif d'entrée ? 

La [spécification dit](https://w3c.github.io/uievents/#code-virtual-keyboards) que si le clavier virtuel a une disposition de touches et une fonctionnalité similaires à celles d'un clavier standard, alors il doit en résulter un attribut de code approprié. Sinon, il ne va pas retourner la bonne valeur.

# En résumé

Pour résumer :

* Vous pouvez utiliser `KeyboardEvent` pour capturer les interactions utilisateur avec un clavier.
* Il existe principalement trois événements clés, `keydown`, `keypress` et `keyup`.
* Nous devrions utiliser le type d'événement `keydown` autant que possible car il satisfait la plupart des cas d'utilisation.
* Le type d'événement `keypress` a été déprécié.
* La propriété `event.which` a été dépréciée. Utilisez `event.key` partout où possible.
* Si vous devez supporter un navigateur plus ancien, utilisez un repli approprié pour la détection des touches.
* Nous pouvons combiner plusieurs touches et effectuer des opérations.
* Le clavier virtuel supporte ces événements tant que la disposition et les fonctions sont similaires à celles d'un clavier standard.

C'est tout pour l'instant. Merci d'avoir lu jusqu'ici ! Restons en contact. Vous pouvez me mentionner sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary) avec des commentaires ou n'hésitez pas à suivre.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/keytype.gif)
_De https://giphy.com/_