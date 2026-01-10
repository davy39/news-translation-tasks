---
title: Git Blame Expliqué avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/git-blame-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d19740569d1a4ca35e5.jpg
tags:
- name: Git
  slug: git
- name: toothbrush
  slug: toothbrush
- name: version control
  slug: version-control
seo_title: Git Blame Expliqué avec des Exemples
seo_desc: With git blame you can see who changed what in a specific file, line by
  line, which is useful if you work in a team, instead of alone. For example, if a
  line of code makes you wonder why it is there, you can use git blame and you will
  know who you mu...
---

Avec `git blame`, vous pouvez voir qui a modifié quoi dans un fichier spécifique, ligne par ligne, ce qui est utile si vous travaillez en équipe plutôt que seul. Par exemple, si une ligne de code vous fait vous demander pourquoi elle est là, vous pouvez utiliser `git blame` et vous saurez à qui poser la question.

### **Utilisation**

Vous utilisez `git blame` comme ceci : `git blame NOM_DU_FICHIER`

Par exemple : `git blame triple_welcome.rb`

Vous verrez une sortie comme ceci :

```shell
0292b580 (Jane Doe      2018-06-18 00:17:23 -0500 1) 3.times do
e483daf0 (John Doe      2018-06-18 23:50:40 -0500 2)   print 'Welcome '
0292b580 (Jane Doe      2018-06-18 00:17:23 -0500 3) end
```

Chaque ligne est annotée avec le SHA, le nom de l'auteur et la date du dernier commit.

### **Alias pour Git Blame**

Certains programmeurs n'aiment pas le mot « blame » en raison de la connotation négative qu'il implique. De plus, cet outil est rarement (voire jamais) utilisé pour blâmer quelqu'un, mais plutôt pour demander des conseils ou comprendre l'historique d'un fichier. Par conséquent, certaines personnes utilisent un alias pour remplacer `git blame` par quelque chose de plus agréable comme `git who`, `git history` ou `git praise`. Pour cela, il suffit d'ajouter un alias git comme ceci :

`git config --global alias.history blame`

Vous pouvez trouver plus d'informations sur la création d'alias pour les commandes git [ici](https://guide.freecodecamp.org/git/git-alias/index.md).

### **Plugins d'Éditeurs de Texte Utilisant Git Blame**

Il existe plusieurs plugins pour divers éditeurs de texte qui utilisent `git blame`. Par exemple, pour créer des cartes thermiques ou ajouter des informations en ligne pour la ligne actuelle que vous inspectez. Un exemple célèbre est [GitLens](https://gitlens.amod.io/) pour VSCode.