---
title: Comment renommer une branche locale ou distante dans Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-10T19:03:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-rename-a-local-or-remote-branch-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/git.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment renommer une branche locale ou distante dans Git
seo_desc: "Git is a version control system that software developers use to keep track\
  \ of changes in their applications and collaborate with others. \nOne helpful feature\
  \ of Git is branches. Different people working on a software project can work in\
  \ different bra..."
---

Git est un système de contrôle de version que les développeurs de logiciels utilisent pour suivre les modifications de leurs applications et collaborer avec d'autres.

Une fonctionnalité utile de Git est les branches. Différentes personnes travaillant sur un projet logiciel peuvent travailler dans différentes branches avant de fusionner leurs modifications avec le code original.

Vous pouvez également ajouter de nouvelles fonctionnalités et corriger des bugs sur une branche différente sans affecter le code original.

Parfois, vous pouvez vouloir changer le nom d'une branche en raison de fautes de frappe ou d'autres erreurs, et c'est ce que je vais vous montrer comment faire dans ce guide.

## Comment renommer une branche Git locale
**Étape 1** : Pour voir les branches que vous avez, exécutez `git branch --list` ou `git branch -a`
![ss-1-2](https://www.freecodecamp.org/news/content/images/2022/03/ss-1-2.png)

**Étape 2** : Passez à la branche que vous souhaitez renommer en exécutant `git checkout nom-de-la-branche`.

Dans ce cas, je vais passer à la branche `mistake-fixes` pour la renommer `bug-fixes`.

Pour passer à une branche, exécutez `git switch nom-de-la-branche` ou `git checkout nom-de-la-branche`.

**Étape 3** : Pour renommer la branche, exécutez `git branch -m nouveau-nom`
![ss-2-2](https://www.freecodecamp.org/news/content/images/2022/03/ss-2-2.png)

Vous pouvez voir que la branche a été renommée de `mistake-fixes` à `bug-fixes`.

Si vous êtes sur une autre branche, par exemple, main et que vous souhaitez renommer la branche depuis là, exécutez `git branch -m ancien-nom nouveau-nom`.

**N.B.** : Assurez-vous de vérifier que la branche a été renommée en exécutant `git branch -a` pour voir toutes les branches.

## Comment renommer une branche Git distante
Renommer une branche distante n'est pas aussi simple que renommer une branche locale.

Pour être précis, renommer une branche distante n'est pas direct – vous devez supprimer l'ancien nom de la branche distante puis pousser un nouveau nom de branche vers le dépôt.

**Suivez les étapes ci-dessous pour renommer une branche git distante** :

**Étape 1** : Supprimez l'ancien nom en exécutant `git push origin --delete ancien-nom-de-branche`.

Dans l'exemple que j'ai utilisé, cela serait `git push origin --delete mistake-fixes`.
![ss-3-1](https://www.freecodecamp.org/news/content/images/2022/03/ss-3-1.png)

**Étape 2** : Réinitialisez la branche amont au nom de votre nouvelle branche locale en exécutant `git push origin -u nouveau-nom-de-branche`.

Donc, pour l'exemple, cela serait `git push origin -u bug-fixes`.
![ss-4-1](https://www.freecodecamp.org/news/content/images/2022/03/ss-4-1.png)

Pour confirmer que vous avez renommé avec succès le dépôt distant, connectez-vous au site web de votre client et vérifiez le dépôt.

Dans le cas de ce tutoriel, j'utilise Github comme client et le renommage a été réussi :
![ss-5-1](https://www.freecodecamp.org/news/content/images/2022/03/ss-5-1.png)

## Conclusion

Les branches sont une fonctionnalité géniale de Git qui rendent votre projet logiciel hébergé plus sûr.

Souvent, renommer des branches localement et à distance peut être inévitable, c'est pourquoi j'ai écrit cet article pour vous aider à renommer vos branches sans erreurs coûteuses.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.

Merci d'avoir lu.