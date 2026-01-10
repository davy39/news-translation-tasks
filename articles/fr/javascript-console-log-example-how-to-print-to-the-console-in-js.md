---
title: Exemple JavaScript Console.log() – Comment afficher dans la console en JS
subtitle: ''
author: Jesse Hall
co_authors: []
series: null
date: '2020-09-09T21:01:11.000Z'
originalURL: https://freecodecamp.org/news/javascript-console-log-example-how-to-print-to-the-console-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/fCC_-Console.log.png
tags:
- name: console
  slug: console
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
seo_title: Exemple JavaScript Console.log() – Comment afficher dans la console en
  JS
seo_desc: 'Logging messages to the console is a very basic way to diagnose and troubleshoot
  minor issues in your code.

  But, did you know that there is more to console than just log? In this article,
  I''ll show you how to print to the console in JS, as well as al...'
---

L'enregistrement de messages dans la console est un moyen très basique de diagnostiquer et de résoudre des problèmes mineurs dans votre code.

Mais, saviez-vous qu'il y a plus à `console` que juste `log` ? Dans cet article, je vais vous montrer comment afficher dans la console en JS, ainsi que toutes les choses que vous ne saviez pas que `console` pouvait faire.

## Éditeur Multi-lignes de la Console Firefox

Si vous n'avez jamais utilisé le mode éditeur multi-lignes dans Firefox, vous devriez l'essayer dès maintenant !

Ouvrez simplement la console, `Ctrl+Shift+K` ou `F12`, et dans le coin supérieur droit, vous verrez un bouton qui dit "Passer en mode éditeur multi-lignes". Alternativement, vous pouvez appuyer sur `Ctrl+B`.

Cela vous donne un éditeur de code multi-lignes directement dans Firefox.

## console.log

Commençons par un exemple de log très basique.

```js
let x = 1
console.log(x)
```

Tapez cela dans la console Firefox et exécutez le code. Vous pouvez cliquer sur le bouton "Exécuter" ou appuyer sur `Ctrl+Entrée`.

Dans cet exemple, nous devrions voir "1" dans la console. Assez simple, n'est-ce pas ?

## Valeurs Multiples

Saviez-vous que vous pouvez inclure plusieurs valeurs ? Ajoutez une chaîne au début pour identifier facilement ce que vous enregistrez.

```js
let x = 1
console.log("x:", x)
```

Mais que faire si nous avons plusieurs valeurs que nous voulons enregistrer ?

```js
let x = 1
let y = 2
let z = 3
```

Au lieu de taper `console.log()` trois fois, nous pouvons toutes les inclure. Et nous pouvons ajouter une chaîne avant chacune d'elles si nous le souhaitons.

```js
let x = 1
let y = 2
let z = 3
console.log("x:", x, "y:", y, "z:", z)
```

Mais c'est trop de travail. Il suffit de les envelopper avec des accolades ! Maintenant, vous obtenez un objet avec les valeurs nommées.

```js
let x = 1
let y = 2
let z = 3
console.log( {x, y, z} )
```

![Sortie de la Console](https://www.freecodecamp.org/news/content/images/2020/09/image-34.png align="left")

*Sortie de la Console*

Vous pouvez faire la même chose avec un objet.

```js
let user = {
  name: 'Jesse',
  contact: {
    email: 'codestackr@gmail.com'
  }
}
console.log(user)
console.log({user})
```

Le premier log affichera les propriétés de l'objet utilisateur. Le second identifiera l'objet comme "user" et affichera les propriétés qu'il contient.

Si vous enregistrez de nombreuses choses dans la console, cela peut vous aider à identifier chaque log.

## Variables dans le log

Saviez-vous que vous pouvez utiliser des portions de votre log comme variables ?

```js
console.log("%s a %d ans.", "John", 29)
```

Dans cet exemple, `%s` fait référence à une option de chaîne incluse après la valeur initiale. Cela ferait référence à "John".

Le `%d` fait référence à une option de chiffre incluse après la valeur initiale. Cela ferait référence à 29.

La sortie de cette instruction serait : "John a 29 ans.".

## Variations des logs

Il existe quelques variations de logs. Il y a le plus largement utilisé `console.log()`. Mais il y a aussi :

```js
console.log('Console Log')
console.info('Console Info')
console.debug('Console Debug')
console.warn('Console Warn')
console.error('Console Error')
```

Ces variations ajoutent du style à nos logs dans la console. Par exemple, le `warn` sera coloré en jaune, et le `error` sera coloré en rouge.

Note : Les styles varient d'un navigateur à l'autre.

## Logs Optionnels

Nous pouvons afficher des messages dans la console conditionnellement avec `console.assert()`.

```js
let isItWorking = false
console.assert(isItWorking, "voici la raison")
```

Si le premier argument est faux, alors le message sera enregistré.

Si nous devions changer `isItWorking` en `true`, alors le message ne sera pas enregistré.

## Compter

Saviez-vous que vous pouvez compter avec la console ?

```js
for(i=0; i<10; i++){
  console.count()
}
```

Chaque itération de cette boucle affichera un compte dans la console. Vous verrez "default: 1, default: 2", et ainsi de suite jusqu'à ce qu'il atteigne 10.

Si vous exécutez cette même boucle à nouveau, vous verrez que le compte reprend là où il s'était arrêté ; 11 - 20.

Pour réinitialiser le compteur, nous pouvons utiliser `console.countReset()`.

Et, si vous voulez nommer le compteur autre chose que "default", vous pouvez !

```js
for(i=0; i<10; i++){
  console.count('Compteur 1')
}
console.countReset('Compteur 1')
```

Maintenant que nous avons ajouté une étiquette, vous verrez "Compteur 1, Compteur 2", et ainsi de suite.

Et pour réinitialiser ce compteur, nous devons passer le nom dans `countReset`. De cette façon, vous pouvez avoir plusieurs compteurs en cours d'exécution en même temps et ne réinitialiser que ceux spécifiques.

## Suivre le Temps

Outre le comptage, vous pouvez également chronométrer quelque chose comme un chronomètre.

Pour démarrer un chronomètre, nous pouvons utiliser `console.time()`. Cela ne fera rien par lui-même. Donc, dans cet exemple, nous utiliserons `setTimeout()` pour émuler l'exécution de code. Ensuite, dans le timeout, nous arrêterons notre chronomètre en utilisant `console.timeEnd()`.

```js
console.time()
setTimeout(() => {
  console.timeEnd()
}, 5000)
```

Comme vous vous en doutez, après 5 secondes, nous aurons un log de fin de chronomètre de 5 secondes.

Nous pouvons également enregistrer le temps actuel de notre chronomètre pendant son exécution, sans l'arrêter. Nous faisons cela en utilisant `console.timeLog()`.

```js
console.time()

setTimeout(() => {
  console.timeEnd()
}, 5000)

setTimeout(() => {
  console.timeLog()
}, 2000)
```

Dans cet exemple, nous obtiendrons d'abord notre `timeLog` de 2 secondes, puis notre `timeEnd` de 5 secondes.

Tout comme le compteur, nous pouvons étiqueter les chronomètres et en avoir plusieurs en cours d'exécution en même temps.

## Groupes

Une autre chose que vous pouvez faire avec `log` est de les regrouper.

Nous commençons un groupe en utilisant `console.group()`. Et nous terminons un groupe avec `console.groupEnd()`.

```js
console.log('Je ne suis pas dans un groupe')

console.group()
console.log('Je suis dans un groupe')
console.log('Je suis aussi dans un groupe')
console.groupEnd()

console.log('Je ne suis pas dans un groupe')
```

Ce groupe de logs sera pliable. Cela facilite l'identification des ensembles de logs.

Par défaut, le groupe n'est pas plié. Vous pouvez le définir comme plié en utilisant `console.groupCollapsed()` à la place de `console.group()`.

Les étiquettes peuvent également être passées dans le `group()` pour mieux les identifier.

## Trace de la Pile

Vous pouvez également faire une trace de la pile avec `console`. Il suffit de l'ajouter dans une fonction.

```js
function one() {
  two()
}
function two() {
  three()
}
function three() {
  console.trace()
}
one()
```

Dans cet exemple, nous avons des fonctions très simples qui s'appellent simplement les unes les autres. Ensuite, dans la dernière fonction, nous appelons `console.trace()`.

![Sortie de la Console](https://www.freecodecamp.org/news/content/images/2020/09/image-35.png align="left")

*Sortie de la Console*

## Tableaux

Voici l'une des utilisations les plus incroyables de la console : `console.table()`.

Alors, préparons quelques données à enregistrer :

```js
let devices = [
  {
    name: 'iPhone',
    brand: 'Apple'
  },
  {
    name: 'Galaxy',
    brand: 'Samsung'
  }
]
```

Maintenant, nous allons enregistrer ces données en utilisant `console.table(devices)`.

![Sortie de la Console](https://www.freecodecamp.org/news/content/images/2020/09/image-36.png align="left")

*Sortie de la Console*

Mais attendez – ça devient encore mieux !

Si nous voulons seulement les marques, il suffit de faire `console.table(devices, ['brand'])` !

![Sortie de la Console](https://www.freecodecamp.org/news/content/images/2020/09/image-37.png align="left")

*Sortie de la Console*

Et un exemple plus complexe ? Dans cet exemple, nous allons utiliser jsonplaceholder.

```js
async function getUsers() {
  let response = await fetch('https://jsonplaceholder.typicode.com/users')
  let data = await response.json()
 
  console.table(data, ['name', 'email'])
}

getUsers()
```

Ici, nous imprimons simplement le "name" et "email". Si vous `console.log` toutes les données, vous verrez qu'il y a beaucoup plus de propriétés pour chaque utilisateur.

## Style

Saviez-vous que vous pouvez utiliser des propriétés CSS pour styliser vos logs ?

Pour ce faire, nous utilisons `%c` pour spécifier que nous avons des styles à ajouter. Les styles sont passés dans le deuxième argument du `log`.

```js
console.log("%c Ceci est un texte jaune sur un fond bleu.", "color:yellow; background-color:blue")
```

Vous pouvez utiliser cela pour faire ressortir vos logs.

## Effacer

Si vous essayez de résoudre un problème en utilisant des logs, vous pouvez actualiser beaucoup et votre console peut devenir encombrée.

Il suffit d'ajouter `console.clear()` en haut de votre code et vous aurez une console fraîche à chaque fois que vous actualisez.

Il suffit de ne pas l'ajouter en bas de votre code, lol.

## Merci d'avoir lu !

Si vous voulez revisiter les concepts de cet article via une vidéo, vous pouvez consulter cette [version vidéo que j'ai faite ici](https://youtu.be/_-bHhEGcDiQ).

%[https://youtu.be/_-bHhEGcDiQ]

![Jesse Hall (codeSTACKr)](https://www.freecodecamp.org/news/content/images/2020/06/footer-banner-1.png align="left")

Je suis Jesse du Texas. Consultez mes autres contenus et faites-moi savoir comment je peux vous aider dans votre parcours pour devenir développeur web.

* [Abonnez-vous à ma chaîne YouTube](https://youtube.com/codeSTACKr)
    
* Dites Bonjour ! [Instagram](https://instagram.com/codeSTACKr) | [Twitter](https://twitter.com/codeSTACKr)
    
* [Inscrivez-vous à ma Newsletter](https://codestackr.com/)