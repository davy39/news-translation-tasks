---
title: Apprendre TypeScript en 5 minutes - Un tutoriel pour débutants
date: '2018-07-02T16:44:56.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/learn-typescript-in-5-minutes-13eda868daeb
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_2cFbIAg4bow_0pdaBNr7Cw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: reactjs
- name: TypeScript
  slug: typescript
- name: Vue.js
  slug: vuejs
seo_desc: 'By Per Harald Borgen


  _Click here to check out the free Scrimba course on TypeScript_

  TypeScript is a typed superset of JavaScript, aimed at making the language more
  scalable and reliable.

  It’s open-source and has been maintained by Microsoft since t...'
---


Par Per Harald Borgen

<!-- more -->

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-06-at-07.58.51.png) \_[Cliquez ici pour consulter le cours gratuit de Scrimba sur TypeScript][1]\_

TypeScript est un sur-ensemble (superset) typé de JavaScript, visant à rendre le langage plus évolutif et fiable.

Il est open-source et maintenu par Microsoft depuis sa création en 2012. Cependant, TypeScript a connu sa première percée en tant que langage de programmation principal d'Angular 2. Il n'a cessé de croître depuis, notamment au sein des communautés React et Vue.

Dans ce tutoriel, vous apprendrez les bases de TypeScript à l'aide d'exemples pratiques.

**Nous sommes également sur le point de lancer un cours TypeScript gratuit en 22 parties sur Scrimba.** [**Laissez votre e-mail ici si vous voulez un accès anticipé !**][2]

C'est parti.

### Installation de TypeScript

Avant de commencer à coder, nous devons installer TypeScript sur notre ordinateur. Nous utiliserons `npm` pour cela, il suffit donc d'ouvrir le terminal et de taper la commande suivante :

```
npm install -g typescript
```

Une fois installé, nous pouvons le vérifier en exécutant la commande `tsc -v` qui affichera la version de TypeScript installée.

### Écrire du code

Créons notre premier fichier TypeScript et écrivons du code à l'intérieur. Ouvrez votre IDE ou éditeur de texte favori et créez un fichier nommé `first.ts` — Pour les fichiers TypeScript, nous utilisons l'extension `.ts`.

Pour l'instant, nous allons simplement écrire quelques lignes de JavaScript classique, car tout code JavaScript est également un code TypeScript valide :

```
let a = 5;  
let b = 5;  
let c = a + b;

console.log(c);
```

L'étape suivante consiste à compiler notre TypeScript en JavaScript classique, car les navigateurs ont besoin de fichiers `.js` pour les lire.

### Compiler TypeScript

Pour compiler, nous allons exécuter la commande `tsc filename.ts`, ce qui crée un fichier JavaScript avec le même nom de fichier mais une extension différente, que nous pourrons ensuite transmettre à nos navigateurs.

Ouvrez donc le terminal à l'emplacement du fichier et exécutez la commande suivante :

```
tsc first.ts
```

**Astuce** : Si vous souhaitez compiler tous les fichiers TypeScript d'un dossier, utilisez la commande : `tsc *.ts`

### Types de données

TypeScript — comme son nom l'indique — est la version typée de JavaScript. Cela signifie que nous pouvons spécifier des types pour différentes variables au moment de la déclaration. Elles conserveront toujours le même type de données dans cette portée.

Le typage est une fonctionnalité très utile pour garantir la fiabilité et l'évolutivité. La vérification de type (type checking) permet de s'assurer que notre code fonctionne comme prévu. De plus, cela aide à traquer les bogues et les erreurs, et à documenter correctement notre code.

La syntaxe pour assigner un type à une variable consiste à écrire le nom de la variable suivi d'un signe `:`, puis le nom du type suivi d'un signe `=` et de la valeur de la variable.

Il existe trois types différents dans TypeScript : le type `any`, les types intégrés (`Built-in`), et les types définis par l'utilisateur (`User-defined`). Jetons un coup d'œil à chacun d'eux.

#### Type any

Le type de données `any` est le sur-ensemble de tous les types de données dans TypeScript. Donner à une variable le type `any` équivaut à désactiver la vérification de type pour cette variable.

```
let myVariable: any = 'This is a string'
```

#### Types intégrés

Ce sont les types qui sont intégrés à TypeScript. Ils incluent `number`, `string`, `boolean`, `void`, `null` et `undefined`.

```
let num: number = 5;  
let name: string = 'Alex';  
let isPresent: boolean = true;
```

#### Types définis par l'utilisateur

Les types définis par l'utilisateur incluent `enum`, `class`, `interface`, `array` et `tuple`. Nous aborderons certains d'entre eux plus loin dans cet article.

### Programmation orientée objet

TypeScript prend en charge toutes les fonctionnalités de la programmation orientée objet, telles que les classes et les interfaces. Cette capacité est un énorme atout pour JavaScript — qui a toujours eu du mal avec ses fonctionnalités POO, surtout depuis que les développeurs ont commencé à l'utiliser pour des applications à grande échelle.

#### Classe

En programmation orientée objet, une classe est le modèle des objets. Une classe définit à quoi ressemblerait un objet en termes de caractéristiques et de fonctionnalités. Une classe encapsule également les données pour l'objet.

TypeScript intègre la prise en charge des classes, qui n'étaient pas supportées par ES5 et les versions antérieures. Cela signifie que nous pouvons utiliser le mot-clé `class` pour en déclarer une facilement.

```
class Car {

// fields  
  model: String;  
  doors: Number;  
  isElectric: Boolean;

constructor(model: String, doors: Number, isElectric: Boolean) {  
    this.model = model;  
    this.doors = doors;  
    this.isElectric = isElectric;  
  }

displayMake(): void {  
    console.log(`This car is ${this.model}`);  
  }

}
```

Dans l'exemple ci-dessus, nous avons déclaré une classe `Car`, avec certaines de ses propriétés que nous initialisons dans le `constructor`. Nous avons également une méthode qui affiche un message en utilisant sa propriété.

Voyons comment nous pouvons créer une nouvelle instance de cette classe :

```
const Prius = new Car('Prius', 4, true);  
Prius.displayMake(); // This car is Prius
```

Pour créer un objet d'une classe, nous utilisons le mot-clé `new`, nous appelons le constructeur de la classe et nous lui passons les propriétés. Maintenant, cet objet `Prius` possède ses propres propriétés `model`, `doors` et `isElectric`. L'objet peut également appeler la méthode `displayMake`, qui aura accès aux propriétés de `Prius`.

#### Interface

Le concept d'interface est une autre fonctionnalité puissante de TypeScript, qui vous permet de définir la structure des variables. Une interface est comme un contrat syntaxique auquel un objet doit se conformer.

Les interfaces sont mieux décrites par un exemple concret. Supposons que nous ayons un objet `Car` :

```
const Car = {  
  model: 'Prius',  
  make: 'Toyota',  
  display() => { console.log('hi'); }  
}
```

Si nous regardons l'objet ci-dessus et essayons d'en extraire la signature, elle serait :

```
{  
  model: String,  
  make: String,  
  display(): void  
}
```

Si nous voulons réutiliser cette signature, nous pouvons la déclarer sous la forme d'une interface. Pour créer une interface, nous utilisons le mot-clé `interface`.

```
interface ICar {  
  model: String,  
  make: String,  
  display(): void  
}

const Car: ICar = {  
  model: 'Prius',  
  make: 'Toyota',  
  display() => { console.log('hi'); }  
}
```

Ici, nous avons déclaré une interface appelée `ICar` et créé un objet `Car`. `Car` est maintenant lié à l'interface `ICar`, garantissant que l'objet `Car` définit toutes les propriétés présentes dans l'interface.

### Conclusion

J'espère que cela vous a donné un aperçu rapide de la manière dont TypeScript peut rendre votre JavaScript plus stable et moins sujet aux bogues.

TypeScript gagne beaucoup de terrain dans le monde du développement web. Il y a également un nombre croissant de développeurs React qui l'adoptent. TypeScript est définitivement quelque chose dont tout développeur front-end en 2018 devrait avoir connaissance.

Bon code :)

---

Merci de votre lecture ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba][3] – le moyen le plus simple d'apprendre à coder. Vous devriez consulter notre [bootcamp de responsive web design][4] si vous voulez apprendre à construire des sites web modernes à un niveau professionnel.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png) \_[Cliquez ici pour accéder au bootcamp avancé.][5]\_

[1]: https://scrimba.com/p/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_5_minute_article
[2]: http://eepurl.com/dyqJAj
[3]: https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_5_minute_article
[4]: https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_5_minute_article
[5]: https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_5_minute_article