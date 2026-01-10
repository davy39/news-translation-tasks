---
title: 'Les essentiels de JavaScript : les fonctions sont amusantes (et VIP) — si
  vous les comprenez'
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2017-12-13T16:34:11.000Z'
originalURL: https://freecodecamp.org/news/javascript-essentials-functions-are-fun-and-vip-if-you-understand-them-29da2d4c9641
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dPgqcIzS3u7W4GtshPkqiw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Les essentiels de JavaScript : les fonctions sont amusantes (et VIP) —
  si vous les comprenez'
seo_desc: 'Imagine you live in a village without tap water. To get water, you need
  to take an empty bucket, head to the well in the middle of the village, draw water
  from the well, and head back home.

  You need to draw water from this well multiple times a day. ...'
---

Imaginez que vous vivez dans un village sans eau courante. Pour obtenir de l'eau, vous devez prendre un seau vide, vous rendre au puits au milieu du village, puiser de l'eau et rentrer chez vous.

Vous devez puiser de l'eau dans ce puits plusieurs fois par jour. C'est fastidieux de dire « Je vais prendre un seau vide, aller au puits, puiser de l'eau et la ramener à la maison » chaque fois que vous expliquez ce que vous faites.

Pour simplifier, vous pouvez dire que vous allez « puiser de l'eau ».

Et, mon ami, vous venez de créer une fonction.

### Déclarer des fonctions

Une fonction est un bloc de code qui exécute des tâches dans un ordre spécifique, comme prendre un seau vide, aller au puits, puiser de l'eau, rentrer chez vous.

Elle peut être définie avec la syntaxe suivante :

```
function nomDeLaFonction (paramètres) {   // Faire des choses ici }
```

`function` est un mot-clé qui indique à JavaScript que vous définissez une fonction.

`nomDeLaFonction` est le nom de la fonction. Dans l'exemple donné ci-dessus, le nom de la fonction pourrait être `puiserDeLEau`.

Le nom de la fonction peut être n'importe quoi, tant qu'il suit les mêmes règles que [la déclaration de variables](https://zellwk.com/blog/javascript-variables). En d'autres termes, il doit suivre ces règles :

1. Il doit être en un seul mot
2. Il doit être composé uniquement de lettres, de chiffres ou de traits de soulignement (0–9, a-z, A-Z, `_`)
3. Il ne peut pas commencer par un chiffre
4. Il ne peut pas être l'un de ces [mots réservés](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Keywords)

`paramètres` est facultatif. Il s'agit d'une liste de variables séparées par des virgules que vous souhaitez déclarer pour votre fonction. Elles peuvent recevoir des valeurs lorsque vous utilisez la fonction.

### Utiliser des fonctions

Une fois que vous avez déclaré votre fonction, vous pouvez l'utiliser (ou l'**invoquer**, ou l'**appeler**, ou l'**exécuter**) en écrivant le nom de la fonction, suivi de parenthèses `()`.

Voici un exemple où une fonction `direBonjour` est déclarée et utilisée.

```
// Déclarer une fonction
```

```
function direBonjour () {  console.log('Bonjour le monde !')}
```

```
// Utiliser une fonction
direBonjour()
```

![Image](https://cdn-media-1.freecodecamp.org/images/2tUEWux7KrXmJ3nOwgVWcwYBycGn0C5E7xWq)

### L'indentation

Le code à l'intérieur d'un bloc (tout ce qui est entre les accolades `{}`) doit être indenté vers la droite. C'est une pratique importante qui vous aide à rendre le code plus facile à lire. Elle vous permet de voir d'un coup d'œil que `console.log('Bonjour le monde')` fait partie de `direBonjour`.

```
function direBonjour () {     // Cette instruction console.log fait partie de direBonjour       console.log('Bonjour le monde !') }
```

Vous pouvez choisir d'indenter avec deux espaces ou avec la touche de tabulation. Certaines personnes préfèrent les espaces, d'autres préfèrent la tabulation. Les deux sont corrects, tant que vous restez cohérent.

### Paramètres

La plupart des fonctions prennent des paramètres. Il s'agit d'une **liste de variables séparées par des virgules** que vous souhaitez déclarer pour votre fonction.

Vous pouvez avoir n'importe quel nombre de paramètres.

```
function nomDeLaFonction(param1, param2, param3) {   // Faire des choses ici }
```

Pour attribuer des valeurs à vos paramètres, vous passez des valeurs (appelées arguments) en les écrivant comme des valeurs séparées par des virgules dans les parenthèses.

Le premier argument serait attribué au premier paramètre, le deuxième argument au deuxième paramètre, et ainsi de suite.

```
nomDeLaFonction('arg1', 'arg2')
```

Rendons cela plus clair avec un exemple.

Supposons que vous souhaitiez écrire une fonction appelée `direNom` qui enregistre le prénom et le nom de famille d'une personne. La fonction ressemble à ceci :

```
function direNom(prenom, nomDeFamille) {   console.log('prenom est ' + prenom)   console.log('nomDeFamille est ' + nomDeFamille) }
```

Zell est mon prénom, Liew est mon nom de famille. Pour que la fonction fonctionne correctement, je passe mon `Zell` comme premier argument et `Liew` comme deuxième argument :

```
direNom('Zell', 'Liew') // prenom est Zell // nomDeFamille est Liew
```

Si vous avez déclaré un paramètre mais n'avez pas passé d'argument, votre paramètre serait `undefined`.

```
direNom() // prenom est undefined // nomDeFamille est undefined
```

### L'instruction return

Les fonctions peuvent avoir une instruction return qui se compose du mot-clé return et d'une valeur :

```
function nomDeLaFonction () {   return 'une-valeur' }
```

Lorsque JavaScript voit cette instruction return, il arrête d'exécuter le reste de la fonction et « retourne » (passe la valeur à l'appel de la fonction).

```
function obtenir2 () {   return 2   console.log('blah') // Ceci n'est pas exécuté } 
```

```
const resultats = obtenir2() console.log(resultats) // 2 // Note : Vous ne verriez pas 'blah' dans la console
```

Si la valeur de retour est une expression, JavaScript évalue l'expression avant de retourner la valeur.

Rappelez-vous, **JavaScript ne peut passer que des primitives** (comme String, Numbers, Booleans) **et des objets** (comme des fonctions, des tableaux et des objets) comme valeurs. **Tout le reste doit être évalué.**

### Flux d'une fonction

Les fonctions peuvent être difficiles à comprendre pour les débutants. Pour vous assurer de bien comprendre les fonctions, examinons ce qui se passe lorsque vous déclarez et utilisez une fonction. Cette fois, nous allons procéder étape par étape.

Voici le code que nous analysons :

```
function ajouter2 (nombre) {   return nombre + 2 } 
```

```
const nombre = ajouter2(8) console.log(nombre) // 10
```

Tout d'abord, vous devez déclarer une fonction avant de pouvoir l'utiliser. Dans la première ligne, JavaScript voit le mot-clé `function` et sait que la fonction s'appelle `ajouter2`.

Il saute le code dans la fonction à ce stade car la fonction n'est pas encore utilisée.

![Image](https://cdn-media-1.freecodecamp.org/images/3Lyv3yrvRYDJejfkjzqwIEI2kVVBuAf7eKiL)

Ensuite, JavaScript voit que vous déclarez une variable appelée `nombre` et que vous lui attribuez le résultat de `ajouter2(8)`.

Comme le côté droit (RHS) est un appel de fonction (une expression), JavaScript doit évaluer la valeur de `ajouter2(8)` avant de pouvoir l'attribuer à la variable `nombre`. Ici, il définit le paramètre `nombre` à `8`, puisque vous avez passé 8 comme argument lorsque vous appelez `ajouter2(8)`.

![Image](https://cdn-media-1.freecodecamp.org/images/841CTdivYu82iJ2t47IAH1jeXYAdxpRqUyuj)

Dans la fonction `ajouter2`, JavaScript voit une instruction return qui dit `nombre + 2`. Il s'agit d'une expression, il doit donc l'évaluer avant de continuer. Comme `nombre` est 8, `nombre + 2` doit être 10.

![Image](https://cdn-media-1.freecodecamp.org/images/9vp36RDRxZEuwXqTj-rVzVb8-HFey32Ye927)

Une fois que `nombre + 2` est évalué, JavaScript retourne la valeur à l'appel de la fonction. Il remplace l'appel de la fonction par la valeur retournée. Ainsi, `ajouter2(8)` devient 10.

![Image](https://cdn-media-1.freecodecamp.org/images/JK4u4jLfGskHLt-Dk4ByAo-pHvg0YMJeacuF)

Enfin, une fois que le RHS est évalué, JavaScript crée la variable `nombre` et lui attribue la valeur 10.

C'est ainsi que vous lisez le flux d'une fonction.

### Hoisting

Lorsque les fonctions sont déclarées avec une déclaration de fonction (ce que vous avez appris ci-dessus), elles sont remontées en haut de votre [portée](https://css-tricks.com/javascript-scope-closures/). Cela signifie que les deux ensembles de code suivants sont exactement identiques.

```
function direBonjour () {   console.log('Bonjour le monde !') } direBonjour() 
```

```
// Ceci est automatiquement converti en le code ci-dessus direBonjour() function direBonjour () {   console.log('Bonjour le monde !') }
```

Le hoisting des fonctions peut être déroutant car JavaScript change l'ordre de votre code. Je vous recommande vivement de déclarer vos fonctions avant de les utiliser. **Ne comptez pas sur le hoisting.**

### Déclarer des fonctions avec des expressions de fonction

Une deuxième façon de déclarer des fonctions est avec une expression de fonction. Ici, vous déclarez une variable, puis vous lui attribuez une fonction sans nom (une fonction anonyme).

```
const direBonjour = function () {   console.log('Ceci est déclaré avec une expression de fonction !') }
```

Notez que les fonctions déclarées avec des expressions de fonction ne sont pas automatiquement remontées en haut de votre portée.

```
direBonjour () // Erreur, direBonjour n'est pas défini const direBonjour = function () {   console.log('ceci est une fonction !') }
```

À ce stade, vous vous demandez peut-être si les expressions de fonction sont importantes. C'est une question courante. Pourquoi utiliser des expressions de fonction si vous pouvez déclarer des fonctions avec la syntaxe de déclaration de fonction ?

Elles sont importantes. Vous apprendrez pourquoi lorsque vous apprendrez à déclarer des méthodes d'objet et des [fonctions fléchées](https://zellwk.com/blog/es6#/arrow-functions).

### Conclusion

**Une fonction est un bloc de code qui exécute des tâches dans un ordre spécifique, comme prendre un seau vide, aller au puits, puiser de l'eau, rentrer chez vous.**

Vous appelez les fonctions en ajoutant un `()` à la fin du nom de la fonction. Lorsque vous le faites, vous pouvez ajouter des valeurs supplémentaires comme arguments à la fonction.

Chaque fonction peut avoir une instruction return qui « retourne » une valeur à l'appel de la fonction.

Dans la mesure du possible, ne comptez pas sur le hoisting lorsque vous écrivez des fonctions. Déclarez-les toujours avant de les utiliser.

**Cet article est un exemple de leçon de Learn JavaScript** — un cours qui vous aide à apprendre JavaScript pour créer des composants réels et pratiques à partir de zéro. **Vous aimerez Learn JavaScript si vous avez trouvé cet article utile. Si vous avez aimé cet article, je vous invite à [en savoir plus sur Learn JavaScript](https://learnjavascript.today/).**

(Oh, au fait, si vous avez aimé cet article, j'apprécierais que vous puissiez [le partager](http://twitter.com/share?text=Une%20fonction%20exécute%20des%20tâches%20dans%20un%20ordre%20spécifique%20(comme%20prendre%20un%20seau%20vide%2C%20aller%20au%20puits%2C%20puiser%20de%20l'eau%2C%20rentrer%20chez%20soi)%20?%20&url=https://zellwk.com/blog/js-functions/&hashtags=). ?)

_Publié à l'origine sur [zellwk.com](https://zellwk.com/blog/js-functions/).