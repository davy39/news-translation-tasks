---
title: Rendez vos composants React excellents avec les types mappés et conditionnels
  de TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T16:36:21.000Z'
originalURL: https://freecodecamp.org/news/make-react-components-great-again-with-typescript-mapped-and-conditional-types-fa729bfc1a79
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ypWl28F8NnBdxQaWIDm-YQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Rendez vos composants React excellents avec les types mappés et conditionnels
  de TypeScript
seo_desc: 'By Deepu K Sasidharan

  You’ve probably heard about TypeScript. You may have heard someone claiming how
  great type safety is.

  TypeScript is great. As someone who hates transpiling his code, I would definitely
  do it with TypeScript if I had to. So much ...'
---

Par Deepu K Sasidharan

Vous avez probablement entendu parler de TypeScript. Peut-être avez-vous entendu quelqu'un vanter les mérites de la sécurité des types.

TypeScript est formidable. En tant que personne qui déteste transpiler son code, je le ferais définitivement avec TypeScript si je devais le faire. Tant de choses ont été dites sur TypeScript, et il n'y a vraiment rien de nouveau que je puisse ajouter. Mais je crois que la sécurité des types ne consiste pas à rendre votre code laid avec des définitions de types partout. Alors, comment pouvons-nous écrire du code typé sans avoir à disperser des déclarations de types partout ?

L'inférence de type et les fonctionnalités avancées comme les types dérivés et dynamiques sont la réponse. Les éditeurs et IDE que nous utilisons sont suffisamment intelligents pour gérer le code avec un type inféré de manière élégante sans que nous ayons à voir les types tout le temps visuellement. (Bien sûr, ils montrent généralement le type lorsque vous survolez un type inféré.)

TypeScript a une très bonne inférence de type. En règle générale, vous pouvez toujours commencer sans déclarer le type pour aucune variable et voir si le compilateur l'infère. Avec des éditeurs modernes comme VSCode, vous pouvez voir cela immédiatement. Alors configurez votre tsconfig en mode strict. Ensuite, commencez à déclarer les types lorsque le compilateur se plaint.

De plus, TypeScript 2.1 et 2.8 ont introduit un ensemble de types de recherche cool. Maintenant, vous pouvez inférer dynamiquement des types en utilisant différentes techniques comme les types d'intersection, les types d'union, les types d'index, les types mappés et les types conditionnels.

### Types d'index

Les types d'index nous permettent de vérifier les propriétés et les types d'une interface ou d'un type dynamiquement en utilisant `keyof T` (**opérateur de requête de type d'index**) et `T[K]` (**opérateur d'accès indexé**). Prenons l'interface suivante comme exemple.

```ts
interface Person {
  name: string;
  age: number;
  address: string;
  sayHi: (msg: string) => string;
}
```

L'opérateur `keyof T` obtient un type d'union de tous les noms de clés du type `T` et donc `keyof Person` nous donnera `'name' | 'age' | 'address' | sayHi'` comme résultat.

L'opérateur `T[K]` obtient le type pour la clé fournie. `Person['name']` résultra en `string` et `Person[keyof Person]` résultra en `string | number | ((msg: string) => string)`.

### Types mappés

Voyons ce que sont les types mappés. Supposons que nous avons l'interface suivante pour une Person.

```ts
interface Person {
  name: string;
  age: number;
  address: string;
  sayHi: (msg: string) => string;
}
```

Dans chaque projet, il est presque toujours une exigence commune d'avoir des variations d'une certaine interface. Par exemple, disons que nous avons besoin d'une version en lecture seule de la personne comme ci-dessous.

```ts
interface ReadonlyPerson {
  readonly name: string;
  readonly age: number;
  readonly address: string;
  readonly sayHi: (msg: string) => string;
}
```

Dans ce cas, nous devrions répliquer l'interface Person et nous devons les maintenir en synchronisation manuellement. C'est là que les types mappés seront utiles, alors utilisons le type mappé intégré, `Readonly`, pour cela.

```ts
type ReadonlyPerson  = Readonly<Person>
```

Si vous survolez le type `ReadonlyPerson`, vous pouvez voir le type inféré comme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GLnLx-iMscyEMe9BQqCazg.png)
_Vue du type inféré dans VsCode_

C'est cool, n'est-ce pas ? Maintenant, nous pouvons créer des types à partir de types existants et nous n'avons pas à nous soucier de les maintenir en synchronisation. Comment cela fonctionne-t-il, que fait `Readonly<Person>` ? Jetons un coup d'œil au type mappé.

```ts
type Readonly<T> = {
    readonly [K in keyof T]: T[K];
}
```

L'opérateur `in` de TypeScript fait le tour ici. Il mappe toutes les déclarations du type existant dans le nouveau type. L'opérateur `keyof` fournit les clés de notre type pour le mappage. Construisons notre propre type mappé.

Disons que nous avons besoin d'une interface Person en lecture seule où tous les champs sont également nullables. Nous pouvons construire un type mappé comme ci-dessous pour cela.

```ts
type ReadonlyNullablePerson = {
    readonly [P in keyof Person]: Person[P] | null;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*R24n6ufx4STh96tfldlgJw.png)

Rendons-le générique afin qu'il puisse être utilisé avec n'importe quelle interface.

```ts
type ReadonlyNullable<T> = {
    readonly [K in keyof T]: T[K] | null;
}

type ReadonlyNullablePerson  = ReadonlyNullable<Person>
```

TypeScript inclut `Readonly<T>`, `Partial<T>`, `Pick<T, K extends keyof T>` et `Record<K extends string, T>` comme types mappés intégrés. Pick et Record peuvent être utilisés comme ci-dessous, vérifiez-les dans votre éditeur pour voir quels types ils produisent.

```ts
type PersonMinimal = Pick<Person, 'name' | 'age'>

type RecordedPerson = Record<'name' | 'address', string>
```

Pour tous les autres cas d'utilisation, vous pouvez construire vos propres types mappés.

### Types conditionnels

> Un type conditionnel sélectionne l'un des deux types possibles en fonction d'une condition exprimée comme un test de relation de type.

Regardons un exemple.

```ts
type Foo<T, U> = T extends U ? string : boolean

interface Me {}
interface You extends Person {}

type FooBool = Foo<Me, Person> // résultra en boolean
type FooString = Foo<You, Person> // résultra en string
```

Le type dynamiquement inféré de `Foo<T, U>` sera soit `string` soit `boolean` selon ce que le premier générique est étendu.

Voyons comment nous pouvons mélanger les types conditionnels avec les types mappés pour inférer un nouveau type de Person qui n'inclut que les propriétés non-fonction.

```ts
type NonFunctionPropNames<T> = {
  [K in keyof T]: T[K] extends Function ? never : K
}[keyof T];

type NonFunctionProps<T> = Pick<T, NonFunctionPropNames<T>>

type PersonProps = NonFunctionProps<Person>

// Produit le type ci-dessous
// type PersonProps = {
//     name: string;
//     age: number;
//     address: string;
// }
```

Nous obtenons d'abord tous les noms de propriétés non-fonction de l'interface. Ensuite, nous utilisons le type mappé **Pick** pour les sélectionner dans l'interface afin de former la nouvelle interface.

TypeScript fournit les types conditionnels intégrés suivants :

* `Exclude<T, U>` – Exclure de `T` les types qui sont assignables à `U`.
* `Extract<T, U>` – Extraire de `T` les types qui sont assignables à `U`.
* `NonNullable<T>` – Exclure `null` et `undefined` de `T`.
* `ReturnType<T>` – Obtenir le type de retour d'un type de fonction.
* `InstanceType<T>` – Obtenir le type d'instance d'un type de fonction constructeur.

### Mettons cela en pratique

Ces types avancés deviennent encore plus puissants lorsque vous les combinez ensemble. Voyons quelques utilisations pratiques de cela dans React.

#### Composant React et réducteur Redux en ES6

Regardons un simple composant React avec un réducteur écrit en ES6. Jetez un coup d'œil à **_index.jsx_** dans le bac à sable de code ci-dessous :

%[https://codesandbox.io/s/40n3y52qlx?from-embed]

Comme vous pouvez le voir, nous utilisons la bibliothèque prop-types pour définir les props du composant. Ce n'est pas la méthode la plus efficace, car elle inclut un overhead considérable pendant le développement. Elle ne fournit pas une sécurité de type complète de toute façon.

#### Composant React et réducteur Redux en TypeScript

Maintenant, convertissons cet exemple simple en TypeScript pour qu'il soit typé. Jetez un coup d'œil à **_index.tsx_** dans le bac à sable de code ci-dessous :

%[https://codesandbox.io/s/znv36k09op?from-embed]

Comme vous pouvez le voir, le code est maintenant plus typé. Il est également beaucoup plus verbeux même sans la bibliothèque PropTypes et toute l'inférence de type.

#### Composant React et réducteur Redux en TypeScript avec des types avancés

Maintenant, appliquons les types avancés que nous avons appris pour rendre cet exemple moins verbeux et encore plus typé. Jetez un coup d'œil à **_index.tsx_** dans le bac à sable de code ci-dessous :

%[https://codesandbox.io/s/zq7w69p57x?from-embed]

Comme vous pouvez le voir, nous avons utilisé `Readonly` et `ReturnType` mapping ainsi que quelques autres techniques d'inférence de type pour écrire une version plus typée mais moins verbeuse du composant.

### Conclusion

Si vous utilisez React avec TypeScript, ce sont quelques-unes des techniques que vous devez appliquer. Si vous envisagez un système de types pour React, ne cherchez pas plus loin que TypeScript. Il a de grandes fonctionnalités, de grands outils, un excellent support IDE/Éditeur et une communauté géniale.

J'ai donné une conférence sur TypeScript pour Devoxx 2018, et vous pouvez voir la vidéo et les diapositives si vous le souhaitez ici.

%[https://www.youtube.com/watch?v=SBwGH4kbkms]

%[https://speakerdeck.com/deepu105/why-you-should-love-typescript-a-practical-guide]

Consultez mon livre "Développement Full Stack avec JHipster" sur [Amazon](https://www.amazon.com/Stack-Development-JHipster-Deepu-Sasidharan/dp/178847631X) et [Packt](https://www.packtpub.com/application-development/full-stack-development-jhipster) si vous souhaitez apprendre le développement Full stack avec une pile géniale.

Si vous aimez JHipster, n'oubliez pas de lui donner une étoile sur [Github](https://github.com/jhipster/generator-jhipster).

Si vous aimez cet article, veuillez laisser quelques applaudissements (Saviez-vous que vous pouvez applaudir plusieurs fois ? ? )

Vous pouvez me suivre sur [Twitter](https://twitter.com/deepu105) et [LinkedIn](https://www.linkedin.com/in/deepu05/).