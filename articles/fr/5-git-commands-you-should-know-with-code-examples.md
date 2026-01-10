---
title: 5 commandes Git que vous devriez connaître, avec des exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-09T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/5-git-commands-you-should-know-with-code-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a67740569d1a4ca2575.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Git
  slug: git
- name: Software Engineering
  slug: software-engineering
seo_title: 5 commandes Git que vous devriez connaître, avec des exemples de code
seo_desc: 'By Sarah Chima Atuonwu

  I''ve used Git for some years now, and I still find myself googling how to do some
  basic tasks. So this article is my attempt to learn how to do some of these things
  by writing about them. And even if I still forget, at least I''...'
---

Par Sarah Chima Atuonwu

J'utilise Git depuis quelques années maintenant, et je me surprends encore à chercher sur Google comment effectuer certaines tâches de base. Cet article est donc ma tentative d'apprendre à faire certaines de ces choses en écrivant à leur sujet. Et même si j'oublie encore, au moins j'aurai une référence où je pourrai facilement trouver ces commandes – et vous aussi.

Avant de passer à l'apprentissage de ces choses, quelque chose qu'un collègue m'a dit un jour est resté avec moi. Il m'a dit que tout est possible avec Git et que rien n'est perdu dans Git. 

Je ne sais pas si la première partie de sa déclaration est entièrement vraie, mais je la garde à l'esprit chaque fois que j'essaie de faire quelque chose avec Git. Je crois que je vais trouver une commande qui m'aidera à faire ce dont j'ai besoin. Je dois simplement chercher sur Google avec les bons mots. Si vous êtes nouveau dans Git, je veux que vous y croyiez aussi.

Dans cet article, nous apprendrons à faire ce qui suit :

1. Ajouter des dépôts distants
2. Changer les dépôts distants
3. Supprimer une branche
4. Fusionner un fichier d'une branche à une autre
5. Annuler un commit localement et à distance

Bien que cet article soit destiné aux personnes ayant une connaissance de base de Git, je ferai de mon mieux pour expliquer les termes autant que possible.

## 1. Ajouter des dépôts distants

Les dépôts distants sont des versions de vos projets qui sont stockées sur Internet ou ailleurs. Ajouter un dépôt distant est une façon de dire à Git où votre code est stocké. 

Nous pouvons le faire en utilisant l'URL du dépôt. Cela pourrait être l'URL de votre dépôt, le fork d'un autre utilisateur, ou même un serveur complètement différent.

Lorsque vous clonez un dépôt, Git ajoute implicitement ce dépôt comme dépôt distant `origin` pour vous. Pour ajouter un nouveau dépôt Git, vous utilisez cette commande :

```text
git remote add <shortname> <url>
```

où `shortname` est un nom de dépôt distant unique et `url` est l'URL du dépôt que vous souhaitez ajouter.

Par exemple, si je veux ajouter un dépôt avec le nom court `upstream`, je peux faire ceci :

```text
git remote add upstream https://github.com/sarahchima/personal-website.git
```

Rappelez-vous que votre `shortname` peut être n'importe quoi, il doit simplement être unique, c'est-à-dire différent des noms des dépôts distants que vous avez déjà. Il doit également être quelque chose que vous pouvez facilement retenir pour votre santé mentale.

Pour voir la liste des URL distantes que vous avez ajoutées, exécutez la commande suivante :

```text
git remote -v
```

Vous verrez une liste des noms distants et des URL que vous avez ajoutées.

Mais que faire si vous voulez changer ces URL distantes ? Passons à la commande Git suivante.

## 2. Changer les dépôts distants

Il existe plusieurs raisons pour lesquelles vous pourriez vouloir changer une URL distante. Par exemple, j'ai récemment dû passer de l'utilisation des URL `https` aux URL `SSH` pour un projet sur lequel j'ai travaillé.

Pour ce faire, vous utilisez la commande suivante :

```text
git remote set-url <an-existing-remote-name> <url>
```

Pour que cette commande fonctionne, le nom distant doit être un nom distant existant. Cela signifie qu'elle ne fonctionnera pas si vous n'avez pas ajouté ce nom distant auparavant.

En utilisant l'exemple ci-dessus, si je veux changer l'URL distante, je ferai ceci :

```text
git remote set-url upstream git@github.com:sarahchima/personal-website.git
```

N'oubliez pas d'exécuter `git remote -v` pour vérifier que votre changement a fonctionné.

Assez parlé des dépôts distants. Passons à quelque chose de différent.

## 3. Supprimer une branche localement et à distance

Une branche est une version du dépôt qui est différente du projet de travail principal. Vous pourriez vouloir lire sur les branches Git et comment ajouter une branche si vous n'êtes pas familier avec ce processus.

### Comment supprimer une branche locale

Pour supprimer une branche localement, assurez-vous de ne pas être sur la branche que vous souhaitez supprimer. Vous devez donc basculer vers une autre branche et utiliser la commande suivante :

```text
git branch -d <name-of-branch>
```

Donc, si je veux supprimer une branche nommée `fix/homepage-changes`, je ferai ce qui suit :

```text
git branch -d fix/homepage-changes
```

Vous pouvez exécuter `git branch` sur votre terminal pour confirmer que la branche a été supprimée avec succès.

Parfois, vous devrez peut-être supprimer une branche que vous avez déjà poussée vers un dépôt distant. Comment pouvez-vous faire cela ?

### Comment supprimer une branche distante

Pour supprimer une branche à distance, vous utilisez la commande suivante :

```text
git push <remote-name> --delete <name-of-branch>
```

où `remote-name` est le nom du dépôt distant dont vous souhaitez supprimer la branche.

Si je veux supprimer la branche `fix/homepage-changes` de `origin`, je ferai ceci :

```text
git push origin --delete fix/homepage-changes
```

La branche sera supprimée à distance maintenant.

## 4. Fusionner un fichier d'une branche à une autre

Parfois, vous pourriez vouloir fusionner le contenu d'un fichier spécifique dans une branche vers une autre. Par exemple, vous voulez fusionner le contenu d'un fichier `index.html` dans la branche `master` d'un projet vers la branche `development`. Comment pouvez-vous faire cela ?

Tout d'abord, basculez vers la bonne branche (la branche dans laquelle vous souhaitez fusionner le fichier) si vous ne l'avez pas déjà fait. Dans notre cas, c'est la branche `development`.

```text
git checkout development
```

Ensuite, fusionnez le fichier en utilisant la commande checkout --patch.

```text
git checkout --patch master index.html
```

Si vous souhaitez complètement écraser le fichier `index.html` sur la branche `development` avec celui sur la branche `master`, vous omettez le drapeau `--patch`.

```text
git checkout master index.html
```

De plus, omettez le drapeau `--patch` si le fichier `index.html` n'existe pas sur la branche `development`.

## 5. Annuler un commit

Il arrive que vous ayez commis vos changements incorrectement et que vous souhaitiez annuler ce commit. Parfois, vous avez peut-être même poussé les changements vers une branche distante. Comment annuler ou supprimer ce commit ? Commençons par annuler un commit local.

### Comment annuler un commit local

Une façon d'annuler un commit localement est d'utiliser `git reset`. Par exemple, si vous souhaitez annuler le dernier commit effectué, vous pouvez exécuter cette commande :

```text
git reset --soft HEAD~1
```

Le drapeau `--soft` préserve les changements que vous avez apportés aux fichiers que vous avez commis, seul le commit est annulé. Cependant, si vous ne souhaitez pas conserver les changements apportés aux fichiers, vous pouvez utiliser le drapeau `--hard` comme ceci :

```text
git reset --hard HEAD~1
```

Notez que vous devez utiliser le drapeau `--hard` uniquement lorsque vous êtes sûr de ne pas avoir besoin des changements.

De plus, notez que `HEAD~1` pointe vers le dernier commit. Si vous souhaitez annuler un commit avant celui-ci, vous pouvez utiliser `git reflog` pour obtenir un journal de tous les commits précédents. Ensuite, utilisez la commande `git reset` avec le hash du commit (le numéro que vous obtenez au début de chaque ligne d'historique). Par exemple, si mon hash de commit est `9157b6910`, je ferai ceci :

```text
git reset --soft 9157b6910 
```

### Comment annuler un commit distant

Il arrive que vous souhaitiez annuler un commit que vous avez poussé vers un dépôt distant. Vous pouvez utiliser `git revert` pour l'annuler localement et pousser ce changement vers la branche distante.

Tout d'abord, obtenez le hash du commit en utilisant git reflog.

```text
git reflog
```

Ensuite, annulez-le. En supposant que mon hash de commit est 9157b6910, je ferai ce qui suit :

```text
git revert 9157b6910 
```

Enfin, poussez ce changement vers la branche distante.

## Résumé

Dans cet article, nous avons discuté des commandes pour faire ce qui suit dans Git :

1. Ajouter des dépôts distants
2. Changer les dépôts distants
3. Supprimer une branche
4. Fusionner un fichier d'une branche à une autre
5. Annuler un commit localement et à distance

Peut-être qu'un jour, j'écrirai sur d'autres choses que vous pouvez faire avec Git.

J'espère que vous avez apprécié l'article. Merci d'avoir lu.

_Voulez-vous être informé lorsque je publie un nouvel article ? [Cliquez ici](https://mailchi.mp/69ea601a3f64/join-sarahs-mailing-list)._