---
title: Ne vous contentez pas de lint votre code - corrigez-le avec Prettier
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-11-06T15:45:00.000Z'
originalURL: https://freecodecamp.org/news/dont-just-lint-your-code-fix-it-with-prettier
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/formatting-1.jpg
tags:
- name: clean code
  slug: clean-code
- name: Code Quality
  slug: code-quality
- name: code review
  slug: code-review
- name: eslint
  slug: eslint
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: Prettier
  slug: prettier
- name: React
  slug: reactjs
seo_title: Ne vous contentez pas de lint votre code - corrigez-le avec Prettier
seo_desc: 'Linting makes our lives easier because it tells us what’s wrong with our
  code. But how can we avoid doing the actual work that goes into fixing it?

  Previously I wrote about linting, what it is, and how it makes your life easier.
  At the end, I actuall...'
---

Le linting facilite notre vie car il nous indique ce qui ne va pas dans notre code. Mais comment éviter de faire le travail réel qui consiste à le corriger ?

[Précédemment, j'ai écrit sur le linting](https://www.freecodecamp.org/news/what-is-linting-and-how-can-it-save-you-time/), ce que c'est et comment il facilite votre vie. À la fin, j'ai même inclus une méthode pour corriger automatiquement votre code. Alors pourquoi j'écris ceci ?

## **Que voulez-vous dire par "le corriger" ?**

Avant d'aller plus loin, abordons ce point rapidement. Les linters sont puissants et offrent un moyen facile de scanner votre code pour détecter les erreurs de syntaxe qui pourraient entraîner des bugs. Ou ils peuvent simplement aider à maintenir une base de code propre, saine et cohérente. Lorsqu'ils sont exécutés, ils montrent tous les problèmes et vous permettent de les corriger un par un.

En passant au niveau supérieur, certains linters vous permettent de passer un argument à la commande exécutant le linter pour qu'il corrige automatiquement les problèmes pour vous. Cela signifie que vous n'avez pas à corriger manuellement toutes ces petites erreurs d'espacement et de points-virgules (ajoutez-les ! ?) vous-même !

![Image](https://www.freecodecamp.org/news/content/images/2019/11/ron-swanson-happy.gif)
_Ron Swanson heureux_

## **Que puis-je faire de plus pour corriger les choses ?**

Si vous utilisez déjà l'option de correction, c'est un bon début. Mais il existe des outils développés spécifiquement pour résoudre ce problème au-delà d'un simple flag dans votre commande. Celui que je vais aborder est Prettier.

## **Qu'est-ce que Prettier ?**

[Prettier](https://prettier.io/) se présente comme "un formateur de code opiniâtre". Il prend en entrée votre code et le sortie dans un format cohérent en supprimant tout style de code original. Il convertit en réalité votre code en un [arbre syntaxique](https://github.com/benjamn/recast), puis le réécrit en utilisant les styles et règles que vous et Prettier fournissez ensemble via votre configuration ESLint et les règles par défaut de Prettier.

Vous pouvez facilement utiliser Prettier seul pour formater votre code, ce qui fonctionne très bien. Mais si vous combinez cela avec un processus ESLint sous-jacent, vous obtenez à la fois un linter puissant et un correcteur puissant. Je vais vous montrer comment faire fonctionner ces deux outils ensemble.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/voltron.gif)
_Voltron_

## **Prise en main de Prettier**

Pour ce guide, je vais supposer que vous avez ESLint configuré et installé dans une application. Plus particulièrement, je vais reprendre là où je m'étais arrêté dans mon précédent guide où [nous avons installé ESLint dans une application React](https://www.freecodecamp.org/news/what-is-linting-and-how-can-it-save-you-time/).

De plus, il est important de noter que Prettier nous indique dès le départ qu'il s'agit d'un formateur de code opiniâtre. Vous devez vous attendre à ce qu'il formate votre code de manière cohérente, mais peut-être différemment de ce que vous avez actuellement configuré. Mais ne vous inquiétez pas ! Vous pouvez ajuster cette configuration.

Alors, par où commençons-nous ? Nous avons déjà :

* Installé [ESLint](https://github.com/eslint/eslint)
* Ajouté [Babel](https://github.com/babel/babel-eslint) comme notre parseur
* Ajouté un [plugin](https://github.com/yannickcr/eslint-plugin-react) qui inclut les configurations React

Ensuite, commençons par installer quelques packages :

```shell
yarn add prettier prettier-eslint prettier-eslint-cli -D
```

_Note : la commande ci-dessus est similaire à l'utilisation de `npm`. Si votre projet n'utilise pas `yarn`, remplacez par `npm` si nécessaire._

Ci-dessus, nous installons :

* [prettier](https://github.com/prettier/prettier) : package et moteur principal de Prettier
* [prettier-lint](https://github.com/prettier/prettier-eslint) : transmet le résultat de Prettier à ESLint pour le corriger en utilisant votre configuration ESLint
* [prettier-eslint-cli](https://github.com/prettier/prettier-eslint-cli) : aide Prettier et ESLint à travailler ensemble sur divers fichiers de votre projet

Et nous les installons comme dépendance de développement, car nous n'en avons pas besoin en dehors du développement.

## **Configurer votre nouveau formateur**

Maintenant que nos packages sont installés, nous pouvons configurer `yarn` pour exécuter cette commande pour nous.

Précédemment, nous avons configuré un script `lint` pour qu'il ressemble à ceci dans notre `package.json` :

```json
"scripts": {
  ...
  "lint": "eslint . --ext .js"
  ...
}
```

Nous allons le laisser tel quel, mais nous allons faire quelque chose de similaire et créer un nouveau script à côté appelé `format` pour notre formateur Prettier :

```json
"scripts": {
  ...
  "format": "prettier-eslint --eslint-config-path ./.eslintrc.js --write '**/*.js'",
  "lint": "eslint . --ext .js"
  ...
}
```

Alors, que se passe-t-il là ? Nous :

* Ajoutons un nouveau script appelé `format`, que nous pouvons exécuter avec `yarn format`
* Utilisons notre package `prettier-eslint-cli` pour exécuter le formatage pour nous
* Passons notre configuration ESLint située à côté de notre `package.json` à la racine du projet (changez cela si elle se trouve à un autre endroit)
* Et enfin, nous disons à Prettier d'écrire tous les fichiers correspondant à `**/*.js`, ou tout fichier JS qu'il trouve récursivement dans notre projet

La beauté ici est que nous passons notre configuration ESLint à Prettier. Cela signifie que nous n'avons à maintenir qu'une seule configuration pour les deux outils, mais nous utilisons toujours la puissance de linting de ESLint ainsi que la puissance de formatage de Prettier.

## **Exécutez votre formateur !**

Maintenant que tout est configuré, exécutons-le ! Exécutez ce qui suit :

```
yarn format

```

et immédiatement, nous voyons que cela fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/prettier-command-line-success.png)
_Exécution réussie de Prettier_

## **Hé, mon code a l'air différent !**

![Image](https://www.freecodecamp.org/news/content/images/2019/11/spongebob-pitchforks.gif)
_Foule en colère avec des fourches_

Comme je l'ai mentionné précédemment, Prettier nous le dit clairement, c'est un formateur opiniâtre. Il est livré avec ses propres règles, un peu comme sa propre configuration ESLint, donc il apportera également ces modifications.

N'abandonnez pas votre code ! Au lieu de cela, vous pouvez examiner les modifications, voir si cela a peut-être du sens de le garder ainsi (ce sera très cohérent) ou vous pouvez mettre à jour votre configuration ESLint (`.eslintrc.js`) pour écraser les règles que vous n'aimez pas. C'est aussi un bon moyen d'apprendre peut-être de nouvelles choses que vous ne vous attendiez pas à attraper auparavant.

## **Alors, où cela nous mène-t-il ?**

Si vous avez suivi jusqu'à présent, nous avons maintenant deux commandes :

* `lint` : qui vérifie votre code et vous indique ce qui ne va pas
* `format` : qui tente automatiquement de corriger les problèmes pour vous

Lorsque vous utilisez ces commandes en pratique, votre meilleur choix est de toujours exécuter `format` en premier pour qu'il tente de corriger automatiquement tout ce qu'il peut. Ensuite, exécutez immédiatement `lint` pour attraper tout ce que Prettier n'a pas pu corriger automatiquement.

## **Qu'est-ce qui suit ?**

Maintenant que nous pouvons formater notre code automatiquement, nous devrions être capables de corriger notre code automatiquement !

![Image](https://www.freecodecamp.org/news/content/images/2019/11/fresh-off-the-boat-mind-blown.gif)
_Eddie de Fresh Off the Boat, l'esprit soufflé_

La prochaine fois, nous irons plus loin et configurerons un hook `git` qui permettra d'exécuter cela avant de faire un commit. Cela signifie que vous n'aurez plus jamais à vous soucier d'oublier d'exécuter cela à nouveau !

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? 0fe0f Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 0fe0f Inscription à ma newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine sur [https://www.colbyfayock.com/2019/11/dont-just-lint-your-code-fix-it-with-prettier/](https://www.colbyfayock.com/2019/11/dont-just-lint-your-code-fix-it-with-prettier/)_