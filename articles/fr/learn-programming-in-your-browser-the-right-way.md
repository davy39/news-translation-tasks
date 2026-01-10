---
title: GitHub Codespaces – Comment coder directement dans votre navigateur avec votre
  propre environnement de développement cloud
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2020-06-09T21:34:29.000Z'
originalURL: https://freecodecamp.org/news/learn-programming-in-your-browser-the-right-way
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a61740569d1a4ca2547.jpg
tags:
- name: codespaces
  slug: codespaces
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
- name: Rust
  slug: rust
- name: Visual Studio Code
  slug: vscode
- name: WebAssembly
  slug: webassembly
seo_title: GitHub Codespaces – Comment coder directement dans votre navigateur avec
  votre propre environnement de développement cloud
seo_desc: 'GitHub Codespaces enable you to experiment with complex software development
  stacks right from the web browser. No software to install or configure. No stress.
  No mess.


  A gif showing the setup process of a GitHub Codespace

  In the recent GitHub Satel...'
---

GitHub Codespaces vous permet d'expérimenter avec des piles de développement logiciel complexes directement depuis votre navigateur web. Aucun logiciel à installer ou à configurer. Pas de stress. Pas de désordre.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/SSVM-edited-without-music-1-1.gif align="left")

*Un gif montrant le processus d'installation d'un GitHub Codespace*

Lors de la récente conférence en ligne GitHub Satellite, l'une des annonces de produits les plus excitantes était GitHub Codespaces. L'idée est d'avoir un bouton de code sur chaque dépôt.

Lorsque vous cliquez dessus, il lance un IDE VSCode entièrement fonctionnel avec toutes les dépendances logicielles nécessaires, y compris les bibliothèques au niveau du système d'exploitation, pour construire et exécuter le projet. Cet IDE VSCode fonctionne entièrement dans votre navigateur et n'installera aucun logiciel ni ne modifiera aucune configuration pour perturber votre ordinateur.

Cela semble trop beau pour être vrai ? Eh bien, regardez vous-même le segment de la keynote de GitHub Satellite sur Codespaces !

%[https://www.youtube.com/watch?v=fQbH3meWNQ8]

Un avantage clé de GitHub Codespaces est la rapidité avec laquelle vous pouvez intégrer de nouveaux développeurs à un projet. Un nouveau développeur peut être opérationnel en quelques minutes, au lieu de jours, et commencer immédiatement à contribuer au projet. C'est un excellent outil d'apprentissage pour de nouveaux langages, frameworks et outils logiciels.

Sous le capot, il démarre un conteneur Docker sur un serveur distant, installe toute la pile logicielle requise par le projet et exécute des tâches comme la compilation et le débogage dans le Docker distant.

Le navigateur web agit comme une interface utilisateur frontale pour l'instance Docker. Cette approche ne nécessite aucune installation de logiciel sur la machine du développeur. Mais le compromis est que toute l'installation logicielle, du système d'exploitation jusqu'à l'application finale, se fait sur le serveur.

GitHub doit démarrer un nouveau serveur pour chaque instance Codespaces. Cela nécessite beaucoup de ressources de centre de données. En fait, la [page web de GitHub Codespaces](https://github.com/features/codespaces/) a une liste d'attente à ce jour (juin 2020).

![Image](https://www.freecodecamp.org/news/content/images/2024/04/codespaces-beta.png align="left")

Personnellement, je n'arrive pas à attendre que GitHub Codespaces soit disponible. Mais une machine à remonter le temps existe. Vous pouvez expérimenter toutes les fonctionnalités de GitHub Codespaces dès aujourd'hui, gratuitement.

## VS Codespaces

Le logiciel derrière GitHub Codespaces est en fait basé sur un produit Microsoft VSCode appelé [VS Codespaces](https://online.visualstudio.com/). VS Codespaces est disponible aujourd'hui pour tous les utilisateurs de Microsoft Azure. Et oui, il vous permet d'ouvrir des dépôts GitHub dans l'IDE VSCode directement depuis une fenêtre de navigateur.

Dans ce tutoriel, je vais vous montrer comment utiliser Codespaces dans votre propre travail de développement aujourd'hui.

Pour rendre Codespaces disponible dans vos dépôts GitHub, vous devez simplement ajouter le bouton HTML suivant n'importe où sur vos pages web.

Lorsque qu'un utilisateur Azure clique sur le bouton, il lui demande de se connecter à VS Codespaces et le guide à travers l'ouverture du dépôt dans l'IDE en ligne. Vous pouvez voir comment cela fonctionne dans les exemples de la section suivante.

```html
<p>
  <a href="https://online.visualstudio.com/environments/new?name=My%20Project&repo=username/reponame">
    <img src="https://img.shields.io/endpoint?style=social&url=https%3A%2F%2Faka.ms%2Fvso-badge">
  </a>
</p>
```

> VS Codespaces fonctionne entièrement dans votre navigateur et coûte environ 1 $ par jour de travail. C'est moins cher qu'une tasse de café au bureau.

## Exemples

Maintenant, examinons plusieurs exemples de la façon dont vous pourriez apprendre de nouvelles compétences en programmation en utilisant VS Codespaces.

Rust est l'un des langages de programmation qui croît le plus rapidement aujourd'hui. Il a été élu langage de programmation le plus apprécié par les utilisateurs de Stackoverflow pendant quatre années consécutives.

Mais pour expérimenter avec Rust, il faut une chaîne d'outils complexe comprenant un compilateur, un éditeur de liens, un gestionnaire de paquets, un gestionnaire d'outils, etc.

VS Codespaces offre un moyen facile d'[apprendre Rust](https://www.secondstate.io/articles/how-to-learn-rust-without-installing-any-software/). Il suffit de cliquer sur le bouton VS Codespaces dans [ce dépôt](https://github.com/second-state/learn-rust-with-github-actions) et vous avez maintenant un projet Rust fonctionnel à expérimenter !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/learn-rust-20-seconds.gif align="left")

[*https://github.com/second-state/learn-rust-with-github-actions*](https://github.com/second-state/learn-rust-with-github-actions)

En tant que langage système, Rust est bien positionné pour construire des applications côté serveur à haute performance. La pile la plus prometteuse consiste à compiler et exécuter des fonctions Rust dans un conteneur WebAssembly, puis à accéder à ces fonctions haute performance à partir d'un framework d'application web existant, tel que Node.js.

Cependant, comme vous pouvez déjà le voir, cette configuration "meilleure pratique" nécessite une pile complexe de logiciels.

En cliquant sur le bouton VS Codespaces dans [ce dépôt](https://github.com/second-state/ssvm-nodejs-starter), vous obtenez un projet Node.js entièrement fonctionnel qui utilise [des fonctions Rust dans WebAssembly](https://www.secondstate.io/articles/getting-started-with-rust-function/) comme modules. Vous pouvez immédiatement commencer à modifier le code Rust et JavaScript et exécuter l'application Node.js depuis l'IDE du navigateur web.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/SSVM-edited-without-music.gif align="left")

[*https://github.com/second-state/ssvm-nodejs-starter*](https://github.com/second-state/ssvm-nodejs-starter)

[Rust côté serveur et WebAssembly](https://www.secondstate.io/articles/why-webassembly-server/) semblent cool. Mais avons-nous réellement un exemple plus complet qui démontre la puissance et la performance de Rust au-delà d'un simple hello world ?

[Ce dépôt](https://github.com/second-state/rust-wasm-ai-demo) est un tel exemple. Ouvrez-le dans VS Codespaces et vous aurez un projet pour une [application Rust + JavaScript qui utilise Tensorflow pour effectuer la reconnaissance d'images](https://www.secondstate.io/articles/artificial-intelligence/). Comme l'application s'exécute à l'intérieur de Node.js, elle fournit un modèle pour les applications web AI-as-a-Service.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/68747470733a2f2f626c6f672e7365636f6e6473746174652e696f2f696d616765732f414961617325323033307365636f6e64732e676966.gif align="left")

[*https://github.com/second-state/rust-wasm-ai-demo*](https://github.com/second-state/rust-wasm-ai-demo)

Et si vous voulez rester à la pointe et utiliser le runtime web basé sur Rust Deno au lieu de Node.js basé sur C ? Eh bien, il existe également un [modèle VS Codespaces pour exécuter Deno en tant qu'Azure Function](https://github.com/anthonychu/azure-functions-deno-worker) !

## Comment cela fonctionne

Si vous regardez de près, chaque dépôt activé pour VS Codespaces possède un dossier `.devcontainer`. À l'intérieur de ce dossier, le `Dockerfile` spécifie comment construire le conteneur Docker pour l'environnement de développement.

Par exemple, le conteneur Docker Node.js est basé sur Ubuntu Linux avec Node.js et des paquets NPM sélectionnés préinstallés. [Consultez un exemple ici](https://github.com/second-state/ssvm-nodejs-starter/tree/master/.devcontainer).

Le fichier `devcontainer.json` spécifie la configuration pour l'IDE VSCode sur le Docker distant. Par exemple, il configure les extensions VSCode à installer, les commandes de terminal et de débogueur à utiliser, et les ports hôte à transférer pour les tests et le débogage.

Microsoft fournit [plusieurs modèles `.devcontainer`](https://github.com/microsoft/vscode-dev-containers) que vous pouvez modifier et utiliser. Ils couvrent la plupart des piles de développement logiciel courantes aujourd'hui.

Vous pourriez également personnaliser l'expérience VSCode de l'utilisateur en fournissant des définitions de lancement et de tâches dans le dossier `.vscode`. [Découvrez-les](https://github.com/second-state/ssvm-nodejs-starter/tree/master/.vscode) !

## Conclusion

Avec VS Codespaces, et GitHub Codespaces lorsqu'il sera lancé, les barrières et les frictions pour le développement logiciel sont encore réduites. Vous pouvez commencer avec des piles logicielles complexes sans quitter votre navigateur web. [Essayez-le aujourd'hui](https://www.secondstate.io/articles/getting-started-rust-nodejs-vscode/) !

Enfin, regardez la présentation complète de GitHub Satellite sur GitHub Codespaces.

%[https://www.youtube.com/watch?v=dy2eYaNxaQc]

[Abonnez-vous à ma newsletter](https://webassemblytoday.substack.com/) et restez en contact.

<iframe src="https://webassemblytoday.substack.com/embed" width="480" height="320" style="border:1px solid #EEE;background:white"></iframe>