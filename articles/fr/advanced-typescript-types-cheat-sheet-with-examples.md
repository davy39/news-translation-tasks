---
title: Guide des types avancés de TypeScript (avec exemples)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-15T17:42:45.000Z'
originalURL: https://freecodecamp.org/news/advanced-typescript-types-cheat-sheet-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/cover.png
tags:
- name: TypeScript
  slug: typescript
seo_title: Guide des types avancés de TypeScript (avec exemples)
seo_desc: 'By Ibrahima Ndaw

  TypeScript is a typed language that allows you to specify the type of variables,
  function parameters, returned values, and object properties.

  Here an advanced TypeScript Types cheat sheet with examples.

  Let''s dive in.


  Intersection T...'
---

Par Ibrahima Ndaw

TypeScript est un langage typé qui permet de spécifier le type des variables, des paramètres de fonction, des valeurs retournées et des propriétés d'objet.

Voici un guide des types avancés de TypeScript avec des exemples.

*Commençons.*

* [Types d'intersection](#heading-types-dintersection)
* [Types d'union](#heading-types-dunion)
* [Types génériques](#heading-types-generiques)
* [Types utilitaires](#heading-types-utilitaires)
* [Partial](#heading-partial)
* [Required](#heading-required)
* [Readonly](#heading-readonly)
* [Pick](#heading-pick)
* [Omit](#heading-omit)
* [Extract](#heading-extract)
* [Exclude](#heading-exclude)
* [Record](#heading-record)
* [NonNullable](#heading-nonnullable)
* [Types mappés](#heading-types-mappes)
* [Garde de types](#heading-garde-de-types)
* [Types conditionnels](#heading-types-conditionnels)

## Types d'intersection

Un type d'intersection est un moyen de combiner plusieurs types en un seul. Cela signifie que vous pouvez fusionner un type A donné avec un type B ou plus et obtenir un seul type avec toutes les propriétés.

```ts
type LeftType = {
  id: number
  left: string
}

type RightType = {
  id: number
  right: string
}

type IntersectionType = LeftType & RightType

function showType(args: IntersectionType) {
  console.log(args)
}

showType({ id: 1, left: "test", right: "test" })
// Output: {id: 1, left: "test", right: "test"}

```

Comme vous pouvez le voir, `IntersectionType` combine deux types - `LeftType` et `RightType` et utilise le signe `&` pour construire le type d'intersection.

## Types d'union

Les types d'union permettent d'avoir différentes annotations de types au sein d'une variable donnée.

```ts
type UnionType = string | number

function showType(arg: UnionType) {
  console.log(arg)
}

showType("test")
// Output: test

showType(7)
// Output: 7

```

La fonction `showType` est un type d'union qui accepte à la fois des chaînes de caractères et des nombres comme paramètre.

## Types génériques

Un type générique est un moyen de réutiliser une partie d'un type donné. Il aide à capturer le type `T` passé en paramètre.

```ts
function showType<T>(args: T) {
  console.log(args)
}

showType("test")
// Output: "test"

showType(1)
// Output: 1

```

Pour construire un type générique, vous devez utiliser les crochets et passer `T` comme paramètre.  
Ici, j'utilise `T` (le nom est à votre convenance) et ensuite, j'appelle la fonction `showType` deux fois avec différentes annotations de type car elle est générique - elle peut être réutilisée.

```ts
interface GenericType<T> {
  id: number
  name: T
}

function showType(args: GenericType<string>) {
  console.log(args)
}

showType({ id: 1, name: "test" })
// Output: {id: 1, name: "test"}

function showTypeTwo(args: GenericType<number>) {
  console.log(args)
}

showTypeTwo({ id: 1, name: 4 })
// Output: {id: 1, name: 4}

```

Ici, nous avons un autre exemple qui a une interface `GenericType` qui reçoit un type générique `T`. Et comme il est réutilisable, nous pouvons l'appeler d'abord avec une chaîne de caractères puis avec un nombre.

```ts
interface GenericType<T, U> {
  id: T
  name: U
}

function showType(args: GenericType<number, string>) {
  console.log(args)
}

showType({ id: 1, name: "test" })
// Output: {id: 1, name: "test"}

function showTypeTwo(args: GenericType<string, string[]>) {
  console.log(args)
}

showTypeTwo({ id: "001", name: ["This", "is", "a", "Test"] })
// Output: {id: "001", name: Array["This", "is", "a", "Test"]}

```

Un type générique peut recevoir plusieurs arguments. Ici, nous passons deux paramètres : `T` et `U`, puis nous les utilisons comme annotations de type pour les propriétés. Cela dit, nous pouvons maintenant utiliser l'interface et fournir différents types comme arguments.

## Types utilitaires

TypeScript fournit des utilitaires intégrés pratiques qui aident à manipuler les types facilement. Pour les utiliser, vous devez passer dans les `<>` le type que vous souhaitez transformer.

### Partial

* `Partial<T>`

Partial permet de rendre toutes les propriétés du type `T` optionnelles. Il ajoutera un `?` à côté de chaque champ.

```ts
interface PartialType {
  id: number
  firstName: string
  lastName: string
}

function showType(args: Partial<PartialType>) {
  console.log(args)
}

showType({ id: 1 })
// Output: {id: 1}

showType({ firstName: "John", lastName: "Doe" })
// Output: {firstName: "John", lastName: "Doe"}

```

Comme vous pouvez le voir, nous avons une interface `PartialType` qui est utilisée comme annotation de type pour les paramètres reçus par la fonction `showType()`. Et pour rendre les propriétés optionnelles, nous devons utiliser le mot-clé `Partial` et passer le type `PartialType` comme argument. Cela dit, maintenant tous les champs deviennent optionnels.

### Required

* `Required<T>`

Contrairement à `Partial`, l'utilitaire `Required` rend toutes les propriétés du type `T` obligatoires.

```ts
interface RequiredType {
  id: number
  firstName?: string
  lastName?: string
}

function showType(args: Required<RequiredType>) {
  console.log(args)
}

showType({ id: 1, firstName: "John", lastName: "Doe" })
// Output: { id: 1, firstName: "John", lastName: "Doe" }

showType({ id: 1 })
// Error: Type '{ id: number: }' is missing the following properties from type 'Required<RequiredType>': firstName, lastName

```

L'utilitaire `Required` rendra toutes les propriétés obligatoires même si nous les avons rendues optionnelles avant d'utiliser l'utilitaire. Et si une propriété est omise, TypeScript générera une erreur.

### Readonly

* `Readonly<T>`

Ce type utilitaire transformera toutes les propriétés du type `T` afin de les rendre non réassignables avec une nouvelle valeur.

```ts
interface ReadonlyType {
  id: number
  name: string
}

function showType(args: Readonly<ReadonlyType>) {
  args.id = 4
  console.log(args)
}

showType({ id: 1, name: "Doe" })
// Error: Cannot assign to 'id' because it is a read-only property.

```

Ici, nous utilisons l'utilitaire `Readonly` pour rendre les propriétés de `ReadonlyType` non réassignables. Cela dit, si vous essayez de donner une nouvelle valeur à l'un de ces champs, une erreur sera générée.

En outre, vous pouvez également utiliser le mot-clé `readonly` devant une propriété pour la rendre non réassignable.

```ts
interface ReadonlyType {
  readonly id: number
  name: string
}

```

### Pick

* `Pick<T, K>`

Il permet de créer un nouveau type à partir d'un modèle existant `T` en sélectionnant certaines propriétés `K` de ce type.

```ts
interface PickType {
  id: number
  firstName: string
  lastName: string
}

function showType(args: Pick<PickType, "firstName" | "lastName">) {
  console.log(args)
}

showType({ firstName: "John", lastName: "Doe" })
// Output: {firstName: "John"}

showType({ id: 3 })
// Error: Object literal may only specify known properties, and 'id' does not exist in type 'Pick<PickType, "firstName" | "lastName">'

```

`Pick` est un peu différent des utilitaires précédents que nous avons déjà vus. Il attend deux paramètres - `T` est le type dont vous voulez sélectionner des éléments et `K` est la propriété que vous voulez sélectionner. Vous pouvez également sélectionner plusieurs champs en les séparant par un pipe (`|`).

### Omit

* `Omit<T, K>`

L'utilitaire `Omit` est l'inverse du type `Pick`. Et au lieu de sélectionner des éléments, il supprimera les propriétés `K` du type `T`.

```ts
interface PickType {
  id: number
  firstName: string
  lastName: string
}

function showType(args: Omit<PickType, "firstName" | "lastName">) {
  console.log(args)
}

showType({ id: 7 })
// Output: {id: 7}

showType({ firstName: "John" })
// Error: Object literal may only specify known properties, and 'firstName' does not exist in type 'Pick<PickType, "id">'

```

Cet utilitaire est similaire au fonctionnement de `Pick`. Il attend le type et les propriétés à omettre de ce type.

### Extract

* `Extract<T, U>`

`Extract` permet de construire un type en sélectionnant des propriétés qui sont présentes dans deux types différents. L'utilitaire extraira de `T` toutes les propriétés qui peuvent être assignées à `U`.

```ts
interface FirstType {
  id: number
  firstName: string
  lastName: string
}

interface SecondType {
  id: number
  address: string
  city: string
}

type ExtractType = Extract<keyof FirstType, keyof SecondType>
// Output: "id"

```

Ici, nous avons deux types qui ont en commun la propriété `id`. Et donc, en utilisant le mot-clé `Extract`, nous obtenons le champ `id` puisqu'il est présent dans les deux interfaces. Et si vous avez plus d'un champ partagé, l'utilitaire extraira toutes les propriétés similaires.

### Exclude

Contrairement à `Extract`, l'utilitaire `Exclude` construira un type en excluant les propriétés qui sont déjà présentes dans deux types différents. Il exclut de `T` tous les champs qui peuvent être assignés à `U`.

```ts
interface FirstType {
  id: number
  firstName: string
  lastName: string
}

interface SecondType {
  id: number
  address: string
  city: string
}

type ExcludeType = Exclude<keyof FirstType, keyof SecondType>

// Output; "firstName" | "lastName"

```

Comme vous pouvez le voir ici, les propriétés `firstName` et `lastName` peuvent être assignées au type `SecondType` puisqu'elles ne sont pas présentes là-bas. Et en utilisant le mot-clé `Extract`, nous obtenons ces champs comme prévu.

### Record

* `Record<K,T>`

Cet utilitaire aide à construire un type avec un ensemble de propriétés `K` d'un type donné `T`. `Record` est vraiment pratique lorsqu'il s'agit de mapper les propriétés d'un type à un autre.

```ts
interface EmployeeType {
  id: number
  fullname: string
  role: string
}

let employees: Record<number, EmployeeType> = {
  0: { id: 1, fullname: "John Doe", role: "Designer" },
  1: { id: 2, fullname: "Ibrahima Fall", role: "Developer" },
  2: { id: 3, fullname: "Sara Duckson", role: "Developer" },
}

// 0: { id: 1, fullname: "John Doe", role: "Designer" },
// 1: { id: 2, fullname: "Ibrahima Fall", role: "Developer" },
// 2: { id: 3, fullname: "Sara Duckson", role: "Developer" }

```

La manière dont `Record` fonctionne est relativement simple. Ici, il attend un `number` comme type, c'est pourquoi nous avons 0, 1 et 2 comme clés pour la variable `employees`. Et si vous essayez d'utiliser une chaîne de caractères comme propriété, une erreur sera générée. Ensuite, l'ensemble des propriétés est donné par `EmployeeType`, d'où l'objet avec les champs id, fullName et role.

### NonNullable

* `NonNullable<T>`

Il permet de supprimer `null` et `undefined` du type `T`.

```ts
type NonNullableType = string | number | null | undefined

function showType(args: NonNullable<NonNullableType>) {
  console.log(args)
}

showType("test")
// Output: "test"

showType(1)
// Output: 1

showType(null)
// Error: Argument of type 'null' is not assignable to parameter of type 'string | number'.

showType(undefined)
// Error: Argument of type 'undefined' is not assignable to parameter of type 'string | number'.

```

Ici, nous passons le type `NonNullableType` comme argument à l'utilitaire `NonNullable` qui construit un nouveau type en excluant `null` et `undefined` de ce type. Cela dit, si vous passez une valeur nullable, TypeScript générera une erreur.

Au fait, si vous ajoutez le drapeau `--strictNullChecks` au fichier `tsconfig`, TypeScript appliquera des règles de non-nullabilité.

## Types mappés

Les types mappés permettent de prendre un modèle existant et de transformer chacune de ses propriétés en un nouveau type. Notez que certains types utilitaires couverts précédemment sont également des types mappés.

```ts
type StringMap<T> = {
  [P in keyof T]: string
}

function showType(arg: StringMap<{ id: number; name: string }>) {
  console.log(arg)
}

showType({ id: 1, name: "Test" })
// Error: Type 'number' is not assignable to type 'string'.

showType({ id: "testId", name: "This is a Test" })
// Output: {id: "testId", name: "This is a Test"}

```

`StringMap<>` transformera tous les types passés en chaîne de caractères. Cela dit, si nous l'utilisons dans la fonction `showType()`, les paramètres reçus doivent être une chaîne de caractères - sinon, une erreur sera générée par TypeScript.

## Garde de types

Les gardes de types permettent de vérifier le type d'une variable ou d'un objet avec un opérateur. Il s'agit d'un bloc conditionnel qui retourne un type en utilisant `typeof`, `instanceof` ou `in`.

* `typeof`

```ts
function showType(x: number | string) {
  if (typeof x === "number") {
    return `Le résultat est ${x + x}`
  }
  throw new Error(`Cette opération ne peut pas être effectuée sur un ${typeof x}`)
}

showType("Je ne suis pas un nombre")
// Error: Cette opération ne peut pas être effectuée sur une chaîne de caractères

showType(7)
// Output: Le résultat est 14

```

Comme vous pouvez le voir, nous avons un bloc conditionnel JavaScript normal qui vérifie le type de l'argument reçu avec `typeof`. Avec cela en place, vous pouvez maintenant protéger votre type avec cette condition.

* `instanceof`

```ts
class Foo {
  bar() {
    return "Hello World"
  }
}

class Bar {
  baz = "123"
}

function showType(arg: Foo | Bar) {
  if (arg instanceof Foo) {
    console.log(arg.bar())
    return arg.bar()
  }

  throw new Error("Le type n'est pas supporté")
}

showType(new Foo())
// Output: Hello World

showType(new Bar())
// Error: Le type n'est pas supporté

```

Comme l'exemple précédent, celui-ci est également un garde de type qui vérifie si le paramètre reçu fait partie de la classe `Foo` ou non et le traite en conséquence.

* `in`

```ts
interface FirstType {
  x: number
}
interface SecondType {
  y: string
}

function showType(arg: FirstType | SecondType) {
  if ("x" in arg) {
    console.log(`La propriété ${arg.x} existe`)
    return `La propriété ${arg.x} existe`
  }
  throw new Error("Ce type n'est pas attendu")
}

showType({ x: 7 })
// Output: La propriété 7 existe

showType({ y: "ccc" })
// Error: Ce type n'est pas attendu

```

L'opérateur `in` permet de vérifier si une propriété `x` existe ou non sur l'objet reçu comme paramètre.

## Types conditionnels

Les types conditionnels testent deux types et en sélectionnent un en fonction du résultat de ce test.

```ts
type NonNullable<T> = T extends null | undefined ? never : T

```

Cet exemple du type utilitaire `NonNullable` vérifie si le type est null ou non et le traite en conséquence. Et comme vous pouvez le noter, il utilise l'opérateur ternaire JavaScript.

Merci d'avoir lu.

Vous pouvez trouver d'autres contenus intéressants comme celui-ci sur [mon blog](https://www.ibrahima-ndaw.com) ou me suivre [sur Twitter](https://twitter.com/ibrahima92_) pour être informé.