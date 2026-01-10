---
title: Pourquoi j'ai quitté Gulp et Grunt pour les scripts npm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-17T14:01:24.000Z'
originalURL: https://freecodecamp.org/news/why-i-left-gulp-and-grunt-for-npm-scripts-3d6853dd22b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DnSo0yGbkLsYscYR4sWOnA.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Pourquoi j'ai quitté Gulp et Grunt pour les scripts npm
seo_desc: 'By Cory House

  I know what you’re thinking. WAT?! Didn’t Gulp just kill Grunt? Why can’t we just
  be content for a few minutes here in JavaScript land? I hear ya, but…


  I’ve found Gulp and Grunt to be unnecessary abstractions. npm scripts are plenty
  po...'
---

Par Cory House

Je sais ce que vous pensez. WAT?! Gulp n'a-t-il pas tué Grunt ? Pourquoi ne pouvons-nous pas être satisfaits pendant quelques minutes ici dans le monde JavaScript ? Je vous entends, mais...

> J'ai trouvé que Gulp et Grunt étaient des abstractions inutiles. Les scripts npm sont suffisamment puissants et souvent plus faciles à vivre.

#### Commençons par un exemple...

J'étais un grand fan de Gulp. Mais sur mon dernier projet, j'ai fini avec des centaines de lignes dans mon fichier gulpfile et environ une douzaine de plugins Gulp. J'avais du mal à intégrer Webpack, Browsersync, le rechargement à chaud, Mocha et bien plus en utilisant Gulp. Pourquoi ? Eh bien, certains plugins n'avaient pas suffisamment de documentation pour mon cas d'utilisation. Certains plugins n'exposaient qu'une partie de l'API dont j'avais besoin. L'un d'eux avait un bug étrange où il ne surveillait qu'un petit nombre de fichiers. Un autre supprimait les couleurs lors de la sortie vers la ligne de commande.

Ce sont des problèmes solubles, mais **aucun de ces problèmes ne s'est produit lorsque j'ai appelé les outils directement.**

Récemment, j'ai remarqué que de nombreux projets open-source utilisent simplement des scripts npm. J'ai décidé de faire un pas en arrière et de réexaminer. Avais-je vraiment besoin de Gulp ? Il s'avère que non.

J'ai décidé d'essayer d'utiliser uniquement des scripts npm sur mon nouveau projet open-source. J'ai créé un environnement de développement riche et un processus de construction pour les applications React en utilisant uniquement des scripts npm. Curieux de voir à quoi cela ressemble ? Consultez [React Slingshot](https://github.com/coryhouse/react-slingshot). Je montre comment créer ce processus de construction en utilisant des scripts npm dans « [Building a JavaScript Development Environment](https://app.pluralsight.com/library/courses/javascript-development-environment/table-of-contents) » sur Pluralsight.

La chose surprenante est que je préfère maintenant travailler avec des scripts npm plutôt qu'avec Gulp. Voici pourquoi.

### Qu'est-ce qui ne va pas avec Gulp et Grunt ?

Avec le temps, j'ai remarqué trois problèmes principaux avec les exécuteurs de tâches comme Gulp et Grunt :

1. Dépendance aux auteurs de plugins
2. Débogage frustrant
3. Documentation disjoint

Examinons chacun de ces problèmes.

#### Problème #1 : Dépendance aux auteurs de plugins

Lorsque vous travaillez avec des technologies nouvelles ou impopulaires, aucun plugin peut ne pas exister du tout. Et lorsqu'un plugin existe, il peut être obsolète. Par exemple, Babel 6 a été récemment publié. L'API a changé de manière significative, donc de nombreux plugins Gulp étaient incompatibles avec la dernière version. En utilisant Gulp, j'étais bloqué parce que le plugin Gulp dont j'avais besoin n'était pas encore mis à jour.

Avec Gulp ou Grunt, vous devez attendre que les mainteneurs de plugins fournissent des mises à jour, ou le corriger vous-même. Cela retarde votre capacité à utiliser de nouvelles versions d'outils modernes. En revanche, **lorsque j'utilise des scripts npm, je consomme des outils directement sans une couche supplémentaire d'abstraction**. Cela signifie que lorsque de nouvelles versions de Mocha, Istanbul, Babel, Webpack, Browserify et ainsi de suite sont publiées, je suis en mesure d'utiliser les nouvelles versions immédiatement.

En termes de sélection, rien ne bat npm :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ukvg75zwIh7eZn35s8bs3g.png)
_Gulp a ~2 100 plugins. Grunt a ~5 400. npm offre plus de 227 000 packages, croissant à un rythme de 400+ par jour._

> Lorsque vous utilisez **npm scripts, vous ne cherchez pas un plugin Grunt ou Gulp. Vous choisissez parmi plus de 227 000 packages npm.**

Pour être juste, si le plugin Grunt ou Gulp dont vous avez besoin n'est pas disponible, vous pouvez certainement utiliser des packages npm directement. Mais alors vous n'utilisez plus Grunt ou Gulp pour cette tâche spécifique.

#### Problème #2 : Débogage frustrant

Lorsque les intégrations échouent, le débogage dans Grunt et Gulp peut être frustrant. Puisque vous travaillez avec une couche supplémentaire d'abstraction, il y a plus de causes potentielles pour tout bug :

1. L'outil de base est-il cassé ?
2. Le plugin Grunt/Gulp est-il cassé ?
3. Ma configuration est-elle cassée ?
4. Utilisé-je des versions incompatibles ?

L'utilisation de scripts npm élimine le #2. Et je trouve que le #3 est beaucoup moins courant puisque j'appelle généralement l'interface de ligne de commande de l'outil directement. Enfin, le #4 est moins courant puisque j'ai réduit le nombre de packages dans mon projet en utilisant npm directement au lieu d'utiliser l'abstraction d'un exécuteur de tâches.

#### Problème #3 : Documentation disjoint

La documentation pour les outils principaux dont j'ai besoin est presque toujours meilleure que celle des plugins Grunt et Gulp associés. Par exemple, si j'utilise gulp-eslint, je finis par diviser mon temps entre les [docs de gulp-eslint](https://github.com/adametry/gulp-eslint) et le site web d'ESLint. Je dois changer de contexte entre le plugin et l'outil qu'il abstrait. Le principal point de friction dans Gulp et Grunt est celui-ci :

> **Comprendre l'outil n'est pas suffisant. Gulp et Grunt vous obligent à comprendre l'abstraction du plugin.**

La plupart des outils liés à la construction offrent des interfaces de ligne de commande claires, puissantes et bien documentées. Voir les [docs sur l'interface de ligne de commande d'ESLint](http://eslint.org/docs/user-guide/command-line-interface) comme bon exemple. Je trouve que la lecture et l'implémentation d'un court appel de ligne de commande dans les scripts npm sont plus claires, moins de friction et plus faciles à déboguer (puisqu'il y a une couche d'abstraction en moins).

Maintenant que j'ai établi les points de douleur, la question est, pourquoi pensons-nous avoir besoin d'exécuteurs de tâches comme Gulp et Grunt ?

### Pourquoi avons-nous ignoré npm pour les builds ?

Je crois qu'il y a **quatre idées fausses principales** qui ont conduit à la popularité de Gulp et Grunt :

1. Les gens pensent que les scripts npm nécessitent de solides compétences en ligne de commande
2. Les gens pensent que les scripts npm ne sont pas assez puissants
3. Les gens pensent que les flux de Gulp sont nécessaires pour des builds rapides
4. Les gens pensent que les scripts npm ne s'exécutent pas sur plusieurs plateformes

Abordons ces idées fausses dans l'ordre.

#### Idée fausse #1 : Les scripts npm nécessitent de solides compétences en ligne de commande

Vous n'avez pas besoin de connaître beaucoup de choses sur la ligne de commande de votre système d'exploitation pour profiter de la puissance des scripts npm. Bien sûr, [grep, sed, awk et les pipes](http://www.tutorialspoint.com/unix/unix-useful-commands.htm) sont des compétences à vie qui valent la peine d'être apprises, mais **vous n'avez pas besoin d'être un sorcier de la ligne de commande Unix ou Windows pour utiliser les scripts npm**. Vous pouvez tirer parti des milliers de packages dans npm pour accomplir la tâche.

Par exemple, vous ne savez peut-être pas que dans Unix, cela supprime de force un répertoire : rm -rf. Ce n'est pas grave. Vous pouvez utiliser [rimraf](https://www.npmjs.com/package/rimraf) qui fait la même chose (et il fonctionne sur plusieurs plateformes). La plupart des packages npm offrent des interfaces qui supposent très peu de connaissances de la ligne de commande de votre système d'exploitation. Il suffit de rechercher des packages npm qui font ce dont vous avez besoin, de lire les docs, d'apprendre en cours de route. Je recherchais autrefois des plugins Gulp. Maintenant, je recherche des packages npm à la place. Une excellente ressource : [libraries.io](https://libraries.io).

#### Idée fausse #2 : Les scripts npm ne sont pas assez puissants

Les scripts npm sont surprenamment puissants par eux-mêmes. Il existe des hooks [pre et post basés sur des conventions](https://docs.npmjs.com/misc/scripts#description) :

```js
{
  "name": "npm-scripts-example",
  "version": "1.0.0",
  "description": "npm scripts example",
  "scripts": {
    "prebuild": "echo Je m'exécute avant le script de build",
    "build": "cross-env NODE_ENV=production webpack",
    "postbuild": "echo Je m'exécute après le script de build"
  }
}
```

Tout ce que vous faites est de suivre la convention. Les scripts ci-dessus s'exécuteront dans l'ordre en fonction de leur préfixe. Le script prebuild s'exécutera avant le script build car il a le même nom, mais est préfixé avec « pre ». Le script postbuild s'exécutera après le script build car il a le préfixe « post ». Donc si je crée des scripts nommés prebuild, build et postbuild, ils s'exécuteront automatiquement dans cet ordre lorsque je tape `npm run build`.

Vous pouvez également décomposer de gros problèmes en appelant un script depuis un autre :

```js
{
  "name": "npm-scripts-example",
  "version": "1.0.0",
  "description": "npm scripts example",
  "scripts": {
    "clean": "rimraf ./dist && mkdir dist",
    "prebuild": "npm run clean",
    "build": "cross-env NODE_ENV=production webpack"
  }
}
```

Dans cet exemple, la tâche prebuild appelle la tâche clean. Cela vous permet de décomposer vos scripts en petits, bien nommés, à responsabilité unique, en une seule ligne.

Vous pouvez appeler plusieurs scripts en série sur une seule ligne en utilisant &&. Les scripts dans l'étape clean ci-dessus s'exécuteront les uns après les autres. Cette simplicité vous fera vraiment sourire si vous êtes quelqu'un qui a eu du mal à faire exécuter une liste de tâches dans l'ordre dans Gulp.

Et si une commande devient trop compliquée, vous pouvez toujours appeler un fichier séparé :

```js
{
  "name": "npm-scripts-example",
  "version": "1.0.0",
  "description": "npm scripts example",
  "scripts": {
    "build": "node build.js"
  }
}
```

J'appelle un script séparé dans la tâche build ci-dessus. Ce script sera exécuté par Node et pourra ainsi utiliser tous les packages npm dont j'ai besoin, et utiliser toute la puissance de JavaScript à l'intérieur.

Je pourrais continuer, mais [les fonctionnalités principales sont documentées ici](https://docs.npmjs.com/misc/scripts). De plus, il y a aussi un court [cours Pluralsight sur l'utilisation de npm comme outil de build](https://www.pluralsight.com/courses/npm-build-tool-introduction). Ou, consultez [React Slingshot](https://github.com/coryhouse/react-slingshot) pour un exemple de tout cela en action.

#### Idée fausse #3 : Les flux de Gulp sont nécessaires pour des builds rapides

Gulp a rapidement gagné du terrain sur Grunt parce que les flux en mémoire de Gulp sont plus rapides que l'approche basée sur les fichiers de Grunt. Mais vous n'avez pas besoin de Gulp pour profiter de la puissance du streaming. En fait, **le streaming a toujours été intégré aux lignes de commande Unix et Windows**. L'opérateur pipe (|) diffuse la sortie d'une commande vers l'entrée d'une autre commande. Et l'opérateur de redirection (>) redirige la sortie vers un fichier.

Ainsi, par exemple, dans Unix, je peux utiliser `grep` le contenu d'un fichier et rediriger la sortie vers un nouveau fichier :

```
grep 'Cory House' bigFile.txt > linesThatHaveMyName.txt
```

**Le travail ci-dessus est diffusé. Aucun fichier intermédiaire n'est écrit.** (Vous vous demandez comment faire la commande ci-dessus de manière multiplateforme ? Lisez la suite...)

Vous pouvez également utiliser l'opérateur `&` pour exécuter deux commandes en même temps sur Unix :

```
npm run script1.js & npm run script2.js
```

Les deux scripts ci-dessus s'exécuteront en même temps. Pour exécuter des scripts simultanément sur plusieurs plateformes, utilisez [npm-run-all](https://www.npmjs.com/package/npm-run-all). Cela conduit à l'idée fausse suivante...

#### Idée fausse #4 : Les scripts npm ne s'exécutent pas sur plusieurs plateformes

De nombreux projets sont liés à un système d'exploitation spécifique, donc les préoccupations multiplateformes n'ont pas d'importance. Mais si vous avez besoin de fonctionner sur plusieurs plateformes, les scripts npm peuvent encore bien fonctionner. D'innombrables projets open-source en sont la preuve. Voici comment.

La ligne de commande de votre système d'exploitation exécute vos scripts npm. Ainsi, sur Linux et OSX, vos scripts npm s'exécutent sur une ligne de commande Unix. Sur Windows, les scripts npm s'exécutent sur la ligne de commande Windows. Ainsi, si vous voulez que vos scripts de build s'exécutent sur toutes les plateformes, vous devez satisfaire à la fois Unix et Windows. Voici trois approches :

**Approche 1 :** Utilisez [des commandes qui s'exécutent sur plusieurs plateformes](http://www.yolinux.com/TUTORIALS/unix_for_dos_users.html). Il y a un nombre surprenant de commandes multiplateformes. En voici quelques-unes :

```
&& enchaîner les tâches (Exécuter une tâche après une autre)
< contenu du fichier d'entrée vers une commande
> rediriger la sortie de la commande vers un fichier
| rediriger la sortie de la commande vers une autre commande
```

**Approche 2 :** Utilisez des packages node. Vous pouvez utiliser des packages node au lieu de commandes shell. Par exemple, utilisez [rimraf](https://www.npmjs.com/package/rimraf) au lieu de `rm -rf`. Utilisez [cross-env](https://www.npmjs.com/package/cross-env) pour définir des variables d'environnement de manière multiplateforme. Recherchez sur Google, npm ou [libraries.io](https://libraries.io) ce que vous voulez faire et il y a presque certainement un package node qui le fera de manière multiplateforme. Et si vos appels de ligne de commande deviennent trop longs, vous pouvez également appeler des packages Node dans des scripts séparés comme ceci :

```
node scriptName.js
```

Le script ci-dessus est du bon vieux JavaScript, exécuté par Node. Et puisque vous appelez simplement un script sur la ligne de commande, vous n'êtes pas limité aux fichiers .js. Vous pouvez exécuter n'importe quel script que votre système d'exploitation peut exécuter, comme Bash, Python, Ruby ou Powershell.

**Approche 3 :** Utilisez [ShellJS](https://www.npmjs.com/package/shelljs). ShellJS est un package npm qui exécute des commandes Unix via Node. Cela vous donne le pouvoir d'exécuter des commandes Unix sur toutes les plateformes, y compris Windows.

J'ai utilisé une combinaison des approches #1 et #2 sur [React Slingshot](https://github.com/coryhouse/react-slingshot).

### Point de douleur

Il y a admis quelques inconvénients : La spécification JSON ne supporte pas les commentaires, donc vous ne pouvez pas ajouter de commentaires dans package.json. Il y a quelques moyens de contourner cette limitation :

1. Écrire de petits scripts, bien nommés, à responsabilité unique
2. Documenter les scripts séparément (dans un README.md par exemple)
3. Appeler un fichier .js séparé

Je préfère l'option #1. Si vous décomposez chaque script pour qu'il ait une responsabilité unique, les commentaires sont rarement nécessaires. **Le nom du script devrait décrire pleinement l'intention, tout comme toute petite fonction bien nommée.** Comme je le discute dans « [Clean Code: Writing Code for Humans](https://www.pluralsight.com/courses/writing-clean-code-humans) », les petites fonctions à responsabilité unique nécessitent rarement des commentaires. Lorsque je sens qu'un commentaire est nécessaire, j'utilise l'option #3 et je déplace le script vers un fichier séparé. Cela me donne toute la puissance compositionnelle de JavaScript lorsque j'en ai besoin.

Package.json ne supporte pas non plus les variables. Cela semble être un gros problème, mais ce n'est pas le cas pour deux raisons. Premièrement, le besoin le plus courant de variables tourne autour de l'environnement, que vous pouvez définir sur la ligne de commande. Deuxièmement, si vous avez besoin de variables pour d'autres raisons, vous pouvez appeler un fichier .js séparé. Consultez [React-starter-kit](https://github.com/kriasoft/react-starter-kit/blob/master/package.json#L74) pour un exemple élégant de ce modèle.

Enfin, il y a aussi un risque de créer de longs arguments de ligne de commande complexes qui sont difficiles à comprendre. Les revues de code et le refactoring diligent sont un excellent moyen de s'assurer que les scripts npm sont décomposés en petites fonctions bien nommées, à responsabilité unique, que tout le monde comprend. Si c'est suffisamment complexe pour nécessiter un commentaire, vous devriez probablement refactoriser le script unique en plusieurs scripts bien nommés ou l'extraire dans un fichier séparé.

#### Les abstractions doivent être justifiées

Gulp et Grunt sont des abstractions sur les outils que j'utilise. Les abstractions sont utiles, mais les abstractions ont un coût. Elles fuient. Elles nous rendent dépendants des mainteneurs de plugins et de leur documentation. Et elles ajoutent de la complexité en augmentant le nombre de dépendances. J'ai décidé que les exécuteurs de tâches comme Gulp et Grunt sont des abstractions dont je n'ai plus besoin.

Vous cherchez des détails ? Je montre comment créer un processus de build en utilisant des scripts npm à partir de zéro dans « [Building a JavaScript Development Environment](https://app.pluralsight.com/library/courses/javascript-development-environment/table-of-contents) » sur Pluralsight.

Des commentaires ? Faites-vous entendre ci-dessous ou sur [Reddit](https://www.reddit.com/r/javascript/comments/41e1ys/why_i_left_gulp_and_grunt_for_npm_scripts/) ou [Hacker News](https://news.ycombinator.com/item?id=10929476).

Enfin, je suis loin d'être la première personne à suggérer cela. Voici quelques excellents liens :

* [Task automation with npm run](http://substack.net/task_automation_with_npm_run) — James Holliday
* [Advanced front-end automation with npm scripts](https://www.youtube.com/watch?v=0RYETb9YVrk) — Kate Hudson
* [How to use npm as a build tool](http://blog.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/) — Kieth Cirkel
* [Introduction to npm as a Build Tool](http://app.pluralsight.com/courses/npm-build-tool-introduction) — Marcus Hammarberg
* [Gulp is awesome, but do we really need it?](http://gon.to/2015/02/26/gulp-is-awesome-but-do-we-really-need-it/) — Gonto
* [NPM Scripts for Build Tooling](http://code.tutsplus.com/courses/npm-scripts-for-build-tooling) — Andrew Burgess

**_Cory House_** est l'auteur de « [React and Redux in ES6](https://pluralsight.com/courses/react-redux-react-router-es6) », « [Clean Code: Writing Code for Humans](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiK1pXx89nJAhUujoMKHeuWAEUQFggcMAA&url=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwriting-clean-code-humans&usg=AFQjCNEBfkBoN-IgCn_1jFUqWDAUIxcmAw&sig2=Ub9Wup4k4mrw_ffPgYu3tA) » et [de plusieurs autres cours sur Pluralsight](https://app.pluralsight.com/profile/author/cory-house). Il est architecte logiciel chez VinSolutions et [forme des développeurs de logiciels à l'international](http://www.bitnative.com/training/) sur des pratiques logicielles comme le développement front-end et le codage propre. Cory est un MVP Microsoft, un expert développeur Telerik et le fondateur de [outlierdeveloper.com](http://www.outlierdeveloper.com).