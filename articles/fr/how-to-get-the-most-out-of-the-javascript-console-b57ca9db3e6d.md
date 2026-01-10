---
title: Comment tirer le meilleur parti de la console JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-05T16:29:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-most-out-of-the-javascript-console-b57ca9db3e6d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mM2AMk0TRENA2zF2RMEebA.jpeg
tags:
- name: coding
  slug: coding
- name: console
  slug: console
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment tirer le meilleur parti de la console JavaScript
seo_desc: 'By Darryl Pargeter

  One of the most basic debugging tools in JavaScript is console.log(). The console
  comes with several other useful methods that can add to a developer’s debugging
  toolkit.

  You can use the console to perform some of the following tas...'
---

Par Darryl Pargeter

L'un des outils de débogage les plus basiques en JavaScript est `console.log()`. La `console` offre plusieurs autres méthodes utiles qui peuvent enrichir la boîte à outils de débogage d'un développeur.

Vous pouvez utiliser la `console` pour effectuer certaines des tâches suivantes :

* Afficher un minuteur pour aider au benchmarking simple
* Afficher un tableau pour présenter un tableau ou un objet dans un format facile à lire
* Appliquer des couleurs et d'autres options de style à la sortie avec CSS

### L'objet Console

L'objet `console` vous donne accès à la console du navigateur. Il vous permet d'afficher des chaînes de caractères, des tableaux et des objets qui aident à déboguer votre code. La `console` fait partie de l'objet `window` et est fournie par le [Browser Object Model (BOM)](https://www.w3schools.com/js/js_window.asp).

Nous pouvons accéder à la `console` de deux manières :

1. `window.console.log('Cela fonctionne')`
2. `console.log('Cela aussi')`

La deuxième option est essentiellement une référence à la première, nous utiliserons donc la deuxième pour économiser des frappes.

Une note rapide sur le BOM : il n'a pas de standard défini, donc chaque navigateur l'implémente de manière légèrement différente. J'ai testé tous mes exemples dans Chrome et Firefox, mais votre sortie peut apparaître différemment selon votre navigateur.

### Affichage de texte

![Image](https://cdn-media-1.freecodecamp.org/images/CDHqDu8Ng7T8WrGBf9mgWokjyNnIEjd2ShO0)
_Journalisation de texte dans la console_

L'élément le plus courant de l'objet `console` est `console.log`. Dans la plupart des scénarios, vous l'utiliserez pour accomplir la tâche.

Il existe quatre façons différentes d'afficher un message dans la console :

1. `log`
2. `info`
3. `warn`
4. `error`

Les quatre fonctionnent de la même manière. Vous passez simplement un ou plusieurs arguments à la méthode sélectionnée. Elle affiche ensuite une icône différente pour indiquer son niveau de journalisation. Dans les exemples ci-dessous, vous pouvez voir la différence entre un journal de niveau info et un journal de niveau avertissement/erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/DgMbvQnFNQOC7Y-1bMrzwtt9GJrXX9XQUAxy)
_Sortie simple et facile à lire_

![Image](https://cdn-media-1.freecodecamp.org/images/kJBGhn74KnIDM7HH23K6Lj9WS3z14rNLnKNq)
_Avec beaucoup de choses en cours, cela peut devenir difficile à lire_

Vous avez peut-être remarqué le message de journalisation d'erreur - il est plus voyant que les autres. Il affiche à la fois un fond rouge et une [trace de pile](https://en.wikipedia.org/wiki/Stack_trace), alors que `info` et `warn` ne le font pas. Bien que `warn` ait un fond jaune dans Chrome.

Ces différences visuelles aident lorsque vous devez identifier rapidement les erreurs ou avertissements dans la console. Vous voudrez vous assurer qu'ils sont supprimés pour les applications prêtes pour la production, sauf s'ils sont là pour avertir les autres développeurs qu'ils font quelque chose de mal avec votre code.

### Substitutions de chaînes

Cette technique utilise un espace réservé dans une chaîne qui est remplacé par le ou les autres arguments que vous passez à la méthode. Par exemple :

**Entrée** : `console.log('chaîne %s', 'substitutions')`

**Sortie** : `chaîne substitutions`

Le `%s` est l'espace réservé pour le deuxième argument `'substitutions'` qui vient après la virgule. Toutes les chaînes, entiers ou tableaux seront convertis en chaîne et remplaceront le `%s`. Si vous passez un objet, il affichera `[object Object]`.

Si vous voulez passer un objet, vous devez utiliser `%o` ou `%O` au lieu de `%s`.

`console.log('ceci est un objet %o', { obj: { obj2: 'bonjour' }})`

![Image](https://cdn-media-1.freecodecamp.org/images/7e7Q5uEtCa9FDlBIV2bDnMKrgGMQzLj7MuNv)

#### Nombres

La substitution de chaînes peut être utilisée avec des entiers et des valeurs à virgule flottante en utilisant :

* `%i` ou `%d` pour les entiers,
* `%f` pour les nombres à virgule flottante.

**Entrée** : `console.log('entier: %d, virgule flottante: %f', 1, 1.5)`

**Sortie** : `entier: 1, virgule flottante: 1.500000`

Les nombres à virgule flottante peuvent être formatés pour afficher uniquement un chiffre après le point décimal en utilisant `%.1f`. Vous pouvez faire `%.nf` pour afficher n chiffres après la virgule.

Si nous formatons l'exemple ci-dessus pour afficher un chiffre après le point décimal pour le nombre à virgule flottante, cela ressemblerait à ceci :

**Entrée** : `console.log('entier: %d, virgule flottante: %.1f', 1, 1.5)`

**Sortie** : `entier: 1, virgule flottante: 1.5`

#### Spécificateurs de format

1. `%s` | remplace un élément par une chaîne
2. `%(d|i)` | remplace un élément par un entier
3. `%f` | remplace un élément par un nombre à virgule flottante
4. `%(o|O)` | l'élément est affiché comme un objet.
5. `%c` | Applique le CSS fourni

#### Modèles de chaînes

Avec l'avènement d'ES6, les littéraux de gabarit sont une alternative aux substitutions ou à la concaténation. Ils utilisent des backticks (``) au lieu de guillemets, et les variables vont à l'intérieur de `${}` :

```
const a = 'substitutions';
```

```
console.log(`ours : ${a}`);
```

```
// ours : substitutions
```

Les objets s'affichent comme `[object Object]` dans les littéraux de gabarit, vous devrez donc utiliser la substitution avec `%o` ou `%O` pour voir les détails, ou les journaliser séparément.

L'utilisation de substitutions ou de modèles crée un code plus facile à lire par rapport à l'utilisation de la concaténation de chaînes : `console.log('bonjour' + str + '!');`.

#### Interlude de jolies couleurs !

Maintenant, il est temps pour quelque chose de plus amusant et coloré !

Il est temps de faire ressortir notre `console` avec différentes couleurs grâce aux substitutions de chaînes.

Je vais utiliser un exemple simulé d'Ajax qui nous donne à la fois un succès (en vert) et un échec (en rouge) à afficher. Voici la sortie et le code :

![Image](https://cdn-media-1.freecodecamp.org/images/n1PXbwS2SeGH0dXE007ItqJHQCuggJHktM4R)
_Ours dansants réussis et chauves-souris échouées_

```
const success = [ 'background: green', 'color: white', 'display: block', 'text-align: center'].join(';');
```

```
const failure = [ 'background: red', 'color: white', 'display: block', 'text-align: center'].join(';');
```

```
console.info('%c /dancing/bears a réussi !', success);console.log({data: { name: 'Bob', age: 'inconnu'}}); // réponse de données "simulée"
```

```
console.error('%c /dancing/bats a échoué !', failure);console.log('/dancing/bats n'existe pas');
```

Vous appliquez des règles CSS dans la substitution de chaîne avec l'espace réservé `%c`.

```
console.error('%c /dancing/bats a échoué !', failure);
```

Ensuite, placez vos éléments CSS comme argument de chaîne et vous pouvez avoir des journaux stylisés avec CSS. Vous pouvez ajouter plus d'un `%c` dans la chaîne également.

```
console.log('%cred %cblue %cwhite','color:red;','color:blue;', 'color: white;')
```

Cela affichera les mots 'red', 'blue' et 'white' dans leurs couleurs respectives.

Il y a assez peu de propriétés CSS supportées par la console. Je recommande d'expérimenter pour voir ce qui fonctionne et ce qui ne fonctionne pas. Encore une fois, vos résultats peuvent varier selon votre navigateur.

### Autres méthodes disponibles

Voici quelques autres méthodes `console` disponibles. Notez que certains éléments ci-dessous n'ont pas encore standardisé leurs APIs, donc il peut y avoir des incompatibilités entre les navigateurs. Les exemples ont été créés avec Firefox 51.0.1.

#### Assert()

`Assert` prend deux arguments — si le premier argument est évalué à une valeur fausse, alors il affiche le deuxième argument.

```
let isTrue = false;
```

```
console.assert(isTrue, 'Cela sera affiché');
```

```
isTrue = true;
```

```
console.assert(isTrue, 'Cela ne le sera pas');
```

Si l'assertion est fausse, elle affiche dans la console. Elle est affichée comme un journal de niveau erreur comme mentionné ci-dessus, vous donnant à la fois un message d'erreur rouge et une trace de pile.

#### Dir()

La méthode `dir` affiche une liste interactive de l'objet passé.

```
console.dir(document.body);
```

![Image](https://cdn-media-1.freecodecamp.org/images/7H18v4UkQtV4pWkPQRd-2SZ59PAJrCJRs8wU)
_Chrome affiche dir différemment_

En fin de compte, `dir` ne fait économiser qu'un ou deux clics. Si vous devez inspecter un objet à partir d'une réponse d'API, alors l'afficher de cette manière structurée peut vous faire gagner du temps.

#### Table()

La méthode `table` affiche un tableau ou un objet sous forme de tableau.

```
console.table(['Javascript', 'PHP', 'Perl', 'C++']);
```

![Image](https://cdn-media-1.freecodecamp.org/images/AofilibA6MzrmyNl3H7RsgBm1K2QLuyV29EI)
_Sortie pour un tableau_

Les indices du tableau ou les noms des propriétés de l'objet viennent sous la colonne d'index de gauche. Ensuite, les valeurs sont affichées dans la colonne de droite.

```
const superhero = {     firstname: 'Peter',    lastname: 'Parker',}console.table(superhero);
```

![Image](https://cdn-media-1.freecodecamp.org/images/SbvV6TS9682I3VROSpaOYkGwQvAcwxLiNZJ3)
_Sortie pour un objet_

**Note pour les utilisateurs de Chrome :** Cela a été porté à mon attention par un collègue, mais les exemples ci-dessus de la méthode `table` ne semblent pas fonctionner dans Chrome. Vous pouvez contourner ce problème en plaçant les éléments dans un tableau de tableaux ou un tableau d'objets :

```
console.table([['Javascript', 'PHP', 'Perl', 'C++']]);
```

```
const superhero = {     firstname: 'Peter',    lastname: 'Parker',}console.table([superhero]); 
```

#### Group()

`console.group()` est composé d'au moins trois appels `console`, et est probablement la méthode qui nécessite le plus de frappe pour être utilisée. Mais c'est aussi l'une des plus utiles (surtout pour les développeurs utilisant [Redux Logger](https://github.com/evgenyrodionov/redux-logger)).

Un appel quelque peu basique ressemble à ceci :

```
console.group();console.log('Je vais afficher');console.group();console.log('plus d'indentations')console.groupEnd();console.log('ohh regardez un ours');console.groupEnd();
```

Cela affichera plusieurs niveaux et s'affichera différemment selon votre navigateur.

Firefox montre une liste indentée :

![Image](https://cdn-media-1.freecodecamp.org/images/jSdMYntev2ydVCx140kpmRe7tEjhFnz8EJXz)

Chrome les montre dans le style d'un objet :

![Image](https://cdn-media-1.freecodecamp.org/images/Oh8RGjXDlufRuWiz0FWDsfRN7aTIxWcqaio3)

Chaque appel à `console.group()` démarrera un nouveau groupe, ou créera un nouveau niveau s'il est appelé à l'intérieur d'un groupe. Chaque fois que vous appelez `console.groupEnd()`, il terminera le groupe ou le niveau actuel et remontera d'un niveau.

Je trouve que le style de sortie de Chrome est plus facile à lire car il ressemble davantage à un objet pliable.

Vous pouvez passer à `group` un argument d'en-tête qui sera affiché au-dessus de `console.group` :

```
console.group('En-tête');
```

Vous pouvez afficher le groupe comme replié dès le départ si vous appelez `console.groupCollapsed()`. D'après mon expérience, cela semble fonctionner uniquement dans Chrome.

#### Time()

La méthode `time`, comme la méthode `group` ci-dessus, se compose de deux parties.

Une méthode pour démarrer le minuteur et une méthode pour l'arrêter.

Une fois le minuteur terminé, il affichera le temps d'exécution total en millisecondes.

Pour démarrer le minuteur, vous utilisez `console.time('id pour le minuteur')` et pour arrêter le minuteur, vous utilisez `console.timeEnd('id pour le minuteur')`. Vous pouvez avoir jusqu'à 10 000 minuteurs en cours d'exécution simultanément.

La sortie ressemblera un peu à ceci `minuteur : 0.57ms`

C'est très utile lorsque vous devez faire un peu de benchmarking rapide.

### Conclusion

Nous y voilà, un regard un peu plus approfondi sur l'objet console et certaines des autres méthodes qui l'accompagnent. Ces méthodes sont de grands outils à avoir à disposition lorsque vous devez déboguer du code.

Il y a quelques méthodes dont je n'ai pas parlé car leur API est encore en évolution. Vous pouvez en lire plus sur elles ou sur la console en général sur la [page MDN Web API](https://developer.mozilla.org/en/docs/Web/API/console) et sa [page de spécification vivante](https://console.spec.whatwg.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/JpR7GD0Z7rB6uiRKYUTQ9zJGSsQrXVZDCjjW)
_[https://developer.mozilla.org/en/docs/Web/API/console](https://developer.mozilla.org/en/docs/Web/API/console" rel="noopener" target="_blank" title=")_