---
title: Comment créer une application calculatrice HTML à partir de zéro en utilisant
  JavaScript
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-05-03T01:41:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-html-calculator-app-from-scratch-using-javascript-4454b8714b98
coverImage: https://cdn-media-1.freecodecamp.org/images/0*7GfUdSILXBLyAbQy.png
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment créer une application calculatrice HTML à partir de zéro en utilisant
  JavaScript
seo_desc: 'This is an epic article where you learn how to build a calculator from
  scratch. We’ll focus on the JavaScript you need to write—how to think about building
  the calculator, how to write the code, and eventually, how to clean up your code.

  By the end o...'
---

Ceci est un article épique où vous apprenez à créer une calculatrice à partir de zéro. Nous nous concentrerons sur le JavaScript que vous devez écrire—comment penser à la construction de la calculatrice, comment écrire le code, et finalement, comment nettoyer votre code.

À la fin de l'article, vous devriez obtenir une calculatrice qui fonctionne exactement comme une calculatrice iPhone (sans les fonctionnalités `+/-` et de pourcentage).

![Image](https://cdn-media-1.freecodecamp.org/images/Cw7jNVIhWFV4NSNY8-Lv8uX4583Hr5LvzYFq)

### Les prérequis

Avant d'essayer de suivre le cours, assurez-vous d'avoir une bonne maîtrise de JavaScript. Au minimum, vous devez connaître ces éléments :

1. [Les instructions if/else](https://zellwk.com/blog/js-if-else)
2. [Les boucles for](https://zellwk.com/blog/js-for-loops)
3. [Les fonctions JavaScript](https://zellwk.com/blog/js-functions)
4. [Les fonctions fléchées](https://zellwk.com/blog/es6/#arrow-functions)
5. Les opérateurs `&&` et `||`
6. Comment changer le texte avec la propriété `textContent`
7. Comment ajouter des écouteurs d'événements avec le modèle de délégation d'événements

### Avant de commencer

Je vous encourage à essayer de construire la calculatrice vous-même avant de suivre le cours. C'est une bonne pratique, car vous vous entraînerez à penser comme un développeur.

Revenez à ce cours une fois que vous aurez essayé pendant une heure (peu importe que vous réussissiez ou échouiez. Lorsque vous essayez, vous réfléchissez, et cela vous aidera à absorber le cours en un temps record).

Avec cela, commençons par comprendre comment fonctionne une calculatrice.

### Construction de la calculatrice

Tout d'abord, nous voulons construire la calculatrice.

La calculatrice se compose de deux parties : l'affichage et les touches.

![Image](https://cdn-media-1.freecodecamp.org/images/rfV0r9RtFghhau8sZU5CzOFMuJAT1H48tFeL)

```html
<div class="calculator">
  <div class="calculator__display">0</div>
  <div class="calculator__keys"> … </div>
</div>
```

Nous pouvons utiliser CSS Grid pour créer les touches, car elles sont disposées dans un format de grille. Cela a déjà été fait pour vous dans le fichier de démarrage. Vous pouvez trouver le fichier de démarrage à [ce lien](https://codepen.io/zellwk/pen/pLgmGL).

```css
.calculator__keys { 
  display: grid; 
  /* autre CSS nécessaire */ 
}
```

Pour nous aider à identifier les touches opérateur, décimale, effacer et égale, nous allons fournir un attribut data-action qui décrit ce qu'elles font.

```html
<div class="calculator__keys">
  <button class="key--operator" data-action="add">+</button>
  <button class="key--operator" data-action="subtract">-</button>
  <button class="key--operator" data-action="multiply">&times;</button>
  <button class="key--operator" data-action="divide">7</button>
  <button>7</button>
  <button>8</button>
  <button>9</button>
  <button>4</button>
  <button>5</button>
  <button>6</button>
  <button>1</button>
  <button>2</button>
  <button>3</button>
  <button>0</button>
  <button data-action="decimal">.</button>
  <button data-action="clear">AC</button>
  <button class="key--equal" data-action="calculate">=</button>
</div>
```

### Écoute des pressions de touches

Cinq choses peuvent se produire lorsqu'une personne utilise une calculatrice. Elle peut appuyer sur :

1. une touche numérique (0-9)
2. une touche opérateur (+, -, ×, ÷)
3. la touche décimale
4. la touche égale
5. la touche effacer

Les premières étapes pour construire cette calculatrice sont de pouvoir (1) écouter toutes les pressions de touches et (2) déterminer le type de touche qui est pressée. Dans ce cas, nous pouvons utiliser un modèle de délégation d'événements pour écouter, puisque les touches sont toutes des enfants de `.calculator__keys`.

```js
const calculator = document.querySelector('.calculator')
const keys = calculator.querySelector('.calculator__keys')

keys.addEventListener('click', e => {
  if (e.target.matches('button')) {
    // Faire quelque chose
  }
})
```

Ensuite, nous pouvons utiliser l'attribut `data-action` pour déterminer le type de touche qui est cliquée.

```js
const key = e.target
const action = key.dataset.action
```

Si la touche n'a pas d'attribut `data-action`, ce doit être une touche numérique.

```js
if (!action) {
  console.log('touche numérique !')
}
```

Si la touche a une `data-action` qui est soit `add`, `subtract`, `multiply` ou `divide`, nous savons que la touche est un opérateur.

```js
if (
  action === 'add' ||
  action === 'subtract' ||
  action === 'multiply' ||
  action === 'divide'
) {
  console.log('touche opérateur !')
}
```

Si la `data-action` de la touche est `decimal`, nous savons que l'utilisateur a cliqué sur la touche décimale.

En suivant le même processus de pensée, si la `data-action` de la touche est `clear`, nous savons que l'utilisateur a cliqué sur la touche effacer (celle qui dit AC). Si la `data-action` de la touche est `calculate`, nous savons que l'utilisateur a cliqué sur la touche égale.

```js
if (action === 'decimal') {
  console.log('touche décimale !')
}

if (action === 'clear') {
  console.log('touche effacer !')
}

if (action === 'calculate') {
  console.log('touche égale !')
}
```

À ce stade, vous devriez obtenir une réponse `console.log` de chaque touche de la calculatrice.

![Image](https://cdn-media-1.freecodecamp.org/images/lbXTncsu2Ni5V-Ejx6RYCO-kW8XJm7f5woGC)

### Construction du chemin heureux

Considérons ce que la personne moyenne ferait lorsqu'elle prend une calculatrice. **Ce « ce que la personne moyenne ferait » est appelé le chemin heureux.**

Appelons notre personne moyenne Mary.

Lorsque Mary prend une calculatrice, elle pourrait appuyer sur l'une de ces touches :

1. une touche numérique (0-9)
2. une touche opérateur (+, -, ×, ÷)
3. la touche décimale
4. la touche égale
5. la touche effacer

Il peut être accablant de considérer cinq types de touches à la fois, alors prenons cela étape par étape.

### Lorsque l'utilisateur appuie sur une touche numérique

À ce stade, si la calculatrice affiche 0 (le nombre par défaut), le nombre cible doit remplacer zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/mpr4JFLSU-MHaq8LPMedsaDxnU5Y-MTx56SU)

Si la calculatrice affiche un nombre non nul, le nombre cible doit être ajouté au nombre affiché.

![Image](https://cdn-media-1.freecodecamp.org/images/PNfa-nAlgIBtFt1MaVEDvuzisaIps6Kdb482)

Ici, nous devons connaître deux choses :

1. Le nombre de la touche qui a été cliquée
2. Le nombre actuellement affiché

Nous pouvons obtenir ces deux valeurs grâce à la propriété `textContent` de la touche cliquée et `.calculator__display`, respectivement.

```js
const display = document.querySelector('.calculator__display')

keys.addEventListener('click', e => {
  if (e.target.matches('button')) {
    const key = e.target
    const action = key.dataset.action
    const keyContent = key.textContent
    const displayedNum = display.textContent
    // ...
  }
})
```

**Si la calculatrice affiche 0, nous voulons remplacer l'affichage de la calculatrice par la touche cliquée.** Nous pouvons le faire en remplaçant la propriété textContent de l'affichage.

```js
if (!action) {
  if (displayedNum === '0') {
    display.textContent = keyContent
  }
}
```

**Si la calculatrice affiche un nombre non nul, nous voulons ajouter la touche cliquée au nombre affiché.** Pour ajouter un nombre, nous concaténons une chaîne.

```js
if (!action) {
  if (displayedNum === '0') {
    display.textContent = keyContent
  } else {
    display.textContent = displayedNum + keyContent
  }
}
```

À ce stade, Mary peut cliquer sur l'une de ces touches :

1. Une touche décimale
2. Une touche opérateur

Disons que Mary appuie sur la touche décimale.

### Lorsque l'utilisateur appuie sur la touche décimale

Lorsque Mary appuie sur la touche décimale, une décimale doit apparaître sur l'affichage. Si Mary appuie sur un nombre après avoir appuyé sur une touche décimale, le nombre doit être ajouté à l'affichage également.

![Image](https://cdn-media-1.freecodecamp.org/images/5Pc6RLFHdPNzPi3BrlXJSs3xrFf2L90A2WXx)

Pour créer cet effet, nous pouvons concaténer `.` au nombre affiché.

```js
if (action === 'decimal') {
  display.textContent = displayedNum + '.'
}
```

Ensuite, disons que Mary continue son calcul en appuyant sur une touche opérateur.

### Lorsque l'utilisateur appuie sur une touche opérateur

Si Mary appuie sur une touche opérateur, l'opérateur doit être mis en surbrillance pour que Mary sache que l'opérateur est actif.

![Image](https://cdn-media-1.freecodecamp.org/images/VarwRgJGrN0mwcgYGpX1Zw54QRfbXdMmQNEG)

Pour ce faire, nous pouvons ajouter la classe `is-depressed` à la touche opérateur.

```js
if (
  action === 'add' ||
  action === 'subtract' ||
  action === 'multiply' ||
  action === 'divide'
) {
  key.classList.add('is-depressed')
}
```

Une fois que Mary a appuyé sur une touche opérateur, elle appuiera sur une autre touche numérique.

### Lorsque l'utilisateur appuie sur une touche numérique après une touche opérateur

Lorsque Mary appuie à nouveau sur une touche numérique, l'affichage précédent doit être remplacé par le nouveau nombre. La touche opérateur doit également libérer son état pressé.

![Image](https://cdn-media-1.freecodecamp.org/images/GDuLfupPob7rW0UWTH6RqI5CuQX36vcILKwo)

Pour libérer l'état pressé, nous supprimons la classe `is-depressed` de toutes les touches via une boucle `forEach` :

```js
keys.addEventListener('click', e => {
  if (e.target.matches('button')) {
    const key = e.target
    // ...
    
    // Supprimer la classe .is-depressed de toutes les touches
    Array.from(key.parentNode.children)
      .forEach(k => k.classList.remove('is-depressed'))
  }
})
```

Ensuite, nous voulons mettre à jour l'affichage avec la touche cliquée. Avant de le faire, nous avons besoin d'un moyen de savoir si la touche précédente est une touche opérateur.

Une façon de le faire est via un attribut personnalisé. Appelons cet attribut personnalisé `data-previous-key-type`.

```js
const calculator = document.querySelector('.calculator')
// ...

keys.addEventListener('click', e => {
  if (e.target.matches('button')) {
    // ...
    
    if (
      action === 'add' ||
      action === 'subtract' ||
      action === 'multiply' ||
      action === 'divide'
    ) {
      key.classList.add('is-depressed')
      // Ajouter un attribut personnalisé
      calculator.dataset.previousKeyType = 'operator'
    }
  }
})
```

Si le `previousKeyType` est un opérateur, nous voulons remplacer le nombre affiché par le nombre cliqué.

```js
const previousKeyType = calculator.dataset.previousKeyType

if (!action) {
  if (displayedNum === '0' || previousKeyType === 'operator') {
    display.textContent = keyContent
  } else {
    display.textContent = displayedNum + keyContent
  }
}
```

Ensuite, disons que Mary décide de terminer son calcul en appuyant sur la touche égale.

### Lorsque l'utilisateur appuie sur la touche égale

Lorsque Mary appuie sur la touche égale, la calculatrice doit calculer un résultat qui dépend de trois valeurs :

1. Le **premier nombre** entré dans la calculatrice
2. L'**opérateur**
3. Le **deuxième nombre** entré dans la calculatrice

Après le calcul, le résultat doit remplacer la valeur affichée.

![Image](https://cdn-media-1.freecodecamp.org/images/TMFTHXrjCGzKQBIzBFApP7usoJCjcQ-oz2Jc)

À ce stade, nous ne connaissons que le **deuxième nombre** — c'est-à-dire le nombre actuellement affiché.

```js
if (action === 'calculate') {
  const secondValue = displayedNum
  // ...
}
```

Pour obtenir le **premier nombre**, nous devons stocker la valeur affichée de la calculatrice avant de l'effacer. Une façon de sauvegarder ce premier nombre est de l'ajouter à un attribut personnalisé lorsque le bouton opérateur est cliqué.

Pour obtenir l'**opérateur**, nous pouvons également utiliser la même technique.

```js
if (
  action === 'add' ||
  action === 'subtract' ||
  action === 'multiply' ||
  action === 'divide'
) {
  // ...
  calculator.dataset.firstValue = displayedNum
  calculator.dataset.operator = action
}
```

Une fois que nous avons les trois valeurs dont nous avons besoin, nous pouvons effectuer un calcul. Finalement, nous voulons que le code ressemble à quelque chose comme ceci :

```js
if (action === 'calculate') {
  const firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  const secondValue = displayedNum
  
  display.textContent = calculate(firstValue, operator, secondValue)
}
```

Cela signifie que nous devons créer une fonction `calculate`. Elle doit prendre trois paramètres : le premier nombre, l'opérateur et le deuxième nombre.

```js
const calculate = (n1, operator, n2) => {
  // Effectuer le calcul et retourner la valeur calculée
}
```

Si l'opérateur est `add`, nous voulons additionner les valeurs. Si l'opérateur est `subtract`, nous voulons soustraire les valeurs, et ainsi de suite.

```js
const calculate = (n1, operator, n2) => {
  let result = ''
  
  if (operator === 'add') {
    result = n1 + n2
  } else if (operator === 'subtract') {
    result = n1 - n2
  } else if (operator === 'multiply') {
    result = n1 * n2
  } else if (operator === 'divide') {
    result = n1 / n2
  }
  
  return result
}
```

N'oubliez pas que `firstValue` et `secondValue` sont des chaînes à ce stade. Si vous additionnez des chaînes, vous les concaténerez (`1 + 1 = 11`).

Ainsi, avant de calculer le résultat, nous voulons convertir les chaînes en nombres. Nous pouvons le faire avec les deux fonctions `parseInt` et `parseFloat`.

* `parseInt` convertit une chaîne en un **entier**.
* `parseFloat` convertit une chaîne en un **nombre à virgule flottante** (c'est-à-dire un nombre avec des décimales).

Pour une calculatrice, nous avons besoin d'un nombre à virgule flottante.

```js
const calculate = (n1, operator, n2) => {
  let result = ''
  
  if (operator === 'add') {
    result = parseFloat(n1) + parseFloat(n2)
  } else if (operator === 'subtract') {
    result = parseFloat(n1) - parseFloat(n2)
  } else if (operator === 'multiply') {
    result = parseFloat(n1) * parseFloat(n2)
  } else if (operator === 'divide') {
    result = parseFloat(n1) / parseFloat(n2)
  }
  
  return result
}
```

C'est tout pour le chemin heureux !

Vous pouvez obtenir le code source pour le chemin heureux via [ce lien](http://zellwk.com/blog/calculator-part-1) (faites défiler vers le bas et entrez votre adresse e-mail dans la boîte, et je vous enverrai les codes sources directement dans votre boîte mail).

### Les cas limites

Le chemin heureux n'est pas suffisant. Pour construire une calculatrice robuste, vous devez rendre votre calculatrice résistante aux modèles d'entrée étranges. Pour ce faire, vous devez imaginer un faiseur de troubles qui essaie de casser votre calculatrice en appuyant sur les touches dans le mauvais ordre. Appelons ce faiseur de troubles Tim.

Tim peut appuyer sur ces touches dans n'importe quel ordre :

1. Une touche numérique (0-9)
2. Une touche opérateur (+, -, ×, ÷)
3. La touche décimale
4. La touche égale
5. La touche effacer

### Que se passe-t-il si Tim appuie sur la touche décimale

Si Tim appuie sur une touche décimale alors que l'affichage montre déjà un point décimal, rien ne devrait se passer.

![Image](https://cdn-media-1.freecodecamp.org/images/Lbvc-ZcYHO2iWjXIjdYiOVJcmPTmtwkknBw5)

![Image](https://cdn-media-1.freecodecamp.org/images/Orj4wS6vgnPAMYFq1xI3DEYXBMS4PWLlSw8a)

Ici, nous pouvons vérifier que le nombre affiché contient un `.` avec la méthode `includes`.

`includes` vérifie les chaînes pour une correspondance donnée. Si une chaîne est trouvée, elle retourne `true` ; sinon, elle retourne `false`.

**Note** : `includes` est sensible à la casse.

```js
// Exemple de fonctionnement de includes.
const string = 'The hamburgers taste pretty good!'
const hasExclaimation = string.includes('!')
console.log(hasExclaimation) // true
```

Pour vérifier si la chaîne contient déjà un point, nous faisons ceci :

```js
// Ne rien faire si la chaîne contient un point
if (!displayedNum.includes('.')) {
  display.textContent = displayedNum + '.'
}
```

Ensuite, si Tim appuie sur la touche décimale après avoir appuyé sur une touche opérateur, l'affichage doit montrer `0.`.

![Image](https://cdn-media-1.freecodecamp.org/images/fLLhOqkyFZqsOZIxgMPAkpezrUisGpDKFEsw)

Ici, nous devons savoir si la touche précédente est un opérateur. Nous pouvons le savoir en vérifiant l'attribut personnalisé, `data-previous-key-type`, que nous avons défini dans la leçon précédente.

`data-previous-key-type` n'est pas encore complet. Pour identifier correctement si `previousKeyType` est un opérateur, nous devons mettre à jour `previousKeyType` pour chaque touche cliquée.

```js
if (!action) {
  // ...
  calculator.dataset.previousKey = 'number'
}

if (action === 'decimal') {
  // ...
  calculator.dataset.previousKey = 'decimal'
}

if (action === 'clear') {
  // ...
  calculator.dataset.previousKeyType = 'clear'
}

if (action === 'calculate') {
 // ...
  calculator.dataset.previousKeyType = 'calculate'
}
```

Une fois que nous avons le `previousKeyType` correct, nous pouvons l'utiliser pour vérifier si la touche précédente est un opérateur.

```js
if (action === 'decimal') {
  if (!displayedNum.includes('.')) {
    display.textContent = displayedNum + '.'
  } else if (previousKeyType === 'operator') {
    display.textContent = '0.'
  }
  
calculator.dataset.previousKeyType = 'decimal'
}
```

### Que se passe-t-il si Tim appuie sur une touche opérateur

Si Tim appuie d'abord sur une touche opérateur, la touche opérateur doit s'allumer. (Nous avons déjà couvert ce cas limite, mais comment ? Voyez si vous pouvez identifier ce que nous avons fait).

![Image](https://cdn-media-1.freecodecamp.org/images/q3D72rgBjtPOPUltYm1MMIN06dvxGOKyJyUs)

Deuxièmement, rien ne devrait se passer si Tim appuie plusieurs fois sur la même touche opérateur. (Nous avons également déjà couvert ce cas limite).

**Note** : si vous souhaitez offrir une meilleure expérience utilisateur, vous pouvez montrer que l'opérateur est cliqué à plusieurs reprises avec quelques modifications CSS. Nous ne l'avons pas fait ici, mais voyez si vous pouvez programmer cela vous-même comme un défi de codage supplémentaire.

![Image](https://cdn-media-1.freecodecamp.org/images/IXW7zY77RWE7tNQ6HZMYma73hsxW44EjWg0n)

Troisièmement, si Tim appuie sur une autre touche opérateur après avoir appuyé sur la première touche opérateur, la première touche opérateur doit être relâchée. Ensuite, la deuxième touche opérateur doit être enfoncée. (Nous avons également couvert ce cas limite — mais comment ?).

![Image](https://cdn-media-1.freecodecamp.org/images/Rez20RY9AcS6ORFWIIumk69YWzwTyv8qseM7)

Quatrièmement, si Tim appuie sur un nombre, un opérateur, un nombre et un autre opérateur, dans cet ordre, l'affichage doit être mis à jour avec une valeur calculée.

![Image](https://cdn-media-1.freecodecamp.org/images/MAMWFTkNu6Ho8tlMGyJlTfjCbeYq8rO0bQyR)

Cela signifie que nous devons utiliser la fonction `calculate` lorsque `firstValue`, `operator` et `secondValue` existent.

```js
if (
  action === 'add' ||
  action === 'subtract' ||
  action === 'multiply' ||
  action === 'divide'
) {
  const firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  const secondValue = displayedNum
  
// Note: Il suffit de vérifier firstValue et operator car secondValue existe toujours
  if (firstValue && operator) {
    display.textContent = calculate(firstValue, operator, secondValue)
  }
  
key.classList.add('is-depressed')
  calculator.dataset.previousKeyType = 'operator'
  calculator.dataset.firstValue = displayedNum
  calculator.dataset.operator = action
}
```

Bien que nous puissions calculer une valeur lorsque la touche opérateur est cliquée une deuxième fois, nous avons également introduit un bug à ce stade — des clics supplémentaires sur la touche opérateur calculent une valeur alors qu'ils ne devraient pas.

![Image](https://cdn-media-1.freecodecamp.org/images/8ktjtHeYaRTEn-lPbOM3fhEg3qrvDl5WfOVY)

Pour empêcher la calculatrice d'effectuer un calcul lors des clics ultérieurs sur la touche opérateur, nous devons vérifier si le `previousKeyType` est un opérateur. Si c'est le cas, nous n'effectuons pas de calcul.

```js
if (
  firstValue &&
  operator &&
  previousKeyType !== 'operator'
) {
  display.textContent = calculate(firstValue, operator, secondValue)
}
```

Cinquième, après que la touche opérateur a calculé un nombre, si Tim appuie sur un nombre, suivi d'un autre opérateur, l'opérateur doit continuer le calcul, comme ceci : `8 - 1 = 7`, `7 - 2 = 5`, `5 - 3 = 2`.

![Image](https://cdn-media-1.freecodecamp.org/images/RSsXyuKJe0biqkH-WPDdrGLhFBWmyZ2R1J2Y)

Actuellement, notre calculatrice ne peut pas effectuer de calculs consécutifs. La deuxième valeur calculée est incorrecte. Voici ce que nous avons : `99 - 1 = 98`, `98 - 1 = 0`.

![Image](https://cdn-media-1.freecodecamp.org/images/0r9I8Gu7J9pMbfzUG4hL6tU7RCP-cDhsaGp1)

La deuxième valeur est calculée incorrectement, car nous avons alimenté la fonction `calculate` avec de mauvaises valeurs. Passons en revue quelques images pour comprendre ce que fait notre code.

### Comprendre notre fonction calculate

Tout d'abord, disons qu'un utilisateur clique sur un nombre, 99. À ce stade, rien n'est enregistré dans la calculatrice.

![Image](https://cdn-media-1.freecodecamp.org/images/0hH4Cz5kOEaDOcTQ2PMPmkDl26a8JHSXNrJ7)

Deuxièmement, disons que l'utilisateur clique sur l'opérateur de soustraction. Après avoir cliqué sur l'opérateur de soustraction, nous définissons `firstValue` à 99. Nous définissons également `operator` à subtract.

![Image](https://cdn-media-1.freecodecamp.org/images/0K-KPTzdCBgfVvVaDNcVDYSjXfUO8p5LRs2v)

Troisièmement, disons que l'utilisateur clique sur une deuxième valeur — cette fois, c'est 1. À ce stade, le nombre affiché est mis à jour à 1, mais notre `firstValue`, `operator` et `secondValue` restent inchangés.

![Image](https://cdn-media-1.freecodecamp.org/images/0MacG-A5Tl7rZeB6NLeNvghVyBpmSqaZQkn9)

Quatrièmement, l'utilisateur clique à nouveau sur subtract. Juste après avoir cliqué sur subtract, avant de calculer le résultat, nous définissons `secondValue` comme le nombre affiché.

![Image](https://cdn-media-1.freecodecamp.org/images/RgDMKK92og4djxxmaYO1HUYiVoetKDK9x0j7)

Cinquième, nous effectuons le calcul avec `firstValue` 99, `operator` subtract, et `secondValue` 1. Le résultat est 98.

Une fois le résultat calculé, nous définissons l'affichage au résultat. Ensuite, nous définissons `operator` à subtract, et `firstValue` au nombre affiché précédent.

![Image](https://cdn-media-1.freecodecamp.org/images/X3VFJ5ar--k84pP3pM5VDVODvYlX4fCwHcnS)

Eh bien, c'est terriblement faux ! Si nous voulons continuer le calcul, nous devons mettre à jour `firstValue` avec la valeur calculée.

![Image](https://cdn-media-1.freecodecamp.org/images/gp-lkqhUOjoo46fIwx-7oLtbV7CP7jZwzc9y)

```js
const firstValue = calculator.dataset.firstValue
const operator = calculator.dataset.operator
const secondValue = displayedNum

if (
  firstValue &&
  operator &&
  previousKeyType !== 'operator'
) {
  const calcValue = calculate(firstValue, operator, secondValue)
  display.textContent = calcValue
  
// Mettre à jour la valeur calculée comme firstValue
  calculator.dataset.firstValue = calcValue
} else {
  // Si aucun calcul n'est effectué, définir displayedNum comme firstValue
  calculator.dataset.firstValue = displayedNum
}

key.classList.add('is-depressed')
calculator.dataset.previousKeyType = 'operator'
calculator.dataset.operator = action
```

Avec cette correction, les calculs consécutifs effectués par les touches opérateur doivent maintenant être corrects.

![Image](https://cdn-media-1.freecodecamp.org/images/tKZ-VlIHo7dRNHDR2BBxZChE1cgqIuMU0Uh-)

### Que se passe-t-il si Tim appuie sur la touche égale ?

Tout d'abord, rien ne devrait se passer si Tim appuie sur la touche égale avant toute touche opérateur.

![Image](https://cdn-media-1.freecodecamp.org/images/FBvnFZadNPXTllID0R7JfAkrsDb5SLcWTUhV)

![Image](https://cdn-media-1.freecodecamp.org/images/fKJV0ZqgVf-ppPqrx-70FpByKioVL2T9oAsF)

Nous savons que les touches opérateur n'ont pas encore été cliquées si `firstValue` n'est pas défini à un nombre. Nous pouvons utiliser cette connaissance pour empêcher l'égalité de calculer.

```js
if (action === 'calculate') {
  const firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  const secondValue = displayedNum
  
if (firstValue) {
    display.textContent = calculate(firstValue, operator, secondValue)
  }
  
calculator.dataset.previousKeyType = 'calculate'
}
```

Deuxièmement, si Tim appuie sur un nombre, suivi d'un opérateur, suivi d'une égalité, la calculatrice doit calculer le résultat de telle sorte que :

1. `2 + =` → `2 + 2 = 4`
2. `2 - =` → `2 - 2 = 0`
3. `2 × =` → `2 × 2 = 4`
4. `2 ÷ =` → `2 ÷ 2 = 1`

![Image](https://cdn-media-1.freecodecamp.org/images/MUgIi0ck8OJRV18hfJ-kdn8k7Ydyy5mDvV6z)

Nous avons déjà pris en compte cette entrée étrange. Pouvez-vous comprendre pourquoi ? :)

Troisièmement, si Tim appuie sur la touche égale après qu'un calcul est terminé, un autre calcul doit être effectué à nouveau. Voici comment le calcul doit se lire :

1. Tim appuie sur les touches 5-1
2. Tim appuie sur égal. La valeur calculée est `5 - 1 = 4`
3. Tim appuie sur égal. La valeur calculée est `4 - 1 = 3`
4. Tim appuie sur égal. La valeur calculée est `3 - 1 = 2`
5. Tim appuie sur égal. La valeur calculée est `2 - 1 = 1`
6. Tim appuie sur égal. La valeur calculée est `1 - 1 = 0`

![Image](https://cdn-media-1.freecodecamp.org/images/vB2oVoTXZsMABqV60qqclJhoOxYu2JeVhLx4)

Malheureusement, notre calculatrice se trompe dans ce calcul. Voici ce que montre notre calculatrice :

1. Tim appuie sur la touche 5-1
2. Tim appuie sur égal. La valeur calculée est `4`
3. Tim appuie sur égal. La valeur calculée est `1`

![Image](https://cdn-media-1.freecodecamp.org/images/8roqRbhSH3hLVvtK7t-T2iRsRegqPWSrn4SF)

### Correction du calcul

Tout d'abord, disons que notre utilisateur clique sur 5. À ce stade, rien n'est enregistré dans la calculatrice.

![Image](https://cdn-media-1.freecodecamp.org/images/2vf5VGXNZ0vjGkyaY0y22PRTqqHDwgEKvCC3)

Deuxièmement, disons que l'utilisateur clique sur l'opérateur de soustraction. Après avoir cliqué sur l'opérateur de soustraction, nous définissons `firstValue` à 5. Nous définissons également `operator` à subtract.

![Image](https://cdn-media-1.freecodecamp.org/images/Fc-QupYbv3HInXqv1vHFCc1avhDe3iyEErhs)

Troisièmement, l'utilisateur clique sur une deuxième valeur. Disons que c'est 1. À ce stade, le nombre affiché est mis à jour à 1, mais notre `firstValue`, `operator` et `secondValue` restent inchangés.

![Image](https://cdn-media-1.freecodecamp.org/images/lW3CtoXJ1gxpUS5SZM3zh3zmqSB-ksM6E0vr)

Quatrièmement, l'utilisateur clique sur la touche égale. Juste après avoir cliqué sur égal, mais avant le calcul, nous définissons `secondValue` comme `displayedNum`

![Image](https://cdn-media-1.freecodecamp.org/images/yeQCYcu0ecbNbJlHa9aqEZopHj-FyTqXuRmw)

Cinquième, la calculatrice calcule le résultat de `5 - 1` et donne `4`. Le résultat est mis à jour sur l'affichage. `firstValue` et `operator` sont reportés au calcul suivant puisque nous ne les avons pas mis à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/YOsfq7AWCs0YbABkiebax-oaQVGc5tWsNyXJ)

Sixième, lorsque l'utilisateur appuie à nouveau sur égal, nous définissons `secondValue` à `displayedNum` avant le calcul.

![Image](https://cdn-media-1.freecodecamp.org/images/BF7tBEUHJN4gnIwQqUTq9ctHIUIVcYM026Ro)

Vous pouvez voir ce qui ne va pas ici.

Au lieu de `secondValue`, nous voulons définir `firstValue` au nombre affiché.

```js
if (action === 'calculate') {
  let firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  const secondValue = displayedNum
  
if (firstValue) {
    if (previousKeyType === 'calculate') {
      firstValue = displayedNum
    }
    
display.textContent = calculate(firstValue, operator, secondValue)
  }
  
calculator.dataset.previousKeyType = 'calculate'
}
```

Nous voulons également reporter le `secondValue` précédent dans le nouveau calcul. Pour que `secondValue` persiste dans le calcul suivant, nous devons le stocker dans un autre attribut personnalisé. Appelons cet attribut personnalisé `modValue` (pour valeur modificatrice).

```js
if (action === 'calculate') {
  let firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  const secondValue = displayedNum
  
if (firstValue) {
    if (previousKeyType === 'calculate') {
      firstValue = displayedNum
    }
    
display.textContent = calculate(firstValue, operator, secondValue)
  }
  
// Définir l'attribut modValue
  calculator.dataset.modValue = secondValue
  calculator.dataset.previousKeyType = 'calculate'
}
```

Si le `previousKeyType` est `calculate`, nous savons que nous pouvons utiliser `calculator.dataset.modValue` comme `secondValue`. Une fois que nous savons cela, nous pouvons effectuer le calcul.

```js
if (firstValue) {
  if (previousKeyType === 'calculate') {
    firstValue = displayedNum
    secondValue = calculator.dataset.modValue
  }
  
display.textContent = calculate(firstValue, operator, secondValue)
}
```

Avec cela, nous avons le calcul correct lorsque la touche égale est cliquée consécutivement.

![Image](https://cdn-media-1.freecodecamp.org/images/sjYX-ImohfhbFFbw1-FqmKagBvfFQKm0PzAu)

### Retour à la touche égale

Quatrièmement, si Tim appuie sur une touche décimale ou une touche numérique après la touche calculatrice, l'affichage doit être remplacé par `0.` ou le nouveau nombre respectivement.

Ici, au lieu de simplement vérifier si le `previousKeyType` est `operator`, nous devons également vérifier s'il est `calculate`.

```js
if (!action) {
  if (
    displayedNum === '0' ||
    previousKeyType === 'operator' ||
    previousKeyType === 'calculate'
  ) {
    display.textContent = keyContent
  } else {
    display.textContent = displayedNum + keyContent
  }
  calculator.dataset.previousKeyType = 'number'
}

if (action === 'decimal') {
  if (!displayedNum.includes('.')) {
    display.textContent = displayedNum + '.'
  } else if (
    previousKeyType === 'operator' ||
    previousKeyType === 'calculate'
  ) {
    display.textContent = '0.'
  }
  
calculator.dataset.previousKeyType = 'decimal'
}
```

Cinquième, si Tim appuie sur une touche opérateur juste après la touche égale, la calculatrice ne doit **pas** calculer.

![Image](https://cdn-media-1.freecodecamp.org/images/uuifuJ41Oo86NXMsPj44RSQf7ExULROc2GaI)

Pour ce faire, nous vérifions si le `previousKeyType` est `calculate` avant d'effectuer des calculs avec les touches opérateur.

```js
if (
  action === 'add' ||
  action === 'subtract' ||
  action === 'multiply' ||
  action === 'divide'
) {
  // ...
  
if (
    firstValue &&
    operator &&
    previousKeyType !== 'operator' &&
    previousKeyType !== 'calculate'
  ) {
    const calcValue = calculate(firstValue, operator, secondValue)
    display.textContent = calcValue
    calculator.dataset.firstValue = calcValue
  } else {
    calculator.dataset.firstValue = displayedNum
  }
  
// ...
}
```

La touche effacer a deux utilisations :

1. Tout effacer (dénoté par `AC`) efface tout et réinitialise la calculatrice à son état initial.
2. Effacer l'entrée (dénoté par `CE`) efface l'entrée actuelle. Elle conserve les nombres précédents en mémoire.

Lorsque la calculatrice est dans son état par défaut, `AC` doit être affiché.

![Image](https://cdn-media-1.freecodecamp.org/images/22fj2VLJJ1SPexybqdWIqPRkj9JkrlI3AAYl)

Tout d'abord, si Tim appuie sur une touche (n'importe quelle touche sauf effacer), `AC` doit être changé en `CE`.

![Image](https://cdn-media-1.freecodecamp.org/images/Hs9tjp3JQIYOaAgh8KDnxj5QShScU0nMkDa7)

Nous faisons cela en vérifiant si la `data-action` est `clear`. Si ce n'est pas `clear`, nous cherchons le bouton effacer et changeons son `textContent`.

```js
if (action !== 'clear') {
  const clearButton = calculator.querySelector('[data-action=clear]')
  clearButton.textContent = 'CE'
}
```

Deuxièmement, si Tim appuie sur `CE`, l'affichage doit lire 0. En même temps, `CE` doit être réinitialisé à `AC` pour que Tim puisse réinitialiser la calculatrice à son état initial.

![Image](https://cdn-media-1.freecodecamp.org/images/Dv6SFw5LY8wB0WqTFQBe46-QoraBiq8TvpdY)

```js
if (action === 'clear') {
  display.textContent = 0
  key.textContent = 'AC'
  calculator.dataset.previousKeyType = 'clear'
}
```

Troisièmement, si Tim appuie sur `AC`, réinitialisez la calculatrice à son état initial.

Pour réinitialiser la calculatrice à son état initial, nous devons effacer tous les attributs personnalisés que nous avons définis.

```js
if (action === 'clear') {
  if (key.textContent === 'AC') {
    calculator.dataset.firstValue = ''
    calculator.dataset.modValue = ''
    calculator.dataset.operator = ''
    calculator.dataset.previousKeyType = ''
  } else {
    key.textContent = 'AC'
  }
  
display.textContent = 0
  calculator.dataset.previousKeyType = 'clear'
}
```

C'est tout — pour la partie des cas limites, en tout cas !

Vous pouvez obtenir le code source pour la partie des cas limites via [ce lien](http://zellwk.com/blog/calculator-part-2) (faites défiler vers le bas et entrez votre adresse e-mail dans la boîte, et je vous enverrai les codes sources directement dans votre boîte mail).

À ce stade, le code que nous avons créé ensemble est assez confus. Vous vous perdrez probablement si vous essayez de lire le code par vous-même. Refactorisons-le pour le rendre plus propre.

### Refactorisation du code

Lorsque vous refactorisez, vous commencez souvent par les améliorations les plus évidentes. Dans ce cas, commençons par `calculate`.

Avant de continuer, assurez-vous de connaître ces pratiques/fonctionnalités JavaScript. Nous les utiliserons dans la refactorisation.

1. [Retours précoces](http://blog.timoxley.com/post/47041269194/avoid-else-return-early)
2. [Opérateurs ternaires](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)
3. [Fonctions pures](https://medium.com/@jamesjefferyuk/javascript-what-are-pure-functions-4d4d5392d49c)
4. [Destructuration ES6](https://zellwk.com/blog/es6#destructuring)

Avec cela, commençons !

### Refactorisation de la fonction calculate

Voici ce que nous avons jusqu'à présent.

```js
const calculate = (n1, operator, n2) => {
  let result = ''
  if (operator === 'add') {
    result = parseFloat(n1) + parseFloat(n2)
  } else if (operator === 'subtract') {
    result = parseFloat(n1) - parseFloat(n2)
  } else if (operator === 'multiply') {
    result = parseFloat(n1) * parseFloat(n2)
  } else if (operator === 'divide') {
    result = parseFloat(n1) / parseFloat(n2)
  }
  
  return result
}
```

Vous avez appris que nous devrions réduire les réaffectations autant que possible. Ici, nous pouvons supprimer les affectations si nous retournons le résultat du calcul dans les instructions `if` et `else if` :

```js
const calculate = (n1, operator, n2) => {
  if (operator === 'add') {
    return firstNum + parseFloat(n2)
  } else if (operator === 'subtract') {
    return parseFloat(n1) - parseFloat(n2)
  } else if (operator === 'multiply') {
    return parseFloat(n1) * parseFloat(n2)
  } else if (operator === 'divide') {
    return parseFloat(n1) / parseFloat(n2)
  }
}
```

Puisque nous retournons toutes les valeurs, nous pouvons utiliser des **retours précoces**. Si nous le faisons, il n'y a pas besoin de conditions `else if`.

```js
const calculate = (n1, operator, n2) => {
  if (operator === 'add') {
    return firstNum + parseFloat(n2)
  }
  
  if (operator === 'subtract') {
    return parseFloat(n1) - parseFloat(n2)
  }
  
  if (operator === 'multiply') {
    return parseFloat(n1) * parseFloat(n2)
  }
  
  if (operator === 'divide') {
    return parseFloat(n1) / parseFloat(n2)
  }
}
```

Et puisque nous avons une instruction par condition `if`, nous pouvons supprimer les accolades. (Note : certains développeurs jurent par les accolades, cependant). Voici à quoi ressemblerait le code :

```js
const calculate = (n1, operator, n2) => {
  if (operator === 'add') return parseFloat(n1) + parseFloat(n2)
  if (operator === 'subtract') return parseFloat(n1) - parseFloat(n2)
  if (operator === 'multiply') return parseFloat(n1) * parseFloat(n2)
  if (operator === 'divide') return parseFloat(n1) / parseFloat(n2)
}
```

Enfin, nous avons appelé `parseFloat` huit fois dans la fonction. Nous pouvons la simplifier en créant deux variables pour contenir les valeurs flottantes :

```js
const calculate = (n1, operator, n2) => {
  const firstNum = parseFloat(n1)
  const secondNum = parseFloat(n2)
  if (operator === 'add') return firstNum + secondNum
  if (operator === 'subtract') return firstNum - secondNum
  if (operator === 'multiply') return firstNum * secondNum
  if (operator === 'divide') return firstNum / secondNum
}
```

Nous avons terminé avec `calculate`. Ne pensez-vous pas que c'est plus facile à lire par rapport à avant ?

### Refactorisation de l'écouteur d'événements

Le code que nous avons créé pour l'écouteur d'événements est énorme. Voici ce que nous avons pour le moment :

```js
keys.addEventListener('click', e => {
  if (e.target.matches('button')) {
  
    if (!action) { /* ... */ }
    
    if (action === 'add' ||
      action === 'subtract' ||
      action === 'multiply' ||
      action === 'divide') {
      /* ... */
    }
    
    if (action === 'clear') { /* ... */ }
    if (action !== 'clear') { /* ... */ }
    if (action === 'calculate') { /* ... */ }
  }
})
```

Comment commencez-vous à refactoriser ce morceau de code ? Si vous ne connaissez pas les meilleures pratiques de programmation, vous pourriez être tenté de refactoriser en divisant chaque type d'action en une fonction plus petite :

```js
// Ne faites pas cela !
const handleNumberKeys = (/* ... */) => {/* ... */}
const handleOperatorKeys = (/* ... */) => {/* ... */}
const handleDecimalKey = (/* ... */) => {/* ... */}
const handleClearKey = (/* ... */) => {/* ... */}
const handleCalculateKey = (/* ... */) => {/* ... */}
```

Ne faites pas cela. Cela n'aide pas, car vous divisez simplement des blocs de code. Lorsque vous le faites, la fonction devient plus difficile à lire.

Une meilleure façon est de diviser le code en fonctions pures et impures. Si vous le faites, vous obtiendrez un code qui ressemble à ceci :

```js
keys.addEventListener('click', e => {
  // Fonction pure
  const resultString = createResultString(/* ... */)
  
  // Choses impures
  display.textContent = resultString
  updateCalculatorState(/* ... */)
})
```

Ici, `createResultString` est une fonction pure qui retourne ce qui doit être affiché sur la calculatrice. `updateCalculatorState` est une fonction impure qui change l'apparence visuelle de la calculatrice et ses attributs personnalisés.

### Création de createResultString

Comme mentionné précédemment, `createResultString` doit retourner la valeur qui doit être affichée sur la calculatrice. Vous pouvez obtenir ces valeurs grâce aux parties du code qui disent `display.textContent = 'some value'`.

```js
display.textContent = 'some value'
```

Au lieu de `display.textContent = 'some value'`, nous voulons retourner chaque valeur afin de pouvoir l'utiliser plus tard.

```js
// remplacer ce qui précède par ceci
return 'some value'
```

Faisons cela ensemble, étape par étape, en commençant par les touches numériques.

### Création de la chaîne de résultat pour les touches numériques

Voici le code que nous avons pour les touches numériques :

```js
if (!action) {
  if (
    displayedNum === '0' ||
    previousKeyType === 'operator' ||
    previousKeyType === 'calculate'
  ) {
    display.textContent = keyContent
  } else {
    display.textContent = displayedNum + keyContent
  }
  calculator.dataset.previousKeyType = 'number'
}
```

La première étape consiste à copier les parties qui disent `display.textContent = 'some value'` dans `createResultString`. Lorsque vous faites cela, assurez-vous de changer `display.textContent =` en `return`.

```js
const createResultString = () => {
  if (!action) {
    if (
      displayedNum === '0' ||
      previousKeyType === 'operator' ||
      previousKeyType === 'calculate'
    ) {
      return keyContent
    } else {
      return displayedNum + keyContent
    }
  }
}
```

Ensuite, nous pouvons convertir l'instruction `if/else` en un opérateur ternaire :

```js
const createResultString = () => {
  if (action!) {
    return displayedNum === '0' ||
      previousKeyType === 'operator' ||
      previousKeyType === 'calculate'
      ? keyContent
      : displayedNum + keyContent
  }
}
```

Lorsque vous refactorisez, n'oubliez pas de noter une liste des variables dont vous avez besoin. Nous reviendrons à cette liste plus tard.

```js
const createResultString = () => {
  // Variables requises sont :
  // 1. keyContent
  // 2. displayedNum
  // 3. previousKeyType
  // 4. action
  
  if (action!) {
    return displayedNum === '0' ||
      previousKeyType === 'operator' ||
      previousKeyType === 'calculate'
      ? keyContent
      : displayedNum + keyContent
  }
}
```

### Création de la chaîne de résultat pour la touche décimale

Voici le code que nous avons pour la touche décimale :

```js
if (action === 'decimal') {
  if (!displayedNum.includes('.')) {
    display.textContent = displayedNum + '.'
  } else if (
    previousKeyType === 'operator' ||
    previousKeyType === 'calculate'
  ) {
    display.textContent = '0.'
  }
  
  calculator.dataset.previousKeyType = 'decimal'
}
```

Comme précédemment, nous voulons déplacer tout ce qui change `display.textContent` dans `createResultString`.

```js
const createResultString = () => {
  // ...
  
  if (action === 'decimal') {
    if (!displayedNum.includes('.')) {
      return = displayedNum + '.'
    } else if (previousKeyType === 'operator' || previousKeyType === 'calculate') {
      return = '0.'
    }
  }
}
```

Puisque nous voulons retourner toutes les valeurs, nous pouvons convertir les instructions `else if` en retours précoces.

```js
const createResultString = () => {
  // ...
  
  if (action === 'decimal') {
    if (!displayedNum.includes('.')) return displayedNum + '.'
    if (previousKeyType === 'operator' || previousKeyType === 'calculate') return '0.'
  }
}
```

Une erreur courante ici est d'oublier de retourner le nombre actuellement affiché lorsque aucune condition n'est remplie. Nous en avons besoin car nous allons remplacer `display.textContent` par la valeur retournée par `createResultString`. Si nous l'oublions, `createResultString` retournera `undefined`, ce qui n'est pas ce que nous voulons.

```js
const createResultString = () => {
  // ...
  
  if (action === 'decimal') {
    if (!displayedNum.includes('.')) return displayedNum + '.'
    if (previousKeyType === 'operator' || previousKeyType === 'calculate') return '0.'
    return displayedNum
  }
}
```

Comme toujours, notez les variables nécessaires. À ce stade, les variables nécessaires restent les mêmes qu'avant :

```js
const createResultString = () => {
  // Variables requises sont :
  // 1. keyContent
  // 2. displayedNum
  // 3. previousKeyType
  // 4. action
}
```

### Création de la chaîne de résultat pour les touches opérateur

Voici le code que nous avons écrit pour les touches opérateur.

```js
if (
  action === 'add' ||
  action === 'subtract' ||
  action === 'multiply' ||
  action === 'divide'
) {
  const firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  const secondValue = displayedNum
  
  if (
    firstValue &&
    operator &&
    previousKeyType !== 'operator' &&
    previousKeyType !== 'calculate'
  ) {
    const calcValue = calculate(firstValue, operator, secondValue)
    display.textContent = calcValue
    calculator.dataset.firstValue = calcValue
  } else {
    calculator.dataset.firstValue = displayedNum
  }
  
  key.classList.add('is-depressed')
  calculator.dataset.previousKeyType = 'operator'
  calculator.dataset.operator = action
}
```

Vous connaissez la routine maintenant : nous voulons déplacer tout ce qui change `display.textContent` dans `createResultString`. Voici ce qui doit être déplacé :

```js
const createResultString = () => {
  // ...
  if (
    action === 'add' ||
    action === 'subtract' ||
    action === 'multiply' ||
    action === 'divide'
  ) {
    const firstValue = calculator.dataset.firstValue
    const operator = calculator.dataset.operator
    const secondValue = displayedNum
    
    if (
      firstValue &&
      operator &&
      previousKeyType !== 'operator' &&
      previousKeyType !== 'calculate'
    ) {
      return calculate(firstValue, operator, secondValue)
    }
  }
}
```

N'oubliez pas que `createResultString` doit retourner la valeur à afficher sur la calculatrice. Si la condition `if` n'est pas remplie, nous voulons toujours retourner le nombre affiché.

```js
const createResultString = () => {
  // ...
  if (
    action === 'add' ||
    action === 'subtract' ||
    action === 'multiply' ||
    action === 'divide'
  ) {
    const firstValue = calculator.dataset.firstValue
    const operator = calculator.dataset.operator
    const secondValue = displayedNum
    
    if (
      firstValue &&
      operator &&
      previousKeyType !== 'operator' &&
      previousKeyType !== 'calculate'
    ) {
      return calculate(firstValue, operator, secondValue)
    } else {
      return displayedNum
    }
  }
}
```

Nous pouvons ensuite refactoriser l'instruction `if/else` en un opérateur ternaire :

```js
const createResultString = () => {
  // ...
  if (
    action === 'add' ||
    action === 'subtract' ||
    action === 'multiply' ||
    action === 'divide'
  ) {
    const firstValue = calculator.dataset.firstValue
    const operator = calculator.dataset.operator
    const secondValue = displayedNum
    
    return firstValue &&
      operator &&
      previousKeyType !== 'operator' &&
      previousKeyType !== 'calculate'
      ? calculate(firstValue, operator, secondValue)
      : displayedNum
  }
}
```

Si vous regardez de près, vous réaliserez qu'il n'est pas nécessaire de stocker une variable `secondValue`. Nous pouvons utiliser `displayedNum` directement dans la fonction `calculate`.

```js
const createResultString = () => {
  // ...
  if (
    action === 'add' ||
    action === 'subtract' ||
    action === 'multiply' ||
    action === 'divide'
  ) {
    const firstValue = calculator.dataset.firstValue
    const operator = calculator.dataset.operator
    
    return firstValue &&
      operator &&
      previousKeyType !== 'operator' &&
      previousKeyType !== 'calculate'
      ? calculate(firstValue, operator, displayedNum)
      : displayedNum
  }
}
```

Enfin, notez les variables et propriétés nécessaires. Cette fois, nous avons besoin de `calculator.dataset.firstValue` et `calculator.dataset.operator`.

```js
const createResultString = () => {
  // Variables & propriétés requises sont :
  // 1. keyContent
  // 2. displayedNum
  // 3. previousKeyType
  // 4. action
  // 5. calculator.dataset.firstValue
  // 6. calculator.dataset.operator
}
```

### Création de la chaîne de résultat pour la touche effacer

Nous avons écrit le code suivant pour gérer la touche `clear`.

```js
if (action === 'clear') {
  if (key.textContent === 'AC') {
    calculator.dataset.firstValue = ''
    calculator.dataset.modValue = ''
    calculator.dataset.operator = ''
    calculator.dataset.previousKeyType = ''
  } else {
    key.textContent = 'AC'
  }
  
  display.textContent = 0
  calculator.dataset.previousKeyType = 'clear'
}
```

Comme ci-dessus, nous voulons déplacer tout ce qui change `display.textContent` dans `createResultString`.

```js
const createResultString = () => {
  // ...
  if (action === 'clear') return 0
}
```

### Création de la chaîne de résultat pour la touche égale

Voici le code que nous avons écrit pour la touche égale :

```js
if (action === 'calculate') {
  let firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  let secondValue = displayedNum
  
  if (firstValue) {
    if (previousKeyType === 'calculate') {
      firstValue = displayedNum
      secondValue = calculator.dataset.modValue
    }
    
    display.textContent = calculate(firstValue, operator, secondValue)
  }
  
  calculator.dataset.modValue = secondValue
  calculator.dataset.previousKeyType = 'calculate'
}
```

Comme ci-dessus, nous voulons copier tout ce qui change `display.textContent` dans `createResultString`. Voici ce qui doit être copié :

```js
if (action === 'calculate') {
  let firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  let secondValue = displayedNum
  
  if (firstValue) {
    if (previousKeyType === 'calculate') {
      firstValue = displayedNum
      secondValue = calculator.dataset.modValue
    }
    display.textContent = calculate(firstValue, operator, secondValue)
  }
}
```

Lorsque vous copiez le code dans `createResultString`, assurez-vous de retourner des valeurs pour chaque scénario possible :

```js
const createResultString = () => {
  // ...
  
  if (action === 'calculate') {
    let firstValue = calculator.dataset.firstValue
    const operator = calculator.dataset.operator
    let secondValue = displayedNum
    
    if (firstValue) {
      if (previousKeyType === 'calculate') {
        firstValue = displayedNum
        secondValue = calculator.dataset.modValue
      }
      return calculate(firstValue, operator, secondValue)
    } else {
      return displayedNum
    }
  }
}
```

Ensuite, nous voulons réduire les réaffectations. Nous pouvons le faire en passant les bonnes valeurs dans `calculate` via un opérateur ternaire.

```js
const createResultString = () => {
  // ...
  
  if (action === 'calculate') {
    const firstValue = calculator.dataset.firstValue
    const operator = calculator.dataset.operator
    const modValue = calculator.dataset.modValue
    
    if (firstValue) {
      return previousKeyType === 'calculate'
        ? calculate(displayedNum, operator, modValue)
        : calculate(firstValue, operator, displayedNum)
    } else {
      return displayedNum
    }
  }
}
```

Vous pouvez simplifier davantage le code ci-dessus avec un autre opérateur ternaire si vous vous sentez à l'aise avec cela :

```js
const createResultString = () => {
  // ...
  
  if (action === 'calculate') {
    const firstValue = calculator.dataset.firstValue
    const operator = calculator.dataset.operator
    const modValue = calculator.dataset.modValue
    
    return firstValue
      ? previousKeyType === 'calculate'
        ? calculate(displayedNum, operator, modValue)
        : calculate(firstValue, operator, displayedNum)
      : displayedNum
  }
}
```

À ce stade, nous voulons noter à nouveau les propriétés et variables nécessaires :

```js
const createResultString = () => {
  // Variables & propriétés requises sont :
  // 1. keyContent
  // 2. displayedNum
  // 3. previousKeyType
  // 4. action
  // 5. calculator.dataset.firstValue
  // 6. calculator.dataset.operator
  // 7. calculator.dataset.modValue
}
```

### Passage des variables nécessaires

Nous avons besoin de sept propriétés/variables dans `createResultString` :

1. `keyContent`
2. `displayedNum`
3. `previousKeyType`
4. `action`
5. `firstValue`
6. `modValue`
7. `operator`

Nous pouvons obtenir `keyContent` et `action` à partir de `key`. Nous pouvons également obtenir `firstValue`, `modValue`, `operator` et `previousKeyType` à partir de `calculator.dataset`.

Cela signifie que la fonction `createResultString` a besoin de trois variables — `key`, `displayedNum` et `calculator.dataset`. Puisque `calculator.dataset` représente l'état de la calculatrice, utilisons une variable appelée `state` à la place.

```js
const createResultString = (key, displayedNum, state) => {
  const keyContent = key.textContent
  const action = key.dataset.action
  const firstValue = state.firstValue
  const modValue = state.modValue
  const operator = state.operator
  const previousKeyType = state.previousKeyType
  // ... Refactoriser si nécessaire
}

// Utilisation de createResultString
keys.addEventListener('click', e => {
  if (e.target.matches('button')) return
  const displayedNum = display.textContent
  const resultString = createResultString(e.target, displayedNum, calculator.dataset)
  
  // ...
})
```

N'hésitez pas à déstructurer les variables si vous le souhaitez :

```js
const createResultString = (key, displayedNum, state) => {
  const keyContent = key.textContent
  const { action } = key.dataset
  const {
    firstValue,
    modValue,
    operator,
    previousKeyType
  } = state
  
  // ...
}
```

### Cohérence dans les instructions if

Dans `createResultString`, nous avons utilisé les conditions suivantes pour tester le type de touches qui ont été cliquées :

```js
// Si la touche est un nombre
if (!action) { /* ... */ }

// Si la touche est décimale
if (action === 'decimal') { /* ... */ }

// Si la touche est un opérateur
if (
  action === 'add' ||
  action === 'subtract' ||
  action === 'multiply' ||
  action === 'divide'
) { /* ... */}

// Si la touche est effacer
if (action === 'clear') { /* ... */ }

// Si la touche est calculer
if (action === 'calculate') { /* ... */ }
```

Ils ne sont pas cohérents, donc ils sont difficiles à lire. Si possible, nous voulons les rendre cohérents afin de pouvoir écrire quelque chose comme ceci :

```js
if (keyType === 'number') { /* ... */ }
if (keyType === 'decimal') { /* ... */ }
if (keyType === 'operator') { /* ... */}
if (keyType === 'clear') { /* ... */ }
if (keyType === 'calculate') { /* ... */ }
```

Pour ce faire, nous pouvons créer une fonction appelée `getKeyType`. Cette fonction doit retourner le type de touche qui a été cliquée.

```js
const getKeyType = (key) => {
  const { action } = key.dataset
  if (!action) return 'number'
  if (
    action === 'add' ||
    action === 'subtract' ||
    action === 'multiply' ||
    action === 'divide'
  ) return 'operator'
  // Pour tout le reste, retourner l'action
  return action
}
```

Voici comment vous utiliserez la fonction :

```js
const createResultString = (key, displayedNum, state) => {
  const keyType = getKeyType(key)
  
  if (keyType === 'number') { /* ... */ }
  if (keyType === 'decimal') { /* ... */ }
  if (keyType === 'operator') { /* ... */}
  if (keyType === 'clear') { /* ... */ }
  if (keyType === 'calculate') { /* ... */ }
}
```

Nous avons terminé avec `createResultString`. Passons à `updateCalculatorState`.

### Création de updateCalculatorState

`updateCalculatorState` est une fonction qui change l'apparence visuelle de la calculatrice et ses attributs personnalisés.

Comme avec `createResultString`, nous devons vérifier le type de touche qui a été cliquée. Ici, nous pouvons réutiliser `getKeyType`.

```js
const updateCalculatorState = (key) => {
  const keyType = getKeyType(key)
  
  if (keyType === 'number') { /* ... */ }
  if (keyType === 'decimal') { /* ... */ }
  if (keyType === 'operator') { /* ... */}
  if (keyType === 'clear') { /* ... */ }
  if (keyType === 'calculate') { /* ... */ }
}
```

Si vous regardez le code restant, vous remarquerez que nous changeons `data-previous-key-type` pour chaque type de touche. Voici à quoi ressemble le code :

```js
const updateCalculatorState = (key, calculator) => {
  const keyType = getKeyType(key)
  
  if (!action) {
    // ...
    calculator.dataset.previousKeyType = 'number'
  }
  
  if (action === 'decimal') {
    // ...
    calculator.dataset.previousKeyType = 'decimal'
  }
  
  if (
    action === 'add' ||
    action === 'subtract' ||
    action === 'multiply' ||
    action === 'divide'
  ) {
    // ...
    calculator.dataset.previousKeyType = 'operator'
  }
  
  if (action === 'clear') {
    // ...
    calculator.dataset.previousKeyType = 'clear'
  }
  
  if (action === 'calculate') {
    calculator.dataset.previousKeyType = 'calculate'
  }
}
```

C'est redondant car nous connaissons déjà le type de touche avec `getKeyType`. Nous pouvons refactoriser ce qui précède en :

```js
const updateCalculatorState = (key, calculator) => {
  const keyType = getKeyType(key)
  calculator.dataset.previousKeyType = keyType
    
  if (keyType === 'number') { /* ... */ }
  if (keyType === 'decimal') { /* ... */ }
  if (keyType === 'operator') { /* ... */}
  if (keyType === 'clear') { /* ... */ }
  if (keyType === 'calculate') { /* ... */ }
}
```

### Création de `updateCalculatorState` pour les touches opérateur

Visuellement, nous devons nous assurer que toutes les touches libèrent leur état enfoncé. Ici, nous pouvons copier et coller le code que nous avions avant :

```js
const updateCalculatorState = (key, calculator) => {
  const keyType = getKeyType(key)
  calculator.dataset.previousKeyType = keyType
  
  Array.from(key.parentNode.children).forEach(k => k.classList.remove('is-depressed'))
}
```

Voici ce qui reste de ce que nous avons écrit pour les touches opérateur, après avoir déplacé les morceaux liés à `display.textContent` dans `createResultString`.

```js
if (keyType === 'operator') {
  if (firstValue &&
      operator &&
      previousKeyType !== 'operator' &&
      previousKeyType !== 'calculate'
  ) {
    calculator.dataset.firstValue = calculatedValue
  } else {
    calculator.dataset.firstValue = displayedNum
  }
  
  key.classList.add('is-depressed')
  calculator.dataset.operator = key.dataset.action
}
```

Vous remarquerez peut-être que nous pouvons raccourcir le code avec un opérateur ternaire :

```js
if (keyType === 'operator') {
  key.classList.add('is-depressed')
  calculator.dataset.operator = key.dataset.action
  calculator.dataset.firstValue = firstValue &&
    operator &&
    previousKeyType !== 'operator' &&
    previousKeyType !== 'calculate'
    ? calculatedValue
    : displayedNum
}
```

Comme précédemment, notez les variables et propriétés dont vous avez besoin. Ici, nous avons besoin de `calculatedValue` et `displayedNum`.

```js
const updateCalculatorState = (key, calculator) => {
  // Variables et propriétés nécessaires
  // 1. key
  // 2. calculator
  // 3. calculatedValue
  // 4. displayedNum
}
```

### Création de `updateCalculatorState` pour la touche effacer

Voici le code restant pour la touche effacer :

```js
if (action === 'clear') {
  if (key.textContent === 'AC') {
    calculator.dataset.firstValue = ''
    calculator.dataset.modValue = ''
    calculator.dataset.operator = ''
    calculator.dataset.previousKeyType = ''
  } else {
    key.textContent = 'AC'
  }
}

if (action !== 'clear') {
  const clearButton = calculator.querySelector('[data-action=clear]')
  clearButton.textContent = 'CE'
}
```

Il n'y a pas grand-chose que nous pouvons refactoriser ici. N'hésitez pas à copier/coller tout dans `updateCalculatorState`.

### Création de `updateCalculatorState` pour la touche égale

Voici le code que nous avons écrit pour la touche égale :

```js
if (action === 'calculate') {
  let firstValue = calculator.dataset.firstValue
  const operator = calculator.dataset.operator
  let secondValue = displayedNum
  
  if (firstValue) {
    if (previousKeyType === 'calculate') {
      firstValue = displayedNum
      secondValue = calculator.dataset.modValue
    }
    
    display.textContent = calculate(firstValue, operator, secondValue)
  }
  
  calculator.dataset.modValue = secondValue
  calculator.dataset.previousKeyType = 'calculate'
}
```

Voici ce qu'il nous reste si nous supprimons tout ce qui concerne `display.textContent`.

```js
if (action === 'calculate') {
  let secondValue = displayedNum
  
  if (firstValue) {
    if (previousKeyType === 'calculate') {
      secondValue = calculator.dataset.modValue
    }
  }
  
  calculator.dataset.modValue = secondValue
}
```

Nous pouvons refactoriser cela en ce qui suit :

```js
if (keyType === 'calculate') {
  calculator.dataset.modValue = firstValue && previousKeyType === 'calculate'
    ? modValue
    : displayedNum
}
```

Comme toujours, notez les propriétés et variables utilisées :

```js
const updateCalculatorState = (key, calculator) => {
  // Variables et propriétés nécessaires
  // 1. key
  // 2. calculator
  // 3. calculatedValue
  // 4. displayedNum
  // 5. modValue
}
```

### Passage des variables nécessaires

Nous savons que nous avons besoin de cinq variables/propriétés pour `updateCalculatorState` :

1. `key`
2. `calculator`
3. `calculatedValue`
4. `displayedNum`
5. `modValue`

Puisque `modValue` peut être récupéré à partir de `calculator.dataset`, nous n'avons besoin de passer que quatre valeurs :

```js
const updateCalculatorState = (key, calculator, calculatedValue, displayedNum) => {
  // ...
}

keys.addEventListener('click', e => {
  if (e.target.matches('button')) return
  
  const key = e.target
  const displayedNum = display.textContent
  const resultString = createResultString(key, displayedNum, calculator.dataset)
  
  display.textContent = resultString
  
  // Passer les valeurs nécessaires
  updateCalculatorState(key, calculator, resultString, displayedNum)
})
```

### Refactorisation de updateCalculatorState à nouveau

Nous avons changé trois types de valeurs dans `updateCalculatorState` :

1. `calculator.dataset`
2. La classe pour appuyer/enfoncer les opérateurs
3. Le texte `AC` vs `CE`

Si vous voulez le rendre plus propre, vous pouvez diviser (2) et (3) dans une autre fonction — `updateVisualState`. Voici à quoi `updateVisualState` peut ressembler :

```js
const updateVisualState = (key, calculator) => {
  const keyType = getKeyType(key)
  Array.from(key.parentNode.children).forEach(k => k.classList.remove('is-depressed'))
  
  if (keyType === 'operator') key.classList.add('is-depressed')
  
  if (keyType === 'clear' && key.textContent !== 'AC') {
    key.textContent = 'AC'
  }
  
  if (keyType !== 'clear') {
    const clearButton = calculator.querySelector('[data-action=clear]')
    clearButton.textContent = 'CE'
  }
}
```

### Conclusion

Le code devient beaucoup plus propre après la refactorisation. Si vous regardez l'écouteur d'événements, vous saurez ce que fait chaque fonction. Voici à quoi ressemble l'écouteur d'événements à la fin :

```js
keys.addEventListener('click', e => {
  if (e.target.matches('button')) return
  const key = e.target
  const displayedNum = display.textContent
  
  // Fonctions pures
  const resultString = createResultString(key, displayedNum, calculator.dataset)
  
  // Mettre à jour les états
  display.textContent = resultString
  updateCalculatorState(key, calculator, resultString, displayedNum)
  updateVisualState(key, calculator)
})
```

Vous pouvez obtenir le code source pour la partie refactorisation via [ce lien](https://zellwk.com/blog/calculator-part-3) (faites défiler vers le bas et entrez votre adresse e-mail dans la boîte, et je vous enverrai les codes sources directement dans votre boîte mail).

J'espère que vous avez apprécié cet article. Si c'est le cas, vous pourriez aimer [Learn JavaScript](https://learnjavascript.today/) — un cours où je vous montre comment construire 20 composants, étape par étape, comme nous avons construit cette calculatrice aujourd'hui.

Note : nous pouvons améliorer davantage la calculatrice en ajoutant la prise en charge du clavier et des fonctionnalités d'accessibilité comme les régions en direct. Vous voulez savoir comment ? Allez voir Learn JavaScript :)