---
title: Apprenez les bases du système de modules JavaScript et construisez votre propre
  bibliothèque
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-08T17:06:32.000Z'
originalURL: https://freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TAApMtvwRDbQ3dTU4bAg7Q.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: webpack
  slug: webpack
seo_title: Apprenez les bases du système de modules JavaScript et construisez votre
  propre bibliothèque
seo_desc: 'By Kamlesh Chandnani

  Lately we all have been hearing a lot about “JavaScript Modules”. Everyone is likely
  wondering what to do with them, and how do they even play a vital role in our daily
  lives…?

  So what the heck is the JS module system? ?

  As JavaS...'
---

Par Kamlesh Chandnani

Récemment, nous avons tous beaucoup entendu parler des « Modules JavaScript ». Tout le monde se demande probablement quoi en faire et comment ils jouent un rôle vital dans notre vie quotidienne...

### **Alors, qu'est-ce que le système de modules JS ? ?**

Alors que le développement JavaScript devient de plus en plus répandu, les espaces de noms et les dépendances deviennent beaucoup plus difficiles à gérer. Différentes solutions ont été développées pour traiter ce problème sous la forme de systèmes de modules.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xM9pXLcsQa641gzCfTz0iw.jpeg)

### Pourquoi est-il important de comprendre le système de modules JS ?

Permettez-moi de vous raconter une histoire.

> Raconter des histoires est aussi fondamental pour les êtres humains que manger. Plus encore, en fait, car si la nourriture nous fait vivre, les histoires sont ce qui rend notre vie digne d'être vécue - Richard Kearney

Pourquoi est-ce que je parle de tout cela ?

Mon travail quotidien consiste à concevoir et architecturer des projets, et j'ai rapidement réalisé qu'il y avait de nombreuses fonctionnalités communes nécessaires à travers les projets. Je me suis toujours retrouvé à copier-coller ces fonctionnalités dans de nouveaux projets encore et encore.

Le problème était que chaque fois qu'un morceau de code changeait, je devais synchroniser manuellement ces changements à travers tous mes projets. Pour éviter toutes ces tâches manuelles fastidieuses, j'ai décidé d'extraire les fonctionnalités communes et de composer un package npm à partir de celles-ci. De cette façon, les autres membres de l'équipe pourraient les réutiliser comme dépendances et simplement les mettre à jour chaque fois qu'une nouvelle version était publiée.

Cette approche avait certains avantages :

* Si un changement intervenait dans la bibliothèque principale, alors un changement ne devait être fait qu'à un seul endroit sans refactoriser tout le code des applications pour la même chose.
* Toutes les applications restaient synchronisées. Chaque fois qu'un changement était fait, toutes les applications devaient simplement exécuter la commande « npm update ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*aCeYnQZBAYNdxG4mkJCGrQ.png)
_Code source de la bibliothèque_

Donc, l'étape suivante était de publier la bibliothèque. N'est-ce pas ? ?

C'était la partie la plus difficile, car il y avait un tas de choses qui me trottaient dans la tête, comme :

1. Comment rendre l'arborescence secouable ?
2. Quels systèmes de modules JS devrais-je cibler (commonjs, amd, harmony).
3. Devrais-je transpiler la source ?
4. Devrais-je bundler la source ?
5. Quels fichiers devrais-je publier ?

Chacun d'entre nous a eu ce genre de questions qui lui trottent dans la tête en créant une bibliothèque. N'est-ce pas ?

Je vais essayer de répondre à toutes les questions ci-dessus maintenant.

### Différents types de systèmes de modules JS ?

**1. CommonJS**

* Implémenté par **node**
* Utilisé pour le **côté serveur** lorsque vous avez des modules installés
* Pas de chargement de module runtime/asynchrone
* import via « **require** »
* export via « **module.exports** »
* Lorsque vous importez, vous obtenez un objet en retour
* Pas de **tree shaking**, car lorsque vous importez, vous obtenez un objet
* Pas d'analyse statique, car vous obtenez un objet, donc la recherche de propriété est à l'exécution
* Vous obtenez toujours une copie d'un objet, donc **pas de changements en direct** dans le module lui-même
* Gestion médiocre des dépendances cycliques
* Syntaxe simple

**2. AMD : Async Module Definition**

* Implémenté par **RequireJs**
* Utilisé pour le **côté client (navigateur)** lorsque vous voulez un chargement dynamique des modules
* Import via « require »
* Syntaxe complexe

**3. UMD : Universal Module Definition**

* Combinaison de **CommonJs + AMD** (c'est-à-dire, Syntaxe de CommonJs + chargement asynchrone de AMD)
* Peut être utilisé pour les environnements **AMD/CommonJs**
* UMD crée essentiellement un moyen d'utiliser l'un ou l'autre des deux, tout en supportant la définition de variable globale. En conséquence, les modules UMD sont capables de fonctionner à la fois sur le **client et le serveur**.

**4. ECMAScript Harmony (ES6)**

* Utilisé pour les côtés **serveur/client**
* **Chargement runtime/statique** des modules supporté
* Lorsque vous **importez**, vous obtenez la **valeur des liaisons** (valeur réelle)
* Import via « import » et export via « export »
* **Analyse statique** — Vous pouvez déterminer les imports et exports au moment de la compilation (statiquement) — vous n'avez qu'à regarder le code source, vous n'avez pas à l'exécuter
* **Tree shakeable**, grâce à l'**analyse statique** supportée par ES6
* Obtenez toujours une **valeur réelle** donc des changements en direct dans le module lui-même
* Meilleure gestion des dépendances cycliques que CommonJS

Maintenant, vous connaissez tout sur les différents types de systèmes de modules JS et comment ils ont évolué.

Bien que le système de modules **ES Harmony** soit supporté par tous les outils et les navigateurs modernes, nous ne savons jamais, lors de la publication de bibliothèques, comment nos utilisateurs pourraient les utiliser. Nous devons donc toujours nous assurer que nos bibliothèques fonctionnent dans tous les environnements.

Plongeons plus profondément et concevons une bibliothèque d'exemple pour répondre à toutes les questions liées à la publication d'une bibliothèque de la bonne manière.

J'ai construit une petite bibliothèque UI (vous pouvez trouver le code source sur [GitHub](https://github.com/kamleshchandnani/js-module-system)), et je vais partager toutes mes expériences et explorations pour la transpilation, le bundling et la publication.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u1HxrxTNgFJmIVMd5I-ucw.png)
_Structure du répertoire_

Ici, nous avons une petite bibliothèque UI qui contient 3 composants : Button, Card et NavBar. Transpilons et publions-la étape par étape.

### Bonnes pratiques avant la publication ?

1. **Tree Shaking ?**

* **Tree shaking** est un terme couramment utilisé dans le contexte de JavaScript pour l'élimination de code mort. Il repose sur la [structure statique](http://exploringjs.com/es6/ch_modules.html#static-module-structure) de la syntaxe des modules ES2015, c'est-à-dire, `[import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)` et `[export](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export)`. Le nom et le concept ont été popularisés par le bundler de modules ES2015 [rollup](https://github.com/rollup/rollup).
* Webpack et Rollup supportent tous deux le **Tree Shaking**, ce qui signifie que nous devons garder certaines choses à l'esprit pour que notre code soit tree shakeable.

2. **Publier toutes les variantes de modules**

* Nous devons publier toutes les variantes de modules, comme `UMD` et `ES`, car nous ne savons jamais quelles versions de navigateur/webpack nos utilisateurs pourraient utiliser pour cette bibliothèque/package.
* Même si tous les bundlers comme [**Webpack**](https://webpack.js.org) et [**Rollup**](https://rollupjs.org) comprennent les modules ES, si notre utilisateur utilise **Webpack 1.x**, alors il ne peut pas comprendre le module ES.

```
// package.json
```

```
{"name": "js-module-system","version": "0.0.1",...
```

```
"main": "dist/index.js","module": "dist/index.es.js",
```

```
...}
```

* Le champ `main` du fichier `package.json` est généralement utilisé pour pointer vers la version `UMD` de la bibliothèque/package.
* **Vous vous demandez peut-être — comment puis-je publier la version `ES` de ma bibliothèque/package ? ?**
Le champ `module` du `package.json` est utilisé pour pointer vers la version `ES` de la bibliothèque/package. Auparavant, de nombreux champs étaient utilisés comme `js:next` et `js:main`, mais `module` est maintenant standardisé et est utilisé par les bundlers comme une recherche pour la version `ES` de la bibliothèque/package.

> **Fait moins connu :** Webpack utilise [resolve.mainfields](https://webpack.js.org/configuration/resolve/#resolve-mainfields) pour déterminer quels champs dans `package.json` sont vérifiés.

> **Conseil de performance :** Essayez toujours de publier la version `ES` de votre bibliothèque/package, car tous les navigateurs modernes supportent maintenant les modules `ES`. Ainsi, vous pouvez transpiler moins, et finalement vous finirez par livrer moins de code à vos utilisateurs. Cela améliorera les performances de votre application.

**Alors, quelle est la prochaine étape ? Transpilation ou Bundling ? Quels outils devons-nous utiliser ?**

Ah, voici la partie la plus délicate ! Plongeons-nous. **?**

### Webpack vs Rollup vs Babel ?

Ce sont tous les outils que nous utilisons dans notre vie quotidienne pour livrer nos applications/bibliothèques/packages. Je ne peux pas imaginer le développement web moderne sans eux — **#_blessed_**. Par conséquent, nous ne pouvons pas les comparer, donc ce serait la mauvaise question à poser ! F645

Chaque outil a ses propres avantages et sert différents objectifs en fonction de vos besoins.

Regardons chacun de ces outils maintenant :

#### **Webpack**

[Webpack](https://webpack.js.org) est un excellent **bundler ?** largement accepté et principalement utilisé pour construire des SPAs. Il vous offre toutes les fonctionnalités prêtes à l'emploi comme le [code splitting,](https://webpack.js.org/guides/code-splitting/) le [chargement asynchrone](https://webpack.js.org/guides/code-splitting/#dynamic-imports) des bundles, le [tree shaking,](https://webpack.js.org/guides/tree-shaking/) et ainsi de suite. Il utilise le système de modules **CommonJS**.

**PS :** [Webpack-4.0.0](https://github.com/webpack/webpack/issues/6064) alpha est déjà sorti ?. Espérons qu'avec la version stable, il deviendra le bundler universel pour tous les types de systèmes de modules.

#### **RollupJS**

[Rollup](https://rollupjs.org/) est également un **bundler** similaire à Webpack. Cependant, l'avantage principal de rollup est qu'il suit le nouveau format standardisé pour les modules de code inclus dans la révision **ES6**, donc vous pouvez l'utiliser pour bundler la variante de module **ES** de votre bibliothèque/package. Il ne supporte pas le **chargement asynchrone** des bundles.

#### **Babel**

[Babel](http://babeljs.io/) est un **transpileur** pour JavaScript, surtout connu pour sa capacité à transformer le code ES6 en code qui s'exécute dans votre navigateur (ou sur votre serveur) aujourd'hui. Rappelez-vous qu'il **transpile** simplement et ne bundle pas votre code.

Mon conseil : utilisez Rollup pour les bibliothèques et Webpack pour les applications.

### Transpiler (Babel-ify) la source ou la bundler

Il y a encore une histoire derrière celle-ci. ?

J'ai passé la plupart de mon temps à essayer de trouver la réponse à cette question lorsque je construisais cette bibliothèque. J'ai commencé à fouiller dans mes node_modules pour examiner toutes les grandes bibliothèques et vérifier leurs systèmes de build.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JJ0hPQW4V7rnaCVHO0nV4w.jpeg)
_Comparaison de la sortie de build des bibliothèques vs packages_

Après avoir examiné la sortie de build pour différentes bibliothèques/packages, j'ai eu une image claire des différentes stratégies que les auteurs de ces bibliothèques ont pu avoir en tête avant la publication. Voici mes observations.

Comme vous pouvez le voir sur l'image ci-dessus, j'ai divisé ces bibliothèques/packages en deux groupes en fonction de leurs caractéristiques :

1. Bibliothèques UI (`styled-components`, `material-ui`)
2. Packages Core (`react`, `react-dom`)

Si vous êtes un bon observateur ? vous avez peut-être compris la différence entre ces deux groupes.

Les **bibliothèques UI** ont un dossier `dist` qui contient la version bundlée et minifiée pour les systèmes de modules **ES** et **UMD/CJS**. Il y a un dossier `lib` qui contient la version **transpilée** de la bibliothèque.

Les **packages Core** n'ont qu'un seul dossier qui contient la version bundlée et minifiée pour le système de modules **CJS** ou **UMD**.

**Mais pourquoi y a-t-il une différence dans la sortie de build des bibliothèques UI et des packages Core ? ?**

#### **Bibliothèques UI**

Imaginez si nous publions simplement la version bundlée de notre bibliothèque et l'hébergeons sur un CDN. Notre utilisateur l'utilisera directement dans une balise `<script/>`. Maintenant, si mon utilisateur veut utiliser uniquement le composant `<Button/>`, il doit charger toute la bibliothèque. De plus, dans un navigateur, il n'y a pas de bundler qui prendra en charge le tree shaking, et nous finirons par livrer tout le code de la bibliothèque à notre utilisateur. Nous ne voulons pas cela.

```
<script type="module">import {Button} from "https://unpkg.com/uilibrary/index.js";</script>
```

Maintenant, si nous transpilons simplement le `src` en `lib` et hébergeons le `lib` sur un CDN, nos utilisateurs peuvent réellement obtenir ce qu'ils veulent sans aucun surcoût. « Livrer moins, charger plus vite ». ✅

```
<script type="module">import {Button} from "https://unpkg.com/uilibrary/lib/button.js";</script>
```

#### **Packages Core**

Les packages Core ne sont jamais utilisés via la balise `<script/>`, car ils doivent faire partie de l'application principale. Nous pouvons donc publier en toute sécurité la version bundlée (UMD, ES) pour ces types de packages et laisser le système de build aux utilisateurs.

Par exemple, ils peuvent utiliser la variante **UMD** mais sans tree shaking, ou ils peuvent utiliser la variante **ES** si le bundler est capable d'identifier et de tirer les avantages du tree shaking.

```
// CJS requireconst Button = require("uilibrary/button");
```

```
// ES importimport {Button} from "uilibrary";
```

Mais... qu'en est-il de notre question : devons-nous **transpiler (Babelify) la source ou la bundler ? ?**

Pour la bibliothèque UI, nous devons **transpiler** la source avec **Babel** avec le système de modules `es` comme cible, et la placer dans `lib`. Nous pouvons même héberger le `lib` sur un CDN.

Nous devons **bundler** et minifier la source en utilisant **rollup** pour le système de modules `cjs/umd` et le système de modules `es` comme cible. Modifier le `package.json` pour pointer vers les systèmes cibles appropriés.

```
// package.json
```

```
{"name": "js-module-system","version": "0.0.1",...
```

```
"main": "dist/index.js",      // pour les builds umd/cjs"module": "dist/index.es.js", // pour le build es
```

```
...}
```

Pour les **packages core**, nous n'avons pas besoin de la version `lib`.

Nous devons simplement **bundler** et minifier la source en utilisant **rollup** pour le système de modules `cjs/umd` et le système de modules `es` comme cible. Modifier le `package.json` pour pointer vers les systèmes cibles appropriés, comme ci-dessus.

**Conseil** : Nous pouvons héberger le dossier `dist` sur le CDN également, pour les utilisateurs qui souhaitent télécharger toute la bibliothèque/package via la balise `<script/>`.

### Comment devons-nous construire cela ?

Nous devons avoir différents scripts pour chaque système cible dans `package.json`. Vous pouvez trouver la [configuration rollup](https://github.com/kamleshchandnani/js-module-system/blob/master/rollup.config.js) dans le dépôt GitHub.

```
// package.json
```

```
{..."scripts": {"clean": "rimraf dist","build": "run-s clean && run-p build:es build:cjs build:lib:es","build:es": "NODE_ENV=es rollup -c","build:cjs": "NODE_ENV=cjs rollup -c","build:lib:es": "BABEL_ENV=es babel src -d lib"}...}
```

### Que devons-nous publier ?

* Licence
* README
* Changelog
* Métadonnées (`main`, `module`, `bin`) — **package.json**
* Contrôle via la propriété `files` de **package.json**

Dans `package.json`, le champ `"files"` est un tableau de motifs de fichiers qui décrit les entrées à inclure lorsque votre package est installé comme une dépendance. Si vous nommez un dossier dans le tableau, il inclura également les fichiers à l'intérieur de ce dossier.

Nous inclurons les dossiers `lib` et `dist` dans le champ `"files"` dans notre cas.

```
// package.json
```

```
{..."files": ["dist", "lib"]...}
```

Enfin, la bibliothèque est prête à être publiée. Il suffit de taper la commande `npm run build` dans le terminal, et vous pouvez voir la sortie suivante. Regardez de près les dossiers `dist` et `lib`. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*C0wMVo17NTVcTroA8dPe9g.png)
_Prêt à publier ?_

### Conclusion

Wow ! Où le temps passe-t-il ? C'était une aventure folle, mais j'espère sincèrement que cela vous a donné une meilleure compréhension du système de modules JavaScript et de la manière dont vous pouvez créer votre propre bibliothèque et la publier.

Assurez-vous simplement de prendre soin des éléments suivants :

1. Rendez-le **Tree Shakeable**. ?
2. Ciblez au moins les systèmes de modules **ES Harmony** et **CJS**. ?
3. Utilisez **Babel** et **Bundlers** pour les bibliothèques. ?
4. Utilisez **Bundlers** pour les packages Core. ?
5. Définissez le champ `module` de `package.json` pour pointer vers la version **ES** de votre module (PS : Cela aide au tree shaking). ?
6. Publiez les dossiers qui contiennent les versions **transpilées** ainsi que les versions **bundlées** de votre module. ?

### Tendances de cette semaine ?

1. [Webpack-V4](https://github.com/webpack/webpack/issues/6064) alpha publié. ?
2. [ParcelJs](https://parceljs.org/) : Bundler d'applications web ultra-rapide, sans configuration. ?
3. [Turbo](https://medium.com/@ericsimons/introducing-turbo-5x-faster-than-yarn-npm-and-runs-natively-in-browser-cc2c39715403) : 5x plus rapide que Yarn & NPM, et s'exécute nativement dans le navigateur ?

_Merci à [Juho Vepsäläinen](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) et [Lakshya Ranganath](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) pour leurs critiques et commentaires, [Sean T. Larkin](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) et [Tobias Koppers](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) pour avoir partagé les insights de webpack à [ReactiveConf](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined), [Addy Osmani](https://www.freecodecamp.org/news/anatomy-of-js-module-systems-and-building-libraries-fadcd8dbd0e/undefined) pour avoir partagé le fonctionnement des différents systèmes de modules JS dans « [Writing Modular JavaScript With AMD, CommonJS & ES Harmony](https://addyosmani.com/writing-modular-js/) »._

**_P.S. Si vous aimez cela, assurez-vous de recommander (en applaudissant ? ), de [me suivre sur twitter,](https://twitter.com/_kamlesh_) et de partager cela avec vos amis ! ?_**