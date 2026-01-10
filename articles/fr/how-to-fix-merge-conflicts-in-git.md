---
title: Comment corriger les conflits de fusion dans Git
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-28T20:25:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-merge-conflicts-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/fixConflicts.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment corriger les conflits de fusion dans Git
seo_desc: 'If you’ve ever worked on a team that''s working on a large codebase, you’ve
  likely experienced merge conflicts while creating a pull request or merging two
  branches.

  Even if you’ve never worked with a team or on a large codebase, it is still possible
  ...'
---

Si vous avez déjà travaillé en équipe sur une base de code importante, vous avez probablement déjà rencontré des conflits de fusion (merge conflicts) lors de la création d'une pull request ou de la fusion de deux branches.

Même si vous n'avez jamais travaillé en équipe ou sur une base de code importante, il est toujours possible d'avoir des conflits de fusion tant que vous avez plus d'une branche. Dans le processus de fusion d'une branche avec une autre, un conflit de fusion peut survenir.

Dans cet article, vous en apprendrez plus sur les conflits de fusion dans Git et sur les types de conflits que vous pourriez rencontrer. Plus important encore, vous apprendrez comment résoudre les conflits de fusion sur GitHub et avec l'éditeur de fusion à 3 voies (3-way merge editor) de VS Code.

## Ce que nous allons aborder
- [Qu'est-ce qu'un conflit de fusion dans Git ?](#heading-quest-ce-quun-conflit-de-fusion-dans-git)
- [Que faire lorsque des conflits de fusion surviennent](#heading-que-faire-lorsque-des-conflits-de-fusion-surviennent)
- [Quels sont les types de conflits de fusion dans Git ?](#heading-quels-sont-les-types-de-conflits-de-fusion-dans-git)
  - [Conflit de fusion de contenu](#heading-conflit-de-fusion-de-contenu)
  - [Conflit de fusion structurel](#heading-conflit-de-fusion-structurel)
- [Comment résoudre les conflits de fusion dans Git](#heading-comment-resoudre-les-conflits-de-fusion-dans-git)
   - [Comment résoudre les conflits de fusion dans Git avec l'interface GitHub](#heading-comment-resoudre-les-conflits-de-fusion-dans-git-avec-linterface-github)
   - [Comment résoudre les conflits de fusion dans Git avec VS Code](#heading-comment-resoudre-les-conflits-de-fusion-dans-git-avec-vs-code)
   - [Comment résoudre les conflits de fusion dans Git avec l'éditeur de fusion à 3 voies de VS Code](#heading-comment-resoudre-les-conflits-de-fusion-dans-git-avec-lediteur-de-fusion-a-3-voies-de-vs-code)
- [Conclusion](#heading-conclusion)


## Qu'est-ce qu'un conflit de fusion dans Git ?
Dans Git, un conflit de fusion survient lorsque vous ou l'un des membres de votre équipe effectuez des modifications contradictoires sur le même fichier à partir de deux branches différentes.

Les conflits de fusion peuvent également survenir même si vous ne travaillez pas avec des membres d'une équipe. Si vous avez apporté des modifications au même fichier à partir de différentes branches et que ces modifications sont contradictoires, il y aura un conflit de fusion.

Dans de nombreux cas, Git gère automatiquement la fusion pour vous. Mais s'il y a des modifications contradictoires sur le même fichier, vous devez les résoudre manuellement.

Un scénario typique de conflit de fusion pourrait ressembler à ceci :
- vous travaillez dans la branche `main` et vous modifiez la ligne 1 d'un fichier mytext.txt, par exemple `Hi world`.
- vous passez sur la branche `new-feature` et vous modifiez la même ligne du fichier `mytext.txt`, par exemple `Hello earth`.

Si vous tentez de fusionner la branche `new-feature` dans `main`, Git ne pourra pas décider automatiquement laquelle des deux versions accepter entre `Hi world` et `Hello earth`. Par conséquent, Git signalera une erreur de conflit de fusion et vous demandera de résoudre le conflit manuellement.


## Que faire lorsque des conflits de fusion surviennent
Ce n'est pas la fin du monde si des conflits de fusion surviennent pendant que vous travaillez. Git vous dit simplement : "Je veux faire cette fusion pour vous, mais il y a quelque chose que vous devez faire pour moi d'abord".

Lorsque ces conflits surviennent et que vous tentez de les résoudre, Git annotera automatiquement les lignes en conflit pour vous avec le symbole inférieur à (`<`), le signe égal (`=`) et le symbole supérieur à (`>`) comme ceci :

```
<<<<<<<
=======
>>>>>>>
```

![Screenshot-2023-03-28-at-16.36.58](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-16.36.58.png)

Tout ce qui se trouve entre les signes inférieur à (`<`) et égal (`=`) correspond à la modification dans la branche actuelle (celle dans laquelle vous fusionnez). Tout ce qui se trouve entre les signes égal (`=`) et supérieur à (`>`) est la modification entrante de la branche que vous souhaitez fusionner.

C'est à vous de supprimer ces annotations et de décider de l'aspect final des lignes en conflit – vous pouvez accepter l'une des modifications ou les deux.

Ainsi, au lieu de voir les conflits de fusion comme un obstacle, vous pouvez simplement les considérer comme des annotations à supprimer et des éléments à accepter ou à rejeter.

Continuez à lire cet article pour voir comment résoudre un conflit de fusion. Mais avant cela, examinons les types de conflits de fusion.


## Quels sont les types de conflits de fusion dans Git ?
Il existe deux types de conflits de fusion : le *conflit de contenu* et le *conflit structurel*.

### Conflit de fusion de contenu
Le conflit de contenu survient lorsque les modifications que vous apportez dans deux branches différentes affectent les mêmes lignes de code dans un fichier. Cela entraîne des modifications contradictoires qui ne peuvent pas être fusionnées automatiquement par Git.

Par exemple, vous modifiez la ligne 2 avec `display: flex` dans une branche et vous effectuez une autre modification `text-align: center` sur la même ligne 2 dans le même fichier dans une autre branche.

Lorsque ce *conflit de contenu* se produit, Git arrête le processus de fusion et vous invite à ajuster le code avant de continuer.

### Conflit de fusion structurel
Le conflit structurel survient lorsque les modifications que vous apportez dans deux branches différentes affectent le même fichier mais ne sont pas en conflit ligne par ligne. Au lieu de cela, les modifications affectent la structure ou l'organisation du fichier, comme le renommage d'une variable, d'une fonction, ou le déplacement d'un bloc de code.

Si ce conflit structurel se produit, Git ne sera pas en mesure de déterminer laquelle des modifications accepter et vous demandera de décider quelles modifications vous souhaitez conserver.


## Comment résoudre les conflits de fusion dans Git
Pour vous montrer comment résoudre les conflits de fusion, j'ai initialisé Git dans un répertoire de travail (dossier) en exécutant `git init`. J'ai également créé une nouvelle branche nommée `new-feature` en exécutant `git checkout -b new-feature`.

L'exécution de `git branch` montre que j'ai les branches `main` et `new-feature` :

![Screenshot-2023-03-28-at-11.51.38](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-11.51.38.png)

J'ai également poussé les deux branches sur GitHub, afin de pouvoir vous montrer comment résoudre les conflits de fusion sur GitHub :

![Screenshot-2023-03-28-at-11.52.10](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-11.52.10.png)

J'ai ajouté du code aux fichiers HTML et JavaScript du répertoire. J'ai déclenché des conflits dans les deux fichiers et effectué des Commits :

![Screenshot-2023-03-28-at-11.53.19](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-11.53.19.png)


## Comment résoudre les conflits de fusion dans Git avec l'interface GitHub
Puisque j'ai poussé la branche `new-feature` sur GitHub, GitHub me demandera de créer une pull request pour que la branche `new-feature` soit fusionnée dans `main` :

![Screenshot-2023-03-28-at-12.00.23](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-12.00.23.png)

Dans ce cas, dès que vous cliquez sur “Compare and Pull”, vous verrez qu'il ne peut pas y avoir de fusion automatique car il y a un conflit :

![Screenshot-2023-03-28-at-13.10.15](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.10.15.png)

Cela signifie qu'il y a un conflit que vous devez résoudre. Créez la pull request et faites défiler vers le bas pour voir où vous pouvez résoudre le conflit, puis cliquez sur le bouton “Resolve conflicts” :

![Screenshot-2023-03-28-at-13.12.39](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.12.39.png) 

Lorsque vous cliquez sur “Resolve conflicts”, un éditeur s'affiche et, sur la droite, vous verrez la liste des fichiers présentant des conflits :

![Screenshot-2023-03-28-at-13.15.12](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.15.12.png)

Dans l'éditeur, vous verrez les lignes où les conflits se sont produits :

![Screenshot-2023-03-28-at-13.16.24](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.16.24.png)

Vous pouvez voir que les modifications de la branche entrante se situent entre les signes inférieur à (`<`) et égal (`=`), tandis que les modifications de la branche dans laquelle vous voulez fusionner sont entourées par les signes supérieur à (`>`) et égal (`=`).

Choisissez la ligne que vous souhaitez, supprimez les annotations et cliquez sur “Mark as resolved” dans le coin supérieur droit :

![Screenshot-2023-03-28-at-13.20.10](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.20.10.png)

Répétez le même processus pour tout autre fichier présentant également des conflits.

Si vous le souhaitez, vous pouvez conserver les deux lignes. Assurez-vous simplement de supprimer les annotations.

Après cela, cliquez sur “Commit merge” dans le coin supérieur droit :

![Screenshot-2023-03-28-at-13.23.46](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.23.46.png)

Désormais, il ne devrait plus y avoir de conflit de fusion :

![Screenshot-2023-03-28-at-13.24.30](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-13.24.30.png) 


## Comment résoudre les conflits de fusion dans Git avec VS Code
De nombreux éditeurs de code populaires disposent d'interfaces pour résoudre un conflit de fusion lorsque vous tentez de fusionner localement.

Lorsque vous passez sur la branche dans laquelle vous souhaitez fusionner et exécutez `git merge branch-to-merge`, vous serez invité à résoudre certains conflits (le cas échéant). S'il y a des conflits à résoudre, l'interface ressemble à ceci dans VS Code :

![Screenshot-2023-03-28-at-12.21.03](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-12.21.03.png)

À ce stade, si vous n'êtes pas prêt à résoudre les conflits, vous pouvez abandonner la fusion en exécutant `git merge --abort`.

Mais si vous souhaitez résoudre les conflits, vous pouvez soit accepter les modifications entrantes (incoming changes), accepter la modification actuelle (current change), ou accepter les deux.

Si vous sélectionnez l'une des trois options, le ou les conflits de fusion seront résolus. Après cela, ajoutez le fichier et validez-le par un Commit de la manière habituelle :

```
git add .
git commit -m "<message de commit>"
```


## Comment résoudre les conflits de fusion dans Git avec l'éditeur de fusion à 3 voies de VS Code
Vous pouvez également effectuer un rebase d'un conflit avec l'éditeur de fusion à 3 voies de VS Code.

Après avoir exécuté `git merge <branch-to-merge>`, cliquez sur le bouton “Resolve in Merge Editor”.

Vous verrez que vous avez maintenant 3 vues. Vous verrez les modifications de la branche entrante sur la gauche, les modifications de la branche dans laquelle vous voulez fusionner sur la droite (la branche actuelle), et l'aperçu en dessous des deux :

![Screenshot-2023-03-28-at-14.32.49-copy](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-14.32.49-copy.png)

Commencez maintenant à résoudre les conflits en sélectionnant l'une des options disponibles :
- Accept Incoming (Accepter l'entrant)
- Accept Combination (Incoming First) (Accepter la combinaison, l'entrant d'abord)
- Accept Current (Accepter l'actuel)
- Accept Combination (Current First) (Accepter la combinaison, l'actuel d'abord)

"Incoming" est la modification de la branche que vous voulez fusionner dans une branche cible, et "current" est la modification déjà présente dans la branche dans laquelle vous fusionnez.

Basculez sur chaque fichier, cliquez sur le bouton “Resolve in Merge Editor”, et sélectionnez l'une des options proposées.

![Screenshot-2023-03-28-at-14.31.34](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-14.31.34.png)

Vous pouvez également résoudre les conflits en saisissant le code correct dans chacun des fichiers.

Lorsque vous êtes satisfait, cliquez sur “Complete Merge” dans chaque éditeur de fusion :

![Screenshot-2023-03-28-at-14.32.49](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-14.32.49.png)

Vous devez ajouter les fichiers à nouveau et effectuer un Commit :

```
git add .
git commit -m "<message-de-commit>"
```

Et voilà ! Si vous voulez que l'éditeur de fusion à 3 voies s'ouvre automatiquement lorsque vous devez fusionner des conflits, cliquez sur “Settings” et recherchez “merge editor”, puis cochez “open the merge editor for files that are currently under conflicts”.

![Screenshot-2023-03-28-at-15.01.54](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-15.01.54.png)


## Conclusion
Comme vous l'avez vu, avoir un conflit Git n'est pas aussi effrayant qu'il n'y paraît, et le résoudre n'est pas une tâche impossible. Vous pouvez généralement le résoudre directement sur GitHub ou dans votre éditeur de texte. L'éditeur de fusion à 3 voies de VS Code est également un moyen pratique de résoudre un conflit de fusion.

Si vous avez créé une pull request pour une base de code importante et que vous avez un conflit de fusion, une autre façon de le résoudre pourrait être de faire un rebase avec main en exécutant `git pull --rebase upstream main` (selon le cas). Après cela, une interface vous sera présentée pour résoudre les conflits et les fichiers contenant les conflits. Lorsque vous avez terminé, exécutez `git add .`, `git rebase --continue`, puis effectuez un force push vers votre branche.