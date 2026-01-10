---
title: Maintenant que vous n'avez plus peur de GIT, voici comment tirer parti de ce
  que vous savez
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T18:10:06.000Z'
originalURL: https://freecodecamp.org/news/now-that-youre-not-afraid-of-git-anymore-here-s-how-to-leverage-what-you-know-11e710c7f37b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8rQSJ7R76i_N0r-LjULBZw.jpeg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Maintenant que vous n'avez plus peur de GIT, voici comment tirer parti
  de ce que vous savez
seo_desc: 'By Neil Kakkar

  The first part of this series looked at the inner workings of GIT and showed you
  how not to be afraid of working with Git.

  Now that we understand how Git works, let’s get into the meaty stuff: how to leverage
  what we know in our projec...'
---

Par Neil Kakkar

[La première partie de cette série a examiné le fonctionnement interne de GIT](https://medium.freecodecamp.org/how-not-to-be-afraid-of-git-anymore-fe1da7415286) et vous a montré comment ne plus avoir peur de travailler avec Git.

Maintenant que nous comprenons comment Git fonctionne, plongeons dans le vif du sujet : comment tirer parti de ce que nous savons dans nos projets.

### Fusion

Fusion _fusionne_ votre code.

Vous souvenez-vous comment nous suivions les bonnes pratiques Git, en ayant des branches pour diverses fonctionnalités sur lesquelles nous travaillons, et pas tout sur `master` ? Il viendra un moment où vous aurez terminé cette fonctionnalité et voudrez l'inclure dans votre `master`. C'est là que `merge` intervient. Vous voulez **fusionner** votre branche dans master.

Il existe 2 types de fusions :

#### Fusion rapide (Fast forward merge)

Revenons à notre exemple de la dernière fois :

C'est aussi simple que de déplacer l'étiquette pour `master` vers `the-ending`. Git n'a aucun doute sur ce qui doit être fait — puisque notre "arbre" avait une seule liste liée de nœuds.

```
$ git branch
  master
* the-ending
$ git checkout master
Switched to branch 'master'
$ git merge the-ending
Updating a39b9fd..b300387
Fast-forward
 byeworld | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 byeworld
```

#### Fusion non rapide (Non-Fast Forward Merge)

C'est le type de fusion où Git ne sait pas quoi faire. Il y a des changements sur la branche de base, et d'autres sur la branche que nous voulons fusionner, ce qui entraîne les redoutables _conflits de fusion_ !

Voici la première chose à savoir sur les conflits de fusion : Si vous ne savez pas ce qui se passe :

```
git merge --abort
```

Cela vous ramènera à l'état original, sans effets secondaires. Vous venez d'annuler le désordre que vous alliez faire.

![Image](https://cdn-media-1.freecodecamp.org/images/HAWGpuc2gjD5wYOk9UbaPNorlFq4dXA5FRFU)
_[Vous ne voulez pas être Brian ?](http://www.quickmeme.com/p/3vzhql" rel="noopener" target="_blank" title=")_

Allons-y étape par étape pour résoudre les conflits de fusion.

```
$ git checkout -b the-middle
Switched to a new branch 'the-middle'
```

En continuant notre style, apprenons via un exemple. Je modifie `helloworld` sur la branche `the-middle`.

```
$ git diff
diff --git a/helloworld b/helloworld
index a042389..e702052 100644
--- a/helloworld
+++ b/helloworld
@@ -1 +1,3 @@
 hello world!
+
+Middle World
```

Ajoutez et validez sur `the-middle`.

Ensuite, je passe à `master` et modifie `helloworld` sur master. J'ajoute ce qui suit :

```
$ git diff --cached
diff --git a/helloworld b/helloworld
index a042389..ac7a733 100644
--- a/helloworld
+++ b/helloworld
@@ -1 +1,3 @@
 hello world!
+
+Master World
```

Voyez-vous pourquoi j'ai dû faire `git diff --cached` ici ? Si ce n'est pas le cas, demandez-moi ci-dessous !

Maintenant, il est temps de fusionner !

```
$ git merge the-middle
Auto-merging helloworld
CONFLICT (content): Merge conflict in helloworld
Automatic merge failed; fix conflicts and then commit the result.
```

Lorsque `merge` échoue, voici ce que fait git : il modifie le fichier avec la fusion pour vous montrer exactement ce qu'il ne peut pas décider.

```
$ cat helloworld 
hello world!
```

```
$ cat helloworld 
hello world!
<<<<<<< HEAD
Master World
=======
Middle World
>>>>>>> the-middle
```

Cela a-t-il du sens ? La partie `<<<<< HEAD` est la nôtre (la branche de base) et la partie `>>>>> the-middle` est `la leur` (la branche fusionnée dans la branche de base).

Vous pouvez simplement modifier le fichier pour supprimer les éléments supplémentaires ajoutés par git et choisir ce qui doit aller dans `helloworld` finalement. Il existe des outils et des intégrations d'éditeur pour faciliter cela, mais je pense que savoir comment cela fonctionne sous le capot vous donne plus de confiance lorsque vous n'avez pas votre éditeur préféré à portée de main.

```
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)
Unmerged paths:
  (use "git add <file>..." to mark resolution)
both modified:   helloworld
```

J'ai décidé de garder les deux parties.

```
$ cat helloworld 
hello world!
Master World
Middle World
```

Et voilà :

```
$ git add helloworld 
$ git commit -m "resolve merge conflict"
[master c747e68] resolve merge conflict
```

### Dépôts distants

Puisque l'un des pouvoirs du contrôle de version est de sauvegarder votre code en cas de catastrophe — les dépôts distants sont là pour aider. Un dépôt distant est une copie de votre dépôt git hébergée à l'extérieur. Pour être plus précis, un dépôt distant est un dépôt externe (pas nécessairement du même code que vous avez). Par externe, il pourrait être dans un dossier différent sur votre système ou dans le cloud.

#### Cloner

Cloner _clone_ le dépôt distant dans votre répertoire de travail actuel. Cela consiste simplement à créer une copie du dossier `.git/`, qui nous donne l'historique complet et les fichiers nécessaires pour remplir le répertoire de travail.

```
git clone <repository-url>
```

Si vous n'avez pas cloné, vous n'avez probablement pas de dépôt distant. Vous pouvez créer un dépôt distant comme ceci :

```
git remote add <name> <url>
```

### Pousser et Tirer

Pousser et Tirer sont des actions appliquées sur le `dépôt distant`.

Pousser _pousse_ vos changements vers le dépôt distant. Donc, nous envoyons l'`Index` et les `Objets` correspondants depuis le magasin d'objets !

```
git push <name of remote> <name of branch>
```

Tirer _tire_ le code depuis le dépôt distant. Exactement comme avant, nous copions l'`Index` et les `Objets` correspondants depuis le magasin d'objets !

```
git pull origin master
```

`origin` est le nom par défaut du dépôt distant. Et puisque `master` est la branche par défaut, vous pouvez voir comment la commande se simplifie en le nom simple que nous trouvons partout : `git pull origin master`. Maintenant, vous en savez plus.

### Réinitialiser

Réinitialiser _réinitialise_ votre base de code à une version précédente. Réinitialiser vient avec 3 options :

`--soft`, `--hard` et `--mixed`.

La beauté de `reset`, c'est de pouvoir changer l'historique. Supposons que vous faites une erreur avec un `commit`, et maintenant votre `git log` est tout désordonné avec des commits comme :

`Bugfix`

`Final BugFix`

`Final Final BugFix`

`God why isn't this working last try bug fix`

Si vous voulez garder votre historique `master` propre, vous voulez nettoyer cet historique de commits.

Si vous envoyez une Pull Request où il n'y a pas de squashing, ils s'attendront également à un historique de commits propre !

C'est là que `reset` intervient : Vous pourriez `reset` tous vos commits et les convertir en un seul commit : `got stuff done!`

(Veuillez ne pas utiliser cela comme message de commit — suivez les meilleures pratiques !)

Revenons à notre exemple, voici ce que j'ai fait.

```
$ git log
commit 959781ec78c970d4797c5e938ec154de44d0151b (HEAD -> master)
Author: Neil Kakkar
Date:   Mon Nov 5 07:32:55 2018 +0000
God why isn't this working last final BugFix
commit affa90c0db78999d22c326fdbd6c1d5057228822
Author: Neil Kakkar
Date:   Mon Nov 5 07:32:19 2018 +0000
Final Final BugFix
commit 2e9570cffc0a8206132d75c402d68351eda450bd
Author: Neil Kakkar
Date:   Mon Nov 5 07:31:49 2018 +0000
Final BugFix
commit 4560fc0ec6305d0b7bcfb4be1901438fd126d6d1
Author: Neil Kakkar
Date:   Mon Nov 5 07:31:21 2018 +0000
BugFix
commit c747e6891af419119fd817dc69a2e122084aedae
Merge: 3d01508 fb8b2fc
Author: Neil Kakkar
Date:   Tue Oct 23 07:44:09 2018 +0100
resolve merge conflict
```

Maintenant que le bug est corrigé, je veux nettoyer mon historique avant de pousser vers `master`. Cela fonctionnerait également bien — lorsque, par exemple, je réalise plus tard que j'ai introduit un autre bug et que je dois revenir à la version précédente. Dans ce cas, `c747e689` n'a pas le meilleur message de commit pour comprendre cela.

```
$ git reset c747e6891af419119fd817dc69a2e122084aedae
$ git log
commit c747e6891af419119fd817dc69a2e122084aedae (HEAD -> master)
Merge: 3d01508 fb8b2fc
Author: Neil Kakkar
Date:   Tue Oct 23 07:44:09 2018 +0100
resolve merge conflict
```

Voilà, tout est trié ?

```
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
      clean.txt
nothing added to commit but untracked files present (use "git add" to track)
```

`clean.txt` est le fichier que j'avais validé pour la correction du bug. Maintenant, tout ce que j'ai à faire est :

```
$ git add clean.txt 
$ git commit -m "fix bug: Unable to clean folder"
[master d8487ca] fix bug: Unable to clean folder
 1 file changed, 4 insertions(+)
 create mode 100644 clean.txt
$ git log
commit d8487ca8b9acfa9666bdf2c6b7fa27b3971bd957 (HEAD -> master)
Author: Neil Kakkar
Date:   Mon Nov 5 07:41:41 2018 +0000
fix bug: Unable to clean folder
commit c747e6891af419119fd817dc69a2e122084aedae
Merge: 3d01508 fb8b2fc
Author: Neil Kakkar
Date:   Tue Oct 23 07:44:09 2018 +0100
resolve merge conflict
```

Voilà, c'est fait. Pouvez-vous deviner maintenant, en utilisant les indices du `log`, la syntaxe de la commande `reset` et votre sens technique pour comprendre comment cela fonctionne en coulisses ?

`Reset` coupe l'arbre de commits au commit spécifié. Toutes les étiquettes pour cette branche — si elles sont en avance — sont déplacées vers le commit spécifié. Les fichiers existants restent-ils dans le magasin d'objets ? Vous savez comment vérifier cela maintenant, Ace.

Les fichiers sont également supprimés de la zone de staging. Maintenant, cela pourrait être un problème si vous avez beaucoup de fichiers non suivis/modifiés que vous ne voulez pas ajouter.

Comment faites-vous cela ?

Pouvez-vous relever l'indice que j'ai laissé au début de cette section ?

Les options de comportement !

`--soft` garde tous les fichiers en staging.

```
$ git reset --soft c747e6891af419119fd817dc69a2e122084aedae
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
new file:   clean.txt
```

`--mixed` est l'option par défaut : Supprime tous les fichiers de la zone de staging également.

`--hard` est hardcore. Supprime les fichiers du magasin d'objets — et du répertoire également. À utiliser avec une extrême prudence. Voici ma correction de bug*. Partie.

```
$ git reset --hard c747e6891af419119fd817dc69a2e122084aedae
HEAD is now at c747e68 resolve merge conflict
$ git status
On branch master
nothing to commit, working tree clean
```

*Eh bien, pas complètement. Git est incroyable. Avez-vous entendu parler des méta-méta données ? Un journal de redondance de ce qui s'est passé dans le dépôt ? Oui, bien sûr, git le garde !

```
$ git reflog
c747e68 (HEAD -> master) HEAD@{0}: reset: moving to c747e6891af419119fd817dc69a2e122084aedae
efc6d21 HEAD@{1}: commit: soft reset
c747e68 (HEAD -> master) HEAD@{2}: reset: moving to c747e6891af419119fd817dc69a2e122084aedae
d8487ca HEAD@{3}: commit: fix bug: Unable to clean folder
c747e68 (HEAD -> master) HEAD@{4}: reset: moving to c747e6891af419119fd817dc69a2e122084aedae
959781e HEAD@{5}: commit: God why isn't this working last final BugFix
affa90c HEAD@{6}: commit: Final Final BugFix
2e9570c HEAD@{7}: commit: Final BugFix
4560fc0 HEAD@{8}: commit: BugFix
c747e68 (HEAD -> master) HEAD@{9}: commit (merge): resolve merge conflict
3d01508 HEAD@{10}: commit: add Master World
b300387 (the-ending) HEAD@{11}: checkout: moving from the-middle to master
fb8b2fc (the-middle) HEAD@{12}: commit: add Middle World
b300387 (the-ending) HEAD@{13}: checkout: moving from master to the-middle
b300387 (the-ending) HEAD@{14}: checkout: moving from the-middle to master
b300387 (the-ending) HEAD@{15}: checkout: moving from master to the-middle
b300387 (the-ending) HEAD@{16}: merge the-ending: Fast-forward
a39b9fd HEAD@{17}: checkout: moving from the-ending to master
b300387 (the-ending) HEAD@{18}: checkout: moving from master to the-ending
a39b9fd HEAD@{19}: checkout: moving from the-ending to master
b300387 (the-ending) HEAD@{20}: commit: add byeworld
a39b9fd HEAD@{21}: checkout: moving from master to the-ending
a39b9fd HEAD@{22}: commit (initial): Add helloworld
```

C'est tout depuis le début de l'exemple dans l'article précédent. Cela signifie-t-il que je peux récupérer des choses si j'ai fait une erreur terrible ?

```
$ git checkout d8487ca
Note: checking out 'd8487ca'.
You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.
If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:
git checkout -b <new-branch-name>
HEAD is now at d8487ca... fix bug: Unable to clean folder

$ ls
byeworld clean.txt  helloworld
```

Voilà.

Félicitations, vous êtes maintenant un Ninja Git — Apprenti.

Y a-t-il autre chose que vous aimeriez savoir ? Quelque chose qui vous a dérouté à propos de Git ? Faites-le moi savoir ci-dessous ! J'essaierai de l'expliquer comme je l'ai appris !

Vous avez aimé cela ? [Ne manquez plus un article — abonnez-vous à ma liste de diffusion !](http://neilkakkar.com/subscribe/)