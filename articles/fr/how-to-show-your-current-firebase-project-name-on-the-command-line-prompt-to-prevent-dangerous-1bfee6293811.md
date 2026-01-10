---
title: Comment afficher le nom de votre projet Firebase actuel dans l'invite de commande
  pour éviter les erreurs dangereuses
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T21:36:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-show-your-current-firebase-project-name-on-the-command-line-prompt-to-prevent-dangerous-1bfee6293811
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8Yvp2a4vtkb5dWzWXh1qcQ.png
tags:
- name: Bash
  slug: bash
- name: Firebase
  slug: firebase
- name: 'tech '
  slug: tech
- name: terminal
  slug: terminal
- name: zsh
  slug: zsh
seo_title: Comment afficher le nom de votre projet Firebase actuel dans l'invite de
  commande pour éviter les erreurs dangereuses
seo_desc: 'By Thang Minh Vu

  When working on a project with multiple stages (development, staging, production),
  developers use the command firebase use to switch between projects. It’s very easy
  to run a command on the production environment instead of the devel...'
---

Par Thang Minh Vu

Lorsqu'on travaille sur un projet avec plusieurs environnements (développement, staging, production), les développeurs utilisent la commande `firebase use` pour basculer entre les projets. Il est très facile d'exécuter une commande sur l'environnement de production au lieu du développement. Cela est très dangereux.

![Image](https://cdn-media-1.freecodecamp.org/images/eFjsis27Zzr7idxjQLbY6pGoFuXoJaFymGRv)
_Commande pour basculer entre les projets Firebase_

**Note** : Vous pouvez toujours trouver le dernier script dans mon [dépôt GitHub](https://github.com/ittus/firebase-prompt).

Normalement, les développeurs ne travaillent que sur le projet de développement. Ils ne basculent vers la production qu'en cas de vérification ou de hotfix. Il m'est arrivé quelques fois d'oublier de revenir au projet de développement. J'ai accidentellement modifié la base de données sans penser que cela pouvait impacter les utilisateurs réels.

En explorant le _CLI Firebase_, j'ai découvert qu'il utilise [configstore](https://github.com/yeoman/configstore) pour gérer la configuration locale. Toute la configuration est sauvegardée dans un fichier JSON et est facilement lisible. J'ai créé un petit script destiné à afficher le nom du projet Firebase dans **l'invite de shell**.

### Comment l'installer

#### Bash

Ajoutez le script suivant à la fin de `~/.bash_profile` :

![Image](https://cdn-media-1.freecodecamp.org/images/vxqUWLsAfgLirG49oRLax03ekT7t5SfgaXYq)
_Ajouter le script à ~/.bash_profile_

Ensuite, exécutez `source ~/.bash_profile` ou ouvrez une nouvelle fenêtre de terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/ziaCqfVR0i6tyepr38KBdQ8jnmcdwq7pzHNl)
_Le nom du projet Firebase est affiché comme dev-project, stage-project et prod-project_

#### iTerm2 avec oh-my-zsh

[Oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) est un framework open source populaire pour Zshell. Je l'apprécie car il propose de nombreux thèmes de terminal magnifiques et de nombreux plugins utiles.

Ici, je vais faire un exemple avec le thème _agnoster_ :
Éditez `~/.oh-my-zsh/themes/agnoster.zsh-theme`

![Image](https://cdn-media-1.freecodecamp.org/images/RtXGYfMLwplrpQj-BQkXr3M9cMxpRKWuo4z4)
_Script pour oh-my-zsh_

Puis ajoutez `prompt_firebase` aux fonctions `build_prompt` :

![Image](https://cdn-media-1.freecodecamp.org/images/uHVO625HTQdptNI1faRbYW8EZgHVpAEycvh4)
_Changer la fonction build_prompt_

Pour la dernière étape, exécutez `source ~/.zshrc` ou ouvrez une nouvelle fenêtre de terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/CsElxb8a3b4VSJjAqXkyFL-XrwhSXlLEIbuF)
_saas-cs-deploy-taguro-5c55e est affiché comme dernier texte dans l'invite de terminal_

J'espère que cela pourra vous aider à éviter une situation inattendue (et mauvaise).

**Note** : Vous pouvez toujours trouver le dernier script dans mon [dépôt GitHub](https://github.com/ittus/firebase-prompt).