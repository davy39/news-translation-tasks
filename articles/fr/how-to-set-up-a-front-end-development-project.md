---
title: Tutoriel JavaScript – Comment configurer un projet de développement Front End
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2025-02-12T21:44:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-front-end-development-project
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739318785959/23632d35-1d5a-4797-8c7d-fbad6c80a879.png
tags:
- name: eslint
  slug: eslint
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: Prettier
  slug: prettier
- name: Web Development
  slug: web-development
seo_title: Tutoriel JavaScript – Comment configurer un projet de développement Front
  End
seo_desc: 'Let’s say you plan to build a website. Before you start, you want to set
  up a few tools to make your life easier. But which tools should you have?

  The JavaScript ecosystem is changing so fast that it can be overwhelming to pick
  the best tools to use....'
---

Disons que vous prévoyez de créer un site web. Avant de commencer, vous souhaitez configurer quelques outils pour faciliter votre travail. Mais quels outils devriez-vous avoir ?

L'écosystème JavaScript évolue si rapidement qu'il peut être difficile de choisir les meilleurs outils à utiliser. Pour résoudre ce problème, dans cet article, je vais vous guider à travers la configuration d'un projet front-end à partir de zéro.

Nous aborderons des sujets comme les extensions d'éditeur indispensables, l'ajout de bibliothèques JavaScript à votre projet, pourquoi vous utiliserez Node.js même si vous souhaitez faire du développement front-end, et la configuration d'un bundler d'application qui générera un aperçu en direct lorsque vous coderez dans votre navigateur.

Vous pouvez également [regarder cet article sous forme de vidéo](https://www.youtube.com/watch?v=BiBjuphZQxA) sur YouTube. Commençons.

## Table des matières

1. [Comment choisir un éditeur de code](#heading-comment-choisir-un-editeur-de-code)
   
2. [Comment formater automatiquement votre code dans VS Code](#heading-comment-formater-automatiquement-votre-code-dans-vs-code)
   
3. [Pourquoi avez-vous besoin de Node pour un projet Front-End ?](#heading-pourquoi-avez-vous-besoin-de-node-pour-un-projet-front-end)
   
4. [Comment exécuter votre projet](#heading-comment-executer-votre-projet)
   
5. [Comment ajouter des bibliothèques à votre projet JavaScript](#heading-comment-ajouter-des-bibliothèques-à-votre-projet-javascript)
   
6. [Comment obtenir des conseils de codage pendant que vous codez](#heading-comment-obtenir-des-conseils-de-codage-pendant-que-vous-codez)
   
7. [Initialiser un projet avec Vite](#heading-initialiser-un-projet-avec-vite)
   
8. [Résumé](#heading-resume)
   

## **Comment choisir un éditeur de code**

Commençons par les bases. En tant que développeur web, vous modifiez principalement du texte, vous avez donc besoin d'un bon éditeur. Lequel devriez-vous utiliser ?

Le choix d'un éditeur est très subjectif, car la plupart des éditeurs ont des fonctionnalités très similaires.

Si vous n'avez pas de préférence personnelle, je vous recommande vivement [VS Code](https://vscode.dev/). Ces derniers temps, il est devenu l'éditeur de facto pour le développement web.

[![VS Code est de loin l'éditeur le plus utilisé](https://cdn.hashnode.com/res/hashnode/image/upload/v1738945424232/9f41d802-e672-4cd7-ada3-5e8d54000446.png align="center")](https://survey.stackoverflow.co/2024/technology#1-integrated-development-environment)

L'une des meilleures fonctionnalités de tous les éditeurs grand public est que vous pouvez leur ajouter des extensions. Passons en revue deux extensions indispensables.

## **Comment formater automatiquement votre code dans VS Code**

Prettier est une extension qui rend votre code plus lisible et plus cohérent.

Disons que vous avez copié-collé du code, et qu'il est difficile à lire. La tabulation est incorrecte, une ligne est trop longue, etc. Ensuite, vous enregistrez simplement le fichier, et magiquement, tout semble comme il devrait être.

![Prettier formate le code en fonction des meilleures pratiques](https://cdn.hashnode.com/res/hashnode/image/upload/v1738948709710/c64a427d-b868-4704-87db-338ebf079c67.png align="center")

C'est ce que fait Prettier. Il formate le code en fonction des meilleures pratiques. Il ne corrige pas seulement la tabulation et les retours à la ligne. Il ajoute également des parenthèses pour améliorer la lisibilité du code, s'assure que vous êtes cohérent avec les guillemets, et bien plus encore.

Pour le faire fonctionner dans VS Code, nous devons d'abord installer l'extension Prettier. Pour ce faire, allez dans le panneau des extensions dans VS Code, recherchez Prettier, puis installez-le.

![Pour installer Prettier, allez dans le panneau des extensions, recherchez Prettier et installez-le](https://cdn.hashnode.com/res/hashnode/image/upload/v1738955063143/7e8378e5-cf70-4527-9951-b822a745f4bf.png align="center")

L'installation de cette extension ne formate pas automatiquement vos fichiers à l'enregistrement par défaut. Le comportement par défaut est que, une fois cette extension installée, vous pouvez faire un clic droit dans un fichier et sélectionner **Formater le document**. Vous pouvez également sélectionner une partie d'un fichier et choisir **Formater la sélection**.

![Faites un clic droit dans un fichier et sélectionnez Formater le document pour le formater](https://cdn.hashnode.com/res/hashnode/image/upload/v1738955102891/2e55eaa7-ec2a-4aca-ad79-b1df82d31e5c.png align="center")

La première fois que vous faites cela, vous devez sélectionner le formateur par défaut. VS Code a déjà un formateur, mais il n'est pas aussi puissant que Prettier. Maintenant que vous avez deux formateurs, vous devez indiquer à VS Code que vous souhaitez utiliser Prettier pour le formatage à l'avenir.

![La première fois, vous devez sélectionner le formateur par défaut](https://cdn.hashnode.com/res/hashnode/image/upload/v1738955119781/d0ef8bc3-54d0-4428-9731-c8857171f3e7.png align="center")

Si vous souhaitez formater automatiquement vos fichiers lorsque vous les enregistrez, vous devez modifier les paramètres. Allez dans Paramètres dans vos préférences VS Code et recherchez l'option **Formater à l'enregistrement**. Par défaut, cette option est désactivée, assurez-vous donc de cocher cette case. Avec cela, Prettier formate vos fichiers à chaque fois que vous les enregistrez.

![Définissez l'option Formater à l'enregistrement dans les paramètres](https://cdn.hashnode.com/res/hashnode/image/upload/v1738955201893/fd3fbec6-5265-4c9b-adab-c1a9d524a635.png align="center")

Le formatage peut être controversé, cependant. Je recommande vivement les paramètres par défaut, surtout pour les débutants. Mais si vous préférez un style différent, vous pouvez personnaliser les choses.

Vous pouvez indiquer avec des commentaires pour [ignorer des lignes spécifiques](https://prettier.io/docs/en/ignore.html) et créer un fichier de configuration pour lister vos préférences.

Dans le dossier racine de votre projet, vous pouvez créer un fichier appelé **.prettierrc** et ajouter quelques options. Une option typique pourrait être si vous préférez les guillemets simples au lieu des guillemets doubles dans vos fichiers. Ou si vous ne voulez pas de points-virgules à la fin de vos lignes.

![Ajout d'une configuration Prettier personnalisée](https://cdn.hashnode.com/res/hashnode/image/upload/v1738955259640/d430386f-de2a-49f3-b252-aee4a9bc1089.png align="center")

Avec cette configuration, vous aurez un format différent une fois que vous enregistrez vos fichiers.

```json
{
  "singleQuote": true,
  "semi": false
}
```

Il existe bien sûr de nombreuses autres options. Si vous souhaitez approfondir, consultez la [documentation de Prettier](https://prettier.io/docs/en/configuration.html)[.](https://prettier.io/docs/en/configuration.html)

## **Pourquoi avez-vous besoin de Node pour un projet Front-End ?**

Avant d'en venir à la deuxième extension indispensable, nous devons configurer quelques autres choses. Tout d'abord, nous devons parler de Node.js. Qu'est-ce que Node, et pourquoi en avez-vous besoin même si vous travaillez en tant que développeur front-end ?

Node est souvent associé au développement backend, mais ce n'est pas son seul rôle. Node est un environnement d'exécution JavaScript – cela signifie qu'il exécute des fichiers JavaScript en dehors du navigateur.

![Vous pouvez exécuter JavaScript dans le cadre d'un site web dans votre navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1738949060189/11f39633-76a1-4c38-92ef-88846ffdeb8f.png align="center")

Il existe deux façons d'exécuter du code JavaScript. Vous pouvez soit l'avoir dans le cadre d'un site web et exécuter l'ensemble du site dans un navigateur, soit exécuter uniquement le fichier Javascript avec un environnement d'exécution comme Node.

![Vous pouvez exécuter JavaScript seul avec Node](https://cdn.hashnode.com/res/hashnode/image/upload/v1738949071655/68552f47-63ba-4cfc-9ba0-abb9218a4857.png align="center")

Dans l'exemple ci-dessous, nous avons un fichier Javascript très simple qui imprime "Hello World" dans la console. Si nous avons Node installé, nous pouvons aller dans le terminal, naviguer vers le dossier où se trouve ce fichier, puis l'exécuter avec Node comme ceci. Vous pouvez voir que le fichier a été exécuté, et le résultat est dans la console.

![Node peut exécuter des fichiers JavaScript seuls](https://cdn.hashnode.com/res/hashnode/image/upload/v1738947073105/9b56af05-e925-4cd1-9475-b3e49898dd39.png align="center")

C'est ce qu'est vraiment Node : un outil qui exécute des fichiers JavaScript seuls.

JavaScript se comporte principalement de la même manière dans les deux environnements. Mais il existe également des différences dans ce que JavaScript peut faire dans un navigateur par rapport à lorsqu'il s'exécute avec Node.

Par exemple, lorsqu'il s'exécute dans le navigateur, JavaScript peut accéder et modifier des éléments HTML. C'est le principal intérêt d'avoir JavaScript en premier lieu.

![Dans le navigateur, JavaScript peut accéder et modifier vos éléments HTML](https://cdn.hashnode.com/res/hashnode/image/upload/v1738949133299/b1c6d0a6-ba11-4659-a51e-b72e4bbfde68.png align="center")

Dans Node, il n'y a pas de fichier HTML. JavaScript s'exécute seul. En revanche, dans Node, JavaScript a accès à votre système de fichiers et peut lire et écrire vos fichiers.

![Avec Node, JavaScript peut accéder et modifier votre système de fichiers](https://cdn.hashnode.com/res/hashnode/image/upload/v1738949113586/e8702a9c-91bf-4096-8768-cf06e4e41082.png align="center")

Par exemple, vous pouvez exécuter des scripts sur votre machine pour initialiser un projet. Nous allons faire cela. Vous pouvez exécuter des vérifications sur vos fichiers et corriger automatiquement les erreurs. Ou vous pouvez exécuter vos fichiers de test.

En bref, Node vous permet d'exécuter certains outils qui facilitent grandement votre vie en tant que développeur.

Pour installer Node, allez sur [nodejs.org](http://nodejs.org) et installez-le. Si vous n'êtes pas sûr d'avoir déjà Node, vous pouvez également aller dans votre terminal et exécuter **node -v** pour vérifier. Si vous obtenez un numéro de version, vous avez Node.

![Le site web de Node.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1738949153110/c9e63db3-d52b-4122-a31c-6b871ed2e4b5.png align="center")

Alors, pourquoi les gens associent-ils principalement Node au développement backend ? Si le code backend est en JavaScript, les serveurs doivent l'exécuter d'une manière ou d'une autre sans navigateur. Donc oui, si vous êtes un développeur backend utilisant JavaScript, alors vous allez probablement utiliser Node. Mais Node est bien plus que cela.

## **Comment exécuter votre projet**

Maintenant que nous avons Node, nous pouvons utiliser un serveur en direct pour voir notre site en direct dans le navigateur pendant que nous le développons. Sans cela, vous devez actualiser manuellement la fenêtre du navigateur chaque fois que vous apportez une modification.

![Un bundler crée un package que vous pouvez exécuter dans le navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1738949223269/97bc1d15-4ab6-4204-88d6-257fa471f95d.png align="center")

Ces outils sont appelés bundlers car ils prennent tous vos fichiers et les transforment en un package soigné que vous pouvez exécuter dans le navigateur. Alors, pourquoi en avez-vous besoin ?

* Ils mettent à jour votre site en direct dans le navigateur avec le rechargement à chaud. Lorsque vous enregistrez un fichier, vous voyez immédiatement le résultat dans votre navigateur.
  
* À mesure que les outils de développement web ont évolué, le navigateur ne comprendra pas vos fichiers lorsque vous utiliserez quelque chose de plus avancé. Par exemple, utilisez-vous React ? Alors, vous utilisez la syntaxe JSX – celle qui ressemble à HTML. La syntaxe JSX ne fait pas partie de JavaScript. Vous avez besoin d'un outil pour la convertir en JavaScript simple. Sinon, elle ne s'exécutera pas dans votre navigateur. Ou utilisez-vous TypeScript ? Vous devez également le convertir en JavaScript. Ou, si vous utilisez SCSS ou un autre dialecte CSS, vous devez le convertir en CSS simple.
  
* Si vous importez des bibliothèques en utilisant le système de modules JavaScript, vous avez besoin d'un serveur en direct pour éviter les problèmes CORS dans votre navigateur.
  

C'est ce que font les bundlers. Ils s'assurent que vous pouvez utiliser des outils modernes pendant que vous développez votre application, et ils peuvent également créer une version finale de production que vous pouvez publier sur Internet.

Comment choisir un bundler ? Il existe plusieurs options, et essentiellement, elles font toutes la même chose. La différence entre elles réside dans leurs performances, leurs options de configuration et leur facilité d'utilisation.

Le bundler le plus utilisé est encore [webpack](https://webpack.js.org/), l'un des premiers bundlers dans le domaine. Mais celui qui semble avoir pris le trône et gagné de plus en plus en popularité est [Vite](https://vite.dev/). Voici un graphique de la dernière édition de l'enquête State of JavaScript.

[![Le sentiment envers WebPack et Vite](https://cdn.hashnode.com/res/hashnode/image/upload/v1738947476843/195adbd5-5aba-427e-9b00-c507542235d2.png align="center")](https://2024.stateofjs.com/en-US/libraries/#all_tools_experience)

Ce graphique montre que, bien que la plupart des développeurs aient utilisé Webpack, ils ne l'aiment pas nécessairement. En même temps, la popularité de Vite est en hausse tout en maintenant un sentiment positif.

Si vous n'avez pas encore consulté l'enquête [State of JavaScript](https://stateofjs.com/en-US), je vous recommande vivement de la parcourir. Elle vous donne un excellent aperçu des dernières tendances avec JavaScript. Vous pouvez apprendre quels outils et bibliothèques les gens aiment utiliser et lesquels ils abandonneront bientôt. Si vous vous sentez submergé par tous les changements dans l'écosystème JavaScript, les résultats de cette enquête peuvent être un excellent guide.

Une fois que nous avons un dossier pour notre projet, naviguons jusqu'à celui-ci en utilisant notre terminal. La manière la plus simple de faire cela est d'ouvrir le dossier dans VS Code, puis d'utiliser le terminal intégré. VS Code ouvrira le terminal avec le bon dossier.

Ensuite, vous pouvez exécuter le projet dans le terminal avec la commande suivante. npx est un outil en ligne de commande qui vient avec Node. C'est l'une des raisons pour lesquelles nous avons installé Node : pour pouvoir exécuter des commandes comme celle-ci.

```bash
npx vite
```

La première fois que vous exécutez ce script, il vous demandera d'installer Vite. Dites oui. Ensuite, il vous montrera l'URL d'un serveur local, que vous pouvez ouvrir dans un navigateur pour voir votre projet.

```bash
  VITE v6.1.0  ready in 162 ms

   Local:   http://localhost:5173/
   Network: use --host to expose
   press h + enter to show help
```

Maintenant, si vous mettez à jour un fichier et enregistrez les modifications, la nouvelle version apparaît immédiatement dans le navigateur. Il génère un aperçu en direct de votre site jusqu'à ce que vous arrêtiez le script ou fermiez le terminal. Vous pouvez le laisser fonctionner pendant que vous développez votre site.

Une fois que vous avez terminé, vous pouvez appuyer sur **Ctrl+C** pour arrêter le script. Si cela se désynchronise ou si vous le cassez avec une erreur, redémarrez-le en appuyant sur **Ctrl+C** pour l'arrêter et en réexécutant le même script. C'est ainsi que vous exécutez un projet avec Vite.

## **Comment ajouter des bibliothèques à votre projet JavaScript**

Maintenant que nous avons Node, nous pouvons également utiliser npm ou Note Package Manager pour ajouter des bibliothèques à notre projet. npm est un autre outil inclus avec Node. Alors, comment cela fonctionne-t-il ?

Tout d'abord, je vais vous guider à travers la configuration étape par étape de manière manuelle afin que ce soit clair comment les différentes parties s'assemblent. Ensuite, je vous montrerai comment automatiser la plupart de ces étapes.

Naviguez jusqu'à votre dossier actuel dans le terminal et exécutez la commande suivante pour initialiser le projet. Cette commande initialise un fichier package.json avec quelques métadonnées.

```bash
npm init --yes
```

À ce stade, ce fichier n'est pas très intéressant. Il contient le nom du projet, la description, le numéro de version, etc. Vous pouvez modifier ces valeurs.

Maintenant, nous pouvons ajouter des bibliothèques à notre package avec la commande npm install. Dans un [article précédent](https://www.freecodecamp.org/news/render-3d-objects-in-browser-drawing-a-box-with-threejs/), nous avons utilisé Three.js pour rendre des boîtes 3D dans le navigateur.

Alors, à titre d'exemple, installons [Three.js](https://threejs.org/). Allez à nouveau dans votre terminal, assurez-vous d'être dans le bon dossier, et exécutez la commande suivante :

```bash
npm install three
```

Cette commande installera Three.js. Mais comment savez-vous que le mot-clé est three ici, et non Three.js ?

Lorsque vous ne connaissez pas le nom du package, vous pouvez simplement rechercher npm et le nom de la bibliothèque dont vous avez besoin sur Google. Ou, si vous ne connaissez même pas le nom de la bibliothèque, vous pouvez également rechercher une bibliothèque npm 3D et voir ce que Google propose.

Nous pouvons passer en revue chaque package un par un et en choisir un en fonction de leurs capacités et d'autres informations. Ces packages viennent principalement avec des descriptions et des exemples rapides pour vous donner une idée de ce que la bibliothèque peut faire pour vous.

![Comment choisir une bibliothèque à utiliser](https://cdn.hashnode.com/res/hashnode/image/upload/v1738949563130/ce677d97-20c4-48ed-a168-b99eb01c84d4.png align="center")

Un autre indicateur que vous pourriez vouloir rechercher est le nombre de téléchargements hebdomadaires et la date de la dernière mise à jour pour vous assurer de sélectionner une bibliothèque activement maintenue que les gens utilisent encore.

Une fois que vous avez trouvé le package que vous cherchez, vous pouvez voir la commande pour l'installer en haut à droite : `npm i three`. Le `i` ici est simplement une abréviation pour install. Une autre façon d'apprendre à installer Three.js est d'aller dans sa documentation officielle et de vérifier le [guide d'installation](https://threejs.org/docs/index.html#manual/en/introduction/Installation).

![Le fichier package.json après l'initialisation du projet et l'installation de Three.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1738952468171/7a54e0bb-d88d-428b-911c-cf7a71676562.png align="center")

Lorsque nous installons un package, trois choses se produisent :

* Il ajoute la dernière version de Three.js dans notre fichier package.json en tant que dépendance du projet.
  
* Il crée également un fichier package-lock, que NPM utilise pour suivre les dépendances. Vous ne devriez jamais éditer manuellement la section des dépendances de votre fichier package.json ou le fichier package-lock. Au lieu de cela, vous devriez toujours utiliser des commandes comme npm install et uninstall pour ajouter, supprimer ou mettre à jour des packages.
  
* Enfin, le dossier node\_modules est créé. Ce dossier contient le code source de Three.js. Lorsque nous importons Three.js dans notre projet, il le recherche dans ce dossier. Le contenu de ce dossier est également quelque chose que vous ne devriez jamais changer. Vous pouvez le consulter si vous êtes intéressé par le code source de la bibliothèque que vous utilisez, mais vous ne devriez pas le modifier.
  

Si quelque chose ne va pas et que vous avez une erreur avec vos dépendances que vous ne pouvez pas résoudre, alors vous pouvez toujours supprimer en toute sécurité le dossier node\_modules et le fichier package-lock et réinstaller vos dépendances en fonction du fichier package.json. Ce n'est pas quelque chose que vous devriez faire, mais vous pouvez toujours revenir à une ardoise propre.

Maintenant que nous avons installé Three.js, nous pouvons créer un site web simple qui affiche une boîte 3D. C'est un simple fichier HTML et un fichier JavaScript avec le code pour la boîte 3D. Le point clé ici est que nous importons Three.js avec l'instruction d'importation dans le fichier JavaScript. Cette importation utilisera le package que nous venons d'installer.

![Utilisation de Three.js dans un projet d'exemple](https://cdn.hashnode.com/res/hashnode/image/upload/v1738952825715/9828ea05-e75a-4fdf-b1a3-39bd3aa8e380.png align="center")

Ensuite, nous pouvons exécuter le projet avec Vite. L'utilisation d'importations signifie que nous utilisons maintenant le système de modules. L'exécution d'un projet avec la syntaxe de module peut être un peu délicate, car le navigateur donne des erreurs CORS par défaut. Cependant, comme nous utilisons Vite pour exécuter notre projet, cela fonctionne de manière transparente sans aucune question. C'est l'une des raisons pour lesquelles nous utilisons Vite.

Si vous souhaitez en savoir plus sur la création de jeux 3D avec Three.js, consultez mon [article précédent](https://www.freecodecamp.org/news/three-js-tutorial/) sur la création d'une voiture minimaliste dans le navigateur.

## **Comment obtenir des conseils de codage pendant que vous codez**

La deuxième extension d'éditeur indispensable est ESLint. Alors que Prettier formatait le code, ESLint vous donne des conseils de codage.

Il vous aide à attraper des erreurs de base et à éviter des schémas qui peuvent causer des bugs ou être trompeurs lorsque vous essayez de comprendre le code.

Voici un exemple simple où vous déclarez une variable, mais ensuite vous avez une faute de frappe, et vous essayez d'utiliser une autre variable qui n'existe pas. ESLint vous signalera cela. Il vous donnera une erreur à la fois à la déclaration de la variable, en disant que vous avez créé une variable que vous n'utilisez pas, et ajoutera l'utilisation, en disant que vous essayez d'utiliser une variable qui n'est pas déclarée. Avec ESLint, il est facile de repérer que vous avez fait une faute de frappe.

![ESLint met en évidence les erreurs dans le code](https://cdn.hashnode.com/res/hashnode/image/upload/v1738953388793/c081f406-f964-4c4c-95ef-83cdc8e403df.png align="center")

ESLint, bien sûr, est beaucoup plus complexe que de simplement pouvoir attraper des erreurs simples. Il existe également des cas d'utilisation moins évidents où vous ne comprenez peut-être pas pourquoi ESLint se plaint. Ensuite, vous pouvez toujours cliquer sur le lien dans la fenêtre contextuelle d'erreur pour plus de détails expliquant pourquoi ce schéma est nocif et ce que vous pouvez faire pour l'éviter.

Alors, comment pouvons-nous utiliser ESLint dans nos projets ? Cette fois, nous devons avoir une extension et une configuration. Tout d'abord, comme nous l'avons fait avec Prettier, nous devons installer l'extension ESLint. Allez dans vos extensions, recherchez ESLint et installez-le.

![Pour installer ESLint, allez dans le panneau des extensions, recherchez ESLint et installez-le](https://cdn.hashnode.com/res/hashnode/image/upload/v1738953594259/a6f02e96-069d-4463-8322-86a23c523df3.png align="center")

Nous devons également configurer ESLint pour notre projet. Avant de faire cela, nous devons nous assurer que le projet a déjà un fichier package.json. Si vous n'avez pas déjà un fichier package.json, nous devons d'abord exécuter `npm init --yes` pour initialiser le projet. Ensuite, nous pouvons générer une configuration ESLint avec la commande suivante :

```bash
npm init @eslint/config@latest
```

Ce script vous posera quelques questions. En fonction de vos réponses, il personnalisera la configuration et les règles à vérifier. Pour la plupart des cas, vous pouvez utiliser l'option par défaut.

* La première fois, il demandera la permission d'installer ESLint. Dites oui.
  
* Ensuite, il vous demandera si vous souhaitez utiliser ESLint uniquement pour les vérifications de syntaxe ou pour trouver des problèmes également. Choisissez la deuxième option pour obtenir le plus d'aide de ESLint.
  
* Ensuite, sélectionnez que vous l'utiliserez avec des modules JavaScript. Les projets de développement web modernes utilisent le système de modules JavaScript. Nous utilisons des modules JavaScript si nous avons des imports et des exports dans notre code.
  
* Ensuite, il vous demandera quel framework nous utilisons. Si nous sélectionnons un framework, il ajoutera des règles spécifiques au framework à notre projet. Par exemple, l'utiliser avec React nous obligera à définir les types de props. Si nous n'utilisons pas de framework front-end, juste du JavaScript vanilla, alors sélectionnez "Aucun de ceux-ci".
  
* Ensuite, il vous demandera si le projet utilise TypeScript. Choisissez en fonction de votre préférence.
  
* Il demande où vous exécutez le code. Comme nous avons un projet front-end, sélectionnez "Navigateur".
  
* Ensuite, il vous demandera si vous souhaitez installer les dépendances supplémentaires nécessaires pour les règles basées sur vos sélections. Sélectionnez oui.
  
* Il vous demandera également quel gestionnaire de packages nous utilisons. Nous n'en avons pas beaucoup parlé, mais il existe plusieurs gestionnaires de packages que nous pouvons utiliser. Sélectionnez le défaut : npm.
  

![Installation de ESLint](https://cdn.hashnode.com/res/hashnode/image/upload/v1738953735596/a69f62ac-b5b4-459e-8e78-6956442adfe4.png align="center")

C'étaient beaucoup de questions. Voyons ce qui s'est passé après avoir exécuté cette commande.

Après cette étape, nous avons ESLint et quelques autres dépendances basées sur les réponses dans le fichier package.json en tant que dépendances de développement. Dépendance de développement signifie que ESLint ne fera pas partie du code final de votre site web, mais nous en avons besoin pendant le développement.

ESLint est également devenu partie de notre dossier node\_modules, et il y a beaucoup plus de packages ici maintenant. Cela est dû au fait qu'une dépendance peut avoir d'autres dépendances, et les dépendances des dépendances feront également partie du dossier node\_modules.

ESLint a également créé un fichier de configuration qui définit les règles en fonction de vos réponses. Nous verrons comment personnaliser les règles.

Maintenant que ESLint fonctionne, vous devriez également voir des erreurs dans le code une fois que quelque chose ne va pas. Si vous allez dans votre fichier JavaScript et essayez d'utiliser une variable non déclarée, ESLint mettra en évidence le problème.

ESLint est également hautement personnalisable. Par exemple, nous ne voulons peut-être pas marquer une variable inutilisée comme une erreur. Tout d'abord, nous allons dans la fenêtre contextuelle d'erreur et sélectionnons l'identifiant de ce type d'erreur. Ensuite, nous allons dans la configuration ESLint et remplaçons cette erreur comme suit. Ici, nous pouvons réduire la gravité à un avertissement ou désactiver complètement cette règle.

![Désactivation des règles ESLint dans la configuration](https://cdn.hashnode.com/res/hashnode/image/upload/v1738953834462/387e36f3-81ee-461c-ae02-3ca614c7b765.png align="center")

```javascript
import globals from "globals";
import pluginJs from "@eslint/js";


/** @type {import('eslint').Linter.Config[]} */
export default [
  {languageOptions: { globals: globals.browser }},
  pluginJs.configs.recommended,
  {
    rules: {
      "no-unused-vars": "off", // Désactiver la règle No Unused Variables
    }
  }
];
```

Mais si vous êtes débutant, je recommande de suivre les règles que ESLint a par défaut. Parfois, il peut être ennuyeux de corriger tous les problèmes apparemment inoffensifs, mais toutes ces règles sont basées sur les meilleures pratiques de l'industrie, il est donc bon de les suivre. Pour plus de détails, consultez la [documentation d'ESLint](https://eslint.org/docs/latest/use/configure/rules).

## Initialiser un projet avec Vite

Nous avons passé en revue le processus étape par étape de la configuration d'un projet. Nous avons utilisé **npm init** pour initialiser le projet, configuré manuellement ESLint et exécuté notre projet avec Vite. Vite peut également initialiser le projet avec une application d'exemple et tous les fichiers nécessaires, ce qui est particulièrement pratique lorsque nous configurons un projet React.

Voyons comment configurer un projet JavaScript vanilla et un projet React. Naviguons vers un dossier dans le terminal qui contiendra notre projet. Nous n'avons pas besoin de créer un dossier de projet cette fois car le script le fera pour nous. Ensuite, exécutez la commande suivante pour initialiser un projet :

```bash
npm create vite@latest
```

Cette commande vous pose quelques questions.

* Tout d'abord, elle vous demandera le nom du projet, qui sera également le nom du dossier créé comme racine du projet.
  
* Ensuite, elle vous demandera quel framework vous utilisez. Si vous n'utilisez aucun framework et souhaitez du JavaScript vanilla, choisissez "Vanilla". Si vous utilisez React, choisissez React.
  
* Ensuite, elle vous demandera si vous souhaitez utiliser TypeScript ou JavaScript. Ici, le défaut est TypeScript. Si vous êtes débutant en développement web, choisissez JavaScript. Si vous êtes plus confiant avec vos compétences, alors optez pour TypeScript. TypeScript est plus compliqué, mais il est devenu la norme de l'industrie dans le développement web, et la plupart des emplois exigent que vous le connaissiez. En tant que débutant, vous pouvez opter pour JavaScript.
  

![Création d'un projet avec Vite](https://cdn.hashnode.com/res/hashnode/image/upload/v1738953943915/884e22b0-f096-4338-a392-588b032834f4.png align="center")

Maintenant, nous pouvons naviguer vers le nouveau dossier créé et voir ce que nous avons ici. Si vous choisissez un projet JavaScript vanilla, vous pouvez voir qu'il a généré une application simple avec HTML, CSS et quelques fichiers JavaScript. Vous pouvez modifier ou même supprimer ceux-ci. Vous aurez besoin d'un fichier HTML comme point d'entrée, mais vous pouvez remplacer le reste.

![Vite peut créer une application d'exemple avec un fichier HTML, CSS et JavaScript](https://cdn.hashnode.com/res/hashnode/image/upload/v1738954107608/0234f409-6f78-4039-b5d1-133c8cd09530.png align="center")

Nous pouvons exécuter ce projet avec **npx vite** comme nous l'avons fait auparavant, mais il y a une meilleure façon. Pour un projet réel, nous voulons ajouter Vite comme une dépendance de développement pour assurer la cohérence avec la version que nous utilisons.

```json
{
  "name": "my-project",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "vite": "^6.1.0"
  }
}
```

Le fichier package.json montre que Vite a été ajouté comme une dépendance de développement. Pour utiliser cette version codée en dur, nous devons d'abord l'installer via `npm install`. Cette commande installe toutes les dépendances listées dans le fichier package.json.

```bash
npm install
```

Ce fichier package.json a maintenant également une section scripts. Cette section peut définir des scripts pour exécuter votre application localement, créer une version de production ou tester votre application. Vous pouvez les exécuter avec **npm run**. Donc, par exemple, pour exécuter l'application, vous pouvez ouvrir le terminal avec le bon dossier et exécuter la commande suivante.

```bash
npm run dev
```

Cela exécute le script étiqueté comme "dev" dans la section scripts, qui exécutera la version Vite que nous venons d'installer avec **npm install**.

Vite n'installe pas ESLint lorsque vous créez un projet vanilla, mais vous pouvez toujours l'installer manuellement, comme nous l'avons fait auparavant avec **npm init @eslint/config@latest**.

Si vous choisissez React comme framework lorsque nous initialisons le projet, nous aurons quelques fichiers supplémentaires. Par exemple, nous avons une configuration ESLint avec les paramètres recommandés pour React. Nous avons également une configuration Vite qui nous permet d'utiliser React et une application d'exemple que nous pouvons exécuter.

![Vite peut également créer un projet React pour vous](https://cdn.hashnode.com/res/hashnode/image/upload/v1738954174340/26c5a9a5-b983-4ed7-8e43-fbab4400e08b.png align="center")

Pour exécuter cette application, nous devons installer les dépendances. Donc, allons dans le terminal et exécutons `npm install`. Cela installera toutes les dépendances, y compris React. Ensuite, nous pouvons exécuter cette application avec `npm run dev`, et nous aurons une application React fonctionnelle.

## Résumé

Dans cet article, nous avons configuré et exécuté un projet front-end avec Vite. Nous avons également couvert comment trouver et ajouter des dépendances, comment avoir un formatage cohérent et automatique avec Prettier, et comment éviter les bugs avec ESLint.

Que se passe-t-il une fois que vous avez terminé de développer votre application ? Comment la téléchargez-vous sur le web et la partagez avec le monde ? C'est le sujet d'un futur article.

### **Abonnez-vous pour plus de tutoriels sur le développement web :**

%[https://www.youtube.com/watch?v=BiBjuphZQxA]