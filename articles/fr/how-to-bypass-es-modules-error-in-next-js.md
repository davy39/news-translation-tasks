---
title: Comment contourner les erreurs de modules ES dans Next.js avec les imports
  dynamiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-19T19:58:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-bypass-es-modules-error-in-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/tim-gouw-1K9T5YiZ2WU-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: ES6
  slug: es6
- name: modules
  slug: modules
- name: Next.js
  slug: nextjs
seo_title: Comment contourner les erreurs de modules ES dans Next.js avec les imports
  dynamiques
seo_desc: 'By Caleb Olojo

  When you are building an application that can be accessed on the web, there are
  a lot of dependencies or packages that you will need for your application to function
  well.

  You''ll need most of these packages when you''re building JAMStac...'
---

Par Caleb Olojo

Lorsque vous construisez une application accessible sur le web, il y a beaucoup de dépendances ou de packages dont vous aurez besoin pour que votre application fonctionne bien.

Vous aurez besoin de la plupart de ces packages lorsque vous construisez des applications JAMStack avec des frameworks ou des bibliothèques comme React, Vuejs, Next.js ou Angular.

Dans cet article, je vais vous expliquer une erreur que vous pourriez rencontrer lorsque vous construisez des applications JavaScript avec Next.js, et comment la contourner.

## Qu'est-ce que les ESModules ?

Les ESModules sont les standards ECMAScript pour travailler avec des modules JavaScript dans le navigateur.

"Qu'est-ce que cela a à voir avec ces erreurs ennuyeuses et frustrantes que je vois depuis quelques jours ?" pourriez-vous me demander.

Eh bien... Node.js a utilisé les standards **CommonJS** pendant très longtemps pour structurer correctement le code JavaScript ou les modules dans ce scénario, et la majorité du code que nous écrivons réside/fonctionne dans le navigateur.

Il n'y avait pas de standards pour guider correctement l'utilisation ou l'interprétation des modules JavaScript, du moins dans les navigateurs web. Ce défi a donné lieu aux standards ESModules qui guident le fonctionnement des modules JavaScript dans le navigateur.

Ce standard a été approuvé lors du lancement d'ES6 (ECMAScript 6) en 2015, et a conduit à la mise en œuvre des standards dans divers navigateurs web comme Chrome, Safari, Firefox et Microsoft Edge.

La plupart des packages que nous utilisons pour construire des interfaces utilisateur front-end sont écrits en JavaScript. Ils ont des modules qui exportent une fonction particulière (ce pourrait être un composant JavaScript), un objet, une chaîne de caractères, un ensemble de tableaux, etc.

Ces fonctions, tableaux ou chaînes de caractères peuvent être exposés en tant que bibliothèques à d'autres fichiers JavaScript. Par exemple, nous avons une fonction qui imprime le nom de quelqu'un dans la console. La syntaxe sera comme ceci :

```js
// name.js
export default (name) => console.log(name)

```

Le snippet ci-dessus décrit une exportation par défaut, sans nom spécifique. Cela signifie que si nous voulons utiliser la fonction dans ce module, nous pouvons l'appeler par n'importe quel nom, puisque aucun nom n'a été explicitement assigné lors de la déclaration.

```js
import printName from "./name.js"

printName("Dodo")

```

## D'accord, mais pourquoi j'ai toujours cette erreur ?

Oui. Passons maintenant à cette erreur. Lorsque nous commençons à interfacer avec beaucoup de dépendances ou de packages dans nos applications, certaines choses peuvent commencer à mal fonctionner si nous ne prenons pas soin de nos bases de code.

Nous commençons à gérer les versions de ces packages, les changements cassants et les releases parfois, que nous ne pouvons pas suivre. Ensuite, nous pourrions commencer à descendre dans le terrier du lapin en rétrogradant ou en mettant à niveau un package npm particulier avant que quoi que ce soit ne fonctionne.

La plupart de ces erreurs peuvent provenir des mainteneurs de ces packages. Prenons, par exemple, le standard ESModules - qui est relativement nouveau - dont nous parlons dans cet article. Il peut prendre un certain temps pour qu'il soit adopté par certains frameworks ou bibliothèques JavaScript front-end, par exemple, Next.js.

L'erreur dans l'image ci-dessous montre que nous ne pouvons pas utiliser l'approche CommonJS pour importer un module.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/serialize-1.png)

Ce nouveau standard et le fait qu'il soit un peu méconnu de ces outils que nous utilisons est la raison de cette erreur. [Nirmalya Ghosh a écrit cet article sur la maintenance des grandes applications Next.js](https://www.smashingmagazine.com/2021/11/maintain-large-nextjs-application/), vous devriez y jeter un coup d'œil.

## Comment utiliser les imports dynamiques dans Next.js

Maintenant que nous avons passé en revue les rudiments des ESModules, voyons comment nous pouvons corriger l'erreur qui est assez similaire à celle que nous avons vue dans l'image ci-dessus. Nous verrons comment nous pouvons la corriger avec les imports dynamiques dans Next.js.

Je vais supposer que vous avez déjà une application Next.js en cours d'exécution, donc je vais simplement partager l'erreur ESModule correspondante que j'ai obtenue de mon terminal dans le bloc de code ci-dessous :

```bash
Error [ERR_REQUIRE_ESM]: Must use import to load ES Module: /path/to/package

require() of ES modules is not supported. 

ES module file as it is a .js file whose nearest parent package.json contains "type": "module" which defines all .js files in that package scope as ES modules.

Instead rename index.js to end in .cjs, change the requiring code to use import(), or remove "type": "module" from /path/to/package

```

Jetez un coup d'œil à l'erreur ci-dessus pour vous familiariser avec elle. Une fois que vous l'avez fait, procédons.

### Qu'est-ce que les imports dynamiques ?

Les imports dynamiques sont une fonctionnalité de Next.js qui vous permet de travailler avec des modules JavaScript de manière pratique dans le navigateur.

Ils fournissent un moyen de pré-rendre ces modules avec SSR (Server-side Rendering) afin que les utilisateurs n'aient pas besoin d'envoyer des requêtes en continu au serveur lorsqu'ils ont besoin - par exemple - d'une page qui utilise un module JavaScript. Avec les imports dynamiques, les modules sont déjà pré-rendus dans le navigateur.

Récemment, je travaillais sur un projet qui concernait le contenu markdown. J'avais besoin d'utiliser des plugins rehype, mais je continuais à obtenir l'erreur dans le bloc de code précédent.

```js
const rehypeSlug = dynamic(() => import('rehype-slug'), { ssr: false })
const rehypeCodeTitles = dynamic(() => import('rehype-code-titles'), {
  ssr: false,
})
const rehypeAutolinkHeadings = dynamic(
  () => import('rehype-autolink-headings'),
  { ssr: false }
)
const rehypePrism = dynamic(() => import('rehype-prism-plus'), { ssr: false })

```

Le snippet ci-dessus montre comment vous pouvez importer un module avec des imports dynamiques et passer l'objet `ssr` comme argument.

Avec cette approche utilisant les imports dynamiques, les erreurs ESModule qui continuaient à apparaître ont été supprimées.

## Conclusion

J'espère donc que vous pourrez utiliser cette fonctionnalité et qu'elle vous libérera de cette erreur.

Il y a beaucoup de choses auxquelles vous devez penser lorsque vous construisez des applications JavaScript, donc cela peut être une chose en moins. Merci d'avoir lu cet article, et j'espère que vous l'avez apprécié.