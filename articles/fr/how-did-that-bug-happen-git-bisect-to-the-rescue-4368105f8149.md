---
title: Comment ce bug est-il arrivé ? Git bisect à la rescousse !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T19:59:32.000Z'
originalURL: https://freecodecamp.org/news/how-did-that-bug-happen-git-bisect-to-the-rescue-4368105f8149
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cac58740569d1a4ca97d4.jpg
tags:
- name: debugging
  slug: debugging
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment ce bug est-il arrivé ? Git bisect à la rescousse !
seo_desc: 'By Alex Nadalin

  git bisect is a very handy command that lets you isolate which commit introduced
  a bug. You tell it which version of your repository was bug-free, and it runs a
  binary search between your current commit and the one that seems to have ...'
---

Par Alex Nadalin

`git bisect` est une commande très pratique qui vous permet d'[isoler quel commit a introduit un bug](https://git-scm.com/docs/git-bisect). Vous lui indiquez quelle version de votre dépôt était exempt de bug, et il exécute une [recherche binaire](https://en.wikipedia.org/wiki/Binary_search_algorithm) entre votre commit actuel et celui qui semble contenir le bug, vous demandant de confirmer si le bug semble présent à chaque étape de la recherche.

Curieux ? Voyons cela en action !

Créons d'abord un dépôt avec une série de commits "fictifs" :

```
/tmp 🖕 mkdir test-repo
```

```
/tmp 🖕 cd test-repo
```

```
/tmp/test-repo 🖕 git initInitialized empty Git repository in /tmp/test-repo/.git/
```

```
/tmp/test-repo (master ✓) 🖕 touch test.txt
```

```
/tmp/test-repo (master ✓) 🖕 for i in $(seq 1 100); do echo $i > test.txt && git add test.txt && git commit -m "Now: $i"; done[master (root-commit) 28ea863] Now: 1 1 file changed, 1 insertion(+) create mode 100644 test.txt[master fc57245] Now: 2 1 file changed, 1 insertion(+), 1 deletion(-)[master 81e693c] Now: 3 1 file changed, 1 insertion(+), 1 deletion(-).........[master b68f338] Now: 100 1 file changed, 1 insertion(+), 1 deletion(-)
```

Disons que le commit qui a introduit notre bug est celui où le nombre dans le fichier `test.txt` est supérieur à 9 (donc le commit qui commence à 10 est le coupable) — comment le trouverions-nous en réalité ?

Entrez `git bisect` — disons à git que :

* nous voulons commencer la _bisecting_
* notre commit actuel, le plus récent, semble être cassé
* un commit dans l'historique ne semble pas avoir le bug

...et laissons git faire le travail pour nous :

```
/tmp/test-repo (master ✓) 🖕 git bisect start
```

```
/tmp/test-repo (master ✓) 🖕 git bisect bad # Notre dernier commit semble avoir un bug
```

```
/tmp/test-repo (master ✓) 🖕 git checkout 28ea863 # revenons à un commit dont nous sommes sûrs qu'il n'a pas le bugNote: checking out '28ea863'.
```

```
You are in 'detached HEAD' state. You can look around, make experimentalchanges and commit them, and you can discard any commits you make in thisstate without impacting any branches by performing another checkout.
```

```
If you want to create a new branch to retain commits you create, you maydo so (now or later) by using -b with the checkout command again. Example:
```

```
git checkout -b <new-branch-name>
```

```
HEAD is now at 28ea863... Now: 1
```

```
/tmp/test-repo (28ea863 ✓) 🖕 git bisect goodBisecting: 49 revisions left to test after this (roughly 6 steps)[bcba603c516783f6ad42b9410f6889e10aea0717] Now: 50
```

Maintenant, git va vérifier exactement au milieu de ces deux commits. Il vous demande de tester vos changements et de lui indiquer si ce commit est bon ou mauvais. Continuons :

```
/tmp/test-repo (bcba603 ✓) 🖕 cat test.txt50
```

```
/tmp/test-repo (bcba603 ✓) 🖕 git bisect badBisecting: 24 revisions left to test after this (roughly 5 steps)[b276476e9f1d989f011db4fefc5b92df1685b313] Now: 25
```

```
/tmp/test-repo (b276476 ✓) 🖕 cat test.txt25
```

```
/tmp/test-repo (b276476 ✓) 🖕 git bisect badBisecting: 11 revisions left to test after this (roughly 4 steps)[ba653f4df25a0192d83c813e14ca5851653ab30f] Now: 13
```

```
/tmp/test-repo (ba653f4 ✓) 🖕 cat test.txt  13
```

```
/tmp/test-repo (ba653f4 ✓) 🖕 git bisect badBisecting: 5 revisions left to test after this (roughly 3 steps)[a77f93ed29fe3bfaac69c686ce140a4284acee68] Now: 7
```

```
/tmp/test-repo (a77f93e ✓) 🖕 cat test.txt  7
```

```
/tmp/test-repo (a77f93e ✓) 🖕 git bisect goodBisecting: 2 revisions left to test after this (roughly 2 steps)[affade823e7f0cb72a1a97052f700c31dc90cfee] Now: 10
```

```
/tmp/test-repo (affade8 ✓) 🖕 cat test.txt   10
```

```
/tmp/test-repo (affade8 ✓) 🖕 git bisect badBisecting: 0 revisions left to test after this (roughly 1 step)[11e5f969458ad51f4009e2e3ac81f38d1ede6d07] Now: 9
```

```
/tmp/test-repo (11e5f96 ✓) 🖕 cat test.txt  9
```

```
/tmp/test-repo (11e5f96 ✓) 🖕 git bisect goodaffade823e7f0cb72a1a97052f700c31dc90cfee is the first bad commitcommit affade823e7f0cb72a1a97052f700c31dc90cfeeAuthor: odino <some.one@gmail.com>Date:   Sun Jun 24 23:29:02 2018 +0400
```

```
Now: 10
```

```
:100644 100644 ec635144f60048986bc560c5576355344005e6e7 f599e28b8ab0d8c9c57a486c89c4a5132dcbd3b2 M    test.txt
```

Incroyable — `git bisect` a trouvé le commit exact où notre bug a été introduit. Rien de plus, rien de moins : juste un truc incroyable qui peut vous faire économiser des heures de débogage !

_Publié à l'origine sur [odino.org](https://odino.org/how-did-that-bug-happen-git-bisect-to-the-rescue/) (24 juin 2018)._
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) — les rants sont les bienvenus !_ 😊