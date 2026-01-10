---
title: Comment récupérer un fichier supprimé dans Git – Annuler les modifications
  après un reset hard
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-06-21T21:31:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-recover-a-deleted-file-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Copy-of-read-write-files-python--1-.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment récupérer un fichier supprimé dans Git – Annuler les modifications
  après un reset hard
seo_desc: "Git is a version control system that helps you keep track of the changes\
  \ in a project's life cycle. It preserves the history of the project and allows\
  \ you and your team members to coordinate effectively throughout. \nThere could\
  \ be situations where yo..."
---

Git est un système de contrôle de version qui vous aide à suivre les changements dans le cycle de vie d'un projet. Il préserve l'historique du projet et permet à vous et à vos membres d'équipe de coordonner efficacement tout au long du projet. 

Il pourrait y avoir des situations où vous avez supprimé un fichier et vous souhaitez le récupérer. La bonne nouvelle est que vous pouvez – la plupart du temps – récupérer les fichiers lorsque vous utilisez un système de contrôle de version (VCS). 

Dans ce tutoriel, nous allons apprendre les différentes méthodes que Git offre pour restaurer les fichiers supprimés.

## Comment récupérer des fichiers après avoir validé des modifications 

Supposons que vous avez validé une modification mais que vous avez fait un reset hard (`git reset --hard HEAD`) vers un commit différent qui a supprimé le dernier commit de votre branche actuelle.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Untitled-2022-06-21-2120.png)
_Explication du reset hard._

Dans ce cas, vous pouvez restaurer le fichier en utilisant soit `git checkout` soit `git reflog`.

Vous pouvez trouver le hash-ID du commit précédent à partir de la commande : `git log`.

Après cela, revenez simplement au commit précédent en utilisant :

```git
git checkout <hash-id>
```

Au cas où vous n'auriez pas le hash ID, vous pouvez utiliser la commande `git reflog`.

`reflog` est un mécanisme de journalisation et garde une trace de tous les changements contre leur `hash-id` unique.

Voici un exemple de la sortie de `git reflog` :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-155.png)
_Sortie de `git reflog`_

Choisissez l'ID de commit et utilisez-le pour revenir à ce commit.

```
git reflog <hash-id>
```

## Comment récupérer des fichiers lorsque les modifications sont indexées mais non validées

Supposons que vous avez indexé un fichier avec `git add <nom-du-fichier>` puis que vous avez fait un reset hard avec `git reset --hard HEAD` avant de valider. Ensuite, vous avez découvert que le fichier indexé est manquant. Dans ce cas également, vous pouvez récupérer les fichiers.

Nous pouvons utiliser la commande `git fsck` pour récupérer les fichiers après un reset hard.

### Qu'est-ce que `git fsck` ?

`git fsck` signifie file system check. Il vérifie tous les "blobs pendants" dans le répertoire `.git` qui ne font pas partie de quelque changement. Par exemple, il pourrait y avoir des changements qui étaient indexés mais non ajoutés quelque part.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-154.png)
_Sortie de `git fsck`._

Une fois que nous sommes en mesure d'identifier les "blobs pendants", nous pouvons voir les détails en utilisant `git show`.

```
git show f24facc98b387a375a50ba6d19193626cbfe7d45
```

Selon le changement, vous serez en mesure de voir vos changements respectifs.

Vous pourriez également vouloir sauvegarder les changements dans un fichier. Vous pouvez simplement rediriger la sortie vers un fichier en utilisant l'opérateur `>`.

```
git show f24facc98b387a375a50ba6d19193626cbfe7d45 > restored_file.txt
```

Maintenant, `restored_file.txt` inclura le contenu du commit.

## Comment restaurer des changements qui ne sont ni validés ni indexés

Dans le cas où les changements ne sont ni indexés ni validés, Git ne peut pas vous aider à récupérer les fichiers. 

La raison est que les fichiers n'ont pas été ajoutés à l'index et Git ne peut pas indiquer le statut de ces fichiers. 

Dans ce cas, il serait utile de rechercher dans les fichiers temporaires ou l'historique en cache de votre éditeur de texte.

## Conclusion

Lorsque vous travaillez sur des fichiers à risque, il est toujours préférable d'utiliser un VCS. De cette manière, les fichiers seront préservés et les risques de perte de données accidentelle seront réduits.

Dans ce tutoriel, nous avons appris comment restaurer des fichiers supprimés, qu'ils soient indexés ou validés. 

J'espère que vous avez trouvé ce tutoriel utile. Merci d'avoir lu jusqu'à la fin.

Quelle est votre chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez également lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).



##