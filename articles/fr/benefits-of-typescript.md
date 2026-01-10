---
title: Comment TypeScript vous aide à écrire un meilleur code
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2023-11-03T15:16:26.000Z'
originalURL: https://freecodecamp.org/news/benefits-of-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/thumbnail.001.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Comment TypeScript vous aide à écrire un meilleur code
seo_desc: "TypeScript is taking over the web. In this article I'll give you a high-level\
  \ overview of the benefits of TypeScript and how can it help you create websites\
  \ with fewer bugs. \nYou'll learn how TypeScript helps with handling edge cases,\
  \ catching typos,..."
---

TypeScript prend d'assaut le web. Dans cet article, je vais vous donner un aperçu général des avantages de TypeScript et comment il peut vous aider à créer des sites web avec moins de bugs. 

Vous apprendrez comment TypeScript aide à gérer les cas limites, à attraper les fautes de frappe, à refactoriser le code, et comment les types rendent le code plus facile à comprendre. 

La dernière enquête [State of JavaScript](https://2022.stateofjs.com/en-US/usage/) a révélé que les développeurs passent plus de temps à écrire du TypeScript que du code JavaScript. [L'enquête de GitHub](https://octoverse.github.com/2022/top-programming-languages) affirme de manière plus modeste que TypeScript n'est que le 4ème langage le plus utilisé sur la plateforme – derrière JavaScript – mais son utilisation a augmenté de près de 40% en un an. Pourquoi ce changement se produit-il ?

![Image](https://www.freecodecamp.org/news/content/images/2023/11/part0.png)
_Graphique montrant le pourcentage de temps que les développeurs passent à écrire du JavaScript vs TypeScript_

Si vous préférez le format vidéo, vous pouvez également [regarder cet article sous forme de vidéo](https://youtu.be/3nmQj450zk0?si=1HLg0pHnSL5lUe-t) avec un peu plus de contenu.

## Qu'est-ce que les Types ?

Vous savez peut-être que dans JavaScript (comme dans d'autres langages de programmation), il existe divers types de données comme les chaînes de caractères, les nombres, les tableaux, les objets, les fonctions, les booléens, les valeurs undefined et null. Ce sont tous des types. 

Mais JavaScript est typé dynamiquement, ce qui signifie que les variables peuvent changer de type. Vous pouvez définir la valeur d'une variable comme une chaîne de caractères dans une ligne et définir la même variable comme un nombre dans une autre ligne, par exemple :

```javascript
let value = 'Hello';
value = 3;
```

D'une part, c'est un avantage du langage. Cela signifie qu'il est simple et très flexible. Vous n'avez pas à vous restreindre en définissant des types. 

D'autre part, vous pouvez facilement vous tirer une balle dans le pied si vous n'êtes pas assez prudent. Lorsque vous écrivez du JavaScript, c'est votre responsabilité d'utiliser le bon type de valeur dans votre code. 

Si vous utilisez accidentellement les mauvais types, vous rencontrerez des erreurs. Avez-vous essayé d'obtenir la longueur de undefined ? Ne le faites pas, cela vous renvoie une erreur. Mais peut-être aviez-vous un cas limite qui a changé votre valeur et vous ne vous en êtes pas rendu compte :

```javascript
value = 3;
...
console.log(value.length); // TypeError: Cannot read properties of undefined
```

Parce que les variables peuvent changer de type à tout moment, JavaScript ne vérifie si votre code fonctionnera que lorsque vous l'exécutez. Vous ne savez pas que vous avez une erreur jusqu'à ce que vous exécutiez le code. 

Et si vous n'avez une erreur que dans un cas limite très rare, peut-être que vous ne réalisez même pas que votre code pourrait échouer pendant très longtemps. Lorsque vous écrivez le code, JavaScript ne vous avertit pas que vous pourriez avoir un problème.

TypeScript, en revanche, est typé statiquement. Cela signifie que les variables ne peuvent pas changer de type. Cela rend le code plus prévisible et permet à TypeScript d'analyser le code au fur et à mesure que vous l'écrivez et de repérer les erreurs dès qu'elles se produisent (pour qu'elles n'apparaissent pas comme des erreurs dans votre code plus tard).

Bon, maintenant que vous avez une compréhension de base de ce que sont les types et comment JavaScript et TypeScript diffèrent dans leur gestion, plongeons dans la partie principale du tutoriel.

## Vous utilisez déjà TypeScript

Révision des bases : TypeScript vous donne des informations sur les types. Il vous indique les types de vos variables, le type des arguments que vous devez passer à vos fonctions, et quel type de données elles retourneront. 

Mais que se passe-t-il si je vous dis que vous utilisez déjà TypeScript, même en JavaScript simple ?

Prenons cet exemple rapide. Il s'agit d'un fichier JavaScript simple dans VS Code. Parce que VS Code et TypeScript sont tous deux créés par Microsoft, VS Code est déjà livré avec des fonctionnalités TypeScript intégrées.

![Enregistrement d'écran de VS Code avec un simple code JavaScript. Dans une ligne, il y a une variable appelée 'input' qui est définie avec une valeur de chaîne. L'enregistrement montre que lorsque vous survolez le nom de la variable, dans une info-bulle, son type est correctement révélé comme une chaîne. Il montre également qu'une autre variable nommée 'greeting' est définie avec la valeur de retour d'une fonction. En survolant ce nom de variable, il montre également que son type est une chaîne. Enfin, une troisième variable nommée 'greetingLength' est assignée à la longueur de greeting. En la survolant, il est révélé que sa valeur est un nombre.](https://www.freecodecamp.org/news/content/images/2023/11/part1-1.gif)
_Lorsque vous survolez vos variables, VS Code vous indiquera leur type chaque fois que possible_

```javascript
function getGreeting(str) {
	return `Hello ${str}!`;
}

let input = 'Bob'; // Type: string
let greeting = getGreeting(input); // Type: string
let greetingLength = greeting.length; // Type: number

console.log(greeting, greetingLength);
```

Si vous survolez la variable `input`, VS Code vous indiquera que son type est une `string`. C'est assez clair, car nous avons assigné une chaîne de caractères dans la même ligne.

Mais si nous allons plus loin et vérifions le type de `greeting`, il indique également qu'il s'agit d'une `string`. C'est un peu plus intéressant. La valeur de greeting provient d'une fonction. Comment savons-nous qu'il s'agit d'une chaîne de caractères ?

VS Code, avec l'aide de TypeScript, analyse la fonction, vérifie chaque chemin de retour possible et conclut que la seule chose que cette fonction peut retourner est une `string`.

Bien sûr, c'est un exemple très simple. Mais même si nous avions une logique plus complexe, avec plusieurs instructions de retour différentes, TypeScript analyserait toujours chaque chemin différent et vous indiquerait quelles sont les valeurs de retour possibles.

Pour rester un peu plus longtemps sur cet exemple, si nous survolons la variable `length`, nous allons voir que son type est un `number`. Cela peut sembler évident à nouveau, mais la logique derrière est plus intelligente qu'il n'y paraît. 

La propriété `length` d'une `string` est un nombre. Mais cela n'est vrai que si nous regardons une `string`. Dans ce cas, nous savons que c'est une `string` parce que TypeScript a déjà déterminé que le type de retour de notre fonction est une `string`. Il y a plusieurs étapes ici en coulisses.

Donc, la première raison pour laquelle TypeScript est génial : vous pouvez voir les types des valeurs simplement en les survolant. Et cela fonctionne même dans une certaine mesure en JavaScript simple.

### Vérification des arguments requis pour les fonctions intégrées

Voyons un autre exemple. Ce code est toujours en JavaScript, nous ne définissons toujours pas les types explicitement, mais l'analyseur TypeScript peut toujours déduire les types.

Ici, nous avons une valeur d'entrée, nous la codons à nouveau en dur à 'bob', puis nous mettons la chaîne en majuscule. Nous prenons le premier caractère, le mettons en majuscule, puis ajoutons le reste de la chaîne en minuscule.

![Enregistrement d'écran de VS Code avec un simple code JavaScript. Dans le code, nous définissons une variable 'input', nous la mettons en majuscule, puis nous obtenons la longueur de la variable mise en majuscule. L'enregistrement montre que lorsque vous survolez les fonctions utilisées comme charAt et toUpperCase, leur signature est révélée.](https://www.freecodecamp.org/news/content/images/2023/11/part2.gif)
_Vous pouvez vérifier la signature des fonctions JavaScript dans VS Code_

```javascript
let input = 'bob';
let formattedInput = 
	input.charAt(0).toUpperCase() + input.slice(1).toLowerCase();
let formattedLength = formattedInput.length;

console.log(greeting, greetingLength);
```

Nous pouvons vérifier la signature de ces fonctions. Nous pouvons voir que `charAt` nécessite un paramètre de type nombre, `toUpperCase` ne nécessite aucun paramètre, et la fonction `slice` a deux paramètres optionnels qui peuvent être soit un `number` soit `undefined`. 

Ce sont des annotations TypeScript. Les points d'interrogation signifient qu'une valeur est optionnelle, et les caractères pipe signifient qu'un type pourrait être soit ceci soit cela.

En résumé, nous savons que notre entrée formatée est de type `string`.

### Où JavaScript ne peut plus déterminer les types

Extrayons la logique qui met en majuscule notre entrée dans une fonction. Les types devraient rester les mêmes, n'est-ce pas ? Eh bien, pas exactement. Maintenant, notre entrée mise en majuscule est de type `any`.

![VS Code avec un simple code JavaScript. Tout d'abord, nous définissons une fonction simple qui met en majuscule une chaîne, puis nous utilisons cette fonction pour mettre en majuscule une chaîne. L'image montre que lorsque vous survolez la valeur retournée, son type est maintenant de type 'any'.](https://www.freecodecamp.org/news/content/images/2023/11/part3.png)
_Après avoir extrait la logique qui met en majuscule l'entrée, la valeur de retour est maintenant de type 'any'_

```javascript
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input); // Type: any
let formattedLength = formattedInput.length;
```

Intéressant ! Que s'est-il passé ? Notre fonction devrait toujours retourner une chaîne, n'est-ce pas ? Si vous regardez l'ensemble du code dans ce cas spécifique, alors oui. Elle devrait retourner une chaîne. 

Mais nous devons regarder la fonction de manière isolée. Nous ne pouvons pas supposer ce qu'elle recevra. Nous pourrions également lui passer un nombre et dans ce cas, elle échouerait. Vous ne pouvez pas lire le premier caractère d'un nombre ou le mettre en minuscule ou en majuscule.

En JavaScript, nous ne pouvons pas indiquer que nous avons besoin d'une chaîne ici, donc nous ne pouvons pas être sûrs que la fonction retourne une chaîne. En TypeScript, nous allons spécifier le type de ce paramètre pour éviter toute confusion.

Vous avez peut-être remarqué que l'exemple précédent avec la fonction `getGreeting` était différent. Là, peu importe ce qu'était l'entrée, la fonction retournait toujours une `string`. Ici, cependant, la sortie dépend de l'entrée.

## Et les cas limites en JavaScript ?

Pourrions-nous éviter d'obtenir une erreur en cas de mauvaise entrée en JavaScript ? Oui.

Vérifier le type tôt et retourner avant que la fonction ne puisse échouer est un moyen de rendre notre fonction infaillible. Cela reste du JavaScript, et l'opérateur `typeof` fait partie de JavaScript.

Maintenant, cette fonction ne va pas échouer. Mais j'ai introduit un bug.

![VS Code avec le même fichier JavaScript simple que nous avions précédemment. Sauf que maintenant, notre fonction capitalize retourne simplement si son argument n'est pas une chaîne. L'image montre que maintenant le type de la valeur retournée est passé de any à string ou undefined.](https://www.freecodecamp.org/news/content/images/2023/11/part4.png)
_Après avoir ajouté une instruction de retour anticipé à notre fonction capitalize, le type de la valeur retournée est passé de any à string ou undefined_

```javascript
function capitalize(str) {
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input); // Type: string or undefined
let formattedLength = formattedInput.length;
```

Si nous vérifions la signature de la fonction ou le type de la nouvelle valeur, il est passé de `any` à `string | undefined`. 

D'une certaine manière, c'est très bien. Nous avons limité les valeurs de retour possibles et nous avons une meilleure compréhension de ce que fait la fonction, simplement en regardant la valeur retournée. D'un autre côté, dans le cas où elle retourne `undefined`, l'application échouera à la ligne suivante. Vous ne pouvez pas vérifier la longueur de `undefined`.

Bien sûr, nous aurions également pu retourner une chaîne vide comme solution de repli et alors nous n'aurions pas ce problème. Nous travaillons avec des chaînes ici. Mais c'est un excellent exemple d'un sujet qui est très facile à négliger en JavaScript et qui peut vous causer beaucoup de maux de tête plus tard : les cas limites.

Et si vous n'aviez pas écrit la fonction capitalize et que vous ne saviez pas exactement comment elle fonctionne ? 

Peut-être qu'elle est également située dans un fichier différent et que vous avez simplement supposé qu'elle retournerait toujours une chaîne. Peut-être que la fonction que vous utilisez est beaucoup plus longue et beaucoup plus compliquée. 

Peut-être que vous avez vérifié la fonction, mais seulement la dernière ligne et que vous dites 'D'accord, cette fonction retourne une chaîne'. Et vous manquez complètement qu'à une autre ligne – qui peut aussi être au milieu de la fonction – il y a une autre instruction return qui retourne un type de valeur différent.

Le point ici est que les cas limites peuvent se produire et il est très facile de les manquer. C'est une source typique de bugs lorsque les développeurs couvrent le chemin heureux d'une application, mais qu'ils sont moins attentifs lorsqu'ils couvrent les cas limites. 

En JavaScript, vous devez être conscient des cas limites, tester différents scénarios et entrées utilisateur, et écrire des tests unitaires approfondis pour vous assurer que votre logique ne tombe pas en panne.

Ne serait-ce pas bien si l'éditeur vous disait que vous avez un problème ?

## Transformer le code en TypeScript

Alors, après toute cette introduction, transformons enfin ce code en TypeScript. Pour ce faire, changeons simplement l'extension de `.js` à `.ts` et voyons ce qui se passe. 

Tout de suite, nous verrons une erreur disant que notre `formattedInput` pourrait être `undefined`. Et cela ne fonctionne pas bien avec l'obtention de la longueur de la valeur. Nous avons déjà attrapé le bug qui a causé des problèmes plus tôt et nous n'avons même pas investi de temps à ajouter des types à notre code.

![VS Code avec le même fichier que nous avions précédemment. Sauf que maintenant nous avons changé l'extension du fichier en TypeScript. L'image montre qu'une nouvelle erreur apparaît.](https://www.freecodecamp.org/news/content/images/2023/11/part-5.png)
_Après avoir changé l'extension en .ts, une erreur révèle que notre valeur mise en majuscule pourrait être indéfinie_

```typescript
function capitalize(str) {
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input);
let formattedLength = formattedInput.length; // Error
```

Avant de corriger cette erreur, activons le mode `strict`. Par défaut, TypeScript peut être très permissif, mais nous obtenons également moins de valeur sans le mode `strict`. 

Pour cela, nous avons besoin d'un fichier `tsconfig.json` à la racine de notre projet. Cela peut sembler un peu effrayant maintenant, mais ce fichier est probablement généré automatiquement pour vous lorsque vous créez un projet avec l'un des frameworks. Ce qui est important pour l'instant, c'est que nous avons le mode `strict` défini sur true.

```json
{
    "compilerOptions": {
      "target": "ESNext",
      "module": "ESNext",
      "strict": true,
      "esModuleInterop": true,
      "skipLibCheck": true,
      "forceConsistentCasingInFileNames": true,
      "lib": ["DOM", "ESNext"],
      "moduleResolution": "node",
      "noImplicitAny": true,
      "allowSyntheticDefaultImports": true,
      "baseUrl": "./src",
      "paths": {
        "*": ["src/*"]
      },
      "outDir": "./dist",
      "rootDir": "./src",
      "strictPropertyInitialization": false,
      "noEmit": false,
    },
    "include": ["src/**/*.ts", "src/index.js"],
    "exclude": ["node_modules"]
  }

```

Cela affichera plus d'erreurs car avec ce paramètre, nous devons définir les types de nos arguments de fonction.

![VS Code avec le même fichier TypeScript que précédemment. Maintenant avec le mode strict, une autre erreur apparaît indiquant que nous devons définir le type de notre argument de fonction.](https://www.freecodecamp.org/news/content/images/2023/11/part-6.png)
_Après avoir activé le mode strict, nous devons définir le type des arguments de fonction_

```typescript
function capitalize(str) { // Error
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input);
let formattedLength = formattedInput.length; // Error
```

Alors, spécifions que notre fonction capitalize nécessite une `string` en définissant l'argument sur `str: string`. Et c'est tout ce que nous devons ajouter dans ce cas car c'est le seul que TypeScript n'a pas pu déterminer lui-même.

![VS Code avec le même fichier TypeScript que précédemment. Sauf que nous avons défini le type de l'argument de la fonction sur string.](https://www.freecodecamp.org/news/content/images/2023/11/part-7.png)
_Définition du type de l'argument de la fonction sur string_

```typescript
function capitalize(str: string) {
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput = capitalize(input);
let formattedLength = formattedInput.length; // Error
```

Une idée fausse sur TypeScript est que vous devez ajouter des types à tout. Bien que ce ne soit pas une mauvaise pratique, ce n'est pas strictement nécessaire. TypeScript est très intelligent. Il analyse le code et détermine les types de autant de choses que possible.

Nous pouvons bien sûr spécifier des types à d'autres endroits. Nous pouvons spécifier que nous avons besoin que notre valeur `formattedInput` soit une `string` en définissant `let formattedInput: string`. C'est tout notre problème ici. Nous pensions que c'était une chaîne, mais dans certains cas, ce n'était pas le cas.

![VS Code avec le même fichier TypeScript que précédemment. Sauf que maintenant, la variable que nous avons définie avec la valeur retournée par notre fonction capitalize doit être une string. Cela a révélé qu'il pourrait y avoir une incompatibilité de type car la fonction capitalize pourrait retourner undefined.](https://www.freecodecamp.org/news/content/images/2023/11/part-8.png)
_Après avoir défini le type de la variable 'formattedInput', l'erreur a changé_

```typescript
function capitalize(str: string) {
    if (typeof str !== 'string') return;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput: string = capitalize(input); // Error
let formattedLength = formattedInput.length;
```

Cela met en évidence notre problème immédiatement. Nous voulons que ce soit une `string`, mais notre fonction pourrait retourner `undefined`. Nous pouvons lire dans l'info-bulle que `undefined` ne peut pas être assigné au type `string`.

Nous pouvons aller plus loin en disant que nous voulons que cette fonction retourne une `string`. Cela changera à nouveau l'erreur. Maintenant, le problème n'est pas que nous ne pouvons pas assigner la valeur retournée à une variable `string`, mais que la fonction elle-même retourne une valeur incorrecte.

![VS Code avec le même fichier TypeScript que précédemment. Sauf que maintenant, nous avons défini le type de retour de notre fonction capitalize sur string. Cela change notre erreur car la fonction pourrait retourner undefined.](https://www.freecodecamp.org/news/content/images/2023/11/part-9.png)
_Après avoir défini le type de retour de la fonction capitalize, l'erreur a changé à nouveau_

```typescript
function capitalize(str: string): string {
    if (typeof str !== 'string') return; // Error
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

let input = 'bob';
let formattedInput: string = capitalize(input);
let formattedLength = formattedInput.length;
```

Pour résoudre cela, supprimons cette ligne entière. Plus tôt, nous avons ajouté cette ligne pour la vérification de type, mais maintenant, nous laissons TypeScript faire toute la vérification de type pour nous. La signature de la fonction indique déjà que cette propriété doit être une `string`, il n'est pas nécessaire de la vérifier à nouveau. Notre code est devenu plus simple et en même temps plus sûr.

Donc, une autre raison pour laquelle TypeScript est incroyable est qu'il vous force à penser aux cas limites. Non seulement à y penser, mais aussi à les gérer. Quelque chose qui est très facile à négliger en JavaScript.

## Refactorisation du code

Maintenant que nous avons les bases, passons à notre troisième sujet : la refactorisation. Mettons à jour notre fonction de salutation un peu, et disons qu'elle prend maintenant deux arguments : un prénom et un nom de famille. Imaginez que ce soit une fonction utilitaire utilisée à de nombreux endroits dans un projet énorme et complexe :

![VS Code avec un simple fichier TypeScript. Dans ce fichier, nous définissons une fonction 'getGreeting' qui reçoit deux arguments, un prénom et un nom de famille. Le type de ces deux arguments est une chaîne.](https://www.freecodecamp.org/news/content/images/2023/11/part10-1.png)
_Notre nouvelle fonction 'getGreeting' mise à jour qui reçoit un prénom et un nom de famille_

```typescript
export function getGreeting(firstName: string, lastName: string) {
    const formattedFirstName = capitalize(firstName);
    const formattedLastName = capitalize(lastName);
    return `Hello ${formattedFirstName} ${formattedLastName}!`;
}

function capitalize(str: string): string {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}
```

Et si nous décidons que nous devons refactoriser ce code ? Au lieu de passer deux chaînes, nous voulons passer un objet qui a les propriétés de prénom et de nom de famille.

En TypeScript, nous pouvons définir précisément la forme d'un objet. Nous pouvons définir que nous devons passer un paramètre `person` qui devrait être un objet avec une propriété `firstName` et `lastName`, qui doivent toutes deux être des `strings`.

Nous pouvons définir un type pour cet argument. Nous disons que nous avons un type `Person` avec un P majuscule par convention. Ce type décrit un objet avec les propriétés `firstName` et `lastName` qui sont toutes deux des chaînes. 

Nous pouvons même ajouter plus de choses si nous le voulons, comme ajouter une propriété `birthday` qui a un type `Date`. Mais faisons de cela une option car nous ne voulons pas nous en occuper pour l'instant. 

Ajouter un point d'interrogation ici rend cette propriété optionnelle. Nous pouvons la définir, mais nous n'y sommes pas obligés. Mais lorsque nous essayons de l'utiliser, nous ne pouvons pas non plus supposer qu'elle existe.

![VS Code avec le même fichier TypeScript. Sauf que maintenant nous définissons un type personnalisé 'person' comme ceci : `type Person = { firstName: string, lastName: string, birthday?: Date }`. Ensuite, nous changeons les deux arguments de la fonction en un seul argument 'person' de type 'Person'. En conséquence, l'éditeur montre des erreurs dans ce fichier et il met également en évidence dans l'explorateur de fichiers que les autres fichiers ont également des erreurs.](https://www.freecodecamp.org/news/content/images/2023/11/part-10.png)
_Après avoir changé le type d'argument de la fonction, l'éditeur met en évidence les parties que nous devons changer_

```typescript
type Person = {
    firstName: string,
    lastName: string,
    birthDay?: Date
}

export function getGreeting(person: Person) {
    const formattedFirstName = capitalize(firstName);
    const formattedLastName = capitalize(lastName);
    return `Hello ${formattedFirstName} ${formattedLastName}!`;
}

function capitalize(str: string): string {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}
```

Maintenant, nous pouvons définir que notre argument `person` est de type `Person`.

Alors que nous faisons ce changement, l'éditeur s'illumine en rouge. Il dit que j'essaie d'utiliser des variables qui n'existent pas. Dans cette fonction, je fais référence à `firstName` et `lastName`, et il n'y a plus qu'un objet `person`. 

Encore plus, les autres fichiers dans l'explorateur de fichiers s'illuminent également, disant que j'ai appelé la fonction avec deux arguments alors qu'elle n'en attend qu'un.

Corrigeons l'erreur dans ce fichier et remplaçons `firstName` et `lastName` par `person.firstName` et `person.lastName`. TypeScript est très pointilleux sur l'utilisation de variables qui n'existent pas. 

Pour vous donner un exemple encore meilleur : Et si je faisais une faute de frappe ici ? Et si je manquais une lettre de `firstName` ? Cela pourrait être un problème très facilement négligé en JavaScript. Ici, cependant, il n'est pas seulement mis en évidence qu'il n'y a pas une telle propriété sur une `Person`, mais il suggère même que vous pourriez vouloir utiliser `firstName` à la place.

![VS Code avec le même fichier TypeScript. Sauf que maintenant nous avons mis à jour la fonction pour utiliser le nouvel argument de fonction. Par erreur, nous avons fait une faute de frappe. L'éditeur met en évidence la faute de frappe et fait une suggestion.](https://www.freecodecamp.org/news/content/images/2023/11/part-11.png)
_Si nous faisons une faute de frappe, l'éditeur suggère des corrections_

```typescript
type Person = {
    firstName: string,
    lastName: string,
    birthDay?: Date
}

export function getGreeting(person: Person) {
    const formattedFirstName = capitalize(person.frstName);
    const formattedLastName = capitalize(person.lastName);
    return `Hello ${formattedFirstName} ${formattedLastName}!`;
}

function capitalize(str: string): string {
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}
```

Ensuite, corrigeons les erreurs dans les autres fichiers. Comme vous pouvez le voir, les fichiers avec une erreur sont déjà mis en évidence dans l'explorateur de fichiers. Cela reste bien sûr un exemple très simple, mais imaginez que vous avez un projet énorme et que cette fonction est appelée à cent endroits différents. Bien sûr, vous pouvez être minutieux et les corriger un par un, mais en JavaScript, il serait très facile d'en manquer un.

![VS Code avec un autre fichier TypeScript appelant notre fonction définie précédemment. Alors que nous mettons à jour l'appel de fonction de la signature à deux arguments précédente à notre nouvelle, TypeScript donne des erreurs pertinentes si nous faisons des erreurs.](https://www.freecodecamp.org/news/content/images/2023/11/part-12.gif)
_Lors de la mise à jour des appels de fonction, TypeScript vous donne des erreurs si nous faisons des erreurs_

```typescript
import { getGreeting } from "./utils";

let greeting = getGreeting({ firstName: 'bob', lastName:  'marley' });

console.log(greeting);

```

Maintenant, l'erreur dit que nous passons deux paramètres, mais un seul est attendu. Si nous supprimons simplement le deuxième argument, il dit que nous passons une chaîne, mais il attendait un objet de type `Person`. Si nous passons un objet avec seulement le prénom, il se plaindra encore que nous manquons le nom de famille. Si nous ajoutons le nom de famille, mais encore avec une faute de frappe, alors il dira à nouveau que nous avons une mauvaise propriété et il suggère même que nous avons peut-être fait une faute de frappe ici.

TypeScript est très précis sur ce qu'est notre problème, et nous pouvons facilement comprendre comment le corriger.

Maintenant, corrigeons l'autre fichier. Au lieu d'inclure l'argument, nous pouvons également le définir comme une variable et TypeScript reconnaîtra qu'un objet de cette forme correspond aux critères de cette fonction. 

Si nous voulons être sûrs que notre variable est de type Person, nous pouvons également importer le type et l'assigner à cet objet. D'abord, nous devons l'exporter, dans le fichier utilitaire, puis nous pouvons l'importer comme notre fonction, puis l'assigner à notre objet.

![VS Code avec un autre fichier TypeScript appelant notre fonction définie précédemment. Cette fois, nous n'incluons pas l'argument de la fonction, mais créons une nouvelle variable pour celui-ci. Lors de la définition du type de cet argument, nous réutilisons le type 'Person' défini précédemment.](https://www.freecodecamp.org/news/content/images/2023/11/part-13.png)
_Nous pouvons également utiliser notre type Person dans d'autres fichiers_

```typescript
import { Person, getGreeting } from "./utils";

let person: Person = {
    firstName: 'bob',
    lastName: 'dylan'
}

let greeting = getGreeting(person);

console.log(greeting);
```

## Résumé

TypeScript peut être beaucoup plus compliqué que cela. Mais c'est l'essentiel. Pour la plupart, vous définissez vos propres types et TypeScript s'assure que vous les utilisez correctement.

En résumé, il y a trois raisons principales pour lesquelles vous devriez envisager d'utiliser TypeScript :

1. Vous obtenez des informations sur les types des fonctions
2. Vous savez ce qu'elles retournent
3. Vous savez ce qu'elles attendent de vous, même sans regarder la fonction elle-même

TypeScript s'assure que vous assemblez correctement votre application. Il vous force à appeler les fonctions avec les bons arguments et il vous force à penser aux cas limites.

TypeScript aide beaucoup pendant la refactorisation. Il ne vous permet pas de manquer une partie de votre code que vous devez changer et il ne vous laisse pas vous en tirer avec des fautes de frappe.

%[https://youtu.be/3nmQj450zk0?si=hLgdKiFrveP3e6eQ]

### Abonnez-vous pour plus de tutoriels sur le développement web :

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]