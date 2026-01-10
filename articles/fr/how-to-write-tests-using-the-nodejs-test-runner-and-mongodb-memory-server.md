---
title: Comment écrire des tests en utilisant le test runner de Node.js et mongodb-memory-server
subtitle: ''
author: Orim Dominic Adah
co_authors: []
series: null
date: '2025-02-13T16:33:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-tests-using-the-nodejs-test-runner-and-mongodb-memory-server
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739464298236/f5d6c959-4570-4813-bdd2-28c27dae4e1f.png
tags:
- name: Node.js
  slug: nodejs
- name: MongoDB
  slug: mongodb
- name: Testing
  slug: testing
seo_title: Comment écrire des tests en utilisant le test runner de Node.js et mongodb-memory-server
seo_desc: I recently migrated some tests from Jest to the Node.js test runner in two
  of my projects that use MongoDB. In one of those projects, test runtime was reduced
  from 107 seconds to 25 seconds (screenshot below). In the other project, test runtime
  was r...
---

J'ai récemment migré certains tests de Jest vers le test runner de Node.js dans deux de mes projets qui utilisent MongoDB. Dans l'un de ces projets, le temps d'exécution des tests a été réduit de 107 secondes à 25 secondes (capture d'écran ci-dessous). Dans l'autre projet, le temps d'exécution des tests a été réduit d'environ 66 %.

![Réduction de 76 % du temps nécessaire pour exécuter les tests dans Jest vs Node.js test runner](https://cdn.hashnode.com/res/hashnode/image/upload/v1738830673460/1560f7a3-38c1-42f3-8944-df06b40d73e4.png align="center")

J'ai décidé de partager avec vous comment j'ai pu implémenter cela. Je pense que vous trouverez cela utile, car c'est plus rentable (en termes de réduction des coûts liés à l'exécution des tests dans CI/CD), et cela améliore également votre expérience de développeur.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Le test runner de Node.js](#heading-le-test-runner-de-nodejs)
    
* [Serveur MongoDB en mémoire](#heading-serveur-mongodb-en-memoire)
    
* [Comment écrire les tests](#heading-comment-ecrire-les-tests)
    
    * [1\. Configurer le projet](#heading-1-configurer-le-projet)
        
    * [2\. Configurer le schéma Mongoose](#heading-2-configurer-le-schema-mongoose)
        
    * [3\. Configurer les services](#heading-3-configurer-les-services)
        
    * [4\. Configurer les tests](#heading-4-configurer-les-tests)
        
    * [5\. Écrire les tests](#heading-5-ecrire-les-tests)
        
    * [6\. Passer les tests](#heading-6-passer-les-tests)
        
    * [7\. Utiliser TypeScript (Optionnel)](#heading-7-utiliser-typescript-optionnel)
        
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre ce guide, vous devez avoir de l'expérience avec Node.js, MongoDB et Mongoose (ou tout autre mapper d'objets de données MongoDB). Vous devez également avoir Node.js (au moins v20.18.2) et MongoDB installés sur votre ordinateur.

## Le test runner de Node.js

Le test runner de Node.js a été introduit comme une fonctionnalité expérimentale dans la version 18 de Node.js. Il est devenu pleinement disponible dans la version 20. Il vous donne la possibilité de :

1. Exécuter des tests
    
2. Rapporter les résultats des tests
    
3. Rapporter la couverture des tests (toujours expérimental à la version 23)
    

Il est judicieux d'utiliser le test runner intégré lors de l'écriture de tests en Node.js car cela signifie que vous avez besoin de moins de dépendances externes. Vous n'avez pas besoin d'installer une bibliothèque externe (et ses dépendances associées) pour exécuter des tests.

Le test runner intégré est également plus rapide. Sur la base de mon expérience en l'utilisant sur deux projets (qui utilisaient auparavant Jest), j'ai vu des améliorations d'au moins 66 % de réduction du temps nécessaire pour exécuter complètement les tests.

Et contrairement à d'autres frameworks ou bibliothèques de test, le test runner de Node.js a été construit spécifiquement pour les projets Node.js. Il ne tente pas de s'adapter aux spécificités d'autres environnements de programmation comme le navigateur. Les spécificités de Node.js sont sa principale et unique priorité.

## Serveur MongoDB en mémoire

Pour les tests qui impliquent de faire des requêtes à une base de données, certains développeurs préfèrent simuler les requêtes pour éviter de faire des requêtes à une vraie base de données. Ils le font parce que faire une requête à une vraie base de données nécessite beaucoup de configuration, ce qui peut coûter du temps et des ressources.

L'écriture et la récupération de données en utilisant une vraie base de données sont plus lentes [par rapport à l'écriture et la récupération de données depuis la mémoire](https://www.mongodb.com/resources/basics/databases/in-memory-database). Lors de l'exécution de tests automatisés, l'utilisation d'un vrai serveur MongoDB sera plus lente que l'utilisation d'un serveur de base de données en mémoire, et c'est là que [mongodb-memory-server](https://github.com/typegoose/mongodb-memory-server) devient utile.

![Comparaison entre la mémoire et la communication avec la base de données avec le CPU](https://cdn.hashnode.com/res/hashnode/image/upload/v1738832586702/62360547-70e8-4e74-854f-c7ad74d182ea.png align="center")

Selon sa documentation, mongodb-memory-server crée et démarre un vrai serveur MongoDB de manière programmatique depuis Node.js, mais utilise une base de données en mémoire par défaut. Il vous permet également de vous connecter au serveur de base de données qu'il crée en utilisant votre mapper d'objets de données préféré tel que Mongoose, Prisma ou TypeORM. Dans ce guide, nous utiliserons [Mongoose](https://mongoosejs.com/) (v8.9.6).

Puisque les données stockées par mongodb-memory-server résident en mémoire par défaut, il est plus rapide de les lire et de les écrire que lorsque l'on utilise une vraie base de données. mongodb-memory-server est également plus facile à configurer. Ces avantages en font un bon choix pour l'utiliser comme serveur de base de données pour écrire des tests.

Note : Assurez-vous d'installer la version 9.1.6 de mongodb-memory-server pour suivre ce guide. La version 10 a actuellement des problèmes avec le nettoyage des ressources après l'exécution des tests. Voir ce problème intitulé [Node forking will include any --import from the original command](https://github.com/typegoose/mongodb-memory-server/issues/912).

Le problème a été résolu au moment de la rédaction de cet article, mais la correction n'a pas encore été fusionnée pour les installations.

## Comment écrire les tests

Maintenant, je vais vous guider à travers les étapes suivantes pour commencer à écrire des tests :

1. Configurer le projet
    
2. Configurer le schéma Mongoose
    
3. Configurer les services
    
4. Configurer les tests
    
5. Écrire les tests
    
6. Passer les tests
    
7. Utiliser TypeScript (Optionnel)
    

### 1\. Configurer le projet

J'ai créé un dépôt GitHub pour vous faciliter le suivi de ce guide. Clonez le dépôt à l'adresse [nodejs-test-runner-mongoose](https://github.com/orimdominic/nodejs-test-runner-mongoose) et basculez sur la branche `01-setup`.

Dans `01-setup`, les dépendances du projet se trouvent dans le fichier `package.json`. Installez les dépendances en utilisant la commande `npm install` pour configurer le projet. Pour vous assurer que la configuration est complète et correcte, exécutez la commande `node .` dans le terminal de votre projet. Vous devriez voir votre version de Node.js comme sortie dans le terminal.

```bash
# installer les dépendances
npm install
...
# exécuter la commande node
node .
# la sortie
Vous exécutez Node.js v22.13.1
```

### 2\. Configurer le schéma Mongoose

Nous allons configurer le schéma pour deux collections (Task et User) dans la branche [`02-setup-schema`](https://github.com/orimdominic/nodejs-test-runner-mongoose/tree/02-setup-schema) en utilisant Mongoose. Les fichiers [`task/model.mjs`](https://github.com/orimdominic/nodejs-test-runner-mongoose/blob/02-setup-schema/task/model.mjs) et [`user/model.mjs`](https://github.com/orimdominic/nodejs-test-runner-mongoose/blob/02-setup-schema/user/model.mjs) contiennent le schéma pour les collections Task et User, respectivement. Nous allons également configurer une connexion à la base de données dans `index.mjs` pour nous assurer que la configuration du schéma fonctionne correctement.

Je ne vais pas entrer dans les détails des modèles et schémas Mongoose dans cet article car ils sont hors de son champ d'application.

Lorsque vous exécutez la commande `node .` après avoir implémenté les changements dans `02-setup-schema`, vous devriez voir un résultat similaire dans la console comme dans l'extrait ci-dessous :

```bash
node .
Vous exécutez Node.js v22.13.1
Utilisateur créé avec l'id 679f1d7f73fbeaf23b2007df
Tâche "Titre de la tâche" créée pour l'utilisateur avec l'id "679f1d7f73fbeaf23b2007df"
```

Vous pouvez voir les différences entre `01-setup` et `02-setup-schema` via le [diff 01-setup &lt;&gt; 02-setup-schema sur GitHub](https://github.com/orimdominic/nodejs-test-runner-mongoose/compare/01-setup...02-setup-schema).

### 3\. Configurer les services

Ensuite, nous créons des fichiers de service ([`task/service.mjs`](https://github.com/orimdominic/nodejs-test-runner-mongoose/blob/03-setup-services/task/service.mjs) et [`user/service.mjs`](https://github.com/orimdominic/nodejs-test-runner-mongoose/blob/03-setup-services/user/service.mjs)) dans la branche [`03-setup-services`](https://github.com/orimdominic/nodejs-test-runner-mongoose/tree/03-setup-services). Les deux fichiers contiennent actuellement des fonctions vides pour lesquelles nous écrirons des tests plus tard. Ces fonctions contiendront la logique métier et communiqueront également avec la base de données. Nous utilisons les commentaires [JSDoc](https://jsdoc.app/) pour typer les paramètres et les valeurs de retour.

Cliquez sur [diff 02-setup-schema &lt;&gt; 03-setup-services](https://github.com/orimdominic/nodejs-test-runner-mongoose/compare/01-setup...02-setup-schema) pour voir les changements de code entre `02-setup-schema` et `03-setup-services`.

### 4\. Configurer les tests

Dans la branche [`04-set-up-tests`](https://github.com/orimdominic/nodejs-test-runner-mongoose/tree/04-set-up-tests), nous configurons le code pour exécuter les tests. Nous créons [`test.setup.mjs`](https://github.com/orimdominic/nodejs-test-runner-mongoose/blob/04-set-up-tests/test.setup.mjs) qui contient le code qui sera exécuté avant chaque fichier de test.

Dans `test.setup.mjs`, la fonction `connect` crée un serveur MongoDB en mémoire et se connecte à celui-ci avec Mongoose pour exécuter les tests. La fonction `closeDatabase` ferme la connexion à la base de données et nettoie toutes les ressources pour libérer la mémoire.

Les fonctions `connect` et `closeDatabase` sont exécutées dans le hook [`t.before`](https://nodejs.org/api/test.html#beforefn-options) et le hook [`t.after`](https://nodejs.org/api/test.html#afterfn-options) respectivement. Cela garantit que, avant qu'un fichier de test ne soit exécuté, une connexion à la base de données est établie via `t.before`. Ensuite, après que les tests pour le fichier ont été complètement exécutés, la connexion à la base de données est interrompue et les ressources utilisées sont libérées via `t.after`.

Dans `package.json`, nous allons mettre à jour le script npm `test` en `node --test --import ./test.setup.mjs`. Cette commande garantit que le module ES `test.setup.mjs` est préchargé et exécuté via la commande CLI [\--import](https://nodejs.org/api/cli.html#--importmodule) avant chaque fichier de test.

Ensuite, nous allons créer les fichiers de test avec des tests vides dans les dossiers `__tests__` pour `user` et `task`. Après avoir implémenté les [nouveaux changements dans 04-set-up-tests](https://github.com/orimdominic/nodejs-test-runner-mongoose/compare/03-setup-services...04-set-up-tests), l'exécution du script `test` avec `npm run test` devrait afficher une sortie similaire à l'extrait ci-dessous :

```bash
npm run test

> nodejs-test-runner-mongoose@1.0.0 test
> node --test --import ./test.setup.mjs

...

✓ tests 8
✓ suites 5
✓ pass 8
✓ fail 0
✓ cancelled 0
✓ skipped 0
✓ todo 0
✓ duration_ms 941.768873
```

Tous les tests passent actuellement car il n'y a pas d'assertions qui échouent. Nous allons écrire des tests avec des assertions dans la section suivante.

### 5\. Écrire les tests

Il est maintenant temps d'écrire des tests pour les fonctions dans les fichiers de service dans la branche [`05-write-tests`](https://github.com/orimdominic/nodejs-test-runner-mongoose/blob/05-write-tests). Nous utilisons la [bibliothèque assert de Node.js](https://nodejs.org/api/assert.html) pour nous assurer que les valeurs retournées par les fonctions sont celles que nous attendons. Vous pouvez voir les tests que nous avons écrits lorsque vous comparez [les différences entre 04-set-up-tests et 05-write-tests](https://github.com/orimdominic/nodejs-test-runner-mongoose/compare/04-set-up-tests...05-write-tests)

Lorsque le script `tests` est exécuté, tous les tests échouent car nous n'avons pas encore écrit les fonctions dans les fichiers de service. Vous devriez voir une sortie similaire à l'extrait ci-dessous lorsque vous exécutez le script `test` :

```bash
npm run test

> nodejs-test-runner-mongoose@1.0.0 test
> node --test --import ./test.setup.mjs

...

✓ tests 8
✓ suites 5
✓ pass 0
✓ fail 8
✓ cancelled 0
✓ skipped 0
✓ todo 0
✓ duration_ms 1202.031961
```

### 6\. Passer les tests

Dans [`06-pass-tests`](https://github.com/orimdominic/nodejs-test-runner-mongoose/blob/06-pass-tests), nous écrivons les fonctions dans les fichiers de service pour passer les tests. Seuls 6 des 7 tests passent lorsque le script `test` est exécuté car nous avons ignoré le test pour la fonction `getById` dans `user/service.mjs` avec `t.skip`. Nous n'avons pas terminé la fonction `getById` dans `user/service.mjs`. J'ai pensé que nous pourrions la laisser comme exercice.

Lorsque vous exécutez le script `test`, vous devriez obtenir une sortie similaire dans le terminal comme ci-dessous :

```bash
✓ tests 7
✓ suites 4
✓ pass 6
✓ fail 0
✓ cancelled 0
✓ skipped 1
✓ todo 0
✓ duration_ms 1287.564918
```

Vous pouvez voir le code que nous avons écrit pour passer les tests dans les [changements de code entre 05-write-tests et 06-pass-tests](https://github.com/orimdominic/nodejs-test-runner-mongoose/compare/05-write-tests...06-pass-tests).

### 7\. Utiliser TypeScript (Optionnel)

Si vous avez l'intention d'exécuter des tests avec TypeScript, vous pouvez consulter la branche [`07-with-typescript`](https://github.com/orimdominic/nodejs-test-runner-mongoose/tree/07-with-typescript). Vous devez avoir Node.js `>=v22.6.0` installé car nous utilisons l'option `--experimental-strip-types` dans le `test`. Pour configurer les tests pour qu'ils s'exécutent avec TypeScript, suivez les étapes suivantes :

1. Installez TypeScript en utilisant la commande `npm install typescript --save-dev`
    
2. Installez tsx en utilisant la commande `npm install tsx`
    
3. Créez un fichier `tsconfig.json` par défaut à la racine du projet en utilisant la commande `npx tsc --init`
    

Dans `package.json`, mettez à jour le script `test` comme suit :

```bash
"test": "node --test --experimental-strip-types --import tsx --import ./test.setup.mjs"
```

* [`--experimental-strip-types`](https://nodejs.org/docs/latest-v22.x/api/cli.html#--experimental-strip-types) aide à supprimer les types avant l'exécution de chaque fichier de test.
    
* Le préchargement de `tsx` avec `--import` aide à exécuter le fichier TypeScript. Sans cela, le test runner ne pourra pas trouver les fichiers importés sans l'extension `.ts`. Par exemple, `user/model.ts` importé avec l'extrait de code ci-dessous ne sera pas trouvé.
    
    ```typescript
    import { UserModel } from "./model";
    ```
    

Le reste des [changements de 06-pass-tests à 07-with-typescript](https://github.com/orimdominic/nodejs-test-runner-mongoose/compare/06-pass-tests...07-with-typescript) implique la mise à jour des types, le changement des extensions de fichiers de `.mjs` à `.ts` et la mise à jour des instructions d'importation.

## Conclusion

Dans ce guide, vous avez appris à utiliser le test runner intégré de Node.js et pourquoi c'est souvent un meilleur choix que d'autres bibliothèques et frameworks de test. Vous avez également appris à utiliser mongodb-memory-server comme remplacement pour un vrai serveur MongoDB, ainsi que pourquoi c'est une bonne idée d'utiliser cela au lieu d'un vrai serveur MongoDB pour les tests.

Plus important encore, vous avez appris à configurer et exécuter des tests en Node.js en utilisant le test runner de Node.js et mongodb-memory-server. Vous devriez maintenant savoir comment configurer vos projets pour exécuter les tests si vous utilisez TypeScript.

Si vous trouvez le dépôt [nodejs-test-runner-mongoose](https://github.com/orimdominic/nodejs-test-runner-mongoose) utile, n'hésitez pas à lui donner une étoile. Cela m'encourage. Merci.