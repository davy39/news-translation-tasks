---
title: Guide TypeScript et React Intermédiaire – Comment Construire des Composants
  Polymorphes Fortement Typés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-26T14:49:10.000Z'
originalURL: https://freecodecamp.org/news/build-strongly-typed-polymorphic-components-with-react-and-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/6Lc6ro2.png
tags:
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Guide TypeScript et React Intermédiaire – Comment Construire des Composants
  Polymorphes Fortement Typés
seo_desc: 'By Emmanuel Ohans

  Hey everyone! 😎 In this detailed guide, I’ll show you how to build strongly typed
  Polymorphic React components with Typescript.

  If you prefer to read the entire guide in a single PDF document, you can download
  the accompanying free...'
---

Par Emmanuel Ohans

Salut à tous ! 😊 Dans ce guide détaillé, je vais vous montrer comment construire des **composants React polymorphes fortement typés avec TypeScript**.

Si vous préférez lire l'ensemble du guide dans un seul document PDF, vous pouvez télécharger le [PDF gratuit accompagnant](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-173.png)
_Vous pouvez [télécharger l'eBook gratuitement](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components)._

## Table des matières

* [Dépôt Github](#heading-depot-github)
* [Public idéal pour ce livre](#heading-public-ideal-pour-ce-livre)
* [Qu'est-ce que les Composants Polymorphes ?](#heading-quest-ce-que-les-composants-polymorphes)
* [Exemples de Composants Polymorphes dans le Monde Réel](#heading-exemples-de-composants-polymorphes-dans-le-monde-reel)
* [Composants polymorphes dans Chakra UI](#heading-composants-polymorphes-dans-chakra-ui)
* [La prop component de Material UI](#heading-la-prop-component-de-material-ui)
* [Comment Construire Votre Premier Composant Polymorphe](#heading-comment-construire-votre-premier-composant-polymorphe)
* [Les Problèmes avec Cette Implémentation Simple](#heading-les-problemes-avec-cette-implementation-simple)
* [Bienvenue, TypeScript](#heading-bienvenue-typescript)
* [Introduction aux Génériques TypeScript](#heading-introduction-aux-generiques-typescript)
* [Comment Contraindre les Génériques](#heading-comment-contraindre-les-generiques)
* [Assurer que la prop Polymorphe n'accepte que des chaînes HTML valides](#heading-assurer-que-la-prop-as-naccepte-que-des-chaines-html-valides)
* [Comment Gérer les Attributs Valides des Composants](#heading-comment-gerer-les-attributs-valides-des-composants)
* [Comment Gérer les Props Polymorphes par Défaut](#heading-comment-gerer-les-props-as-par-defaut)
* [Le Composant Doit Être Réutilisable avec ses Props](#heading-le-composant-doit-etre-reutilisable-avec-ses-props)
* [Comment Créer un Utilitaire Réutilisable pour les Types Polymorphes](#heading-comment-creer-un-utilitaire-reutilisable-pour-les-types-polymorphes)
* [Le Composant Doit Supporter les Refs](#heading-le-composant-doit-supporter-les-refs)
* [Conclusion et Prochaines Étapes](#heading-conclusion-et-prochaines-etapes)

## Dépôt Github

Le [dépôt Github](https://github.com/ohansemmanuel/polymorphic-react-component) contient toute l'implémentation du code de ce guide.

## Public idéal pour ce livre

Si vous n'avez aucune idée de ce que signifie des composants React polymorphes fortement typés avec TypeScript, ce n'est pas grave. C'est un bon indicateur que ce guide est fait pour vous.

Ce guide a été écrit spécifiquement pour les débutants et les développeurs de niveau intermédiaire. Cela vous aidera à apprendre des concepts TypeScript plus avancés de manière pratique.

Prêt ? Plongeons-nous.

## Qu'est-ce que les Composants Polymorphes ?

Lorsque vous apprenez React, l'un des premiers concepts que vous apprenez est comment construire des composants réutilisables.

C'est l'art de écrire des composants une fois et de les réutiliser plusieurs fois.

Si vous vous souvenez de React 101, les blocs de construction essentiels des composants réutilisables classiques sont les props et l'état — où les props sont externes et l'état est interne.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-129.png)
_Blocs de construction des composants réutilisables_

Les blocs de construction essentiels de la réutilisabilité restent valables pour cet article. Cependant, nous allons tirer parti des props pour permettre aux utilisateurs de votre composant de décider quel « élément » rendre finalement.

D'accord, attendez, ne soyez pas confus par cela.

Considérez le composant React suivant :

```js
const MyComponent = (props) => {
  return (
    <div>
     C'est un excellent composant avec des props {JSON.stringify(props)}
   </div>
  );
};
```

Typiquement, votre composant recevrait certaines props. Vous les utiliseriez en interne et rendriez finalement un élément React qui est traduit en l'élément DOM correspondant. Dans ce cas, l'élément div.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-131.png)
_Rendu d'un seul élément_

Et si votre composant pouvait prendre des props pour faire plus que simplement fournir des données à consommer dans votre composant ?

Au lieu que `MyComponent` rende toujours un `div`, et si vous pouviez passer une prop pour déterminer l'élément finalement rendu dans le `DOM` ?

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-132.png)
_Une illustration sur la décision de l'UI de rendu d'un composant_

C'est là que les composants polymorphes entrent en jeu.

Par définition standard, le mot _Polymorphe_ signifie se produisant sous plusieurs formes. Dans le monde des composants React, un composant polymorphe est un composant qui peut être rendu avec un élément/conteneur différent.

Même si le concept peut vous sembler étrange (si vous êtes nouveau dans ce domaine en général), vous avez probablement déjà utilisé un composant polymorphe.

## Exemples de Composants Polymorphes dans le Monde Réel

Les bibliothèques de composants open-source implémentent généralement une sorte de composant polymorphe.

Considérons quelques exemples que vous pourriez connaître.

Je ne discuterai peut-être pas de votre bibliothèque open-source préférée, mais n'hésitez pas à jeter un coup d'œil à votre bibliothèque OS préférée après avoir compris les exemples ici.

### Composants polymorphes dans Chakra UI

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-133.png)
_Chakra UI_

[Chakra UI](https://chakra-ui.com/) a été ma bibliothèque de composants de choix pour un nombre décent d'applications de production.

Elle est facile à utiliser, prend en charge le thème sombre et est accessible par défaut (oh, sans oublier les animations subtiles des composants !).

Alors, comment Chakra UI implémente-t-elle les props polymorphes ? La réponse est en exposant une prop `as`.

La prop `as` est passée à un composant pour déterminer quel élément conteneur final rendre.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CleanShot-2022-05-24-at-20.33.33@2x.png)
_La prop as de Chakra UI utilisée avec le composant Box_

L'utilisation de la prop `as` est assez simple.

Vous la passez au composant, dans ce cas, `Box` :

```js
<Box as="button"> Hello </Box>
```

Et le composant rendra un élément button.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CleanShot-2022-05-24-at-20.34.22@2x.png)
_Le composant Box rendu en tant qu'élément "button"_

Si vous changiez la prop `as` en `h1` :

```js
<Box as="h1"> Hello </Box>
```

Maintenant, le composant `Box` rend un h1 :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CleanShot-2022-05-24-at-20.40.06@2x-1.png)
_Le composant Box rendu en tant qu'élément "h1"_

C'est un composant polymorphe en action !

Ce composant peut être rendu en éléments entièrement uniques, simplement en passant une seule prop.

### La prop component de Material UI

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-134.png)
_La bibliothèque de composants Material UI_

Material UI, dans la plupart des cas, ne nécessite aucune introduction. C'est une référence des bibliothèques de composants depuis des années. C'est une bibliothèque de composants robuste avec une base d'utilisateurs mature.

Similaire à Chakra UI, Material UI permet une prop polymorphe appelée `component` — peu importe ce que vous choisissez d'appeler votre prop polymorphe (par exemple, Chakra UI l'appelle `as`).

Son utilisation est similaire. Vous la passez à un composant, en indiquant quel élément ou composant personnalisé vous souhaitez rendre.

Assez parlé, voici un exemple des docs officiels :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/CleanShot-2022-05-24-at-20.41.34@2x.png)
_La prop component de Material UI_

```jsx
<List component="nav">
 <ListItem button>
   <ListItemText primary="Trash" />
 </ListItem>
</List>
```

`List` reçoit une prop component de `nav`, donc lorsqu'elle est rendue, elle rendra un élément conteneur `nav`.

Un autre utilisateur peut utiliser le même composant, mais pas comme navigation. Il peut simplement vouloir rendre une liste de tâches :

```jsx
<List component="ol">
...
</List>
```

Et dans ce cas, List rendra un élément de liste ordonnée `ol`.

Parlez de flexibilité ! Vous pouvez voir un résumé des [cas d'utilisation ici](https://github.com/ohansemmanuel/polymorphic-react-component/blob/master/use-cases.pdf) (PDF) pour les composants polymorphes.

Comme vous le verrez dans les sections suivantes de ce manuel, les composants polymorphes sont puissants. En plus d'accepter simplement une prop de type d'élément, ils peuvent également accepter des composants personnalisés en tant que props.

Nous en discuterons dans une section à venir de ce guide. Pour l'instant, commençons à construire votre premier composant polymorphe !

![Image](https://www.freecodecamp.org/news/content/images/2022/05/stprc-meta-2.png)
_[Le ebook Construire des Composants React Polymorphes Fortement Typés](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components)_

Si vous êtes sérieux pour devenir un développeur React TypeScript pro, vous pouvez [télécharger le ebook gratuit accompagnant](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components). Je vous enverrai également une newsletter gratuite par e-mail sur TypeScript dans le monde réel intitulée : **5 secrets TypeScript que vous ne connaissiez pas.** Vous pouvez [l'obtenir ici](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).

## Comment Construire Votre Premier Composant Polymorphe

Contrairement à ce que vous pourriez penser, construire votre premier composant polymorphe est assez simple.

Voici une implémentation de base :

```jsx
const MyComponent = ({ as, children }) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Ce qu'il faut noter ici, c'est la prop polymorphe `as` — similaire à celle de Chakra UI. C'est la prop exposée pour contrôler l'élément de rendu du composant polymorphe.

Deuxièmement, notez que la prop `as` n'est pas rendue directement. Ce qui suit serait incorrect :

```jsx
const MyComponent = ({ as, children }) => {
  // mauvais rendu ci-dessous 👋
  return <as>{children}</as>;
};
```

Lors du rendu d'un [type d'élément à l'exécution](https://reactjs.org/docs/jsx-in-depth.html#choosing-the-type-at-runtime), vous devez d'abord l'assigner à une variable en majuscule, puis rendre la variable en majuscule.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-135.png)
_Utilisation d'une variable en majuscule dans un composant React_

Vous pouvez maintenant utiliser ce composant comme suit :

```jsx
<MyComponent as="button">Hello Polymorphe!</MyComponent>
<MyComponent as="div">Hello Polymorphe!</MyComponent>
<MyComponent as="span">Hello Polymorphe!</MyComponent>
<MyComponent as="em">Hello Polymorphe!</MyComponent>
```

Notez la différente prop `as` passée aux composants rendus ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-136.png)
_Les différents éléments rendus du composant_

## Les Problèmes avec Cette Implémentation Simple

L'implémentation de la section précédente, bien que standard, présente plusieurs problèmes.

Explorons certains d'entre eux.

### 1. La prop `as` peut recevoir des éléments HTML invalides.

Actuellement, il est possible pour un utilisateur d'écrire ce qui suit :

```tsx
<MyComponent as="emmanuel">Hello Wrong Element</MyComponent>
```

La prop `as` passée ici est `emmanuel`.

`Emmanuel` est un élément `HTML` incorrect, mais le navigateur essaie également de rendre cet élément.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-152.png)
_Rendu d'un type d'élément HTML incorrect_

Une expérience de développement idéale consiste à montrer une sorte d'erreur pendant le développement. Par exemple, un utilisateur peut faire une simple faute de frappe : `divv` au lieu de `div` — et n'aurait aucune indication de ce qui ne va pas.

### 2. Des attributs incorrects peuvent être passés pour des éléments valides.

Considérez l'utilisation suivante du composant :

```tsx
<MyComponent as="span" href="https://www.google.com">
   Hello Wrong Attribute
</MyComponent>
```

Un consommateur peut passer un élément `span` à la prop `as`, et une prop `href` également.

Cela est techniquement invalide.

Un élément `span` ne prend pas (et ne devrait pas) un attribut `href`. C'est une syntaxe `HTML` invalide.

Cependant, maintenant, un consommateur du composant que nous avons construit pourrait écrire cela et n'aurait aucune erreur pendant le développement.

### 3. Aucune prise en charge des attributs !

Considérez à nouveau l'implémentation simple :

```tsx
const MyComponent = ({ as, children }) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Les seules props que ce composant accepte sont `as` et children, rien d'autre. Il n'y a aucune prise en charge des attributs, même pour les props d'éléments `as` valides. C'est-à-dire, si `as` était un élément d'ancrage `a`, nous devrions également prendre en charge le passage d'un `href` au composant.

```tsx
<MyComponent as="a" href="...">A link </MyComponent>
```

Même si `href` est passé dans l'exemple ci-dessus, l'implémentation du composant ne reçoit aucune autre prop. Seules `as` et children sont déstructurées.

Vos premières pensées pourraient être de passer toutes les autres props au composant comme suit :

```jsx
const MyComponent = ({ as, children, ...rest }) => { 
  const Component = as || "span";

  return <Component {...rest}>{children}</Component>;
};
```

Cela semble être une solution décente, mais cela met maintenant en évidence le deuxième problème mentionné ci-dessus. Les mauvais attributs seront également passés au composant.

Considérez ce qui suit :

```jsx
<MyComponent as="span" href="https://www.google.com">
  Hello Wrong Attribute
</MyComponent>
```

Et notez le balisage rendu final :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-153.png)
_Un élément span avec un attribut href_

Un span avec un `href` est un `HTML` invalide.

Comment résoudre ces préoccupations ?

Pour être clair, il n'y a pas de baguette magique à agiter ici. Cependant, nous allons tirer parti de TypeScript pour nous assurer que vous construisez des composants polymorphes fortement typés.

Une fois terminé, les développeurs utilisant votre composant éviteront les erreurs d'exécution ci-dessus et les attraperont plutôt pendant le développement ou le temps de construction — grâce à TypeScript.

### Pourquoi est-ce mauvais ?

Pour récapituler, notre implémentation simple est médiocre parce que :

* Elle offre une mauvaise expérience développeur
* Elle n'est pas sécurisée en termes de types. Des bugs peuvent (et vont) s'immiscer.

## Bienvenue, TypeScript

Si vous lisez ceci, un prérequis est que vous connaissez déjà un peu de `TypeScript` — au moins les bases. Si vous n'avez aucune idée de ce qu'est TypeScript, je vous recommande fortement de lire ce [document](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html) d'abord.

D'accord, nous avons établi un point de départ — c'est-à-dire que nous allons tirer parti de TypeScript pour résoudre les préoccupations que nous venons de discuter. Essentiellement, nous allons tirer parti de TypeScript pour construire des composants polymorphes fortement typés.

Les deux premières exigences que nous allons commencer incluent :

* La prop `as` ne doit pas recevoir de chaînes d'éléments `HTML` invalides
* Les mauvais attributs ne doivent pas être passés pour des éléments valides

Dans la section suivante, nous verrons comment TypeScript peut rendre notre solution plus robuste, conviviale pour les développeurs et digne de production.

## Introduction aux Génériques TypeScript

Si vous avez une bonne compréhension des génériques TypeScript, vous pouvez sauter cette section. Cela ne fournit qu'une brève introduction pour les lecteurs qui ne sont pas aussi familiers avec les génériques.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-154.png)
_Illustration : Les variables Javascript et les génériques Typescript sont identiques_

### Qu'est-ce que les Génériques en TypeScript ?

Si vous êtes nouveau dans les génériques TypeScript, ils peuvent sembler difficiles. Mais une fois que vous avez compris, vous les verrez pour ce qu'ils sont vraiment : une construction apparemment simple pour paramétrer vos types.

Alors, qu'est-ce que les génériques ?

Un modèle mental simple que vous pouvez utiliser pour aborder les génériques est de les voir comme des variables spéciales pour vos types. Là où JavaScript a des variables, TypeScript a des génériques (pour les types).

Jetons un coup d'œil à un exemple classique.

Ci-dessous se trouve une fonction `echo` où `v` représente n'importe quelle valeur arbitraire :

```jsx
const echo = (v) => {
  console.log(v)
  return v
}
```

La fonction `echo` prend cette valeur v, la journalise dans la console, puis retourne la même valeur à l'appelant. Aucune transformation d'entrée effectuée !

Maintenant, nous pouvons utiliser cette fonction sur différents types d'entrée :

```js
echo(1) // number
echo("hello world") // string
echo({}) // object
```

Et cela fonctionne parfaitement.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-155.png)
_Le bloc de code de la fonction echo_

Il y a juste un problème. Nous n'avons pas typé cette fonction du tout.

Ajoutons un peu de TypeScript ici. 🧑‍🍳

Commencez par une manière naïve d'accepter n'importe quelle valeur d'entrée `v` en utilisant le mot-clé `any` :

```js
const echo = (v: any) => {
  console.log(v)
  return v
}
```

Cela semble fonctionner.

Vous n'aurez aucune erreur TypeScript lorsque vous ferez cela. Cependant, si vous regardez où vous invoquez cette fonction, vous remarquerez une chose importante : vous avez maintenant perdu toute forme de sécurité de type.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-156.png)
_Le type any utilisé dans la fonction echo_

Cela peut ne pas être clair maintenant, mais si vous effectuiez une opération comme suit :

```ts
const result = echo("hello world")
let failure = result.hi.me
```

La ligne 2 échouera avec une erreur.

```tsx
let failure = result.hi.me
```

`result` est techniquement une `string` car echo retournera la string `hello world`, et `"hello world".hi.me` lancera une erreur.

Cependant, en typant `v` comme `any`, `result` est également typé comme `any`. Cela est dû au fait que `echo` retourne la même valeur. TypeScript infère le type de retour comme étant le même que `v`. c'est-à-dire, any.

Avec `result` étant de type `any`, vous n'avez aucune sécurité de type ici. TypeScript ne peut pas attraper cette erreur. C'est l'un des inconvénients de l'utilisation de `any`.

D'accord, utiliser `any` ici est une mauvaise idée. Évitons-le.

Que pourriez-vous faire d'autre ?

Une autre solution serait d'épeler exactement quels types sont acceptables par la fonction `echo`, comme suit :

```tsx
const echo = (v: string | number | object) => {
  console.log(v);
  return v;
};
```

Essentiellement, vous représentez v avec un type d'union.

`v` peut être soit une `string`, un `number` ou un `object`.

Cela fonctionne très bien.

Maintenant, si vous allez de l'avant et accédez incorrectement à une propriété sur le type de retour de echo, vous obtiendrez une erreur appropriée. Par exemple,

```js
const result = echo("hi").hi
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-157.png)
_Erreur "La propriété "hi" n'existe pas"_

Vous obtiendrez l'erreur suivante : La propriété 'hi' n'existe pas sur le type 'string | number | object'.

Cela semble parfait.

Nous avons représenté v avec une gamme décente de valeurs acceptables.

Cependant, que faire si vous vouliez accepter plus de types de valeurs ? Vous devriez continuer à ajouter plus de types d'union.

Y a-t-il une meilleure façon de gérer cela ? Par exemple, en déclarant un type de variable basé sur ce que l'utilisateur passe à `echo` ?

Pour commencer, remplaçons le type d'union par un type hypothétique que nous appellerons `Value` :

```ts
const echo = (v: Value) => {
  console.log(v);
  return v;
};
```

Une fois que vous faites cela, vous obtiendrez l'erreur TypeScript suivante :

```ts
Impossible de trouver le nom 'Value'.ts (2304)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-158.png)
_Erreur "Impossible de trouver le nom "Value""_

Cela est attendu.

Cependant, voici la beauté des génériques. Nous pouvons définir ce type `Value` comme un générique — une sorte de variable représentée par le type de `v` passé à echo lors de l'invocation.

Pour compléter cela, nous utiliserons des chevrons juste après le signe `=` comme suit :

```ts
const echo = <Value> (v: Value) => {
  console.log(v);
  return v;
};
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-159.png)
_Le générique "Value"_

Si vous codez en même temps, vous remarquerez qu'il n'y a plus d'erreurs TypeScript. TypeScript comprend qu'il s'agit d'un générique. Le type Value est un générique.

Mais comment TypeScript sait-il ce qu'est Value ?

Eh bien, c'est là que la forme variable d'un générique devient évidente.

Jetez un coup d'œil à la façon dont echo est invoqué :

```ts
echo(1)
echo("hello world")
echo({})
```

Le générique `Value` prendra le type de l'argument passé dans echo au moment de l'invocation.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-160.png)
_Le générique Value représente le type d'argument de la fonction_

Par exemple, avec `echo(1)`, le type de `Value` sera le nombre littéral `1`. Pour `echo("hello world")`, le type de `Value` sera la chaîne littérale `hello world`.

Remarquez comment cela change en fonction du type d'argument passé à `echo`.

C'est merveilleux.

Si vous effectuiez des opérations sur le type de retour de echo, vous obtiendriez toute la sécurité de type que vous attendez — sans spécifier un seul type mais en représentant l'entrée avec un **générique**, alias un type variable.

### Comment contraindre les génériques

Ayant appris les bases des génériques, il y a un autre concept à comprendre avant de revenir à l'utilisation de TypeScript dans notre solution de composant polymorphe.

Considérons une variante de la fonction echo. Appelons cela `echoLength` :

```js
const echoLength = <Value> (v: Value) => {
  console.log(v.length);
  return v.length;
};
```

Au lieu d'échoir la valeur d'entrée v, la fonction échoit la longueur de la valeur d'entrée, c'est-à-dire `v.length`.

Si vous écriviez ce code tel quel, le compilateur TypeScript crierait avec une erreur :

```ts
La propriété 'length' n'existe pas sur le type 'Value'.ts (2339)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-161.png)
_Erreur "La propriété 'length' n'existe pas"_

C'est une erreur assez importante.

Le paramètre `echoLength`, `v`, est représenté par le générique `Value` — qui en fait représente le type de l'argument passé à la fonction.

Cependant, dans le corps de la fonction, nous accédons à la propriété `length` du paramètre variable.

Alors, quel est le problème ici ?

Le problème est que toutes les entrées n'auront pas une propriété `length`.

Le générique `Value` tel qu'il est représente n'importe quel type d'argument passé par l'appelant de la fonction — mais tous les types d'arguments n'auront pas une propriété `length`.

Considérez ce qui suit :

```js
echoLength("hello world")
echoLength(2)
echoLength({})
```

`echoLength("hello world")` fonctionnera comme prévu car une `string` a une propriété `length`.

Cependant, les deux autres exemples retourneront undefined. Les nombres et les objets n'ont pas de propriétés de longueur. Donc le code dans le corps de la fonction n'est pas le plus sûr en termes de type.

Maintenant, comment corrigeons-nous cela ?

Nous devons pouvoir prendre un générique, mais nous voulons spécifier exactement quel type de générique est valide.

En termes plus techniques, nous devons contraindre le générique accepté par cette fonction pour qu'il soit limité aux types qui ont une propriété de longueur.

Pour accomplir cela, nous allons utiliser le mot-clé `extends`.

Jetez un coup d'œil :

```ts
const echoLength = <Value extends {length: number}> (v: Value) => {
    console.log(v.length);
    return v.length;
};
```

Maintenant, lorsque vous déclarez le générique `Value`, ajoutez `extends {length: number}` pour indiquer que le générique sera contraint aux types qui ont une propriété de longueur.

Si vous utilisez `echoLength` comme avant, vous devriez maintenant obtenir une erreur TypeScript lorsque vous passez des valeurs sans propriété de longueur, par exemple :

```js
// ceux-ci produiront une erreur typescript
echoLength(2)
echoLength({})
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-162.png)
_Erreur "L'argument de type number n'est pas assignable"_

Ce que nous avons fait ici, c'est contraindre le générique `Value` à un moule spécifique. Oui, nous voulons des types variables. Mais nous ne voulons que ceux qui correspondent à ce moule spécifique, c'est-à-dire qui correspondent à une certaine signature de type.

Magnifique !

Maintenant que vous comprenez ces deux concepts, nous allons maintenant revenir à la mise à jour de notre solution de composant polymorphe pour qu'elle soit beaucoup plus sûre en termes de type — en commençant par les exigences initiales que nous allons définir.

### Assurer que la prop `as` ne reçoit que des chaînes d'éléments HTML valides

Voici notre solution actuelle :

```tsx
const MyComponent = ({ as, children }) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Pour rendre les sections suivantes de ce guide pratiques, nous allons changer le nom du composant de MyComponent à `Text`. C'est-à-dire, supposons que nous construisons un composant Text polymorphe.

Maintenant, avec vos connaissances en génériques, il devient clair que nous sommes mieux de représenter as avec un type générique, c'est-à-dire un type variable basé sur ce que l'utilisateur passe.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-163.png)
_La prop as : une variable passée par l'utilisateur lorsque le composant est rendu_

Allons-y et faisons le premier pas comme suit :

```jsx
export const Text = <C>({
  as,
  children,
}: {
  as?: C;
  children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Notez comment le générique `C` est défini puis passé dans la définition de type pour la prop `as`.

Cependant, si vous écriviez ce code apparemment parfait, vous auriez TypeScript criant de nombreuses erreurs avec plus de lignes rouges ondulées que vous ne le souhaiteriez 🧑‍♀️

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-164.png)
_Le bloc de code d'erreur générique JSX_

Ce qui se passe ici est un défaut dans la [syntaxe des génériques](https://stackoverflow.com/questions/32308370/what-is-the-syntax-for-typescript-arrow-functions-with-generics?) dans les fichiers `.tsx`. Il y a deux façons de résoudre cela.

**1. Ajoutez une virgule après la déclaration du générique.**

C'est la syntaxe pour déclarer plusieurs génériques. Une fois que vous faites cela, le compilateur TypeScript comprend clairement votre intention et l'erreur est bannie.

```jsx
// notez la virgule après "C" ci-dessous 👋
export const Text = <C,>({
as,
children,
}: {
as?: C;
 children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

**2. Contraignez le générique.**

La deuxième option est de contraindre le générique comme vous le jugez approprié. Pour commencer, vous pouvez simplement utiliser le type unknown comme suit :

```jsx
// notez le mot-clé extends ci-dessous 👋
export const Text = <C extends unknown>({
  as,
  children,
}: {
  as?: C;
  children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Pour l'instant, je vais m'en tenir à la solution 2 car elle est plus proche de notre solution finale. Dans la plupart des cas, j'utilise la syntaxe des génériques multiples (ajout d'une virgule).

D'accord, maintenant, que faire ensuite ?

Avec notre solution actuelle, nous obtenons une autre erreur TypeScript :

```ts
Le type d'élément JSX 'Component' n'a aucune signature de constructeur ou d'appel.ts(2604)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-165.png)
_Erreur "Aucune signature de constructeur ou d'appel" mise en évidence_

Cela est similaire à l'erreur que nous avions lorsque nous avons travaillé avec la fonction `echoLength`. Tout comme l'accès à la propriété length d'un type de variable inconnu, on peut en dire autant ici.

Essayer de rendre n'importe quel type générique comme un composant React valide n'a pas de sens.

Nous devons contraindre le générique UNIQUEMENT pour qu'il corresponde au moule d'un type d'élément React valide.

Pour y parvenir, nous allons utiliser le type interne React : `React.ElementType`, et nous assurer que le générique est contraint pour correspondre à ce type :

```jsx
// regardez juste après le mot-clé extends 👋
export const Text = <C extends React.ElementType>({
  as,
  children,
}: {
  as?: C;
  children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Notez que si vous êtes sur une version plus ancienne de React, vous devrez peut-être importer React comme suit : `**import** **React** **from** **'react'**`**.**

Avec cela, nous n'avons plus d'erreurs !

Maintenant, si vous utilisez ce composant comme suit, cela fonctionnera très bien :

```jsx
<Text as="div">Hello Text world</Text>
```

Cependant, si vous passez une prop `as` invalide, vous obtiendrez maintenant une erreur TypeScript appropriée. Considérez l'exemple ci-dessous :

```jsx
<Text as="emmanuel">Hello Text world</Text>
```

Et l'erreur lancée :

```ts
Le type '"emmanuel"' n'est pas assignable au type 'ElementType<any> | undefined'.
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-166.png)
_Erreur "Le type 'emmanuel' n'est pas assignable" mise en évidence_

C'est excellent !

Nous avons maintenant une solution qui n'accepte pas de charabia pour la prop `as` et qui empêchera également les vilaines fautes de frappe, par exemple `divv` au lieu de `div`.

C'est une bien meilleure expérience développeur.

## Comment Gérer les Attributs Valides des Composants

En résolvant ce deuxième cas d'utilisation, vous allez apprécier à quel point les génériques sont vraiment puissants.

Tout d'abord, vous devez comprendre ce que nous essayons d'accomplir ici.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-167.png)
_Illustration montrant les props : "as" et autres attributs valides_

Une fois que nous recevons un générique comme type, nous voulons nous assurer que les props restantes passées à notre composant sont pertinentes, en fonction de la prop `as`.

Donc, par exemple, si un utilisateur passait une prop `as` de img, nous voulons que href soit également une prop valide !

Pour vous donner une idée de la manière dont nous allons accomplir cela, jetez un coup d'œil à l'état actuel de notre solution :

```jsx
export const Text = <C extends React.ElementType>({
  as,
  children,
}: {
  as?: C;
  children: React.ReactNode;
}) => {
  const Component = as || "span";

  return <Component>{children}</Component>;
};
```

Les props de ce composant sont maintenant représentées par le type d'objet :

```jsx
{
  as?: C;
  children: React.ReactNode;
}

```

En pseudocode, ce que nous aimerions serait ce qui suit :

```jsx
{
  as?: C;
  children: React.ReactNode;
 } & {...otherValidPropsBasedOnTheValueOfAs}
```

Cette exigence est suffisante pour laisser quelqu'un à court d'idées. Nous ne pouvons pas écrire une fonction qui détermine les types appropriés en fonction de la valeur de `as`, et ce n'est pas intelligent de lister manuellement un type d'union.

Eh bien, que se passerait-il s'il existait un type fourni par React qui agissait comme une « fonction » qui retournerait des types d'éléments valides en fonction de ce que vous lui passez ?

Avant d'introduire la solution, faisons un peu de refactorisation. Tirons les props du composant dans un type séparé.

```jsx
// 👋 Voir TextProps extrait ci-dessous
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
}

export const Text = <C extends React.ElementType>({
  as,
  children,
}: TextProps<C>) => { // 👈 voir TextProps utilisé
  const Component = as || "span";
  return <Component>{children}</Component>;
};
```

Ce qui est important ici, c'est de noter comment le générique est passé à `TextProps<C>`. Similaire à un appel de fonction en JavaScript — mais avec des chevrons.

Maintenant, passons à la solution.

La baguette magique ici est d'utiliser le type `React.ComponentPropsWithoutRef` comme montré ci-dessous :

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>; // 👈 regardez ici

export const Text = <C extends React.ElementType>({
  as,
  children,
}: TextProps<C>) => {
  const Component = as || "span";
  return <Component>{children}</Component>;
};
```

Notez que nous introduisons une intersection ici. Essentiellement, nous disons que le type de `TextProps` est un type d'objet contenant `as` et `children`, et certains autres types représentés par `React.ComponentPropsWithoutRef`.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-168.png)
_La collection des props du composant et d'autres props basées sur la prop "as"_

Si vous lisez le code, cela devient peut-être apparent ce qui se passe ici.

En fonction du type de `as`, représenté par le générique `C`, `React.componentPropsWithoutRef` retournera des props de composant valides qui correspondent à l'attribut `string` passé à la prop as.

Il y a un autre point significatif à noter.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-169.png)
_Exploration des différentes variantes de types ComponentProps_

Si vous commencez à taper et que vous vous fiez à l'intellisense de votre éditeur, vous réaliserez qu'il existe trois variantes du type `React.ComponentProps`...

1. `React.ComponentProps`
2. `React.ComponentPropsWithRef`
3. `React.ComponentPropsWithoutRef`

Si vous tentiez d'utiliser le premier, ComponentProps, vous verriez une note pertinente qui dit :

> Préférez ComponentPropsWithRef, si la ref est transmise, ou ComponentPropsWithoutRef lorsque les refs ne sont pas supportées.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-170.png)
_Note pour préférer ComponentPropsWithRef ou ComponentPropsWithoutRef_

Et c'est précisément ce que nous avons fait.

Pour l'instant, nous ignorerons le cas d'utilisation pour supporter une prop ref et nous en tiendrons à ComponentPropsWithoutRef.

Maintenant, essayons la solution !

Si vous utilisez ce composant de manière incorrecte, par exemple en passant une prop `as` valide avec d'autres props incompatibles, vous obtiendrez une erreur.

```jsx
<Text as="div" href="www.google.com">Hello Text world</Text>
```

Une valeur de `div` est parfaitement valide pour la prop as, mais un div ne devrait PAS avoir un attribut href. C'est incorrect, et correctement capturé par TypeScript avec l'erreur : La propriété 'href' n'existe pas sur le type ...

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-171.png)
_Erreur : La propriété href n'existe pas_

C'est génial ! Nous avons une solution encore meilleure (robuste).

Enfin, assurez-vous de transmettre d'autres props à l'élément rendu :

```tsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>; 

export const Text = <C extends React.ElementType>({
  as,
  children,
  ...restProps, // 👈 regardez ici
}: TextProps<C>) => {
  const Component = as || "span";
	
  // voir restProps passé 👋
  return <Component {...restProps}>{children}</Component>;
};
```

Continuons 👍🏼

## Comment Gérer les Attributs `as` par Défaut

Considérez notre solution actuelle :

```jsx
export const Text = <C extends React.ElementType>({
 as,
 children,
...restProps
}: TextProps<C>) => {
 const Component = as || "span"; // 👈 regardez ici

 return <Component {...restProps}>{children}</Component>;
};
```

Portons une attention particulière à l'endroit où un élément par défaut est fourni si la prop `as` est omise.

```jsx
const Component = as || "span"
```

Cela est correctement représenté dans le monde JavaScript, c'est-à-dire par implémentation, si `as` est optionnel, il sera par défaut un span.

La question est, comment TypeScript gère-t-il ce cas ? Comme lorsque `as` n'est pas passé ? Passons-nous également un type par défaut ?

Eh bien, la réponse est non. Mais voici un exemple pratique.

Si vous utilisez le composant Text comme suit :

```jsx
<Text>Hello Text world</Text>
```

Notez que nous n'avons passé aucune prop `as` ici. TypeScript sera-t-il conscient des props valides pour ce composant ?

Allons-y et ajoutons un href :

```jsx
<Text href="https://www.google.com">Hello Text world</Text>
```

Si vous faites cela, vous n'aurez aucune erreur.

C'est mauvais.

Un span ne devrait pas recevoir une prop/attribut href. Bien que nous définissions par défaut un span dans l'implémentation, TypeScript n'est pas conscient de cette implémentation par défaut. Corrigons cela avec une affectation par défaut générique simple :

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>;

/**
* Voir la valeur par défaut ci-dessous. TS traitera l'élément rendu comme un
span et fournira les typages en conséquence
*/
export const Text = <C extends React.ElementType = "span">({
  as,
  children,
...restProps
}: TextProps<C>) => {
  const Component = as || "span";
  return <Component {...restProps}>{children}</Component>;
};
```

Le point important est mis en évidence ci-dessous :

```jsx
<C extends React.ElementType = "span">
```

Et voilà ! L'exemple précédent que nous avions devrait maintenant lancer une erreur, c'est-à-dire lorsque vous passez href au composant Text sans prop `as`.

L'erreur devrait indiquer : La propriété 'href' n'existe pas sur le type ...

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-172.png)
_Erreur "href n'est pas assignable..." (comme prévu)_

## Le Composant Doit Être Réutilisable avec ses Props

Notre solution actuelle est bien meilleure que celle avec laquelle nous avons commencé. Faites-vous une tape dans le dos pour être arrivé jusqu'ici. Cependant, cela devient encore plus intéressant à partir de maintenant.

Le cas d'utilisation à prendre en compte dans cette section est très applicable dans le monde réel. Il y a une forte probabilité que si vous construisez un certain type de composant, alors ce composant prendra également certaines props spécifiques, qui sont uniques au composant.

Notre solution actuelle prend en considération les props `as`, children, et autres props de composant basées sur la prop `as`. Mais que se passe-t-il si nous voulions que ce composant gère ses propres props ?

Rendons cela pratique.

Nous allons faire en sorte que le composant `Text` reçoive une prop `color`. Le `color` ici sera l'une des couleurs de l'arc-en-ciel, ou `black`.

Nous allons représenter cela comme suit :

```jsx
type Rainbow =
| "red"
| "orange"
| "yellow"
| "green"
| "blue"
| "indigo"
| "violet";
```

Ensuite, nous devons définir la prop `color` dans l'objet `TextProps` comme suit :

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black"; // 👈 regardez ici
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>;
```

Avant de continuer, faisons un peu de refactorisation.

Représentons les props `réelles` du composant `Text` par un objet `Props`, et typons uniquement les props spécifiques à notre composant dans l'objet `TextProps`.

Cela deviendra clair, comme vous le verrez ci-dessous :

```jsx
// nouveau type "Props"
type Props <C extends React.ElementType> = TextProps<C>

export const Text = <C extends React.ElementType = "span">({
as,
children,
...restProps,
}: Props<C>) => {
const Component = as || "span";
return <Component {...restProps}>{children}</Component>;

```

Maintenant, nettoyons `TextProps` :

```jsx
// avant 
type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black"; // 👈 regardez ici
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<C>;

// après
type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black";
};
```

Maintenant, `TextProps` ne devrait contenir que les props spécifiques à notre composant `Text` : `as` et `color`.

Nous devons maintenant mettre à jour la définition de `Props` pour inclure les types que nous avons supprimés de `TextProps`, c'est-à-dire `children` et `React.ComponentPropsWithoutRef<C>`.

Pour la prop `children`, nous allons tirer parti de la prop `React.PropsWithChildren`.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-141.png)
_Le type PropsWithChildren injecte la prop children_

La façon dont `PropsWithChildren` fonctionne est facile à comprendre. Vous lui passez les props de votre composant, et il injectera la définition des props children pour vous.

Tirons parti de cela ci-dessous :

```jsx
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>>
```

Notez comment nous utilisons les chevrons.

C'est la syntaxe pour transmettre les génériques. Essentiellement, `React.PropsWithChildren` accepte les props de votre composant comme un générique et les augmente avec la prop children. Super !

Pour `React.ComponentPropsWithoutRef<C>`, nous allons simplement utiliser un type d'intersection ici :

```jsx
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> & 
React.ComponentPropsWithoutRef<C>
```

Et voici la solution complète actuelle :

```jsx
type Rainbow =
  | "red"
  | "orange"
  | "yellow"
  | "green"
  | "blue"
  | "indigo"
  | "violet";

type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black";
};

type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> & 
React.ComponentPropsWithoutRef<C>

export const Text = <C extends React.ElementType = "span">({
  as,
  children,
}: Props<C>) => {
  const Component = as || "span";
  return <Component> {children} </Component>;
};
```

Je sais que cela peut sembler beaucoup, mais regardez de plus près, et tout aura du sens. Ce n'est vraiment que l'assemblage de tout ce que vous avez appris jusqu'à présent. Rien ne devrait être particulièrement nouveau.

Tout est clair ? Maintenant, vous devenez quelque chose d'un pro !

Ayant fait cette refactorisation nécessaire, nous pouvons maintenant continuer avec notre solution. Ce que nous avons maintenant fonctionne réellement. Nous avons explicitement typé la prop color, et vous pouvez l'utiliser comme suit :

```jsx
<Text color="violet">Hello world</Text>
```

Il y a juste une chose avec laquelle je ne suis pas particulièrement à l'aise.

Il s'avère que `color` est également un attribut valide pour de nombreuses balises `HTML`. C'était le cas avant HTML5. Donc, si nous supprimions `color` de notre définition de type, il serait accepté comme n'importe quelle chaîne valide.

Voyez ci-dessous :

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  // supprimez color de la définition ici
};
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-142.png)
_Suppression de la définition de type color_

Maintenant, si vous utilisez `Text` comme avant, c'est également valide :

```jsx
<Text color="violet">Hello world</Text>
```

La seule différence ici est la manière dont il est typé. `color` est maintenant représenté par la définition suivante `color?: string | undefined` :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-143.png)
_Le type color par défaut_

Encore une fois, ce n'est PAS une définition que nous avons écrite dans nos types !

C'est une typographie HTML par défaut où color est un attribut valide pour la plupart des éléments HTML. Voir cette [question stackoverflow](https://stackoverflow.com/questions/67142430/why-color-appears-as-html-attribute-on-a-div) pour plus de contexte.

Maintenant, il y a deux façons de procéder.

Tout d'abord, vous pouvez garder notre solution initiale où nous avons explicitement déclaré la prop color :

```jsx
type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black"; // 👈 regardez ici
};
```

Deuxièmement, vous pouvez aller de l'avant et fournir arguer une sécurité supplémentaire. Pour y parvenir, vous devez réaliser d'où venait la définition de couleur par défaut précédente.

Elle venait de la définition `React.ComponentPropsWithoutRef<C>` — c'est ce qui ajoute d'autres props en fonction du type de `as`.

Alors, ce que nous pouvons faire ici, c'est de supprimer explicitement toute définition qui existe dans nos types de composants de `React.ComponentPropsWithoutRef<C>`.

Cela peut être difficile à comprendre avant de le voir en action, alors prenons-le étape par étape.

`React.ComponentPropsWithoutRef<C>`, comme indiqué précédemment, contient toutes les autres props valides en fonction du type de `as`, par exemple `href`, `color`, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-144.png)
_Le type ComponentPropsWithoutRef_

Où tous ces types ont leur définition, comme `color?: string | undefined` et ainsi de suite.

Il est possible que certaines valeurs qui existent dans `React.ComponentPropsWithoutRef<C>` existent également dans notre définition de type de props de composant.

Dans notre cas, `color` existe dans les deux !

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-145.png)
_ComponentPropsWithoutRef et TextProps_

Au lieu de nous fier à notre définition de couleur pour remplacer ce qui provient de `React.ComponentPropsWithoutRef<C>`, nous allons supprimer explicitement tout type qui existe également dans notre définition de types de composants.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-146.png)
_Suppression des props existantes de ComponentPropsWithoutRef_

Donc, si un type existe dans notre définition de types de composants, nous allons l'enlever explicitement de `React.ComponentPropsWithoutRef<C>`.

Comment faisons-nous cela ?

Eh bien, voici ce que nous avions avant :

```jsx
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> & 
React.ComponentPropsWithoutRef<C>
```

Au lieu d'avoir simplement un type d'intersection où nous ajoutons tout ce qui provient de React.ComponentPropsWithoutRef<C>, nous allons être plus sélectifs. Nous allons utiliser les types utilitaires Omit et keyof de TypeScript pour effectuer une magie TS.

Jetez un coup d'œil :

```jsx
// avant 
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> & 
React.ComponentPropsWithoutRef<C>

// après
type Props <C extends React.ElementType> = 
React.PropsWithChildren<TextProps<C>> &   
Omit<React.ComponentPropsWithoutRef<C>, keyof TextProps<C>>;
```

Le point important est celui-ci :

```jsx
Omit<React.ComponentPropsWithoutRef<C>, keyof TextProps<C>>;
```

Si vous ne savez pas comment fonctionnent `Omit` et `keyof`, voici un résumé rapide.

`Omit` prend deux génériques. Le premier est un type d'objet, et le second une union de types que vous souhaitez « omettre » du type d'objet.

Voici mon exemple préféré. Considérez un type d'objet Vowel comme suit :

```jsx
type Vowels = {
  a: 'a',
  e: 'e',
  i: 'i',
  o: 'o',
  u: 'u'
}
```

C'est un type d'objet de clé et de valeur.

Et si je voulais dériver un nouveau type de `Vowels` appelé `VowelsInOhans` ?

Eh bien, je sais que le nom Ohans contient deux voyelles `o` et `a`.

Au lieu de les déclarer manuellement :

```jsx
type VowelsInOhans = {
  a: 'a',
  o: 'o'
}
```

Je peux utiliser `Omit` comme suit :

```jsx
type VowelsInOhans = Omit<Vowels, 'e' | 'i' | 'u'>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-147.png)
_Le type VowelsInOhans utilisant Omit_

`Omit` « omettra » les clés e, i et u du type d'objet Vowels.

D'autre part, `keyof` fonctionne comme vous pourriez l'imaginer. Pensez à `Object.keys` en JavaScript.

Étant donné un type d'objet, `keyof` retournera un type d'union des clés de l'objet. Ouf ! C'est un peu compliqué.

Voici un exemple :

```jsx
type Vowels = {
  a: 'a',
  e: 'e',
  i: 'i',
  o: 'o',
  u: 'u'
}

type Vowel = keyof Vowels 
```

Maintenant, Vowel sera un type d'union des clés de Vowels, c'est-à-dire :

```jsx
type Vowel = 'a' | 'e' | 'i' | 'o' | 'u'

```

Si vous mettez tout cela ensemble et que vous jetez un second regard sur notre solution, tout s'assemblera bien :

```tsx
Omit<React.ComponentPropsWithoutRef<C>, keyof TextProps<C>>;
```

`keyof TextProps<C>` retourne un type d'union des clés de nos props de composant. Cela est à son tour passé à `Omit` pour les omettre de `React.ComponentPropsWithoutRef<C>`.

Super ! 🔮

Pour être complet, allons-y et passons effectivement la prop color à l'élément rendu :

```tsx
xport const Text = <C extends React.ElementType = "span">({
  as,
  color, // 👈 regardez ici
  children,
  ...restProps
}: Props<C>) => {
  const Component = as || "span";
	
  // 👋 composez un objet de style en ligne
  const style = color ? { style: { color } } : {};
	
  // 👋 passez le style en ligne à l'élément rendu
  return (
    <Component {...restProps} {...style}>
      {children}
    </Component>
  );
};
```

## Comment Créer un Utilitaire Réutilisable pour les Types Polymorphes

Vous devez être fier de la distance que vous avez parcourue si vous avez suivi jusqu'à présent.

Nous avons une solution qui fonctionne — bien.

Mais maintenant, allons un peu plus loin.

La solution que nous avons fonctionne très bien pour notre composant Text. Mais que se passerait-il si vous préfériez avoir une solution que vous pouvez réutiliser sur n'importe quel composant de votre choix ?

De cette façon, vous pouvez avoir une solution réutilisable pour chaque cas d'utilisation.

Comment cela vous semble-t-il ? Magnifique, je parie !

Commençons.

Tout d'abord, voici la solution complète actuelle sans annotations :

```tsx
type Rainbow =
  | "red"
  | "orange"
  | "yellow"
  | "green"
  | "blue"
  | "indigo"
  | "violet";

type TextProps<C extends React.ElementType> = {
  as?: C;
  color?: Rainbow | "black";
};

type Props<C extends React.ElementType> = React.PropsWithChildren<
  TextProps<C>
> &
  Omit<React.ComponentPropsWithoutRef<C>, keyof TextProps<C>>;

export const Text = <C extends React.ElementType = "span">({
  as,
  color,
  children,
  ...restProps
}: Props<C>) => {
  const Component = as || "span";

  const style = color ? { style: { color } } : {};

  return (
    <Component {...restProps} {...style}>
      {children}
    </Component>
  );
};
```

Concis et pratique.

Si nous rendions cela réutilisable, alors cela doit fonctionner pour n'importe quel composant. Cela signifie supprimer les TextProps codés en dur et les représenter avec un générique — afin que quiconque puisse passer les props de composant dont il a besoin.

Actuellement, nous représentons nos props de composant avec la définition Props<C>. Où C représente le type d'élément passé pour la prop as.

Nous allons maintenant changer cela en :

```tsx
// avant
Props<C>

// après 
PolymorphicProps<C, TextProps>
```

`PolymorphicProps` représente le type utilitaire que nous allons écrire sous peu. Mais notez que cela accepte deux types génériques. Le second étant les props du composant en question, c'est-à-dire `TextProps`.

Allons-y et définissons le type `PolymorphicProps` :

```tsx
type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = {} // 👈 objet vide pour l'instant 
```

La définition ci-dessus devrait être compréhensible. `C` représente le type d'élément passé dans `as` et `Props` les props réelles du composant, par exemple `TextProps`.

Avant de continuer, divisons les `TextProps` que nous avions auparavant en ce qui suit :

```tsx
type AsProp<C extends React.ElementType> = {
  as?: C;
};

type TextProps = { color?: Rainbow | "black" };
```

Ainsi, nous avons séparé la `AsProp` de la `TextProps`. Pour être honnête, elles représentent deux choses différentes. C'est une représentation plus agréable.

Maintenant, changeons la définition de l'utilitaire PolymorphicComponentProp pour inclure la prop `as`, les props du composant, et la prop children comme nous l'avons fait par le passé :

```tsx
type AsProp<C extends React.ElementType> = {
  as?: C;
};

type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>>
```

Je suis sûr que vous comprenez ce qui se passe ici.

Nous avons maintenant un type d'intersection de `Props` (représentant les props du composant) et AsProp représentant la prop `as`, et tout cela est passé dans `PropsWithChildren` pour ajouter la définition de la prop children.

Excellent !

Maintenant, nous devons inclure la partie où nous ajoutons la définition `React.ComponentPropsWithoutRef<C>`. Cependant, nous devons nous souvenir d'omettre les props qui existent dans notre définition de composant.

Trouvons une solution robuste.

Écrivez un nouveau type qui ne comprend que les props que nous aimerions omettre. À savoir, les clés de `AsProp` et les props du composant également.

```tsx
type PropsToOmit<C extends React.ElementType, P> = keyof (AsProp<C> & P);
```

Vous vous souvenez du type utilitaire `keyof` ?

PropsToOmit comprendra maintenant un type d'union des props que nous voulons omettre, qui est, chaque prop de notre composant représentée par `P` et la prop polymorphe réelle telle que représentée par `AsProps`.

Je suis heureux que vous suiviez toujours.

Maintenant, mettons tout cela ensemble dans la définition `PolymorphicComponentProp` :

```tsx
type AsProp<C extends React.ElementType> = {
  as?: C;
};

// avant 
type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>>

// après
type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>> &
  Omit<React.ComponentPropsWithoutRef<C>, 
   PropsToOmit<C, Props>>;
```

Cela omettra essentiellement les bons types de `React.componentPropsWithoutRef`. Vous vous souvenez encore comment [Omit](https://www.typescriptlang.org/docs/handbook/utility-types.html#omittype-keys) fonctionne ?

Simple comme cela puisse paraître, vous avez maintenant une solution que vous pouvez réutiliser sur plusieurs composants à travers différents projets !

Voici l'implémentation complète :

```tsx
type PropsToOmit<C extends React.ElementType, P> = keyof (AsProp<C> & P);

type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>> &
  Omit<React.ComponentPropsWithoutRef<C>, PropsToOmit<C, Props>>;
```

Maintenant, nous pouvons utiliser `PolymorphicComponentProp` sur notre composant `Text` comme suit :

```tsx
export const Text = <C extends React.ElementType = "span">({
  as,
  color,
  children,
  // regardez ici 👋
}: PolymorphicComponentProp<C, TextProps>) => {
  const Component = as || "span";
  const style = color ? { style: { color } } : {};
  return <Component {...style}>{children}</Component>;
};
```

C'est bien !

Maintenant, si vous construisez un autre composant, vous pouvez le typer comme ceci :

```tsx
PolymorphicComponentProp<C, MyNewComponentProps>
```

Entendez-vous ce son ? C'est le son de la victoire — vous êtes arrivé si loin !

## Le Composant Doit Supporter les Refs

Vous vous souvenez de chaque référence à `React.ComponentPropsWithoutRef` jusqu'à présent ? 😅

Props de composant... _sans_ ref. Eh bien, maintenant c'est le moment de mettre la ref dedans !

C'est la partie finale et la plus complexe de notre solution. J'aurai besoin que vous soyez patient ici, mais je ferai également de mon mieux pour expliquer chaque étape en détail.

Plongeons-nous.

Tout d'abord, vous souvenez-vous comment fonctionnent les refs dans React ?

Le concept le plus important ici est le fait que vous ne passez pas simplement `ref` comme une prop et vous attendez à ce qu'elle soit passée dans votre composant comme toutes les autres props.

La manière recommandée de gérer les refs dans vos composants fonctionnels est d'utiliser la fonction `forwardRef`.

Commençons sur une note pratique.

Si vous passez une `ref` à notre composant `Text` maintenant, vous obtiendrez une erreur qui dit La propriété `'ref'` n'existe pas sur le type ...

```tsx
// Créez l'objet ref 
const divRef = useRef<HTMLDivElement | null>(null);
... 
// Passez la ref au composant Text rendu
<Text as="div" ref={divRef}>
  Hello Text world
</Text>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-148.png)
_Erreur : La propriété ref n'existe pas_

Cela est attendu.

Notre première tentative pour supporter les refs sera d'utiliser `forwardRef` dans le composant `Text` comme montré ci-dessous :

```tsx
// avant 
export const Text = <C extends React.ElementType = "span">({
  as,
  color,
  children,
}: PolymorphicComponentProp<C, TextProps>) => {
  ...
};


// après
import React from "react";

export const Text = React.forwardRef(
  <C extends React.ElementType = "span">({
    as,
    color,
    children,
  }: PolymorphicComponentProp<C, TextProps>) => {
    ...
  }
);
```

Cela consiste essentiellement à envelopper le code précédent dans `React.forwardRef`, c'est tout.

Maintenant, `React.forwardRef` a la signature suivante :

```jsx
React.forwardRef((props, ref) ... )
```

Essentiellement, le deuxième argument reçu est l'objet `ref`.

Allons-y et gérons cela :

```tsx
type PolymorphicRef<C extends React.ElementType> = unknown;

export const Text = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: PolymorphicComponentProp<C, TextProps>,
    // 👋 regardez ici
    ref?: PolymorphicRef<C>
  ) => {
    ...
  }
);
```

Ce que nous avons fait ici, c'est ajouter le deuxième argument ref et déclarer son type comme PolymorphicRef.

Un type qui pointe simplement vers `unknown` pour l'instant.

Notez également que PolymorphicRef prend le générique `C`. Cela est similaire aux solutions précédentes. L'objet ref pour un div diffère de celui d'un `span`. Donc, nous devons prendre en considération le type d'élément passé dans la prop as.

Attirons maintenant l'attention sur le type `PolymorphicRef`.

J'ai besoin que vous réfléchissiez avec moi.

Comment pouvons-nous obtenir le type d'objet `ref` en fonction de la prop as ?

Je vais vous donner un indice : `React.ComponentPropsWithRef` !

Notez que cela dit _avec_ ref. Pas _sans_ ref.

Essentiellement, si cela était un ensemble de clés (ce qui est en fait le cas), il inclurait toutes les props de composant pertinentes en fonction du type d'élément, _plus_ l'objet ref.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-149.png)
_Le type ComponentPropsWithRef_

Donc maintenant, si nous savons que ce type d'objet contient la clé `ref`, nous pouvons tout aussi bien obtenir ce type de ref en faisant ce qui suit :

```tsx
// avant 
type PolymorphicRef<C extends React.ElementType> = unknown;

// après 
type PolymorphicRef<C extends React.ElementType> =
  React.ComponentPropsWithRef<C>["ref"];
```

Essentiellement, `React.ComponentPropsWithRef<C>` retourne un type d'objet, par exemple :

```js
{
  ref: SomeRefDefinition, 
  // ... autres clés, 
  color: string 
  href: string 
  // ... etc
}
```

Pour ne sélectionner que le type ref, nous faisons ensuite ceci :

```jsx
React.ComponentPropsWithRef<C>["ref"];
```

Notez que la syntaxe est similaire à celle de l'accesseur de propriété en JavaScript, c'est-à-dire ["ref"]. En TypeScript, nous appelons cela **l'indexation de type**.

**_Quiz rapide_**_: Savez-vous pourquoi utiliser « Pick » ne fonctionnerait peut-être pas bien ici, par exemple_ Pick<React.ComponentPropsWithRef<C>, "ref">_?_

Vous pouvez [me tweeter](https://twitter.com/ohansemmanuel) vos réponses.

Maintenant que nous avons typé la prop `ref`, nous pouvons passer celle-ci à l'élément rendu :

```tsx
export const Text = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: PolymorphicComponentProp<C, TextProps>,
    ref?: PolymorphicRef<C>
  ) => {
    //...
    
    return (
      <Component {...style} ref={ref}> // 👈 regardez ici
        {children}
      </Component>
    );
  }
);
```

Nous avons fait des progrès décents ! En fait, si vous vérifiez l'utilisation de Text comme nous l'avons fait auparavant, il n'y aura plus d'erreurs :

```tsx
// créez l'objet ref 
const divRef = useRef<HTMLDivElement | null>(null);
... 
// passez la ref au composant Text rendu
<Text as="div" ref={divRef}>
  Hello Text world
</Text>
```

Mais notre solution n'est toujours pas aussi fortement typée que je le souhaiterais.

Allons-y et changeons la ref passée à Text comme montré ci-dessous :

```tsx
// créez un objet ref "button" 
const buttonRef = useRef<HTMLButtonElement | null>(null);
... 
// passez une ref de button à un "div". NB : as = "div"
<Text as="div" ref={buttonRef}>
  Hello Text world
</Text>
```

Typescript devrait lancer une erreur ici, mais ce n'est pas le cas. Nous créons une ref de "button", mais nous la passons à un élément `div`.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-150.png)
_Aucune erreur n'est lancée lorsqu'une ref d'élément incorrecte est passée_

Si vous regardez le type exact, `ref` ressemble à ceci :

```tsx
React.RefAttributes<unknown>.ref?: React.Ref<unknown>
```

Voyez-vous le `unknown` là-dedans ? C'est le signe d'un typage faible. Nous devrions idéalement avoir `HTMLDivElement` là, définissant explicitement l'objet ref comme une ref d'élément `div`.

Nous avons du travail à faire.

Tout d'abord, les types des autres props du composant `Text` font toujours référence au type `PolymorphicComponentProp`.

Changeons cela en un nouveau type appelé `PolymorphicComponentPropWithRef`. Vous avez deviné juste. Cela sera simplement une union de `PolymorphicComponentProp` et de la prop ref.

Le voici :

```tsx
type PolymorphicComponentPropWithRef<
  C extends React.ElementType,
  Props = {}
> = PolymorphicComponentProp<C, Props> & 
{ ref?: PolymorphicRef<C> };
```

Notez que cela est simplement une union du précédent `PolymorphicComponentProp` et `{ ref?: PolymorphicRef<C> }`.

Maintenant, nous devons changer les props du composant pour qu'elles fassent référence au nouveau type `PolymorphicComponentPropWithRef` :

```tsx
// avant
type TextProps = { color?: Rainbow | "black" };

export const Text = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: PolymorphicComponentProp<C, TextProps>,
    ref?: PolymorphicRef<C>
  ) => {
    ...
  }
);


// maintenant 
type TextProps<C extends React.ElementType> = 
PolymorphicComponentPropWithRef<
  C,
  { color?: Rainbow | "black" }
>;

export const Text = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: TextProps<C>, // 👈 regardez ici
    ref?: PolymorphicRef<C>
  ) => {
    ...
  }
);
```

Maintenant, nous avons mis à jour `TextProps` pour qu'il fasse référence à `PolymorphicComponentPropWithRef` et cela est maintenant passé en tant que props pour le composant Text.

Magnifique !

Il ne reste plus qu'une dernière chose à faire maintenant. Nous allons fournir une annotation de type pour le composant `Text`. Cela ressemble à :

```tsx
export const Text : TextComponent = ...
```

Où `TextComponent` est l'annotation de type que nous allons écrire. La voici :

```tsx
type TextProps<C extends React.ElementType> = 
PolymorphicComponentPropWithRef<
  C,
  { color?: Rainbow | "black" }
>;
```

Cela est essentiellement un composant fonctionnel qui prend `TextProps` et retourne `React.ReactElement | null`.

Où `TextProps` est défini comme suit :

```tsx
type TextProps<C extends React.ElementType> = 
PolymorphicComponentPropWithRef<
  C,
  { color?: Rainbow | "black" }
>;
```

Avec cela, nous avons maintenant une solution complète.

Je vais partager la solution complète maintenant. Cela peut sembler intimidant au premier abord, mais rappelez-vous que nous avons travaillé ligne par ligne sur tout ce que vous voyez ici. Lisez-le avec cette confiance.

```tsx
import React from "react";

type Rainbow =
  | "red"
  | "orange"
  | "yellow"
  | "green"
  | "blue"
  | "indigo"
  | "violet";

type AsProp<C extends React.ElementType> = {
  as?: C;
};

type PropsToOmit<C extends React.ElementType, P> = keyof (AsProp<C> & P);

// C'est le premier utilitaire de type réutilisable que nous avons construit
type PolymorphicComponentProp<
  C extends React.ElementType,
  Props = {}
> = React.PropsWithChildren<Props & AsProp<C>> &
  Omit<React.ComponentPropsWithoutRef<C>, PropsToOmit<C, Props>>;

// C'est un nouvel utilitaire de type avec ref !
type PolymorphicComponentPropWithRef<
  C extends React.ElementType,
  Props = {}
> = PolymorphicComponentProp<C, Props> & { ref?: PolymorphicRef<C> };

// C'est le type pour le "ref" uniquement
type PolymorphicRef<C extends React.ElementType> =
  React.ComponentPropsWithRef<C>["ref"];

/**
* Ce sont les props du composant mises à jour utilisant PolymorphicComponentPropWithRef
*/
type TextProps<C extends React.ElementType> = 
PolymorphicComponentPropWithRef<
  C,
  { color?: Rainbow | "black" }
>;

/**
* C'est le type utilisé dans l'annotation de type pour le composant
*/
type TextComponent = <C extends React.ElementType = "span">(
  props: TextProps<C>
) => React.ReactElement | null;

export const Text: TextComponent = React.forwardRef(
  <C extends React.ElementType = "span">(
    { as, color, children }: TextProps<C>,
    ref?: PolymorphicRef<C>
  ) => {
    const Component = as || "span";

    const style = color ? { style: { color } } : {};

    return (
      <Component {...style} ref={ref}>
        {children}
      </Component>
    );
  }
);
```

Et voilà !

Vous avez réussi à construire une solution robuste pour gérer les composants polymorphes dans React.

Je sais que ce n'était pas une promenade de santé, mais vous l'avez fait.

## Conclusion et Prochaines Étapes

Merci d'avoir suivi. Si vous êtes déterminé à continuer à améliorer votre TypeScript, vous pouvez [télécharger le PDF gratuit accompagnant](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/stprc-meta-3.png)
_[Téléchargez le PDF gratuit](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components)_

Je vous enverrai également une série d'e-mails sur 5 secrets TypeScript qui vous feront réfléchir (et écrire) comme un pro.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/5-TS-secrets@3x.png)
_[Téléchargez le livre électronique gratuit](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components) pour obtenir automatiquement ma newsletter de 5 jours sur les secrets de Typescript_

Vous pouvez [l'obtenir ici](https://www.ohansemmanuel.com/books/how-to-build-strongly-typed-polymorphic-react-components).

Merci d'avoir lu !