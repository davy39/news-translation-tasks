---
title: Comment utiliser le React Compiler – Un guide complet
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2024-08-27T22:35:47.879Z'
originalURL: https://freecodecamp.org/news/react-compiler-complete-guide-react-19
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724760187590/f7115fd3-6291-4920-9522-61de269a47f3.png
tags:
- name: React
  slug: reactjs
- name: React 19
  slug: react-19
- name: React-compiler
  slug: react-compiler
- name: Beginner Developers
  slug: beginners
- name: General Programming
  slug: programming
seo_title: Comment utiliser le React Compiler – Un guide complet
seo_desc: 'In this tutorial, you''ll learn how the React compiler can help you write
  more optimized React applications.

  React is a user interface library that has been doing its job quite well for over
  a decade. The component architecture, uni-directional data f...'
---

Dans ce tutoriel, vous apprendrez comment le compilateur React peut vous aider à écrire des applications React plus optimisées.

React est une bibliothèque d'interface utilisateur qui remplit très bien sa mission depuis plus d'une décennie. L'architecture des composants, le flux de données unidirectionnel et la nature déclarative se distinguent en aidant les développeurs à créer des applications logicielles évolutives et prêtes pour la production.

Au fil des versions (même jusqu'à la dernière version stable v18.x), React a fourni diverses techniques et méthodologies pour améliorer les performances des applications.

Par exemple, l'ensemble du paradigme de mémoïsation a été pris en charge à l'aide du composant d'ordre supérieur `React.memo()`, ou avec des hooks comme `useMemo()` et `useCallback()`.

En programmation, la `mémoïsation` est une technique d'optimisation qui accélère l'exécution de vos programmes en mettant en cache le résultat de calculs coûteux.

Bien que les techniques de `mémoïsation` de React soient excellentes pour appliquer des optimisations, comme l'a dit un jour l'Oncle Ben (vous vous souvenez de l'oncle de Spiderman ?), "Un grand pouvoir implique de grandes responsabilités". Nous, en tant que développeurs, devons donc être un peu plus responsables en les appliquant. L'optimisation est une excellente chose, mais la sur-optimisation peut être fatale pour les performances de l'application.

Avec React 19, la communauté des développeurs a reçu une liste d'améliorations et de fonctionnalités dont elle peut se vanter :

* Un compilateur open-source expérimental. Nous nous concentrerons principalement sur celui-ci dans cet article.
    
* React Server Components.
    
* Server Actions.
    
* Une manière plus simple et plus organique de gérer les métadonnées du document.
    
* Des hooks et des API améliorés.
    
* `ref` peut être passé comme accessoire (props).
    
* Des améliorations dans le chargement des ressources pour les styles, les images et les polices.
    
* Une intégration beaucoup plus fluide avec les Web Components.
    

Si ces nouveautés vous passionnent, je vous recommande de [regarder cette vidéo](https://www.youtube.com/watch?v=hiiGUjEkzbM) qui explique comment chaque fonctionnalité vous impactera en tant que développeur React. J'espère qu'elle vous plaira 😊.

L'introduction d'un `compilateur` avec `React 19` va changer la donne. Désormais, nous pouvons laisser le compilateur gérer le casse-tête de l'optimisation plutôt que de nous en charger nous-mêmes.

Cela signifie-t-il que nous n'avons plus besoin d'utiliser `memo`, `useMemo()`, `useCallback`, etc. ? Non – nous n'en aurons plus besoin dans la plupart des cas. Le compilateur peut s'occuper de ces choses automatiquement si vous comprenez et suivez les [Règles de React](https://react.dev/reference/rules) pour les composants et les hooks.

Comment fera-t-il cela ? Eh bien, nous y reviendrons. Mais avant cela, comprenons ce qu'est un `compilateur` et s'il est justifié d'appeler ce nouvel optimiseur de code React le `React Compiler`.

Si vous aimez également apprendre à partir de tutoriels vidéo, cet article est aussi disponible en format vidéo ici :

%[https://www.youtube.com/watch?v=bdWUVp0TbTU] 

## Table des matières

1. [Qu'est-ce qu'un compilateur, traditionnellement ?](#heading-questce-quun-compilateur-traditionnellement)
    
2. [Architecture du React Compiler](#heading-architecture-du-react-compiler)
    
3. [Le React Compiler en action](#heading-le-react-compiler-en-action)
    
4. [Comprendre le problème : Sans le React Compiler](#heading-comprendre-le-probleme-sans-le-react-compiler)
    
5. [Résoudre le problème : Sans le React Compiler](#heading-resoudre-le-probleme-sans-le-react-compiler)
    
6. [Résoudre le problème : En utilisant le React Compiler](#heading-resoudre-le-probleme-en-utilisant-le-react-compiler)
    
7. [Application React optimisée avec le React Compiler](#heading-application-react-optimisee-avec-le-react-compiler)
    
8. [Le React Compiler dans les React DevTools](#heading-le-react-compiler-dans-les-react-devtools)
    
9. [Analyse approfondie - Comment fonctionne le React Compiler ?](#heading-analyse-approfondie-comment-fonctionne-le-react-compiler)
    
10. [Comment activer ou désactiver le React Compiler ?](#heading-comment-activer-ou-desactiver-le-react-compiler)
    
11. [Pouvons-nous utiliser le React Compiler avec React 18.x ?](#heading-pouvons-nous-utiliser-le-react-compiler-avec-react-18x)
    
12. [Dépôts à consulter](#heading-depots-a-consulter)
    
13. [Et ensuite ?](#heading-et-ensuite)
    

## Qu'est-ce qu'un compilateur, traditionnellement ?

Simplement dit, un compilateur est un programme/outil logiciel qui traduit le code d'un langage de programmation de haut niveau (code source) en code machine. Plusieurs étapes sont nécessaires pour compiler le code source et générer le code machine :

* L'`analyseur lexical` segmente le code source en jetons (tokens).
    
* L'`analyseur syntaxique` crée un arbre de syntaxe abstraite (AST) pour structurer logiquement les jetons du code source.
    
* L'`analyseur sémantique` valide la correction sémantique (ou syntaxique) du code.
    
* Après ces trois types d'analyses, un `code intermédiaire` est généré. Il est également connu sous le nom de code IR.
    
* Ensuite, une `optimisation` est effectuée sur le code IR.
    
* Enfin, le `code machine` est généré par le compilateur à partir du code IR optimisé.
    

![Phases du compilateur telles que décrites ci-dessus](https://cdn.hashnode.com/res/hashnode/image/upload/v1724227359567/a3994e4c-9018-4b67-94be-8b5f403eceb9.png align="center")

Maintenant que vous comprenez les bases du fonctionnement d'un compilateur, découvrons le `React Compiler` et son fonctionnement.

## Architecture du React Compiler

Le compilateur React est un outil de build que vous devez configurer explicitement dans votre projet React 19 en utilisant les options de configuration fournies par l'écosystème des outils React.

Par exemple, si vous utilisez `Vite` pour créer votre application React, la configuration du compilateur se fera dans le fichier `vite.config.js`.

Le compilateur React possède trois composants principaux :

1. `Babel Plugin` **:** aide à transformer le code pendant le processus de compilation.
    
2. `ESLint Plugin` **:** aide à détecter et à signaler toute violation des Règles de React.
    
3. `Compiler Core` : la logique centrale du compilateur qui effectue l'analyse du code et les optimisations. Les plugins Babel et ESLint utilisent tous deux cette logique centrale.
    

Le flux de compilation se déroule comme suit :

* Le `Babel Plugin` identifie les fonctions (composants ou hooks) à compiler. Nous verrons quelques configurations plus tard pour apprendre comment activer ou désactiver le processus de compilation. Le plugin appelle la logique centrale du compilateur pour chacune des fonctions et crée enfin l'Arbre de Syntaxe Abstraite (AST).
    
* Ensuite, le cœur du compilateur convertit l'AST Babel en code IR, l'analyse et effectue diverses validations pour s'assurer qu'aucune règle n'est enfreinte.
    
* Ensuite, il essaie de réduire la quantité de code à optimiser en effectuant divers passages pour éliminer le code mort. Le code est ensuite optimisé par mémoïsation.
    
* Enfin, lors de l'étape de génération du code, l'AST transformé est reconverti en code JavaScript optimisé.
    

## Le React Compiler en action

Maintenant que vous savez comment fonctionne le React Compiler, plongeons dans sa configuration avec un projet React 19 afin que vous puissiez commencer à découvrir les diverses optimisations.

### Comprendre le problème : Sans le React Compiler

Créons une page produit simple avec React. La page produit affiche un titre avec le nombre de produits sur la page, une liste de produits et les produits vedettes.

![La page produit](https://cdn.hashnode.com/res/hashnode/image/upload/v1724240252940/bd5118d1-2819-4119-ac96-57e267742432.png align="center")

La hiérarchie des composants et le passage des données entre les composants ressemblent à ceci :

![Hiérarchie des composants de la page produit](https://cdn.hashnode.com/res/hashnode/image/upload/v1724240027326/0a8a653d-9c6a-43ff-9457-81dde019e56e.png align="center")

Comme vous pouvez le voir sur l'image ci-dessus,

* Le composant `ProductPage` possède trois composants enfants : `Heading`, `ProductList` et `FeaturedProducts`.
    
* Le composant `ProductPage` reçoit deux props, `products` et `heading`.
    
* Le composant `ProductPage` calcule le nombre total de produits et transmet la valeur avec le texte du titre au composant `Heading`.
    
* Le composant `ProductPage` transmet la prop `products` au composant enfant `ProductList`.
    
* De même, il calcule les produits vedettes et transmet la prop `featuredProducts` au composant enfant `FeaturedProducts`.
    

Voici à quoi pourrait ressembler le code source du composant `ProductPage` :

```javascript
import React from 'react'

import Heading from './Heading';
import FeaturedProducts from './FeaturedProducts';
import ProductList from './ProductList';

const ProductPage = ({products, heading}) => {
  const featuredProducts = products.filter(product => product.featured);
  const totalProducts = products.length;

  return (
    <div className="m-2">
      <Heading
        heading={heading}
        totalProducts={totalProducts} />

      <ProductList
        products={products} />

      <FeaturedProducts
        featuredProducts={featuredProducts} />  

    </div>
  )
}

export default ProductPage
```

Supposons également que nous utilisions le composant `ProductPage` dans le fichier `App.js` comme ceci :

```javascript

import ProductPage from "./components/compiler/ProductPage";

function App() {
  
  // Une liste de produits alimentaires    
  const foodProducts = [
    {
      "id": "001",
      "name": "Hamburger",
      "image": "🍔",
      "featured": true
    },
    {
      "id": "002",
      "name": "French Fries",
      "image": "🍟",
      "featured": false
    },
    {
      "id": "003",
      "name": "Taco",
      "image": "🌮",
      "featured": false
    },
    {
      "id": "004",
      "name": "Hot Dog",
      "image": "🌭",
      "featured": true
    }
  ];

  return (
      <ProductPage 
            products={foodProducts} 
            heading="The Food Product" />
  );
}

export default App;
```

Tout cela est très bien – alors où est le problème ? Le problème est que React re-rend proactivement le composant enfant lorsque le composant parent est re-rendu. Un rendu inutile nécessite des optimisations. Comprenons d'abord pleinement le problème.

Nous allons ajouter l'horodatage actuel dans chacun des composants enfants. Désormais, l'interface utilisateur affichée ressemblera à ceci :

![Avec horodatage](https://cdn.hashnode.com/res/hashnode/image/upload/v1724241332454/5debcdce-0349-40a3-916f-78e479668c12.png align="center")

Le grand nombre que vous voyez à côté des titres est l'horodatage (utilisant la simple fonction `Date.now()` de l'API JavaScript Date) que nous avons ajouté au code du composant. Maintenant, que se passe-t-il si nous changeons la valeur de la prop `heading` du composant `ProductPage` ?

Avant :

```xml
<ProductPage 
   products={foodProducts} 
   heading="The Food Product" />
```

Et après (remarquez que nous l'avons mis au pluriel en ajoutant un `s` à la fin de la valeur `heading`) :

```xml
<ProductPage 
   products={foodProducts} 
   heading="The Food Products" />
```

Vous remarquerez maintenant un changement immédiat dans l'interface utilisateur. Les trois horodatages ont été mis à jour. En effet, les trois composants ont été re-rendus lorsque le composant parent a été re-rendu en raison du changement de props.

![différence compilateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1724242207319/b3f2aa7e-d387-4de4-a2e6-9491f5cf7996.png align="center")

Si vous remarquez, la prop `heading` n'a été transmise qu'au composant `Heading`, et pourtant les deux autres composants enfants ont été re-rendus. C'est ici que nous avons besoin d'optimisations.

### Résoudre le problème : Sans le React Compiler

Comme discuté précédemment, React nous fournit divers hooks et API pour la `mémoïsation`. Nous pouvons utiliser `React.memo()` ou `useMemo()` pour protéger les composants qui se re-rendent inutilement.

Par exemple, nous pouvons utiliser `React.memo()` pour mémoïser le composant `ProductList` afin de garantir que, tant que la prop `products` ne change pas, le composant `ProductList` ne sera pas re-rendu.

Nous pouvons utiliser le hook `useMemo()` pour mémoïser le calcul des produits vedettes. Les deux implémentations sont indiquées dans l'image ci-dessous.

![Application de la mémoïsation](https://cdn.hashnode.com/res/hashnode/image/upload/v1724242889553/ec0d54fc-8c50-4fef-a4ea-e8c5951da9ad.png align="center")

Mais encore une fois, en nous rappelant les sages paroles de l'Oncle Ben, nous avons commencé ces dernières années à sur-utiliser ces techniques d'optimisation. Ces sur-optimisations peuvent avoir un impact négatif sur les performances de vos applications. Ainsi, la disponibilité du compilateur est une aubaine pour les développeurs React car elle leur permet de déléguer bon nombre de ces optimisations au compilateur.

Résolvons maintenant le problème en utilisant le React Compiler.

### Résoudre le problème : En utilisant le React Compiler

Encore une fois, le React Compiler est un outil de build optionnel. Il n'est pas fourni par défaut avec React 19 RC. Vous devez installer les dépendances requises et configurer le compilateur avec votre projet React 19.

Avant de configurer le compilateur, vous pouvez vérifier si votre base de code est compatible en exécutant cette commande dans le répertoire de votre projet :

```bash
npx react-compiler-healthcheck@experimental
```

Elle vérifiera et signalera :

* Combien de composants peuvent être optimisés par le compilateur
    
* Si les Règles de React sont respectées.
    
* S'il y a des bibliothèques incompatibles.
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1724300204675/d7866215-5cda-4a64-b0d6-ecedb100a428.png align="center")

Si vous constatez que tout est compatible, il est temps d'installer le plugin ESLint alimenté par le React Compiler. Ce plugin vous aidera à détecter toute violation des règles de React dans votre code. Le code non conforme sera ignoré par le React Compiler et aucune optimisation ne sera effectuée dessus.

```bash
npm install eslint-plugin-react-compiler@experimental
```

Ensuite, ouvrez le fichier de configuration ESLint (par exemple, `.eslintrc.cjs` pour Vite) et ajoutez ces configurations :

```javascript
module.exports = {
  plugins: [
    'eslint-plugin-react-compiler',
  ],
  rules: {
    'react-compiler/react-compiler': "error",
  },
}
```

Ensuite, vous utiliserez le plugin Babel pour le React Compiler afin d'activer le compilateur pour l'ensemble de votre projet. Si vous commencez un nouveau projet avec React 19, je vous recommande d'activer le React Compiler pour tout le projet. Installons le plugin Babel pour le React Compiler :

```bash
npm install babel-plugin-react-compiler@experimental
```

Une fois installé, vous devez terminer la configuration en ajoutant les options dans le fichier de config Babel. Comme nous utilisons Vite, ouvrez le fichier `vite.config.js` et remplacez le contenu par l'extrait de code suivant :

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

const ReactCompilerConfig = {/* ... */ };

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react({
    babel: {
      plugins: [
        [
          "babel-plugin-react-compiler",
           ReactCompilerConfig
          ]
        ],
    },
  })],
})
```

Ici, vous avez ajouté `babel-plugin-react-compiler` à la configuration. `ReactCompilerConfig` est nécessaire pour fournir toute configuration avancée, par exemple si vous souhaitez fournir un module de runtime personnalisé ou d'autres configurations. Dans ce cas, il s'agit d'un objet vide sans configurations avancées.

C'est tout. Vous avez fini de configurer le React Compiler avec votre base de code pour utiliser sa puissance. Désormais, le React Compiler examinera chaque composant et hook de votre projet pour tenter de lui appliquer des optimisations.

Si vous souhaitez configurer le React Compiler avec Next.js, Remix, Webpack, etc., vous pouvez [suivre ce guide](https://react.dev/learn/react-compiler#installation).

### Application React optimisée avec le React Compiler

Vous devriez maintenant avoir une application React optimisée grâce à l'inclusion du React Compiler. Effectuons donc les mêmes tests que précédemment. Modifiez à nouveau la valeur de la prop `heading` du composant `ProductPage`.

Cette fois, vous ne verrez pas les composants enfants se re-rendre. L'horodatage ne sera donc pas mis à jour non plus. Mais vous verrez la partie du composant où les données ont changé, car elle reflétera seule les modifications. De plus, vous n'aurez plus besoin d'utiliser `memo`, `useMemo()` ou `useCallback()` dans votre code.

Vous pouvez le voir fonctionner visuellement [ici](https://youtu.be/bdWUVp0TbTU?t=1326).

## Le React Compiler dans les React DevTools

Les [React DevTools](https://react.dev/learn/react-developer-tools) en version 5.0+ intègrent un support pour le React Compiler. Vous verrez un badge avec le texte `Memo ✨` à côté des composants optimisés par le React Compiler. C'est fantastique !

![React DevTools](https://cdn.hashnode.com/res/hashnode/image/upload/v1724303700810/2888b91c-bcec-4da2-88a6-840c51876d83.png align="center")

## Analyse approfondie – Comment fonctionne le React Compiler ?

Maintenant que vous avez vu comment le React Compiler fonctionne sur le code React 19, plongeons dans la compréhension de ce qui se passe en arrière-plan. Nous utiliserons le [Playground du compilateur](https://playground.react.dev/) React pour explorer le code traduit et les étapes d'optimisation.

![React Compiler Playground](https://cdn.hashnode.com/res/hashnode/image/upload/v1724740109843/a5047d83-4407-491f-8e11-6522c1381313.png align="center")

Nous utiliserons le composant `Heading` comme exemple. Copiez et collez le code suivant dans la section la plus à gauche du playground :

```javascript
const Heading = ({ heading, totalProducts }) => {
  return (
    <nav>
      <h1 className="text-2xl">
          {heading}({totalProducts}) - {Date.now()}
      </h1>
    </nav>
  )
}
```

Vous verrez que du code JavaScript est généré immédiatement dans l'onglet `_JS` du playground. Le compilateur React génère ce code JavaScript dans le cadre du processus de compilation. Passons-le en revue étape par étape :

```javascript
function anonymous_0(t0) {
  const $ = _c(4);
  const { heading, totalProducts } = t0;
  let t1;
  if ($[0] === Symbol.for("react.memo_cache_sentinel")) {
    t1 = Date.now();
    $[0] = t1;
  } else {
    t1 = $[0];
  }
  let t2;
  if ($[1] !== heading || $[2] !== totalProducts) {
    t2 = (
      <nav>
        <h1 className="text-2xl">
          {heading}({totalProducts}) - {t1}
        </h1>
      </nav>
    );
    $[1] = heading;
    $[2] = totalProducts;
    $[3] = t2;
  } else {
    t2 = $[3];
  }
  return t2;
}
```

Le compilateur utilise un hook appelé `_c()` pour créer un tableau d'éléments à mettre en cache. Dans le code ci-dessus, un tableau de quatre éléments a été créé pour mettre en cache quatre éléments.

```javascript
const $ = _c(4);
```

Mais, quelles sont les choses à mettre en cache ?

* Le composant prend deux props, `heading` et `totalProducts`. Le compilateur doit les mettre en cache. Il a donc besoin de deux éléments dans le tableau des éléments cachables.
    
* La partie `Date.now()` dans l'en-tête doit être mise en cache.
    
* Le JSX lui-même doit être mis en cache. Il n'est pas utile de calculer le JSX à moins que l'un des éléments ci-dessus ne change.
    

Il y a donc un total de quatre éléments à mettre en cache.

Le compilateur crée des blocs de mémoïsation à l'aide de `if-block`. La valeur de retour finale du compilateur est le JSX qui dépend de trois dépendances :

* La valeur de `Date.now()`.
    
* Deux props, `heading` et `totalProducts`.
    

Le JSX de sortie nécessite un nouveau calcul lorsque l'un des éléments ci-dessus change. Cela signifie que le compilateur doit créer deux blocs de mémoïsation pour chacun d'eux.

Le premier bloc de mémoïsation ressemble à ceci :

```javascript
if ($[0] === Symbol.for("react.memo_cache_sentinel")) {
    t1 = Date.now();
    $[0] = t1;
} else {
    t1 = $[0];
}
```

Le bloc if stocke la valeur de Date.now() dans le premier index du tableau cachable. Il réutilise le même à chaque fois, sauf s'il est modifié.

De même, dans le deuxième bloc de mémoïsation :

```javascript
if ($[1] !== heading || $[2] !== totalProducts) {
    t2 = (
      <nav>
        <h1 className="text-2xl">
          {heading}({totalProducts}) - {t1}
        </h1>
      </nav>
    );
    $[1] = heading;
    $[2] = totalProducts;
    $[3] = t2;
  } else {
    t2 = $[3];
  }
```

Ici, la vérification porte sur les changements de valeur des props `heading` ou `totalProducts`. Si l'une d'entre elles change, le JSX doit être recalculé. Toutes les valeurs sont ensuite stockées dans le tableau cachable. S'il n'y a pas de changement de valeur, le JSX précédemment calculé est renvoyé du cache.

Vous pouvez maintenant coller tout autre code source de composant sur le côté gauche et examiner le code JavaScript généré pour vous aider à comprendre ce qui se passe comme nous l'avons fait ci-dessus. Cela vous aidera à mieux comprendre comment le compilateur effectue les techniques de mémoïsation dans le processus de compilation.

## Comment activer ou désactiver le React Compiler ?

Une fois que vous avez configuré le React Compiler comme nous l'avons fait ici avec notre projet Vite, il est activé pour tous les composants et hooks du projet.

Mais dans certains cas, vous voudrez peut-être activer sélectivement le React Compiler. Dans ce cas, vous pouvez exécuter le compilateur en mode "opt-in" en utilisant l'option `compilationMode: "annotation"`.

```javascript
// Spécifiez l'option dans ReactCompilerConfig
const ReactCompilerConfig = {
  compilationMode: "annotation",
};
```

Annotez ensuite les composants et les hooks pour lesquels vous souhaitez activer la compilation avec la directive `"use memo"`.

```javascript
// src/ProductPage.jsx
export default function ProductPage() {
  "use memo";
  // ...
}
```

Notez qu'il existe également une directive `"use no memo"`. Il peut arriver, dans de rares cas, que votre composant ne fonctionne pas comme prévu après la compilation, et que vous souhaitiez désactiver temporairement la compilation jusqu'à ce que le problème soit identifié et résolu. Dans ce cas, vous pouvez utiliser cette directive :

```javascript
function AComponent() {
  "use no memo";
  // ...
}
```

## Pouvons-nous utiliser le React Compiler avec React 18.x ?

Il est recommandé d'utiliser le React Compiler avec React 19 car il y a des compatibilités requises. Si vous ne pouvez pas mettre à jour votre application vers React 19, vous devrez avoir une implémentation personnalisée de la fonction cache. Vous pouvez consulter [ce fil de discussion](https://github.com/reactwg/react-compiler/discussions/6) décrivant la solution de contournement.

### Dépôts à consulter

* Tout le code source utilisé dans cet article se trouve [dans ce dépôt](https://github.com/tapascript/react-compiler-lesson).
    
* Si vous voulez commencer à coder avec React 19 et ses fonctionnalités, [voici un dépôt modèle](https://github.com/atapas/code-in-react-19) configuré avec React 19 RC, Vite et TailwindCSS. N'hésitez pas à l'essayer.
    

## Et ensuite ?

Pour aller plus loin,

* Consultez la documentation officielle de React Compiler [ici](https://react.dev/learn/react-compiler).
    
* Consultez les [discussions](https://github.com/reactwg/react-compiler/discussions) au sein du Groupe de Travail.
    

Ensuite, si vous souhaitez apprendre `React` et son écosystème comme `Next.js` avec à la fois des concepts fondamentaux et des projets, j'ai une excellente nouvelle : vous pouvez [consulter cette playlist sur ma chaîne YouTube](https://www.youtube.com/watch?v=VSB2h7mVhPg&list=PLIJrr73KDmRwz_7QUvQ9Az82aDM9I8L_8) avec plus de 22 tutoriels vidéo et plus de 12 heures de contenu passionnant jusqu'à présent, gratuitement. J'espère qu'ils vous plairont également.

C'est tout pour le moment. Avez-vous aimé lire cet article et avez-vous appris quelque chose de nouveau ? Si c'est le cas, j'aimerais savoir si le contenu vous a été utile.

* Abonnez-vous à ma [chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1).
    
* [Suivez-moi sur X (Twitter)](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer votre dose quotidienne de conseils de montée en compétence.
    
* Découvrez et suivez mon travail Open Source sur [GitHub](https://github.com/atapas).
    
* Je publie régulièrement des articles pertinents sur mon [Blog GreenRoots](https://blog.greenroots.info/), vous pourriez les trouver utiles également.
    

À bientôt pour mon prochain article. D'ici là, prenez soin de vous et continuez à apprendre.