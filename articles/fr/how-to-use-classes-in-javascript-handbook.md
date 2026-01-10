---
title: Comment utiliser les classes en JavaScript – Un guide pour débutants
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2025-02-18T12:29:27.257Z'
originalURL: https://freecodecamp.org/news/how-to-use-classes-in-javascript-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739878241514/a725b4af-8061-49c2-9575-2aa4096acb74.png
tags:
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Comment utiliser les classes en JavaScript – Un guide pour débutants
seo_desc: Are you curious about classes in JavaScript but feel a little puzzled about
  how they work or why you'd even use them? If that's you, then you're definitely
  in the right place. Lots of developers find classes a bit tricky at first, and honestly,
  I was...
---

Êtes-vous curieux à propos des classes en JavaScript mais vous sentez un peu perplexe quant à leur fonctionnement ou pourquoi vous les utiliseriez ? Si c'est votre cas, alors vous êtes définitivement au bon endroit. De nombreux développeurs trouvent les classes un peu délicates au début, et honnêtement, j'étais une fois dans ce cas aussi.

Cet article est pour vous si l'un de ces points vous semble familier :

* JavaScript est votre premier langage de programmation.
  
* Vous êtes nouveau ou pas entièrement à l'aise avec les principes de la programmation orientée objet (POO).
  
* Vous avez principalement utilisé des fonctions pour structurer votre code JavaScript.
  

Si vous hochez la tête à l'un de ces points, alors continuez à lire.

Dans cet article, nous allons adopter une approche étape par étape, vous montrant comment la programmation orientée objet est implémentée en JavaScript avec des objets et des fonctions constructeurs, et illustrer clairement pourquoi comprendre et utiliser les classes vous rendra un développeur JavaScript plus polyvalent et efficace, même si vous êtes habitué à écrire tout en fonctions. Nous terminerons par un exemple simple d'application de liste de tâches pour que vous puissiez voir comment utiliser les classes.

## Table des matières

* [Des fonctions, des fonctions partout où je me tourne](#heading-des-fonctions-des-fonctions-partout-ou-je-me-tourne)
  
* [Attendez une seconde. Est-ce que nous disons que les fonctions sont mauvaises maintenant ?](#heading-attendez-une-seconde-est-ce-que-nous-disons-que-les-fonctions-sont-mauvaises-maintenant)
  
* [Attendez, quoi ? JavaScript n'a pas de vraies classes ?](#heading-attendez-quoi-javascript-na-pas-de-vraies-classes)
  
* [Parlons des objets en JavaScript.](#heading-parlons-des-objets-en-javascript)
  
* [Fonctions constructeurs : Plans d'objets – Soyons pratiques](#heading-fonctions-constructeurs-plans-dobjets-soyons-pratiques)
  
* [Fonctions constructeurs : Excellentes pour les plans, mais... Gaspillage de mémoire ?](#heading-fonctions-constructeurs-excellentes-pour-les-plans-mais-gaspillage-de-memoire)
  
* [Prototypes à la rescousse (encore) : Partage efficace des méthodes](#heading-prototypes-a-la-rescousse-encore-partage-efficace-des-methodes)
  
* [Fonctions constructeurs + Prototypes : Une combinaison puissante](#heading-fonctions-constructeurs-prototypes-une-combinaison-puissante)
  
* [Héritage avec les fonctions constructeurs : Transmission des traits familiaux (à la manière des constructeurs)](#heading-heritage-avec-les-fonctions-constructeurs-transmission-des-traits-familiaux-a-la-maniere-des-constructeurs)
  
* [Entrée des classes ES6 : Sucre syntaxique pour les prototypes](#heading-entree-des-classes-es6-sucre-syntaxique-pour-les-prototypes)
  
* [Classes ES6 : Syntaxe de classe – Prototypes déguisés](#heading-classes-es6-syntaxe-de-classe-prototypes-deguises)
  
* [Qu'est-ce qui suit ? Plus de fonctionnalités de classe et des exemples concrets](#heading-quest-ce-qui-suit-plus-de-fonctionnalites-de-classe-et-des-exemples-concrets)
  
* [Conclusion](#heading-conclusion)
  

## Des fonctions, des fonctions partout où je me tourne

Si vous avez commencé avec JavaScript, il est probable que vous soyez devenu très à l'aise avec les fonctions. Elles sont comme les blocs de construction de tout pour vous, n'est-ce pas ? Réfléchissez : si je vous demandais d'écrire un programme pour saluer quelqu'un par son nom, vous écriviez probablement quelque chose comme ceci en un clin d'œil :

```javascript
function greetUser(userName) {
  alert("Bonjour, " + userName + " !");
}

greetUser("Alice"); // Comme par magie ! Cela salue Alice.
```

D'accord, passons à un niveau supérieur. Imaginez que je vous demande d'écrire un programme qui détermine l'année de naissance de quelqu'un en connaissant simplement son âge. S'ils ont 25 ans, vous voulez qu'il leur dise '2000' (en supposant que l'année en cours est 2025).

Quelle serait votre première pensée ? Probablement quelque chose comme, 'C'est l'heure des fonctions !' Ai-je raison ? Vous penseriez, 'J'écrirai une fonction ; elle prendra l'âge, et boum, elle donnera l'année de naissance.' Vous voyez ?

Pensée fonction d'abord. Tout à fait naturel en JavaScript. Et voici comment vous pourriez le coder :

```javascript
function getBirthYear(age) {
  const currentYear = 2025; // Pour cet exemple, disons que c'est 2025
  const birthYear = currentYear - age;
  return birthYear;
}
console.log(getBirthYear(25)); // Oui, cela enregistre 2000 !
```

%[https://codepen.io/Spruce_khalifa/pen/gbOYvvo] 

Maintenant, rendons cela un peu plus complexe. Que faire si nous voulons être un peu plus intelligents et nous assurer que l'âge est effectivement un âge valide ? Vous savez, pas une chaîne de caractères folle ou un nombre négatif. En restant fidèles à notre cerveau qui aime les fonctions, quelle est l'étape naturelle suivante ? Une autre fonction, bien sûr. Nous créerions probablement une fonction `validateAge` :

```javascript
function validateAge(age) {
  if (typeof age !== "number" || age <= 0 || age > 120) {
    return "Âge invalide";
  } else {
    return age; // Âge est bon à utiliser !
  }
}

console.log(validateAge(25)); // Sortie : 25 (valide !)
console.log(validateAge("vingt")); // Sortie : Âge invalide (n'est pas un nombre)
console.log(validateAge(-5)); // Sortie : Âge invalide (négatif)
```

%[https://codepen.io/Spruce_khalifa/pen/xbxKYjZ] 

Vous voyez comment nous empilons simplement les fonctions ? `getBirthYear` fait une chose, `validateAge` en fait une autre. Ce sont des petites boîtes de code séparées.

Poussons cela un peu plus loin. Que faire si nous voulions également déterminer le signe zodiacal de quelqu'un en fonction de son année de naissance ? Oui, vous l'avez deviné — le cerveau dit, 'Plus de fonctions.' Écrivons simplement une autre fonction `getZodiacSign` :

```javascript
function getZodiacSign(birthYear) {
    const signs = [
        "Singe", 
        "Coq", 
        "Chien", 
        "Cochon", 
        "Rat",    
        "Bœuf",
        "Tigre", 
        "Lapin", 
        "Dragon", 
        "Serpent", 
        "Cheval", 
        "Mouton"
    ];
    return signs[birthYear % 12]; // Astuce simple de modulo !
}
```

%[https://codepen.io/Spruce_khalifa/pen/RNwbQxg] 

Remarquez-vous le schéma ici ? Pour chaque nouvelle chose que nous voulons faire, nous ajoutons simplement plus *et* plus de fonctions séparées. Les choses commencent à sembler un *peu...* dispersées, n'est-ce pas ? Et nous n'avons même pas fini d'ajouter des fonctionnalités.

D'accord, maintenant, disons que nous voulons stocker encore plus d'informations sur une personne — leur nom, leur pays, leur profession, en plus de leur âge. Comment gérerions-nous tout cela avec notre approche centrée sur les fonctions ? Eh bien, nous pourrions essayer de créer une grande fonction 'Personne' qui prend toutes ces informations :

```javascript
function Person(name, age, country, profession) {
  const personName = name;
  const personAge = age;
  const personCountry = country;
  const personProfession = profession;

  const validatedAge = validateAge(personAge);
  const birthYear = getBirthYear(validatedAge);
  const zodiacSign = getZodiacSign(birthYear);

  alert(
    `${personName}, vous avez ${personAge} ans, né en ${birthYear}, signe zodiacal : ${zodiacSign} !`
  );
}
```

Et si nous voulions ensuite utiliser le nom de la personne dans nos autres fonctions, comme `getZodiacSign` ou `getBirthYear` ? Nous devrions revenir en arrière et ajouter manuellement `name` comme argument à chacune de ces fonctions. Imaginez devoir mettre à jour chaque fonction chaque fois que vous ajoutez une nouvelle information sur la personne.

```js
//  Soudainement, nous avons besoin de 'name' partout !

function getZodiacSign(birthYear, name) {
  alert("Signe zodiacal pour " + name + " est...");
  //... reste de la logique zodiacale...
}

function getBirthYear(age, name) {
  alert("Année de naissance pour " + name + " est...");
  // ... reste de la logique de l'année de naissance...
}
```

Dans cet exemple minuscule, c'est un peu gérable. Mais imaginez un énorme projet avec des tonnes de fonctions réparties dans des fichiers et des dossiers, comment vous essayeriez de tout garder synchronisé et de mettre à jour les fonctions chaque fois que vos données `person` changent. Cela semble être une recette pour des maux de tête, des bugs et beaucoup de frustration. Cela peut devenir incroyablement inefficace et, honnêtement, assez sujet aux erreurs.

## Attendez une seconde. Est-ce que nous disons que les fonctions sont mauvaises maintenant ?

Les fonctions sont incroyables. Considérez cette approche axée sur les fonctions comme la 'manière classique de JavaScript' de faire les choses. Si vous avez commencé avec JavaScript, cela semble probablement tout à fait naturel et confortable — et c'est génial. Même les bibliothèques modernes très populaires comme React sont construites en utilisant des fonctions pour les composants. Les fonctions sont incroyablement puissantes et flexibles.

Mais, même dans React, si vous changez certaines données principales (comme une 'prop' en termes React) dans un composant principal, vous devrez peut-être fouiller dans de nombreux autres composants pour vous assurer que tout fonctionne toujours en douceur. Les fonctions sont fantastiques, mais parfois, pour certains types de problèmes, il pourrait y avoir une autre façon d'organiser notre code. Une façon qui, pour certaines personnes, semble plus intuitive, surtout si elles viennent d'autres horizons de programmation.

Imaginez demander à un programmeur dont le premier langage était Java ou C++ de construire notre programme d'année de naissance. Leur cerveau pourrait s'illuminer, mais ils penseraient probablement quelque chose de légèrement différent. Peut-être quelque chose comme ceci :

'Nous avons besoin d'une `Personne(classe)`. Une `Personne` a un `âge(propriété)` et nous avons besoin d'un moyen de `calculerAnnéeDeNaissance(action)` pour une `Personne`.'

Remarquez quelque chose de différent ? Les fonctions ne sont pas la première chose qui leur vient à l'esprit. Il s'agit davantage d'`objets` et de `choses` ayant des `propriétés` et des `actions`. Étonnant, n'est-ce pas ? De nombreux programmeurs qui ont commencé avec des langages comme Java ou C++ pensent naturellement de cette manière orientée objet (ou POO). Et hé, peut-être que c'est pourquoi vous lisez ceci — peut-être que vous êtes curieux d'explorer cette approche de pensée orientée objet aussi, surtout en JavaScript. Ne vous inquiétez pas, je ne vous demande pas de passer soudainement à Java 😉.

Alors, à propos de ces classes en JavaScript. Préparez-vous pour une petite particularité de JavaScript. Voici le truc : JavaScript n'a techniquement pas de classes de la manière dont les langages comme Java ou C++ en ont. Je sais, cela peut être un peu déroutant. Au lieu de classes classiques comme on en trouve dans des langages comme Java ou C++, JavaScript est construit sur quelque chose appelé prototypes*. *Il utilise ces prototypes flexibles et ces objets pour imiter le fonctionnement des classes dans d'autres langages. Donc, si vous voulez utiliser les classes en JavaScript efficacement, la vraie clé est de comprendre les objets et les prototypes en premier. C'est là que réside la magie de la POO en JavaScript.

## Attendez, quoi ? JavaScript n'a pas de vraies classes ?

Cela signifie-t-il que nous sommes coincés avec juste des fonctions pour toujours ? Non. Même si JavaScript fait les choses à sa manière avec des prototypes (au lieu de classes classiques), il supporte toujours pleinement la 'Programmation Orientée Objet' (POO).

Décomposons la POO en anglais simple. Deux grandes idées dans la POO sont **l'Encapsulation** et **l'Héritage**. Cela semble sophistiqué, n'est-ce pas ? Mais ce sont en réalité des concepts assez simples.

L'Encapsulation ? Imaginez une capsule, comme pour un médicament. Vous regroupez simplement les choses qui appartiennent ensemble. Dans la POO, l'encapsulation signifie regrouper les données (comme l'âge, le nom) et les actions que vous pouvez faire avec ces données (comme calculer l'année de naissance, saluer) à l'intérieur d'un seul 'objet'. Les objets JavaScript sont parfaits pour cela.

Et l'héritage ? Pensez-y comme à l'héritage de traits de votre famille. Dans la POO JavaScript, les objets peuvent 'hériter' de propriétés et de comportements d'autres objets. JavaScript appelle cela l'héritage prototypal, et l'objet dont vous héritez est appelé le prototype (nous plongerons plus profondément dans le prototype bientôt).

Vous voyez ? Pas de prison de fonctions ici. JavaScript est totalement prêt pour la POO. Pour voir cela en action, réécrivons notre programme d'année de naissance, mais cette fois en utilisant ce style POO en JavaScript.

Regardez ceci. Voici comment nous pourrions réécrire notre programme d'année de naissance en utilisant un style POO en JavaScript, en utilisant simplement un bon vieux objet JavaScript :

```javascript
const Person = {
  //  --- Propriétés (Données) ---
  name: "Spruce",
  age: 25,
  country: "Nigeria",
  profession: "Ingénieur",

  //  --- Méthodes (Actions liées aux données de la personne) ---
  isValidAge: function () {
    return typeof this.age === "number" && this.age > 0;
  },

  getBirthYear: function () {
    if (!this.isValidAge()) {
      return "Âge invalide !";
    }
    return new Date().getFullYear() - this.age;
  },

  getZodiacSign: function () {
    if (!this.isValidAge()) {
      return "Oups, impossible d'obtenir le zodiaque pour un âge invalide !";
    }

    const birthYear = this.getBirthYear();
    const zodiacSigns = [
      "Capricorne",
      "Verseau",
      "Poissons",
      "Bélier",
      "Taureau",
      "Gémeaux",
      "Cancer",
      "Lion",
      "Vierge",
      "Balance",
      "Scorpion",
      "Sagittaire",
    ];
    return zodiacSigns[birthYear % 12];
  },

  greet: function () {
    return (
      `Bonjour, je suis ${this.name}. J'ai ${
        this.age
      } ans, né en ${this.getBirthYear()}, ` +
      `travaillant comme ${this.profession} de ${
        this.country
      }.  Mon signe zodiacal est ${this.getZodiacSign()}.`
    );
  },
};

//  --- Utilisons notre objet Person ! ---
console.log(Person.greet());
```

```javascript
//  Sortie (peut varier légèrement selon l'année) :

// "Bonjour, je suis Spruce. J'ai 25 ans, né en 2000, travaillant comme ingénieur du Nigeria.  Mon signe zodiacal est Cochon."
```

%[https://codepen.io/Spruce_khalifa/pen/mydbXKq] 

Vous voyez comme c'est propre ? Tout ce qui concerne une `Personne`, ses détails (nom, âge, etc.) et ce que vous pouvez faire avec une personne (valider l'âge, obtenir l'année de naissance, saluer) est regroupé et bien organisé à l'intérieur de cet objet `Personne` unique. C'est l'encapsulation en action. Plutôt cool, n'est-ce pas ?

Maintenant, voulez-vous connaître le `nom` de la `Personne` ? Super facile :

```javascript
console.log(Person.name); // Sortie : "Spruce"
```

Année de naissance ? Un jeu d'enfant :

```javascript
console.log(Person.getBirthYear()); // Sortie (si l'année en cours est 2025) : 2000
```

Et voici la vraie magie de l'encapsulation : si nous changeons quelque chose à l'intérieur de l'objet `Person` (comme, par exemple, nous décidons de changer l'âge), toutes les méthodes (actions) à l'intérieur s'adaptent automatiquement. Nous n'avons pas à chercher dans des fonctions séparées pour mettre à jour les choses. Laissez-moi vous montrer :

```javascript
//  Âge est 25 initialement...
console.log("Année de naissance lorsque l'âge est 25 :", Person.getBirthYear()); // Sortie (si l'année en cours est 2025) : 2000

//  Mettons à jour l'âge directement dans l'objet Person...
Person.age = 30;

//  Maintenant, getBirthYear utilise automatiquement le *nouvel* âge !
console.log("Année de naissance lorsque l'âge est 30 :", Person.getBirthYear()); // Sortie (si l'année en cours est 2025) : 1995
```

Ainsi, JavaScript utilise des objets — et, comme nous le verrons, des prototypes — pour donner vie à la POO, même s'il n'a pas de classes classiques. Espérons que vous commencez à voir l'attrait d'organiser le code de cette manière. Avant de plonger dans les classes, il est logique d'avoir une compréhension vraiment solide des objets et des prototypes en JavaScript, n'est-ce pas ? C'est ce que nous allons explorer ensuite.

## Parlons des objets en JavaScript.

Si vous êtes déjà familier avec le fonctionnement des objets, c'est fantastique. Cela rendra la compréhension de tout ce que nous couvrons dans cet article encore plus fluide. Pour nous assurer que nous sommes tous sur la même longueur d'onde, commençons par un objet super basique :

```javascript
const Person = {};
```

Alors, est-ce que `Person` est un objet vide ? À première vue, il semble certainement vide. Si vous avez pensé "oui", vous n'êtes pas seul. C'est une pensée initiale courante. Mais en JavaScript, les objets sont un peu plus intéressants que ce que nous y mettons explicitement. Explorons comment les objets fonctionnent vraiment sous le capot.

### D'accord, alors comment fonctionnent les objets en JavaScript ?

Décomposons cela. À sa base, un objet est une collection de propriétés. Pensez aux propriétés comme des conteneurs nommés pour des valeurs. Chaque propriété a un nom (également appelé une 'clé').

```javascript
const Person = {
  firstName: "John",
  lastName: "Doe",
};
```

`firstName` et `lastName` sont les noms des propriétés (clés), et `"John"` et `"Doe"` sont leurs valeurs respectives. Une propriété dans un objet est toujours une paire clé-valeur. La partie valeur peut être beaucoup de choses.

La valeur associée à une propriété peut être un type de données primitif. En JavaScript, les primitives sont des choses comme les chaînes de caractères, les nombres, les booléens (`true` ou `false`), `null`, `undefined`, et les symboles. Voyons quelques exemples :

```javascript
const exampleObject = {
  name: "Example", // Chaîne de caractères
  age: 30, // Nombre
  isStudent: false, // Booléen
  favoriteColor: null, // null
};
```

Mais le truc cool, c'est que les valeurs des propriétés peuvent aussi être des types de données plus complexes ou même d'autres objets, fonctions, et tableaux. Regardons cela :

```js
const anotherObject = {
  address: {
    // Valeur est un autre objet
    street: "123 Main St",
    city: "Anytown",
  },
  hobbies: ["reading", "hiking"], // Valeur est un tableau
  greet: function () {
    // Valeur est une fonction (une méthode !)
    console.log("Hello!");
  },
};
```

Lorsque qu'une fonction est une propriété d'un objet, nous l'appelons une méthode. C'est essentiellement une fonction qui appartient à l'objet et qui opère généralement sur les données de l'objet.

```javascript
const calculator = {
  value: 0,
  add: function(number) {
    this.value += number; // 'this' fait référence à l'objet calculator
  },
  getValue: function() {
    return this.value;
  }
};

calculator.add(5);
console.log(calculator.getValue()); // Output: 5
```

Maintenant, voici où les choses deviennent vraiment intéressantes. Les objets en JavaScript n'ont pas seulement les propriétés que nous définissons explicitement. Ils peuvent également référencer des propriétés d'autres objets. C'est un concept clé appelé héritage prototypal (parfois simplement appelé délégation prototypale).

Vous vous souvenez de notre objet `Person = {}` apparemment vide ? Nous avons dit qu'il semblait vide, n'est-ce pas ? Eh bien, il est temps pour un peu de magie JavaScript. Même si nous n'y avons pas mis de propriétés nous-mêmes, il n'est pas complètement vide. Chaque objet en JavaScript, par défaut, a un lien caché (souvent appelé en interne sa propriété \[\[Prototype\]\]) vers un autre objet appelé son prototype.

Pour les objets créés en utilisant la syntaxe simple `{}` (comme notre objet `person`), leur prototype par défaut est le `Object.prototype` intégré. Pensez à `Object.prototype` comme une sorte d'objet parent qui fournit une fonctionnalité de base intégrée à tous les objets.

C'est pourquoi vous pouvez faire des choses comme ceci, même avec notre objet `Person` "vide" :

```javascript
console.log(Person.toString()); // Output: [object Object]
```

Attendez une minute. Nous n'avons jamais défini de méthode `toString()` dans notre objet `Person`. Alors d'où vient-elle ? Elle provient de son prototype, `Object.prototype`. `toString()` est une méthode intégrée dans `Object.prototype`, et parce que le prototype de `Person` est `Object.prototype`, `Person` peut accéder et utiliser la méthode `toString()`.

Donc, une bonne façon de penser à cela est : "Le prototype d'un objet est un autre objet à partir duquel il peut rechercher et utiliser des propriétés et des méthodes s'il ne les a pas lui-même."

Pourquoi est-il si important de comprendre les prototypes ? Parce que cela déverrouille le pouvoir de la réutilisation du code et de la création d'objets spécialisés basés sur des objets plus généraux. C'est là que les choses deviennent vraiment puissantes, surtout à mesure que vos projets JavaScript grandissent.

Imaginez que nous voulons créer un type plus spécifique de `Personne` — disons, un `Développeur`. Un `Développeur` est toujours une `Personne`, mais il pourrait avoir des propriétés ou des comportements supplémentaires spécifiques aux développeurs. Basiquement, nous voulons qu'un objet `Développeur` soit une `Personne`, mais aussi qu'il ait ses propres trucs uniques.

C'est là que nous pouvons explicitement configurer les prototypes. Au lieu de nous appuyer sur le `Object.prototype` par défaut, nous pouvons dire à JavaScript : "Hey, je veux que le prototype de mon objet `Développeur` soit l'objet `Personne` que nous avons déjà défini." Nous pouvons faire cela en utilisant `Object.create()` :

```js
const Person = {
  firstName: "John",
  lastName: "Doe",
  sayHello: function () {
    console.log(`Bonjour, mon nom est ${this.firstName} ${this.lastName}`);
  },
};

const developer = Object.create(Person); // le prototype de developer est maintenant 'Person'
developer.firstName = "Spruce"; // Ajoute un firstName *spécifique* pour developer
developer.programmingLanguage = "JavaScript"; // Propriété propre au developer

developer.sayHello(); // Output: Bonjour, mon nom est Spruce Person (accède toujours à sayHello depuis le prototype 'person' !)
console.log(developer.programmingLanguage); // Output: JavaScript (propriété propre au developer)
console.log(developer.lastName); // Output: Doe (hérité du prototype 'Person' !)
```

Décomposons ce qui se passe lorsque nous accédons aux propriétés sur `Developer` :

```javascript
console.log(developer.firstName); // Output: Spruce (propriété *propre* de developer)
console.log(developer.programmingLanguage); // Output: JavaScript (propriété *propre* de developer)
console.log(developer.lastName); // Output: Doe (trouvé sur le *prototype* 'Person')
console.log(developer.sayHello()); // Output: Bonjour, mon nom est Spruce Person (méthode du *prototype*)
console.log(developer.job); // Output: undefined (non sur 'Developer' OU prototype 'Person')
```

Lorsque vous essayez d'accéder à une propriété comme `Developer.lastName`, JavaScript fait ce qui suit :

1. Tout d'abord, il vérifie : Est-ce que `Developer` a une propriété nommée `lastName` directement sur lui-même ? Dans notre exemple, `Developer` n'a que `firstName` et `programmingLanguage` comme ses propres propriétés. `lastName` n'est pas là.
   
2. Si elle ne la trouve pas sur l'objet lui-même, JavaScript regarde alors le prototype de l'objet (que nous avons défini comme `Person` en utilisant `Object.create()`).
   
3. Elle vérifie : 'Est-ce que l'objet `Person` (le prototype) a une propriété nommée `lastName` ?' Oui, `Person` a `lastName: "Doe"`. Donc, JavaScript utilise cette valeur.
   
4. Si la propriété n'est pas trouvée sur le prototype non plus, JavaScript regarderait alors le prototype de `Person` (qui est `Object.prototype` par défaut), et ainsi de suite, jusqu'à la chaîne de prototypes. Si elle remonte toute la chaîne et ne trouve toujours pas la propriété, elle retourne finalement `undefined` (comme lorsque nous avons essayé d'accéder à `developer.job`).
   

Les propriétés propres sont simplement les propriétés qui sont définies directement sur l'objet lui-même lorsque vous le créez (comme `firstName` et `programmingLanguage` sur `Developer`). Les propriétés de prototype sont accessibles via la chaîne de prototypes.

Vous pouvez même créer des chaînes de prototypes plus longues. Par exemple, disons que nous voulons créer un objet `JavaScriptDeveloper`, qui est un type de `Developer`. Nous pouvons faire de `Developer` le prototype de `JavaScriptDeveloper` :

```javascript
const JavaScriptDeveloper = Object.create(Developer); // le prototype de javaScriptDeveloper est 'Developer'

JavaScriptDeveloper.framework = "React"; // Propriété propre à JavaScriptDeveloper

console.log(JavaScriptDeveloper.firstName); // Output: Spruce (du prototype 'Developer')

console.log(JavaScriptDeveloper.lastName); // Output: Doe (du prototype 'Person')

console.log(JavaScriptDeveloper.programmingLanguage); // Output: JavaScript (du prototype 'Developer')

console.log(JavaScriptDeveloper.framework); // Output: React (propriété propre à JavaScriptDeveloper)

console.log(JavaScriptDeveloper.job); // Output: undefined (non trouvé nulle part dans la chaîne)
```

(Exploration optionnelle : Si vous êtes curieux, tracez la recherche pour `javaScriptDeveloper.lastName`. Elle va : `JavaScriptDeveloper` -> `Developer` -> `Person` -> `Object.prototype`).

D'accord, les prototypes sont puissants. Nous pouvons créer des objets qui partagent des propriétés et des comportements et les spécialiser pour différents besoins. Mais imaginez si nous voulions créer des centaines d'objets `Person`, des centaines d'objets `Developer`, et des centaines d'objets `JavaScriptDeveloper`.

Utiliser `Object.create()` à chaque fois serait encore assez répétitif, surtout si nous voulons nous assurer que chaque `Person` commence avec les mêmes propriétés de base (comme `firstName` et `lastName`).

Nous avons besoin d'une meilleure façon de créer plusieurs objets qui suivent le même modèle, comme un plan que nous pouvons réutiliser encore et encore pour créer des objets. C'est à cela que servent les classes, ce sont simplement des plans que nous pouvons utiliser pour créer plusieurs objets, et JavaScript utilise des fonctions constructeurs pour créer des classes (les plans).

Dans la section suivante, nous plongerons dans la manière dont JavaScript utilise les fonctions constructeurs pour implémenter les classes.

## Fonctions constructeurs : Plans d'objets – Soyons pratiques

D'accord, les prototypes sont assez cool pour la réutilisation de code et la création d'objets spécialisés. Nous avons vu comment `Object.create()` nous permet de créer des objets qui héritent d'autres. Mais imaginez que nous voulions faire des tonnes d'objets `Person`, comme, des centaines d'entre eux pour un site web. Taper `Object.create(person)` pour chacun d'eux deviendrait super répétitif, surtout si nous voulons toujours que chaque `Person` commence avec les mêmes propriétés de base, comme un `firstName` et `lastName`.

Nous avons besoin d'une manière plus efficace de faire beaucoup d'objets qui suivent le même modèle. Ce dont nous avons vraiment besoin, c'est quelque chose comme un plan — quelque chose que nous pouvons utiliser encore et encore pour créer de nouveaux objets, tous ayant la même apparence et fonctionnant de manière similaire. Et devinez quoi ? C'est exactement à cela que servent les fonctions constructeurs.

Considérez les fonctions constructeurs comme la manière de JavaScript de créer des plans pour les objets. Ce sont comme des usines à objets. Et en JavaScript, nous utilisons des fonctions constructeurs, qui sont des fonctions spécialisées utilisées de manière particulière, pour créer ces plans. Oui, encore des fonctions. Mais nous les utilisons de manière spéciale.

### Alors, qu'est-ce qu'une fonction constructeur, exactement ?

Eh bien, comme je l'ai dit, c'est une fonction qui crée des objets. Jetez un œil à cet exemple :

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    console.log(`Bonjour, je suis ${this.name}`);
  };
}
```

Cela ressemble à une fonction régulière. Vous avez absolument raison. Cela ressemble exactement à n'importe quelle autre fonction que vous avez probablement écrite en JavaScript. En fait, prouvons-le. Si nous affichons simplement `PersonConstructor` lui-même, nous verrons :

```js
console.log(PersonConstructor);
```

```js
// output
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    console.log(`Bonjour, je suis ${this.name}`);
  };
}
```

Vous voyez ? Juste une fonction régulière. Alors, qu'est-ce qui en fait une fonction constructeur ?

### L'ingrédient magique : le mot-clé `new`

Ce qui transforme une fonction ordinaire en un constructeur — quelque chose qui construit des objets — est le mot-clé `new`. C'est comme dire à JavaScript : "Hey, traite cette fonction comme un plan, et utilise-la pour créer un nouvel objet pour moi."

Voyons cela en action :

```js
const person1 = new PersonConstructor("Alice", 25);

console.log(person1);
```

```js
// output

// PersonConstructor { name: 'Alice', age: 25, greet: [Function] }
```

Dans la sortie maintenant, au lieu de simplement voir le code de la fonction, nous voyons un objet `PersonConstructor`. Le mot-clé `new` n'a pas simplement appelé la fonction, il a en fait créé un tout nouvel objet basé sur le plan `PersonConstructor`.

Maintenant, nous pouvons utiliser ce plan, `PersonConstructor`, pour créer autant d'objets `Person` que nous voulons, tous avec la même structure de base :

```js
const person1 = new PersonConstructor("Alice", 25);
const person2 = new PersonConstructor("Bob", 30);
const person3 = new PersonConstructor("Charlie", 28);

console.log(person1);
console.log(person2);
console.log(person3);
```

```js
// output
PersonConstructor { name: 'Alice', age: 25, greet: [Function] }
PersonConstructor { name: 'Bob', age: 30, greet: [Function] }
PersonConstructor { name: 'Charlie', age: 28, greet: [Function] }
```

Cool, n'est-ce pas ? Nous avons trois objets `Person` distincts, tous créés à partir du même plan `PersonConstructor`.

### Attendez... Qu'est-ce que ce mot-clé `this` que je vois partout ?

Vous avez probablement remarqué le mot `this` qui apparaît souvent dans ces exemples de code, comme dans `this.name`, `this.age`, et `this.greet()`. Et vous pourriez penser, "Qu'est-ce que ce `this` dans le monde JavaScript ?"

Ne vous inquiétez pas, `this` peut être un peu déroutant au début, mais c'est en fait assez simple une fois que vous avez compris. Décomposons cela avec une simple analogie.

Imaginez que vous vous décrivez. Vous pourriez dire, "Mon nom est \[Votre Nom\]." Dans cette phrase, "mon" fait référence à vous, la personne qui parle.

Dans les objets JavaScript, `this` est comme "mon" ou "moi." C'est une façon pour un objet de se référer à lui-même.

Regardons cela avec un exemple d'objet régulier d'abord :

```js
const PersonObject = {
  name: "Spruce",
  greet: function () {
    console.log("Bonjour, mon nom est " + PersonObject.name); //  Utilisation directe de PersonObject.name
  },
};

PersonObject.greet(); // Output: Bonjour, mon nom est Spruce
```

Dans cet objet `PersonObject`, à l'intérieur de la fonction `greet`, nous avons utilisé `PersonObject.name` pour accéder à la propriété `name`. Cela fonctionne parfaitement bien. Nous disons directement à JavaScript de récupérer la propriété `name` de `PersonObject`. Nous pourrions utiliser `this` ici aussi, mais voyons pourquoi `this` devient super utile, surtout dans les fonctions constructeurs.

Maintenant, considérons cette version légèrement différente utilisant `this` :

```js
const PersonObjectThis = {
  name: "Spruce",
  greet: function () {
    console.log("Bonjour, mon nom est " + this.name); // Utilisation de 'this.name'
  },
};

PersonObjectThis.greet(); // Output: Bonjour, mon nom est Spruce
```

Vous voyez ? Cela fonctionne de la même manière. Lorsque `greet` est appelé sur `PersonObjectThis`, à l'intérieur de la fonction `greet`, il fait automatiquement référence à `PersonObjectThis`. Donc `this.name` est simplement une manière plus dynamique de dire "la propriété `name` de cet objet actuel."

### Pourquoi utiliser `this` au lieu de nommer directement l'objet ?

Parce que `this` est dynamique et conscient du contexte. Il pointe toujours vers l'objet qui appelle actuellement la méthode. Cela devient essentiel dans les fonctions constructeurs car les fonctions constructeurs sont conçues pour créer de nombreux objets différents.

### Retour aux fonctions constructeurs : Que signifie `this` là-bas ?

Revisitons notre `PersonConstructor` :

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    console.log(`Bonjour, je suis ${this.name}`);
  };
}

const person1 = new PersonConstructor("Alice", 25);
const person2 = new PersonConstructor("Bob", 30);
```

Lorsque nous faisons `const person1 = new PersonConstructor("Alice", 25);` à l'intérieur de la fonction `PersonConstructor` :

* `this` devient `person1`. C'est comme si JavaScript faisait :
  
  * [`person1.name`](http://person1.name) `= "Alice";`
      
  * `person1.age = 25;`
      
  * `person1.greet = function() { ... };`
      

Et lorsque nous faisons `const person2 = new PersonConstructor("Bob", 30);` à l'intérieur de `PersonConstructor` à nouveau :

* `this` devient `person2`. Comme si JavaScript faisait :
  
  * [`person2.name`](http://person2.name) `= "Bob";`
      
  * `person2.age = 30;`
      
  * `person2.greet = function() { ... };`
      

Ainsi, `this` dans une fonction constructeur est comme un espace réservé qui est rempli avec l'objet spécifique en cours de création lorsque vous utilisez `new`. C'est ce qui nous permet de créer de nombreux objets différents à partir du même plan.

## Fonctions constructeurs : Excellentes pour les plans, mais... Gaspillage de mémoire ?

D'accord, maintenant que vous savez comment créer des plans d'objets en utilisant des fonctions constructeurs, et que vous comprenez ce que fait `this`, nous pouvons créer beaucoup d'objets `Person`.

Mais il y a un petit problème qui se cache dans notre `PersonConstructor` :

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
  this.greet = function () {
    // 😬 Regardez cette fonction greet !
    console.log(`Bonjour, je suis ${this.name}`);
  };
}

const person1 = new PersonConstructor("Alice", 25);
const person2 = new PersonConstructor("Bob", 30);

console.log(person1, person2);
```

```js
// output

PersonConstructor {name: "Alice", age: 25, greet: function}

PersonConstructor {name: "Bob", age: 30, greet: function}
```

Remarquez la fonction `greet` à l'intérieur de `PersonConstructor` ? Chaque fois que nous créons un nouvel objet `Person` en utilisant `new PersonConstructor()`, nous copions en fait toute la fonction `greet` à chaque objet.

Imaginez que nous créons mille objets `Person`. Nous aurions mille fonctions `greet` identiques en mémoire. Pour une simple fonction `greet()`, l'impact sur la mémoire peut sembler faible. Cependant, si vous aviez des méthodes plus complexes avec beaucoup de code, ou si vous créiez des milliers voire des millions d'objets, dupliquer ces fonctions pour chaque objet peut devenir un gaspillage significatif de mémoire.

Cela affecte également les performances car JavaScript doit gérer toutes ces fonctions dupliquées. C'est beaucoup de code dupliqué, et ce n'est pas très efficace en termes de mémoire, surtout si la fonction `greet` (ou d'autres méthodes) étaient plus complexes.

## Prototypes à la rescousse (encore) : Partage efficace des méthodes

Vous vous souvenez des prototypes ? Nous avons appris que les objets peuvent hériter de propriétés et de méthodes de leurs prototypes. Eh bien, les fonctions constructeurs ont un moyen intégré d'utiliser les prototypes pour résoudre ce problème de gaspillage de mémoire.

Au lieu de définir la fonction `greet` à l'intérieur du constructeur et ainsi la copier à chaque instance, nous pouvons l'ajouter au `prototype` de la fonction `PersonConstructor`.

Comme ceci :

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
}

//  --- Ajoutez la méthode greet au PROTOTYPE de PersonConstructor ! ---
PersonConstructor.prototype.greet = function () {
  console.log(`Bonjour, je suis ${this.name}`);
};
```

Maintenant, la méthode `greet` est définie une seule fois sur `PersonConstructor.prototype`. Mais tous les objets créés avec `PersonConstructor` peuvent toujours l'utiliser. Ils l'héritent du prototype.

Testons cela :

```js
const person1 = new PersonConstructor("Alice", 25);
const person2 = new PersonConstructor("Bob", 30);

person1.greet(); // Output: Bonjour, je suis Alice  - Ça marche toujours !
person2.greet(); // Output: Bonjour, je suis Bob    - Ça marche toujours !

console.log(person1.greet === person2.greet); // Output: false - Ils ne sont PAS la même fonction objet en mémoire

console.log(person1.__proto__.greet === person2.__proto__.greet); // Output: true - Mais ils partagent la même méthode prototype !
```

`person1.greet()` et `person2.greet()` fonctionnent toujours parfaitement. Mais maintenant, la fonction `greet` n'est pas copiée pour chaque objet. Elle est partagée via le prototype. Cela est beaucoup plus efficace, surtout lorsque nous traitons avec beaucoup d'objets et de méthodes.

## Fonctions constructeurs + Prototypes : Une combinaison puissante

Nous avons maintenant vu comment les fonctions constructeurs agissent comme des plans pour créer des objets, et comment utiliser le prototype d'une fonction constructeur nous permet de partager efficacement des méthodes parmi tous les objets créés à partir de ce plan.

C'est un modèle clé en JavaScript pour créer des structures d'objets réutilisables.

### D'accord, nous avons couvert la création d'objets et les méthodes efficaces... Mais qu'en est-il de l'héritage avec les fonctions constructeurs ?

Et si nous voulions créer un plan `DeveloperPerson` qui hérite de notre plan `PersonConstructor` ? De sorte que les objets `DeveloperPerson` aient automatiquement `name`, `age`, et `greet`, mais puissent également avoir leurs propres propriétés et méthodes spécifiques aux développeurs ?

C'est là que les choses deviennent un peu plus impliquées avec les fonctions constructeurs, et nous devrons utiliser une astuce spéciale appelée `call()` pour faire fonctionner l'héritage. Plongeons-nous dans cela ensuite.

## Héritage avec les fonctions constructeurs : Transmission des traits familiaux (à la manière des constructeurs)

D'accord, nous faisons de bons progrès. Nous avons des fonctions constructeurs pour créer des plans d'objets, et des prototypes pour partager des méthodes efficacement. Mais l'une des grandes raisons pour lesquelles les gens utilisent la POO est l'héritage — l'idée de créer des objets spécialisés qui s'appuient sur des objets plus généraux.

Repensez à notre exemple de `Person` et `Developer`. Un `Developer` est une `Person`, n'est-ce pas ? Ils ont un nom, un âge, peut-être qu'ils saluent les gens, mais ils ont aussi des propriétés spécifiques aux développeurs, comme un langage de programmation préféré et la capacité à coder.

Comment pouvons-nous créer un plan `DeveloperPersonConstructor` qui hérite de toutes les bases de `PersonConstructor`, puis ajoute ses propres fonctionnalités spécifiques aux développeurs ? Avec les fonctions constructeurs, vous pouvez utiliser quelque chose appelé `call()`.

### `call()` : La poignée de main secrète de l'héritage

`call()` est une méthode de fonction qui vous permet de faire quelque chose d'un peu inhabituel : vous pouvez emprunter une fonction à un objet et l'exécuter dans le contexte d'un autre objet. Cela semble confus ? Simplifions.

Pour illustrer `call()`, considérons notre `PersonConstructor`. Nous voulons créer un `DeveloperPersonConstructor` qui configure également `name` et `age` de la même manière que `PersonConstructor`, avant d'ajouter des propriétés spécifiques aux développeurs.

C'est là que `call()` intervient. Nous pouvons utiliser `call()` pour dire essentiellement : "Hey `PersonConstructor`, exécute ton code, mais exécute-le comme si tu étais à l'intérieur de `DeveloperPersonConstructor`, et configure `name` et `age` pour cet objet `DeveloperPerson` que nous sommes en train de créer."

Voyons cela en code pour que ce soit plus clair :

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
}

PersonConstructor.prototype.greet = function () {
  console.log(`Bonjour, je suis ${this.name}`);
};

function DeveloperPersonConstructor(name, age, programmingLanguage) {
  //  --- "Emprunte" le PersonConstructor pour configurer name et age ! ---
  PersonConstructor.call(this, name, age); //  <--  La magie de 'call()'

  // --- Maintenant, ajoute des propriétés spécifiques aux développeurs ---
  this.programmingLanguage = programmingLanguage;
  this.code = function () {
    console.log(`${this.name} est en train de coder en ${this.programmingLanguage}`);
  };
}
```

Voyez cette ligne : [`PersonConstructor.call`](http://PersonConstructor.call)`(this, name, age);` ? C'est la clé de l'héritage ici. Décomposons cela :

* [`PersonConstructor.call`](http://PersonConstructor.call)`(...)` : Nous appelons la fonction `PersonConstructor`, mais pas de la manière habituelle. Nous utilisons `.call()`.
  
* `this` : Le premier argument de `call()` est crucial. Il spécifie ce que `this` doit être à l'intérieur de la fonction `PersonConstructor` lorsqu'elle s'exécute. Ici, nous passons `this` de `DeveloperPersonConstructor`. Pourquoi ? Parce que nous voulons que `PersonConstructor` configure `name` et `age` sur l'objet `DeveloperPerson` qui est actuellement en cours de création.
  
* `name, age` : Ce sont les arguments que nous passons à la fonction `PersonConstructor` elle-même. Donc, lorsque `PersonConstructor` s'exécute (grâce à `.call()`), il recevra `name` et `age` et fera ce qu'il fait normalement : définir `this.name = name` et `this.age = age`. Mais parce que `this` est en fait l'objet `DeveloperPerson`, il définit ces propriétés sur l'objet `DeveloperPerson`.
  

### Mettre tout ensemble : Créer un `DeveloperPerson`

Maintenant, créons un objet `DeveloperPerson` et voyons ce qui se passe :

```js
const devPerson1 = new DeveloperPersonConstructor("Eve", 30, "JavaScript");

console.log(devPerson1.name); // Output: Eve (Hérité de PersonConstructor !)
console.log(devPerson1.age); // Output: 30 (Hérité de PersonConstructor !)
devPerson1.greet(); // Output: (Oups ! Erreur !)
console.log(devPerson1.programmingLanguage); // Output: JavaScript (Spécifique au développeur)
devPerson1.code(); // Output: Eve est en train de coder en JavaScript (Spécifique au développeur)
```

Remarquez que `devPerson1.name` et `devPerson1.age` sont là. `DeveloperPersonConstructor` a emprunté la partie de `PersonConstructor` qui configure ces propriétés de base. Et nous avons également `devPerson1.programmingLanguage` et `devPerson1.code()` qui sont spécifiques aux développeurs.

### Oh Oh ! Où est `greet()` ?

Mais attendez, `devPerson1.greet()` lance une erreur. Pourquoi ? Parce que même si nous avons emprunté la logique du constructeur de `PersonConstructor`, nous n'avons pas encore établi la chaîne de prototypes pour l'héritage des méthodes de prototype comme `greet()`.

Actuellement, le prototype de `devPerson1` est simplement le prototype d'objet par défaut (`Object.prototype`). Il n'hérite pas de `PersonConstructor.prototype`. Nous devons corriger cela.

### Établir la chaîne de prototypes pour l'héritage des constructeurs

Pour que les objets `DeveloperPersonConstructor` héritent également des méthodes de prototype de `PersonConstructor`, nous devons ajuster manuellement la chaîne de prototypes. Nous pouvons faire cela en utilisant `Object.create()` à nouveau.

Nous voulons que le prototype de `DeveloperPersonConstructor` soit un objet qui hérite de `PersonConstructor.prototype`.

Voici le code :

```js
function PersonConstructor(name, age) {
  this.name = name;
  this.age = age;
}

PersonConstructor.prototype.greet = function () {
  console.log(`Bonjour, je suis ${this.name}`);
};

function DeveloperPersonConstructor(name, age, programmingLanguage) {
  PersonConstructor.call(this, name, age);
  this.programmingLanguage = programmingLanguage;
  this.code = function () {
    console.log(`${this.name} est en train de coder en ${this.programmingLanguage}`);
  };
}

// ---  Établir la chaîne de prototypes pour l'héritage ! ---
DeveloperPersonConstructor.prototype = Object.create(
  PersonConstructor.prototype
);
```

Cette ligne `DeveloperPersonConstructor.prototype = Object.create(PersonConstructor.prototype);` fait la magie. Elle dit, "Hey JavaScript, définis le prototype de `DeveloperPersonConstructor` comme étant un nouvel objet qui hérite de `PersonConstructor.prototype`."

Maintenant, essayons `devPerson1.greet()` à nouveau :

```js
const devPerson1 = new DeveloperPersonConstructor("Eve", 30, "JavaScript");

devPerson1.greet(); // Output: Bonjour, je suis Eve  - 🎉 Ça marche maintenant !
```

`devPerson1.greet()` fonctionne maintenant. `devPerson1` hérite de la méthode `greet()` de `PersonConstructor.prototype` via la chaîne de prototypes que nous venons d'établir.

### Traçons la chaîne de prototypes

Comprenons vraiment ce qui se passe lorsque nous faisons `devPerson1.greet()` :

1. JavaScript vérifie : Est-ce que `devPerson1` lui-même a une propriété `greet` ? Non.
   
2. JavaScript regarde le prototype de `devPerson1` : `DeveloperPersonConstructor.prototype`. A-t-il une propriété `greet` ? Non, nous n'avons ajouté que des méthodes ou propriétés spécifiques aux développeurs à `DeveloperPersonConstructor` directement, pas à son prototype dans notre exemple. (Nous pourrions ajouter des méthodes de prototype spécifiques aux développeurs plus tard).
   
3. JavaScript remonte la chaîne de prototypes jusqu'au prototype de `DeveloperPersonConstructor.prototype` : `PersonConstructor.prototype`. A-t-il une propriété `greet` ? Oui. Nous avons défini `PersonConstructor.prototype.greet = function() { ... };`
   
4. JavaScript trouve `greet()` sur `PersonConstructor.prototype`, et l'exécute dans le contexte de `devPerson1` (donc `this.name` à l'intérieur de `greet()` fait référence à `devPerson1.name`).
   

Chaîne de prototypes en action. `devPerson1` -> `DeveloperPersonConstructor.prototype` -> `PersonConstructor.prototype`\- > `Object.prototype`.

### Aller encore plus loin : Développeur JavaScript

Nous pouvons même créer des chaînes d'héritage plus longues. Disons que nous voulons créer un `JavaScriptDeveloperPersonConstructor` qui est un type spécial de `DeveloperPersonConstructor`, peut-être avec une préférence spécifique pour un framework JavaScript.

Nous pouvons faire le même schéma :

```js
function JavaScriptDeveloperPersonConstructor(name, age, framework) {
  //  "Emprunte" d'abord à DeveloperPersonConstructor !
  DeveloperPersonConstructor.call(this, name, age, "JavaScript"); // "JavaScript" codé en dur
  this.framework = framework;
  this.codeJavaScript = function () {
    // Spécifique aux développeurs JavaScript
    console.log(`${this.name} est en train de coder en JavaScript avec ${this.framework}`);
  };
}

// Établir la chaîne de prototypes : JavaScriptDeveloperPerson -> DeveloperPerson -> Person
JavaScriptDeveloperPersonConstructor.prototype = Object.create(
  DeveloperPersonConstructor.prototype
);
```

Maintenant, nous avons une chaîne d'héritage à trois niveaux.

### Fonctions constructeurs : Puissantes, mais un peu... Verboses ?

Les fonctions constructeurs et les prototypes sont vraiment puissants. Ils sont le moyen fondamental pour JavaScript d'atteindre un comportement de type POO. Cependant, comme vous pouvez le voir, la configuration de l'héritage avec `call()` et `Object.create()` peut devenir un peu verbeuse et difficile à lire, surtout lorsque les chaînes d'héritage deviennent plus longues.

Et devinez quoi ? Les développeurs JavaScript l'ont également remarqué. En 2015, une nouvelle syntaxe plus propre pour créer des plans d'objets a été introduite en JavaScript.

## Entrée des classes ES6 : Sucre syntaxique pour les prototypes

Vous voyez, en 2015, les développeurs JavaScript ont reconnu que l'utilisation directe des prototypes et des fonctions constructeurs pour atteindre des motifs de type classe pouvait devenir verbeuse et moins directe à gérer à mesure que les applications grandissaient. Par conséquent, ils ont introduit la syntaxe `class` dans ECMAScript 2015 (ES6).

Les classes en JavaScript offrent une manière beaucoup plus propre et plus familière de créer des plans d'objets et de configurer l'héritage. Mais voici la chose super importante à retenir : les classes JavaScript sont toujours construites sur des prototypes. Elles ne changent pas fondamentalement le fonctionnement de la POO JavaScript. Elles sont simplement du sucre syntaxique — une manière plus agréable et plus facile d'écrire du code qui utilise toujours des prototypes en arrière-plan.

Dans la section suivante, nous verrons comment réécrire nos exemples `Person`, `DeveloperPerson`, et `JavaScriptDeveloperPerson` en utilisant la nouvelle syntaxe `class`, et vous verrez à quel point elle est plus propre et plus familière (jeu de mots intentionnel), tout en utilisant la puissance des prototypes JavaScript.

## Classes ES6 : Syntaxe de classe – Prototypes déguisés

D'accord, nous avons lutté avec les fonctions constructeurs et `call()` et `Object.create()` pour faire fonctionner l'héritage avec les prototypes. C'est puissant, mais soyons honnêtes, cela peut sembler un peu verbeux et indirect, surtout si vous êtes habitué aux langages basés sur les classes.

C'est là que les classes ES6 viennent à la rescousse. Elles offrent une syntaxe beaucoup plus rationalisée et plus proche des classes pour créer des plans d'objets en JavaScript.

Réécrivons notre exemple `PersonConstructor` en utilisant la syntaxe `class`. Préparez-vous à une bouffée d'air frais.

### `PersonClass` - Fonction constructeur réimaginée en tant que classe

Voici comment nous pouvons définir notre plan `Person` en tant que classe :

```js
class PersonClass {
  //  Utilisation du mot-clé 'class' !
  constructor(name, age) {
    //  Méthode 'constructor' - comme notre ancienne fonction constructeur
    this.name = name; //  Toujours utiliser 'this' dans le constructeur
    this.age = age;
  }

  greet() {
    console.log(`Bonjour, je suis ${this.name}`);
  }
}
```

Cela ne semble-t-il pas beaucoup plus propre et mieux organisé ? Décomposons la syntaxe de la classe :

* `class PersonClass { ... }` : Nous commençons par le mot-clé `class`, suivi du nom de la classe (`PersonClass` dans ce cas). Les noms de classe sont conventionnellement en majuscules.
  
* `constructor(name, age) { ... }` : À l'intérieur de la classe, nous avons une méthode spéciale appelée `constructor`. C'est comme notre ancienne fonction `PersonConstructor`. C'est là que nous mettons le code pour initialiser les propriétés d'un nouvel objet `PersonClass` lorsqu'il est créé avec `new`. Nous utilisons toujours `this` à l'intérieur du `constructor` pour faire référence au nouvel objet en cours de création.
  
* `greet() { ... }` : Voici comment nous définissons les méthodes dans une classe. Nous écrivons simplement le nom de la méthode (`greet`), suivi de parenthèses pour les paramètres (aucun dans ce cas), puis le corps de la méthode entre accolades. Remarquez que nous n'utilisons pas le mot-clé `function` ici. C'est simplement `greet() { ... }`.
  

### Créer des objets à partir d'une classe - Toujours en utilisant `new`

Pour créer des objets à partir de notre plan `PersonClass`, nous utilisons toujours le mot-clé `new`, tout comme nous l'avons fait avec les fonctions constructeurs :

```js
const classPerson1 = new PersonClass("Charlie", 28);
const classPerson2 = new PersonClass("Diana", 32);

console.log(classPerson1.name); // Output: Charlie
classPerson1.greet(); // Output: Bonjour, je suis Charlie
```

Oui, cela fonctionne exactement de la même manière que notre exemple de fonction constructeur, mais la syntaxe de la classe est simplement beaucoup plus lisible et moins encombrée.

### `DeveloperPersonClass` - L'héritage facilité avec `extends`

Maintenant, abordons l'héritage en utilisant des classes. Vous souvenez-vous comment nous devions utiliser `call()` et `Object.create()` pour faire en sorte que `DeveloperPersonConstructor` hérite de `PersonConstructor` ? Avec les classes, l'héritage devient super simple en utilisant le mot-clé `extends`.

Voici comment nous pouvons réécrire `DeveloperPersonConstructor` en tant que `DeveloperPersonClass` qui hérite de `PersonClass` :

```js
class DeveloperPersonClass extends PersonClass {
  //  'extends' pour l'héritage !
  constructor(name, age, programmingLanguage) {
    super(name, age); //  'super()' appelle le constructeur de la classe parente !
    this.programmingLanguage = programmingLanguage;
  }

  code() {
    // Méthode spécifique au développeur
    console.log(`${this.name} est en train de coder en ${this.programmingLanguage}`);
  }
}
```

Regardez cela. L'héritage dans les classes est déclaré en utilisant le mot-clé `extends` : `class DeveloperPersonClass extends PersonClass {...}`. Cette ligne seule dit : "Hey JavaScript, `DeveloperPersonClass` devrait hériter de `PersonClass`."

À l'intérieur du constructeur `DeveloperPersonClass`, nous avons cette ligne : `super(name, age);`. `super()` est crucial pour l'héritage des classes. C'est ainsi que nous appelons le constructeur de la classe parente (`PersonClass` dans ce cas). Lorsque nous appelons `super(name, age)`, cela revient essentiellement à faire `PersonConstructor.call(this, name, age)` dans notre exemple de fonction constructeur — cela exécute le constructeur `PersonClass` pour configurer les propriétés héritées (`name` et `age`) sur l'objet `DeveloperPersonClass`.

Après avoir appelé `super()`, nous pouvons ensuite ajouter des propriétés ou méthodes spécifiques aux développeurs à notre `DeveloperPersonClass`, comme `this.programmingLanguage = programmingLanguage;` et la méthode `code()`.

### Utilisation de `DeveloperPersonClass` - Héritage en action, syntaxe plus propre

Créons un objet `DeveloperPersonClass` et voyons l'héritage en action avec cette syntaxe plus propre :

```js
const classDevPerson1 = new DeveloperPersonClass("Eve", 35, "JavaScript");

console.log(classDevPerson1.name); // Output: Eve (Hérité de PersonClass !)
console.log(classDevPerson1.age); // Output: 35 (Hérité de PersonClass !)
classDevPerson1.greet(); // Output: Bonjour, je suis Eve (Hérité de PersonClass !)
console.log(classDevPerson1.programmingLanguage); // Output: JavaScript (Spécifique au développeur)
classDevPerson1.code(); // Output: Eve est en train de coder en JavaScript (Spécifique au développeur)
```

Cela fonctionne exactement comme prévu. `classDevPerson1` hérite de `name`, `age`, et `greet()` de `PersonClass` et a également ses propres `programmingLanguage` et méthodes `code()`. Mais la syntaxe de la classe rend la relation d'héritage beaucoup plus évidente et plus facile à utiliser.

### Classes : Sucre syntaxique, puissance des prototypes en dessous

Soyons à nouveau très clairs : les classes JavaScript sont du sucre syntaxique sur les prototypes. Elles sont une manière plus conviviale d'écrire du code qui est toujours basé sur les prototypes et les fonctions constructeurs en arrière-plan.

Lorsque vous définissez une classe, JavaScript fait en réalité ces choses pour vous en arrière-plan :

* Il crée une fonction constructeur (comme notre `PersonConstructor`).
  
* Il configure la propriété `.prototype` de cette fonction constructeur.
  
* Lorsque vous utilisez `extends`, il utilise `Object.create()` et `call()` pour configurer la chaîne de prototypes pour l'héritage.
  

Les classes ne changent pas la nature fondamentale de la POO basée sur les prototypes de JavaScript. Elles nous donnent simplement une syntaxe plus familière et moins verbeuse pour travailler avec.

### Alors, les classes sont-elles juste des "fausses" classes ?

Certaines personnes soutiennent que les classes JavaScript sont "fausses" parce qu'elles ne sont que du sucre syntaxique. Mais honnêtement, ce n'est pas du tout le propos. Le sucre syntaxique est génial — il rend notre code plus facile à lire, à écrire et à maintenir. Pour ceux qui viennent d'un arrière-plan de langage basé sur les classes, les classes rendent la programmation orientée objet en JavaScript beaucoup plus accessible et compréhensible.

Le point clé à retenir est que si les classes vous offrent une syntaxe nette et familière, vous devez toujours comprendre le mécanisme sous-jacent : les prototypes. Les classes ne sont qu'une couche conviviale au-dessus du système de prototypes de JavaScript.

## Qu'est-ce qui suit ? Plus de fonctionnalités de classe et des exemples concrets

D'accord, maintenant que vous êtes à l'aise avec l'idée des classes, il est temps de les voir en action. Comprendre la théorie n'est que la moitié de la bataille — nous avons besoin d'exemples pratiques.

Et pour solidifier votre compréhension, parcourons la construction d'un exemple classique : une application de liste de tâches de base. Bien qu'une application de liste de tâches soit encore relativement simple en concept, elle introduit suffisamment d'interaction front-end pour voir comment les classes peuvent organiser le code JavaScript front-end pour les éléments interactifs de manière gérable pour l'apprentissage.

Imaginez que vous voulez construire une application de liste de tâches très basique. De quoi avez-vous besoin pour gérer ?

* Tâches : Chaque élément de tâche a une description et un statut (fait ou non).
  
* Actions : Vous voudrez ajouter de nouvelles tâches, les marquer comme terminées, les supprimer et les lister.
  

Cela nous amène naturellement à penser à un élément "ToDo" comme un objet, et si vous créez de nombreuses tâches, une classe `ToDo` est un plan parfait.

### Configuration de vos fichiers

Avant d'écrire du code, créez deux fichiers dans le même dossier :

* `index.html` : C'est la structure de la page web.
  
* `script.js` : C'est là que votre code JavaScript avec des classes vivra.
  

Vous pouvez utiliser n'importe quel éditeur de texte (comme VS Code, Sublime Text, ou même Notepad) pour créer ces fichiers.

### Création de la classe ToDo

Commençons par construire notre classe `ToDo`. Copiez et collez le code suivant dans votre fichier `script.js` :

```javascript
class ToDo {

constructor(description) {

this.description = description; // Chaque tâche a besoin d'une description

this.completed = false; // Par défaut, elle n'est pas terminée

}

markComplete() {

this.completed = true;

console.log("${this.description}" marquée comme terminée !);

}

// Plus de méthodes (par exemple, pour éditer la tâche) peuvent être ajoutées plus tard.

}
```

Remarquez à quel point c'est propre. Le `constructor` définit la description et le statut de complétion pour chaque nouvel élément de tâche. La méthode `markComplete()` met à jour le statut et enregistre un message de confirmation.

### Construction de la classe ToDoList

Ensuite, nous allons construire une classe `ToDoList` pour gérer notre collection de tâches. Ajoutez le code suivant à votre fichier `script.js`, sous la classe `ToDo` :

```javascript
class ToDoList {

constructor() {

this.todos = []; // Commence avec un tableau vide de tâches

}

addTodo(description) {

const newTodo = new ToDo(description); // Crée un nouvel objet ToDo

this.todos.push(newTodo); // Ajoute-le à notre liste

this.renderTodoList(); // Met à jour l'affichage de la page web

}

listTodos() {

return this.todos; // Retourne le tableau des tâches (pour un traitement ou un rendu ultérieur)

}

markTodoComplete(index) {

if (index >= 0 && index < this.todos.length) {

this.todos[index].markComplete();

this.renderTodoList(); // Met à jour l'affichage après avoir marqué comme terminé

}

}

renderTodoList() {

const todoListElement = document.getElementById('todoList');

todoListElement.innerHTML = ''; // Efface la liste actuelle en HTML

this.todos.forEach((todo, index) => {

const listItem = document.createElement('li');

listItem.textContent = todo.description;

if (todo.completed) {

listItem.classList.add('completed'); // Ajoute une classe CSS pour styliser les éléments terminés

}

// Crée un bouton "Terminé" pour chaque tâche

const completeButton = document.createElement('button');

completeButton.textContent = 'Terminé';

completeButton.onclick = () => this.markTodoComplete(index);

listItem.appendChild(completeButton);

todoListElement.appendChild(listItem);

});

}

}
```

Dans cette classe :

* Le `constructor` initialise un tableau vide pour contenir nos éléments de tâche.
  
* `addTodo(description)` crée un nouvel objet `ToDo` et l'ajoute au tableau, puis appelle `renderTodoList()` pour mettre à jour l'affichage.
  
* `listTodos()` retourne la liste des tâches.
  
* `markTodoComplete(index)` marque une tâche spécifique comme terminée et rafraîchit l'affichage.
  
* `renderTodoList()` trouve l'élément HTML avec l'ID `todoList`, efface son contenu, puis crée des éléments de liste pour chaque tâche, y compris un bouton "Terminé".
  

### Création de la structure HTML

Ensuite, ouvrez votre fichier `index.html` et collez le code HTML suivant :

```javascript
<!DOCTYPE html>

<html>

<head>

  <title>Mon application de liste de tâches simple</title>

  <style>

    /* CSS simple pour styliser les éléments terminés */

    .completed {

      text-decoration: line-through;

      color: gray;

    }

  </style>

</head>

<body>

  <h1>Ma liste de tâches</h1>

  <input type="text" id="todoInput" placeholder="Entrez une nouvelle tâche...">

<button id="addButton">Ajouter une tâche</button>

  <ul id="todoList"></ul>

  <script src="script.js"></script>

</body>

</html>
```

Ce fichier HTML configure :

* Un en-tête pour votre liste de tâches.
  
* Une zone de saisie (avec `id="todoInput"`) pour entrer de nouvelles tâches.
  
* Un bouton "Ajouter une tâche" (avec `id="addButton"`).
  
* Une liste non ordonnée vide (avec `id="todoList"`) où vos tâches apparaîtront.
  
* Un lien vers le fichier `script.js` qui contient votre code JavaScript.
  

### Faire fonctionner le tout ensemble

Enfin, relions nos éléments HTML avec notre JavaScript. Au bas de votre fichier `script.js`, ajoutez ce code :

```js
const myTodoList = new ToDoList(); // Crée une instance de ToDoList

// Obtient les références aux éléments HTML

const addButton = document.getElementById("addButton");

const todoInput = document.getElementById("todoInput");

// Écoute les clics sur le bouton "Ajouter une tâche"

addButton.addEventListener("click", () => {
  const todoText = todoInput.value.trim(); // Obtient le texte de la zone de saisie

  if (todoText) {
    // N'ajoute que si la saisie n'est pas vide

    myTodoList.addTodo(todoText); // Ajoute la nouvelle tâche

    todoInput.value = ""; // Efface la zone de saisie
  }
});

// Affiche initialement la liste de tâches (elle sera vide au début)

myTodoList.renderTodoList();
```

Ce code fait ce qui suit :

* Crée une instance de la classe `ToDoList`.
  
* Trouve les éléments HTML pour la saisie et le bouton.
  
* Ce code ajoute un écouteur d'événement à l'élément bouton HTML qui a l'ID "addButton". Cet écouteur est configuré pour réagir aux événements "click" sur ce bouton. Lorsque le bouton "Ajouter une tâche" est cliqué, le code à l'intérieur de la fonction de l'écouteur d'événement sera exécuté. Ce code prend le texte que l'utilisateur a saisi dans le champ de saisie HTML avec l'ID "todoInput" et l'ajoute comme nouvel élément de tâche à notre liste.
  
* Affiche initialement la liste de tâches sur la page web.
  

%[https://codepen.io/Spruce_khalifa/pen/vEYBdQe] 

### Votre défi : Allez à la manière des prototypes

Maintenant que vous avez vu comment les classes peuvent rendre la construction de cette application de liste de tâches plus structurée, voici un défi : Essayez de construire la même application de liste de tâches sans utiliser le mot-clé `class`. Utilisez des littéraux d'objets et des prototypes à la place. Réfléchissez à :

* Comment créeriez-vous un plan "ToDo" en utilisant une fonction constructeur et des prototypes ?
  
* Comment ajouteriez-vous la méthode `markComplete()` au prototype `ToDo` ?
  
* Comment structureriez-vous un plan "ToDoList" de manière similaire ?
  

En construisant la même application en utilisant les deux approches, vous comprendrez vraiment que les classes sont simplement une manière plus agréable et plus familière d'écrire du code basé sur les prototypes.

## Conclusion

Félicitations ! Vous avez construit une application de liste de tâches basique et interactive en utilisant des classes JavaScript et HTML. Vous voyez maintenant comment les classes vous aident à organiser le code et à encapsuler les fonctionnalités connexes. Bien que les classes soient simplement du sucre syntaxique sur les prototypes, elles rendent beaucoup plus facile l'écriture, la lecture et la maintenance de votre code — surtout à mesure que vos applications grandissent.

Votre prochaine étape ? Expérimentez avec l'approche des prototypes et comparez-la avec l'approche basée sur les classes. Plus vous codez, plus ces concepts deviendront naturels. Bon codage, et continuez à construire des choses cool.

Si vous avez des questions, n'hésitez pas à me trouver sur Twitter à l'adresse [@sprucekhalifa](https://x.com/sprucekhalifa), et n'oubliez pas de me suivre pour plus de conseils et de mises à jour. Bon codage !