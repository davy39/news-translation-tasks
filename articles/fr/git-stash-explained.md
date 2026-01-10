---
title: 'Git Stash Expliqué : Comment Stocker Temporairement des Modifications Locales
  dans Git'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T07:23:00.000Z'
originalURL: https://freecodecamp.org/news/git-stash-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d6f740569d1a4ca37bf.jpg
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: version control
  slug: version-control
seo_title: 'Git Stash Expliqué : Comment Stocker Temporairement des Modifications
  Locales dans Git'
seo_desc: 'Git has an area called the stash where you can temporarily store a snapshot
  of your changes without committing them to the repository. It’s separate from the
  working directory, the staging area, or the repository.

  This functionality is useful when yo...'
---

Git possède une zone appelée le stash où vous pouvez stocker temporairement une capture instantanée de vos modifications sans les valider dans le dépôt. Elle est séparée du répertoire de travail, de la zone de préparation ou du dépôt.

Cette fonctionnalité est utile lorsque vous avez apporté des modifications à une branche que vous n'êtes pas prêt à valider, mais que vous devez basculer vers une autre branche.

### Stocker des Modifications

Pour sauvegarder vos modifications dans le stash, exécutez la commande :

```shell
git stash save "message optionnel pour vous-même"
```

Cela sauvegarde vos modifications et rétablit le répertoire de travail tel qu'il était pour le dernier commit. Les modifications stashées sont disponibles à partir de n'importe quelle branche de ce dépôt.

Notez que les modifications que vous souhaitez stasher doivent être sur des fichiers suivis. Si vous avez créé un nouveau fichier et que vous essayez de stasher vos modifications, vous pourriez obtenir l'erreur `No local changes to save`.

### Voir les Modifications Stashées

Pour voir ce qui se trouve dans votre stash, exécutez la commande :

```shell
git stash list
```

Cela retourne une liste de vos captures instantanées sauvegardées au format `stash@{0}: BRANCH-STASHED-CHANGES-ARE-FOR: MESSAGE`. La partie `stash@{0}` est le nom du stash, et le nombre entre les accolades (`{ }`) est l'index de ce stash. Si vous avez plusieurs ensembles de modifications stashés, chacun aura un index différent.

Si vous avez oublié quelles modifications ont été faites dans le stash, vous pouvez voir un résumé avec `git stash show NAME-OF-STASH`. Si vous souhaitez voir le format de patch style diff typique (avec les + et - pour les changements ligne par ligne), vous pouvez inclure l'option `-p` (pour patch). Voici un exemple :

```shell
git stash show -p stash@{0}

# Exemple de résultat :
diff --git a/PathToFile/fileA b/PathToFile/fileA
index 2417dd9..b2c9092 100644
--- a/PathToFile/fileA
+++ b/PathToFile/fileA
@@ -1,4 +1,4 @@
-What this line looks like on branch
+What this line looks like with stashed changes
```

### Récupérer les Modifications Stashées

Pour récupérer les modifications du stash et les appliquer à la branche actuelle sur laquelle vous vous trouvez, vous avez deux options :

1. `git stash apply STASH-NAME` applique les modifications et laisse une copie dans le stash
2. `git stash pop STASH-NAME` applique les modifications et supprime les fichiers du stash

Il peut y avoir des conflits lorsque vous appliquez des modifications. Vous pouvez résoudre les conflits de manière similaire à une fusion ([voir `git merge` pour plus de détails](https://www.freecodecamp.org/news/the-ultimate-guide-to-git-merge-and-git-rebase/)).

### Supprimer les Modifications Stashées

Si vous souhaitez supprimer les modifications stashées sans les appliquer, exécutez la commande :

```shell
git stash drop STASH-NAME
```

Pour vider entièrement le stash, exécutez la commande :

```shell
git stash clear
```