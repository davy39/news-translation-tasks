---
title: Non, les Getters et Setters en TypeScript & JavaScript ne sont pas inutiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-04T20:13:08.000Z'
originalURL: https://freecodecamp.org/news/typescript-javascript-getters-and-setters-are-they-useless
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/typescript-blog-banner-1.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Non, les Getters et Setters en TypeScript & JavaScript ne sont pas inutiles
seo_desc: 'By Khalil Stemmler


  In this blog post, we talk about the utility of getters and setters in modern web
  development. Are they useless? When does it make sense to use them?


  Getters and setters (also known as accessors) were introduced to JavaScript whe...'
---

Par Khalil Stemmler

> Dans cet article de blog, nous parlons de l'utilité des getters et setters dans le développement web moderne. Sont-ils inutiles ? Quand est-il judicieux de les utiliser ?

Les getters et setters (également connus sous le nom d'accesseurs) ont été introduits en JavaScript avec la sortie d'ECMAScript 5 (2009).

Le problème, c'est qu'il y a beaucoup de confusion sur leur utilité et pourquoi vous voudriez jamais les utiliser.

Je suis tombé sur ce [fil Reddit](https://www.reddit.com/r/typescript/comments/87t1h7/are_getters_and_setters_an_antipattern/) où la discussion portait sur le fait de savoir s'ils étaient un anti-pattern.

Malheureusement, le consensus général du fil était "oui". Je pense que c'est parce que la majorité de votre programmation front-end au quotidien n'appelle pas à l'utilité que les getters et setters offrent.

Bien que je ne sois pas d'accord avec le fait que les getters et setters soient un anti-pattern _de manière générale_. Ils ont beaucoup d'utilité dans plusieurs cas différents.

## À quoi servent-ils ?

Les getters et setters sont une autre façon pour vous de fournir un accès aux propriétés d'un objet.

Une utilisation triviale pourrait ressembler à ceci :

```typescript
interface ITrackProps {
  name: string;
  artist: string;
}

class Track {  
  private props: ITrackProps;

  get name (): string {
    return this.props.name;
  }

  set name (name: string) {
	  this.props.name = name;
  }

  get artist (): string {
    return this.props.artist;
  }

  set artist (artist: string) {
	  this.props.artist = artist;
  }

  constructor (props: ITrackProps) {
    this.props = props;
  } 

  public play (): void {	
	  console.log(`Playing ${this.name} by ${this.artist}`);
  }
}
```

La question devient : "pourquoi ne pas simplement utiliser des attributs de classe réguliers ?"

Eh bien, dans ce cas, _nous pourrions_.

```typescript
interface ITrackProps {
  name: string;
  artist: string;
}

class Track {  
  public name: string;
  public artist: string;

  constructor (name: string, artist: string;) {
    this.name = name;
    this.artist = artist;
  } 

  public play (): void {	
	  console.log(`Playing ${this.name} by ${this.artist}`);
  }
}
```

C'est beaucoup plus simple. Et c'est aussi un cas d'utilisation vraiment simple. Regardons des scénarios qui décrivent mieux pourquoi nous pourrions nous soucier d'utiliser des getters et setters par rapport aux attributs de classe réguliers.

## Prévenir les modèles de domaine anémiques

Vous vous souvenez de ce qu'est un [modèle de domaine anémique](https://khalilstemmler.com/wiki/anemic-domain-model/) ? L'une des premières façons de détecter un modèle de domaine anémique est s'il y a des getters et setters pour **chaque attribut** de vos entités de domaine (c'est-à-dire : des opérations de _set_ qui n'ont pas de sens dans le langage spécifique au domaine sont exposées).

Et si vous n'utilisez pas explicitement les mots-clés `get` ou `set`, rendre tout `public` a également le même effet négatif.

Considérez cet exemple :

```javascript
class User {
  // Mauvais. Vous pouvez maintenant `set` l'identifiant de l'utilisateur.
  // Quand auriez-vous besoin de muter l'identifiant d'un utilisateur vers un
  // autre identifiant ? Est-ce sûr ? Devriez-vous pouvoir le faire ?
  public id: UserId;

  constuctor (id: UserId) {
    this.id = id;
  }
}
```

En Domain-Driven Design, pour prévenir un modèle de domaine anémique et favoriser la création d'un langage spécifique au domaine, il est <u>vraiment</u> important pour nous de _ne exposer que les opérations qui sont valides pour le domaine_.

Cela signifie [comprendre le domaine dans lequel vous travaillez](https://khalilstemmler.com/articles/solid-principles/single-responsibility/).

Je vais me mettre sous les projecteurs. Examinons la classe `Vinyl` de [White Label](https://github.com/stemmlerjs/white-label), une application open-source d'échange de vinyles construite avec TypeScript en utilisant le Domain-Driven Design.

```typescript
import { AggregateRoot } from "../../core/domain/AggregateRoot";
import { UniqueEntityID } from "../../core/domain/UniqueEntityID";
import { Result } from "../../core/Result";
import { Artist } from "./artist";
import { Genre } from "./genre";
import { TraderId } from "../../trading/domain/traderId";
import { Guard } from "../../core/Guard";
import { VinylCreatedEvent } from "./events/vinylCreatedEvent";
import { VinylId } from "./vinylId";

interface VinylProps {
  traderId: TraderId;
  title: string;
  artist: Artist;
  genres: Genre[];
  dateAdded?: Date;
}

export type VinylCollection = Vinyl[];

export class Vinyl extends AggregateRoot<VinylProps> {

  public static MAX_NUMBER_GENRES_PER_VINYL = 3;

  // ? 1. Façade. La clé VinylId n'existe pas réellement
  // en tant que propriété de VinylProps, pourtant nous devons
  // toujours fournir un accès à celle-ci.

  get vinylId(): VinylId {
    return VinylId.create(this.id)
  }

  get title (): string {
    return this.props.title;
  }

  // ? 2. Toutes ces propriétés sont imbriquées à un niveau
  // profond en tant que props afin que nous puissions contrôler l'accès
  // et les mutations des VALEURS RÉELLES.

  get artist (): Artist {
    return this.props.artist
  }

  get genres (): Genre[] {
    return this.props.genres;
  }

  get dateAdded (): Date {
    return this.props.dateAdded;
  }

  // ? 3. Vous remarquerez qu'il n'y a pas de setters jusqu'à présent car
  // il n'a pas de sens pour nous de pouvoir changer l'une de ces
  // choses après qu'elles aient été créées

  get traderId (): TraderId {
    return this.props.traderId;
  }

  // ? 4. Cette approche est appelée "Encapsulate Collection". Nous
  // devrons ajouter des genres, oui. Mais nous n'exposons toujours pas le
  // setter car il y a une logique d'invariant ici que nous voulons
  // nous assurer d'appliquer.
  // Invariants :
  // https://khalilstemmler.com/wiki/invariant/

  public addGenre (genre: Genre): void {
    const maxLengthExceeded = this.props.genres
      .length >= Vinyl.MAX_NUMBER_GENRES_PER_VINYL;

    const alreadyAdded = this.props.genres
      .find((g) => g.id.equals(genre.id));

    if (!alreadyAdded && !maxLengthExceeded) {
      this.props.genres.push(genre);
    }
  }

  // ? 5. Fournir un moyen de supprimer également.

  public removeGenre (genre: Genre): void {
    this.props.genres = this.props.genres
      .filter((g) => !g.id.equals(genre.id));
  }

  private constructor (props: VinylProps, id?: UniqueEntityID) {
    super(props, id);
  }

  // ? 6. Voici comment nous créons Vinyl. Après sa création, toutes les propriétés
  // deviennent effectivement "en lecture seule", sauf pour Genre car c'est tout ce
  // qui a du sens à être activé pour être muté.

  public static create (props: VinylProps, id?: UniqueEntityID): Result<Vinyl> {
    const propsResult = Guard.againstNullOrUndefinedBulk([
      { argument: props.title, argumentName: 'title' },
      { argument: props.artist, argumentName: 'artist' },
      { argument: props.genres, argumentName: 'genres' },
      { argument: props.traderId, argumentName: 'traderId' }
    ]);

    if (!propsResult.succeeded) {
      return Result.fail<Vinyl>(propsResult.message)
    } 

    const vinyl = new Vinyl({
      ...props,
      dateAdded: props.dateAdded ? props.dateAdded : new Date(),
      genres: Array.isArray(props.genres) ? props.genres : [],
    }, id);
    const isNewlyCreated = !!id === false;

    if (isNewlyCreated) {
      // ? 7. Voici pourquoi nous avons besoin de VinylId. Pour fournir l'identifiant
      // pour tout abonné à cet événement de domaine.
      vinyl.addDomainEvent(new VinylCreatedEvent(vinyl.vinylId))
    }

    return Result.ok<Vinyl>(vinyl);
  }
}
```

Agir en tant que façade, maintenir des valeurs en lecture seule, renforcer l'expressivité du modèle, encapsuler les collections, ET [créer des événements de domaine](https://khalilstemmler.com/blogs/domain-driven-design/where-do-domain-events-get-dispatched/) sont quelques cas d'utilisation très solides pour les getters et setters en [Domain-Driven Design](https://khalilstemmler.com/articles/domain-driven-design-intro/).

## Détection de changement dans Vue.js

[Vue.js](https://vuejs.org/v2/guide/reactivity.html), l'un des nouveaux frameworks front-end, se targue d'être très rapide et réactif.

La raison pour laquelle Vue.js effectue la détection de changement si efficacement est parce qu'ils utilisent l'API `Object.defineProperty()` [API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty) pour _surveiller_ les changements dans vos View Models !

D'après la documentation de Vue.js sur la Réactivité,

> Lorsque vous passez un objet JavaScript simple à une instance Vue en tant qu'option de données, Vue parcourra toutes ses propriétés et les convertira en getters/setters en utilisant Object.defineProperty. Les getters/setters sont invisibles pour l'utilisateur, mais sous le capot, ils permettent à Vue d'effectuer le suivi des dépendances et la notification de changement lorsque les propriétés sont accédées ou modifiées. - [Vue.js Docs : Réactivité](https://vuejs.org/v2/guide/reactivity.html)

---

En conclusion, les getters et setters _ont_ beaucoup d'utilité pour beaucoup de problèmes différents. Ces problèmes ne se posent simplement pas beaucoup dans le développement web front-end moderne.

--

## Blog avancé sur TypeScript & Node.js

Si vous avez aimé cet article, vous devriez [consulter mon blog](https://khalilstemmler.com). J'écris sur les **meilleures pratiques avancées de TypeScript & Node.js pour les applications à grande échelle** et j'enseigne aux développeurs comment écrire des logiciels flexibles et maintenables.