---
title: Apprendre à utiliser Rekit Studio dans un projet React existant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-24T05:38:33.000Z'
originalURL: https://freecodecamp.org/news/using-rekit-studio-in-an-existing-react-project-39713d9667b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KM9q-edu91s_DYXDFivGlQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprendre à utiliser Rekit Studio dans un projet React existant
seo_desc: 'By Nate Wang

  I introduced Rekit Studio in the last article, and since then many people have been
  interested in using it in an existing React project. This article will introduce
  how to do that. To learn how to migrate is really just to learn how Reki...'
---

Par Nate Wang

J'ai présenté [Rekit Studio](https://github.com/supnate/rekit) dans le [dernier article](https://medium.com/@nate_wang/introducing-rekit-studio-a-real-ide-for-react-and-redux-development-baf0c99cb542), et depuis, beaucoup de gens se sont intéressés à l'utiliser dans un projet React existant. Cet article expliquera comment faire cela. Apprendre à migrer, c'est vraiment apprendre comment Rekit fonctionne. Donc, ce n'est pas seulement un guide pour la migration, mais aussi une introduction à la façon dont Rekit fonctionne.

Il est en fait préférable de penser à ajouter Rekit Studio aux projets existants plutôt qu'à les migrer, car vous n'avez pas besoin de refactoriser tout votre code existant vers Rekit en une seule fois. Vous pouvez écrire un nouveau code avec Rekit et laisser l'ancien code tel quel — votre projet ne sera pas cassé. Ensuite, vous pouvez refactoriser l'ancien code à tout moment plus tard si nécessaire. Peut-être souhaitez-vous voir un diagramme de dépendances complet ou modifier un ancien composant avec Rekit Studio.

Nous prendrons [l'implémentation TodoMVC de Redux](https://github.com/reactjs/redux/tree/master/examples/todomvc) comme exemple, vous devrez donc peut-être consulter son [code source](https://github.com/reactjs/redux/tree/master/examples/todomvc) d'abord. Il est créé par [create-react-app](https://github.com/facebook/create-react-app), qui est un modèle officiel et très populaire pour React. Si votre projet est également créé par ce modèle, cet article sera plus utile.

#### Prérequis

Il n'y a que trois prérequis pour que votre projet utilise Rekit :

1. React v0.14+
2. Redux
3. Modules ES6

Pour pouvoir migrer, le projet doit être basé sur React et Redux. Peu importe si votre projet n'utilise pas React Router. Mais vous aurez peut-être besoin d'un adaptateur pour consommer l'API JSON de React Router, car Rekit l'utilise comme configuration de routage. Cela permet à Rekit de savoir comment créer/mettre à jour/supprimer et afficher les règles de routage.

Rekit utilise [Babylon](https://github.com/babel/babylon), le parseur utilisé par Babel, pour analyser les modules ES6 pour le refactoring et les diagrammes de dépendances. Il ne supporte donc pas les projets TypeScript ou Flow pour l'instant.

### 1. Installer rekit-core et rekit-studio

À la fois Rekit Studio et [Rekit CLI](http://rekit.js.org/docs/cli.html) utilisent `[rekit-core](http://rekit.js.org/docs/core.html)` pour gérer les éléments du projet. Installez-les d'abord dans votre projet :

```
yarn add rekit-core rekit-studio --dev
```

Ou avec npm :

```
npm install rekit-core rekit-studio --save-dev
```

### 2. Copier la structure de dossiers/fichiers de Rekit dans votre projet

Les projets Rekit ont une structure de dossiers spéciale. Pour la créer rapidement pour votre projet, créez une application Rekit propre et copiez les dossiers/fichiers dans votre projet.

```
npm install rekit --globalrekit create my-app --clean
```

Copiez ensuite ces deux dossiers dans votre projet :

* src/
* tools/

Gardez à l'esprit qu'il y aura des conflits avec les vôtres : pour les dossiers, fusionnez-les simplement. Pour les fichiers, ne remplacez aucun de vos fichiers et souvenez-vous de ceux qui ont des conflits — puis fusionnez-les ou renommez-les manuellement (je l'expliquerai plus tard).

### 3. Démarrer Rekit Studio

Rekit utilise le script sous `tools/server.js` pour démarrer les serveurs de développement et Rekit Studio. Pour un projet existant, vous devriez déjà avoir votre propre script pour le serveur de développement et la construction. Nous devons donc les fusionner.

Il y a 4 fonctions dans le fichier server.js de Rekit :

* **startDevServer** : lit la configuration de webpack et démarre le serveur de développement webpack.
* **buildDevDll** : construit les bibliothèques tierces dans un Dll pour améliorer les performances de Webpack pour le développement en utilisant le [plugin Dll de Webpack](https://webpack.js.org/plugins/dll-plugin/).
* **startStudioServer** : démarre un serveur [Express](https://expressjs.com/) avec le middleware Rekit Studio
* **startBuildServer** : démarre un serveur Express pour vérifier le bundle construit.

Vous pouvez soit modifier server.js pour démarrer votre serveur de développement, soit modifier votre propre script `npm start` en copiant la fonction startStudioServer pour démarrer Rekit Studio.

Pour l'exemple TodoMVC de Redux, le script qui démarre le serveur de développement est `scripts/start.js`, nous le modifions en ajoutant le code suivant à la fin pour démarrer Rekit Studio :

Alternativement, vous pouvez également enregistrer le script ci-dessus sous un fichier séparé comme `start_rekit_studio.js`, puis l'exécuter avec node, plutôt que de l'insérer dans votre script existant.

Ensuite, nous devons ajouter les dépendances nécessaires si elles ne sont pas encore installées :

```
yarn add express express-history-api-fallback --dev
```

Ou avec npm :

```
npm install express express-history-api-fallback --save-dev
```

Et configurer le port de Rekit Studio dans package.json :

```
{   ...   "rekit": { "studioPort": 6090 },   ...}
```

Notez que la propriété "rekit" dans package.json est nécessaire car Rekit l'utilise pour détecter un projet Rekit.

C'est tout. Vous pouvez ensuite démarrer Rekit Studio avec `npm start` (en supposant que vous démarrez Studio dans votre script npm start) ! Accédez à [http://localhost:6090](http://localhost:6090) pour y accéder. Et l'application TodoMVC elle-même fonctionne également. Accédez toujours à [http://localhost:3000](http://localhost:3000) pour l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZuNccZ60bvzNHKaF59ai7g.png)

Nous n'avons rien changé, mais Rekit Studio fonctionne maintenant en arrière-plan.

### Commencez à utiliser Rekit Studio pour écrire du code !

Une fois Rekit Studio démarré, vous pouvez l'utiliser pour écrire du code. N'oubliez pas que Rekit aide simplement à écrire du code React et Redux standard, vous pouvez donc l'utiliser sans aucune limitation dans votre projet. Par exemple, créons un composant `HelloRekit` sous la fonctionnalité d'accueil avec Rekit Studio et modifions le texte par défaut en "Hello Rekit !"

![Image](https://cdn-media-1.freecodecamp.org/images/1*yqaZFzt5UQSqokO2kVUZzQ.png)

Nous avons maintenant un composant React : `src/features/home/HelloRekit.js`. Ensuite, utilisez-le dans l'application TodoMVC en modifiant `src/containers/App.js`, qui est le composant racine de l'application. Vous pouvez le trouver dans le dossier `others` dans Rekit Studio. Ouvrez-le et ajoutez seulement 2 lignes de code :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5qEEwSVZ4O46SPzQJqVgFQ.png)

Enregistrez le fichier, et vous pouvez même voir le diagramme de dépendances bien que `App.js` n'ait pas été créé par Rekit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5t_u4z7gPZ_dsviwFujNSg.png)

Une chose à garder à l'esprit est que lors de l'importation d'un module, vous devez utiliser le chemin physique plutôt que le chemin logique affiché dans l'explorateur de projet.

Ensuite, ouvrez l'application TodoMVC, et vous pouvez voir que le composant HelloRekit a été affiché :

![Image](https://cdn-media-1.freecodecamp.org/images/1*IQ4Qp_ye31k6cv4pDJJ9bA.png)

Bien que ce ne soit pas très beau, puisque nous n'avons pas encore ajouté de style, cela fonctionne bien !

### Intégration des styles

Maintenant, intégrons les styles gérés par Rekit dans votre projet. Pour l'instant, Rekit ne supporte que [Less](http://lesscss.org/) ou [Sass](https://sass-lang.com/) comme transpileur CSS. Vous devez configurer votre bundler (Webpack, Rollup, etc.) pour le supporter : prenons Less et Webpack, par exemple, et ajoutons `src/styles/index.less` à l'entrée dans `config/webpack.config.dev.js` :

```
entry: [  ...,  'src/styles/index.less',  ...],
```

Notez que Rekit utilise certains styles par défaut dans `src/styles/reset.css` qui ne doivent pas être utilisés pour les projets existants. Supprimez simplement cette ligne `@import` dans `src/styles/index.less`.

Ensuite, ajoutez le chargeur Less à la configuration sous `oneOf` pour l'application TodoMVC. Cela pourrait être inutile si votre projet utilise déjà Less.

```
{  test: /\.less$/,  loader: 'style-loader!css-loader!less-loader'}
```

Installez Less et Less-loader si nécessaire :

```
yarn add less@2.3.1 less-loader --dev
```

Notez que Less-loader est maintenant uniquement compatible avec Less @2.3.1 et non avec la dernière version 3.0.1.

Toute la configuration pour le style est terminée, alors maintenant ajoutons un peu de style au composant HelloRekit et voyons le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*azHx8UmKcr7Bgdo9xu1AJg.png)

Nous pouvons voir que le style géré par Rekit a été utilisé par le projet existant.

### Intégration de Redux

Ensuite, intégrons le code Redux existant à Rekit. Chaque application Redux a un réducteur racine. La clé est de fusionner le réducteur de Rekit avec celui existant. C'est super facile ! Pour l'application TodoMVC, importez simplement `src/reducers/todos.js` dans le réducteur racine de Rekit `src/common/rootReducer.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oHfUeL5-iEab74Wul0KDtQ.png)

Ensuite, utilisez ce réducteur racine dans l'application TodoMVC en modifiant `src/index.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*afaFngPnqsaQOgFbsacnYg.png)

Ok, vous pouvez utiliser Rekit pour gérer de nouvelles actions et réducteurs Redux. Maintenant, créez une action avec Rekit par vous-même et essayez-la !

### Intégration de React Router

Comme mentionné ci-dessus, Rekit gère les règles de routage au format JSON. Le fichier de configuration de route racine est `src/common/routeConfig.js` qui charge les règles de route depuis chaque fonctionnalité `src/features/<feature-name>/route.js`. Lorsque vous créez un composant avec un chemin d'URL, Rekit met à jour le fichier `route.js` pour insérer une règle de routage.

Il n'est donc pas nécessaire d'utiliser React Router — vous pouvez utiliser n'importe quelle bibliothèque de routage qui peut consommer les règles définies par l'API JSON. Dans une application Rekit, `src/Root.js` est l'endroit où les règles JSON sont traitées pour générer des déclarations React Router v4 en JSX.

Puisque l'application TodoMVC n'utilise pas de routeur, nous utilisons simplement la méthode par défaut de Rekit. Installez d'abord `react-router-dom` et `react-router-redux` dans votre projet si ce n'est pas déjà fait :

```
yarn add react-router-dom react-router-redux@next --dev
```

Ensuite, vous devez modifier deux fichiers de l'application TodoMVC :

1. Mettez à jour `src/index.js` pour rendre Root.js au lieu de `src/containers/App.js`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zakEz2hEGtwOCbWFPIuelA.png)

Notez que Root.js a utilisé Provider de `react-redux` pour un composant, il n'est donc plus nécessaire dans index.js.

2. Mettez à jour `src/features/home/route.js` pour ajouter une règle qui correspond à un chemin d'URL vers le composant TodoMVC `src/containers/App.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*eDC6NFMuABAgZCXZmJ1wfQ.png)

Vous n'avez pas besoin d'ajouter des règles à home's route.js. Cela pourrait appartenir à n'importe quelle fonctionnalité, même à root routeConfig.js.

Maintenant, vous pouvez accéder à TodoApp par cette URL : [http://localhost:3000/todos](http://localhost:3000/todos). Nous pouvons voir que le composant conteneur App.js de TodoMVC est maintenant géré par React Router.

Nous avons terminé la migration de React Router. Ce n'était que le code d'exemple de TodoMVC. Pour votre application, l'approche est similaire. Si vous utilisez également React Router v4, utilisez simplement Root.js — sinon, écrivez votre propre adaptateur pour consommer le JSON de configuration de routage de Rekit.

### Tests unitaires

Rekit Studio utilise le script `tools/run_test.js` pour exécuter les tests unitaires par motif de fichier de test, vous ne devez donc pas le renommer ou le déplacer. Par exemple, utilisez cette commande pour tester la fonctionnalité home :

```
node run_test.js features/home/**/*.test.js
```

Le script utilise [Mocha](https://mochajs.org/) pour exécuter les tests et [nyc](https://github.com/istanbuljs/nyc) pour générer un rapport de couverture de test. Si vous utilisez d'autres frameworks de test, comme [Jest](https://facebook.github.io/jest/), modifiez ce script pour exécuter les tests pour le vôtre.

### Build

Rekit Studio utilise le script `tools/build.js` pour construire le projet. Vous ne devez donc pas le renommer ou le déplacer. Tout ce que vous avez à faire est de mettre votre script de construction à l'intérieur de ce script afin de pouvoir commencer la construction via l'interface graphique de Rekit Studio.

### Configuration de Rekit terminée

Pour l'instant, nous avons ajouté Rekit à un projet existant. Cela signifie que vous pouvez commencer à écrire un nouveau code avec Rekit Studio et laisser l'ancien code tel quel. Le projet devrait toujours fonctionner comme avant.

Mais comme je l'ai mentionné ci-dessus, nous devons peut-être refactoriser l'ancien code afin qu'il puisse être géré par Rekit. Ensuite, voyons comment faire la migration.

### Penser en fonctionnalités

L'une des capacités clés de Rekit est de diviser une application compliquée en fonctionnalités faiblement couplées. Une fonctionnalité est un concept de haut niveau, et j'ai déjà introduit l'architecture [ici](https://medium.com/@nate_wang/feature-oriented-architecture-for-web-applications-2b48e358afb0). Pour votre application, vous devriez également envisager de créer des fonctionnalités pour gérer le code existant plutôt que de mettre tout le code dans une seule fonctionnalité.

### Migration des composants

Chaque composant se compose de trois fichiers :

1. Component.js : doit toujours être placé directement sous un dossier de fonctionnalité : `src/features/<feature-name>/Component.js`
2. Component.less/scss : doit toujours être placé directement sous un dossier de fonctionnalité : `src/features/<feature-name>/Component.less`
3. Component.test.js : doit être dans le dossier des tests : `tests/features/<feature-name>/Component.test.js`

La position des fichiers et le modèle de nommage doivent suivre les conventions de Rekit décrites [ici](http://rekit.js.org/docs/namings.html) afin que Rekit puisse les refactoriser si nécessaire. Rekit détecte un composant en vérifiant si un module sous le dossier de fonctionnalité importe React.

Le nœud DOM racine de chaque composant doit avoir un nom de classe CSS unique. Dans Rekit, le modèle est `<feature-name>-<component-name>`. Il est toujours en kebab case en utilisant la fonction [_.kebabCase](https://lodash.com/docs/4.17.5#kebabCase) de lodash. Ce nom de classe sera automatiquement mis à jour lorsque vous renommerez un composant avec Rekit.

En gardant ces règles à l'esprit, vous pouvez déplacer votre composant vers un dossier de fonctionnalité. Ensuite, Rekit Studio peut le charger dans l'explorateur de projet et l'éditer avec l'éditeur d'éléments (avec des onglets pour différentes parties d'un composant).

Vous pouvez vérifier le résultat final [ici](https://github.com/supnate/rekit-todomvc) pour voir comment Rekit organise les composants pour l'application TodoMVC.

### Migration des actions et des réducteurs

Rekit utilise une approche différente pour organiser les actions et les réducteurs Redux par rapport aux exemples officiels de Redux (décrits [ici](https://medium.com/@nate_wang/a-new-approach-for-managing-redux-actions-91c26ce8b5da)). Vous devez donc diviser vos fichiers `actions.js` et `reducers.js` en différents fichiers. Chaque fichier contient une action et son réducteur. Le moyen le plus simple est de créer une action avec Rekit Studio, puis de déplacer votre ancienne logique d'action/réducteur à l'intérieur.

Les noms des actions et les constantes de type d'action doivent également être nommées [à la manière de Rekit](http://rekit.js.org/docs/namings.html) afin que Rekit puisse les refactoriser. Par exemple, cette image montre comment migrer l'action `addTodo` vers la manière de Rekit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pY19yaWmvDmzlI9vfZyYZw.png)

Vous n'avez pas besoin de changer votre logique métier. Il suffit de les placer dans un nouvel endroit. Avec cette approche, vous pourrez gérer les actions/réducteurs Redux plus facilement.

Vous pouvez également vérifier le résultat final [ici](https://github.com/supnate/rekit-todomvc) pour voir comment Rekit organise les actions pour l'application TodoMVC.

### Résumé

Je dois admettre que l'ajout de Rekit à un projet existant est beaucoup plus facile que je ne le pensais initialement. Vous n'avez pas besoin de changer votre configuration webpack/rollup/parcel, la façon dont vous construisez/testez votre projet, ou la façon dont vous démarrez votre application. Mais assurez-vous simplement que Rekit fonctionne dans votre projet en trois étapes :

1. Créez une structure de dossiers/un modèle de base que Rekit comprend
2. Ajoutez `rekit-core` et `rekit-studio` à votre projet.
3. Créez le script pour démarrer Rekit Studio

Maintenant, vous pouvez écrire un nouveau code avec Rekit Studio !

Cet article utilise l'application TodoMVC comme exemple de migration. Vos projets peuvent être beaucoup plus compliqués, vous pourriez donc avoir d'autres problèmes lors de la migration. Si c'est le cas, n'hésitez pas à poser vos questions dans les commentaires, et je ferai de mon mieux pour vous aider à les résoudre. Merci !