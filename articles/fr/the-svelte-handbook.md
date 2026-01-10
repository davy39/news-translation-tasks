---
title: Le Guide Svelte – Apprendre Svelte pour les Débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2019-10-22T11:37:47.000Z'
originalURL: https://freecodecamp.org/news/the-svelte-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/Screen-Shot-2019-10-21-at-18.39.28.png
tags:
- name: frontend
  slug: frontend
- name: handbook
  slug: handbook
- name: General Programming
  slug: programming
- name: Svelte
  slug: svelte
seo_title: Le Guide Svelte – Apprendre Svelte pour les Débutants
seo_desc: 'I wrote this book to help you quickly learn Svelte and get familiar with
  how it works.

  The ideal reader of the book has zero knowledge of Svelte, has maybe used Vue or
  React, but is looking for something more, or a new approach to things.

  Svelte is v...'
---

J'ai écrit ce livre pour vous aider à apprendre rapidement Svelte et à vous familiariser avec son fonctionnement.

Le lecteur idéal de ce livre n'a aucune connaissance de Svelte, a peut-être utilisé Vue ou React, mais cherche _quelque chose_ de _plus_, ou une nouvelle approche des choses.

Svelte vaut vraiment la peine d'être exploré, car il offre un point de vue rafraîchissant et plusieurs fonctionnalités uniques pour le Web.

Merci d'avoir obtenu cet ebook. J'espère qu'il vous aidera à en apprendre davantage sur Svelte !

Vous pouvez me joindre sur Twitter [@flaviocopes](https://twitter.com/flaviocopes). Mon site web est [flaviocopes.com](https://flaviocopes.com/).

## Table des Matières

* [Introduction à Svelte](#heading-introduction-a-svelte)
* [Composants Svelte](#heading-composants-svelte)
* [Gestion de l'État dans Svelte](#heading-gestion-de-letat-dans-svelte)
* [Réactivité Svelte](#heading-reactivite-svelte)
* [Props Svelte](#heading-props-svelte)
* [Gestion de l'État entre Composants](#heading-gestion-de-letat-entre-composants-dans-svelte)
* [Slots](#heading-slots)
* [Événements du Cycle de Vie Svelte](#heading-evenements-du-cycle-de-vie-svelte)
* [Bindings Svelte](#heading-bindings-svelte)
* [Logique Conditionnelle dans les Templates](#heading-logique-conditionnelle-dans-les-templates)
* [Boucles dans les Templates Svelte](#heading-boucles-dans-les-templates-svelte)
* [Promesses dans les Templates Svelte](#heading-promesses-dans-les-templates-svelte)
* [Travailler avec les Événements dans Svelte](#heading-travailler-avec-les-evenements-dans-svelte)
* [Où Aller à partir d'Ici](#heading-ou-aller-a-partir-dici)

## Introduction à Svelte

Svelte est un framework frontend web passionnant que vous pouvez utiliser pour construire des applications web.

Si vous débutez, Svelte est un excellent choix comme premier framework frontend.

Si vous avez déjà de l'expérience avec React, Vue.js, Angular ou un autre framework frontend, vous serez agréablement surpris par Svelte.

Comparé à React, Vue, Angular et autres frameworks, une application construite avec Svelte est **compilée** au préalable, donc vous n'avez pas à servir l'ensemble du framework à chacun de vos visiteurs.

En conséquence, l'expérience est plus fluide, consomme moins de bande passante, et tout semble plus rapide et plus léger.

Au déploiement, Svelte disparaît et tout ce que vous obtenez est du JavaScript simple (et rapide !).

Ce n'est que la partie émergée de l'iceberg. Plongeons-nous dedans !

[Vous pouvez obtenir une version PDF et ePub de ce Guide Svelte](https://thevalleyofcode.com/download/svelte/)

### Comment commencer avec Svelte

Pour utiliser Svelte, vous devez avoir Node.js installé car tous les outils que nous allons utiliser sont basés sur Node.

> Assurez-vous de consulter également mon [Guide Node.js](https://thevalleyofcode.com/node/)

Un petit conseil que j'ai est que le site web de Svelte fournit un "playground" très pratique pour tester Svelte à l'adresse [https://svelte.dev/repl](https://svelte.dev/repl).

C'est assez pratique pour tester de petites applications Svelte et expérimenter des choses.

Avec le terminal, allez dans le dossier où vous gardez habituellement votre code, par exemple le dossier `dev` dans votre répertoire personnel.

Exécutez cette commande sur votre ordinateur :

```sh
npm create vite@latest helloworld -- --template svelte

```

Cela configure tout ce dont vous avez besoin pour commencer avec votre première application Svelte. Je l'ai appelé `helloworld` donc vous verrez un dossier avec ce nom.

Allez dans ce dossier avec `cd helloworld` puis exécutez

```sh
npm install

```

et lorsque cela se termine :

```sh
npm run dev

```

Cela exécute notre nouveau site Svelte en mode développement, démarrant l'application sur localhost sur le port 5173 :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-07-20-at-20.01.29.png)

Si vous pointez votre navigateur là-bas, vous verrez le projet d'exemple s'afficher :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-07-20-at-20.04.08.png)

Vous êtes maintenant prêt à ouvrir le code dans votre éditeur préféré, par exemple **VS Code**.

Vous pouvez le faire en exécutant `code .` dans le dossier, si vous avez installé [L'interface de ligne de commande de Visual Studio Code](https://code.visualstudio.com/docs/editor/command-line).

Dès que vous ouvrez le projet dans l'éditeur, VS Code vous demandera d'installer l'extension [Svelte pour VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode) (si ce n'est pas le cas, allez dans le panneau des extensions et recherchez-la) :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-07-20-at-20.09.04.png)

Installez-la, car elle fournit le surligneur de syntaxe et d'autres fonctionnalités :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screen-Shot-2022-07-20-at-20.10.11.png)

Maintenant, revenons au projet !

Ouvrez le dossier `src`, vous y verrez quelques fichiers. Le principal, sans jeu de mots, est `main.js`, où l'application Svelte est configurée :

Ce fichier est le point d'entrée et initialise le composant principal App, qui est défini dans `App.svelte` :

```html
<script>
  import svelteLogo from './assets/svelte.svg'
  import Counter from './lib/Counter.svelte'
</script>

<main>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank">
      <img src="{svelteLogo}" class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Vite + Svelte</h1>

  <div class="card">
    <Counter />
  </div>

  <p>
    Consultez
    <a href="https://github.com/sveltejs/kit#readme" target="_blank"
      >SvelteKit</a
    >, le framework officiel d'applications Svelte alimenté par Vite !
  </p>

  <p class="read-the-docs">Cliquez sur les logos Vite et Svelte pour en savoir plus</p>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style>

```

Voyez, nous avons 3 sections principales :

```html
<script></script>

<main></main>

<style></style>

```

C'est ce que nous appelons un **composant à fichier unique**, un seul fichier qui détermine tout ce qui concerne notre composant :

* le balisage (le HTML)
* le comportement (le JavaScript)
* le style (le CSS)

Cette structure sera la base de tous vos composants Svelte.

## Composants Svelte

Le développement Web moderne est très axé sur les composants, et Svelte ne fait pas exception.

Qu'est-ce qu'un composant ? Un composant est une partie atomique de l'application qui est autonome et fait éventuellement référence à d'autres composants pour composer son rendu.

En d'autres termes, c'est une partie atomique de l'application.

Un formulaire peut être un composant.

Un élément d'entrée peut être un composant.

L'ensemble de l'application est un composant.

Les composants Svelte contiennent tout ce qui est nécessaire pour rendre une partie de l'UI.

Chaque composant Svelte est déclaré dans un fichier `.svelte`, et vous y trouverez le contenu (balisage), le comportement (JavaScript) et la présentation (CSS) sans avoir à définir des fichiers séparés.

Ce qui est une bonne façon de définir une partie de l'UI car vous n'avez pas besoin de chercher les éléments qui affectent le même élément dans divers fichiers.

Voici un exemple de composant, que nous stockerons dans un fichier appelé `Dog.svelte` :

```html
<script>
  export let name
</script>

<style>
  h1 {
    color: purple;
  }
</style>

<h1>The dog name is {name}!</h1>

```

Le code JavaScript doit être placé dans la balise `script`.

Le CSS que vous avez dans la balise `style` est **limité** au composant et ne "fuit" pas à l'extérieur.

Si un autre composant a une balise `h1`, ce style n'affectera pas cela.

C'est très pratique lorsque vous réutilisez des composants que vous avez déjà écrits pour d'autres applications, par exemple, ou lorsque vous incluez des bibliothèques Open Source publiées par d'autres personnes.

Par exemple, vous pouvez inclure un composant de sélection de date construit par quelqu'un d'autre et aucun des styles du composant n'affectera le reste de l'application.

Et de la même manière, aucun du CSS que vous avez écrit ne modifiera l'apparence du sélecteur de date.

### Importer le composant dans d'autres composants

Un composant peut être utilisé par d'autres composants.

D'autres composants peuvent maintenant importer le composant `Dog` que nous avons écrit dans leur code.

Par exemple, voici un composant `House` :

```html
<script>
  import Dog from './Dog.svelte'
</script>

```

Vous pouvez maintenant importer et utiliser le composant Dog, comme s'il s'agissait d'une balise HTML :

```html
<script>
  import Dog from './Dog.svelte'
</script>

<Dog />

```

### Exporter des fonctions spécifiques d'un composant

Comme vous l'avez vu ci-dessus, pour exporter le composant, nous n'avons rien eu à faire, car le composant lui-même est l'**exportation par défaut**.

Que faire si vous souhaitez exporter autre chose que le balisage du composant et ses fonctionnalités associées et intégrées ?

Vous devez écrire toutes les fonctions que vous souhaitez exporter à partir d'une balise `script` spéciale avec l'attribut `context="module"`.

Voici un exemple. Supposons que vous avez un composant Button dans `Button.svelte` :

```html
<button>A button</button>

```

et vous souhaitez donner à d'autres composants la possibilité de changer la couleur du bouton.

> Une meilleure solution pour ce cas d'utilisation est d'utiliser les props, ce dont nous parlerons dans le prochain chapitre. Mais restez avec moi pour cet exemple

Vous pouvez fournir une fonction, appelée `changeColor`.

Vous l'écrivez et l'exportez dans cette balise `script` spéciale :

```html
<script context="module">
  export function changeColor() {
    //...logique pour changer la couleur..
  }
</script>

<button>A button</button>

```

Notez que vous pouvez avoir une autre balise "normale" script, dans le composant.

Maintenant, d'autres composants peuvent importer Button, qui est l'exportation par défaut, et la fonction `changeColor` aussi :

```html
<script>
  import Button, { changeColor } from './Button.svelte'
</script>

```

C'est probablement un exemple un peu bête, mais savoir que vous pouvez utiliser cette fonctionnalité peut être assez utile.

## Gestion de l'État dans Svelte

Chaque composant, en plus de définir le balisage, le CSS et la logique JavaScript, peut héberger son propre **état**.

Qu'est-ce que l'état ? L'état est toute donnée nécessaire pour que le composant rende ce qu'il rend.

Par exemple, si un champ de formulaire a la chaîne "test" écrite dedans, il y aura une variable quelque part qui contient cette valeur. C'est l'état du champ de saisie.

Le champ est sélectionné ? Une variable quelque part enregistrera ce fait. Et ainsi de suite.

L'état est défini dans la partie `script` d'un composant :

```html
<script>
  let count = 0
</script>

```

Pour mettre à jour la valeur d'une variable d'état, tout ce dont vous avez besoin est une affectation. Une simple affectation JavaScript, par exemple en utilisant l'opérateur `=`.

Supposons que vous avez une variable `count`. Vous pouvez l'incrémenter simplement en utilisant `count = count + 1`, ou même `count++` :

```html
<script>
  let count = 0

  const incrementCount = () => {
    count++
  }
</script>

{count} <button on:click="{incrementCount}">+1</button>

```

Je trouve que c'est l'une des parties rafraîchissantes de Svelte, car dans React, par exemple, vous devriez utiliser le hook `useState()`, et utiliser une fonction de setter chaque fois que vous voulez mettre à jour la valeur de la variable d'état.

C'est plus intuitif et beaucoup plus proche de la syntaxe "JavaScript-like".

Nous devons être conscients d'une chose, qui est apprise assez rapidement : nous devons également faire une affectation lorsque nous changeons la valeur.

Svelte veut toujours une affectation, sinon il pourrait ne pas reconnaître que l'état a changé.

Pour des valeurs simples comme les chaînes de caractères et les nombres, c'est surtout donné, car toutes les méthodes sur String retournent de nouvelles chaînes, et de même pour les nombres - ils sont immuables.

Mais pour les tableaux ? Nous ne pouvons pas utiliser de méthodes qui altèrent le tableau. Comme `push()`, `pop()`, `shift()`, `splice()`... car il n'y a pas d'affectation. Ils changent la structure de données interne, mais Svelte ne peut pas détecter cela.

Eh bien, vous pouvez _toujours_ les utiliser, mais après avoir fait votre opération, vous pouvez utiliser un "truc" et réaffecter la variable à elle-même, comme ceci :

```js
let list = [1, 2, 3]
list.push(4)
list = list

```

C'est un peu contre-intuitif, comparé à ce que je viens de dire avant, mais c'est une particularité dont vous vous souviendrez avec l'expérience.

Bien sûr, vous pourriez utiliser des alternatives qui vous évitent cette situation, par exemple au lieu d'utiliser `Array.push()` vous pouvez utiliser l'opérateur de décomposition pour ajouter un élément :

```js
let list = [1, 2, 3]
list = [...list, 4]

```

## Réactivité Svelte

Dans Svelte, vous pouvez écouter les changements dans l'état du composant et mettre à jour d'autres variables.

Par exemple, si vous avez une variable `count` :

```html
<script>
  let count = 0
</script>

```

et vous la mettez à jour en cliquant sur un bouton :

```html
<script>
  let count = 0

  const incrementCount = () => {
    count = count + 1
  }
</script>

{count} <button on:click="{incrementCount}">+1</button>

```

Vous pouvez écouter les changements sur `count` en utilisant la syntaxe spéciale `$:` qui définit un nouveau bloc que Svelte réexécutera lorsque toute variable référencée dedans change.

Voici un exemple :

```html
<script>
  let count = 0

  const incrementCount = () => {
    count = count + 1
  }

  $: console.log(`${count}`)
</script>

{count} <button on:click="{incrementCount}">+1</button>

```

J'ai utilisé le bloc :

```js
$: console.log(`${count}`)

```

Vous pouvez en écrire plus d'un :

```html
<script>
  $: console.log(`le compte est ${count}`)
  $: console.log(`le double du compte est ${count * 2}`)
</script>

```

Et vous pouvez également ajouter un **bloc** (accolades ouvrantes et fermantes `{}`) pour regrouper plus d'une instruction :

```html
<script>
  $: {
    console.log(`le compte est ${count}`)
    console.log(`le double du compte est ${count * 2}`)
  }
</script>

```

J'ai utilisé un appel `console.log()` dedans, mais vous pouvez également mettre à jour d'autres variables :

```html
<script>
  let count = 0
  let double = 0

  $: {
    console.log(`le compte est ${count}`)
    double = count * 2
    console.log(`le double du compte est ${double}`)
  }
</script>

```

## Props Svelte

Vous pouvez importer un composant Svelte dans n'importe quel autre composant en utilisant la syntaxe `import name from 'path'`, comme ceci :

```html
<script>
  import SignupForm from './SignupForm.svelte'
</script>

```

> Le chemin est relatif au chemin du composant actuel. `./` signifie "ce même dossier". Vous utiliseriez `../` pour remonter d'un dossier, et ainsi de suite.

Une fois que vous l'avez fait, vous pouvez utiliser le nouveau composant importé dans le balisage, comme une balise HTML :

```html
<SignupForm />

```

De cette manière, vous établissez une relation parent/enfant entre les deux composants : celui qui importe et celui qui est importé.

Souvent, vous souhaitez que le composant parent passe des données au composant enfant.

Vous pouvez le faire en utilisant des **props**. Les props se comportent de manière similaire aux attributs en HTML simple, et ils sont une forme de communication à sens unique.

Dans cet exemple, nous passons la prop `disabled`, en lui passant la valeur JavaScript `true` :

```html
<SignupForm disabled="{true}" />

```

Dans le composant SignupForm, vous devez **exporter** la prop `disabled`, de cette manière :

```html
<script>
  export let disabled
</script>

```

C'est la manière dont vous exprimez le fait que la prop est exposée aux composants parents.

Lors de l'utilisation du composant, vous pouvez passer une variable au lieu d'une valeur, pour la changer dynamiquement :

```html
<script>
  import SignupForm from './SignupForm.svelte'
  let disabled = true
</script>

<SignupForm {disabled} />

```

> Notez que j'ai utilisé `{disabled}` comme une forme abrégée pratique pour `disabled={disabled}`

Lorsque la valeur de la variable `disabled` change, le composant enfant sera mis à jour avec la nouvelle valeur de la prop. Exemple :

```html
<script>
  import SignupForm from './SignupForm.svelte'
  let disabled = true
  setTimeout(() => {
    disabled = false
  }, 2000)
</script>

<SignupForm {disabled} />

```

## Gestion de l'État entre Composants dans Svelte

Nous avons déjà vu comment Svelte facilite la gestion de l'état d'un seul composant.

Mais comment transmettre l'état entre les composants ?

### Transmettre l'état en utilisant les props

La première stratégie est commune à d'autres frameworks UI et consiste à transmettre l'état en utilisant les props, **en remontant l'état**.

Lorsque qu'un composant doit partager des données avec un autre, l'état peut être remonté dans l'arborescence des composants jusqu'à ce qu'il y ait un parent commun à ces composants.

L'état doit être transmis vers le bas jusqu'à ce qu'il atteigne tous les composants qui ont besoin de cette information d'état.

Cela se fait en utilisant des **props**, et c'est une technique que je pense être la meilleure car elle est simple.

### L'API de contexte

Cependant, il existe des cas où les props ne sont pas pratiques. Peut-être que 2 composants sont si éloignés dans l'arborescence des composants que nous devrions remonter l'état jusqu'au composant de niveau supérieur.

Dans ce cas, une autre technique peut être utilisée et elle s'appelle **API de contexte**, et elle est idéale lorsque vous souhaitez permettre à plusieurs composants de communiquer avec des descendants, mais vous ne voulez pas transmettre des props.

L'API de contexte est fournie par 2 fonctions qui sont fournies par le package `svelte` : `getContext` et `setContext`.

Vous définissez un objet dans le contexte, en l'associant à une clé :

```html
<script>
  import { setContext } from 'svelte'

  const someObject = {}

  setContext('someKey', someObject)
</script>

```

Dans un autre composant, vous pouvez utiliser `getContext` pour récupérer l'objet associé à une clé :

```html
<script>
  import { getContext } from 'svelte'

  const someObject = getContext('someKey')
</script>

```

Vous ne pouvez utiliser `getContext` pour récupérer une clé que dans le composant qui a utilisé `setContext` ou dans l'un de ses descendants.

Si vous souhaitez permettre à deux composants vivant dans 2 arbres de composants différents de communiquer, il y a un autre outil pour nous : les **stores**.

### Utilisation des stores Svelte

Les stores Svelte sont un excellent outil pour gérer l'état de votre application lorsque les composants doivent communiquer entre eux sans transmettre trop de props.

Vous devez d'abord importer `writable` depuis `svelte/store` :

```js
import { writable } from 'svelte/store'

```

et créer une variable de store en utilisant la fonction `writable()`, en passant la valeur par défaut comme premier argument :

```js
const username = writable('Guest')

```

Cela peut être placé dans un fichier séparé que vous pouvez importer dans plusieurs composants, par exemple, appelé `store.js` (ce n'est pas un composant, donc il peut être dans un fichier `.js` au lieu de `.svelte`) :

```js
import { writable } from 'svelte/store'
export const username = writable('Guest')

```

Tout autre composant chargeant maintenant ce fichier peut accéder au store :

```html
<script>
  import { username } from './store.js'
</script>

```

Maintenant, la valeur de cette variable peut être définie sur une nouvelle valeur en utilisant `set()`, en passant la nouvelle valeur comme premier argument :

```js
username.set('new username')

```

Et elle peut être mise à jour en utilisant la fonction `update()`, qui diffère de `set()` car vous ne passez pas simplement la nouvelle valeur - vous exécutez une fonction de rappel qui reçoit la valeur actuelle comme argument :

```js
const newUsername = 'new username!'
username.update((existing) => newUsername)

```

Vous pouvez ajouter plus de logique ici :

```js
username.update((existing) => {
  console.log(`Updating username from ${existing} to ${newUsername}`)
  return newUsername
})

```

Pour obtenir la valeur de la variable de store _une fois_, vous pouvez utiliser la fonction `get()` exportée par `svelte/store` :

```js
import { writable, get } from 'svelte/store'
export const username = writable('Guest')
get(username) //'Guest'

```

Pour créer une variable réactive qui est mise à jour chaque fois que la valeur du store change, vous pouvez préfixer la variable de store en utilisant `$` (dans cet exemple `$username`). L'utilisation de cela fera en sorte que le composant se réaffiche chaque fois que la valeur stockée change.

> Svelte considère `$` comme une valeur réservée et vous empêchera de l'utiliser pour des choses qui ne sont pas liées aux valeurs des stores (ce qui pourrait prêter à confusion), donc si vous avez l'habitude de préfixer les références DOM en utilisant `$`, ne le faites pas dans Svelte.

> Une autre option, mieux adaptée si vous devez exécuter une logique lorsque la variable change, est d'utiliser la méthode `subscribe()` de `username` :

```js
username.subscribe((newValue) => {
  console.log(newValue)
})

```

En plus des stores writable, Svelte fournit 2 types spéciaux de stores : les **stores readable** et les **stores derived**.

### Stores Readable Svelte

Les stores readable sont spéciaux car ils ne peuvent pas être mis à jour depuis l'extérieur - il n'y a pas de méthode `set()` ou `update()`. Au lieu de cela, une fois que vous avez défini l'état initial, ils ne peuvent pas être modifiés depuis l'extérieur.

La documentation officielle de Svelte montre un exemple intéressant utilisant un minuteur pour mettre à jour une date. Je peux penser à mettre en place un minuteur pour récupérer une ressource depuis le réseau, effectuer un appel d'API, obtenir des données depuis le système de fichiers (en utilisant un serveur Node.js local) ou toute autre chose qui peut être mise en place de manière autonome.

Dans ce cas, au lieu d'utiliser `writable()` pour initialiser la variable de store, nous utilisons `readable()` :

```js
import { readable } from 'svelte/store'
export const count = readable(0)

```

Vous pouvez fournir une fonction après la valeur par défaut, qui sera responsable de sa mise à jour. Cette fonction reçoit la fonction `set` pour modifier la valeur :

```html
<script>
  import { readable } from 'svelte/store'
  export const count = readable(0, (set) => {
    setTimeout(() => {
      set(1)
    }, 1000)
  })
</script>

```

Dans ce cas, nous mettons à jour la valeur de 0 à 1 après 1 seconde.

Vous pouvez également configurer un intervalle dans cette fonction :

```js
import { readable, get } from 'svelte/store'
export const count = readable(0, (set) => {
  setInterval(() => {
    set(get(count) + 1)
  }, 1000)
})

```

Vous pouvez utiliser cela dans un autre composant comme ceci :

```html
<script>
  import { count } from './store.js'
</script>

{$count}

```

### Stores Derived Svelte

Un store derived vous permet de créer une nouvelle valeur de store qui dépend de la valeur d'un store existant.

Vous pouvez le faire en utilisant la fonction `derived()` exportée par `svelte/store` qui prend comme premier paramètre la valeur du store existant, et comme second paramètre une fonction qui reçoit cette valeur de store comme premier paramètre :

```js
import { writable, derived } from 'svelte/store'

export const username = writable('Guest')

export const welcomeMessage = derived(username, ($username) => {
  return `Welcome ${$username}`
})

```

```html
<script>
  import { username, welcomeMessage } from './store.js'
</script>

{$username} {$welcomeMessage}

```

## Slots

Les slots sont un moyen pratique de vous permettre de définir des composants qui peuvent être composés ensemble.

Et vice versa, selon votre point de vue, les slots sont un moyen pratique de configurer un composant que vous importez.

Voici comment ils fonctionnent.

Dans un composant, vous pouvez définir un slot en utilisant la syntaxe `<slot />` (ou `<slot></slot>`).

Voici un composant `Button.svelte` qui imprime simplement une balise `<button>` HTML :

```html
<button><slot /></button>

```

> Pour les développeurs React, c'est essentiellement la même chose que `<button>{props.children}</button>`

Tout composant l'important peut définir un contenu qui sera placé dans le slot en l'ajoutant dans les balises d'ouverture et de fermeture du composant :

```html
<script>
  import Button from './Button.svelte'
</script>

<button>Insert this into the slot</button>

```

Vous pouvez définir une valeur par défaut, qui est utilisée si le slot n'est pas rempli :

```html
<button>
  <slot> Default text for the button </slot>
</button>

```

Vous pouvez avoir plus d'un slot dans un composant, et vous pouvez distinguer l'un de l'autre en utilisant des slots nommés. Le slot unique sans nom sera celui par défaut :

```html
<slot name="before" />
<button>
  <slot />
</button>
<slot name="after" />

```

Voici comment vous l'utiliseriez :

```html
<script>
  import Button from './Button.svelte'
</script>

<button>
  Insert this into the slot
  <p slot="before">Add this before</p>
  <p slot="after">Add this after</p>
</button>

```

Et cela rendrait le suivant dans le DOM :

```html
<p slot="before">Add this before</p>
<button>Insert this into the slot</button>
<p slot="after">Add this after</p>

```

## Événements du Cycle de Vie Svelte

Chaque composant dans Svelte déclenche plusieurs événements du cycle de vie auxquels nous pouvons nous accrocher, pour nous aider à implémenter la fonctionnalité que nous avons en tête.

En particulier, nous avons

* `onMount` déclenché après que le composant est rendu
* `onDestroy` déclenché après que le composant est détruit
* `beforeUpdate` déclenché avant que le DOM soit mis à jour
* `afterUpdate` déclenché après que le DOM est mis à jour

Nous pouvons planifier des fonctions pour se produire lorsque ces événements sont déclenchés par Svelte.

Nous n'avons pas accès à aucune de ces méthodes par défaut, mais nous devons les importer depuis le package `svelte` :

```html
<script>
  import { onMount, onDestroy, beforeUpdate, afterUpdate } from 'svelte'
</script>

```

Un scénario courant pour `onMount` est de récupérer des données depuis d'autres sources.

Voici un exemple d'utilisation de `onMount` :

```html
<script>
  import { onMount } from 'svelte'

  onMount(async () => {
    //faire quelque chose au montage
  })
</script>

```

`onDestroy` nous permet de nettoyer des données ou d'arrêter toute opération que nous aurions pu démarrer à l'initialisation du composant, comme des minuteurs ou des fonctions périodiques planifiées utilisant `setInterval`.

Une chose particulière à noter est que si nous retournons une fonction depuis `onMount`, cela sert la même fonctionnalité que `onDestroy` - elle est exécutée lorsque le composant est détruit :

```html
<script>
  import { onMount } from 'svelte'

  onMount(async () => {
    //faire quelque chose au montage

    return () => {
      //faire quelque chose à la destruction
    }
  })
</script>

```

Voici un exemple pratique qui définit une fonction périodique pour s'exécuter au montage, et la supprime à la destruction :

```html
<script>
  import { onMount } from 'svelte'

  onMount(async () => {
    const interval = setInterval(() => {
      console.log('hey, juste en train de vérifier !')
    }, 1000)

    return () => {
      clearInterval(interval)
    }
  })
</script>

```

## Bindings Svelte

En utilisant Svelte, vous pouvez créer une liaison bidirectionnelle entre les données et l'UI.

De nombreux autres frameworks Web peuvent fournir des liaisons bidirectionnelles, c'est un modèle de conception UI très courant.

Ils sont particulièrement utiles avec les formulaires.

### bind:value

Commençons par la forme de liaison la plus courante que vous utiliserez souvent, que vous pouvez appliquer en utilisant `bind:value`. Vous prenez une variable de l'état du composant et vous la liez à un champ de formulaire :

```html
<script>
  let name = ''
</script>

<input bind:value="{name}" />

```

Maintenant, si `name` change, le champ d'entrée mettra à jour sa valeur. Et l'inverse est également vrai : si le formulaire est mis à jour par l'utilisateur, la valeur de la variable `name` change.

> Soyez simplement conscient que la variable doit être définie en utilisant `let/var` et non `const`, sinon elle ne peut pas être mise à jour par Svelte, car `const` définit une variable avec une valeur qui ne peut pas être réaffectée.

`bind:value` fonctionne sur toutes les variantes de champs d'entrée (`type="number"`, `type="email"` et ainsi de suite), mais il fonctionne également pour d'autres types de champs, comme `textarea` et `select` (plus sur `select` plus tard).

### Cases à cocher et boutons radio

Les cases à cocher et les entrées radio (`input` éléments avec `type="checkbox"` ou `type="radio"`) permettent ces 3 liaisons :

* `bind:checked`
* `bind:group`
* `bind:indeterminate`

`bind:checked` nous permet de lier une valeur à l'état coché de l'élément :

```html
<script>
  let isChecked
</script>

<input type="checkbox" bind:checked="{isChecked}" />

```

`bind:group` est pratique avec les cases à cocher et les entrées radio, car celles-ci sont très souvent utilisées en groupes. En utilisant `bind:group`, vous pouvez associer un tableau JavaScript à une liste de cases à cocher, et le voir peuplé en fonction des choix faits par l'utilisateur.

Voici un exemple. Le tableau `goodDogs` se remplit en fonction des cases à cocher que je coche :

```html
<script>
  let goodDogs = []
  let dogs = ['Roger', 'Syd']
</script>

<h2>Qui est un bon chien ?</h2>

<ul>
  {#each dogs as dog}
  <li>{dog} <input type="checkbox" bind:group="{goodDogs}" value="{dog}" /></li>
  {/each}
</ul>

<h2>Bons chiens selon moi :</h2>

<ul>
  {#each goodDogs as dog}
  <li>{dog}</li>
  {/each}
</ul>

```

[Voir l'exemple](https://svelte.dev/repl/059c1b5edffc4b058ad36301dd7a1a58)

`bind:indeterminate` nous permet de lier à l'état `indeterminate` d'un élément (si vous voulez en savoir plus, allez sur [https://css-tricks.com/indeterminate-checkboxes/](https://css-tricks.com/indeterminate-checkboxes/))

### Champs de sélection

`bind:value` fonctionne également pour le champ de formulaire `select` pour obtenir la valeur sélectionnée automatiquement assignée à la valeur d'une variable :

```html
<script>
  let selected
</script>

<select bind:value="{selected}">
  <option value="1">1</option>
  <option value="2">2</option>
  <option value="3">3</option>
</select>

{selected}

```

Le truc cool est que si vous générez des options dynamiquement à partir d'un tableau d'objets, l'option sélectionnée est maintenant un objet, pas une chaîne :

```html
<script>
  let selected

  const dogs = [{ name: 'Roger' }, { name: 'Syd' }]
</script>

<h2>Liste des chiens potentiellement bons :</h2>
<select bind:value="{selected}">
  {#each dogs as dog}
  <option value="{dog}">{dog.name}</option>
  {/each}
</select>

{#if selected}
<h2>Chien sélectionné : {selected.name}</h2>
{/if}

```

[Voir cet exemple](https://svelte.dev/repl/7e06f9b7becd4c57880db5ed184ea0f3)

`select` permet également l'attribut `multiple` :

```html
<script>
  let selected = []

  const goodDogs = [{ name: 'Roger' }, { name: 'Syd' }]
</script>

<h2>Liste des chiens potentiellement bons :</h2>
<select multiple bind:value="{selected}">
  {#each goodDogs as goodDog}
  <option value="{goodDog}">{goodDog.name}</option>
  {/each}
</select>

{#if selected.length}
<h2>Bon chien sélectionné :</h2>
<ul>
  {#each selected as dog}
  <li>{dog.name}</li>
  {/each}
</ul>
{/if}

```

[Voir cet exemple](https://svelte.dev/repl/b003248e87f04919a2f9fed63dbdab8c)

### Autres liaisons

Selon la balise HTML sur laquelle vous travaillez, vous pouvez appliquer différents types de liaisons.

`bind:files` est une liaison valide sur les éléments d'entrée `type="file"`, pour lier la liste des fichiers sélectionnés.

L'élément HTML `details` permet l'utilisation de `bind:open` pour lier sa valeur ouverte/fermée.

Les balises média HTML `audio` et `video` permettent de lier plusieurs de leurs propriétés : `currentTime`, `duration`, `paused`, `buffered`, `seekable`, `played`, `volume`, `playbackRate`.

`textContent` et `innerHTML` peuvent être liés sur les champs `contenteditable`.

Toutes choses très utiles pour ces éléments HTML spécifiques.

### Liaisons en lecture seule

`offsetWidth`, `offsetHeight`, `clientWidth`, `clientHeight` peuvent être liés, en lecture seule, sur tout élément HTML de niveau bloc, à l'exclusion des balises vides (comme `br`) et des éléments qui sont définis pour être en ligne (`display: inline`).

### Obtenir une référence à l'élément HTML en JavaScript

`bind:this` est un type spécial de liaison qui vous permet d'obtenir une référence à un élément HTML et de le lier à une variable JavaScript :

```html
<script>
  let myInputField
</script>

<input bind:this="{myInputField}" />

```

C'est pratique lorsque vous devez appliquer une logique aux éléments après les avoir montés, par exemple, en utilisant le rappel de l'événement du cycle de vie `onMount()`.

### Liaison des props des composants

En utilisant `bind:`, vous pouvez lier une valeur à n'importe quelle prop qu'un composant expose.

Supposons que vous avez un composant `Car.svelte` :

```html
<script>
export let inMovement = false
</script>

<button on:click={() => inMovement = true }>Démarrer la voiture</button>

```

Vous pouvez importer le composant et lier la prop `inMovement` :

```html
<script>
  import Car from './Car.svelte'

  let carInMovement
</script>

<Car bind:inMovement="{carInMovement}" />

{carInMovement}

```

Cela peut permettre des scénarios intéressants.

## Logique Conditionnelle dans les Templates

Dans un composant Svelte, lorsqu'il s'agit de rendre du HTML, vous pouvez travailler avec une syntaxe spécifique pour créer l'UI dont vous avez besoin à chaque étape du cycle de vie de l'application.

En particulier, nous allons maintenant explorer les structures conditionnelles.

Le problème est le suivant : vous voulez pouvoir regarder une valeur/expression, et si celle-ci pointe vers une valeur vraie, faire quelque chose, si elle pointe vers une valeur fausse, alors faire autre chose.

Svelte nous fournit un ensemble très puissant de structures de contrôle.

La première est **if** :

```html
{#if isRed}
<p>Rouge</p>
{/if}

```

Il y a une ouverture `{#if}` et une fermeture `{/if}`. Le balisage d'ouverture vérifie qu'une valeur ou une instruction est vraie. Dans ce cas, `isRed` peut être un booléen avec une valeur `true` :

```html
<script>
  let isRed = true
</script>

```

Une chaîne vide est fausse, mais une chaîne avec du contenu est vraie.

0 est faux, mais un nombre > 0 est vrai.

La valeur booléenne `true` est vraie, bien sûr, et `false` est fausse.

Si le balisage d'ouverture n'est pas satisfait (une valeur fausse est fournie), alors rien ne se passe.

Pour faire autre chose si ce n'est pas satisfait, nous utilisons l'instruction appelée `else` :

```html
{#if isRed}
<p>Rouge</p>
{:else}
<p>Pas rouge</p>
{/if}

```

Soit le premier bloc est rendu dans le template, soit le second. Il n'y a pas d'autre option.

Vous pouvez utiliser n'importe quelle expression JavaScript dans la condition du bloc `if`, donc vous pouvez nier une option en utilisant l'opérateur `!` :

```html
{#if !isRed}
<p>Pas rouge</p>
{:else}
<p>Rouge</p>
{/if}

```

Maintenant, à l'intérieur du `else`, vous pourriez vouloir vérifier une condition supplémentaire. C'est là que la syntaxe `{:else if somethingElse}` intervient :

```html
{#if isRed}
<p>Rouge</p>
{:else if isGreen}
<p>Vert</p>
{:else}
<p>Ni rouge ni vert</p>
{/if}

```

Vous pouvez avoir plusieurs de ces blocs, pas seulement un, et vous pouvez les imbriquer. Voici un exemple plus complexe :

```html
{#if isRed}
<p>Rouge</p>
{:else if isGreen}
<p>Vert</p>
{:else if isBlue}
<p>C'est bleu</p>
{:else} {#if isDog}
<p>C'est un chien</p>
{/if} {/if}

```

## Boucles dans les Templates Svelte

Dans les templates Svelte, vous pouvez créer une boucle en utilisant la syntaxe `{#each}{/each}` :

```html
<script>
  let dogs = ['Roger', 'Syd']
</script>

{#each dogs as dog}
<li>{dog}</li>
{/each}

```

Si vous êtes familier avec d'autres frameworks qui utilisent des templates, c'est une syntaxe très similaire.

Vous pouvez obtenir l'index de l'itération en utilisant :

```html
<script>
  let dogs = ['Roger', 'Syd']
</script>

{#each dogs as dog, index}
<li>{index}: {dog}</li>
{/each}

```

(les index commencent à 0)

Lorsque vous éditez dynamiquement les listes en supprimant et en ajoutant des éléments, vous devez toujours passer un identifiant dans les listes, pour éviter les problèmes.

Vous le faites en utilisant cette syntaxe :

```html
<script>
  let dogs = ['Roger', 'Syd']
</script>

{#each dogs as dog (dog)}
<li>{dog}</li>
{/each}

<!-- avec l'index -->
{#each dogs as dog, index (dog)}
<li>{dog}</li>
{/each}

```

Vous pouvez passer un objet, aussi, mais si votre liste a un identifiant unique pour chaque élément, il est préférable de l'utiliser :

```html
<script>
  let dogs = [
    { id: 1, name: 'Roger' },
    { id: 2, name: 'Syd' },
  ]
</script>

{#each dogs as dog (dog.id)}
<li>{dog.name}</li>
{/each}

<!-- avec l'index -->
{#each dogs as dog, index (dog.id)}
<li>{dog.name}</li>
{/each}

```

## Promesses dans les Templates Svelte

Les promesses sont un outil formidable dont nous disposons pour travailler avec des événements asynchrones en JavaScript.

L'introduction relativement récente de la syntaxe `await` dans ES2017 a rendu l'utilisation des promesses encore plus simple.

Svelte nous fournit la syntaxe `{#await}` dans les templates pour travailler directement avec les promesses au niveau du template.

Nous pouvons attendre que les promesses se résolvent et définir une UI différente pour les divers états d'une promesse : non résolue, résolue et rejetée.

Voici comment cela fonctionne. Nous définissons une promesse et, en utilisant le bloc `{#await}`, nous attendons qu'elle se résolve.

Une fois la promesse résolue, le résultat est passé au bloc `{:then}` :

```html
<script>
  const fetchImage = (async () => {
    const response = await fetch('https://dog.ceo/api/breeds/image/random')
    return await response.json()
  })()
</script>

{#await fetchImage}
<p>...en attente</p>
{:then data}
<img src="{data.message}" alt="Image de chien" />
{/await}

```

Vous pouvez détecter un rejet de promesse en ajoutant un bloc `{:catch}` :

```html
{#await fetchImage}
<p>...en attente</p>
{:then data}
<img src="{data.message}" alt="Image de chien" />
{:catch error}
<p>Une erreur s'est produite !</p>
{/await}

```

[Exécuter l'exemple](https://svelte.dev/repl/70e61d6cc91345cdaca2db9b7077a941)

## Travailler avec les Événements dans Svelte

### Écouter les événements DOM

Dans Svelte, vous pouvez définir un écouteur pour un événement DOM directement dans le template, en utilisant la syntaxe `on:<event>`.

Par exemple, pour écouter l'événement `click`, vous passerez une fonction à l'attribut `on:click`.

Pour écouter l'événement `onmousemove`, vous passerez une fonction à l'attribut `on:mousemove`.

Voici un exemple avec la fonction de gestion définie en ligne :

```js
<button
  on:click={() => {
    alert('cliqué')
  }}
>
  Cliquez-moi
</button>

```

et voici un autre exemple avec la fonction de gestion définie dans la section `script` du composant :

```js
<script>
const doSomething = () => {
  alert('cliqué')
}
</script>

<button on:click={doSomething}>Cliquez-moi</button>

```

Je préfère en ligne lorsque le code n'est pas trop verbeux. Si ce n'est que 2-3 lignes, par exemple, sinon je déplacerais cela dans la section script.

Svelte passe le gestionnaire d'événements comme argument de la fonction, ce qui est pratique si vous devez arrêter la propagation ou référencer quelque chose dans l'[objet Event](https://flaviocopes.com/javascript-events/#the-event-object) :

```js
<script>
const doSomething = event => {
  console.log(event)
  alert('cliqué')
}
</script>

<button on:click={doSomething}>Cliquez-moi</button>

```

Maintenant, j'ai mentionné "stop propagation". C'est une chose très courante à faire, pour arrêter les événements de soumission de formulaire par exemple. Svelte nous fournit des **modificateurs**, un moyen de l'appliquer directement sans le faire manuellement.  
`stopPropagation` et `preventDefault` sont les 2 modificateurs que vous utiliserez le plus, je pense.

Vous appliquez un modificateur comme ceci : `<button on:click|stopPropagation|preventDefault={doSomething}>Cliquez-moi</button>`

Il existe d'autres modificateurs, qui sont plus niche. `capture` active [la capture d'événements au lieu du bubbling](https://flaviocopes.com/javascript-events/#event-bubbling-and-event-capturing), `once` ne déclenche l'événement qu'une seule fois, `self` ne déclenche l'événement que si la cible de l'événement est cet objet (en le retirant de la hiérarchie de bubbling/capturing).

### Créer vos événements dans les composants

Ce qui est intéressant, c'est que nous pouvons créer des événements personnalisés dans les composants, et utiliser la même syntaxe que les événements DOM intégrés.

Pour ce faire, nous devons importer la fonction `createEventDispatcher` depuis le package `svelte` et l'appeler pour obtenir un dispatcher d'événements :

```html
<script>
  import { createEventDispatcher } from 'svelte'
  const dispatch = createEventDispatcher()
</script>

```

Une fois que nous l'avons fait, nous pouvons appeler la fonction `dispatch()`, en passant une chaîne qui identifie l'événement (que nous utiliserons pour la syntaxe `on:` dans d'autres composants qui utilisent celui-ci) :

```html
<script>
  import { createEventDispatcher } from 'svelte'
  const dispatch = createEventDispatcher()

  //quand il est temps de déclencher l'événement
  dispatch('eventName')
</script>

```

Maintenant, d'autres composants peuvent utiliser le nôtre en utilisant

```html
<ComponentName on:eventName={event => { //faire quelque chose }} />

```

Vous pouvez également passer un objet à l'événement, en passant un deuxième paramètre à `dispatch()` :

```html
<script>
  import { createEventDispatcher } from 'svelte'
  const dispatch = createEventDispatcher()
  const value = 'something'

  //quand il est temps de déclencher l'événement
  dispatch('eventName', value)

  //ou

  dispatch('eventName', {
    someProperty: value,
  })
</script>

```

l'objet passé par `dispatch()` est disponible sur l'objet `event`.

## Où Aller à partir d'Ici

J'espère que ce petit guide a été utile pour éclairer ce que Svelte peut faire pour vous, et j'espère que vous êtes maintenant intéressé à en apprendre davantage à ce sujet !

Je peux maintenant vous orienter vers deux endroits pour en apprendre davantage :

* [Le site officiel de Svelte](https://svelte.dev/)
* [SvelteKit](https://kit.svelte.dev/), un framework génial construit sur Svelte qui vous permet de construire des applications rendues côté serveur avec Node.js et Svelte

[Vous pouvez obtenir une version PDF et ePub de ce Guide Svelte](https://thevalleyofcode.com/download/svelte/)