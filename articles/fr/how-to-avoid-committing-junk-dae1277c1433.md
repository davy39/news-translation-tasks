---
title: Comment éviter de commiter des fichiers indésirables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-21T21:47:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-committing-junk-dae1277c1433
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ti1Iue11tP3DoOoVDFLZMg.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: version control
  slug: version-control
seo_title: Comment éviter de commiter des fichiers indésirables
seo_desc: 'By Yoel Zeldes

  In the development process, every developer writes stuff they don’t intend to commit
  and push to the remote server, things like debug prints. It happens to all of us
  every now and then: we forget to remove this temporary stuff before c...'
---

Par Yoel Zeldes

Dans le processus de développement, chaque développeur écrit des choses qu'il ne souhaite pas commiter et pousser vers le serveur distant, comme des impressions de débogage. Cela nous arrive à tous de temps en temps : nous oublions de supprimer ces éléments temporaires avant de commiter...

J'ai résolu cette situation quelque peu embarrassante en utilisant une approche simple : à chaque ligne que je ne veux pas commiter accidentellement, j'ajoute la séquence de caractères magique `xxx`. Cette séquence peut se trouver n'importe où dans la ligne : à l'intérieur d'un commentaire, en tant que nom de variable, en tant que nom de fonction, etc. Voici quelques exemples d'utilisation :

* impression de débogage : `print 'xxx reached this line'`.
* variable utilisée pour le débogage : `xxx_counter = 0`.
* fonction temporaire : `def xxx_print_debug_info():`.
* TODO qui doit être traité avant de commiter : `#TODO: don't forget to refactor this function xxx`.

Je l'ai implémenté en utilisant les hooks Git. Un hook est le mécanisme de Git pour déclencher des scripts personnalisés lorsque certaines actions importantes se produisent. J'ai utilisé le hook pre-commit pour valider le contenu du commit.

Il suffit de créer un fichier avec le nom `<VOTRE-DOSSIER-DEPOT>/.git/hooks/pre-commit` avec le contenu suivant :

```
#!/bin/sh
```

```
marks=xxx,aaa
marksRegex=`echo "($marks)" | sed -r 's/,/|/g'`
marksMessage=`echo "$marks" | sed -r 's/,/ or /g'`
if git diff --staged | egrep -q "^\+.*$marksRegex"; then
    echo "you forgot to remove a line containing $marksMessage!"
    echo "you can forcefully commit using \"commit -n\""
    exit 1
fi
```

1. `marks` contient les séquences de caractères qui ne sont pas autorisées à être commitées.
2. `git diff --staged` montre les changements qui seront commités. Les changements sont passés à une expression régulière qui recherche toute marque interdite (en utilisant `egrep`).
3. Si une marque interdite est trouvée, le script se termine avec un code d'erreur, provoquant l'échec du commit.

Vous voulez contourner le hook ? Exécutez `commit -n`. Cela peut être utile lorsque vous souhaitez commiter un fichier binaire tel qu'une image, qui peut contenir une marque interdite.

Avez-vous des astuces que vous avez implémentées dans votre flux de travail git quotidien ? Partagez votre magie dans les commentaires :)

_Cet article a été initialement publié par moi sur [www.anotherdatum.com](http://www.anotherdatum.com).