---
title: 'Gitignore Expliqué : Qu''est-ce que Gitignore et Comment l''Ajouter à Votre
  Dépôt'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T21:48:00.000Z'
originalURL: https://freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e43740569d1a4ca3c32.jpg
tags:
- name: Git
  slug: git
seo_title: 'Gitignore Expliqué : Qu''est-ce que Gitignore et Comment l''Ajouter à
  Votre Dépôt'
seo_desc: 'The .gitignore file is a text file that tells Git which files or folders
  to ignore in a project.

  A local .gitignore file is usually placed in the root directory of a project. You
  can also create a global .gitignore file and any entries in that file w...'
---

Le fichier `.gitignore` est un fichier texte qui indique à Git quels fichiers ou dossiers ignorer dans un projet.

Un fichier `.gitignore` local est généralement placé dans le répertoire racine d'un projet. Vous pouvez également créer un fichier `.gitignore` global et toute entrée dans ce fichier sera ignorée dans tous vos dépôts Git.

Pour créer un fichier `.gitignore` local, créez un fichier texte et nommez-le `.gitignore` (n'oubliez pas d'inclure le `.` au début). Modifiez ensuite ce fichier selon vos besoins. Chaque nouvelle ligne doit lister un fichier ou un dossier supplémentaire que vous souhaitez que Git ignore.

Les entrées de ce fichier peuvent également suivre un motif de correspondance.

* `*` est utilisé comme caractère générique
* `/` est utilisé pour ignorer les noms de chemin relatifs au fichier `.gitignore`
* `#` est utilisé pour ajouter des commentaires à un fichier `.gitignore`

Voici un exemple de ce à quoi le fichier `.gitignore` pourrait ressembler :

```text
# Ignorer les fichiers système Mac
.DS_store

# Ignorer le dossier node_modules
node_modules

# Ignorer tous les fichiers texte
*.txt

# Ignorer les fichiers liés aux clés API
.env

# Ignorer les fichiers de configuration SASS
.sass-cache
```

Pour ajouter ou modifier votre fichier `.gitignore` global, exécutez la commande suivante :

```bash
git config --global core.excludesfile ~/.gitignore_global
```

Cela créera le fichier `~/.gitignore_global`. Vous pouvez maintenant modifier ce fichier de la même manière qu'un fichier `.gitignore` local. Tous vos dépôts Git ignoreront les fichiers et dossiers listés dans le fichier `.gitignore` global.

### Comment Ne Plus Suivre les Fichiers Précédemment Validés depuis le Nouveau Gitignore

Pour ne plus suivre un _seul_ fichier, c'est-à-dire arrêter de suivre le fichier sans le supprimer du système, utilisez :

`git rm --cached nomdufichier`

Pour ne plus suivre _tous_ les fichiers dans `.gitignore` :

D'abord, **validez** toutes les modifications de code en attente, puis exécutez :

`git rm -r --cached`

Cela supprime tous les fichiers modifiés de l'index (zone de staging), puis exécutez :

`git add .`

Validez-le :

`git commit -m ".gitignore fonctionne maintenant"`

Pour annuler `git rm --cached nomdufichier`, utilisez `git add nomdufichier`

### **Plus d'Informations :**

* Documentation Git : [gitignore](https://git-scm.com/docs/gitignore)
* Ignorer des fichiers : [GitHub](https://help.github.com/articles/ignoring-files/)
* Modèles utiles de `.gitignore` : [GitHub](https://github.com/github/gitignore)