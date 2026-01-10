---
title: Comment créer un outil CLI en NodeJS ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-26T16:00:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-cli-tool-in-nodejs-bc4f67d898ec
coverImage: https://cdn-media-1.freecodecamp.org/images/0*WBakKAUjwhRyaoyu
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment créer un outil CLI en NodeJS ?
seo_desc: 'By Al-amin Nowshad

  As developers, we kind of live with CLI tools. From git to cloud shells — we are
  using these tools everywhere. So, it’s time to make your own. We’ll use Heroku’s
  great oclif framework in the process.

  What’s oclif?

  It’s an open fram...'
---

Par Al-amin Nowshad

En tant que développeurs, nous vivons avec les outils CLI. De `git` à `cloud shells` — nous utilisons ces outils partout. Alors, il est temps de créer le vôtre. Nous utiliserons le framework oclif de Heroku dans le processus.

### Qu'est-ce que oclif ?

C'est un **framework** open source pour créer rapidement des outils CLI, et il est fourni par le bien connu **Heroku**.

### Qu'allons-nous construire ?

Nous allons créer une commande de liste de tâches qui peut avoir quatre actions :

* Ajouter une nouvelle tâche
* Voir toutes les tâches
* Mettre à jour une tâche
* Supprimer une tâche

### Initialiser notre projet

Oclif peut générer deux types de projets —

1. Projets qui ont une seule commande.
2. Projets qui peuvent avoir plusieurs commandes, y compris des commandes imbriquées.

Dans cet article, nous aurons besoin d'un projet avec plusieurs commandes, alors générons-le :

```
npx oclif multi todocli
```

L'exécution de cette commande et le suivi des instructions initialiseront un nouveau projet nommé `todocli` dans le répertoire courant.

Maintenant, allons dans le répertoire et exécutons l'aide :

```
cd todocli && ./bin/run --help
```

Cela affichera les résultats ci-dessous :

```
> USAGE       $ todocli [COMMAND]    COMMANDS    hello       help   display help for todocli
```

Cela montre les commandes disponibles et leur documentation.

![Image](https://cdn-media-1.freecodecamp.org/images/7kAIGY3XeWm6MEvHGy1CzqkIaAZgNlRuaRgB)

### Structure du projet

Dans le répertoire `src`, nous trouvons un répertoire nommé `commands`. Ce répertoire contient toutes les commandes avec leurs noms de fichiers respectifs. Par exemple, si nous avons une commande `hello`, nous aurons un fichier nommé `hello.js` dans ce répertoire et la commande fonctionnera sans autre configuration. Supprimons `hello.js` car nous n'en aurons pas besoin.

### Configuration de la base de données

Pour stocker nos tâches, nous avons besoin d'un système de stockage. Pour simplifier, nous utiliserons [lowdb](https://github.com/typicode/lowdb) qui est un système de stockage de fichiers **json** assez simple. Parfait pour ce projet ?

Installons-le :

```
npm install lowdb --save
```

Créons un fichier `db.json` à la racine de notre projet. Ce fichier contiendra nos données. Ensuite, nous devons installer [lowdb](https://github.com/typicode/lowdb). Maintenant, nous allons créer un fichier appelé `db.js` dans le répertoire `src`. Ce fichier contiendra notre base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/ZPMiJ2gQxw0dhQ8nUrNcHEgLKn6sjQZytsUF)

Ici, nous chargeons simplement la bibliothèque et le fichier requis, puis nous définissons un tableau de todos vide comme notre collection de base (c'est comme une table si vous pensez aux bases de données SQL).

### Ajout de tâches

oclif nous fournit une fonctionnalité de génération de commandes fluide. Exécutons ce qui suit :

```
oclif command add
```

Cela créera un fichier nommé `add.js` dans le répertoire `src/commands`. Remplaçons le contenu de ce fichier par le code ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/YL5ieYvGcM7hWUt7U8OVl57BYhEkTnMNOecq)

Le fichier a quelques composants clés :

* une fonction run qui exécute la fonctionnalité principale de cette commande,
* une description, qui est la documentation de la commande, et
* des flags, qui décrivent les flags passés à la commande.

Ici, nous avons un flag nommé `task` qui est de type `string`. Nous pouvons exécuter la commande

```
./bin/run add --task="welcome task"
```

Cette commande ajoutera une tâche à notre base de données et affichera la réponse de cette opération.

### Affichage des tâches

![Image](https://cdn-media-1.freecodecamp.org/images/kavzj2Te9vo0cKMrAqCuzq2y1NQxy9SlE-bE)

Ici, dans `show.js`, nous affichons toutes les tâches dans l'ordre ascendant. Nous avons ajouté un peu de couleur avec `chalkjs` pour donner à nos résultats de commande une meilleure apparence.

![Image](https://cdn-media-1.freecodecamp.org/images/rLEcSp4-OGsNGwPQ5rKFfQEtGtmfmqeD5SfI)

### Mise à jour des tâches

![Image](https://cdn-media-1.freecodecamp.org/images/K9WR09bpADleq90pqY-xJmK-E7ssX235oqjI)

Pour simplifier, nous définissons simplement les tâches comme `done` pour notre partie de mise à jour. Nous devons simplement passer l'`id` de la tâche comme un `flag`.

```
./bin/run update --id=1
```

Cela définira `done = true` pour la tâche avec `id = 1`.

### Suppression des tâches

![Image](https://cdn-media-1.freecodecamp.org/images/of6nVG76saJkI4VyV5mXA-AsZTPNat1Na2fU)

La suppression est assez simple : nous passons `id` comme un flag, puis nous supprimons la tâche correspondante de notre base de données.

### Presque terminé !

Et juste comme ça, nous avons créé notre très simple `todocli`. Maintenant, si nous voulons l'utiliser comme tout autre outil CLI normal ou laisser nos amis l'utiliser, nous devons en faire un package npm. Alors, publions-le sur npm.

### Build et publication sur npm

Tout d'abord, assurez-vous d'avoir un compte npm. Ensuite, vous devez vous connecter en exécutant la commande

```
npm login
```

Ensuite, dans le répertoire du projet, exécutez

```
npm run prepack
```

Cela packagera le projet et le rendra prêt pour npm avec un readme généré à partir des descriptions et des flags.

Maintenant, publiez-le sur npm :

```
npm publish
```

Si tout se passe bien, le module a été publié sur npm avec succès. Si cela ne fonctionne pas, vérifiez le nom et la version du projet.

Maintenant, nous pouvons l'utiliser comme tout autre outil npm avec l'installation globale :

```
npm install -g todocli
```

Et ensuite, n'importe qui peut simplement utiliser ces commandes à tout moment, presque n'importe où ?

```
> todocli add --task="Great task!!!"> todocli show> todocli update --id=1> todocli remove --id=1
```

Si vous êtes arrivé jusqu'ici en suivant tout l'article, félicitations ? Vous êtes génial. Maintenant, vous pouvez faire une petite tâche :

#### Tâche

L'attribution des identifiants des tâches n'est pas correcte, pouvez-vous la corriger ? Faites-moi savoir comment vous la résolvez dans la section des réponses.

Bonne chance, et merci pour la lecture :)

oclif : [https://oclif.io](https://oclif.io)

lowdb: [https://github.com/typicode/lowdb](https://github.com/typicode/lowdb)

chalk: [https://github.com/chalk/chalk](https://github.com/chalk/chalk)

todocli: [https://www.npmjs.com/package/todocli-frombd](https://www.npmjs.com/package/todocli-frombd)