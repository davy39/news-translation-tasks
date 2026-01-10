---
title: Les questions TypeScript les plus posées sur StackOverflow – Guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-11T15:52:33.000Z'
originalURL: https://freecodecamp.org/news/the-top-stack-overflowed-typescript-questions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/combined-blog-cover-6.png
tags:
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
- name: Stack Overflow
  slug: stackoverflow
- name: TypeScript
  slug: typescript
seo_title: Les questions TypeScript les plus posées sur StackOverflow – Guide pour
  débutants
seo_desc: 'By Emmanuel Ohans

  _"I hate stack overflow"_ — said no developer ever.

  While it’s helpful to have your answers a Google search away, what’s even more powerful
  is truly understanding the solutions you stumble upon.

  In this article, I’ll explore the sev...'
---

Par Emmanuel Ohans

_"_Je déteste stack overflow_"_ — n'a jamais dit aucun développeur.

Bien qu'il soit utile d'avoir vos réponses à une recherche Google, ce qui est encore plus puissant, c'est de vraiment comprendre les solutions que vous trouvez.

Dans cet article, je vais explorer les sept questions TypeScript les plus _stackoverflowées_.

J'ai passé des heures à rechercher ces questions.

J'espère que vous allez acquérir une compréhension plus approfondie des problèmes courants que vous pourriez rencontrer avec TypeScript.

Cela est également pertinent si vous apprenez simplement TypeScript — quelle meilleure façon que de vous familiariser avec vos futurs défis !

Commençons.

## Table des matières

1. [Quelle est la différence entre les interfaces et les types dans TypeScript ?](#heading-1-quelle-est-la-difference-entre-les-interfaces-et-les-types-dans-typescript)
2. [Dans TypeScript, qu'est-ce que l'opérateur ! (point d'exclamation / bang) ?](#2-dans-typescript-quest-ce-que-loperateur-point-d-exclamation-bang)
3. [Qu'est-ce qu'un fichier ".d.ts" dans TypeScript ?](#3-quest-ce-quun-fichier-d-ts-dans-typescript)
4. [Comment définir explicitement une nouvelle propriété sur 'window' dans TypeScript ?](#4-comment-definir-explicitement-une-nouvelle-propriete-sur-window-dans-typescript)
5. [Les fonctions fortement typées en tant que paramètres sont-elles possibles dans TypeScript ?](#5-les-fonctions-fortement-typees-en-tant-que-parametres-sont-elles-possibles-dans-typescript)
6. [Comment corriger "Could Not Find Declaration File for Module …" ?](#6-comment-corriger-could-not-find-declaration-file-for-module)
7. [Comment assigner dynamiquement des propriétés à un objet dans TypeScript ?](#7-comment-assigner-dynamiquement-des-proprietes-a-un-objet-dans-typescript)

**Note :** Vous pouvez obtenir une version [PDF ou ePub](https://www.ohansemmanuel.com/cheatsheet/top-7-stack-overflowed-typescript-questions) de cette feuille de triche pour une référence plus facile ou pour la lire sur votre Kindle ou tablette.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-51.png)
_[Version PDF ou Epub de cette feuille de triche disponible](https://www.ohansemmanuel.com/cheatsheet/top-7-stack-overflowed-typescript-questions)_

# 1. Quelle est la différence entre les interfaces et les types dans TypeScript ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-52.png)
_Interfaces vs Types dans Typescript_

La conversation sur les interfaces vs les types (techniquement, alias de type) est très disputée.

Lorsque vous commencez avec TypeScript, vous pouvez trouver cela déroutant de choisir entre les deux. Cet article clarifie la confusion et vous aide à choisir ce qui est le mieux pour vous.

## TL;DR

Dans de nombreux cas, vous pouvez utiliser soit une interface soit un alias de type de manière interchangeable.

Presque toutes les fonctionnalités d'une interface sont disponibles via les alias de type, sauf que vous ne pouvez pas ajouter de nouvelles propriétés à un type en le redéclarant. Vous devez utiliser un type d'intersection.

## Pourquoi la confusion entre les types et les interfaces en premier lieu ?

Chaque fois que nous sommes confrontés à plusieurs options, la plupart des gens commencent à souffrir du [paradoxe du choix](https://en.wikipedia.org/wiki/The_Paradox_of_Choice).

Dans ce cas, il n'y a que deux options.

Qu'y a-t-il de si déroutant à cela ?

Eh bien, la principale confusion ici vient du fait que ces deux options sont si **également assorties** à bien des égards.

Cela rend difficile de faire un choix évident — surtout si vous commencez tout juste avec Typescript.

## Un exemple de base d'alias de type vs interface

Mettons-nous d'accord avec des exemples rapides d'une interface et d'un alias de type.

Considérez les représentations d'un type `Human` ci-dessous :

```ts
// type
type Human = {
  name: string
  legs: number
  head: number
}

// interface
interface Human {
  name: string
  legs: number
  head: number
}

```

Ce sont deux façons correctes de noter le type `Human` — c'est-à-dire via un alias de type ou une interface.

## Les différences entre l'alias de type et les interfaces

Voici les principales différences entre un alias de type et une interface :

### Différence clé : les interfaces ne peuvent décrire que les formes d'objets. Les alias de type peuvent être utilisés pour d'autres types tels que les primitives, les unions et les tuples.

Un alias de type est assez flexible dans les types de données que vous pouvez représenter. Des primitives de base aux unions et tuples complexes, comme montré ci-dessous :

```ts
// primitives
type Name = string

// object
type Male = {
  name: string
}

type Female = {
  name: string
}

// union
type HumanSex = Male | Female

// tuple
type Children = [Female, Male, Female]

```

Contrairement aux alias de type, vous ne pouvez représenter que des types d'objets avec une interface.

### Différence clé : une interface peut être étendue en la déclarant plusieurs fois

Considérez l'exemple suivant :

```ts
interface Human {
  name: string
}

interface Human {
  legs: number
}

```

Les deux déclarations ci-dessus deviendront :

```ts
interface Human {
  name: string
  legs: number
}

```

`Human` sera traité comme une seule interface : une combinaison des membres des deux déclarations.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-53.png)
_La propriété 'legs' est requise dans le type 'Humans'_

Voir [TypeScript playground](https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgBIFcC2cTIN4BQyxyIcmEAXMgM5hSgDmBAvgaJLIihtroSWQAbCIxrUQWAEbRWBAgHoFyMAAtgNZNCgB7KJp3owyGQjjoaKAOQixV5JgvGIADw3GCCHSDrJV1XhxkAF58IhIyCmorAHlVHE0AUUw+dAghK1YgA).

Ce n'est pas le cas avec les alias de type.

Avec un alias de type, ce qui suit entraînera une erreur :

```ts
type Human = {
    name: string
}

type Human = {
    legs: number
}

const h: Human = {
   name: 'gg',
   legs: 5
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-54.png)
_Erreur d'identifiant dupliqué 'Human'_

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/C4TwDgpgBAEgrgWwIYDsoF4oG8BQV9QpIIQBcUAzsAE4CWKA5lDgL57OiSyKob64EoAGwgMK5FIgBGEaszY4AxgHsUVKAAty8ZGkwD8REuQDkDBiYA07YaPFQArPPw5XroA).

Avec les alias de type, vous devrez recourir à un type d'intersection :

```ts
type HumanWithName = {
    name: string
}

type HumanWithLegs = {
    legs: number
}

type Human = HumanWithName & HumanWithLegs

const h: Human = {
   name: 'gg',
   legs: 5
}

```

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/C4TwDgpgBAEgrgWwIYDsDqBLYALAckhaAXigG8AoKKqFAiALigGdgAnDFAcynIF9KeoSLESpMOADIROTKCTICqAG2lNGKRACMIrHv3JDo8ZCioljYrHjpQAZCJPjsUmeXIBjAPYoWUbIwtTEgpqWkJGAHJOTgiAGkUVGUYAVj0qNwygA).

### Différence mineure : les alias de type et les interfaces peuvent être étendus, mais avec des syntaxes différentes

Avec les interfaces, vous utilisez le mot-clé `extends`. Pour les types, vous devez utiliser une intersection.

Considérez les exemples suivants :

#### Alias de type étendant un alias de type

```ts
type HumanWithName = {
  name: string
}

type Human = HumanWithName & {
   legs: number
   eyes: number
}

```

#### Alias de type étendant une interface

```ts
interface HumanWithName {
  name: string
}

type Human = HumanWithName & {
   legs: number
   eyes: number
}

```

#### Interface étendant une interface

```ts
interface HumanWithName {
  name: string
}

interface Human extends HumanWithName {
  legs: number
  eyes: number
}

```

#### Interface étendant un alias de type

```ts
type HumanWithName = {
  name: string
}

interface Human extends HumanWithName {
  legs: number
  eyes: number
}

```

Comme vous pouvez le voir, ce n'est pas particulièrement une raison de choisir l'un plutôt que l'autre. Cependant, les syntaxes diffèrent.

### Différence mineure : les classes ne peuvent implémenter que des membres connus statiquement

Une classe peut implémenter à la fois des interfaces ou des alias de type. Cependant, une classe ne peut pas implémenter ou étendre un type d'union.

Considérez l'exemple suivant :

#### Classe implémentant une interface

```ts
interface Human {
  name: string
  legs: number
  eyes: number
}

class FourLeggedHuman implements Human {
  name = 'Krizuga'
  legs = 4
  eyes = 2
}

```

#### Classe implémentant un alias de type

```ts
type Human = {
  name: string
  legs: number
  eyes: number
}

class FourLeggedHuman implements Human {
  name = 'Krizuga'
  legs = 4
  eyes = 2
}

```

Ces deux exemples fonctionnent sans aucune erreur. Cependant, le suivant échoue :

#### Classe implémentant un type d'union

```ts
type Human = {
    name: string
} | {
    legs: number
    eyes: number
}

class FourLeggedHuman implements Human {
    name = 'Krizuga'
    legs = 4
    eyes = 2
}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-55.png)
_Une classe ne peut implémenter qu'un type d'objet ou une intersection de types d'objets avec des membres connus statiquement._

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/C4TwDgpgBAEgrgWwIYDsoF4oG8BQV9QpIIQBcUAzsAE4CWKA5jgL5QA+2eBANhAxeRSIARhGpd8EEBAGERYljhwBjbkgoUoAMQD2cagBk+DCABN4yNLQRheJFME0XUnAoWLRMAcgDSdAF5wDEheElC8-BhQACxhUjJRAEwsQA).

## Résumé des alias de type vs interfaces

Votre expérience peut varier, mais dans la mesure du possible, je m'en tiens aux alias de type pour leur flexibilité et leur syntaxe plus simple. C'est-à-dire que je choisis les alias de type sauf si j'ai spécifiquement besoin de fonctionnalités d'une interface.

Pour la plupart, vous pouvez également décider en fonction de vos préférences personnelles, mais restez cohérent avec votre choix — au moins dans un projet donné.

Pour être complet, je dois ajouter que dans les types critiques pour les performances, les vérifications de comparaison d'interface peuvent être plus rapides que les alias de type. Je n'ai pas encore trouvé que cela pose un problème.

# Dans TypeScript, qu'est-ce que l'opérateur ! (point d'exclamation / bang) ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-56.png)
_Qu'est-ce que l'opérateur bang dans TypeScript ?_

## TL;DR

Ce `!` est techniquement appelé l'**opérateur d'assertion non-null**. Si le compilateur TypeScript se plaint qu'une valeur est `null` ou `undefined`, vous pouvez utiliser l'opérateur `!` pour affirmer que ladite valeur n'est pas `null` ou `undefined`.

Opinion personnelle : évitez de faire cela autant que possible.

## Qu'est-ce que l'opérateur d'assertion non-null ?

`null` et `undefined` sont des valeurs JavaScript valides.

L'énoncé ci-dessus est vrai pour toutes les applications TypeScript également.

Cependant, TypeScript va plus loin.

`null` et `undefined` sont également des types valides. Par exemple, considérons ce qui suit :

```ts
// null explicite
let a: null

a = null
// les affectations suivantes produiront des erreurs
a = undefined
a = {}


// undefined explicite
let b: undefined
// les affectations suivantes produiront des erreurs
b = null
b = {}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-57.png)
_Erreur : les valeurs autres que null et undefined ne sont pas assignables_

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/DYUwLgBAhgXBB2BXYwICg1QgXgc4aA9IRGABYgQBmA9ijQO4CW8A5tAM4dOvwC2IeGA4RmKCAE8mIYABMIIAE6KaijplyJ4skFRYh5mHBADeAXwxpQkAEZwtOvfAPpipCtTrBGLdlC48-ILCokziUjLySipqaDbGSOJxxuZoQA).

Dans certains cas, le compilateur TypeScript ne peut pas dire si une certaine valeur est définie ou non, c'est-à-dire qu'elle n'est pas `null` ou `undefined`.

Par exemple, supposons que vous avez une valeur `Foo`.

`Foo!` produit une valeur du type de `Foo` avec `null` et `undefined` exclus.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-58.png)
_Foo! exclut null et undefined du type de Foo_

Vous dites essentiellement au compilateur TypeScript, _je suis sûr que `Foo` ne sera PAS `null` ou `undefined`_.

Explorons un exemple naïf.

En JavaScript standard, vous pouvez concaténer deux chaînes avec la méthode `.concat` :

```ts
const str1 = "Hello"
const str2 = "World"

const greeting = str1.concat(' ', str2)
// Hello World

```

Écrivez une simple fonction de duplication de chaîne qui appelle `.concat` avec elle-même comme argument :

```ts
function duplicate(text: string | null) {
  return text.concat(text);
}

```

Notez que l'argument `text` est typé comme `string | null`.

En mode strict, TypeScript se plaindra ici, car appeler `concat` avec `null` peut entraîner des résultats inattendus.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-59.png)
_Le résultat de l'appel de concat avec null_

L'erreur TypeScript sera : `Object is possibly 'null'.(2531)`.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-60.png)
_Erreur TypeScript : Object is possibly null_

D'un autre côté, une manière plutôt paresseuse de faire taire l'erreur du compilateur est d'utiliser l'opérateur d'assertion non-null :

```ts
function duplicate(text: string | null) {
  return text!.concat(text!);
}

```

Notez le point d'exclamation après la variable `text` — `text!`.

Le type `text` représente `string | null`.

`text!` représente simplement `string`, c'est-à-dire avec `null` ou `undefined` retiré du type de la variable.

Le résultat ? Vous avez fait taire l'erreur TypeScript.

Cependant, ce n'est pas une solution judicieuse.

`duplicate` peut effectivement être appelé avec `null`, ce qui peut entraîner des résultats inattendus.

Notez que l'exemple suivant est également vrai si `text` est une propriété optionnelle :

```ts
// text pourrait être "undefined"
function duplicate(text?: string) {
  return text!.concat(text!);
}

```

## Pièges de l'opérateur `!` (et que faire à la place)

Lorsque vous travaillez avec TypeScript en tant que nouvel utilisateur, vous pouvez avoir l'impression de livrer une bataille perdue d'avance.

Les erreurs n'ont pas de sens pour vous.

Votre objectif est de supprimer l'erreur et de continuer votre vie aussi rapidement que possible.

Cependant, vous devez être prudent avec l'utilisation de l'opérateur d'assertion non-null.

Faire taire une erreur TypeScript ne signifie pas qu'il n'y a peut-être pas encore un problème sous-jacent — si non résolu.

Comme vous l'avez vu dans l'exemple précédent, vous perdez toute la sécurité TypeScript pertinente contre les mauvaises utilisations où `null` et `undefined` pourraient être indésirables.

Alors, que devriez-vous faire ?

Si vous écrivez React, considérons un exemple auquel vous êtes probablement familier :

```ts
const MyComponent = () => {
   const ref = React.createRef<HTMLInputElement>();
	
   //erreur de compilation : ref.current est possiblement null
   const goToInput = () => ref.current.scrollIntoView();

    return (
       <div>
           <input ref={ref}/>
           <button onClick={goToInput}>Go to Input</button>
       </div>
   );
};

```

Dans l'exemple ci-dessus (pour ceux qui n'écrivent pas React), dans le modèle mental de `React`, `ref.current` sera certainement disponible au moment où le bouton est cliqué par l'utilisateur.

L'objet `ref` est défini peu après que les éléments UI sont rendus.

TypeScript ne sait pas cela, et vous pouvez être forcé d'utiliser l'opérateur d'assertion non-null ici.

Essentiellement, dites au compilateur TypeScript, je sais ce que je fais, vous ne le savez pas.

```ts
const goToInput = () => ref.current!.scrollIntoView();

```

Notez le point d'exclamation `!`.

Cela « corrige » l'erreur.

Cependant, si à l'avenir, quelqu'un supprime le `ref` de l'entrée, et qu'il n'y avait pas de tests automatisés pour attraper cela, vous avez maintenant un bug.

```ts
// avant
<input ref={ref}/>

// après
<input />

```

TypeScript ne pourra pas repérer l'erreur dans la ligne suivante :

```ts
const goToInput = () => ref.current!.scrollIntoView();

```

En utilisant l'opérateur d'assertion non-null, le compilateur TypeScript agira comme si `null` et `undefined` n'étaient jamais possibles pour la valeur en question. Dans ce cas, `ref.current`.

### Solution 1 : Trouver une solution alternative

La première ligne d'action que vous devriez employer est de trouver une solution alternative.

Par exemple, souvent vous pouvez vérifier explicitement les valeurs `null` et `undefined` comme ceci :

```ts
// avant
const goToInput = () => ref.current!.scrollIntoView();

// maintenant
const goToInput = () => {
  if (ref.current) {
   //Typescript comprendra que ref.current est certainement
   //disponible dans cette branche
     ref.current.scrollIntoView()
  }
};

// ou alors (utiliser l'opérateur AND logique)
const goToInput = () => ref.current && ref.current.scrollIntoView();

```

De nombreux ingénieurs discuteront du fait que cela est plus verbeux.

C'est correct.

Mais vous devriez choisir verbeux plutôt que du code potentiellement cassé qui est poussé en production.

C'est une préférence personnelle. Votre expérience peut varier.

### Solution 2 : Lever explicitement une erreur

Dans les cas où une solution alternative ne suffit pas et où l'opérateur d'assertion non-null semble être la seule solution, je vous conseille généralement de lever une erreur avant de faire cela.

Voici un exemple (en pseudocode) :

```ts
function doSomething (value) {
   // pour une raison quelconque TS pense que la valeur pourrait être
   // null ou undefined mais vous n'êtes pas d'accord

  if(!value) {
    // affirmez explicitement que c'est le cas
    // lever une erreur ou logger cela quelque part où vous pouvez tracer
    throw new Error('erreur inattendue : valeur non présente')
  }

  // allez-y et utilisez l'opérateur d'assertion non-null
  console.log(value)
}

```

Un cas pratique où je me suis parfois retrouvé à faire cela est en utilisant `Formik`.

Sauf que les choses ont changé, et je pense que `Formik` est mal typé dans de nombreux cas.

L'exemple peut être similaire si vous avez fait votre validation Formik et êtes sûr que vos valeurs existent.

Voici un peu de pseudocode :

```ts
<Formik
  validationSchema={...}
  onSubmit={(values) => {
   // vous êtes sûr que values.name devrait exister parce que vous avez
   // validé dans validationSchema mais TypeScript ne le sait pas

   if(!values.name) {
    throw new Error('Formulaire invalide, le nom est requis')		
   }
   console.log(values.name!)
}}>


</Formik>

```

Dans le pseudocode ci-dessus, `values` pourrait être typé comme :

```ts
type Values = {
  name?: string
}

```

Mais avant de cliquer sur `onSubmit`, vous avez ajouté une validation pour montrer une erreur de formulaire UI à l'utilisateur pour qu'il saisisse un `name` avant de passer à la soumission du formulaire.

Il existe d'autres moyens de contourner cela. Mais si vous êtes sûr qu'une valeur existe mais ne pouvez pas tout à fait le communiquer au compilateur TypeScript, utilisez l'opérateur d'assertion non-null. Mais ajoutez également une assertion de votre propre en levant une erreur que vous pouvez tracer.

## Et une assertion implicite ?

Même si le nom de l'opérateur se lit comme opérateur d'assertion non-null, aucune « assertion » n'est réellement faite.

Vous affirmez surtout (en tant que développeur) que la valeur existe.

Le compilateur TypeScript ne fait PAS d'assertion que cette valeur existe.

Donc, si vous devez, vous pouvez aller de l'avant et ajouter votre assertion (par exemple, comme discuté dans la section précédente).

Notez également qu'aucun code JavaScript supplémentaire n'est émis en utilisant l'opérateur d'assertion non-null.

Comme indiqué précédemment, il n'y a pas d'assertion faite ici par TypeScript.

Par conséquent, TypeScript n'émettra pas de code qui vérifie si cette valeur existe ou non.

Le code JavaScript émis agira comme si cette valeur existait toujours.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-62.png)
_Code javascript émis identique au Javascript_

## Conclusion

TypeScript 2.0 a vu la sortie de l'**opérateur d'assertion non-null**. Oui, il est là depuis un certain temps ([sorti en 2016](https://github.com/microsoft/TypeScript/releases/tag/v2.0.3)). Au moment de l'écriture, la dernière version de TypeScript est `v4.7`.

Si le compilateur TypeScript se plaint qu'une valeur est `null` ou `undefined`, vous pouvez utiliser l'opérateur `!` pour affirmer que ladite valeur n'est pas null ou undefined.

Ne faites cela que si vous êtes certain que c'est le cas.

Mieux encore, allez-y et ajoutez une assertion de votre propre, ou essayez de trouver une solution alternative.

Certains peuvent argumenter que si vous devez utiliser l'opérateur d'assertion non-null à chaque fois, c'est un signe que vous représentez mal l'état de votre application via TypeScript.

Je suis d'accord avec cette école de pensée.

# Qu'est-ce qu'un fichier ".d.ts" dans TypeScript ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-63.png)
_Qu'est-ce qu'un fichier d.ts ?_

## TL;DR

Les fichiers `.d.ts` sont appelés fichiers de déclaration de type. Ils existent pour un seul but : décrire la forme d'un module existant et ils ne contiennent que des informations de type utilisées pour la vérification de type.

## Introduction aux fichiers `.d.ts` dans TypeScript

En apprenant les bases de TypeScript, vous déverrouillez des superpouvoirs.

Au moins, c'est ce que j'ai ressenti.

Vous obtenez automatiquement des avertissements sur les erreurs potentielles et vous obtenez la complétion automatique directement dans votre éditeur de code.

Bien que cela semble magique, rien avec les ordinateurs ne l'est vraiment.

Alors, quel est le truc ici, TypeScript ?

En langage plus clair, comment TypeScript sait-il autant ? Comment décide-t-il quelle API est correcte ou non ? Quelles méthodes sont disponibles sur un certain objet ou classe, et lesquelles ne le sont pas ?

La réponse est moins magique.

TypeScript repose sur les types.

Occasionnellement, vous n'écrivez pas ces types, mais ils existent.

Ils existent dans des fichiers appelés fichiers de déclaration.

Ce sont des fichiers avec une extension `.d.ts`.

## Un exemple simple de fichiers `.d.ts`

Considérez le code TypeScript suivant :

```ts
// valide
const amount = Math.ceil(14.99)

// erreur : La propriété 'ciil' n'existe pas sur le type 'Math'.(2339)
const otherAmount = Math.ciil(14.99)

```

Voir le [TypeScript playground](https://www.TypeScriptlang.org/play?#code/MYewdgzgLgBAhgWxAVzLAvDAsnKALAOmAFMBLAGwAoBGAFgIE4GBKAKFdElhH2ICcAgklQZsuQsFIUa9Jm1ZA).

La première ligne de code est parfaitement valide, mais la seconde, pas tout à fait.

Et TypeScript est rapide pour repérer l'erreur : `Property 'ciil' does not exist on type 'Math'.(2339)`.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-64.png)
_L'erreur TypeScript repérant le mauvais accès à la propriété "ciil"_

Comment TypeScript a-t-il su que `ciil` n'existe pas sur l'objet `Math` ?

L'objet `Math` ne fait pas partie de notre implémentation. C'est un objet intégré standard.

Alors, comment TypeScript a-t-il compris cela ?

La réponse est qu'il existe des **fichiers de déclaration** qui décrivent ces objets intégrés.

Imaginez un fichier de déclaration contenant toutes les informations de type relatives à un certain module. Il ne contient aucune implémentation réelle, juste des informations de type.

Ces fichiers ont une extension `.d.ts`.

Vos fichiers d'implémentation auront soit des extensions `.ts` ou `.js` pour représenter les fichiers TypeScript ou JavaScript.

Ces fichiers de déclaration n'ont pas d'implémentations. Ils ne contiennent que des informations de type et ont une extension de fichier `.d.ts`.

## Définitions de type intégrées

Une excellente façon de comprendre cela en pratique est de configurer un tout nouveau projet TypeScript et d'explorer les fichiers de définition de type pour les objets de haut niveau comme `Math`.

Faisons cela.

Créez un nouveau répertoire, et nommez-le comme vous le souhaitez.

Je vais appeler le mien `dts`.

Changez de répertoire pour ce dossier nouvellement créé :

```ts
cd dts

```

Maintenant, initialisez un nouveau projet :

```ts
npm init --yes

```

Installez TypeScript :

```ts
npm install TypeScript --save-dev

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-65.png)
_Installation de TypeScript_

Ce répertoire devrait contenir 2 fichiers et un sous-répertoire :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-66.png)
_Les fichiers après l'installation_

Ouvrez le dossier dans votre éditeur de code préféré.

Si vous inspectez le répertoire `TypeScript` dans `node_modules`, vous trouverez un ensemble de fichiers de déclaration de type prêts à l'emploi.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-67.png)
_Fichiers de déclaration de type dans le répertoire TypeScript_

Ces fichiers sont présents grâce à l'installation de TypeScript.

Par défaut, TypeScript inclura la définition de type pour toutes les API DOM, par exemple pensez à `window` et `document`.

En inspectant ces fichiers de déclaration de type, vous remarquerez que la convention de nommage est simple.

Elle suit le modèle : `lib.[quelquechose].d.ts`.

Ouvrez le fichier de déclaration `lib.dom.d.ts` pour voir toutes les déclarations liées à l'API DOM du navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-68.png)
_Le fichier de déclaration dom_

Comme vous pouvez le voir, ce fichier est assez gigantesque.

Mais il en va de même pour toutes les API disponibles dans le DOM.

Génial !

Maintenant, si vous jetez un coup d'œil au fichier `lib.es5.d.ts`, vous verrez la déclaration de l'objet `Math`, contenant la propriété `ceil`.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-69.png)
_L'objet Math dans le fichier de déclaration_

La prochaine fois que vous pensez, wow, TypeScript est merveilleux. Souvenez-vous, une grande partie de cette merveille est due aux héros moins connus : les fichiers de déclaration de type.

Ce n'est pas de la magie. Juste des fichiers de déclaration de type.

## Définitions de type externes dans TypeScript

Et les API qui ne sont pas intégrées ?

Il existe une multitude de packages `npm` pour faire à peu près tout ce que vous voulez.

Y a-t-il un moyen pour TypeScript de comprendre également les relations de type pertinentes pour ledit module ?

Eh bien, la réponse est un oui retentissant.

Il y a généralement deux façons pour un auteur de bibliothèque de faire cela.

### Types regroupés

Dans ce cas, l'auteur de la bibliothèque a déjà regroupé les fichiers de déclaration de type dans le cadre de la distribution du package.

Vous n'avez généralement rien à faire.

Vous allez de l'avant et installez la bibliothèque dans votre projet, vous importez le module requis de la bibliothèque et voyez si TypeScript doit résoudre automatiquement les types pour vous.

Souvenez-vous, ce n'est pas de la magie.

L'auteur de la bibliothèque a regroupé le fichier de déclaration de type dans la distribution du package.

### DefinitelyTyped (@types)

Imaginez un dépôt public central qui héberge des fichiers de déclaration pour des milliers de bibliothèques ?

Eh bien, ramenez cette image à la maison.

Ce dépôt existe déjà.

Le [dépôt DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped/) est un dépôt centralisé qui stocke les fichiers de déclaration pour des milliers de bibliothèques.

En toute honnêteté, la grande majorité des bibliothèques couramment utilisées ont des fichiers de déclaration disponibles sur **DefinitelyTyped**.

Ces fichiers de définition de type sont automatiquement publiés sur `npm` sous le scope `@types`.

Par exemple, si vous vouliez installer les types pour le package npm `react`, vous feriez ceci :

```ts
npm install --save-dev @types/react

```

Si vous vous retrouvez à utiliser un module dont les types ne sont pas résolus automatiquement par TypeScript, essayez d'installer les types directement depuis DefinitelyTyped.

Voir si les types existent là-bas. Par exemple :

```ts
npm install --save-dev @types/your-library

```

Les fichiers de définition que vous ajoutez de cette manière seront enregistrés dans `node_modules/@types`.

TypeScript les trouvera automatiquement. Donc, il n'y a pas d'étape supplémentaire à suivre.

## Comment écrire vos propres fichiers de déclaration

Dans le cas peu fréquent où une bibliothèque n'a pas regroupé ses types et ne dispose pas d'un fichier de définition de type sur DefinitelyTyped, vous pouvez écrire vos propres fichiers de déclaration.

Écrire des fichiers de déclaration en profondeur dépasse le cadre de cet article, mais un cas d'utilisation que vous rencontrerez probablement est de faire taire les erreurs concernant un module particulier sans fichier de déclaration.

Tous les fichiers de déclaration ont une extension `.d.ts`.

Pour créer le vôtre, créez un fichier avec une extension `.d.ts`.

Par exemple, supposons que j'ai installé la bibliothèque `untyped-module` dans mon projet.

`untyped-module` n'a pas de fichiers de définition de type référencés, donc TypeScript se plaint de cela dans mon projet.

Pour faire taire cet avertissement, je peux créer un nouveau fichier `untyped-module.d.ts` dans mon projet avec le contenu suivant :

```ts
declare module "some-untyped-module";

```

Cela déclarera le module comme étant de type `any`.

Nous n'aurons aucun support TypeScript pour ce module, mais vous aurez fait taire l'avertissement TypeScript.

Les étapes suivantes idéales incluraient l'ouverture d'une issue dans le dépôt public du module pour inclure un fichier de déclaration TypeScript, ou l'écriture d'un fichier décent vous-même.

## Conclusion

La prochaine fois que vous pensez, wow, TypeScript est remarquable. Souvenez-vous, une grande partie de cette merveille est due aux héros moins connus : les fichiers de déclaration de type.

Maintenant, vous comprenez comment ils fonctionnent !

# Comment définir explicitement une nouvelle propriété sur `window` dans Typescript ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-70.png)
_Définir une nouvelle propriété sur l'objet window ?_

## TL;DR

Étendez la déclaration d'interface existante pour l'objet `Window`.

## Introduction à `window` dans TypeScript

Le savoir s'appuie sur le savoir.

Celui qui a dit cela avait raison.

Dans cette section, nous allons nous appuyer sur les connaissances des deux sections précédentes :

* [Interfaces vs Types dans TypeScript](https://blog.ohansemmanuel.com/interfaces-vs-types-in-typescript/)
* [Qu'est-ce qu'un fichier d.t.s dans TypeScript](https://blog.ohansemmanuel.com/what-is-a-dts-file-in-typescript/) ?

Prêt ?

Tout d'abord, je dois dire que dans mes premiers jours avec TypeScript, c'était une question que j'ai googlé encore et encore.

Je n'ai jamais compris. Et je ne me suis pas donné la peine, je me suis contenté de googler.

Ce n'est jamais la bonne mentalité pour maîtriser un sujet.

Discutons des solutions à cela.

## Comprendre le problème

Le problème ici est en fait simple à raisonner.

Considérez le code TypeScript suivant :

```ts
window.__MY_APPLICATION_NAME__ = "freecodecamp"

console.log(window.__MY_APPLICATION_NAME__)

```

TypeScript est rapide pour vous faire savoir que `__MY_APPLICATION_NAME__` n'existe pas sur le type 'Window & typeof globalThis'.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-71.png)
_La propriété n'existe pas sur l'erreur Window_

Voir le [TypeScript playground](https://www.ohansemmanuel.com/cheatsheet/top-7-stack-overflowed-typescript-questions).

D'accord, TypeScript.

Nous comprenons.

En y regardant de plus près, souvenez-vous de la section précédente sur les [fichiers de déclaration](https://blog.ohansemmanuel.com/what-is-a-dts-file-in-typescript/) qu'il existe un fichier de déclaration pour toutes les API de navigateur existantes. Cela inclut les objets intégrés tels que `window`.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-72.png)
_La déclaration d'interface Window par défaut_

Si vous regardez dans le fichier de déclaration `lib.dom.d.ts`, vous trouverez l'interface `Window` décrite.

En termes profanes, l'erreur ici indique que l'interface `Window` décrit comment je comprends l'objet `window` et son utilisation. Cette interface ne spécifie pas une certaine propriété `__MY_APPLICATION_NAME__`.

## Comment corriger l'erreur

Dans la section types vs interface, j'ai expliqué comment étendre une interface.

Appliquons cette connaissance ici.

Nous pouvons étendre la déclaration d'interface `Window` pour qu'elle prenne connaissance de la propriété `__MY_APPLICATION_NAME__`.

Voici comment :

```ts
// avant
window.__MY_APPLICATION_NAME__ = "freecodecamp"

console.log(window.__MY_APPLICATION_NAME__)

// maintenant
interface Window {
  __MY_APPLICATION_NAME__: string
}

window.__MY_APPLICATION_NAME__ = "freecodecamp"

console.log(window.__MY_APPLICATION_NAME__)

```

Les erreurs ont disparu !

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-74.png)
_La solution résolue_

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgOqgCYHsDuyDeAUMsgPqkCyAmqQIIAK9AMgJIDCtAKiwPIBypPrQoBRcgC5kAZzBRQAc0IBfQoRyZcAOnLU6jVh279BwsaWQBeZACIYUCBARYMjuAFsADtdVOQUrAA2EJoBWPIAFOog2DjalDQMzOxcvAJCouQAlEA).

Souvenez-vous qu'une différence clé entre les types et les interfaces est que les interfaces peuvent être étendues en les déclarant plusieurs fois.

Ce que nous avons fait ici est de déclarer l'interface `Window` une fois de plus, étendant ainsi la déclaration de l'interface.

### Une solution dans le monde réel

J'ai résolu ce problème dans le TypeScript playground pour vous montrer la solution sous sa forme la plus simple, c'est-à-dire le cœur du problème.

Dans le monde réel, cependant, vous n'étendriez pas l'interface dans votre code.

Alors, que devriez-vous faire à la place ?

Devinez, peut-être ?

Oui, vous étiez proche... ou peut-être correct :

Créez un fichier de définition de type !

Par exemple, créez un fichier `window.d.ts` avec le contenu suivant :

```ts
interface Window {
  __MY_APPLICATION_NAME__: string
}

```

Et voilà.

Vous avez étendu avec succès l'interface `Window` et résolu le problème.

Si vous avez attribué le mauvais type de valeur à la propriété `__MY_APPLICATION_NAME__`, vous avez maintenant une vérification de type forte activée.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-75.png)
_Une mauvaise affectation à la propriété nouvellement définie attrapée_

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgOqgCYHsDuyDeAUMsgPqkCyAmqQIIAK9AMgJIDCtAKiwPIBypPrQoBRcgC5kAZzBRQAc0IBfQoRyZcAOnLU6jVh279BwsaWQBeAsWQg4AWwiSARDCgQICLBk8OADs7Kql4gUlgANhCa4VjyABTqINg42pQ0DMzsXLwCQqLkAJSqxUA).

_Et _Voilà._

## Conclusion

Dans les [anciens posts de stack overflow](https://stackoverflow.com/questions/12709074/how-do-you-explicitly-set-a-new-property-on-window-in-typescript), vous trouverez des réponses plus compliquées basées sur des versions plus anciennes de TypeScript.

La solution est plus facile à comprendre dans TypeScript moderne.

Maintenant vous savez. 😉

# Les fonctions fortement typées en tant que paramètres sont-elles possibles dans TypeScript ?

## TL;DR

Cette question n'a pas besoin d'être trop expliquée. La réponse courte est oui.

Les fonctions peuvent être fortement typées — même en tant que paramètres d'autres fonctions.

## Introduction

Je dois dire que, contrairement à d'autres sections de cet article, je ne me suis jamais vraiment retrouvé à chercher cela dans mes premiers jours avec TypeScript.

Cependant, ce n'est pas ce qui est le plus important.

C'est une question bien recherchée, alors répondons-y !

## Comment utiliser des paramètres de fonction fortement typés dans TypeScript

La réponse acceptée sur ce [post de stack overflow](https://stackoverflow.com/questions/14638990/are-strongly-typed-functions-as-parameters-possible-in-typescript) est correcte — dans une certaine mesure.

En supposant que vous avez une fonction : `speak` :

```ts
function speak(callback) {
  const sentence = "Hello world"
  alert(callback(sentence))
}

```

Elle reçoit un `callback` qui est appelé en interne avec une `string`.

Pour typer cela, allez-y et représentez le `callback` avec un alias de type de fonction :

```ts
type Callback = (value: string) => void

```

Et tapez la fonction `speak` comme suit :

```ts
function speak(callback: Callback) {
  const sentence = "Hello world"
  alert(callback(sentence))
}

```

Alternativement, vous pourriez également garder le type en ligne :

```ts
function speak(callback: (value: string) => void) {
  const sentence = "Hello world"

  alert(callback(sentence))
}

```

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/GYVwdgxgLglg9mABAZwA4FMCGBrAFBTAG0ICNMJsAuRXANyJHWuSgCcYwBzASkQF4AfIlpwYAE14BvAFCJEEBCxTowUFRHT9EAIgAS6YnEQB3OK0Jjt02YiLpWUfEVLk8yFWsjpu3aQF9rQOkgA).

Et voilà !

Vous avez utilisé une fonction fortement typée comme paramètre.

## Comment gérer les fonctions sans valeur de retour

La réponse acceptée dans le post de stack overflow référencé dit par exemple que _le type du paramètre de rappel doit être_ une _"fonction qui accepte un nombre et retourne le type any"_.

C'est partiellement vrai, mais le type de retour n'a PAS à être `any`.

En fait, n'utilisez PAS `any`.

Si votre fonction retourne une valeur, allez-y et tapez-la de manière appropriée :

```ts
// Callback retourne un objet
type Callback = (value: string) => { result: string }

```

Si votre callback ne retourne rien, utilisez `void` et non `any` :

```ts
// Callback ne retourne rien
type Callback = (value: string) => void

```

Notez que la signature de votre type de fonction doit être :

```ts
(arg1: Arg1type, arg2: Arg2type) => ReturnType

```

Où `Arg1type` représente le type de l'argument `arg1`, `Arg2type` le type de l'argument `arg2`, et `ReturnType` le type de retour de votre fonction.

## Conclusion

Les fonctions sont le moyen principal de transmettre des données en JavaScript.

TypeScript ne vous permet pas seulement de spécifier l'entrée et la sortie des fonctions, mais vous pouvez également typer les fonctions en tant qu'arguments d'autres fonctions.

Allez-y et utilisez-les en toute confiance.

# Comment corriger "Could Not Find Declaration File for Module …" ?

C'est une source courante de frustration pour les débutants en TypeScript.

Cependant, savez-vous comment corriger cela ?

Oui, vous le savez !

Nous avons vu la solution à cela dans la section _qu'est-ce que `d.ts`_.

## TL;DR

Créez un fichier de déclaration, par exemple `untyped-module.d.ts`, avec le contenu suivant : `declare module "some-untyped-module";`. Notez que cela typera explicitement le module comme `any`.

## La solution expliquée

Vous pouvez relire la section sur l'écriture de vos fichiers de déclaration si vous ne vous souvenez pas comment corriger cela.

Essentiellement, vous avez cette erreur parce que la bibliothèque en question n'a pas regroupé ses types et ne dispose pas d'un fichier de définition de type sur [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped/).

Cela vous laisse avec une solution : écrire votre propre fichier de déclaration.

Par exemple, si vous avez installé la bibliothèque `untyped-module` dans votre projet, `untyped-module` n'a pas de fichiers de définition de type référencés, donc TypeScript se plaint.

Pour faire taire cet avertissement, créez un nouveau fichier `untyped-module.d.ts` dans votre projet avec le contenu suivant :

```ts
declare module "some-untyped-module";

```

Cela déclarera le module comme étant de type `any`.

Vous n'aurez aucun support TypeScript pour ce module, mais vous aurez fait taire l'avertissement TypeScript.

Les étapes suivantes idéales incluraient l'ouverture d'une issue dans le dépôt public du module pour inclure un fichier de déclaration TypeScript ou l'écriture d'un fichier décent vous-même (hors du cadre de cet article).

# Comment assigner dynamiquement des propriétés à un objet dans Typescript ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-76.png)
_Assignation dynamique de propriétés aux objets dans Typescript_

## TL;DR

Si vous ne pouvez pas définir le type de variable au moment de la déclaration, utilisez le type utilitaire `Record` ou une signature d'index d'objet.

## Introduction

Considérez l'exemple suivant :

```ts
const organization = {}

organization.name = "Freecodecamp"

```

Ce morceau de code apparemment inoffensif génère une erreur TypeScript lors de l'assignation dynamique de `name` à l'objet `organization`.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-80.png)
_Erreur Typescript lors de l'ajout d'une nouvelle propriété dynamiquement_

Voir le [Typescript playground](https://www.typescriptlang.org/play?#code/MYewdgzgLgBCBOBzAhmAlgL2VN4YF4YBvAXwCgyEV0sdwA6MZAWwFMCYAiAMXlddAATASwAOnCjCnSZsufIWKlylarXqZFIA)

La source de confusion, et peut-être justifiée à juste titre si vous êtes un débutant en TypeScript, est comment quelque chose de si simple en apparence peut être un problème dans TypeScript ?

## Comprendre le problème

De manière générale, TypeScript détermine le type d'une variable lorsqu'elle est déclarée, et ce type déterminé ne change pas — c'est-à-dire qu'il reste le même tout au long de votre application.

Il existe des exceptions à cette règle lors de la prise en compte du rétrécissement de type ou du travail avec le type any, mais c'est une règle générale à retenir sinon.

Dans l'exemple précédent, l'objet `organization` est déclaré comme suit :

```ts
const organization = {}

```

Il n'y a pas de type explicite attribué à la variable `organization`, donc TypeScript infère le type de `organization` basé sur la déclaration comme étant `{}`, c'est-à-dire l'objet vide littéral.

Par exemple, si vous ajoutez un alias de type, vous pouvez explorer le type de `organization` :

```ts
type Org = typeof organization

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-81.png)
_Exploration du type d'objet littéral_

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/MYewdgzgLgBCBOBzAhmAlgL2VN4YF4YBvAXwCgyoBPABwFMYB5JAma+kAMziVU21xgKCFOiw5wAOjDIAtg0IAiAGLw6dUABMNcmoooxDR4ydNnzFy1es3bd4xSA).

Lorsque vous essayez ensuite de référencer la propriété `name` sur cet objet littéral vide :

```ts
organization.name = ...

```

TypeScript crie.

> La propriété 'name' n'existe pas sur le type '{}'.

Lorsque vous comprenez le problème, l'erreur semble appropriée.

Corrigeons cela.

## Comment résoudre l'erreur

Il existe de nombreuses façons de résoudre l'erreur TypeScript ici. Considérons celles-ci :

### 1. Typer explicitement l'objet au moment de la déclaration

C'est la solution la plus facile à comprendre.

Au moment où vous déclarez l'objet, allez-y et tapez-le. De plus, attribuez-lui toutes les valeurs pertinentes.

```ts
type Org = {
    name: string
}

const organization: Org = {
    name: "Freecodecamp"
}

```

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/C4TwDgpgBA8gTgcygXigbwFBW1AdgQwFsIAuKAZ2DgEtcEMBfDDAYwHtdKo3F9dqAXvmDUOZeElSYceIqSgAiAGJwIEdgBN1RMAsbMDQA).

Cela élimine toute surprise.

Vous déclarez clairement quel est ce type d'objet et vous déclarez correctement toutes les propriétés pertinentes lorsque vous créez l'objet.

Cependant, cela n'est pas toujours réalisable si les propriétés de l'objet doivent être ajoutées dynamiquement.

### 2. Utiliser une signature d'index d'objet

Occasionnellement, les propriétés de l'objet doivent vraiment être ajoutées à un moment ultérieur à celui de la déclaration.

Dans ce cas, vous pouvez utiliser la signature d'index d'objet comme suit :

```ts
type Org = {[key: string] : string}

const organization: Org = {}

organization.name = "Freecodecamp"

```

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/C4TwDgpgBA8gTgcygXigbwNoGsIgFxQDOwcAlgHYIC6UBxZlAvgFDMDGA9ucVB4gIblSAL37BSXAvCSo0LZnwSCRYieQB05fgFtoqAEQAxOBAicAJmZ1h9rO0A).

Au moment où la variable `organization` est déclarée, vous allez de l'avant et la tapez explicitement comme suit : `{[key: string] : string}`.

Pour expliquer davantage la syntaxe, vous pouvez être habitué aux types d'objets ayant des types de propriétés fixes :

```ts
type obj = {
  name: string
}

```

Mais vous pouvez également substituer `name` par un type de « variable ».

Par exemple, si vous voulez définir n'importe quelle propriété de chaîne sur `obj` :

```ts
type obj = {
 [key: string]: string
}

```

Notez que la syntaxe est similaire à la manière dont vous utiliseriez une propriété d'objet variable en JavaScript standard :

```ts
const variable = "name"

const obj = {
   [variable]: "Freecodecamp"
}

```

L'équivalent TypeScript est appelé une signature d'index d'objet.

De plus, notez que vous pourriez typer `key` avec d'autres primitives :

```ts
// number
type Org = {[key: number] : string}

// string
type Org = {[key: string] : string}

//boolean
type Org = {[key: boolean] : string}

```

### 3. Utiliser le type utilitaire Record

La solution ici est assez concise :

```ts
type Org = Record<string, string>

const organization: Org = {}


organization.name = "Freecodecamp"

```

Au lieu d'utiliser un alias de type, vous pouvez également mettre le type en ligne :

```ts
const organization: Record<string, string> = {}

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-82.png)
_Utilisation du type utilitaire Record_

Voir le [TypeScript playground](https://www.typescriptlang.org/play?#code/C4TwDgpgBA8gTgcygXigJQgYwPZwCYA8AzsHAJYB2CANFCeVQHwBQzOFJUuCAhhWQC8ewMtgoAuWIhRQA3gF9Wzbn0HDRFAHQUeAW2ioARADE4ELNjxY9YQ0tZA).

Le type utilitaire `Record` a la signature suivante : `Record<Keys, Type>`.

Il vous permet de contraindre un type d'objet dont les propriétés sont `Keys` et les valeurs des propriétés sont `Type`.

Dans notre exemple, `Keys` représente `string` et `Type`, `string` également.

## Conclusion

En dehors des primitives, les types les plus courants que vous devrez gérer sont probablement les types d'objets.

Dans les cas où vous devez construire un objet dynamiquement, tirez parti du type utilitaire Record ou utilisez la signature d'index d'objet pour définir les propriétés autorisées sur l'objet.

Notez que vous pouvez obtenir une version [PDF ou ePub](https://www.ohansemmanuel.com/cheatsheet/top-7-stack-overflowed-typescript-questions) de cette feuille de triche pour une référence plus facile, ou pour la lire sur votre Kindle ou tablette.

Merci d'avoir lu !

## Un livre gratuit sur TypeScript ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-78.png)
_Construire des composants React polymorphes fortement typés_

[Obtenez ce livre gratuitement](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).