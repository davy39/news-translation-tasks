---
title: Comment devenir un expert Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T22:55:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-become-a-git-expert-e7c38bf54826
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tJq8RS_Uv3R9s56E
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment devenir un expert Git
seo_desc: 'By Aditya Sridhar

  I made a mistake in my commit, how do I fix it ?

  My commit history is a mess, how do I make it neater?

  If you have ever had the above questions, then this post is for you. This post covers
  a list of topics which will make you a Git ...'
---

Par Aditya Sridhar

J'ai fait une erreur dans mon commit, comment puis-je la corriger ?

Mon historique de commits est un désordre, comment puis-je le rendre plus propre ?

Si vous vous êtes déjà posé les questions ci-dessus, alors cet article est fait pour vous. Cet article couvre une liste de sujets qui feront de vous un expert Git.

Si vous ne connaissez pas les bases de Git, [cliquez ici](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61) pour consulter mon blog sur les bases de Git. Il est nécessaire que vous connaissiez les bases de Git pour tirer le meilleur parti de cet article.

### J'ai fait une erreur dans mon commit. Que dois-je faire ?

![Image](https://cdn-media-1.freecodecamp.org/images/57nEHwVjqEC1a-ULvcaNS0dmO0uFsBQDUFk0)
_« assiette en céramique cassée sur le sol » par [Unsplash](https://unsplash.com/@chuttersnap?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">chuttersnap</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Scénario 1

Supposons que vous avez commis un ensemble de fichiers et que vous avez réalisé que le message de commit que vous avez entré n'est en fait pas clair. Maintenant, vous voulez changer le message de commit. Pour ce faire, vous pouvez utiliser `git commit --amend`

```bash
git commit --amend -m "Nouveau message de commit"
```

#### Scénario 2

Supposons que vous vouliez commettre six fichiers mais, par erreur, vous n'avez commis que cinq fichiers. Vous pourriez penser que vous pouvez créer un nouveau commit et ajouter le 6ème fichier à ce commit.

Il n'y a rien de mal avec cette approche. Mais, pour maintenir un historique de commits propre, ne serait-il pas plus agréable de pouvoir ajouter ce fichier à votre commit précédent ? Cela peut être fait via `git commit --amend` également :

```bash
git add file6
git commit --amend --no-edit
```

`--no-edit` signifie que le message de commit ne change pas.

#### Scénario 3

Lorsque vous faites un commit dans Git, le commit a un nom d'auteur et un email d'auteur qui lui sont associés. Généralement, lorsque vous configurez Git pour la première fois, vous configurez le nom d'auteur et l'email. Vous n'avez pas besoin de vous soucier des détails de l'auteur pour chaque commit.

Cela dit, il est possible que pour un projet particulier, vous souhaitiez utiliser une adresse email différente. Vous devez configurer l'email pour ce projet avec la commande :

```bash
git config user.email "votre email"
```

Supposons que vous ayez oublié de configurer l'email et que vous ayez déjà fait votre premier commit. `Amend` peut également être utilisé pour changer l'auteur de votre commit précédent. L'auteur du commit peut être changé en utilisant la commande suivante :

```bash
git commit --amend --author "Nom de l'Auteur <Email de l'Auteur>"
```

#### **Point à noter**

Utilisez la commande `amend` **uniquement** dans votre dépôt local. Utiliser `amend` pour le dépôt distant peut créer beaucoup de confusion.

### Mon historique de commits est un désordre. Comment puis-je le gérer ?

Supposons que vous travaillez sur un morceau de code. Vous savez que le code va prendre environ dix jours à compléter. Dans ces dix jours, les autres développeurs vont également commettre du code dans le dépôt distant.

C'est une **bonne pratique** de garder le code de votre dépôt local à jour avec le code du dépôt distant. Cela évite beaucoup de conflits de fusion plus tard lorsque vous créez une pull request. Vous décidez donc que vous allez tirer les changements du dépôt distant une fois tous les deux jours.

Chaque fois que vous tirez le code du dépôt distant vers le dépôt local, un nouveau commit de fusion est créé dans votre dépôt local. Cela signifie que votre historique de commits local va avoir beaucoup de commits de fusion, ce qui peut rendre les choses confuses pour le relecteur.

![Image](https://cdn-media-1.freecodecamp.org/images/Kf0bCgSdXtM1PJTZwn1FJ5-xPxJa7a3aSRZQ)
_Voici à quoi ressemblerait l'historique des commits dans votre dépôt local._

#### Comment rendre l'historique des commits plus propre ?

C'est là que le **rebase** vient à la rescousse.

#### Qu'est-ce que le rebasing ?

Permettez-moi de l'expliquer à travers un exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/HeXMQ3fwvXGfqiBCQJpYCRmzMTGkObShA4NS)
_Ce diagramme montre les commits dans la branche release et votre branche feature_

1. La branche Release a trois commits : Rcommit1, Rcommit2 et Rcommit3.
2. Vous avez créé votre branche Feature à partir de la branche Release lorsqu'elle n'avait qu'un seul commit, qui est Rcommit1.
3. Vous avez ajouté deux commits à la branche Feature. Ils sont Fcommit1 et Fcommit2.
4. Votre objectif est d'obtenir les commits de la branche Release dans votre branche Feature.
5. Vous allez utiliser rebase pour cela.
6. Soit le nom de la branche Release **release** et le nom de la branche Feature **feature**.
7. Le rebasing peut être fait en utilisant les commandes suivantes :

```bash
git checkout feature
git rebase release
```

#### Rebasing

Lors du rebasing, votre objectif est de vous assurer que la branche Feature obtient le dernier code de la branche Release.

Rebasing essaie d'ajouter chaque commit, un par un, et vérifie les conflits. Cela semble-t-il confus ?

Permettez-moi de l'expliquer à l'aide d'un diagramme.

Cela montre ce que le rebasing fait réellement en interne :

![Image](https://cdn-media-1.freecodecamp.org/images/iGgX4jvJOB8Gc2n8T1WSh8VpWEZqd1CoL2g3)

#### Étape 1

1. Dès que vous exécutez la commande, la branche Feature est pointée vers la tête de la branche Release.
2. Maintenant, la branche Feature a trois commits : Rcommit1, Rcommit2 et Rcommit3.
3. Vous vous demandez peut-être ce qui est arrivé à Fcommit1 et Fcommit2.
4. Les commits sont toujours là et seront utilisés dans les étapes ci-dessous.

#### **Étape 2**

1. Maintenant, Git essaie d'ajouter Fcommit1 à la branche Feature.
2. S'il n'y a pas de conflit, Fcommit1 est ajouté après Rcommit3
3. S'il y a un conflit, Git vous en informera et vous devrez résoudre le conflit manuellement. Après avoir résolu le conflit, utilisez les commandes suivantes pour continuer le rebasing

```bash
git add fixedfile
git rebase --continue
```

#### **Étape 3**

1. Une fois Fcommit1 ajouté, Git essaiera d'ajouter Fcommit2.
2. Encore une fois, s'il n'y a pas de conflit, Fcommit2 est ajouté après Fcommit1 et le rebase est réussi.
3. S'il y a un conflit, Git vous en informera et vous devrez le résoudre manuellement. Utilisez les mêmes commandes mentionnées dans l'étape 2 après avoir résolu les conflits
4. Après que tout le rebase soit terminé, vous remarquerez que la branche Feature a Rcommit1, Rcommit2, Rcommit3, Fcommit1 et Fcommit2.

#### Points à noter

1. Le rebase et la fusion sont tous deux utiles dans Git. L'un n'est pas meilleur que l'autre.
2. Dans le cas d'une fusion, vous aurez un commit de fusion. Dans le cas d'un rebase, il n'y a pas de commit supplémentaire comme un commit de fusion.
3. Une bonne pratique consiste à utiliser les commandes à différents moments. Utilisez rebase lorsque vous mettez à jour votre dépôt de code local avec le dernier code du dépôt distant. Utilisez la fusion lorsque vous traitez des pull requests pour fusionner la branche Feature avec la branche Release ou Master.
4. L'utilisation de Rebase altère l'historique des commits (il le rend plus propre). Mais cela dit, altérer l'historique des commits comporte des risques. Assurez-vous donc de ne jamais utiliser rebase sur un code qui se trouve dans le dépôt distant. Utilisez toujours rebase uniquement pour altérer l'historique des commits de votre code de dépôt local.
5. Si le rebase est effectué sur un dépôt distant, cela peut créer beaucoup de confusion puisque les autres développeurs ne reconnaîtront pas le nouvel historique.
6. De plus, si le rebase est effectué sur le dépôt distant, cela peut créer des problèmes lorsque les autres développeurs essaient de tirer le dernier code du dépôt distant. Je répète donc, utilisez toujours rebase uniquement pour le dépôt local.

### Félicitations 🎉

Vous êtes maintenant un expert Git 🎉

Dans cet article, vous avez appris :

* modifier les commits
* rebase

Ce sont deux concepts très utiles. Allez explorer le monde de Git pour en apprendre encore plus.

### À propos de l'auteur

J'aime la technologie et je suis les avancées dans ce domaine. J'aime aussi aider les autres avec mes connaissances technologiques.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

### Autres articles de moi

[Meilleures pratiques lors de l'utilisation de Git](https://adityasridhar.com/posts/how-you-can-go-wrong-with-git)

[Une introduction à Git](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61)

[Comment utiliser Git efficacement](https://medium.freecodecamp.org/how-to-use-git-efficiently-54320a236369)