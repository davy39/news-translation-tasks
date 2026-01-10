---
title: Syntactic Sugar et Diabète JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-07T00:33:58.000Z'
originalURL: https://freecodecamp.org/news/js-diabetes-and-understanding-syntax-sugar-5de249ee9ebc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*54CJtxnsBXiO8Vlt-edX7w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Syntactic Sugar et Diabète JavaScript
seo_desc: 'By Ryan Yurkanin

  Syntactic sugar is shorthand for communicating a larger thought in a programming
  language.

  I like to compare it to acronyms in natural languages. At first, seeing a new acronym
  can be confusing, but once you know what it means it’s w...'
---

Par Ryan Yurkanin

Le syntactic sugar est un raccourci pour communiquer une idée plus large dans un langage de programmation.

J'aime le comparer aux acronymes dans les langues naturelles. Au début, voir un nouvel acronyme peut être déroutant, mais une fois que vous savez ce qu'il signifie, c'est bien plus rapide !

Avec le syntactic sugar - comme avec les acronymes - vous pouvez GTFAMLH ! (aller trop loin et rendre la vie plus difficile)

Je venais de sortir de l'université, je créais des applications amusantes lors de hackathons avec mes amis, et je vivais une expérience palpitante avec JavaScript en tant que débutant. Je me sentais **invincible**. Je comprenais tous les exemples de Codecademy, j'avais mémorisé toutes les questions d'entretien pour le front-end. J'ai regardé ["What the… JavaScript ?"](https://www.youtube.com/watch?v=2pL28CcEijU) tellement de fois que si un singe enragé hurlait et tapait des lignes de code aléatoires dans une console, je savais ce que cela évaluerait.

Il était temps pour moi de me mettre sur GitHub et de partager mon don avec le _monde_. J'ai ouvert le premier projet que j'ai pu trouver et j'ai commencé à lire. Cela ressemblait à quelque chose comme ceci :

```js
function init(userConfig) {
  const DEFAULT_CONFIG = {
    removeSpaces: false,
    allowHighlighting: true,
    priority: "high",
  }
  
  const config = { ...DEFAULT_CONFIG, ...userConfig };
}
```

Quelques instants plus tard…

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fyz7A2P4dj7jsBt0vKltZQ.png)
_Quand vous cherchez désespérément à ne pas perdre une manche de [Pictionary](https://en.wikipedia.org/wiki/Pictionary" rel="noopener" target="_blank" title="), vous êtes dans le pétrin._

Confus et vaincu, j'ai fermé l'onglet du navigateur et j'ai abandonné pour la journée. Cela marquerait le début d'une série d'actions de ma part :

1. Découvrir une ligne de code qui, à l'époque, n'était que des hiéroglyphes JavaScript.
2. Ne pas savoir comment poser les bonnes questions et formuler des recherches Google probablement parmi les pires jamais vues.
3. Déranger des développeurs aléatoires jusqu'à ce que quelqu'un puisse "Expliquer comme si j'avais 5 ans", mais au final, toujours être confus quant à la raison pour laquelle quelqu'un écrirait quelque chose comme ça. Du sadisme, _probablement_.

4. Comprendre, réaliser pourquoi c'est utile, comprendre quel problème cela résout et comprendre ce que les gens faisaient dans le passé pour résoudre le problème. C'était juste une façon plus concise d'écrire du code ! Ce n'est que du sucre !

5. Parfois, l'utiliser beaucoup trop et rendre mon code subjectivement pire.

6. Trouver l'équilibre et ajouter un excellent outil à ma boîte à outils JavaScript. ?

5. Répéter environ 20 fois.

Maintenant, je suis ici pour essayer de simplifier cela pour vous ! Pour chaque astuce sucrée, j'inclurai un peu de contexte, un problème qu'elle pourrait aider à résoudre, comment vous auriez pu l'atteindre avant le syntactic sugar, et des situations où vous ne voudriez peut-être pas l'utiliser ! ?

### Opérateur Ternaire

L'opérateur ternaire est l'un de mes préférés pour commencer quand on parle de sucre en JavaScript, car il est très facile d'aller trop loin. Il prend normalement la forme `x ? a : b`. Voici un exemple plus réaliste :

```js
const amILazy = true;
const dinnerForTonight = amILazy ? "spaghetti" : "chicken";
```

**Problème :** J'ai une variable qui dépend d'une condition vraie ou fausse.

**Solution Diète :** C'est essentiellement juste une façon très abrégée de faire un `if/else` !

```js
const amILazy = true;
let dinnerForTonight = null;

if(amILazy) { dinnerForTonight = "spaghetti"; }
else { dinnerForTonight = "chicken"; }
```

**Quand ne pas l'utiliser :** Les ternaires sont un moyen très simple d'exprimer des chemins conditionnels. À mon avis subjectif, le pire avec eux est qu'ils sont infiniment imbriquables. Donc, si vous êtes fan de la sécurité de l'emploi, vous pourriez potentiellement écrire ce casse-tête.

```js
const canYouFireMe = someCondition1 ?
  (someCondition2 ? false : true) : false
```

Exemple classique de Diabète JavaScript. **Moins de code ne signifie pas un code plus concis.**

### Spread d'Objets

Ah, l'exemple du début qui m'a brisé le cœur. En JavaScript, lorsque vous voyez `...`, **selon le contexte**, il s'agira de Spread d'Objets/Tableaux, ou de Rest d'Objets/Tableaux. Nous allons couvrir Rest un peu plus tard, alors mettons cela de côté pour l'instant.

Le spread consiste essentiellement à prendre un seul objet, à extraire toutes ses paires clé/valeur et à les mettre dans un autre objet. Voici un exemple de base de spread de deux objets dans un nouvel objet :

```js
const DEFAULT_CONFIG = {
  preserveWhitespace: true,
  noBreaks: false,
  foo: "bar",
};

const USER_CONFIG = {
  noBreaks: true, 
}

const config = { ...DEFAULT_CONFIG, ...USER_CONFIG };
// console.log(config) => {
//   preserveWhitespace: true,
//   noBreaks: true, 
//   foo: "bar",
// }
```

**Problème :** J'ai un objet et je veux créer un autre objet qui a toutes les mêmes clés, avec toutes les mêmes valeurs. Peut-être que je veux faire cela avec plusieurs objets, et si des clés sont en double, choisir quelles clés de l'objet l'emportent.

**Solution Diète :** Vous pourriez utiliser `Object.assign()` pour [obtenir un effet similaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign). Il prend n'importe quel nombre d'objets comme arguments, donne la priorité aux objets les plus à droite en ce qui concerne les clés, et finit par muter le tout premier objet donné. Une erreur courante est de ne pas passer un objet vide comme premier argument et de muter accidentellement un argument que vous ne vouliez pas.

Si c'est difficile à suivre, vous serez heureux de savoir que le Spread d'Objets rend cela impossible. Voici un exemple qui réplique la version avec syntactic sugar.

```js
const DEFAULT_CONFIG = {
  preserveWhitespace: true,
  noBreaks: false,
  foo: "bar",
};

const USER_CONFIG = {
  noBreaks: true, 
}

// si nous ne passions pas un objet vide ici, config
// pointerait vers DEFAULT_CONFIG, et default config serait
// muté
const config = Object.assign({}, DEFAULT_CONFIG, USER_CONFIG);
```

Le spread d'objets élimine la possibilité d'une mutation accidentelle. Vous pourriez donc faire des choses, comme mettre à jour l'état Redux, sans craindre de conserver une référence provoquant l'échec de la comparaison superficielle.

**? Bonus ?** Le spread de tableau fonctionne de manière très similaire ! Mais comme il n'y a pas de clés dans les tableaux, il les ajoute simplement au nouveau tableau comme un appel à `Array.Prototype.concat`.

```js
const arr1 = ['a', 'b', 'c'];
const arr2 = ['c', 'd', 'e'];
const arr3 = [...arr1, ...arr2];
// console.log(arr3) => ['a', 'b', 'c', 'c', 'd', 'e']
```

### Destructuration d'Objets

Celui-ci, je le vois assez couramment dans la nature. Maintenant, nous avons notre nouvel objet de configuration de l'exemple précédent et nous voulons l'utiliser dans notre code. Vous pourriez voir quelque chose comme ceci dispersé dans la base de code.

```js
const { preserveWhiteSpace, noBreaks } = config;

// Maintenant, nous avons deux nouvelles variables avec lesquelles jouer !
if (preservedWhitespace && noBreaks) { doSomething(); };
```

**Problème :** Devoir écrire le chemin complet vers une clé dans un objet peut devenir assez lourd et encombrer beaucoup de code. Pour être plus concis, il serait préférable de créer une variable à partir de la valeur pour garder le code propre.

**Solution Diète :** Vous pouvez toujours le faire à l'ancienne ! Cela ressemblerait à quelque chose comme ceci.

```js
const preserveWhitespace = config.preserveWhitepsace;
const noBreaks = config.noBreaks;
// Répéter indéfiniment jusqu'à avoir toutes les variables nécessaires

if (preservedWhitespace && noBreaks) { doSomething(); };
```

**Quand ne pas l'utiliser :** Vous pouvez en fait destructurer un objet à partir d'un objet et continuer à destructurer de plus en plus profondément ! La destructuration n'est pas la seule façon d'extraire une clé d'un objet. Si vous vous retrouvez à n'utiliser la destructuration que pour des clés à deux ou trois niveaux de profondeur, il y a des chances que vous fassiez plus de mal que de bien au projet.

**? Bonus ?** Les tableaux ont également une destructuration, mais ils fonctionnent en fonction de l'index.

```js
const arr1 = ['a', 'b']
const [x, y] = arr1
// console.log(y) => 'b'
```

### Rest d'Objets

Le Rest d'Objets va de pair avec la Destructuration d'Objets et est très facile à confondre avec le Spread d'Objets. Une fois de plus, nous utilisons l'opérateur `...`, cependant le contexte est **différent**. Cette fois, il apparaît lors de la destructuration et est destiné à regrouper les clés restantes dans un objet. ?

```js
const { preserveWhiteSpace, noBreaks, ...restOfKeys } = config;

// restOfKeys est un objet contenant toutes les clés de config
// à l'exception de preserveWhiteSpace et noBreaks
// console.log(restOfKeys) => { foo: "bar" }
```

**Problème :** Vous voulez un objet qui a un sous-ensemble de clés d'un autre objet.

**Solution Diète :** Vous pourriez utiliser notre vieux copain `Object.assign` et [supprimer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete) toutes les clés dont vous n'avez pas besoin ! ?

**Quand ne pas l'utiliser :** L'utiliser pour créer un nouvel objet avec des clés omises est un cas d'utilisation courant. Soyez simplement conscient que les clés que vous omettez dans la destructuration flottent toujours et prennent potentiellement de la mémoire. Si vous n'êtes pas prudent, cela pourrait causer un bug. ?

```js
const restOfKeys = Object.assign({}, config);
delete restOfKeys.preserveWhiteSpace
delete restOfKeys.noBreaks
```

**? Bonus ?** Devinez quoi ? Les tableaux peuvent faire quelque chose de similaire et cela fonctionne exactement de la même manière !

```js
const array = ['a', 'b', 'c', 'c', 'd', 'e'];
const [x, y, ...z] = array;
// console.log(z) = ['c', 'c', 'd', 'e']
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZeRdmY8ppcSqsW7G66unCw.png)
_Diabète ou effets secondaires de la lecture de cet article ?_

### Conclusion

Le sucre JavaScript est génial, et comprendre comment le lire vous permettra d'entrer dans des bases de code plus diverses et d'élargir votre esprit en tant que développeur. N'oubliez pas que **c'est un acte d'équilibre entre être vraiment concis et rendre votre code lisible pour les autres et pour votre futur vous-même.**

Bien que cela puisse sembler génial de montrer votre nouvel outil brillant, notre travail en tant que programmeurs est de laisser les bases de code plus maintenables qu'elles ne l'étaient lorsque nous les avons trouvées.

Voici une collection des documents MDN sur ce que j'ai couvert si vous souhaitez faire quelques lectures supplémentaires. ?

* [Opérateur Ternaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)
* [Syntaxe de Spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator)
* [Affectation par Destructuration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
* [Paramètres Rest](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)