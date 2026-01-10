---
title: Git Supprimer une Branche Distante – Comment Supprimer une Branche Distante
  dans Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-16T17:20:10.000Z'
originalURL: https://freecodecamp.org/news/git-delete-remote-branch
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-nidhi-tokas-dahiya-867677.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Git Supprimer une Branche Distante – Comment Supprimer une Branche Distante
  dans Git
seo_desc: 'When you''re working with Git, you might want to delete remote branches
  pushed to a platform like GitHub for various reasons.

  In this article, I will show you how to delete a remote branch in Git. But firstly,
  let’s look at how to delete a local branc...'
---

Lorsque vous travaillez avec Git, vous pourriez vouloir supprimer des branches distantes poussées vers une plateforme comme GitHub pour diverses raisons.

Dans cet article, je vais vous montrer comment supprimer une branche distante dans Git. Mais d'abord, examinons comment supprimer une branche locale.

J'utiliserai Git bash dans cet article car cela facilite le travail avec Git plus que tout autre terminal. Mais ce n'est pas grave si vous utilisez un autre terminal. Les commandes restent les mêmes.

## Comment Supprimer une Branche Locale dans Git
Exécutez `git branch` ou `git branch -a` pour voir les branches que vous avez créées pour votre projet.
![ss1-3](https://www.freecodecamp.org/news/content/images/2022/08/ss1-3.png) 

Si vous exécutez `git branch -a` en particulier, cela rendra les branches distantes distinctes. C'est une fonctionnalité que j'ai vue uniquement dans Git bash.
![ss2-3](https://www.freecodecamp.org/news/content/images/2022/08/ss2-3.png)

Dans cette situation, `test-branch2` est une branche que je n'ai pas encore poussée, donc c'est une branche locale.

Pour supprimer une branche locale, exécutez `git branch -d nom-de-la-branche`.

Si vous tapez la commande correctement, vous obtiendrez une réponse indiquant que la branche a été supprimée.
![ss3-3](https://www.freecodecamp.org/news/content/images/2022/08/ss3-3.png)

## Comment Supprimer une Branche Distante dans Git

Si vous essayez de supprimer une branche distante avec la même commande utilisée pour supprimer une branche locale, vous obtiendrez un message indiquant que la branche a été supprimée. Mais si vous exécutez `git branch -a`, la branche sera toujours listée.
![ss4-4](https://www.freecodecamp.org/news/content/images/2022/08/ss4-4.png)

Et si vous vérifiez GitHub, la branche sera toujours là :
![ss5-4](https://www.freecodecamp.org/news/content/images/2022/08/ss5-4.png) 

Pour supprimer complètement une branche distante, vous devez utiliser la commande `git push origin` avec un drapeau `-d`, puis spécifier le nom de la branche distante.

La syntaxe représentant la commande pour supprimer une branche distante ressemble à ceci : `git push origin -d nom-de-la-branche`.

Par exemple, pour supprimer la branche `test-branch1`, j'exécuterai `git push origin -d test-branch1` :
![ss6-3](https://www.freecodecamp.org/news/content/images/2022/08/ss6-3.png) 

Pour vérifier que la branche distante a été supprimée, exécutez à nouveau `git branch -a`.
![ss7-2](https://www.freecodecamp.org/news/content/images/2022/08/ss7-2.png) 

Vous pouvez voir que la branche distante, `test-branch1`, n'est plus listée.

Si vous vérifiez à nouveau GitHub, elle n'y sera plus :
![ss8-2](https://www.freecodecamp.org/news/content/images/2022/08/ss8-2.png) 

## Conclusion

Gardez à l'esprit que pour supprimer complètement une branche Git de votre projet, vous devez utiliser la commande `git push origin`.

C'est parce que vous avez déjà poussé la branche. Ainsi, exécuter la commande `git branch -d` ne supprimerait la branche qu'en local. 

Et si vous avez des problèmes avec Git, je vous suggère de passer votre terminal à Git bash. C'est parce qu'il a une coloration syntaxique pour tout – ce qui facilite le travail avec Git.

Merci d'avoir lu.