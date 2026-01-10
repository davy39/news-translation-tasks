---
title: Git Undo Merge – Comment annuler le dernier Commit de Merge dans Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-30T17:40:00.000Z'
originalURL: https://freecodecamp.org/news/git-undo-merge-how-to-revert-the-last-merge-commit-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/puppy-g3ddb72a98_1920.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Undo Merge – Comment annuler le dernier Commit de Merge dans Git
seo_desc: 'Branching is an integral part of Git because it lets you work without tampering
  with code that''s already in production.

  When you finish working with a branch other than main, you''ll want to merge it
  with the main so the feature or bug fix you just in...'
---

Le branching est une partie intégrante de Git car il vous permet de travailler sans altérer le code déjà en production.

Lorsque vous avez terminé de travailler sur une branche autre que `main`, vous voudrez la fusionner (merger) avec la branche principale afin que la fonctionnalité ou la correction de bug que vous venez d'intégrer soit répercutée.

Mais que se passe-t-il si vous avez terminé le merge et que vous vous rendez compte que vous avez oublié de faire une chose de plus ? Ou si vous effectuez accidentellement un merge alors que vous n'êtes pas prêt ?

Vous pouvez annuler presque tout dans Git. Ainsi, dans cet article, je vais vous montrer comment annuler un merge dans Git afin de pouvoir revenir au dernier Commit que vous avez effectué.

## Comment annuler un Commit de Merge dans Git

Vous pouvez utiliser la commande Git reset pour annuler un merge. 

Tout d'abord, vous devez rechercher le hash (ou l'id) du Commit afin de pouvoir l'utiliser pour revenir au Commit précédent. 

Pour vérifier le hash, lancez `git log` ou `git reflog`. `git reflog` est une meilleure option car les informations y sont plus lisibles.
![ss1-2](https://www.freecodecamp.org/news/content/images/2022/03/ss1-2.png)

Lorsque vous obtenez le hash du Commit auquel vous souhaitez revenir, lancez `git reset --hard commit-before-the-merge` :
![ss-2-5](https://www.freecodecamp.org/news/content/images/2022/03/ss-2-5.png)

Vous devriez voir certains éléments être supprimés de votre éditeur de code lorsque vous lancez la commande.

Si vous n'êtes pas sûr du hash du dernier Commit, vous pouvez lancer `git reset --hard HEAD~1` pour revenir au Commit précédant le merge :
![ss-3-3](https://www.freecodecamp.org/news/content/images/2022/03/ss-3-3.png)

Notez que lorsque vous utilisez le flag `--hard` pour annuler un merge, tout changement non commité sera annulé.

## Une meilleure façon d'annuler un Merge dans Git

Étant donné que les méthodes mentionnées ci-dessus annuleront les modifications non commitées, Git propose un flag plus sûr qui est `--merge`. 

Pour annuler un merge avec le flag `--merge`, lancez `git reflog` pour voir les hashs des Commits, puis lancez `git reset --merge previous-commit` :
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/03/ss4-1.png)

Vous pouvez également utiliser le mot-clé HEAD avec le flag `--merge` en lançant `git reset --merge HEAD~1` :
![ss5](https://www.freecodecamp.org/news/content/images/2022/03/ss5.png)

**N.B.** : Si vous n'obtenez pas de réponse de cette commande lorsque vous utilisez le flag `--merge`, ne vous inquiétez pas, cela fonctionne.

## Conclusion
Dans cet article, vous avez appris comment annuler un merge dans Git, afin de pouvoir annuler un merge erroné ou indésirable et travailler plus efficacement avec Git.

Voici ce qu'il faut retenir des flags `--hard` et `--merge` lors de leur utilisation pour annuler un merge : le flag `--hard` supprime les modifications non commitées, tandis que le flag `--merge` conserve les modifications non commitées.

Merci de votre lecture !