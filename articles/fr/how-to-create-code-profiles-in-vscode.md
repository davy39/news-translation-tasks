---
title: Comment créer des profils de code dans VSCode
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-23T13:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-code-profiles-in-vscode
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-06-at-1.52.10-PM-1.png
tags:
- name: Productivity
  slug: productivity
- name: teaching
  slug: teaching
- name: Visual Studio Code
  slug: vscode
seo_title: Comment créer des profils de code dans VSCode
seo_desc: 'By JavaScript Joe

  This post piggybacks off of the work done by @avanslaars who is a fellow instructor
  at egghead.io. He shared this in the egghead Slack sometime ago and I never got
  around to setting this up myself.

  Now, I''m setting up a new laptop a...'
---

Par JavaScript Joe

Cet article s'appuie sur le travail réalisé par [@avanslaars](https://twitter.com/avanslaars) qui est un fellow instructor chez [egghead.io](https://github.com/avanslaars/code-profiles). Il a partagé cela dans le Slack d'egghead il y a quelque temps et je n'ai jamais pris le temps de le configurer moi-même.

Maintenant, je configure un nouvel ordinateur portable et j'ai décidé d'essayer. En suivant le [dépôt d'Andy ici](https://github.com/avanslaars/code-profiles), je vais vous guider à travers le processus afin que vous puissiez suivre.

Avant de commencer, un "profil de code" est essentiellement une configuration différente de `settings.json`. Vous pouvez également personnaliser les extensions qui se chargent par profil de code, mais cela dépasse le cadre de cet article.

### 1. Créer un répertoire `code_profiles`

La première chose que nous devons faire est de créer un endroit pour stocker nos "paramètres de profil". Il n'est pas obligatoire de l'appeler `code_profiles`, mais nous allons utiliser ce terme puisque Andy le fait et cela sonne bien.

Il garde le sien à la racine de son ordinateur, donc nous ferons de même :

```shell
# Depuis la racine de votre ordinateur ~/
mkdir code_profiles
```

Après avoir terminé, `cd` dans ce répertoire :

```shell
cd code_profiles
```

### 2. Créer votre premier profil

Puisque je vais utiliser cela pour les enregistrements egghead, je vais créer un nouveau répertoire appelé `egghead` :

```shell
# mkdir nom-du-profil
mkdir egghead
```

Ensuite, `cd` dans ce répertoire :

```shell
cd egghead
```

### 3. Ajouter votre settings.json

VSCode attend un répertoire `data` avec un sous-répertoire `User`. Nous y placerons nos paramètres :

```shell
# -p créera les répertoires parents si nécessaire
mkdir -p data/User
```

Après avoir créé ceux-ci, changez dans ce nouveau sous-répertoire `User` et créez votre fichier `settings.json` :

```shell
# Allez dans ce répertoire
cd data/User

# Créez votre fichier de paramètres
touch settings.json
```

Ensuite, ouvrez votre fichier `settings.json` et ajoutez vos paramètres. Je vais ajouter une version modifiée de ce qu'Andy [a dans le sien](https://github.com/avanslaars/code-profiles/blob/master/egghead/data/User/settings.json) :

```json
{
  "editor.tabSize": 2,
  "editor.quickSuggestions": false,
  "editor.parameterHints": false,
  "editor.suggestOnTriggerCharacters": false,
  "editor.hover": false,
  "editor.fontSize": 18,
  "editor.tabCompletion": true,
  "window.zoomLevel": 1,
  "workbench.colorTheme": "Night Owl",
  "editor.cursorBlinking": "solid",
  "editor.cursorStyle": "line",
  "editor.minimap.renderCharacters": false,
  "terminal.integrated.fontSize": 16,
  "explorer.openEditors.visible": 0
}
```

### 4. Tester votre nouveau profil de code

Maintenant, assurons-nous que nous avons tout fait correctement. En supposant que vous avez déjà configuré VSCode pour [lancer depuis la ligne de commande](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line), nous pouvons lancer notre nouveau profil en exécutant :

```shell
# remplacer CODE_PROFILE_NAME par le nom du profil utilisé précédemment
code --user-data-dir ~/code_profiles/CODE_PROFILE_NAME/data
```

Et si cela a fonctionné, vous devriez voir VSCode s'ouvrir avec vos paramètres :

![capture d'écran de vscode avec les nouveaux paramètres](https://thepracticaldev.s3.amazonaws.com/i/8r277j7k5r0oi1b3axym.png)

### 5. Créer un alias pour votre profil.

Je ne sais pas pour vous, mais je ne veux pas avoir à me souvenir de `code --user-data-dir ...` alors suivons le conseil d'Andy et créons un alias.

J'utilise `zsh` donc je vais ajouter cet alias à mon fichier `.zshrc` comme ceci en utilisant le mot-clé "teach" :

```shell
# remplacer CODE_PROFILE_NAME par le nom du profil utilisé précédemment
alias teach="code --user-data-dir ~/code_profiles/CODE_PROFILE_NAME/data"
```

Maintenant, lorsque vous voulez utiliser ce profil de code, tout ce que vous avez à faire est de taper :

```shell
teach ~/projects/lesson
```

Hourra ! Et c'est tout.

Un grand merci à [@avanslaars](https://twitter.com/avanslaars) pour avoir partagé cela. Voici un lien vers son [dépôt `code_profiles`](https://github.com/avanslaars/code-profiles) où j'ai appris à faire cela.

_NOTE_ : Si vous utilisez VSCode en mode Portable, il existe un [bug connu](https://github.com/microsoft/vscode/issues/63657) où le flag `user-data-dir` ne fonctionne actuellement pas (un grand merci à @myfonj pour avoir signalé cela).

###

_Cet article est initialement paru sur [DEV](https://dev.to/jsjoeio/how-to-create-code-profiles-in-vscode-3ofo)._

? Plug éhonté : si vous souhaitez voir plus de contenu comme celui-ci, abonnez-vous à ma newsletter : [https://buttondown.email/jsjoeio](https://buttondown.email/jsjoeio)