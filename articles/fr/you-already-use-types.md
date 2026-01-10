---
title: Vous Utilisez Déjà des Types - Voici Pourquoi Vous Devriez Utiliser un Système
  de Types
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-29T15:41:00.000Z'
originalURL: https://freecodecamp.org/news/you-already-use-types
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca094740569d1a4ca4989.jpg
tags:
- name: flowtype
  slug: flowtype
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Vous Utilisez Déjà des Types - Voici Pourquoi Vous Devriez Utiliser un
  Système de Types
seo_desc: 'By swyx

  This post is for skeptics and newcomers to type systems, and aims to articulate
  rather than hard sell.


  First we''ll look at how static type conventions appear in your dynamically typed
  coding.

  Then we''ll step back and try to think about what ...'
---

Par swyx

Cet article s'adresse aux sceptiques et aux nouveaux venus dans les systèmes de types, et vise à articuler plutôt qu'à vendre à tout prix.

1. Nous allons d'abord examiner comment les conventions de types statiques apparaissent dans votre codage dynamiquement typé.
2. Ensuite, nous allons prendre du recul et essayer de réfléchir à ce que ce phénomène nous dit sur la façon dont nous voulons coder.
3. Enfin, nous poserons quelques questions (orientées!) qui devraient découler de ces réflexions.

## 1A: Types dans les Noms

Indépendamment du langage, votre parcours avec les types commence presque dès que vous apprenez à coder. La structure de données de liste de base invite à un pluriel correspondant:

```js
var dog = 'Fido'
var dogs = ['Fido', 'Sudo', 'Woof']
```

Au fur et à mesure que vous travaillez avec de plus en plus de code, vous commencez à former des opinions que vous pouvez imposer à votre équipe ou à votre guide de style:

- utilisez toujours des noms spécifiques comme `dogID` vs `dogName` vs `dogBreed` ou un espace de noms/classe/objet comme `dog.name` ou `dog.id` ou `dog.breed`
- les singuliers ne doivent pas être des sous-chaînes de pluriels, par exemple MAUVAIS: `blog` et `blogs`, BON: `blogPost` vs `blogList`
- les booléens [devraient avoir un préfixe booléen](https://github.com/typescript-eslint/typescript-eslint/issues/515), comme `isLoading`, `hasProperty`, `didChange`
- les fonctions avec effets de bord doivent avoir des verbes
- les variables internes doivent avoir un `_prefix`

Cela peut sembler trivial puisque nous parlons de noms de variables, mais cette veine est en fait _extrêmement_ profonde. Les noms dans notre codage reflètent les concepts et les contraintes que nous plaçons sur notre code pour le rendre plus maintenable à grande échelle:

- [Composants de Présentation vs Conteneurs avec État/Connectés](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0)
- [Atomes, Molécules, Organismes, Modèles, Pages](http://bradfrost.com/blog/post/atomic-web-design/)
- [Concepts, Actions, Opérandes](https://reactjs.org/blog/2016/09/28/our-first-50000-stars.html#api-churn) (l'une des grammaires de noms les plus réussies jamais)
- [Block\_\_Element--Modifier](http://getbem.com/naming/)
- [Composants d'Ordre Supérieur](https://reactjs.org/docs/higher-order-components.html)

Tous ces éléments s'infiltrent dans votre code en conséquence: `*Container`, `*Component`, `*Reducer`, `*Template`, `*Page`, `with*`.

Une fois que vous commencez à traverser les paradigmes d'exécution, vous commencez à sentir votre chemin vers des indices de types monadiques.

Node.js a ressenti cela très tôt:

```js
fs.readFile(myfile, callback)
fs.readFileSync(myfile) // introduit lorsque les gens ont réalisé que l'enfer des callbacks ne valait peut-être pas le non-blocage
```

React a introduit le préfixe `use` pour indiquer l'accrochage au runtime qui doit respecter [certaines règles](https://reactjs.org/docs/hooks-rules.html):

```js
function Component() {
  const [bool, setBool] = React.useState(true)
  React.useEffect(callback)
  const foo = useCustomHook()
  // ...
}
```

Je suis personnellement amateur de rappels de nullabilité:

```js
const maybeResult = await fetchAPI()
if (maybeResult) {
  const result = maybeResult
  // faire des choses avec result
} else {
  // maybeResult est falsy, ne supposez pas qu'il est là
}
```

**Dans presque tout ce que vous nommez, vous utilisez déjà des types.**

Alors quoi, demandez-vous?

Continuez à lire, je construis vers cela.

## 1B: Types dans les Structures de Données

Le problème avec l'encodage des types dans les noms est que le langage ne se soucie probablement pas de vos variables soigneusement nommées (en effet, en JavaScript, il est probablement minifié sans pitié au-delà de toute reconnaissance). Il exécutera volontiers votre code et lancera une erreur d'exécution si vous oubliez de respecter vos propres indices de type de nom. Et si nous rendions les types formellement vérifiables à travers des structures de données?

Les plus basiques sont les constantes. Dans Redux, il est [courant de définir explicitement (et de manière redondante) des SCREAMING_CASE_CONSTANTS](https://decembersoft.com/posts/a-simple-naming-convention-for-action-creators-in-redux-js/):

```js
const ADD_TODO = 'slice/ADD_TODO'

// plus tard dans le code redux:
import { ADD_TODO } from './redux/types'
switch (action.type) {
  case ADD_TODO:
  // faire des choses en fonction de l'action
  // ...
}
```

Cela est principalement fait parce que vous ne pouvez pas faire confiance à votre collègue développeur pour ne pas faire de faute de frappe dans ses chaînes de caractères.

Cependant, même ces chaînes de caractères offrent trop de confiance, et nous avons trouvé important d'ajouter une nouvelle fonctionnalité de langage pour garantir l'unicité:

```js
const ADD_TODO = Symbol('slice/ADD_TODO')
```

Nous faisons également semblant de nous diriger vers des énumérations de cette manière:

```js
const colors = {
  BLUE: Symbol(1),
  GREEN: Symbol(2),
  RED: Symbol(3),
}
```

Mais les valeurs simples (chaînes de caractères, nombres, booléens) sont en fait faciles à comparer et à traiter en conséquence.

Plus pressant est l'encodage des types dans les valeurs complexes.

Cela se produit généralement lorsque vous avez des tableaux d'objets et que les objets sont différents à certains égards et similaires à d'autres:

```js
const animals = [{ name: 'Fido', legs: 4, says: 'woof' }, { name: 'Kermit', legs: 2, marriedTo: 'Piggy' }]
// aura des bugs si un animal avec à la fois `says` et `marriedTo` existe
animals.forEach((animal) => {
  if (animal.says) {
    // je suppose que c'est un chien?
  }
  if (animal.marriedTo) {
    // je suppose que c'est une grenouille?
  }
})
```

La vérification boguée et les types implicitement supposés sont souvent une cause de beaucoup de douleur. Mieux vaut typer explicitement:

```js
const animals = [
  {
    type: 'dog', // nouveau!
    name: 'Fido',
    legs: 4,
    says: 'woof',
  },
  {
    type: 'frog', // nouveau!
    name: 'Kermit',
    legs: 2,
    marriedTo: 'Piggy',
  },
]
animals.forEach((animal) => {
  if (animal.type === 'dog') {
    // doit être un chien!
  }
  if (animal.type === 'frog') {
    // doit être une grenouille!
  }
})
```

C'est en fait ce qui se passe pour Redux (et, assez intéressamment, pratique pour d'autres choses comme [Discriminated Unions](https://basarat.gitbooks.io/typescript/docs/types/discriminated-unions.html)), mais vous verrez cela **partout** dans [Gatsby](https://github.com/sw-yx/overreacted.io/blob/master/gatsby-config.js#L25-L50) et [Babel](https://babeljs.io/docs/en/plugins/#plugin-options) et [React](https://reactjs.org/docs/react-without-jsx.html) et je suis sûr que vous connaissez des cas que je ne connais pas.

Les types existent même en HTML: `<input type="file">` et `<input type="checkbox">` se comportent si différemment! (et j'ai déjà mentionné les Types en CSS avec [Block\_\_Element--Modifier](http://getbem.com/naming/))

**Même en HTML/CSS, vous utilisez déjà des types.**

## 1C: Types dans les APIs

J'ai presque terminé. Même en dehors de votre langage de programmation, les interfaces entre machines impliquent des types.

La grande innovation de REST était essentiellement une forme primitive de typage des requêtes client-serveur: `GET`, `PUT`, `POST`, `DELETE`. Les conventions Web ont introduit d'autres champs de type dans les requêtes, comme l'en-tête `accept-encoding`, que vous devez respecter pour obtenir ce que vous voulez. Cependant, la RESTfulness n'est essentiellement pas appliquée, et parce qu'elle n'offre pas de garanties, les outils en aval ne peuvent pas supposer des endpoints bien comportés.

GraphQL prend cette idée et la pousse à 11: Les types sont clés pour les requêtes et les mutations et les fragments, mais aussi sur chaque champ et chaque variable d'entrée, validés à la fois côté client et côté serveur par spécification. Avec des garanties beaucoup plus fortes, il est capable de fournir [de bien meilleurs outils](https://github.com/graphql/graphiql) comme norme communautaire.

Je ne connais pas l'histoire de SOAP et XML et gRPC et d'autres protocoles de communication machine-machine, mais je suis prêt à parier qu'il y a de fortes similitudes.

## Partie 2: Que Nous Dit Cela?

Cela a été un examen très long, et pourtant non exhaustif, des types qui imprègnent tout ce que vous faites. Maintenant que vous avez vu ces modèles, vous pouvez probablement penser à plus d'exemples que j'oublie en ce moment. Mais à chaque tournant, il semble que la voie vers un code plus maintenable, et de meilleurs outils, est d'ajouter des types d'une manière ou d'une autre.

J'ai mentionné des parties de cette thèse dans [Comment Nommer les Choses](https://www.swyx.io/writing/how-to-name-things), mais en fait, tous les schémas de nommage relèvent d'une forme éclairée de la notation hongroise, comme décrit dans l'article de Joel Spolsky [Making Wrong Code Look Wrong](https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/).

Si rien de ce que j'ai décrit ne résonne avec vous, et n'est pas quelque chose que vous avez déjà fait, alors les types ne sont peut-être pas pour vous.

Mais si c'est le cas, et que vous l'avez fait de manière négligée, vous pourriez être intéressé par plus de structure autour de la façon dont vous utilisez les types dans votre code, et par l'utilisation de meilleurs outils qui tirent parti de tout le travail acharné que vous avez déjà mis dans les types.

Vous pourriez être en train de travailler vers un système de types, sans même le savoir.

## Partie 3: Questions Orientées

Alors, sachant ce que nous savons maintenant sur l'utilisation des types dans notre code sans un système de types. Je vais poser quelques questions difficiles.

**Question 1: Que faites-vous actuellement pour appliquer les types sans un système de types?**

Au niveau individuel, vous vous engagez dans le codage défensif et la vérification manuelle. En gros, vous examinez manuellement votre propre code et ajoutez des vérifications et des gardes de manière réflexe sans savoir s'ils sont vraiment nécessaires (ou, pire, vous ne le faites PAS et vous le découvrez après avoir vu des exceptions d'exécution).

Au niveau de l'équipe, vous passez des multiples d'heures de développement en revue de code, invitant à des discussions interminables sur les noms, ce que nous savons tous être très amusant.

Ces deux processus sont des méthodes manuelles, et une très mauvaise utilisation du temps des développeurs. [Ne soyez pas le mauvais flic](https://hackernoon.com/dont-be-the-bad-cop-in-pull-request-reviews-let-software-do-that-job-1eb9e574c2d1) - cela détruit la dynamique de l'équipe. À grande échelle, vous êtes mathématiquement assuré d'avoir des lacunes dans la qualité du code (causant ainsi des bugs de production), soit parce que tout le monde a manqué quelque chose, soit parce qu'il n'y avait tout simplement pas assez de temps et que vous deviez livrer quelque chose, soit parce qu'il n'y avait pas encore de politique suffisamment bonne en place.

La solution, bien sûr, est de l'automatiser. Comme le dit Nick Schrock, [Déléguer à l'Outiling Chaque Fois que Possible](https://medium.com/@schrockn/on-code-reviews-b1c7c94d868c). Prettier et ESLint aident à maintenir votre qualité de code - seulement dans la mesure où le programme peut vous comprendre en fonction d'un AST. Il n'offre aucune aide pour traverser les frontières de fonctions et de fichiers - si la fonction `Foo` attend 4 arguments et que vous ne lui passez que 3, aucun linter ne vous criera dessus et vous devrez coder de manière défensive à l'intérieur de `Foo`.

Il n'y a donc que tant de choses que vous pouvez automatiser avec un linter. Qu'en est-il du reste que vous ne pouvez pas automatiser?

Là réside la dernière option: Ne Rien Faire.

La plupart des gens ne font rien pour appliquer leurs systèmes de types conçus de manière informelle.

**Question 2: Combien de ces types écrivez-vous vous-même?**

Il va sans dire que si toutes vos politiques de types sont créées par vous, alors elles doivent être écrites par vous et appliquées par vous.

Cela est totalement différent de la façon dont nous écrivons du code aujourd'hui. Nous nous appuyons fortement sur l'open source - [97% du code des applications web modernes provient de npm](https://mobile.twitter.com/housecor/status/1078634947831914496). Nous importons du code partagé, puis écrivons les dernières parties qui rendent notre application spéciale (aka logique métier).

Y a-t-il un moyen de partager des types?

([oui](https://github.com/DefinitelyTyped/DefinitelyTyped/))

**Question 3: Et si vos types étaient standardisés?**

Les recherches ont montré que la raison n°1 pour laquelle les programmeurs adoptent un langage est les capacités et fonctionnalités existantes disponibles pour eux à utiliser. J'apprendrai Python pour utiliser TensorFlow. J'apprendrai Objective C pour créer des expériences natives iOS. Correspondamment, JS a été si réussi parce qu'il fonctionne partout, amplifié par la large disponibilité de logiciels open source gratuits écrits _par d'autres personnes_. Avec un système de types standardisé, nous pouvons [importer des types aussi facilement que nous importons des logiciels open source](https://github.com/DefinitelyTyped/DefinitelyTyped/) écrits par d'autres personnes.

Tout comme GraphQL vs REST, les types standardisés dans un langage débloquent de bien meilleurs outils. Je vais offrir 4 exemples:

**Exemple 1: Retour d'Information Plus Rapide**

Nous pouvons mettre des mois et des jours à apprendre des **erreurs d'exécution**, et celles-ci sont exposées aux utilisateurs, donc ce sont les pires résultats possibles.

Nous écrivons des tests et appliquons des règles de lint et d'autres vérifications pour déplacer ces erreurs vers des **erreurs de build**, ce qui raccourcit les cycles de retour d'information à des minutes et des heures. (Comme je l'ai écrit récemment: [Les Types ne Remplacent Pas les Tests!](https://css-tricks.com/types-or-tests-why-not-both/))

Les Systèmes de Types peuvent raccourcir ce retour d'information d'un autre ordre de grandeur, à des secondes, en vérifiant pendant le **temps d'écriture**. (Les linters peuvent aussi faire cela. Les deux sont conditionnés par un IDE supportif comme VS Code) En effet secondaire, vous obtenez l'autocomplétion gratuitement, car l'autocomplétion et la validation au moment de l'écriture sont deux côtés de la même pièce.

**Exemple 2: Meilleurs Messages d'Erreur**

```js
const Foo = {
  getData() {
    return 'data'
  },
}
Foo['getdata']() // Erreur: undefined is not a function
```

JavaScript est intentionnellement évalué de manière paresseuse par conception. Au lieu de l'erreur redoutée et non descriptive `undefined is not a function` pendant l'exécution, nous pouvons déplacer cela au moment de l'écriture. Voici le message d'erreur au moment de l'écriture pour le même code exact:

```ts
const Foo = {
  getData() {
    return 'data'
  },
}
Foo['getdata']() // La propriété 'getdata' n'existe pas sur le type '{ getData(): string; }'. Vouliez-vous dire 'getData'?
```

Oui, TypeScript, c'est ce que je voulais dire.

**Exemple 3: Épuisement des Cas Limites**

```ts
let fruit: string | undefined
fruit.toLowerCase() // Erreur: L'objet est peut-être 'undefined'.
```

En plus de la vérification intégrée de nullabilité (qui prend en charge les problèmes comme passer 3 arguments lorsqu'une fonction en attend 4), un système de types peut tirer le meilleur parti de vos énumérations (aka types d'union). J'ai eu du mal à trouver un bon exemple, mais en voici un:

```ts
type Fruit = 'banana' | 'orange' | 'apple'
function makeDessert(fruit: Fruit) {
  // Erreur: Tous les chemins de code ne retournent pas une valeur.
  switch (fruit) {
    case 'banana':
      return 'Banana Shake'
    case 'orange':
      return 'Orange Juice'
  }
}
```

**Exemple 4: Refactorisation Sans Crainte**

Beaucoup de gens ont mentionné cela et je dois avouer que cela m'a pris un certain temps pour m'y faire. La réflexion est: "et alors? Je ne refactorise pas tant que ça. donc cela signifie que le bénéfice de TypeScript est plus petit pour moi que pour vous parce que je suis meilleur que vous."

C'est la mauvaise approche.

Lorsque nous commençons à explorer un problème, nous commençons avec une idée vague de la solution. Au fur et à mesure que nous progressons, nous en apprenons davantage sur le problème, ou les priorités changent, et à moins de l'avoir fait un million de fois, nous avons probablement choisi quelque chose de faux en cours de route, qu'il s'agisse de l'API de la fonction, de la structure de données, ou de quelque chose de plus grande échelle.

![](http://www.methodsandtools.com/archive/refact8.png)

La question est alors de soit s'en tenir jusqu'à ce que cela casse, soit de refactoriser dès que vous pouvez sentir que vous allez dépasser ce que vous aviez l'habitude d'utiliser. Je vais supposer que vous acceptez qu'il y a souvent des avantages à refactoriser. Alors pourquoi évitons-nous la refactorisation?

**La raison pour laquelle vous reportez cette refactorisation est qu'elle est coûteuse, pas parce qu'elle n'est pas bénéfique pour vous. Pourtant, la reporter ne fait qu'augmenter le coût futur.**

L'outil de Système de Types aide à réduire considérablement le coût de cette refactorisation, afin que vous puissiez en tirer les avantages plus tôt. Il réduit ce coût via un retour d'information plus rapide, une vérification d'exhaustivité et de meilleurs messages d'erreur.

## Vérité en Publicité

Il y a un coût à apprendre les Systèmes de Types que vous n'avez pas écrits. Ce coût peut compenser tout bénéfice imaginé de la vérification automatique des types. C'est pourquoi je mets beaucoup d'efforts pour aider à réduire cette courbe d'apprentissage. Cependant, soyez conscient que c'est un nouveau langage et qu'il impliquera des concepts peu familiers, et aussi que même l'outil est un travail en progrès imparfait.

Mais c'est assez bon pour [AirBnb](https://www.reddit.com/r/typescript/comments/aofcik/38_of_bugs_at_airbnb_could_have_been_prevented_by/) et [Google](http://neugierig.org/software/blog/2018/09/typescript-at-google.html) et [Atlassian](https://github.com/atlassian/react-beautiful-dnd/issues/982) et [Lyft](https://eng.lyft.com/typescript-at-lyft-64f0702346ea) et [Priceline](https://medium.com/priceline-labs/trying-out-typescript-part-1-15a5267215b9) et [Slack](https://slack.engineering/typescript-at-slack-a81307fa288d) et cela pourrait être pour vous.