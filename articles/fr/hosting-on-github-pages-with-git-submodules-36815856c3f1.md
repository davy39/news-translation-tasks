---
title: Comment héberger sur GitHub Pages avec les sous-modules Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T17:25:51.000Z'
originalURL: https://freecodecamp.org/news/hosting-on-github-pages-with-git-submodules-36815856c3f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NNm6FdS2dbSlstMML1yduw.png
tags:
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment héberger sur GitHub Pages avec les sous-modules Git
seo_desc: 'By Felix Wu

  Git Submodules is one of the most terrific but exhausting features in Git.I mean,
  we all love Git, right? But have you ever tried using Git Submodules?

  Actually, standalone Git Submodules aren’t hard to understand. Initializing is easily
  ...'
---

Par Felix Wu

Les sous-modules Git sont l'une des fonctionnalités les plus terrifiantes mais épuisantes de Git. 
Je veux dire, nous aimons tous **Git**, n'est-ce pas ? Mais avez-vous déjà essayé d'utiliser les sous-modules Git ?

En fait, les sous-modules Git autonomes ne sont pas difficiles à comprendre. L'initialisation se fait facilement en tapant :

```
git submodule add <lien-vers-le-depot-distant>
```

Cependant, j'ai récemment voulu utiliser des sous-modules pour héberger mes présentations reveal.js basées sur un sous-chemin, et cela s'est compliqué car je n'avais aucun tutoriel auquel me référer.

Je voulais essentiellement avoir un dépôt appelé « presentations », afin que GH-Pages héberge ce dépôt sur le sous-chemin respectif ([http://presentations.flxwu.com/](http://presentations.flxwu.com/)) dans lequel je pourrais inclure mes dépôts reveal actuels.

Ainsi, je pourrais avoir **des dépôts autonomes séparés pour mes présentations qui seraient automatiquement mis à jour dans le dépôt « presentations ».** Cela ferait en sorte que mon dépôt « firebase-101 » soit hébergé sur [http://flxwu.com/presentations/firebase-101](http://flxwu.com/presentations/firebase-101).

Vous pouvez également héberger sur un sous-domaine personnalisé — j'ai mes présentations à [**presentations.flxwu.com/[nom-du-depot]**](http://presentations.flxwu.com/[nom-du-depot]). Vous pouvez donc toujours avoir vos autres dépôts non-présentations sous [username.github.io/[nom-du-depot]](http://username.github.io/[nom-du-depot])

### Configuration du dépôt local

Tout d'abord, nous initialisons un nouveau dépôt et ajoutons les sous-modules respectifs.

```
mkdir parentrepo && cd parentrepo/git initgit submodule add https://github.com/flxwu/firebase-101
```

Vous pouvez remplacer le lien de mon dépôt par votre dépôt respectif que vous souhaitez héberger sur votre sous-chemin [username.github.io/parentrepo/[nom-du-depot]](http://username.github.io/parentrepo/[nom-du-depot]). **Assurez-vous simplement que le lien utilise HTTPS et que le dépôt est public.**

Maintenant, validez tout et suivez la procédure habituelle de création du dépôt GitHub, d'ajout du dépôt GitHub distant localement et de poussée vers celui-ci :

```
git commit -a -m "Initial Commit"git remote add origin [lien .git de votre dépôt github]git push origin master
```

Votre dépôt GitHub devrait maintenant ressembler à ceci (sauf avec un seul dossier lié si vous n'avez ajouté qu'un seul sous-module)

![Image](https://cdn-media-1.freecodecamp.org/images/o9f8sM3ccAkSpITYVAAPUoy6D3iMkg49OPOP)

Maintenant, allez dans les paramètres et publiez la branche « master » sur GitHub Pages. Vous devriez maintenant voir ceci ci-dessous, en remplaçant [flxwu.com] par votre propre domaine de pages GitHub utilisateur (username.github.io si vous n'avez pas défini un domaine personnalisé).

![Image](https://cdn-media-1.freecodecamp.org/images/4wrrjCiLFksvG2UmDIwqFYTUoFJUu-oEGDqM)

Vous pouvez maintenant également définir un sous-domaine personnalisé :

![Image](https://cdn-media-1.freecodecamp.org/images/4y3gU4qaLbvZeoO-sXUdeOWLiK5YZWcwlWCL)
_C'est ainsi que j'ai configuré GitHub Pages_

Maintenant, votre sous-module respectif `**firebase-101**` (si vous n'avez pas ajouté votre propre dépôt au lieu du mien) est hébergé sur **sous-domaine.domaine.com/firebase-101**.

#### Succès !

Si cet article vous a aidé, suivez-moi sur twitter [@flxwu](http://twitter.com/flxwu)

### Bonus : Comment supprimer un sous-module

* Supprimez la section faisant référence au sous-module du fichier `.gitmodules`
* Indexez les changements via `git add .gitmodules`
* Supprimez la section pertinente du sous-module de `.git/config`.
* Exécutez `git rm --cached chemin_vers_sousmodule` (sans barre oblique de fin)
* Exécutez `rm -rf .git/modules/chemin_vers_sousmodule`
* Validez les changements avec `git commit -m "Suppression du sous-module "`
* Supprimez les fichiers du sous-module maintenant non suivis `rm -rf chemin_vers_sousmodule`