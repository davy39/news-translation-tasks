---
title: Un guide pratique de TypeScript - Comment construire une application Pokedex
  en utilisant HTML, CSS et TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-21T15:16:13.000Z'
originalURL: https://freecodecamp.org/news/a-practical-guide-to-typescript-how-to-build-a-pokedex-app-using-html-css-and-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/cover-1.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Un guide pratique de TypeScript - Comment construire une application Pokedex
  en utilisant HTML, CSS et TypeScript
seo_desc: "By Ibrahima Ndaw\nTypeScript is a superset that needs to compile to plain\
  \ JavaScript. It offers more control over your code since it uses type annotations,\
  \ interfaces, classes, and static type checking to throw errors at compile-time.\
  \ \nTypeScript help..."
---

Par Ibrahima Ndaw

TypeScript est un sur-ensemble qui doit être compilé en JavaScript simple. Il offre plus de contrôle sur votre code puisqu'il utilise des annotations de type, des interfaces, des classes et une vérification de type statique pour lancer des erreurs au moment de la compilation. 

TypeScript aide à améliorer la qualité du code et sa compréhensibilité, surtout avec une base de code volumineuse.

Dans ce guide, je vais vous guider à travers TypeScript en apprenant d'abord toutes les bases nécessaires pour commencer avec ce langage formidable. Ensuite, nous terminerons en construisant une application à partir de zéro en utilisant HTML, CSS et TypeScript.

_Plongeons-nous_

* [Qu'est-ce que TypeScript ?](#heading-qu-est-ce-que-typescript)
* [Installation de TypeScript](#heading-installation-de-typescript)
* [Configuration de TypeScript avec tsconfig](#heading-configuration-de-typescript-avec-tsconfig)
* [Types TypeScript](#heading-types-typescript)
* [Types de base de TypeScript](#heading-types-de-base-de-typescript)
* [Interfaces et alias de type](#heading-interfaces-et-alias-de-type)
* [Construire une application Pokedex en utilisant TypeScript](#heading-construire-une-application-pokedex-en-utilisant-typescript)
* [Balises](#heading-balises)
* [Récupérer et afficher des données en utilisant TypeScript](#heading-recuperer-et-afficher-des-donnees-en-utilisant-typescript)
* [Compiler TypeScript en JavaScript](#heading-compiler-typescript-en-javascript)
* [Ressources](#heading-ressources)

## Qu'est-ce que TypeScript ?

TypeScript est un langage de programmation orienté objet développé et maintenu par Microsoft. C'est un sur-ensemble de JavaScript, ce qui signifie que tout code JavaScript valide s'exécutera également comme prévu en TypeScript. 

TypeScript possède toutes les fonctionnalités de JavaScript ainsi que certaines fonctionnalités supplémentaires. Il doit être compilé en JavaScript simple pendant l'exécution, vous avez donc besoin d'un compilateur pour récupérer le code JS.

TypeScript utilise la typage statique, ce qui signifie que vous pouvez donner un type à une variable lors de sa déclaration. Et c'est quelque chose qui ne peut pas être fait avec JavaScript car c'est un langage à typage dynamique – il ne connaît pas le type de données d'une variable jusqu'à ce qu'il lui attribue une valeur à l'exécution.

La vérification de type statique rend TypeScript formidable car elle aide à lancer une erreur au moment de la compilation si la variable n'est pas utilisée ou réassignée avec une annotation de type différente. Cependant, l'erreur n'empêche pas le code de s'exécuter (et le code JavaScript sera toujours généré).

Le typage statique est facultatif en TypeScript. Si aucun type n'est défini mais que la variable a une valeur, TypeScript déduira la valeur comme type. Et si la variable n'a pas de valeur, le type sera défini sur any par défaut.

Maintenant, commençons à utiliser TypeScript dans la section suivante pour le voir en action.

## Installation de TypeScript

Comme je l'ai dit plus tôt, TypeScript doit être compilé en JavaScript simple. Nous devons donc utiliser un outil pour faire la compilation. Et pour avoir accès à cet outil, vous devez installer TypeScript en exécutant cette commande dans le terminal.

```shell
  yarn add -g typescript

```

Ou si vous utilisez npm :

```shell
  npm install -g typescript

```

Notez que ici, j'utilise le drapeau `-g` pour installer TypeScript globalement afin de pouvoir y accéder de n'importe où.

En installant TypeScript, nous avons maintenant accès au compilateur, et nous pouvons compiler notre code en JavaScript. 

Plus tard, nous plongerons dans le sujet et verrons ce qu'il fait, mais pour l'instant, ajoutons un fichier de configuration à notre projet. Il n'est pas obligatoire d'ajouter un fichier de configuration - mais dans de nombreux cas, il est utile de l'avoir puisqu'il nous permet de définir des ensembles de règles pour le compilateur.

## Configuration de TypeScript avec tsconfig

`tsconfig` est un fichier JSON qui aide à configurer TypeScript. Avoir un fichier de configuration est mieux puisqu'il aide à contrôler le comportement du compilateur. 

Pour créer le fichier de configuration, vous devez d'abord créer un nouveau répertoire nommé `Pokedex` et naviguer jusqu'à la racine du dossier. Ensuite, ouvrez-le dans le terminal ou un IDE et exécutez cette commande pour générer un nouveau fichier de configuration TypeScript.

```shell
  tsc --init

```

Une fois le fichier généré, nous pouvons maintenant l'explorer dans un IDE.

* `tsconfig.json`

```js
{
    "compilerOptions": {
        "target": "es5",
        "module": "commonjs",
        "outDir": "public/js",
        "rootDir": "src",
        "strict": true,
        "esModuleInterop": true,
        "forceConsistentCasingInFileNames": true
    },
    "include": ["src"]
}

```

Ce fichier de configuration est beaucoup plus verbeux que ce que vous voyez ci-dessus – j'ai supprimé les commentaires et les valeurs inutilisées pour le rendre plus facile à lire. Cela dit, nous pouvons maintenant décomposer ces valeurs, expliquer chacune d'elles et voir ce qu'elles font.

target : il spécifie la version cible d'ECMAScript lors de la compilation du code TypeScript. Ici, nous ciblons `es5` pour supporter tous les navigateurs, vous pouvez le changer en ES6, ES3 (c'est la valeur par défaut si aucune cible n'est spécifiée), ES2020, etc.

module : il définit le module du code compilé. Le module peut être Common JS, ES2015, ES2020, etc.

outDir : il spécifie le répertoire de sortie pour le code compilé en JavaScript.

rootDir : il définit l'emplacement où se trouvent les fichiers TypeScript qui doivent être compilés.

include : il aide à définir quel répertoire doit être compilé. Si vous n'avez pas cette valeur, le compilateur prendra chaque fichier `.ts` et le compilera en JavaScript même si un répertoire de sortie est défini.

Avec cela en place, nous pouvons maintenant plonger dans l'une des parties les plus importantes de TypeScript : les Types.

## Types TypeScript

Les types fournissent un moyen d'améliorer la qualité du code, et ils rendent également le code plus facile à comprendre puisqu'ils définissent les types de variables. Ils sont facultatifs et aident à définir ce qu'une variable donnée doit avoir comme valeur. Ils permettent également au compilateur de détecter les erreurs avant l'exécution.

TypeScript possède plusieurs types tels que number, string, boolean, enum, void, null, undefined, any, never, array et tuple. Nous ne verrons pas tous les types dans ce guide, mais gardez à l'esprit qu'ils existent.

Maintenant, voyons quelques exemples de types de base.

### Types de base de TypeScript

```js
let foo: string = "test"
let bar: number = 1
let baz: string[] = ["This", "is", "a", "Test"]

```

Comme vous pouvez le voir ici, nous avons trois variables avec différents types. `foo` attend une chaîne de caractères, `bar` un nombre, et `baz` un tableau de chaînes de caractères. Si elles reçoivent autre chose que le type déclaré, une erreur sera lancée par TypeScript.

Vous pouvez également déclarer `baz` comme ceci : `let baz: Array<string> = ["This", "is", "a", "Test"]`.

Maintenant, essayons de réassigner l'une de ces variables et voyons comment TypeScript se comporte.

```js
let foo: string = "test"
foo = 1

```

```js
Le type '1' ne peut pas être assigné au type 'string'

```

TypeScript lancera une erreur parce que nous avons déjà déclaré `foo` pour attendre une chaîne de caractères comme valeur. Et cette erreur est détectée au moment de la compilation, ce qui rend TypeScript formidable et utile.

Avec TypeScript, les types peuvent être explicites comme ci-dessus, mais ils peuvent aussi être implicites. Il est préférable de définir explicitement le type d'une valeur donnée car cela aide le compilateur et le prochain développeur qui hérite du code. Mais vous pouvez également déclarer des variables avec une annotation de type implicite.

```js
let foo = "test"
let bar = 1
let baz = ["This", "is", "a", "Test"]

```

TypeScript essaiera ici de déduire autant que possible pour vous donner une sécurité de type avec moins de code. Il prendra la valeur et la définira comme un type pour la variable. Et rien ne changera concernant les erreurs.

Essayons de réassigner ces variables pour voir ce qui se passera.

```js
foo = 7
bar = "updated"
baz = [2, true, "a", 10]

```

TypeScript détectera les erreurs comme avant, même si les types de variables sont déclarés implicitement.

```js
Le type '7' ne peut pas être assigné au type 'string'.
Le type '"updated"' ne peut pas être assigné au type 'number'.
Le type 'true' ne peut pas être assigné au type 'string'.

```

Lorsqu'on traite un objet avec plusieurs propriétés, il peut être délicat et ennuyeux de définir les types. Mais heureusement, TypeScript a quelque chose pour vous aider avec ce cas d'utilisation. Alors, plongeons dans les interfaces et les alias de type de TypeScript dans la section suivante.

### Interfaces et alias de type

Les interfaces et les alias de type nous aident à définir la forme de structures de données similaires à des objets. Ils semblent être la même chose concernant leur structure, mais gardez à l'esprit qu'ils sont différents.

Cependant, le consensus parmi les développeurs est d'utiliser `interface` chaque fois que vous le pouvez puisque c'est dans l'ensemble de règles par défaut de `tslint`.

Maintenant, créons une interface et un alias de type dans la section suivante pour les voir en action.

```js
interface ITest {
  id: number;
  name?: string;
}

type TestType = {
  id: number,
  name?: string,
}

function myTest(args: ITest): string {
  if (args.name) {
    return `Hello ${args.name}`
  }
  return "Hello Word"
}

myTest({ id: 1 })

```

Comme vous pouvez le voir, la structure d'une interface et d'un alias de type ressemble à un objet JavaScript. Ils doivent définir la forme des données données avec TypeScript.

Remarquez que ici, j'utilise un champ optionnel `name` en ajoutant un point d'interrogation (`?`). Cela nous permet de rendre la propriété `name` optionnelle. Cela signifie que si aucune valeur n'est passée à la propriété `name`, elle retournera `undefined` comme valeur.

Ensuite, nous utilisons l'interface `ITest` comme type pour l'argument reçu par la fonction `myTest`. Et comme pour les variables, les fonctions peuvent également être définies pour retourner un type spécifique. Et ici, la valeur de retour doit être une chaîne de caractères, sinon une erreur sera lancée par TypeScript.

Jusqu'à présent, nous avons couvert toutes les connaissances de base nécessaires pour commencer avec TypeScript. Maintenant, utilisons-le pour construire un Pokedex avec HTML et CSS.

_Plongeons-nous._

![excited](https://media.giphy.com/media/WUq1cg9K7uzHa/source.gif)

## Construire une application Pokedex en utilisant TypeScript

Le projet que nous allons construire récupérera des données distantes depuis l'API [Pokemon API](https://pokeapi.co/) et affichera chaque pokemon avec TypeScript.

Alors, commençons par créer trois nouveaux fichiers à la racine du dossier `Pokedex` : `index.html`, `style.css` et `src/app.ts`. Et pour la configuration de TypeScript, nous utiliserons le même fichier `tsconfig.json` créé précédemment.

Maintenant, passons à la partie balisage et ajoutons du contenu au fichier HTML.

### Balises

* `index.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>TypeScript Pokedex</title>
  </head>
  <body>
    <main>
      <h1>Typed Pokedex</h1>
      <div id="app"></div>
    </main>
    <script src="public/js/app.js"></script>
  </body>
</html>

```

Comme vous pouvez le voir, nous avons un balisage relativement simple. Il y a deux choses importantes à retenir : 

* l'id `app` de la balise `div` qui sera utilisé pour ajouter le contenu en utilisant TypeScript, et 
* la balise `script` qui pointe vers le dossier `public` et plus précisément le fichier JavaScript que TypeScript créera pour nous pendant la compilation.

Par ailleurs, le fichier CSS est un peu long, donc je ne le couvrirai pas – je ne veux pas perdre votre temps et je veux rester concentré sur TypeScript. Cela dit, nous pouvons maintenant plonger dedans et commencer à récupérer des données depuis l'API.

### Récupérer et afficher des données en utilisant TypeScript

Nous commençons la partie TS en sélectionnant l'id `app` qui est l'id de la balise div.

* `src/app.ts`

```js
const container: HTMLElement | any = document.getElementById("app")
const pokemons: number = 100

interface IPokemon {
  id: number;
  name: string;
  image: string;
  type: string;
}

```

Ici, nous avons une annotation de type qui n'a pas encore été couverte. Il s'agit d'un type d'union qui permet d'avoir des types alternatifs pour une variable donnée. Cela signifie que si `container` n'est pas de type `HTMLElement`, TypeScript vérifiera à nouveau si la valeur est égale au type après le symbole pipe (`|`) et ainsi de suite car vous pouvez avoir plusieurs types.

Ensuite, nous avons une interface `IPokemon` qui définit la forme d'un objet pokemon qui sera utilisé ensuite dans la fonction responsable de l'affichage du contenu.

* `src/app.ts`

```js
const fetchData = (): void => {
  for (let i = 1; i <= pokemons; i++) {
    getPokemon(i)
  }
}

const getPokemon = async (id: number): Promise<void> => {
  const data: Response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
  const pokemon: any = await data.json()
  const pokemonType: string = pokemon.types
    .map((poke: any) => poke.type.name)
    .join(", ")

  const transformedPokemon = {
    id: pokemon.id,
    name: pokemon.name,
    image: `${pokemon.sprites.front_default}`,
    type: pokemonType,
  }

  showPokemon(transformedPokemon)
}

```

La fonction `fetchData` nous permet de parcourir le nombre de pokemons à récupérer et pour chaque objet d'appeler `getPokemon` avec le numéro du pokemon.

Cela peut prendre du temps pour récupérer les données, nous allons donc utiliser une fonction asynchrone qui retourne une `Promise` de type `void`. Cela signifie que la fonction ne retournera pas de valeur.

Et une fois les données récupérées, nous pouvons maintenant créer un nouvel objet `transformedPokemon` qui reflète l'interface `IPokemon`, puis le passer comme argument à `showPokemon()`.

* `src/app.ts`

```js
const showPokemon = (pokemon: IPokemon): void => {
  let output: string = `
        <div class="card">
            <span class="card--id">#${pokemon.id}</span>
            <img class="card--image" src=${pokemon.image} alt=${pokemon.name} />
            <h1 class="card--name">${pokemon.name}</h1>
            <span class="card--details">${pokemon.type}</span>
        </div>
    `
  container.innerHTML += output
}

fetchData()

```

Comme vous pouvez le voir, la fonction `showPokemon` reçoit en paramètre l'objet pokemon de type `IPokemon` et retourne `void` ou aucune valeur pour être précis. Elle ajoutera simplement le contenu au fichier HTML avec l'aide de l'id `container` (rappelez-vous, c'est la balise `div`).

Super ! Nous avons maintenant fait beaucoup de choses, mais quelque chose manque encore car le fichier `index.html` n'affichera rien si vous essayez de le lancer dans le navigateur. Cela est dû au fait que TypeScript doit être compilé en JavaScript simple. Alors, faisons cela dans la section suivante.

## Compiler TypeScript en JavaScript

Plus tôt dans ce tutoriel, nous avons installé le compilateur TypeScript qui permet de compiler notre code TS en JavaScript. Et pour ce faire, vous devez naviguer jusqu'à la racine du projet et exécuter la commande suivante.

```shell
  tsc

```

Cette commande compilera chaque fichier avec une extension `.ts` en JavaScript. Et puisque nous avons un fichier `tsconfig`, le compilateur suivra les règles définies et ne compilera que les fichiers TS situés dans le dossier `src` et placera le code JS dans le répertoire `public`.

Le compilateur permet également de compiler un seul fichier.

```shell
  tsc myFile.ts

```

Et si vous ne spécifiez pas de nom après le fichier TS (`myFile.ts`), le fichier JS compilé prendra le même nom que le fichier TS.

Si vous ne voulez pas exécuter la commande à chaque changement, ajoutez simplement un drapeau `-w` pour que le compilateur continue de surveiller les changements et recompile le code lorsque nécessaire.

```shell
  tsc -w

```

Et maintenant, si vous lancez le fichier `index.html`, vous verrez votre Pokedex correctement rendu dans le navigateur.

![Pokedex app preview image](https://www.freecodecamp.org/news/content/images/2021/10/pokedex-app.png)

Super ! Nous avons maintenant appris les bases de TypeScript en construisant une application Pokedex avec HTML et CSS.

Prévisualisez le projet terminé [ici](https://codesandbox.io/s/typescript-pokedex-yluzs?file=/src/index.ts) ou trouvez le code source [ici](https://github.com/ibrahima92/pokedex-typescript).

Vous pouvez également trouver d'autres contenus intéressants comme celui-ci sur [mon blog](https://www.ibrahima-ndaw.com) ou me suivre [sur Twitter](https://twitter.com/ibrahima92_) pour être informé lorsque j'écris quelque chose de nouveau.

Merci d'avoir lu.

## Ressources

Voici quelques ressources utiles pour approfondir TypeScript.

[Types TypeScript](https://www.typescriptlang.org/docs/handbook/basic-types.html)

[Options du compilateur TypeScript](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

[Manuel TypeScript](https://www.typescriptlang.org/docs/handbook/basic-types.html)