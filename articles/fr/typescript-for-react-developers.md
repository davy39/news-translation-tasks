---
title: TypeScript pour les développeurs React – Pourquoi TypeScript est utile et comment
  il fonctionne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-03T15:00:03.000Z'
originalURL: https://freecodecamp.org/news/typescript-for-react-developers
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/typescript-cover.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: TypeScript pour les développeurs React – Pourquoi TypeScript est utile
  et comment il fonctionne
seo_desc: "By Daniel Asta\nIf you've been using React for a while, you may have noticed\
  \ times when the freedom and wild nature of JavaScript works against you (and not\
  \ because of JS \U0001F604). This can be especially true if you're working in a\
  \ team. \nYou may not know ..."
---

Par Daniel Asta

Si vous utilisez React depuis un certain temps, vous avez peut-être remarqué des moments où la liberté et la nature sauvage de JavaScript jouent contre vous (et pas à cause de JS 😄). Cela peut être particulièrement vrai si vous travaillez en équipe. 

**Vous ne le savez peut-être pas, mais vous avez besoin de TypeScript – ou au moins, vous devez le tester.**

Permettez-moi d'être clair, j'aime JavaScript et la liberté qu'il offre. En fait, pendant longtemps, j'étais "contre" TypeScript.

Alors, je veux partir en voyage ensemble, pour déterminer si TypeScript vaut la peine d'être utilisé ou s'il est seulement pour les personnes qui ne savent pas coder correctement (c'était une blague interne dans mon équipe il y a longtemps !).

L'idée derrière cet article est de passer en revue les bases de TS et de comprendre les avantages. Cela devrait vous aider à décider si vous voulez ces avantages ou non. Ensuite, dans la deuxième section de cet article, je couvrirai les spécificités de TS avec React.

## Table des matières

- [Ressources](#heading-ressources)
- [Pourquoi utiliser ESLint, Prettier et Husky ?](#heading-pourquoi-utiliser-eslint-prettier-et-husky)
- [Qu'est-ce que TypeScript ?](#heading-quest-ce-que-typescript)
- [Pourquoi se donner la peine de gérer TS ?](#heading-pourquoi-se-donner-la-peine-de-gerer-ts)
- [Comment installer TypeScript](#heading-comment-installer-typescript)
- [Projet de liste de courses exemple](#heading-projet-de-liste-de-courses-exemple)
  - [Modules TypeScript](#heading-modules-typescript)
  - [Types TypeScript](#heading-types-typescript)
    - [Inférence dans TypeScript](#heading-inference-dans-typescript)
    - [`any` et `unknown` dans TypeScript](#heading-any-et-unknown-dans-typescript)
    - [Tableaux dans TypeScript](#heading-tableaux-dans-typescript)
    - [Objets dans TypeScript](#heading-objets-dans-typescript)
    - [Alias dans TypeScript](#heading-alias-dans-typescript)
  - [Fonctions dans TypeScript](#heading-fonctions-dans-typescript)
    - [Paramètres optionnels dans TypeScript](#heading-parametres-optionnels-dans-typescript)
  - [Énumérations TypeScript](#heading-enumerations-typescript)
  - [Génériques TypeScript](#heading-generiques-typescript)
  - [Tuples dans TypeScript](#heading-tuples-dans-typescript)
  - [Classes dans TypeScript](#heading-classes-dans-typescript)
  - [Interfaces dans TypeScript](#heading-interfaces-dans-typescript)
  - [Manipulation du DOM dans TypeScript](#heading-manipulation-du-dom-dans-typescript)
- [Comment combiner React + TypeScript](#heading-comment-combiner-react-typescript)
  - [Installation](#heading-installation)
  - [Typage des props des composants](#heading-typage-des-props-des-composants)
    - [Types intégrés de React](#heading-types-integres-de-react)
    - [Type de retour d'un composant React](#heading-type-de-retour-dun-composant-react)
    - [Combinations avec les littéraux de gabarit](#heading-combinations-avec-les-litteraux-de-gabarit)
    - [Comment utiliser `Exclude`](#heading-comment-utiliser-exclude)
    - [Composants HTML personnalisés](#heading-composants-html-personnalises)
  - [Typage des Hooks](#heading-typage-des-hooks)
    - [Hook useState](#heading-hook-usestate)
    - [Hook useReducer](#heading-hook-usereducer)
    - [useContext](#heading-usecontext)
    - [Hook useRef](#heading-hook-useref)
  - [Transmission de ref](#heading-transmission-de-ref)
  - [Comment utiliser les génériques TypeScript dans React](#heading-comment-utiliser-les-generiques-typescript-dans-react)
  - [Typage d'un Hook useFetch personnalisé](#heading-typage-dun-hook-usefetch-personnalise)
- [Conclusion](#heading-conclusion)

## Ressources

Voici quelques petits modèles de base pour commencer :

- [Create React App + TypeScript + ESLint + Prettier Boilerplate](https://github.com/dastasoft/react-boilerplate/tree/cra-typescript)
- [Vite + TypeScript + ESLint + Prettier Boilerplate](https://github.com/dastasoft/react-boilerplate/tree/vite-typescript)

Si vous aimez les jeux de programmation, essayez [PhaserJS](https://phaser.io/). Vous pouvez créer des jeux pour le navigateur avec TypeScript et c'est une manière amusante de l'apprendre.

Assurez-vous également de consulter [The Official Handbook of TS](https://www.typescriptlang.org/docs/handbook/intro.html). Il contient des tonnes de documentation et d'exemples utiles.

Nous allons également examiner deux projets exemples afin que vous ayez du code réel à consulter et à tester des implémentations réelles. Les voici :

### Projet de liste de courses

![shopping-list](https://www.freecodecamp.org/news/content/images/2022/10/shopping-list.jpg)

Il s'agit d'un projet simple pour tester l'expérience du développeur TypeScript sans Webpack, React ou tout autre ajout – juste du TypeScript pur converti en JavaScript.

- [Exemple en direct](https://shopping-list.dastasoft.com/)
- [Code source](https://github.com/dastasoft/shopping-list)

### Projet AnimeTrailers

![animetrailers-screenshot](https://www.freecodecamp.org/news/content/images/2022/10/animetrailers-screenshot.jpg)

Pour l'intégration de TypeScript avec React, j'ai construit un autre projet exemple. Il s'agit d'une application fictive qui, grâce à [JikanAPI](https://jikan.moe/), fournit une liste d'anime et des informations de base pour regarder les dernières bandes-annonces de vos anime préférés.

- [Exemple en direct](https://animetrailers.dastasoft.com/)
- [Code source](https://github.com/dastasoft/animetrailers)

## Pourquoi utiliser ESLint, Prettier et Husky ?

Dans les modèles de base, j'ai tendance à utiliser les règles ESLint d'Airbnb, les règles recommandées de Prettier et les actions de pré-commit de Husky. Cela est assez utile, surtout dans un environnement d'équipe où vous avez besoin que tout le monde suive le même style de code. Mais vous pouvez également en bénéficier en tant que développeur solo ou en tant qu'apprenant.

Les règles d'Airbnb peuvent parfois sembler étranges, mais elles fournissent une excellente explication et des exemples. Ainsi, vous pouvez décider si la règle a du sens pour vous ou non. Si ce n'est pas le cas, vous pouvez la désactiver dans le fichier `.eslintrc`. 

J'ai trouvé que pour les développeurs juniors ou les personnes qui commencent tout juste avec JS ou TS, ces règles sont très utiles. Je vous recommande donc au moins d'essayer de les inclure dans un projet et de vérifier les résultats. 😉

## Qu'est-ce que TypeScript ?

[TypeScript](https://www.typescriptlang.org/) ou TS est un langage open source développé et maintenu par Microsoft. Voici quelques autres faits sur TS :

- C'est un langage multi-paradigme (comme JavaScript).
- C'est une alternative à JavaScript (plus précisément, un sur-ensemble)
- Il permet l'utilisation de types statiques
- Il a des fonctionnalités supplémentaires (génériques, interfaces, tuples, etc., qui seront expliqués en détail ci-dessous)
- Il permet une adoption progressive (c'est-à-dire que vous pouvez transformer un projet existant en un projet TS en changeant les fichiers un par un, ce n'est pas un changement radical).
- Vous pouvez l'utiliser pour le développement front-end et back-end (comme JS)

Le navigateur ne comprend pas le code TS. Il doit être *transcompilé* en JS. JS a une cartographie de type dynamique et TS a des types statiques qui sont moins sujets aux erreurs.

Dans React, vous *transcompilez* déjà JS avec [Babel](https://babeljs.io/), donc avoir à *transcompiler* le code n'est pas un inconvénient supplémentaire de nos jours.

## Pourquoi se donner la peine de gérer TS ?

C'est la question – pourquoi se donner la peine avec TS quand vous êtes heureux avec JS et que tout va bien ? Il y a quelque temps, comme je l'ai dit avant, nous avions une blague interne sur les langues comme TS avec des types (je faisais du Java à l'époque d'ailleurs). Mon équipe plaisantait en disant que vous avez besoin de types si vous ne savez pas comment coder correctement.

TypeScript, Java et un tas d'autres langages ont une **typage statique** qui définira un type associé à une variable. Le type sera vérifié lors de la compilation. Une fois que vous avez défini quelque chose comme une *chaîne* ou un *booléen*, vous ne pouvez pas changer son type.

JavaScript, en revanche, a un **typage dynamique**. Cela signifie que vous pouvez assigner une chaîne à une variable, et plus tard la convertir en booléen, en nombre, ou ce que vous voulez. Le type sera assigné dynamiquement à l'exécution.

Mais quand vous regardez le code TS sur Internet, vous pouvez voir...

![sintactic sugar](https://blog.dastasoft.com/_next/image?url=%2Fassets%2Fposts%2Fcontent%2Ftypescript%2Fsyntaxsugar.jpeg&w=1920&q=75 "Syntactic Sugar, syntactic sugar everywhere.")

Alors, en revenant à l'ancienne blague de mon équipe, oui en effet **c'était correct** : si vous savez exactement ce que vous faites, vous n'avez pas besoin de quelqu'un qui vous dit constamment que ceci est une chaîne et seulement une chaîne, et si à un moment donné cela devient un booléen ou autre chose.... Je sais ce que je fais !

Mais la vérité est que nous ne sommes pas parfaits, et des choses arrivent :

- Travailler dans la précipitation.
- Avoir une mauvaise journée.
- Laisser une idée le vendredi et quand vous revenez le lundi vous n'avez plus la même image de la situation.
- Travailler en équipe, et tout le monde n'a pas le même niveau et/ou la même vision.

Pour les mêmes raisons, nous utilisons un IDE, des extensions d'IDE, la coloration syntaxique et les linters au lieu de l'application Notepad. TypeScript peut s'intégrer dans ces aides.

![airbnb bugs](https://blog.dastasoft.com/_next/image?url=%2Fassets%2Fposts%2Fcontent%2Ftypescript%2Fairbnb.jpg&w=1920&q=75 "Airbnb affirme que 38 % des bugs sur Airbnb auraient pu être évités en utilisant TypeScript.")


### Quelques exemples d'erreurs courantes

Examinons quelques exemples de base avec et sans TS dans l'équation :

#### S'il vous plaît, je sais ce que j'utilise

```js
// App.js
import { MemoryRouter as Router } from 'react-router-dom'

import Routes from './routes'

export default function App() {
  return (
    <Router basename="/my-fancy-app">
      <Routes />
    </Router>
  )
}
```

Voyez-vous quelque chose d'inhabituel dans le code ci-dessus ? Si oui, félicitez-vous.

Ce fichier était dans mon modèle de base pendant longtemps. Ce n'est pas un bug mais... `MemoryRouter` n'a pas besoin de `basename` du tout. Cela arrive parce qu'à un moment donné dans le passé, `BrowserRouter` était utilisé, qui en fait a besoin d'une propriété `basename`.

Avec TS, vous serez informé que `No overload matches this call` qui vous indique qu'il n'y a pas de signature pour ce composant avec cette propriété.

**TypeScript ne fonctionne pas seulement comme un typage statique, mais il vous aide à mieux comprendre les besoins des autres bibliothèques**. Par autres, je veux dire les composants et fonctions de tiers ou de vos collègues.

Oui, je peux entendre la réponse – vous devez bien connaître les bibliothèques que vous utilisez, et encore une fois, vous avez raison. Mais supposer que tout le monde impliqué dans un projet connaît chaque bibliothèque "externe" et les nuances des versions peut être une tâche ardue.

#### Le drapeau du diable

```ts
let isVerified = false;
verifyAmount();

// isVerified = "false"
if (isVerified) proceedPayment();
```

J'ai vu cette erreur de nombreuses fois. Je n'ai pas le code exact et chaque fois il a une nuance différente, mais vous pouvez comprendre le point. Vous avez une variable booléenne qui est responsable de laisser un certain code s'exécuter ou non et à un moment donné quelqu'un d'autre (ou peut-être vous-même dans une erreur) transforme le booléen en chaîne et une chaîne non vide est une valeur vraie.

Avec TypeScript, vous auriez eu l'erreur : `Le type 'string' ne peut pas être assigné au type 'boolean'`. Cette erreur se produira au moment de la compilation, même si vous n'avez pas votre application en cours d'exécution à ce moment-là. Les chances que l'erreur se retrouve en production sont donc très faibles.

Encore une fois, nous pouvons appliquer la même règle que précédemment – si vous codez correctement, cela n'arrive pas. Si vous suivez les règles du Clean Code et que vous êtes prudent avec ce que vous faites, cela peut également être évité. **TypeScript n'est pas destiné à nous permettre d'être paresseux et désorganisés – mais il peut être un bon allié**, comme la coloration syntaxique peut aider à éviter certaines erreurs ou à détecter les variables inutilisées.

#### Je pensais que le chat était vivant dans cette boîte

```ts
const MONTH_SELECT_OPTIONS = MONTHS.map((month) => ({
  label: getMonthName(month),
  value: month,
}))

export default function PaymentDisplayer() {
  const [currentMonthFilter, setCurrentMonthFilter] = useState(
    MONTH_SELECT_OPTIONS[0]
  )

  const onChangeHandler = option => {
    setCurrentMonthFilter(option.value)
  }

  return (
    <select onChange={onChangeHandler}>
      {MONTH_SELECT_OPTIONS.map(({ label, value }) => (
        <option key="value" value={value}>
          {label}
        </option>
      ))}
    </select>
  )
}
```

Il est très courant (et peut-être non recommandé) de changer le type d'un état. Parfois, c'est intentionnel comme avoir un indicateur `isError` et soudainement le changer de booléen faux à une chaîne de message d'erreur (et encore une fois, pas du tout recommandé !). Mais dans d'autres scénarios, c'est par erreur, comme dans l'exemple ci-dessus.

La personne qui a écrit cela en premier lieu pensait que dans `currentMonthFilter`, elle stockerait l'option réelle de la sélection, un `HTMLOptionElement` avec label et value. Plus tard, la même personne un autre jour (ou peut-être un autre développeur) crée le `changeHandler` et définit la valeur au lieu de l'option complète.

L'exemple ci-dessus fonctionne et est simplifié pour l'apprentissage. Mais imaginez cela à grande échelle, surtout dans ces composants où les actions sont passées en dessous en tant que props.

Ici, TypeScript nous aiderait de deux manières :

- Le typage statique générera une erreur lors de la tentative de changement du type de `currentMonthFilter` de `{label: string, value: number}` à `number`.
- La personne codant l'étape suivante de l'appel d'un service pour récupérer les paiements avec ce filtre saura grâce à *IntelliSense* quel type elle obtiendra de l'état et si cela correspond au type dont le service a besoin.

Ainsi, TypeScript nous permet également d'**inspecter depuis l'IDE les différentes fonctions, paramètres et documentation des bibliothèques tierces et des composants de nos pairs**.

À travers ces exemples (qui ne sont peut-être pas trop représentatifs pour être honnête), nous pouvons conclure que TypeScript essaie de nous aider dans un environnement React avec :

- Être cohérent dans le typage et constant avec les types statiques
- Fournir une documentation et *IntelliSense* des possibilités disponibles
- Détecter les bugs tôt

## Comment installer TypeScript

Dans cet article, nous utiliserons l'installation globale. C'est parce que je pense qu'il est préférable de plonger d'abord dans TypeScript en isolation sans aucun Webpack, React ou autre variable et de voir comment il fonctionne et quels problèmes il résout.

### Comment installer TypeScript globalement

```bash
npm install -g typescript

#ou

yarn install --global typescript
```

### Comment fonctionne le compilateur TypeScript (tsc)

Une fois que vous avez installé TypeScript sur votre système ou avec l'une des autres options mentionnées ci-dessus, vous pouvez utiliser le compilateur TypeScript, en utilisant la commande `tsc`.

Testons le compilateur avec la configuration minimale :

- Créez un nouveau dossier vide
- Placez un `index.html` avec la structure HTML5 de base à l'intérieur.
- Créez un fichier `index.ts` vide au même niveau que `index.html`.
- Ouvrez un terminal et tapez `tsc --init` (en supposant que vous avez installé TypeScript globalement), cela créera pour vous un `tsconfig.json` (nous examinerons ce fichier en détail dans la section suivante).

Vous aurez quelque chose comme ceci :

```sh
- index.html
- index.ts
- tsconfig.json
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body></body>
</html>
```

Maintenant, vous devez inclure le fichier TS dans le HTML. Mais les navigateurs ne comprennent pas TypeScript, ils comprennent JavaScript, donc vous pouvez modifier votre `index.html` comme suit :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body></body>
  <script src="./index.js"></script>
</html>
```

Ouvrez un nouveau terminal et tapez `tsc`. Votre fichier `index.ts` sera converti en un `index.js` que le navigateur peut lire.

Au lieu de taper la commande `tsc` chaque fois que vous voulez compiler le fichier TS en un fichier JS, vous pouvez mettre TypeScript en mode surveillance avec `tsc -w`.

Maintenant, ma recommandation est que vous ouvriez les fichiers TS et JS côte à côte. Ensuite, tapez du JS régulier dans le fichier `index.ts`, et testez les sorties. (Nous utiliserons beaucoup cela dans les sections suivantes pour tester ce que TS génère).

![side by side](https://blog.dastasoft.com/_next/image?url=%2Fassets%2Fposts%2Fcontent%2Ftypescript%2Fside-by-side.png&w=1920&q=75 "Do some test using tsc -w option")

### Qu'y a-t-il dans `tsconfig.json`

Si vous suivez l'article, vous avez créé ce fichier avec la commande `tsc --init`. Il crée le `tsconfig.json` avec une configuration par défaut et un tas de commentaires qui sont excellents pour commencer.

Examinons quelques-unes des propriétés qui peuvent être utiles pour vous lancer :

- `target` est la version de JS vers laquelle nous convertissons notre code TS. Selon les navigateurs que vous souhaitez supporter, vous devrez peut-être définir une version plus ancienne. Cela peut également être une bonne ressource d'apprentissage – essayez de jouer avec différentes versions et voyez quel code JS est généré.
- `module` définit quel type de syntaxe vous utiliserez pour les modules. `commonjs` qui est la valeur par défaut utilise `require/module.exports` et le JS moderne (ES6+) utilise `import/export`. Si vous voulez utiliser `import/export`, vous devez changer `target` en ES6 ou supérieur. Dans le projet exemple, nous utiliserons cette syntaxe, alors vérifiez le reste de l'article pour cela.
- `lib` Vous en avez besoin pour spécifier les bibliothèques supplémentaires que vous utiliserez dans votre projet et vérifier les types supplémentaires, par exemple ceux liés au DOM.
- `jsx` Dans React, vous devrez le définir au moins à `preserve`. Ce mode suppose qu'un autre outil compilera cette partie (Babel dans ce cas) mais TSC effectuera la vérification des types. Vous pouvez définir cette propriété à `react` ou `react-native`. Vous l'utilisez si vous voulez que TSC compile votre code JSX en code JS régulier. Dans la plupart des cas, nous laisserons cette propriété à `preserve` qui enverra le fichier en tant que JSX régulier et Babel/Webpack fera le reste.
- `outDir` où les fichiers seront placés après la compilation, par exemple dans la plupart des projets React, il sera placé dans un dossier `build`.
- `rootDir` où les fichiers seront pris pour la compilation. Dans la plupart des projets React, ce sera `./src`.
- `strict` active un ensemble de règles pour la vérification des types, ce qui entraîne une vérification plus stricte de ce qui est considéré comme "correct". Je recommande de commencer avec cette option désactivée lorsque vous apprenez. Ensuite, lorsque vous vous sentez suffisamment confiant, activez-la et vérifiez quels nouveaux drapeaux rouges vous avez. Mais rappelez-vous que vous obtiendrez le plein potentiel de TS avec cette option activée. Cette option active également toutes les options strictes ci-dessous, que vous pouvez désactiver individuellement.
- `include` le(s) dossier(s) que vous souhaitez inclure pour être compilé(s), par exemple le dossier `src`
- `exclude` le(s) dossier(s) que vous souhaitez empêcher d'être compilé(s), par exemple le dossier `node_modules`.

Dans le projet exemple pour cet article, nous prendrons les fichiers `rootDir` de `./src` et les placerons dans le dossier `public` avec `outDir`.

## Projet de liste de courses exemple

Le projet exemple est très basique : vous pouvez insérer différents articles et leurs quantités dans différentes sections de votre liste de courses. Ensuite, vous pouvez les supprimer pendant que vous faites vos courses et vérifier ce que vous devez acheter ensuite.

L'idée derrière ce projet exemple est de se familiariser avec TypeScript et le flux de travail général. Une fois que vous entrez dans l'environnement React, beaucoup de la magie est faite pour vous par Webpack ou tout autre bundler. Je pense donc qu'il est important de connaître les choses très basiques et ensuite de profiter du travail que le bundler fait pour vous.

Voyons ce que nous pouvons utiliser de TS pour obtenir une base de code meilleure et moins sujette aux erreurs.

### Modules TypeScript

Si vous voulez utiliser les modules `import/export` ES6, vous devez configurer `tsconfig` avec :

- **target** : es6 ou supérieur
- **module** : es2015 ou ultérieur

Et dans le fichier `index.html`, vous devez ajouter le type de module comme ceci :

```html
<script type="module" src="app.js"></script> 
```

Mais gardez à l'esprit que l'utilisation de modules a deux inconvénients :

- La compatibilité avec les anciens navigateurs est moins probable.
- Les fichiers en production seront divisés, donc vous aurez plusieurs requêtes pour chaque fichier (ceci peut être corrigé en utilisant un bundler comme Webpack).

### Types TypeScript

En JavaScript, les types sont assignés à l'exécution. Lorsque l'interpréteur voit votre variable et la valeur, il décide de quel type il s'agit. Cela signifie que nous pouvons faire des choses comme ceci :

```ts
let job = "Warrior"; // string
let level = 75; // number
let isExpansionJob = false; // boolean

level = "iLevel" + 75 
// maintenant c'est une string
```

Dans TypeScript, les types sont assignés au moment de la compilation. Donc une fois le type défini, il sera protégé sous cette signature.

```ts
let job: string = "Samurai";
let level: number = 75;
let isExpansionJob: boolean = true;

level = "iLevel" + 75 
// Erreur, le type string ne peut pas
// être assigné au type number !
```

#### Inférence dans TypeScript

En fait, il n'est pas nécessaire de préciser explicitement le type que vous voulez pour les variables. TS peut inférer le type par sa valeur.

```ts
let job = "Samurai";
let level = 75;
let isExpansionJob = true;

level = "iLevel" + 75 
// Erreur, le type string ne peut pas 
// être assigné au type number !
```

Dans React, que nous examinerons dans la deuxième section de cet article en détail, vous verrez également l'inférence – par exemple dans `useState`

```ts
const [currentMonthFilter, setCurrentMonthFilter] = useState("January")

useEffect(() => {
   setCurrentMonthFilter(1) 
   // Erreur, le type number ne peut pas 
   // être assigné au type string !
}, [])
```

#### `any` et `unknown` dans TypeScript

J'ai dit tout au long que TS a des types statiques, mais il y a une nuance à cette déclaration.

```ts
let level: any = 10;

level = "iLevel" + 125; 
// OK, toujours type any

level = false; 
// OK, toujours type any
```

Bienvenue à JavaScript ! `any` est un type dynamique pour quand vous ne savez pas quel type la variable sera à l'avenir – mais il inverse d'une certaine manière tous les avantages que TS fournit.

```ts
let level: any = 10;

level = "iLevel" + 125;

level = false;

let stringLevel: string = level;
console.log(typeof stringLevel);
stringLevel.replace("false", "true");
```

Lorsque vous assignez `level` à `stringLevel` de type `string`, il ne devient pas une chaîne, il reste un booléen. Donc la fonction `replace` n'existe pas et le code échoue à l'exécution. Vous obtiendrez `Uncaught TypeError: stringLevel.replace is not a function`.

Pour cela, nous avons un autre type qui est le pendant sûr du type `any` :

```ts
let level: unknown = 10;

level = "iLevel" + 125;

level = false;

let stringLevel: string = level; 
// Erreur
```

Avec `unknown`, vous pouvez assigner n'importe quel type comme dans `any`, mais cette fois le compilateur obtient l'erreur lorsque vous essayez d'assigner à un autre type. Donc si vous ne savez pas quel type il sera, essayez d'utiliser `unknown` au lieu de `any`.

#### Tableaux dans TypeScript

```ts
let job = "Red Mage";
let level = 75;
let isExpansionJob = false;
let jobAbilities = ['Chainspell', 'Convert'];

jobAbilities.push('Composure'); // OK
jobAbilities.push(2); // Erreur
jobAbilities[0] = 2; // Erreur
```

Dans l'exemple ci-dessus, nous avons déclaré un tableau de chaînes `jobAbilities`. Nous pouvons ajouter plus de chaînes, mais nous ne pouvons pas ajouter d'autres types ou changer les valeurs actuelles en valeurs d'autres types. Cela est dû au fait que dans la déclaration, nous avons fait l'inférence du type `string[]`.

```ts
let job = "Red Mage";
let level = 75;
let isExpansionJob = false;
let jobAbilities = ['Chainspell', 'Convert'];
let swordSkill = ["B", 5, 144, 398]; 

swordSkill.push("B+"); // OK
swordSkill.push(230); // OK

swordSkill[1] = "C"; 
// OK, le type n'est pas lié à la position

swordSkill.push(true); // Erreur
```

Comme dans l'exemple précédent, l'inférence de type est faite dans la déclaration. Nous déclarons maintenant un tableau de chaînes et de nombres pour `swordSkill`.

Si vous voulez déclarer explicitement les types pour les tableaux que nous avons vus dans les exemples :

```ts
let jobAbilities: string[] = ['Chainspell', 'Convert'];
let swordSkill: (string | number)[] = ["B", 5, 144, 398];
```

Au fait, `|` est pour faire une `union` de différents types.

#### Objets dans TypeScript

Revenons à l'exemple – mais maintenant sous la forme d'un objet :

```ts
let job = {
  name: "Summoner",
  level: 75,
  isExpansion: true,
  jobAbilities: ["Astral Flow", "Elemental Siphon"]
};

job.name = "Blue Mage"; // OK
job.level = "Four" // Erreur
job.avatars = ["Carbuncle"]; // Erreur
```

- `job.level = "Four"` ne peut pas être fait car nous ne pouvons pas changer le type d'une propriété. Les propriétés ont également des types statiques.
- `job.avatars = ["Carbuncle"]` – nous ne pouvons pas ajouter de nouvelles propriétés, car l'objet `job` a déjà un type qui a une structure définie.

```ts
let job = {
  name: "Summoner",
  level: 75,
  isExpansion: true,
  jobAbilities: ["Astral Flow", "Elemental Siphon"]
};

job = {
  name: "Blue Mage",
  level: 4,
  isExpansion: true,
  jobAbilities: ["Azure Lore", "Burst Affinity"]
}; // OK

job = {
  name: "Corsair",
  level: 25,
  isExpansion: true
}; // Erreur
```

Nous pouvons assigner un autre objet, car nous définissons l'objet comme `let`, mais il doit être dans la forme exacte.

Prenez un moment et réfléchissez-y : combien de fois répétez-vous les structures d'objets dans le front-end sans aucun type de vérification comme celle-ci ? Combien de fois avez-vous fait une faute de frappe en tapant `data.descrption` et des jours plus tard vous découvrez le bug ? Si ce n'est pas le cas, je peux vous promettre que cela arrivera plus tôt que tard.

Vérifions le type explicite de notre exemple :

```ts
let job: {
  name: string;
  level: number;
  isExpansion: boolean;
  jobAbilities: string[];
} = {
  name: "Summoner",
  level: 75,
  isExpansion: true,
  jobAbilities: ["Astral Flow", "Elemental Siphon"]
};
```

Comme vous pouvez le voir, cela devient un peu plus grand pour un simple objet, donc dans ce cas, nous pouvons utiliser des `alias de type`.

#### Alias dans TypeScript

```ts
type Job = {
  name: string;
  level: number;
  isExpansion: boolean;
  jobAbilities: string[];
};

let Summoner: Job = {
  name: "Summoner",
  level: 75,
  isExpansion: true,
  jobAbilities: ["Astral Flow", "Elemental Siphon"]
};

let BlueMage: Job = {
  name: "Blue Mage",
  level: 4,
  isExpansion: true,
  jobAbilities: ["Azure Lore", "Burst Affinity"]
};
```

Avec les alias de type, nous pouvons définir un type commun pour la réutilisation. Dans React, DOM et d'autres bibliothèques, vous trouverez beaucoup de types prêts à l'emploi définis.

### Fonctions dans TypeScript

La syntaxe des fonctions est assez similaire à celle de JS, mais vous pouvez spécifier le type du paramètre et le type du retour.

```ts
type Enemy = {
  name: string;
  hp: number;
  level: number;
  exp: number;
};

let attack = (target: Enemy) => {
  console.log(`Attacking to ${target.name}`);
};

attack = "Hello Enemy"; // Erreur
```

J'utilise une fonction fléchée, mais vous pouvez également utiliser des déclarations de fonction régulières. Il y a deux différences principales dans les fonctions entre JS et TS :

- Vous spécifiez le type des paramètres que vous passez à la fonction, comme notre `target: Enemy`.
- La variable `attack` reçoit le type du retour de la fonction, donc vous ne pouvez pas changer son type par la suite.

Le type de la fonction est décrit comme suit :

```ts
let attack = (target: Enemy): void => {
  console.log(`Attacking to ${target.name}`);
};
```

Le type `void` est utilisé lorsque le type de retour est rien, et il n'est pas non plus nécessaire de définir explicitement le type :

```ts
// let attack = (target: Enemy): number => {
let attack = (target: Enemy) => {
  return target.hp - 2;
};
```

Comme avec `any`, le type `void` a quelques nuances :

```ts
let attack = (target: Enemy): void => {
  console.log(`Attacking to ${target.name}`);
};

attack = (target: Enemy): number => {
  return target.hp - 2;
};

// lizard has 200hp
console.log(attack(lizard)); // 198
```

L'exemple ci-dessus n'a pas d'erreurs – même si vous pensez avoir changé `attack` de `(target: Enemy) => void` à `(target: Enemy) => number`, il est toujours `void`.

Vérifiez ce qui se passe si vous définissez la fonction avec le `number` en premier.

```ts
let attack = (target: Enemy) => {
  return target.hp - 2;
};

attack = (target: Enemy) => {
  console.log(`Attacking to ${target.name}`);
}; // Erreur

let attackResult = attack(lizard);
```

`Type '(target: Enemy) => void' is not assignable to the type '(target: Enemy) => number'`. `Type 'void' is not assignable to the type 'number'`. Donc, `void` fonctionne comme `any` dans ce scénario.

Pour `attackResult`, le type sera `number`. Il n'est pas nécessaire de le spécifier – TS inférera le type à partir du type de retour de la fonction.

#### Paramètres optionnels dans TypeScript

Vous pouvez définir des paramètres optionnels dans les fonctions avec `?`.

```ts
let heal = (target: Player | Enemy, spell: Spell, message?: string) => {
  if (message) console.log(message);
  return target.hp + spell.power;
};

heal(player1); // Erreur
heal(player1, cure, "Healing player1"); // OK
heal(skeleton, cure); // OK
```

Le premier appel ne fonctionnera pas car nous devons passer au moins deux paramètres, mais le deuxième et le troisième sont corrects. `message` est un paramètre optionnel. Lorsqu'il n'est pas passé, il sera reçu comme `undefined`.

Si vous comparez le dernier exemple avec une simple fonction JS :

```ts
let heal = (target, spell, message) => {
  if (message) console.log(message);
  return target.hp + spell.power;
};

heal(player1); // Erreur
heal(player1, cure, "Healing player1"); // OK
heal(skeleton, cure); // OK
```

Le comportement de base sera le même, mais la différence est que l'erreur apparaîtra à l'exécution, car dans le premier appel, vous ne pouvez pas appeler `power` à partir d'une valeur indéfinie.

Comme vous pouvez le voir à partir de ces exemples, travailler avec des fonctions est plus sûr dans TS car vous n'avez pas besoin de vous fier à ce qui se passe à l'extérieur. Vous savez quels paramètres doivent arriver et sous quelle forme. 

Il en va de même pour les personnes utilisant votre fonction : elles sauront exactement quels paramètres sont nécessaires, la forme et ce qu'elles obtiendront de la fonction.

### Énumérations TypeScript

Avec les énumérations, nous pouvons définir une collection de constantes.

```ts
enum BattleMenu {
  ATTACK,
  MAGIC,
  ABILITIES,
  ITEMS,
  DISENGAGE
}

enum Equipment {
  WEAPON = 0,
  HEAD = 1,
  BODY = 2,
  HANDS = 3,
  LEGS = 4
}

console.log(BattleMenu.ATTACK, Equipment.WEAPON); 
// 0 0
```

Les énumérations sont auto-indexées par défaut – les deux déclarations dans l'exemple ci-dessus sont équivalentes.

Les énumérations peuvent également stocker des chaînes. Par exemple, dans React, j'utilise souvent des énumérations pour stocker des chemins :

```ts
enum Routes {
  HOME = "/",
  ABOUT = "/about",
  BLOG = "/blog"
}
```

### Génériques TypeScript

```ts
const getPartyLeader = (memberList: Player[]) => {
  return memberList[0];
};

const partyLeader = getPartyLeader(partyA);
```

Nous voulons implémenter une fonction `getPartyLeader` qui retourne le leader du groupe qui est le premier dans le tableau.

Et si nous voulons supporter d'autres types que `Player` ? Nous pouvons trouver cette solution pour l'instant :

```ts
const getPartyLeader = (memberList: Player[] | Enemy[]) => {
  return memberList[0];
};

const partyLeader = getPartyLeader(partyA); 
// Player[] | Enemy[]
```

OK, maintenant nous pouvons passer un groupe de `Player` ou un groupe d'`Enemy`, mais notre constante `PartyLeader` peut être l'un ou l'autre. Donc la vérification de type est `Player[] | Enemy[]`.

Si nous voulons assigner le type exactement, une façon est d'utiliser les génériques :

```ts
const getPartyLeader = <T>(memberList: T[]) => {
  return memberList[0];
};

const partyLeader = getPartyLeader(partyA); // Player
```

Comme `partyA` est rempli de types `Player`, `partyLeader` sera de type `Player`. Mais vérifions la syntaxe :

- `T` est la manière commune de définir un générique, mais vous pouvez l'appeler comme vous voulez.

Maintenant, le problème peut être, comme avec `any`, que T accepte tout. Donc nous pouvons ajuster le type de choses que nous voulons pouvoir passer à cette fonction :

```ts
type Player = {
  name: string;
  hp: number;
};

type Enemy = {
  name: string;
  hp: number;
};

type Spell = {
  name: string;
  power: number;
};

const getPartyLeader = <T extends { hp: number }>(memberList: T[]) => {
  return memberList[0];
};

const playerPartyLeader = getPartyLeader(partyOfPlayers); // Ok
const enemyPartyLeader = getPartyLeader(partyOfEnemies); // Ok
const whatAreYouTrying = getPartyLeader(spellList); // Erreur
```

Nous pouvons maintenant seulement passer des types contenant la propriété `hp`.

### Tuples dans TypeScript

Comme nous l'avons vu précédemment, un Array peut contenir différents types mais n'est pas restreint à la position. Le type Tuple est juste pour couvrir cela :

```ts
type Weapon = {
  name: string;
  damage: number;
};

type Shield = {
  name: string;
  def: number;
};

const sword: Weapon = {
  name: "Onion Sword",
  damage: 10
};

const shield: Shield = {
  name: "Rusty Shield",
  def: 5
};

let equipment: [Weapon, Shield, boolean];

equipment = [sword, shield, true]; // OK
equipment[2] = false; // OK

equipment = [shield, sword, false]; // Erreur
equipment[1] = true; // Erreur
```

Nous avons maintenant un type similaire à un tableau, qui se soucie de l'endroit où les types sont placés.

### Classes dans TypeScript

Avec ES6, les classes ont été ajoutées à JavaScript. Il n'y a donc pas de grande différence entre les classes JS et TS.

```ts
class Job {
  public name: string;
  private level: number;
  readonly isExpansion: boolean;

  constructor(name: string, level: number, isExpansion: boolean) {
    this.name = name;
    this.level = level;
    this.isExpansion = isExpansion;
  }
}

const whiteMage = new Job("White Mage", 75, false);

console.log(whiteMage.name); // "White Mage"
console.log(whiteMage.level); // Erreur
console.log(whiteMage.isExpansion); // false

whiteMage.name = "Blue Mage"; // Ok
whiteMage.level = 50; // Erreur
whiteMage.isExpansion = true; // Erreur
```

Dans les classes TS, vous avez des modificateurs d'accès pour les propriétés d'une classe :

- **public** - les propriétés et méthodes seront accessibles depuis tous les emplacements. C'est la valeur par défaut.
- **private** - vous ne pouvez accéder à la propriété qu'à l'intérieur de la même classe.
- **protected** - limite l'accès à la classe et aux sous-classes.
- **readonly** - marque la propriété comme immuable.

### Interfaces dans TypeScript

De manière similaire à ce que nous avons vu avec les `alias de type`, nous pouvons définir un type via une `interface`.

```ts
interface Enemy {
  name: string;
  hp: number;
}

let attack = (target: Enemy): void => {
  console.log(`Attacking to ${target.name}`);
};
```

Donc, cela semble être la même chose que les `alias de type`, n'est-ce pas ? Lequel utiliser ? Les deux ont gagné en capacités au fil des différentes versions de TS et les nuances entre eux sont maintenant très faibles.

Vous devez suivre ces règles :

- Si vous écrivez du code orienté objet, utilisez des interfaces. Si vous écrivez du code fonctionnel, utilisez des alias de type.
- Utilisez des interfaces pour les bibliothèques d'API publiques et des types pour les composants, l'état, JSX, etc.

Pour cette raison, j'ai inclus dans les modèles de base que ESLint corrige automatiquement les interfaces en types.

Si vous voulez approfondir les différences, vous pouvez lire [cet article dans le Handbook TS](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces), mais de nos jours, la plupart des fonctionnalités présentes dans une interface sont également dans un type, et vice versa. 

### Manipulation du DOM dans TypeScript

Dans React, nous n'utiliserons pas (directement) beaucoup de manipulation du DOM. Mais je pense qu'il est utile de savoir comment cela fonctionne.

#### Comment récupérer des éléments du DOM

```ts
// HTMLFormElement | null
const form = document.querySelector("form");

// HTMLElement | null
const otherForm = document.getElementById("myFancyForm");

// HTMLSelectElement
const select = document.createElement("select"); 
```

Lorsque nous effectuons `document.querySelector("form")`, notre constante `form` est inférée avec le type `HTMLFormElement` ou `null`. Mais dans le deuxième exemple, nous obtenons un formulaire via son ID. TS ne sait pas quel élément HTML exact il s'agit, donc il donne un type plus générique `HTMLElement`.

```ts
const form = document.querySelector("form");

form.addEventListener("submit", (e: Event) => {
  e.preventDefault();
  console.log(e);
}); // Erreur
```

TS ne sait pas s'il trouvera quelque chose dans le HTML concernant le sélecteur de requête, donc il ne peut pas assigner la fonction `addEventListener` à un type possible null. Vous pouvez corriger cela de trois manières.

Je vous promets que vous trouverez cet élément :

```ts
// HTMLFormElement
const form = document.querySelector("form")!; 
```

Avec `!`, vous dites à TS de ne pas s'inquiéter, il le trouvera, et il ne peut pas être `null`.

Faites-le seulement s'il n'est pas null :

```ts
const form = document.querySelector("form");

form?.addEventListener("submit", (e: Event) => {
  e.preventDefault();
  console.log(e);
});
```

Vous avez peut-être déjà vu `?` de l'opérateur [JS Optional Chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

C'est le moment du transtypage :

```ts
const otherForm = document.getElementById("myFancyForm") as HTMLFormElement;

otherForm.addEventListener("submit", (e: Event) => {
  e.preventDefault();
  console.log(e);
});
```

Vous dites à TS quel type il obtiendra lorsqu'il trouvera cet élément. Avec cela, vous vous assurez qu'il sera `HTMLFormElement` et non `null`.


## Comment combiner React + TypeScript

Commençons avec la deuxième section de cet article. Rappelez-vous, la première section concernait pourquoi utiliser TypeScript en général, comment l'utiliser et un aperçu du langage. 

Dans cette deuxième section, vous pouvez examiner de plus près comment utiliser TypeScript dans React et comment résoudre les différents défis que vous rencontrerez en essayant de développer une application avec React et TypeScript.

### Installation

#### Create React App

Pour les utilisateurs de [CRA](https://create-react-app.dev), vous devez simplement spécifier le modèle :

```bash
npx create-react-app my-awesome-project --template typescript
```

#### Vite

Créer un projet TypeScript avec [Vite](https://vitejs.dev) est aussi simple que d'utiliser l'interface de ligne de commande et de choisir le modèle TypeScript.

```bash
npm create vite@latest my-awesome-project
```

#### Ajouter à un projet existant

Si vous souhaitez ajouter TypeScript à un projet qui est en JavaScript, ajoutez simplement TypeScript comme dépendance de développement.

```bash
npm install -D typescript
```

Je dois vous avertir que si c'est votre première rencontre avec TypeScript, je ne vous recommande pas de l'essayer sur un projet que vous avez déjà construit. Cela est dû au fait que votre expérience sera de penser constamment que vous avez quelque chose qui fonctionne et que tout cela n'est que plus de travail pour rien. Mais cela ne pourrait pas être plus éloigné des véritables avantages de TypeScript.

### Typage des props des composants

Le premier et le scénario le plus courant lors de l'utilisation de TypeScript dans un projet React est d'écrire les props pour un composant.

Pour écrire correctement les props des composants, vous devez spécifier quelles propriétés vous acceptez sur le composant, le type et si c'est requis ou non. 

```ts
// src/components/AnimeDetail/Cover/index.tsx

type CoverProps = {
  url: string
}

export default function Cover({ url }: CoverProps) {
  // ...
}
```

Nous utilisons uniquement une prop `url` qui est une `string` et est une prop obligatoire.

Un autre exemple avec plus de props et des optionnels :

```ts
// src/components/AnimeDetail/StreamingList/PlatformLink/index.tsx

type PlatformLinkProps = {
  name: string
  url?: string
}

export default function PlatformLink({ name, url }: PlatformLinkProps) {
  // ...
}
```

Avec `?`, nous indiquons qu'il s'agit d'un paramètre optionnel, donc TypeScript sait que le type de `url` dans ce cas sera `string` ou `undefined`. De plus, les consommateurs de ce composant n'obtiendront pas d'erreur s'ils ne passent pas de prop `url` au composant.

Examinons un dernier exemple, plus complexe :

```ts
// src/components/AnimeDetail/Detail/index.tsx

type AnimeType = 'TV' | 'Movie'

type DetailProps = {
  liked: boolean
  toggleFav: () => void
  title: string
  type: AnimeType
  episodeCount: number
  score: number
  status: string
  year: number
  votes: number
}

export default function Detail({
  liked,
  toggleFav,
  title,
  type,
  episodeCount,
  score,
  status,
  year,
  votes,
}: DetailProps) {
  // ...
}
```

Cette fois, vous pouvez voir une myriade de types, y compris une `fonction` et un type personnalisé `AnimeType`.

Donc, pour résumer, écrire des props est utile pour :

- Validation réelle du type de prop du côté du consommateur.
  - Plus de devinettes sur ce dont un composant a besoin.
  - Plus d'ouverture du code source d'un composant pour vérifier ce qu'il fait avec les données.
- Auto-complétion et documentation
  - Connaître directement du côté du consommateur les props et valeurs nécessaires via l'auto-complétion sans connaître à l'avance.

![autocomplete](https://blog.dastasoft.com/_next/image?url=%2Fassets%2Fposts%2Fcontent%2Ftypescript2%2Fautocomplete.webp&w=1920&q=75)

Bien sûr, cela brillera absolument sur des composants complexes et des composants tiers qui proviennent de bibliothèques fantaisistes que vous utilisez dans votre projet.

#### Types intégrés de React

Avec React et de nombreuses bibliothèques, vous trouverez des tonnes de types pré-construits pour faciliter votre expérience en tant que développeur. Par exemple, dans React, il est assez courant d'avoir le composant suivant :

```ts
// src/components/Layout/index.tsx

type LayoutProps = {
  children: React.ReactNode
}

export default function Layout({ children }: LayoutProps) {
  // ...
}
```

Un composant React personnalisé qui reçoit d'autres éléments en tant qu'enfants. Pour ces cas, vous définirez `children` comme un type `ReactNode`.

##### Un avertissement concernant React.FC && React.FunctionComponent

Vous pouvez trouver du code avec cette syntaxe pour déclarer les props des composants :

```ts
type PlatformLinkProps = {
  name: string
  url?: string
}

const PlatformLink: React.FC<PlatformLinkProps> = ({ name, url }) => {
  // ...
}
```

Ce code fonctionne en utilisant `React.FC`, ou sa version plus longue `React.FunctionComponent`. Mais vous devez savoir qu'il a quelques inconvénients et c'est pourquoi nous ne l'utilisons pas dans cet article :

- Vous devez utiliser une expression de fonction et vous ne pouvez pas utiliser une déclaration de fonction. C'est un point mineur, mais j'ai construit tous les composants avec une déclaration de fonction exprès.
- Vous ne pouvez pas utiliser de génériques (nous verrons cela plus tard).
- Dans le passé, cela faisait que vos props acceptaient indirectement la propriété `children` et dans ce composant, vous ne l'utilisez pas. Cela était vrai jusqu'à React 18, de nos jours cela ne s'applique plus.

#### Type de retour d'un composant React

Dernière pièce du puzzle, que retourne un composant ? Vous pouvez utiliser les types intégrés de React `React.ReactElement`, `React.ReactNode` et `JSX.Element` :

```ts
export default function Favorites(): JSX.Element {
  // ...
}
```

Pour résumer la réponse de cette section : **laissez TypeScript inférer automatiquement le type de retour**. Si vous avez besoin d'une liste détaillée des différences entre ces 3 types, je vous suggère de [jeter un coup d'œil à ce post SO](https://stackoverflow.com/questions/58123398/when-to-use-jsx-element-vs-reactnode-vs-reactelement)


#### Combinations avec les littéraux de gabarit

Dans [AnimeTrailers](https://animetrailers.dastasoft.com/), j'ai inclus une simple interface utilisateur personnalisée qui sera utile pour démontrer des cas comme celui-ci. Vous pouvez vérifier les différents composants simples dans `src/components/UI`, mais la plupart d'entre eux seront expliqués à travers ce guide.

Jetons un coup d'œil au composant personnalisé `Position` :

```ts
// src/components/UI/Position/index.tsx

import React from 'react'

import { StyledPosition } from './StyledPosition'

type VPosition = 'top' | 'bottom'
type HPositon = 'left' | 'right'

export type PositionValues = `${VPosition}-${HPositon}`

type PositionProps = {
  children: React.ReactNode
  position?: PositionValues
}

export default function Position({
  children,
  position = 'top-right',
}: PositionProps) {
  return <StyledPosition position={position}>{children}</StyledPosition>
}
```

Position est un composant simple à utiliser avec tout autre composant avec une position absolue et le placer sur l'un des quatre bords avec `top-left`, `top-right`, `bottom-left` et `bottom-right`.

Créer un nouveau type avec des littéraux de gabarit n'est pas un secret si vous l'utilisez déjà en JavaScript. Le truc astucieux ici est lorsque vous combinez des littéraux de gabarit `${VPosition}-${HPositon}` avec des types d'union `top` | `bottom` comme dans l'exemple ci-dessus, TypeScript générera toutes les combinaisons possibles des deux. Cela nous permet de générer les quatre valeurs différentes dont nous avons besoin.


#### Comment utiliser `Exclude`

Prenons l'exemple précédent et ajoutons plus de valeurs à l'union :

```ts
type VPosition = 'top' | 'middle' | 'bottom'
type HPositon = 'left' | 'center' | 'right'

export type PositionValues = `${VPosition}-${HPositon}`
```

Ce littéral de gabarit générera toutes les combinaisons possibles des unions, donc nous aurons `"top-left" | "top-center" | "top-right" | "top-left" | "center-left" | "center-right" | "bottom-left" | "bottom-center" | "bottom-right"`. 

Il y a un cas qui est un peu étrange, `middle-center`. Dans ce cas, vous voulez peut-être simplement mettre `center`, auquel cas `Exclude` est très utile.

```ts
type PositionValues =
  | Exclude<`${VPosition}-${HPositon}`, 'middle-center'>
  | 'center'
```

Maintenant, `PositionValues` générera `"center" | "top-left" | "top-center" | "top-right" | "middle-left" | "middle-right" | "bottom-left" | "bottom-center" | "bottom-right"`. 

Avec exclude, vous pouvez supprimer le `middle-center` et ajouter `center` ensuite avec une union.

#### Composants HTML personnalisés

Si vous souhaitez créer un composant qui se comporte comme un `input` mais que vous ne souhaitez pas écrire chaque propriété et fonction de l'input HTML, vous pouvez y parvenir avec :

```ts
// src/components/UI/Input/index.tsx

import React from 'react'

import styles from './StyledInput.module.css'

type InputProps = React.ComponentProps<'input'>

const Input = React.forwardRef(
  (props: InputProps, ref: React.Ref<HTMLInputElement>) => {
    return <input {...props} className={styles.StyledInput} ref={ref} />
  }
)

export default Input
```

Avec `React.ComponentProps`, vous pouvez spécifier sur quel élément vous basez votre nouveau type et obtenir tout ce qu'un vrai input HTML a pour créer un composant UI personnalisé. Mais que se passe-t-il lorsque vous souhaitez remplacer certaines de ces propriétés ou interdire leur utilisation ?

##### Omit

Jetons un coup d'œil au composant UI `Tag` :

```ts
// src/components/UI/Tag/index.tsx

import React from 'react'

import { StyledTag } from './StyledTag' // aka un span stylisé

type TagProps = {
  variant?: 'solid' | 'outlined'
  text: string
} & Omit<React.ComponentProps<'span'>, 'children'>

export default function Tag({ text, variant = 'solid' }: TagProps) {
  return <StyledTag variant={variant}>{text}</StyledTag>
}
```

Dans ce cas, ce composant passe explicitement un `text` à afficher en tant que `children` du composant. Vous ne voulez peut-être pas que les consommateurs de ce composant utilisent le `children` original, donc vous pouvez omettre cette propriété de la collection donnée par `React.ComponentProps`.

### Typage des Hooks

Maintenant, plongeons dans la manière d'écrire chacun des hooks les plus couramment utilisés dans React.

#### Hook useState

Dans la plupart des cas, le typage de `useState` ne nécessitera rien de votre part, car TypeScript essaiera d'inférer le type. Dans d'autres scénarios, par exemple lorsque la valeur initiale est différente des valeurs futures, vous devez le spécifier directement.

```ts
// src/pages/Search.tsx

export default function Search() {
  const [animeList, setAnimeList] = useState<Anime[] | null>(null)
  const [page, setPage] = useState(1)
  // const [page, setPage] = useState<number>(1)
  // ...
}
```

À partir de l'état `page`, le type est inféré comme un nombre basé sur la valeur initiale fournie. Il sera exactement le même que la version commentée. De plus, les setters d'état sont automatiquement typés comme `React.Dispatch<React.SetStateAction<number>>` avec `number` remplacé par le type inféré/spécifié.

D'autre part, `animeList` sans aucun type explicite serait seulement `null`. Cela est vrai avant que le composant n'obtienne les données nécessaires, mais contiendra éventuellement une collection de types `Anime` pour lesquels vous devez explicitement définir le type avec une union des deux types possibles.

Au-delà de la définition du type à null pour les états de contrôle initiaux dans useState, il existe d'autres solutions similaires, telles que :

```ts
export default function Search() {
  // const [animeList, setAnimeList] = useState<Anime[] | null>(null)
  const [animeList, setAnimeList] = useState<Anime[]>([])
  const [anime, setAnime] = useState<Anime>({} as Anime)
  // ...
}
```

Il est important de regarder de plus près la ligne `anime, setAnime`. Dans ce cas, cela fonctionne car ce n'est pas une collection, mais plutôt un seul élément.

La principale différence avec ces solutions supplémentaires est que vous n'êtes pas 100% honnête avec le compilateur. Vous supposez que vous aurez une valeur avec cette forme, et cela comporte un risque implicite.


```ts
export default function Search() {
  const [anime, setAnime] = useState<Anime>({} as Anime)
  // ...

  return <div>{anime.coverURL}</div>
}
```

Si vous ne fournissez pas une valeur correcte avec cette option, cela peut exploser à l'exécution.

##### Comment passer l'état en tant que props

Très souvent, vous devrez peut-être passer l'état vers le bas dans la hiérarchie et déléguer à un enfant lorsqu'un état est lu ou défini. Vous devrez écrire les props pour ce composant en gardant à l'esprit les types d'état.

```ts
type FancyComponentProps = {
  anime: Anime,
  setAnime: React.Dispatch<React.SetStateAction<Anime>>
}

const FancyComponent = ({anime, setAnime}: FancyComponentProps) => {
  // ...
}
```

Il est préférable de comprendre quels types vous devez passer. Mais si vous avez des difficultés avec cela, vous pouvez vérifier les variables d'état actuelles et l'IDE vous dira ce que vous devez passer.

![type intellisense](https://blog.dastasoft.com/_next/image?url=%2Fassets%2Fposts%2Fcontent%2Ftypescript2%2Ftype-intellisense.webp&w=1920&q=75)

#### Hook useReducer

À ce stade, vous avez principalement tous les outils pour définir correctement les types pour `useReducer`.

Pour l'exemple suivant, je l'ai simplifié ici et nous couvrirons le code réel dans la section Génériques.

```ts
// src/hooks/useFetch.ts

const enum ACTIONS {
  LOADING,
  FETCHED,
  ERROR,
}

type State = {
  data?: Anime[]
  loading: boolean
  error?: Error
}

type Action =
  | { type: ACTIONS.LOADING }
  | { type: ACTIONS.FETCHED; payload: Anime }
  | { type: ACTIONS.ERROR; payload: Error }

const initialState: State = {
  loading: true,
  error: undefined,
  data: undefined,
}

const fetchReducer = (state: State, action: Action): State => {
    switch (action.type) {
      case ACTIONS.LOADING:
        return { ...initialState }
      case ACTIONS.FETCHED:
        return { ...initialState, data: action.payload, loading: false }
      case ACTIONS.ERROR:
        return { ...initialState, error: action.payload, loading: false }
      default:
        return state
    }
  }

const [state, dispatch] = useReducer(fetchReducer, initialState)
```

Comme toujours, vous obtenez un `status` et un `dispatch` de `useReducer` lorsque vous fournissez une `fonction de réducteur` et un `état initial`. Vous n'avez rien à faire dans le useReducer lui-même, mais vous devez écrire le `state` et les `actions` car cela définira comment l'état et le dispatch se comporteront.

##### initialState

Pour l'`état initial`, vous pouvez simplifier le processus. Au lieu de créer un type `State`, vous pouvez utiliser `typeof initialState` chaque fois que vous devez définir un type basé sur l'état initial.

```ts
const initialState: State = {
  loading: true,
  error: undefined,
  data: undefined,
}

const fetchReducer = (state: typeof initialState, action: Action) => {
  // ...
}
```

L'inconvénient de cette version est qu'elle ne contrôle pas les valeurs futures de `data` et `error`. Cela peut fonctionner lorsque le type est toujours le même, mais ce n'est pas le cas ici, donc vous pouvez utiliser un type `State` personnalisé pour cela.

##### Actions

Vous devez spécifier quelles actions le réducteur sera capable de gérer, et vous le faites avec des unions. La partie enum est entièrement facultative, mais elle aide à être moins sujette aux erreurs que d'écrire des chaînes à plusieurs endroits.

##### fonction de réducteur

Vous devez seulement spécifier les types des paramètres passés à la fonction, qui sont en fait ceux que vous avez créés dans les étapes précédentes.

##### Passage en tant que props

Encore une fois, si vous voulez passer quelque chose de useReducer en tant que prop, vous devrez écrire les props du consommateur en conséquence.

- `state` sera le type que vous avez défini dans votre `initialState` et/ou un type `State` personnalisé comme dans l'exemple ci-dessus.
- `dispatch` sera `React.Dispatch<Action>` où `Action` est le type personnalisé pour les actions.

#### useContext

Le contexte dans le projet exemple est utilisé pour gérer une liste d'anime que vous aimez et basculer l'état à différents points de l'application. À ce stade, `useContext` ne devrait pas vous poser de problème car il s'agit simplement d'une combinaison de ce que vous avez vu jusqu'à présent – mais regardons un exemple :

```ts
// src/context/FavContext.tsx

type FavContextType = {
  favList: Favorite[]
  // setFavList: React.Dispatch<React.SetStateAction<Favorite[]>>
  toggleFav: (id: number, favorite: Favorite) => void
}

export const FavContext = createContext({} as FavContextType)

export const FavContextProvider = ({ children }: FavContextProviderProps) => {
  const [favList, setFavList] = useState<Favorite[]>([])

  const toggleFav = (id: number, favorite: Favorite) => { /* ... */ }

  // ...

  return (
    <FavContext.Provider value={{ favList, toggleFav }}>
      {children}
    </FavContext.Provider>
  )
}
```

`useContext` suit les mêmes règles que `useState` pour le typage. Dans ce cas, la valeur initiale sera nulle, mais nous trompons TypeScript avec `as` sur `createContext` et définissons un objet qui contiendra un tableau de `favourite animes` et une fonction pour basculer.

Commenté, vous avez le scénario de setter typique au cas où vous en auriez besoin.

Pour le reste du code, vous avez déjà appris `useState` dans la section précédente, donc rien de nouveau. Avec le type `Favorite`, useState déterminera les types nécessaires et ces types seront disponibles directement du côté du consommateur.

```ts
// src/components/AnimeDetail/index.tsx

const { favList, toggleFav } = useContext(FavContext)
```

#### Hook useRef

Vous pouvez utiliser `useRef` de deux manières différentes, donc le typage sera légèrement différent dans chaque cas.

##### Références DOM

L'une des utilisations de `useRef` est de conserver une référence à un élément DOM. 

Dans le projet exemple, vous trouverez cela pour le défilement infini en conservant une référence à un observable du dernier élément de la liste d'anime. Cela vous permet de savoir quand l'utilisateur visualise cet élément dans la fenêtre et de déclencher une nouvelle récupération.

Regardons un exemple plus court de useRef pour la référence DOM, mais vous pouvez [vérifier la version complète de useRef + observer](https://github.com/dastasoft/animetrailers/blob/main/src/components/AnimeList/index.tsx) :

```ts
  const myDomReference = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if(myDomReference.current) myDomReference.current.focus()
  }, [])
```

Un cas typique pourrait être lorsqu'une page se charge et que vous voulez un focus automatique sur une entrée. Il suffit de spécifier le type de l'élément DOM référencé, dans ce cas `HTMLInputElement`.

Quelques considérations sur le code ci-dessus :

- Le hook retournera une propriété `current` en lecture seule.
- Vous n'avez pas besoin d'écrire manuellement `current`. React le gérera via `React.RefObject<HTMLInputElement>` dans ce cas.
- Si l'élément DOM est toujours présent, vous pouvez définir la valeur initiale à `null!` et éviter la vérification if.

##### Références mutables

La deuxième utilisation de `useRef` est lorsque vous souhaitez conserver des valeurs mutables entre les rendus. Par exemple, dans les cas où vous avez besoin d'une variable unique pour chaque instance d'un composant qui survit entre les rendus et ne déclenche pas de re-rendu.

```ts
const isFirstRun = useRef(true)

useEffect(() => {
  if(isFirstRun) {
    // ...
    isFirstRun.current = false
  }
}, [])
```

Quelques considérations que vous remarquerez par rapport à l'exemple précédent : 

- Vous pouvez maintenant muter la valeur à l'intérieur de `current`.
- React fournit `React.MutableRefObject<boolean>` qui est maintenant un `MutableRefObject` au lieu de `RefObject`.

### Transmission de ref

Si à un moment donné vous devez passer une référence à un élément HTML comme dans la section `useRef`, l'écriture des props pour ce composant sera légèrement différente :


```ts
// src/components/AnimeGrid/Card/index.tsx

const Card = React.forwardRef(
(
  { id, coverURL, title, status, score, type, year }: CardProps,
  ref: React.Ref<HTMLImageElement>
) => {
  // ...
})
```

Pour passer la référence, vous devrez envelopper votre composant avec `React.forwardRef`. Cela injectera, avec les props régulières du composant, la `ref` (qui sera n'importe quel élément HTML enveloppé dans le type `React.Ref`).

Dans ce cas, nous connaissons le type de l'élément HTML que nous transmettons, mais si ce n'est pas votre cas, ce pourrait être un bon moment pour utiliser les génériques.

### Comment utiliser les génériques TypeScript dans React

Imaginons que nous voulons créer un composant UI personnalisé en enveloppant des éléments HTML existants mais en lui donnant un ensemble de propriétés personnalisées comme le font la plupart des bibliothèques de composants.

La plupart de ces bibliothèques offrent également la flexibilité de décider quel élément HTML est finalement rendu avec une propriété `as` – et c'est exactement le cas pour le composant UI `Text`. 

Ce composant UI Text est utilisé pour afficher n'importe quel texte avec un ensemble de tailles et de couleurs. De plus, nous voulons permettre à l'utilisateur de choisir n'importe quel élément HTML dont il a besoin, sans se restreindre à un seul `p` ou `span`.

Dans ce scénario, vous ne savez pas à l'avance quel élément le consommateur passera à votre composant, vous devez donc utiliser des génériques pour inférer le type à celui qu'ils passent. 

Ainsi, les types de props pour le composant seront :

```ts
// src/components/UI/Text/index.tsx

type TextOwnProps<T extends React.ElementType> = {
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl'
  variant?: 'base' | 'primary' | 'secondary'
  as?: T | 'div'
}

type TextProps<T extends React.ElementType> = TextOwnProps<T> &
  React.ComponentPropsWithoutRef<T>

export default function Text<T extends React.ElementType = 'div'>({
  size = 'md',
  variant = 'base',
  children,
  as = 'div',
}: TextProps<T>) {
  // ...
}
```

Examinons en détail ce qui se passe dans l'exemple ci-dessus :

- Nous utilisons `T` pour les génériques ici, mais vous pouvez utiliser n'importe quel nom que vous voulez.
- T étend `React.ElementType` qui est le type le plus générique pour les éléments HTML. Donc nous savons que tout ce qui est passé au composant est basé sur un élément HTML plutôt que sur une union de tous les éléments HTML possibles typés manuellement.
- Le deuxième type `TextProps` est utilisé pour deux choses :
  - Nous avons besoin de propriétés supplémentaires en fonction du type d'élément HTML. Lorsque qu'un consommateur utilise le composant Text comme un `label`, nous voulons vérifier et suggérer différentes propriétés que lorsqu'il s'agit d'un `span`. Pour cela, nous devons utiliser `React.ComponentProps`. Dans ce cas, nous n'avons pas besoin de références, donc nous utilisons explicitement le type `ComponentPropsWithoutRef`.
  - `React.ComponentProps` fournit également la prop `children`, donc vous n'avez pas besoin de l'inclure dans `TextOwnProps`.
  - Il n'est pas nécessaire de gérer `Omit` ou d'autres techniques d'exclusion car `children` n'est pas modifié ou écrasé par une prop `TextOwnProps`.

Avec cet exemple, nous avons un composant très flexible qui est correctement typé et offre une bonne expérience de développement.

Dans le projet exemple, vous pouvez examiner les différents composants UI personnalisés pour vérifier l'implémentation suivant ce même modèle.


### Typage d'un Hook useFetch personnalisé

Dans le projet exemple, j'ai inclus un hook simple pour obtenir les données et utiliser `localStorage` comme cache temporaire afin de ne pas dépasser la limite de l'API. Ce n'est pas grand-chose, mais je pense que c'est un exemple complet de tout ce qui est expliqué dans cet article.

Jetons un coup d'œil à certaines parties de ce hook – mais je vous encourage à regarder [le fichier réel](https://github.com/dastasoft/animetrailers/blob/main/src/hooks/useFetch.ts) et à essayer de tout comprendre avec les différentes sections expliquées dans cet article.

```ts
// src/hooks/useFetch.ts

type State<T> = {
  data?: T
  loading: boolean
  error?: Error
}

function useFetch<T = unknown>(
  url?: string,
  { initialFetch, delayFetch }: Options = { initialFetch: true, delayFetch: 0 }
): State<T> {
// ...
}
```

- Le hook reçoit un type générique dont vous ne pouvez pas savoir à l'avance quel type de données il gérera.
- Le hook accepte `url` où effectuer la récupération et des options pour décider si le hook effectue une récupération initiale et s'il y a un délai entre les récupérations.
- L'objet `options` a des valeurs par défaut si rien n'est fourni.
- Le hook retourne un `State` du type spécifié par le consommateur via les génériques.
- Le type de statut définit que, facultativement, une donnée du type fourni par le consommateur, un indicateur de chargement ou une erreur est retournée si quelque chose ne va pas.

Vérifions l'utilisation côté consommateur :

```ts
// src/pages/AnimeDetail.tsx

const { data, loading, error } = useFetch<JikanAPIResponse<RawAnimeData>>(
    getAnimeFullById(Number(id))
  )
```

- `getAnimeFullById` retourne l'URL de cet endpoint.
- `useFetch` dans ce cas retournera une `data` de type `JikanAPIResponse` qui a également différentes possibilités, dans ce cas `RawAnimeData`.


## Conclusion

Tout au long de cet article, vous avez vu les points de douleur les plus courants que l'utilisation de TypeScript peut aider à résoudre. Il est particulièrement utile lorsque vous travaillez avec d'autres personnes pour que vous compreniez parfaitement les tenants et aboutissants de chaque composant, hook et contexte que vous devez utiliser. 

Utiliser TypeScript signifie investir dans un code plus fiable, mieux documenté et plus lisible. Il est également moins sujet aux erreurs et plus maintenable.

Coder ne consiste pas seulement à créer un algorithme efficace. Vous allez travailler avec d'autres personnes (même si vous travaillez en tant que développeur solo, à un moment donné vous publierez peut-être votre travail, chercherez une collaboration ou de l'aide). Dans ces scénarios, une bonne communication entre les membres est essentielle.

J'aime penser à TypeScript comme le Babel pour les humains : vous pouvez optimiser votre code pour le CPU avec Babel, mais vous avez besoin de quelque chose pour mettre à l'échelle et guider les autres autour de vos idées et vice versa.

Une seule question reste, **quand devez-vous utiliser TypeScript** ?

- Si vous travaillez avec plus de personnes ou prévoyez de publier votre code, il y a des chances que vous souhaitiez que le code soit aussi lisible et représentatif de vos idées que possible.
- Si vous travaillez sur un grand projet.

Chaque grand projet commence comme un petit projet, alors soyez prudent avec cette déclaration sur l'utilisation de TypeScript uniquement sur des projets "grands".

Cela a été un long article sans aucun doute. Si vous avez atteint ce point, je dois vraiment vous remercier pour votre effort et votre passion. Mon idée initiale n'était pas si large, mais je voulais expliquer les pourquoi et les comment. 

J'espère que vous apprécierez cet article. Si vous êtes déjà passé de JS à TS, utilisez les deux, envisagez de le faire, avez pensé à un moment donné mais n'avez pas aimé ou toute autre situation – **j'aimerais lire votre expérience**.