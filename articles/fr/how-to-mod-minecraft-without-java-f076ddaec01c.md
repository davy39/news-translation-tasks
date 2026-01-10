---
title: Comment modifier Minecraft en toute simplicité avec TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-21T11:26:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-mod-minecraft-without-java-f076ddaec01c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gcZnkUqguix0zVi7Fsd3_Q.png
tags:
- name: JavaScript
  slug: javascript
- name: minecraft
  slug: minecraft
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Comment modifier Minecraft en toute simplicité avec TypeScript
seo_desc: 'By Josh Wulf

  Usually, modifying Minecraft requires coding in Java, and a lot of scaffolding.
  Now you can write and share Minecraft mods using TypeScript/Javascript.

  ScriptCraft is an open source JavaScript Minecraft modding library, and we’ve written...'
---

Par Josh Wulf

Habituellement, la modification de Minecraft nécessite de coder en Java et beaucoup de préparation (scaffolding). Désormais, vous pouvez écrire et partager des mods Minecraft en utilisant TypeScript/JavaScript.

[ScriptCraft](https://scriptcraftjs.org/) est une bibliothèque de modding Minecraft JavaScript open source, et nous avons ajouté le support pour TypeScript ainsi qu'une série d'outils pour créer une expérience de développement familière pour ceux qui viennent de l'univers JavaScript (y compris Yeoman et NPM).

Dans cet article, je vais vous guider à travers l'installation et la création de votre premier mod Minecraft en TypeScript en moins d'une heure — seulement 20 minutes, selon votre connexion internet.

Dans cette vidéo ([cliquez ici](https://www.youtube.com/watch?v=RqohEXw9yvw) si l'intégration ne fonctionne pas ci-dessus), je vous montre comment écrire un mod Minecraft de base en utilisant TypeScript, et comment l'exécuter sur votre ordinateur local avec un serveur Minecraft pour bureau et mobile.

Ci-dessous, je vais vous guider à travers les étapes, avec des liens vers les ressources.

### Prérequis

Vous aurez besoin de certains logiciels installés sur votre ordinateur pour faire fonctionner le serveur Minecraft et les outils d'écriture de votre plugin. Installez les quatre éléments suivants :

* [Docker](https://www.docker.com/get-started) — une solution de conteneurisation.
* [Node.js](https://nodejs.org/en/) — un moteur d'exécution et une bibliothèque JavaScript.
* [Portainer](https://www.portainer.io/) — une interface graphique web pour gérer les conteneurs Docker.
* [Visual Studio Code](https://code.visualstudio.com/) — un éditeur de code.

#### Client Minecraft

Vous avez besoin d'un *client* Minecraft pour tester votre plugin.

Installez au moins l'un des éléments suivants :

* [Minecraft](https://www.minecraft.net/en-us/) Java Edition — un client de bureau, si vous voulez tester sur un serveur Bukkit.
* [Minecraft Pocket Edition](https://play.google.com/store/apps/details?id=com.mojang.minecraftpe) — un client mobile, si vous voulez tester sur un serveur Nukkit (téléphone/tablette/Xbox). Si vous utilisez celui-ci, vous pouvez utiliser [Minecraft Pocket Edition Bedrock Launcher](https://mcpelauncher.readthedocs.io/en/latest/) pour exécuter le client mobile sur votre ordinateur.

### Installation

Maintenant que vous avez installé les prérequis, il est temps d'installer les outils pour le serveur et pour le développement de plugins.

1. Exécutez la commande suivante :

```
npm i -g smac yo generator-sma-plugin typescript
```

Cela installera quatre choses sur votre ordinateur :

* `smac` — *Scriptcraft Modular Architecture Controller,* un programme qui gère les serveurs Minecraft pour vos plugins.
* `yo` — *Yeoman*, un outil de scaffolding (génération de structure).
* `generator-sma-plugin` — un plugin Yeoman pour générer un nouveau plugin Minecraft utilisant la Scriptcraft Modular Architecture.
* `typescript` — le transpileur TypeScript, pour convertir le code TypeScript en JavaScript ES5 pouvant s'exécuter dans Minecraft.

### Créer un nouveau plugin

Maintenant que vous avez installé l'ensemble d'outils, créez un nouveau plugin en exécutant cette commande :

```
yo sma-plugin
```

Cela lance l'assistant de plugin :

```
➜ yo sma-plugin
```

```
     _-----_     ╭──────────────────────────╮    |       |    │      Welcome to the      │    |--(o)--|    │  Scriptcraft SMA Plugin  │   `---------´   │       generator by       │    ( _´U`_ )    │      Magikcraft.io!      │    /___A___\   /╰──────────────────────────╯     |  ~  |   __'.___.'__ ´   `  |° ´ Y `
```

```
? Your package name (workspace)
```

Il n'y a qu'une seule question à laquelle vous devez répondre ici — le nom de votre plugin. L'assistant créera un nouveau dossier portant le nom du plugin et y placera les fichiers du nouveau plugin.

![Image](https://cdn-media-1.freecodecamp.org/images/a1XoTzt4ZRLxbrU36k05TsO9kxhNGRqCzCgM)

Ce screencast vous montre le processus :

[**Générer la structure d'un plugin Minecraft avec Magikcraft**](https://asciinema.org/a/242028)  
[_Magikcraft.io vous permet d'écrire des plugins Minecraft en TypeScript/JavaScript qui s'exécuteront sur Bureau / Mobile._asciinema.org](https://asciinema.org/a/242028)

Une fois l'assistant terminé, il affiche un message similaire à celui-ci (j'ai choisi le nom `my-sma-plugin` dans cet exemple) :

![Image](https://cdn-media-1.freecodecamp.org/images/OwKfUaZWvNXjUrZwQtri1h2pupfpzGZyPnuT)

### Modifier votre nouveau plugin

Lancez Visual Studio Code et ouvrez le répertoire contenant votre nouveau plugin.

![Image](https://cdn-media-1.freecodecamp.org/images/UE-tfGoC5k0p3SzTpJtXNgJtBMo037vN3Td0)

Voici une description des fichiers de votre nouveau plugin :

* `__tests__` — un répertoire contenant les tests unitaires pour votre plugin. Ils sont exécutés avec Jasmine. Ajoutez plus de tests ici au fur et à mesure que vous développez votre plugin.
* `.vscode` — paramètres pour Visual Studio Code.
* `autoload` — tous les fichiers ici sont automatiquement exécutés lorsque votre plugin est activé dans le serveur Minecraft. Utilisez ceci pour les tâches d'initialisation, l'enregistrement des gestionnaires d'événements, etc.
* `lib` — Un endroit pour placer les fichiers qui ne doivent pas être chargés automatiquement (ou qui sont requis par vos fichiers chargés automatiquement). Si votre plugin fournit des fonctionnalités à d'autres plugins, vous les exportez via `lib/index.ts`.
* `node_modules` — les modules de npm sont installés ici. Vous ne pouvez pas utiliser de modules npm qui utilisent les API V8 (comme fs ou http). La plupart des fonctionnalités dont vous avez besoin sont fournies par l'[API Scriptcraft](https://github.com/walterhiggins/ScriptCraft) et par le paquet `[@magikcraft/core](https://github.com/Magikcraft/magikcraft-core)`.
* `.editorconfig` — paramètres pour l'éditeur.
* `.gitattributes` — paramètres pour `git`.
* `.gitignore` — fichiers à ignorer pour `git`.
* `.prettierrc` — paramètres pour le formatage du code.
* `package-lock.json` — versions des dépendances installées.
* `package.json` — configuration de ce plugin, y compris les dépendances et les scripts.
* `README.md` — instructions pour le développement et le test de votre plugin.
* `smac-nukkit.json` — une configuration pour exécuter un serveur Nukkit avec votre plugin chargé.
* `smac.json` — une configuration pour exécuter un serveur Bukkit avec votre plugin chargé.
* `tsconfig.json` — la configuration TypeScript pour la transpilation de votre plugin en JavaScript.

Ouvrez `autoload/index.ts` :

![Image](https://cdn-media-1.freecodecamp.org/images/xxgXedotPGJ74shzoji3ZABDK2ugZweX82Nz)

Ce fichier est automatiquement exécuté lorsque le plugin est chargé. Les modifications que vous apportez ici seront visibles lorsque vous (re)chargerez le plugin.

### Démarrer un serveur de développement

Vous pouvez charger votre plugin dans un serveur de développement. Il y a deux serveurs que vous pouvez utiliser — l'un pour le client Java de bureau, et l'autre pour le client mobile Pocket Edition.

#### Démarrer le serveur de bureau

Exécutez ceci pour démarrer un serveur de bureau :

```
npm run start:bukkit
```

Cela va :

1. Récupérer l'image du serveur Bukkit depuis Docker Hub.
2. Démarrer le serveur Bukkit avec votre plugin chargé.
3. Démarrer le transpileur TypeScript pour transpiler votre code en ES5.

Vous pouvez maintenant vous connecter au serveur avec votre client de bureau. Cliquez sur `Multijoueur` puis `Connexion directe`, puis utilisez l'adresse du serveur `127.0.0.1` :

![Image](https://cdn-media-1.freecodecamp.org/images/8m5ZKnSSh-6wIWIiAfDCFPSgpUt7XAO6dWzB)

#### Démarrer le serveur mobile

Exécutez cette commande pour démarrer un serveur mobile :

```
npm run start:nukkit
```

Cela va :

1. Récupérer l'image du serveur Nukkit depuis Docker Hub.
2. Démarrer le serveur Nukkit avec votre plugin chargé.
3. Démarrer le transpileur TypeScript pour transpiler votre code en ES5.

Vous pouvez maintenant vous connecter au serveur avec votre client Pocket Edition. Cliquez sur `Jouer` puis `Serveurs`, puis ajoutez un serveur avec l'adresse `127.0.0.1` :

![Image](https://cdn-media-1.freecodecamp.org/images/-s4613jKo2qUOJtE2NiFkdwsDPUsqpB61LKt)

### Recharger les modifications de votre plugin

Au fur et à mesure que vous modifiez votre plugin et enregistrez le TypeScript modifié, il sera automatiquement transpiler en JavaScript.

Pour recharger les modifications dans le serveur de développement, tapez ce qui suit dans la console du serveur :

```
ts onrefresh()
```

Regardez le screencast ci-dessous pour voir à quoi cela ressemble.

### Arrêter le serveur

Pour arrêter le serveur, tapez cette commande dans la console du serveur :

```
smac stop
```

Regardez le screencast ci-dessous pour voir à quoi cela ressemble lorsque vous exécutez cette commande.

### Screencast : Démarrer, Recharger et Arrêter

Ce screencast vous montre le démarrage du serveur de bureau, le rechargement du code du plugin, ainsi que l'arrêt du serveur de développement.

[**Démarrer un serveur de développement Magikcraft**](https://asciinema.org/a/242023)  
[_Démarrer un serveur de développement Magikcraft._asciinema.org](https://asciinema.org/a/242023)

### Ressources complémentaires

* [Magikcraft sur GitHub](https://github.com/Magikcraft)
* [Magikcraft sur YouTube](https://www.youtube.com/channel/UC9cEOcTkQEyiKr2nCZDBYeg)
* [Code source MCT1 (Exemple de plugin)](https://github.com/Magikcraft/mct1)
* [ScriptCraft sur GitHub](https://github.com/walterhiggins/ScriptCraft)
* [Documentation de l'API Bukkit](https://bukkit.magikcraft.io)