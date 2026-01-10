---
title: Découvrez les différents environnements JavaScript dans React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T15:57:50.000Z'
originalURL: https://freecodecamp.org/news/get-to-know-different-javascript-environments-in-react-native-4951c15d61f5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*O9VH0AoEkPaiexMT
tags:
- name: Google Chrome
  slug: chrome
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
seo_title: Découvrez les différents environnements JavaScript dans React Native
seo_desc: 'By Khoa Pham

  React Native can be very easy to get started with, and then at some point problems
  occur and we need to dive deep into it.

  The other day we had a strange bug that was only occurring in production build,
  and in iOS only. A long backtrace ...'
---

Par Khoa Pham

React Native peut être très facile à [démarrer](https://facebook.github.io/react-native/docs/getting-started.html), et puis à un certain moment, des problèmes surviennent et nous devons plonger profondément dedans.

L'autre jour, nous avions un bug étrange qui ne se produisait que dans la version de production, et uniquement sur iOS. Une longue trace dans l'application a révélé qu'il était dû à l'échec du constructeur `Date`.

```
const date = new Date("2019-01-18 12:00:00")
```

Cela retourne l'objet `Date` correct en mode débogage, mais donne `Invalid Date` en version release. Qu'y a-t-il de spécial avec le constructeur `Date` ? Ici, j'utilise React Native 0.57.5 et aucune bibliothèque `Date`.

### Constructeur de Date

La meilleure ressource pour apprendre JavaScript est via les documents web de Mozilla, et en entrant [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) :

> Crée une instance JavaScript `**Date**` qui représente un moment unique dans le temps. Les objets `Date` utilisent un [Unix Time Stamp](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap04.html#tag_04_16), une valeur entière qui est le nombre de millisecondes depuis le 1er janvier 1970 UTC.

Faites attention à la manière dont Date peut être construit par dateString :

> `dateString` Valeur de chaîne représentant une date. La chaîne doit être dans un format reconnu par la méthode `[Date.parse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse)` (horodatages [IETF-compliant RFC 2822](http://tools.ietf.org/html/rfc2822#page-14) et également une [version de ISO8601](http://www.ecma-international.org/ecma-262/5.1/#sec-15.9.1.15)).

Ainsi, le constructeur `Date` utilise la méthode statique `Date.parse` sous le capot. Cela a des exigences très spécifiques concernant le format de la chaîne de date qu'il supporte.

> La représentation standard d'une chaîne de date et d'heure est une simplification du format étendu de date de calendrier ISO 8601 (voir la section [Date Time String Format](https://tc39.github.io/ecma262/#sec-date-time-string-format) dans la spécification ECMAScript pour plus de détails). Par exemple, `"2011-10-10"` (forme date uniquement), `"2011-10-10T14:48:00"` (forme date-heure), ou `"2011-10-10T14:48:00.000+09:00"` (forme date-heure avec millisecondes et fuseau horaire) peuvent être passés et seront analysés. Lorsque le décalage de fuseau horaire est absent, les formes date uniquement sont interprétées comme une heure UTC et les formes date-heure sont interprétées comme une heure locale.

> La spécification ECMAScript stipule : Si la chaîne ne conforme pas au format standard, la fonction peut revenir à des heuristiques spécifiques à l'implémentation ou à un algorithme d'analyse spécifique à l'implémentation. Les chaînes ou dates non reconnaissables contenant des valeurs d'éléments illégales dans les chaînes formatées ISO doivent amener `Date.parse()` à retourner `[NaN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)`.

La raison pour laquelle nous obtenons Invalid Date sur iOS doit être parce que le code a été exécuté dans deux environnements JavaScript différents et qu'ils ont somehow des implémentations différentes de la fonction d'analyse de date.

### Environnement JavaScript

Le guide React Native a une section dédiée sur les [environnements JavaScript](https://facebook.github.io/react-native/docs/javascript-environment).

Lorsque vous utilisez React Native, vous allez exécuter votre code JavaScript dans deux environnements :

* Dans la plupart des cas, React Native utilisera [JavaScriptCore](http://trac.webkit.org/wiki/JavaScriptCore), le moteur JavaScript qui alimente Safari. Notez que sur iOS, JavaScriptCore n'utilise pas JIT en raison de l'absence de mémoire exécutable writable dans les applications iOS.
* Lorsque vous utilisez le débogage Chrome, tout le code JavaScript s'exécute dans Chrome lui-même, communiquant avec le code natif via WebSockets. Chrome utilise [V8](https://code.google.com/p/v8/) comme moteur JavaScript.

Bien que les deux environnements soient très similaires, vous pourriez rencontrer certaines incohérences. Nous allons probablement expérimenter avec d'autres moteurs JavaScript à l'avenir, il est donc préférable d'éviter de dépendre des spécificités de tout runtime.

React Native utilise également Babel et certains polyfills pour avoir quelques transformateurs de syntaxe sympas, donc une partie du code que nous écrivons peut ne pas être nécessairement supportée nativement par `JavascriptCore`.

Maintenant, il est clair que lorsque nous déboguons notre application via le débogueur Chrome, cela fonctionne parce que le moteur V8 gère cela. Maintenant, essayez de désactiver le débogage JS à distance : nous pouvons voir que le constructeur Date ci-dessus échoue, ce qui signifie qu'il utilise `JavascriptCore`.

![Image](https://cdn-media-1.freecodecamp.org/images/McX7R1GC4WxTlr9sbez6pnjIDj8Fgld2VYmZ)

Pour confirmer ce problème, exécutons notre application dans Xcode et allons dans l'application Safari sur MacOS pour entrer dans le menu Développement. Sélectionnez le Simulateur actif et choisissez JSContext sur l'application iOS actuelle. N'oubliez pas de désactiver le débogage JS à distance afin que l'application utilise JavascriptCore :

![Image](https://cdn-media-1.freecodecamp.org/images/0pzO1brfkVZl7XGUWFYYaZ1UKwradjbpBDXY)

Maintenant, ouvrez la Console dans les outils de développement Safari, et nous devrions avoir accès à JavascriptCore à l'intérieur de notre application. Essayez d'exécuter le constructeur `Date` ci-dessus pour confirmer qu'il échoue :

![Image](https://cdn-media-1.freecodecamp.org/images/WiSWzBJwmprcSx0WmTJWwVcpViH39wKXodYu)

### Quels sont les formats de chaîne de date légitimes ?

Depuis 2016, [JavascriptCore](https://webkit.org/blog/6756/es6-feature-complete/) supporte la plupart des fonctionnalités ES6 :

> À partir de [r202125](https://trac.webkit.org/changeset/202125), JavaScriptCore supporte toutes les nouvelles fonctionnalités de la [spécification du langage ECMAScript 6 (ES6)](https://tc39.github.io/ecma262/#sec-integerindexedelementget)

Et cela a été pleinement confirmé un an plus tard dans [JSC ? ES6](https://webkit.org/blog/7536/jsc-loves-es6/)

> [ES2015](http://www.ecma-international.org/ecma-262/6.0/) (également connu sous le nom de ES6), la version de la spécification JavaScript ratifiée en 2015, est une énorme amélioration du pouvoir expressif du langage grâce à des fonctionnalités comme les [classes](http://www.2ality.com/2015/02/es6-classes-final.html), [for-of](https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/), [destructuring](http://www.2ality.com/2015/01/es6-destructuring.html), [spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator), [tail calls](http://www.2ality.com/2015/06/tail-call-optimization.html), et [beaucoup plus](http://kangax.github.io/compat-table/es6/)

> L'implémentation JavaScript de WebKit, appelée JSC (JavaScriptCore), [implémente toutes les fonctionnalités de ES6](https://webkit.org/blog/6756/es6-feature-complete/)

Pour plus de détails sur les fonctionnalités JavaScript supportées par différents moteurs JavaScript, visitez ce [tableau de comparaison ECMAScript](https://kangax.github.io/compat-table/es6/).

Maintenant, pour le format de chaîne de date, à partir de [Date.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/parse), visitons la spécification ECMAScript 2015 pour voir ce qu'elle dit sur le [format de chaîne de date](https://www.ecma-international.org/ecma-262/6.0/#sec-date-time-string-format) :

![Image](https://cdn-media-1.freecodecamp.org/images/yzDoA6FifKgbUKjcgt3Fe-dZAlgBGNnUicJV)

ECMAScript définit un format d'échange de chaîne pour les dates et heures basé sur une simplification du format étendu ISO 8601. Le format est le suivant : `**YYYY-MM-DDTHH:mm:ss.sss_Z_**`

Où les champs sont les suivants :

`**"T"**` apparaît littéralement dans la chaîne, pour indiquer le début de l'élément temps.

Ainsi, `JavascriptCore` nécessite le spécificateur `T` et V8 peut fonctionner sans lui. La solution pour l'instant est de toujours inclure ce spécificateur T. De cette manière, nous suivons toujours les normes ECMAScript pour nous assurer qu'il fonctionne dans différents environnements JavaScript.

```
const date = new Date("2019-01-18 12:00:00".replace(' ', 'T'))
```

Et maintenant, il retourne l'objet `Date` correct. Il peut y avoir des différences entre JavascriptCore sur iOS et macOS, et parmi différentes versions d'iOS. La leçon apprise ici est que nous devons toujours tester notre application minutieusement en production et sur des appareils pour nous assurer qu'elle fonctionne comme prévu.