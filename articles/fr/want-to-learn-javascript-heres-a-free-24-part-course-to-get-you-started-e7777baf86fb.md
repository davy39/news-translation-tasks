---
title: Apprenez JavaScript en UNE heure avec ce cours gratuit et interactif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T14:30:48.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-javascript-heres-a-free-24-part-course-to-get-you-started-e7777baf86fb
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cae64740569d1a4caa61c.jpg
tags:
- name: learning to code
  slug: learning-to-code
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
seo_title: Apprenez JavaScript en UNE heure avec ce cours gratuit et interactif
seo_desc: 'By Per Harald Borgen


  _A breakdown of the course. You can click here to jump directly to the course._

  JavaScript is the most popular programming language on the web. You can use it to
  create websites, servers, games and even native apps. So no wonder...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*qwstevkkpIh4WQeO0503aw.png)
_Une décomposition du cours. [Vous pouvez cliquer ici pour accéder directement au cours.](https://scrimba.com/g/gintrotojavascript?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotojavascript_launch_article)_

JavaScript est le langage de programmation le plus populaire sur le web. Vous pouvez l'utiliser pour créer des sites web, des serveurs, des jeux et même des applications natives. Il n'est donc pas surprenant que ce soit une compétence si précieuse sur le marché du travail actuel.

J'ai donc contacté [Dylan C. Israel](https://medium.com/u/7f21f9c02e5b) — un YouTuber en programmation et diplômé de freeCodeCamp — et je lui ai demandé de créer un [cours gratuit sur JavaScript sur Scrimba](https://scrimba.com/g/gintrotojavascript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotojavascript_launch_article).

Le cours contient 15 leçons et 7 défis interactifs et est adapté aux débutants. Il vous donnera une introduction rapide aux concepts les plus importants de JavaScript.

Voici comment le cours est structuré.

### Partie #1 : Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gpj7-WF-Esr45IoY8TPjyg.png)

Comme toujours, le cours commence par une présentation générale du sujet et un aperçu de la structure du cours. Dylan vous parlera également un peu de lui afin que vous fassiez connaissance avant de plonger dans la programmation.

### Partie #2 : Variables

Le premier concept que vous devrez apprendre est celui des _variables_, qui servent à stocker des valeurs. En JavaScript moderne, il existe deux mots-clés pour cela : `let` et `const`.

Stockons le nom _Dylan_ dans une variable `let` que nous appellerons `name`.

```js
let name = 'Dylan';  
console.log(name);

// --> 'Dylan'

```

Comme vous pouvez le voir, nous pouvons ensuite faire référence à cette variable plus tard pour récupérer la valeur, par exemple, pour l'afficher dans la console, en utilisant la méthode `console.log()`.

### Partie #3 : Chaînes de caractères

Dans la deuxième leçon, vous apprendrez votre premier type de données : les _chaînes de caractères_. Une chaîne de caractères stocke simplement une séquence de caractères entourée de guillemets. Donc, chaque fois que vous entourez quelque chose de guillemets simples ou doubles, cela devient une chaîne de caractères en JavaScript, comme ceci :

```js
let name = "Dylan";

```

### Partie #4 : Défi sur les chaînes de caractères

Il est temps pour le premier défi du cours ! Dans celui-ci, vous allez essayer de combiner deux variables en une seule.

```js
let firstName = "Dylan";  
let lastName = "Israel";

console.log(fullName);

// --> ReferenceError: fullName is not defined

```

Si c'est votre toute première introduction à JavaScript, vous devrez utiliser vos connaissances fraîchement acquises sur les _variables_ et les _chaînes de caractères_ pour résoudre ce problème. Vous devrez peut-être aussi faire quelques expériences de code. Heureusement, cela est possible sur la plateforme Scrimba.

### Partie #5 : Nombres

Ensuite, vient le deuxième type de données que vous devrez apprendre : les _nombres_. D'autres langages ont souvent plusieurs types de données pour les nombres, comme les _floats_ pour les nombres décimaux et les _integers_ pour les nombres entiers. Cependant, en JavaScript, ils sont tous deux des _nombres_.

Nous pouvons utiliser `typeof` pour vérifier le type de données :

```js
let example1 = 7;  
let example2 = 7.77;

console.log(typeof example1);  
console.log(typeof example2);

// --> "number"  
// --> "number"

```

Dans cette leçon, vous apprendrez également à convertir des valeurs entre chaînes de caractères et nombres en utilisant les méthodes `parseInt()` et `parseFloat()`.

### Partie #6 : Défi sur les nombres

Dans le défi sur les nombres, vous serez exposé à quelques chaînes de caractères et nombres différents combinés avec les méthodes que vous avez apprises jusqu'à présent. Votre tâche est de deviner quelles valeurs ces expressions finissent par avoir.

```js
let example1 = parseInt("33 World 22");  
let example2 = parseFloat('44 Dylan 33');  
let example3 = 55.3333.toFixed(0);  
let example4 = 200.0.toFixed(2);

```

Cela peut être un peu délicat, alors ne vous découragez pas si vous faites des erreurs !

### Partie #7 : Booléens

Les booléens sont simples, ils sont soit _vrais_ soit _faux_. Voici comment créer une valeur booléenne :

```js
let example = true;

```

Le fait que `example` soit maintenant défini sur _true_ peut être utile lorsque vous programmez, car vous souhaitez parfois prendre des actions basées sur des conditions comme celle-ci.

Vous apprendrez également les valeurs _truthy_ ou _falsy_ dans cette leçon, qui sont d'autres types de données, comme les chaînes de caractères ou les nombres, mais qui ont un côté _truthy_ ou _falsy_.

### Partie #8 : Défi sur les booléens

Dans le défi sur les booléens, Dylan suit le même schéma que celui sur les nombres, où vous devez deviner un ensemble de valeurs. Votre tâche est de deviner si ces variables sont _truthy_ ou _falsy_ :

```js
let example1 = false;  
let example2 = true;  
let example3 = null;  
let example4 = undefined;  
let example5 = '';  
let example6 = NaN;  
let example7 = -5;  
let example8 = 0;

```

### Partie #9 : Tableaux

Les types de données que vous avez appris jusqu'à présent sont des valeurs dites _primitives_. Il est maintenant temps d'apprendre les tableaux, qui sont des valeurs _non primitives_.

Un tableau est simplement une liste de valeurs, comme ceci :

```js
let example = ['programming', 'design', 'art'];

```

Vous apprendrez à créer des tableaux, à ajouter et supprimer des éléments, et même à parcourir l'ensemble du tableau en utilisant la méthode `forEach()`.

### Partie #10 : Défi sur les tableaux

Dans le défi sur les tableaux, vous serez introduit au concept de passage par _référence_ ou par _valeur_, ce qui est important pour comprendre correctement JavaScript. Nous revisiterons également ce concept plus tard, car la répétition aidera à ancrer les connaissances.

```js
let example1 = ['Dylan', 5, true];  
let example2 = example1;

example2.push(11);

console.log(example1);  
console.log(example2);

```

Les résultats affichés ci-dessus pourraient vous surprendre si vous n'êtes pas conscient du concept de _passage par référence_.

### Partie #11 : Objets

Des tableaux, nous passerons à leurs proches parents appelés _objets_. Les objets sont similaires aux tableaux en ce sens qu'ils peuvent stocker plusieurs valeurs. Cependant, au lieu de se composer d'une liste de valeurs, un objet se compose de paires clé-valeur. Nous créons un objet en utilisant des accolades :

```js
let example = {  
  firstName: 'Dylan',  
  lastName: 'Israel'  
};

```

Dans cette leçon, vous apprendrez à remplir des objets et à récupérer leurs valeurs.

### Partie #12 : Défi sur les objets

Dans ce défi, nous revisiterons le concept de passage par _référence_ ou par _valeur_. Vous apprendrez également la méthode `Object.assign()`, qui vous permet de créer des copies d'objets.

```js
let example1 = {  
  firstName: 'Dylan'  
};  
let example2 = example1;  
example2.lastName = 'Israel';

console.log(example1);  
console.log(example2);

```

### Partie #13 : Opérateurs arithmétiques

Un langage de programmation serait presque inutile s'il ne savait pas comment effectuer des opérations arithmétiques. En JavaScript, c'est assez simple :

```js
let example = 5 + 5;

console.log(example)

// --> 10

```

Dans cette leçon, vous découvrirez également comment JavaScript gère les expressions où plusieurs opérations sont combinées.

### Partie #14 : Opérateurs relationnels

En programmation, nous devons souvent comparer des valeurs pour voir si elles sont égales ou si l'une est plus grande que l'autre. Dans cette leçon, vous apprendrez à le faire.

```js
let example1 = 10;  
let example2 = 15;

console.log(example1 > example2)

// --> false

```

Un exemple concret serait lorsque vous souhaitez vérifier si un utilisateur a suffisamment de crédit pour acheter un article. Si le crédit est supérieur au prix, alors il est autorisé à acheter, sinon, il ne l'est pas.

### Partie #15 : Défi sur les opérateurs relationnels

Dans ce défi, vous pourrez tester votre compréhension des opérateurs relationnels en devinant la valeur booléenne de ces variables :

```js
let example1 = 5 === 5;  
let example2 = 5 == '5';  
let example3 = 6 != '6';  
let example4 = 7 !== '7';

```

### Partie #16 : Incrémentation et décrémentation

Faire croître ou décroître des valeurs est très souvent fait en programmation, par exemple lorsque vous comptez. Cela peut être fait de plusieurs manières, donc cela mérite sa propre leçon.

```js
let example = 1;  
example = example + 1;

console.log(example);

// --> 2

```

### Partie #17 : Défi sur l'incrémentation et la décrémentation

Ce défi examinera la différence entre `example++` et `++example`.

Cela peut nécessiter quelques expériences pour le comprendre, ou même une recherche sur Google, ce qui est également une compétence critique pour tout développeur.

### Partie #18 : If, else if, else

Les instructions conditionnelles comme `if`, `else if` et `else` sont essentielles en programmation. C'est ce qui permet d'avoir de la logique dans votre application. Dans cette leçon, vous apprendrez à travailler avec les trois.

```js
let example = 5;

if (example === 5) {  
  console.log('Runs');  
} else if ( true ) {  
  console.log('else if');  
} else {  
  console.log('else');  
}

```

Vous apprendrez également à combiner ces conditionnelles avec des opérateurs relationnels pour créer une logique complexe.

### Partie #19 : Défi sur if, else if, else

Dans ce défi, vous essaierez de deviner ce que les expressions suivantes évaluent. Cela s'appuie sur ce que vous avez appris dans la leçon sur les opérateurs relationnels et dans la précédente.

```js
console.log(10 === 10 && 5 < 4);  
console.log(10 === 10 || 5 < 4);  
console.log((5 >= 5 || 4 > 4) && 3 + 2 === 5);

```

Encore une fois, ne perdez pas courage si vous ne parvenez pas à deviner correctement. Ces concepts sont délicats pour un débutant !

### Partie #20 : Switch

Dans cette leçon, vous apprendrez les instructions `switch`, qui sont très pratiques si vous avez de nombreuses conditions à vérifier. Voici un exemple :

```js
let studentAnswer = 'D';

switch(studentAnswer) {  
  case 'A':  
    console.log('A is wrong.');  
    break;  
  case 'B' :  
    console.log('B is wrong.');  
    break;  
  case 'C':  
    console.log('C is correct.');  
    break;  
  default:  
    console.log('Not a real answer.');  
}

```

### Partie #21 : Boucle For

Les boucles For vous permettent d'exécuter un bloc de code un certain nombre de fois. Le nombre est dicté par vous en définissant trois conditions. Voici un exemple de boucle `for` simple :

```js
for (let i = 0; i < 5; i++) {  
  console.log(i);  
}

// -->  
// 0  
// 1  
// 2  
// 3  
// 4 

```

Dans cette leçon, vous verrez comment calculer la somme totale d'un tableau de nombres en utilisant une boucle `for`.

### Partie #22 : While et do while

Si vous souhaitez exécuter un morceau de code plusieurs fois mais ne savez pas _combien_ de fois, alors une boucle `while` pourrait être exactement ce dont vous avez besoin. Elle vous permet d'exécuter un bloc de code tant qu'une certaine condition est remplie.

```js
let count = 0;

while (count < 20) {  
  count++;  
}

console.log(count);

```

Vous apprendrez également l'instruction `do/while`.

### Partie #23 : Fonctions

Enfin, vous devrez apprendre les fonctions, car c'est essentiel pour toute application. Vous apprendrez la syntaxe des fonctions, comment elles sont appelées et comment vous pouvez leur ajouter des paramètres.

```js
function add() {  
  console.log('add');  
}

add();

// --> 'add'

```

Et lorsque vous aurez terminé cette leçon, vous aurez terminé le programme de ce cours, car vous aurez une compréhension des concepts de base de JavaScript.

### Partie #24 : Qu'est-ce qui suit ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*H3vOeCjQV7IlHFqbjLmm_A.png)

Dylan termine le cours en vous parlant un peu de ce que vous pouvez faire ensuite pour améliorer davantage vos compétences en JavaScript ! N'oubliez pas, ce cours n'était qu'un début.

Une fois que vous serez arrivé à ce stade, je vous encourage vivement à continuer, car vous êtes sur la bonne voie pour acquérir une compétence très précieuse dans la société d'aujourd'hui.

Non seulement JavaScript peut vous aider à améliorer votre carrière, mais vous serez également en mesure de construire des produits par vous-même !

Alors, assurez-vous de [suivre ce cours gratuit aujourd'hui](https://scrimba.com/g/gintrotojavascript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotojavascript_launch_article). Vous serez en mesure de construire des projets en JavaScript par vous-même avant de vous en rendre compte !

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) — la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrotojavascript_launch_article) si vous souhaitez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrotojavascript_launch_article)_