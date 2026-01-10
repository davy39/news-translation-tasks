---
title: Tout sur les membres statiques de TypeScript | TypeScript OOP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-09T12:28:44.000Z'
originalURL: https://freecodecamp.org/news/all-about-typescript-static-members-typescript-oop
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/typescript-blog-banner-2.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: TypeScript
  slug: typescript
seo_title: Tout sur les membres statiques de TypeScript | TypeScript OOP
seo_desc: 'By Khalil Stemmler

  In Object-Oriented Programming, we write a lot of classes.

  Classes contain properties (methods and attributes) which hold variables and operations.

  Every time we define the properties of a class, they are said to belong to either:

  ...'
---

Par Khalil Stemmler



En programmation orientée objet, <u>nous écrivons beaucoup de _classes_</u>.

Les classes contiennent des _propriétés_ (**méthodes** et **attributs**) qui détiennent des variables et des opérations.

Chaque fois que nous définissons les propriétés d'une classe, on dit qu'elles appartiennent soit à :

- une _instance_ de la classe (un objet créé via le constructeur) OU
- la classe _elle-même_ (nous appelons cela un membre de classe)

_Que voulons-nous dire par là ?_

Comment les propriétés peuvent-elles appartenir uniquement à l'_instance_ ou uniquement à la _classe_ ?

Lorsque nous choisissons d'utiliser ou d'omettre le mot-clé `static`, cela change à qui les propriétés appartiennent.

Regardons l'utilisation régulière sans le mot-clé `static`.

## Utilisation régulière (les propriétés appartiennent à l'instance)

Normalement, lorsque nous définissons des propriétés sur une classe, le seul moment où elles peuvent être _accessibles_ est **après** avoir créé une instance de cette classe ou si nous utilisons `this` pour faire référence aux propriétés qui résideront finalement sur une instance de l'objet.

Prenons cet exemple précoce de [White Label](https://github.com/stemmlerjs/white-label).

```typescript
type Genre = 'rock' | 'pop' | 'electronic' | 'rap'

class Vinyl {
  public title: string;
  public artist: string;
  public genres: Genre[];

  constructor (title: string, artist: string, genres: Genre[]) {
    this.title = title;
    this.artist = artist;
    this.genres = genres;
  } 

  public printSummary (): void {
    console.log(`${this.title} is an album by ${this.artist}`);
  }
}

const vinyl = new Vinyl('Goo', 'Sonic Youth', ['rock']);
console.log(vinyl.title)    // 'Goo'
console.log(vinyl.artist)   // 'Sonic Youth'
console.log(vinyl.genres)   // ['rock']
vinyl.printSummary();	      // 'Goo is an album by Sonic Youth'
```

Chacune des méthodes (`printSummary(): void`) et des attributs (`title`, `artist`, `genres`) de la classe `Vinyl` sont dites appartenir à une _instance_ de la classe.

Dans l'exemple, nous n'avons pu accéder aux propriétés `title`, `artist` et `genres` directement depuis l'objet qu'_après_ sa création.

```typescript
console.log(vinyl.title)    // Cela est valide !
```

Notez également que lorsque nous utilisons `printSummary(): void`, nous pouvons accéder à `title` et `artist` en utilisant le mot-clé `this` :

```typescript
class Vinyl {
  ...
  public printSummary (): void {
    console.log(`${this.title} is an album by ${this.artist}`);
  }
}
```

Cela fonctionne parce qu'à ce stade, l'objet résultant / l'instance de `Vinyl` possède ces propriétés.

Si nous consultons [TypeScript Playground](http://www.typescriptlang.org/play/), nous pouvons voir le JavaScript compilé pour cet exemple de code :

```javascript
"use strict";
class Vinyl {
  constructor(title, artist, genres) {
    this.title = title;
    this.artist = artist;
    this.genres = genres;
  }
  printSummary() {
    console.log(`${this.title} is an album by ${this.artist}`);
  }
}

const vinyl = new Vinyl('Goo', 'Sonic Youth', ['rock']);
console.log(vinyl.title); // 'Goo'
console.log(vinyl.artist); // 'Sonic Youth'
console.log(vinyl.genres); // ['rock']
vinyl.printSummary(); // 'Goo is an album by Sonic Youth'
```

Le JavaScript résultant semble _presque identique_.

Parlons un peu de ce qui se passe lorsque les propriétés sont détenues par la _classe_.

## Propriétés statiques (les propriétés appartiennent à la classe)

Lorsque nous utilisons le mot-clé `static` sur les propriétés que nous définissons sur une classe, elles appartiennent à _la classe elle-même_.

Cela signifie que nous <u>ne pouvons pas</u> accéder à ces propriétés à partir d'une instance de la classe.

Nous ne pouvons accéder aux propriétés qu'en référençant directement la classe elle-même.

Pour démontrer, ajoutons un compteur `NUM_VINYL_CREATED` qui incrémente le nombre de fois qu'un `Vinyl` a été créé.

```typescript
type Genre = 'rock' | 'pop' | 'electronic' | 'rap'

class Vinyl {
  public title: string;
  public artist: string;
  public genres: Genre[];
  public static NUM_VINYL_CREATED: number = 0;

  constructor (title: string, artist: string, genres: Genre[]) {
    this.title = title;
    this.artist = artist;
    this.genres = genres;

	  Vinyl.NUM_VINYL_CREATED++;        // incrémente le nombre de vinyl créés
    console.log(Vinyl.NUM_VINYL_CREATED)  
  } 

  public printSummary (): void { 
    console.log(`${this.title} is an album by ${this.artist}`);
  }
}

let goo = new Vinyl ('Goo', 'Sonic Youth', ['rock']);
// affiche 0

let daydream = new Vinyl ('Daydream Nation', 'Sonic Youth', ['rock']);
// affiche 1
```

Parce que les propriétés ne peuvent être accessibles que par la classe elle-même, nous ne pouvons pas faire :

```typescript
let goo = new Vinyl ('Goo', 'Sonic Youth', ['rock']);
goo.MAX_GENRES_PER_VINYL    // Erreur
goo.NUM_VINYL_CREATED       // Erreur
```

Vous avez peut-être entendu parler d'un terme appelé **Class Members**. Un attribut ou une méthode est un _membre de classe_ parce qu'ils ne peuvent être accessibles que par la classe elle-même ; par conséquent, ils sont membres de la classe.

C'est bien et tout, mais _quand voudriez-vous utiliser des propriétés statiques ?_

## Comment savoir quand utiliser les propriétés statiques

Avant d'ajouter cet attribut ou cette méthode, demandez-vous :

> Cette propriété devra-t-elle jamais être utilisée par une autre classe, sans avoir une instance de _cette_ classe ?

En d'autres termes, devrais-je avoir besoin de l'appeler sur un **objet** créé par cette classe ? Si oui, alors continuez normalement.

Si non, alors vous voudrez peut-être faire un membre `static`.

### Scénarios où cela pourrait avoir du sens d'utiliser une propriété statique

- pour vérifier une règle ou une contrainte métier depuis une autre classe
- pour implémenter une `méthode de fabrication` afin [d'encapsuler la complexité](https://khalilstemmler.com/articles/typescript-value-object/) requise pour créer une instance de la classe
- pour utiliser une `fabrique abstraite` afin [de créer un type spécifique d'instance de la classe](https://khalilstemmler.com/wiki/abstract-factory/)
- lorsque la propriété ne devrait jamais changer

### Scénarios où cela _semble_ avoir du sens mais conduit en réalité à un [modèle de domaine anémique](https://khalilstemmler.com/wiki/anemic-domain-model/) :

- pour effectuer une logique de validation sur les attributs de cette classe (utilisez [Value Objects](https://khalilstemmler.com/articles/typescript-value-object/) à la place)

Pour démontrer un scénario valable, ajoutons un attribut `static` `MAX_GENRES_PER_VINYL` pour "documenter une contrainte" qu'un `Vinyl` peut avoir au maximum 2 types différents de `Genres`.

```typescript
type Genre = 'rock' | 'pop' | 'electronic' | 'rap'

class Vinyl {
  public title: string;
  public artist: string;
  public genres: Genre[];
  public static MAX_GENRES_PER_VINYL: number = 2;

  constructor (title: string, artist: string, genres: Genre[]) {
    this.title = title;
    this.artist = artist;
    this.genres = genres;
  }

  public printSummary (): void { 
    console.log(`${this.title} is an album by ${this.artist}`);
  }
}
```

Puis ajoutons une méthode `addGenre(genre: Genre): void` pour appliquer cette règle métier.

```typescript 
type Genre = 'rock' | 'pop' | 'electronic' | 'rap'

class Vinyl {
  public title: string;
  public artist: string;
  public genres: Genre[];
  public static MAX_GENRES_PER_VINYL: number = 2;

  constructor (title: string, artist: string, genres: Genre[]) {
    this.title = title;
    this.artist = artist;
    this.genres = genres;
  }

  public addGenre (genre: Genre): void {
    // Remarquez que pour référencer la valeur, nous devons passer par la classe
    // elle-même (Vinyl), et non par une instance de la classe (this).
    const maxLengthExceeded = this.genres.length < Vinyl.MAX_GENRES_PER_VINYL;
    const alreadyAdded = this.genres.filter((g) => g === genre).length !== 0;

    if (!maxLengthExceeded && !alreadyAdded) {
      this.genres.push(genre);
    }
  }

  public printSummary (): void { 
    console.log(`${this.title} is an album by ${this.artist}`);
  }
}
```


---

## Blog avancé sur TypeScript & Node.js

Si vous avez aimé cet article, vous devriez [consulter mon blog](https://khalilstemmler.com). J'écris sur **les meilleures pratiques avancées de TypeScript & Node.js pour les applications à grande échelle** et j'enseigne aux développeurs comment écrire des logiciels flexibles et maintenables.