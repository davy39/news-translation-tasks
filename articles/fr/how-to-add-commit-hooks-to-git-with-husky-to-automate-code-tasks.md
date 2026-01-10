---
title: Comment ajouter des hooks de commit à Git avec Husky pour automatiser les tâches
  de code
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-10-14T15:58:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-commit-hooks-to-git-with-husky-to-automate-code-tasks
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/husky.jpg
tags:
- name: automation
  slug: automation
- name: Git
  slug: git
- name: Prettier
  slug: prettier
seo_title: Comment ajouter des hooks de commit à Git avec Husky pour automatiser les
  tâches de code
seo_desc: "There are a lot of tools to automate our code tasks. We can check for syntax\
  \ issues with ESLint and format our code with Prettier. \nBut not everyone on the\
  \ team will remember to run those commands every time they commit. How can we use\
  \ Husky to add G..."
---

Il existe de nombreux outils pour automatiser nos tâches de code. Nous pouvons vérifier les problèmes de syntaxe avec ESLint et formater notre code avec Prettier.

Mais tout le monde dans l'équipe ne se souviendra pas d'exécuter ces commandes à chaque fois qu'ils font un commit. Comment pouvons-nous utiliser Husky pour ajouter des hooks Git afin de les exécuter pour nous ?

* [Qu'est-ce que les hooks Git ?](#heading-quest-ce-que-les-hooks-git)
* [Qu'est-ce que Husky ?](#heading-quest-ce-que-husky)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Configuration d'un nouveau projet](#step-0-configuration-dun-nouveau-projet)
* [Étape 1 : Installation de Husky dans un projet](#step-1-installation-de-husky-dans-un-projet)
* [Étape 2 : Configuration de Husky pour exécuter des hooks Git](#step-2-configuration-de-husky-pour-executer-des-hooks-git)
* [Étape 3 : Utilisation de Husky pour formater le code avec Prettier](#step-3-utilisation-de-husky-pour-formater-le-code-avec-prettier)

%[https://www.youtube.com/watch?v=tuzys2b1J70]

## Qu'est-ce que les hooks Git ?

Les [hooks Git](https://git-scm.com/docs/githooks) sont des scripts que vous pouvez configurer pour [s'exécuter à certains événements](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) dans le cycle de vie de Git. Ces événements incluent différentes étapes d'un commit, comme avant un commit (pre-commit) et après un commit (post-commit).

Ces hooks sont utiles car ils permettent aux développeurs d'exécuter des tâches de code personnalisées ou même de faire respecter des standards en automatisant d'autres scripts pour exécuter ces tâches.

## Qu'est-ce que Husky ?

[Husky](https://github.com/typicode/husky) est un outil qui nous permet de gérer facilement les hooks Git et d'exécuter les scripts que nous voulons à ces étapes.

Il fonctionne en incluant un objet directement dans notre fichier `package.json` qui configure Husky pour exécuter les scripts que nous spécifions. Après cela, Husky gère le moment où nos scripts seront exécutés dans le cycle de vie de Git.

## Que allons-nous construire ?

Nous allons configurer un projet simple que nous pouvons utiliser pour tester les hooks Git.

Bien que vous devriez pouvoir suivre avec n'importe quel projet sur lequel vous travaillez, je vais utiliser [Next.js](https://nextjs.org/) comme point de départ pour ce projet, simplement parce que nous pouvons exécuter une seule commande pour démarrer un projet.

Une considération concernant ce projet est que nous allons utiliser [Prettier](https://prettier.io/) comme exemple de ce que vous pouvez faire avec les hooks Git.

Prettier est un outil qui formatera automatiquement notre code pour nous, ce qui, si vous ne vous attendez pas à ce que cela se produise, peut causer beaucoup de stress. Suivre avec moi en utilisant le projet Next.js vous permettra de tester cela sans apporter de modifications involontaires.

En ce qui concerne les tests des hooks Git, nous allons commencer par ajouter une simple instruction de ligne de commande pour voir Husky fonctionner. Mais nous allons également tester l'ajout de Prettier, qui formatera automatiquement notre code pour nous.

Enfin, au moment de la rédaction de cet article, Husky a publié une [version Alpha v5](https://typicode.github.io/husky/#/) de leur solution de hooks Git. Étant donné qu'il s'agit toujours d'une version Alpha, nous allons continuer avec [v4](https://github.com/typicode/husky/tree/v4.3.0), qui nous permet d'installer facilement Husky avec npm.

## Étape 0 : Comment configurer un nouveau projet

Comme je l'ai mentionné, vous pouvez vraiment suivre les mêmes étapes ici avec n'importe quel projet qui est géré avec un fichier `package.json`.

Next.js est absolument excessif pour ce tutoriel, mais le but est de minimiser les étapes pour se mettre en place pour travailler avec Husky.

Pour commencer avec Next.js, naviguez vers le répertoire où vous souhaitez démarrer votre projet et exécutez la commande suivante :

```
yarn create next-app my-husky-project
# ou
npx create-next-app my-husky-project

```

_Note : n'hésitez pas à remplacer `my-husky-project` par ce que vous souhaitez nommer votre répertoire._

Cela créera un nouveau dossier, créera un nouveau projet Next.js et installera toutes les dépendances.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/create-next-app.jpg)

Une fois terminé, naviguez vers ce nouveau dossier, et nous devrions être prêts à partir !

[Suivez avec le commit](https://github.com/colbyfayock/my-husky-project/commit/9e0b39c8f34c2755e074a32ef9de8d4047b68f67).

## Étape 1 : Comment installer Husky dans un projet

Pour installer Husky, nous pouvons utiliser yarn ou npm.

```
yarn add husky
# ou
npm install husky

```

_Note : si l'installation de Husky à ce stade installe v5, cela signifie que v5 a été officiellement publiée. Veuillez consulter la [documentation mise à jour de Husky](https://typicode.github.io/husky/#/) ou vous pouvez installer la dernière version v4 en spécifiant husky@4.3.0 (ou la dernière version disponible) lors de l'installation._

Une fois le package installé, nous devrions être prêts à utiliser Husky.

[Suivez avec le commit](https://github.com/colbyfayock/my-husky-project/commit/720728cd595d41c9197640bd4c48e9133bd7d956).

## Étape 2 : Comment configurer Husky pour exécuter des hooks Git

Ensuite, nous allons configurer Husky pour pouvoir l'utiliser pour nos hooks Git.

À l'intérieur de notre fichier `package.json`, créez une nouvelle propriété appelée `husky` avec un objet vide.

```json
"husky": {},
```

Vous pouvez ajouter cela où vous voulez dans le fichier `package.json`, mais je vais l'ajouter juste en dessous de la propriété `scripts` pour pouvoir les gérer plus facilement ensemble.

À l'intérieur de cela, nous voulons ajouter une autre propriété appelée `hooks` qui spécifie également un objet vide :

```json
"husky": {
  "hooks": {}
},

```

C'est ici que nous allons ajouter nos hooks Git. Husky prend en charge presque tous les [hooks Git définis par Git](https://git-scm.com/docs/githooks), donc nous pouvons être aussi flexibles que nous le souhaitons dans notre flux d'événements Git.

Pour tester cela, j'ai créé [une nouvelle branche](https://github.com/colbyfayock/my-husky-project/tree/main+test) où j'ai littéralement ajouté chaque hook Git de cette page incluant un script qui écrit simplement dans le terminal `[Husky] event name`.

_Note : ne vous sentez pas obligé de faire cela sauf si vous êtes curieux. Le but est de pouvoir vous montrer avec mon exemple comment cela fonctionne._

```
"husky": {
  "hooks": {
    "applypatch-msg": "echo \"[Husky] applypatch-msg\"",
    "pre-applypatch": "echo \"[Husky] pre-applypatch\"",
    "post-applypatch": "echo \"[Husky] post-applypatch\"",
    "pre-commit": "echo \"[Husky] pre-commit\"",

```

Ce que cela va faire, c'est dire à Husky qu'à chaque étape où nous sommes autorisés à nous connecter à Git, il nous le dira !

Lorsque je valide ce changement, nous pouvons immédiatement voir que Husky déclenche certains de nos scripts.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/husky-commit-hooks.jpg)

Ce sont tous les événements que Git nous permet de connecter et qui se produisent pendant le processus de validation.

Et de manière similaire, si je pousse ces changements vers Github, je peux voir que le processus de poussée exécute le hook `pre-push` !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/husky-push-hooks.jpg)

Vous n'utiliserez peut-être jamais la plupart des hooks que Husky et Git fournissent (nous n'en avons vu que quelques-uns entre ces deux commandes).

Mais c'est génial de pouvoir voir à quel point cela peut être puissant, que ce soit pour exécuter du code qui formate notre code, empêche les clés d'accès secrètes d'être validées, ou vraiment n'importe quoi d'autre qui peut aider à automatiser les tâches importantes de votre flux de travail.

Nous pouvons maintenant voir que nous pouvons configurer Husky en spécifiant la configuration et les hooks directement dans notre `package.json`.

[Suivez avec le commit](https://github.com/colbyfayock/my-husky-project/commit/108583a7e96564baf0fac994eafa6cf98d65d03e).

_Note : Si vous souhaitez consulter ma branche qui inclut chaque hook Git pour tester, [vous pouvez la trouver sur Github](https://github.com/colbyfayock/my-husky-project/tree/main+test)._

## Étape 3 : Comment utiliser Husky pour formater le code avec Prettier

Enfin, pour un cas d'utilisation réel, nous allons tester l'utilisation de Prettier pour formater automatiquement notre code.

Prettier est un outil de formatage de code opinionné qui vous permet de nettoyer facilement votre code pour qu'il semble avoir été écrit par une seule personne.

Pourquoi des outils comme Prettier sont-ils importants ? Lorsque vous travaillez sur du code, surtout avec une équipe, il est important de maintenir la cohérence afin que tout le monde sache à quoi s'attendre. Cela aidera à éviter les disputes sur un point-virgule lors d'une revue de code, mais cela aidera également à attraper les erreurs de syntaxe et à prévenir les bugs.

_Avertissement : l'exécution de Prettier formatera automatiquement tout votre code. Bien que nous allons tester cela avant de valider les changements, une fois que vous appliquez cela comme un hook Git, cela automatisera ce processus._

Pour commencer avec Prettier, installons-le avec notre gestionnaire de paquets :

```
yarn add prettier -D
# ou
npm install prettier --save-dev

```

_Note : nous installons Prettier comme une `devDependency` car notre application n'a pas besoin de cela pour fonctionner._

Ensuite, nous pouvons ajouter un nouveau script dans notre `package.json` qui facilitera l'exécution de Prettier pour tester cela.

À l'intérieur de la propriété `scripts`, ajoutez :

```json
"lint": "prettier --check ."

```

Pour ce premier test, nous allons l'exécuter en tant que "check" ce qui nous permettra de voir quels fichiers seraient modifiés.

Exécutez la commande suivante :

```
yarn lint
# ou 
npm run lint

```

Et une fois que nous l'avons fait, nous pouvons voir que Prettier nous indique quels fichiers seraient modifiés.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/prettier-check.jpg)

À ce stade, notre code restera inchangé. Mais si nous voulons exécuter Prettier pour de vrai afin d'apporter ces modifications, nous pouvons d'abord ajouter un script supplémentaire :

```json
"format": "prettier --write ."

```

Et si nous exécutons ce script, il mettra à jour tous ces fichiers pour formater le code selon les spécifications de Prettier.

_Avertissement : juste une autre note, l'exécution de Prettier pour écrire les modifications apportera des modifications à vos fichiers. Ce sont toutes des modifications de style de code qui ne devraient pas affecter le fonctionnement du code, mais son apparence. Avant d'exécuter le formatage, vous devriez enregistrer toutes les modifications en les validant avec Git afin de pouvoir facilement revenir en arrière si vous n'êtes pas satisfait des modifications._

Vous pouvez maintenant exécuter le script avec :

```
yarn format

```

Et nous pouvons voir que Prettier a mis à jour nos fichiers !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/prettier-write.jpg)

Maintenant, la partie pertinente pour ce tutoriel : nous pouvons ajouter cela comme un hook Git. Ainsi, lorsque quelqu'un essaie de valider du code, Prettier est exécuté avant que le code ne soit enregistré. Cela signifie que nous garderons toujours le code cohérent avec le style de formatage de Prettier.

À l'intérieur de notre configuration des hooks Husky, ajoutons :

```json
"husky": {
  "hooks": {
    "pre-commit": "prettier --write . && git add -A ."
  }
},

```

Si vous remarquez dans notre hook pre-commit, nous ajoutons également `git add -A .`.

Lorsque Husky s'exécute, il exécute simplement le script fourni. Lorsque nous exécutons notre commande Prettier, nous ne faisons que formater le code, mais nous n'enregistrons jamais ces modifications dans le cadre du processus. Nous utilisons donc `git add` pour stocker toutes ces modifications et les inclure dans le commit.

Pour tester cela, j'ai annulé les modifications de tous les fichiers qui avaient été formatés auparavant. Si vous suivez avec le même projet, vous pouvez exécuter :

```
git checkout pages

```

Ce qui réinitialisera toutes les modifications dans `pages` au dernier commit.

Maintenant, essayons d'ajouter tous nos fichiers avec Git et de valider les modifications.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/git-commit-husky-precommit-prettier.jpg)

Et une fois que nous exécutons notre commande de validation, nous pouvons voir que le hook pre-commit de Husky se déclenche déjà et formate notre code !

[Suivez avec le commit](https://github.com/colbyfayock/my-husky-project/commit/315112d062a791f20eda11f9c608c5fa794ba73e).

## Que puis-je faire ensuite ?

### Utiliser lint-staged pour n'exécuter le formatage que sur les fichiers modifiés

Nous utilisons Prettier directement dans notre hook pre-commit et spécifions `.` ce qui signifie qu'il va s'exécuter sur tous les fichiers à chaque fois.

Nous pouvons utiliser un outil appelé [lint-staged](https://github.com/okonet/lint-staged), qui nous permet toujours d'exécuter nos hooks Git avec Husky, mais il ne s'exécutera que sur les fichiers qui sont staged.

Par exemple, si nous voulions faire cela avec Husky et Prettier, notre configuration pourrait ressembler à ceci :

```
"husky": {
  "hooks": {
    "pre-commit": "lint-staged"
  }
},
"lint-staged": {
  "*": "prettier --write"
},

```

Dans le cadre de l'exécution de lint-staged, il attachera automatiquement les fichiers modifiés à la fin de notre instruction Prettier pour nous.

Vous remarquerez également que nous n'avons pas inclus `git add`. lint-staged ajoutera également automatiquement les modifications à Git pour nous.

### Configurer une configuration Prettier pour personnaliser les règles de formatage

Prettier est très opinionné. Il y a certaines choses que je ne préfère pas personnellement et vous pourriez ressentir la même chose.

Heureusement, Prettier vous permet de configurer un fichier de configuration qui peut remplacer certaines de ces règles pour rendre votre code exactement comme vous et votre équipe le souhaitez.

### Dire à Prettier d'ignorer les fichiers avec .prettierignore

Vous ne voulez probablement pas que Prettier s'exécute sur "toutes les choses" (peut-être que si).

Prettier vous permet de configurer un fichier `.prettierignore` directement à la racine du projet à côté de `package.json`, similaire à `.gitignore`, qui vous permet de dire à Prettier quels fichiers il ne doit pas exécuter.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">4e93fb Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>