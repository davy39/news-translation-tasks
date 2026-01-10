---
title: Le Guide Définitif de la Fusion dans Git
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2023-04-27T17:07:19.000Z'
originalURL: https://freecodecamp.org/news/the-definitive-guide-to-git-merge
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/The-Git-Merge-Handbook-Book-Cover.png
tags:
- name: Git
  slug: git
- name: handbook
  slug: handbook
- name: version control
  slug: version-control
seo_title: Le Guide Définitif de la Fusion dans Git
seo_desc: 'By reading this post, you are going to really understand git merge, one
  of the most common operations you''ll perform in your Git repositories.

  Notes before we start


  I also created two videos covering the contents of this post. If you wish to watch
  a...'
---

En lisant cet article, vous allez *vraiment* comprendre `git merge`, l'une des opérations les plus courantes que vous effectuerez dans vos dépôts Git.

## Notes avant de commencer

1. J'ai également créé deux vidéos couvrant le contenu de cet article. Si vous souhaitez les regarder en parallèle de votre lecture, vous pouvez les trouver ici ([Partie 1](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief), [Partie 2](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief)).
2. Je travaille sur un livre sur Git ! Êtes-vous intéressé à lire les versions initiales et à fournir des commentaires ? Envoyez-moi un email : gitting.things@gmail.com

OK, êtes-vous prêt ?



# Table des Matières

* [Qu'est-ce qu'une Fusion dans Git ?](#heading-questce-quune-fusion-dans-git)
* [Passons à la Pratique 👌🏻](#heading-passons-a-la-pratique)
* [Un Cas Plus Avancé](#heading-un-cas-plus-avance)
* [Récapitulatif rapide sur une fusion à trois voies](#heading-recapitulatif-rapide-sur-une-fusion-a-trois-voies)
* [Continuons 👣](#heading-continuons)
* [Cas Plus Avancés de Fusion Git](#heading-cas-plus-avances-de-fusion-git)
* [Comment Fonctionne l'Algorithme de Fusion à 3 Voies de Git](#heading-comment-fonctionne-lalgorithme-de-fusion-a-3-voies-de-git)
* [Comment Résoudre les Conflits de Fusion](#heading-comment-resoudre-les-conflits-de-fusion)
* [Comment Utiliser VS Code pour Résoudre les Conflits](#heading-comment-utiliser-vs-code-pour-resoudre-les-conflits)
* [Un Outil Puissant de Plus 🧫](#heading-un-outil-puissant-de-plus)
* [Récapitulatif](#heading-recapitulatif)

# Qu'est-ce qu'une Fusion dans Git ?

La fusion est le processus de combinaison des changements récents de plusieurs branches en un seul nouveau commit qui sera sur toutes ces branches.

En quelque sorte, la fusion est le complément du branchement dans le contrôle de version : une branche vous permet de travailler simultanément avec d'autres sur un ensemble particulier de fichiers, tandis qu'une fusion vous permet de combiner plus tard le travail séparé sur des branches qui ont divergé d'un commit ancêtre commun.

OK, décomposons cela.

Rappelez-vous que dans Git, [une branche est simplement un nom pointant vers un seul commit](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/). Lorsque nous pensons aux commits comme étant "sur" une branche spécifique, ils sont en fait accessibles via la chaîne parentale à partir du commit vers lequel la branche pointe. 

C'est-à-dire, si vous considérez ce graphe de commits :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-140.png)
_Graphe de commits avec deux pointeurs (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Vous voyez la branche `feature_1`, qui pointe vers un commit avec la valeur SHA-1 de `ba0d2`. Bien sûr, comme dans d'autres articles, j'écris seulement les cinq premiers chiffres de la valeur SHA-1. 

Remarquez que le commit `54a9d` est également sur cette branche, car il est le commit parent de `ba0d2`. Donc si vous partez du pointeur de `feature_1`, vous arrivez à `ba0d2`, qui pointe ensuite vers `54a9d`.

Lorsque vous fusionnez avec Git, vous fusionnez des **commits**. Presque toujours, nous fusionnons deux commits en les référençant avec les noms de branches qui pointent vers eux. Ainsi, nous disons que nous "fusionnons des branches" – bien que sous le capot, nous fusionnons en réalité des commits.

# Passons à la Pratique 👌🏻

OK, alors disons que j'ai ce dépôt simple ici, avec une branche appelée `main`, et quelques commits avec les messages de commit "Commit 1", "Commit 2" et "Commit 3" :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-141.png)
_Un dépôt simple avec trois commits (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Ensuite, créez une branche de fonctionnalité en tapant `git branch new_feature` :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-142.png)
_Création d'une nouvelle branche avec `git branch` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Et basculez `HEAD` pour pointer vers cette nouvelle branche, en utilisant `git checkout new_feature`. Vous pouvez regarder le résultat en utilisant `git log` :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-143.png)
_La sortie de `git log` après avoir utilisé `git checkout new_feature` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Pour rappel, vous auriez également pu écrire `git checkout -b new_feature`, ce qui créerait une nouvelle branche et changerait `HEAD` pour pointer vers cette nouvelle branche. 

Si vous avez besoin d'un rappel sur les branches et leur implémentation sous le capot, veuillez consulter [un article précédent sur le sujet](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/). Oui, checkout. Jeu de mots intentionnel 😇

Maintenant, sur la branche `new_feature`, implémentez une nouvelle fonctionnalité. Dans cet exemple, je vais modifier un fichier existant qui ressemble à ceci avant la modification :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-144.png)
_`code.py` avant de le modifier (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Et je vais maintenant le modifier pour inclure une nouvelle fonction :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-145.png)
_Implémentation de `new_feature` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Et heureusement, ce n'est pas un tutoriel de programmation, donc cette fonction est légitime 😇  
Ensuite, indexez et commitez ce changement :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-146.png)
_Commit des changements vers "Commit 4" (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

En regardant l'historique, vous avez la branche `new_feature`, pointant maintenant vers "Commit 4", qui pointe vers son parent, "Commit 3". La branche `main` pointe également vers "Commit 3".

Il est temps de fusionner la nouvelle fonctionnalité ! C'est-à-dire, fusionner ces deux branches, `main` et `new_feature`. Ou, dans le jargon de Git, fusionner `new_feature` *dans* `main`. Cela signifie fusionner "Commit 4" et "Commit 3". Cela est assez trivial, après tout, "Commit 3" est un ancêtre de "Commit 4".

Passez à la branche principale (avec `git checkout main`), et effectuez la fusion en utilisant `git merge new_feature` :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-197.png)
_Fusion de `new_feature` dans `main` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Puisque `new_feature` n'a jamais vraiment *divergé* de `main`, Git a pu simplement effectuer une fusion par avance rapide. Alors, que s'est-il passé ici ? Considérez l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image--7-.png)
_Le résultat d'une fusion par avance rapide (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Même si vous avez utilisé `git merge`, il n'y a pas eu de fusion réelle ici. En fait, Git a fait quelque chose de très simple – il a réinitialisé la branche `main` pour pointer vers le même commit que la branche `new_feature`.

Au cas où vous ne voudriez pas que cela se produise, mais plutôt que vous voulez que Git effectue vraiment une fusion, vous pourriez soit changer la configuration de Git, soit exécuter la commande `merge` avec le flag `--no-ff`.

Tout d'abord, annulez le dernier commit :

```git
git reset --hard HEAD~1
```

Si cette façon d'utiliser reset n'est pas claire pour vous, n'hésitez pas à consulter [un article où j'ai couvert `git reset` en profondeur](https://medium.com/@Omer_Rosenbaum/git-undo-how-to-rewrite-git-history-with-confidence-d4452e2969c2). Ce n'est pas crucial pour cette introduction de `merge`, cependant. Pour l'instant, il est important de comprendre qu'il annule essentiellement l'opération de fusion.

Juste pour clarifier, maintenant si vous avez vérifié `new_feature` à nouveau :

```git
git checkout new_feature
```

L'historique ressemblerait à avant la fusion :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image--8-.png)
_L'historique après avoir utilisé `git reset --hard HEAD~1` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Ensuite, effectuez la fusion avec le flag `--no-fast-forward` (`--no-ff` pour faire court) :
```git
git checkout main
git merge new_feature --no-ff
```

Maintenant, si nous regardons l'historique en utilisant `git lol` :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-200.png)
_Historique après la fusion avec le flag `--no-ff` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

(`git lol` est un alias que j'ai ajouté à Git pour voir visuellement l'historique de manière graphique. Vous pouvez le trouver [ici](https://gist.github.com/Omerr/8134a61b56ca82dd90e546e7ef04eb77)).

En considérant cet historique, vous pouvez voir que Git a créé un nouveau commit, un commit de fusion.

Si vous considérez ce commit un peu plus près :
```
git log -n1
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-201.png)
_Le commit de fusion a deux parents (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Vous verrez que ce commit a en réalité deux parents – "Commit 4", qui était le commit vers lequel `new_feature` pointait lorsque vous avez exécuté `git merge`, et "Commit 3", qui était le commit vers lequel `main` pointait. Donc un commit de fusion a deux parents : les deux commits qu'il a fusionnés.

Le commit de fusion nous montre bien le concept de fusion. Git prend deux commits, généralement référencés par deux branches différentes, et les fusionne ensemble. 

Après la fusion, comme vous avez commencé le processus à partir de `main`, vous êtes toujours sur `main`, et l'historique de `new_feature` a été fusionné dans cette branche. Puisque vous avez commencé avec `main`, alors "Commit 3", vers lequel `main` pointait, est le premier parent du commit de fusion, tandis que "Commit 4", que vous avez fusionné *dans* `main`, est le second parent du commit de fusion.

Remarquez que vous avez commencé sur `main` lorsqu'il pointait vers "Commit 3", et Git a fait un long chemin pour vous. Il a changé l'arborescence de travail, l'index, et aussi `HEAD` et créé un nouvel objet de commit. Au moins lorsque vous utilisez `git merge` sans le flag `--no-commit` et lorsque ce n'est pas une fusion par avance rapide, Git fait tout cela.

C'était un cas super simple, où les branches que vous avez fusionnées n'ont pas divergé du tout.

Au fait, vous pouvez utiliser `git merge` pour fusionner plus de deux commits – en fait, n'importe quel nombre de commits. Cela est rarement fait et je ne vois pas de bonne raison d'élaborer sur ce sujet ici.

Une autre façon de penser à `git merge` est de joindre deux ou plusieurs *historiques de développement* ensemble. C'est-à-dire, lorsque vous fusionnez, vous incorporez les changements des commits nommés, depuis le moment où leurs historiques ont divergé *de* la branche actuelle, *dans* la branche actuelle. J'ai utilisé le terme `branche` ici, mais je le souligne à nouveau – nous fusionnons en réalité des commits.

# Un Cas Plus Avancé 💪🏻

Il est temps de considérer un cas plus avancé, qui est probablement le cas le plus courant où nous utilisons explicitement `git merge` – où vous devez fusionner des branches qui *ont* divergé l'une de l'autre.

Supposons que nous avons maintenant deux personnes travaillant sur ce dépôt, John et Paul.

John a créé une branche :
```
git checkout -b john_branch
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-348.png)
_Une nouvelle branche, `john_branch` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Et John a écrit une nouvelle chanson dans un nouveau fichier, `lucy_in_the_sky_with_diamonds.md`. Eh bien, je crois que John Lennon n'a pas vraiment écrit en format Markdown, ou utilisé Git d'ailleurs, mais faisons semblant qu'il l'a fait pour cette explication.

```
git add lucy_in_the_sky_with_diamonds.md
git commit -m "Commit 5"
```

Pendant que John travaillait sur cette chanson, Paul écrivait aussi, sur une autre branche. Paul était parti de `main` :
```
git checkout main
```

Et a créé sa propre branche :
```
git checkout -b paul_branch
```

Et Paul a écrit sa chanson dans un fichier :
```
nano penny_lane.md
```

Et l'a committée :
```
git add penny_lane.md
git commit -m "Commit 6"
```

Donc maintenant notre historique ressemble à ceci – où nous avons deux branches différentes, bifurquant de `main`, avec des historiques différents.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-203.png)
_La sortie de `git lol` montre l'historique après que John et Paul ont committé (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

John est satisfait de sa branche (c'est-à-dire, de sa chanson), donc il décide de la fusionner dans la branche `main` :
```
git checkout main
git merge john_branch
```

En fait, il s'agit d'une fusion par avance rapide, comme nous l'avons appris précédemment. Vous pouvez valider cela en regardant l'historique (en utilisant `git lol`, par exemple) :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-349.png)
_Fusion de `john_branch` dans `main` résulte en une fusion par avance rapide (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

À ce stade, Paul veut également fusionner sa branche dans `main`, mais maintenant une fusion par avance rapide n'est plus pertinente – il y a deux *historiques* différents ici : l'historique de `main` et celui de `paul_branch`. Ce n'est pas que `paul_branch` ajoute simplement des commits au-dessus de la branche `main` ou vice versa.

Maintenant, les choses deviennent intéressantes. 😎😎

Tout d'abord, laissez Git faire le travail difficile pour vous. Après cela, nous comprendrons ce qui se passe réellement sous le capot.

```
git merge paul_branch
```

Considérez l'historique maintenant :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-206.png)
_Lorsque vous fusionnez `paul_branch`, vous obtenez un nouveau commit de fusion (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Ce que vous avez est un nouveau commit, avec deux parents – "Commit 5" et "Commit 6".
Dans le répertoire de travail, vous pouvez voir que les chansons de John ainsi que celles de Paul sont là :
`ls`

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-242.png)
_Le répertoire de travail après la fusion (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Bien, Git a vraiment fusionné les changements pour nous. Mais comment cela se passe-t-il ?

Annulez ce dernier commit :
```
git reset --hard HEAD~
```

## Comment effectuer une fusion à trois voies dans Git

Il est temps de comprendre ce qui se passe réellement sous le capot. 😎

Ce que Git a fait ici, c'est qu'il a appelé une `fusion à 3 voies`. En décrivant le processus d'une fusion à 3 voies, j'utiliserai le terme "branche" pour simplifier, mais vous devez vous souvenir que vous pourriez également fusionner deux (ou plus) commits qui ne sont pas référencés par une branche.

Le processus de fusion à 3 voies comprend ces étapes :

Tout d'abord, Git localise l'ancêtre commun des deux branches. C'est-à-dire, le commit commun à partir duquel les branches à fusionner ont divergé le plus récemment. Techniquement, il s'agit en fait du premier commit qui est accessible depuis les deux branches. Ce commit est alors appelé la **base de fusion**.

Deuxièmement, Git calcule deux diffs – un diff de la base de fusion à la première branche, et un autre diff de la base de fusion à la deuxième branche. Git génère des patches basés sur ces diffs.

Troisièmement, Git applique les deux patches à la base de fusion en utilisant un algorithme de fusion à 3 voies. Le résultat est l'état du nouveau commit de fusion.


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-357.png)
_Les trois étapes de l'algorithme de fusion à 3 voies : (1) localiser l'ancêtre commun ; (2) calculer les diffs de la base de fusion à la première branche, et de la base de fusion à la deuxième branche ; (3) appliquer les deux patches ensemble (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Donc, revenons à notre exemple.

Dans la première étape, Git regarde depuis les deux branches – `main` et `paul_branch` – et parcourt l'historique pour trouver le premier commit qui est accessible depuis les deux. Dans ce cas, ce serait... quel commit ?

Correct, "Commit 4".

Si vous n'êtes pas sûr, vous pouvez toujours demander directement à Git :
```
git merge-base main paul_branch
```

Au fait, il s'agit du cas le plus courant et le plus simple, où nous avons un seul choix évident pour la base de fusion. Dans des cas plus compliqués, il peut y avoir plusieurs possibilités pour une base de fusion, mais c'est un sujet pour un autre article.

Dans la deuxième étape, Git calcule les diffs. Il calcule donc d'abord le diff entre "Commit 4" et "Commit 5" :
```
git diff 4f90a62 4683aef
```

(Les valeurs SHA-1 seront différentes sur votre machine)

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-247.png)
_Le diff entre "Commit 4" et "Commit 5" (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Si vous ne vous sentez pas à l'aise avec la sortie de `git diff`, veuillez lire [l'article précédent](https://www.freecodecamp.org/news/git-diff-and-patch/) où je l'ai décrit en détail.

Vous pouvez stocker ce diff dans un fichier :
```
git diff 4f90a62 4683aef > john_branch_diff.patch
```

Ensuite, Git calcule le diff entre "Commit 4" et "Commit 6" :
```
git diff 4f90a62 c5e4951
```



![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-249.png)
_Le diff entre "Commit 4" et "Commit 6" (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Écrivez celui-ci également dans un fichier :
```
git diff 4f90a62 c5e4951 > paul_branch_diff.patch
```

Maintenant, Git applique ces patches sur la base de fusion. 

Tout d'abord, essayez cela directement – appliquez simplement les patches (je vais vous guider à travers cela dans un moment). Ce n'est *pas* ce que Git fait réellement sous le capot, mais cela vous aidera à mieux comprendre pourquoi Git doit faire quelque chose de différent.

Tout d'abord, passez à la base de fusion, c'est-à-dire "Commit 4" :
```
git checkout 4f90a62
```

Et appliquez d'abord le patch de John :
```
git apply --index john_branch_diff.patch
```

Remarquez que pour l'instant, il n'y a pas de commit de fusion. `git apply` met à jour le répertoire de travail ainsi que l'index, car nous avons utilisé l'option `--index`.

Vous pouvez observer le statut en utilisant `git status` :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-250.png)
_Application du patch de John sur "Commit 4" (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Ainsi, la nouvelle chanson de John est incorporée dans l'index. Appliquez l'autre patch :

`git apply --index paul_branch_diff.patch`

En conséquence, l'index contient les changements des deux branches.

Il est maintenant temps de commiter votre fusion. Puisque la commande porcelaine `git commit` génère toujours un commit avec un *seul* parent, vous auriez besoin de la commande de plomberie sous-jacente – `git commit-tree`. 

Si vous avez besoin d'un rappel sur les commandes porcelaine vs plomberie, consultez [l'article où j'ai expliqué ces termes, et créé un dépôt entier à partir de zéro](https://medium.com/swimm/getting-hardcore-creating-a-repo-from-scratch-cc747edbb11c).

Rappelez-vous que [chaque objet commit Git pointe vers un seul arbre](https://medium.com/swimm/a-visualized-intro-to-git-internals-objects-and-branches-68df85864037). Vous devez donc enregistrer le contenu de l'index dans un arbre :

```
git write-tree
```

Maintenant, vous obtenez la valeur SHA-1 de l'arbre créé, et vous pouvez créer un objet commit en utilisant `git commit-tree` :

```
git commit-tree <TREE_SHA> -p <COMMIT_4> -p <COMMIT_5> -m "Commit de fusion !"
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-251.png)
_Création d'un commit de fusion (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Super, vous avez créé un objet commit 💪🏻

Rappelez-vous que `git merge` change également `HEAD` pour pointer vers le nouvel objet commit de fusion. Vous pouvez donc simplement faire de même :
`git reset --hard db315a`

Si vous regardez l'historique maintenant :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-252.png)
_L'historique après avoir créé un commit de fusion et réinitialisé `HEAD` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Vous pouvez voir que vous avez atteint le même résultat que la fusion effectuée par Git, à l'exception de l'horodatage et donc de la valeur SHA-1, bien sûr.

Ainsi, vous avez fusionné à la fois le **contenu** des deux commits – c'est-à-dire, l'état des fichiers, et aussi l'**historique** de ces commits – en créant un commit de fusion qui pointe vers les deux historiques.

Dans ce cas simple, vous auriez pu appliquer les patches en utilisant `git apply`, et tout aurait fonctionné assez bien.

## Récapitulatif rapide sur une fusion à trois voies

Donc, pour récapituler rapidement, lors d'une fusion à trois voies, Git :
* Tout d'abord, localise la base de fusion – l'ancêtre commun des deux branches. C'est-à-dire, le premier commit qui est accessible depuis les deux branches. 
* Deuxièmement, Git calcule deux diffs – un diff de la base de fusion à la *première* branche, et un autre diff de la base de fusion à la *deuxième* branche. 
* Troisièmement et enfin, Git applique les deux patches à la base de fusion en utilisant un algorithme de fusion à 3 voies. Le résultat est l'état du nouveau commit de fusion.

Vous pouvez également comprendre pourquoi on l'appelle une "fusion à 3 voies" : Git fusionne trois états différents – celui de la première branche, celui de la deuxième branche, et leur ancêtre commun. Dans notre exemple précédent, `main`, `paul_branch`, et "Commit 4".

Cela diffère, par exemple, des exemples de fusion par avance rapide que nous avons vus précédemment. Les exemples de fusion par avance rapide sont en fait un cas de fusion à **deux** voies, car Git ne compare que deux états – par exemple, où `main` pointait, et où `john_branch` pointait.

# Continuons 👣

Néanmoins, il s'agissait d'un cas simple de fusion à trois voies. John et Paul ont créé des chansons différentes, donc chacun a touché un fichier différent. Il était assez simple d'exécuter la fusion.

Et les cas plus intéressants ?

Supposons maintenant que John et Paul co-écrivent une nouvelle chanson.

Donc, John a vérifié la branche `main` et a commencé à écrire la chanson :
```
git checkout main
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-253.png)
_La nouvelle chanson de John (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Il a indexé et commité ("Commit 7") :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-254.png)
_La nouvelle chanson de John est committée (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Maintenant, Paul crée une branche :
```
git checkout -b paul_branch_2
```


Et modifie la chanson, ajoutant un autre couplet :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-255.png)
_Paul a ajouté un nouveau couplet (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Bien sûr, dans la chanson originale, nous n'avons pas le titre "Le Couplet de Paul", mais je l'ajouterai ici pour simplifier.

Paul indexe et commite les changements :

```
git add a_day_in_the_life.md
git commit -m "Commit 8"
```


John crée également une branche à partir de `main` et ajoute quelques dernières lignes :
```git checkout main
git checkout -b john_branch_2
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-256.png)
_Paul a commité, et maintenant c'est à nouveau au tour de John (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-257.png)
_John a ajouté quelques lignes (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Et il indexe et commite ses changements aussi ("Commit 9") :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-258.png)
_John a commité ses changements (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Voici l'historique résultant :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-350.png)
_L'historique après le dernier commit de John (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Donc, Paul et John ont modifié le même fichier sur différentes branches. Git réussira-t-il à les fusionner ? 🤔

Disons maintenant que nous ne passons pas par `main`, mais que John va essayer de fusionner la nouvelle branche de Paul dans sa branche :

```
git merge paul_branch_2
```

Attendez !! 🤪🏻 N'exécutez pas cette commande ! Pourquoi laisser Git faire tout le travail difficile ? Vous essayez de comprendre le processus ici.

Donc, d'abord, Git doit trouver la base de fusion. Pouvez-vous voir quel commit ce serait ?

Correct, ce serait le dernier commit sur la branche `main`, où les deux ont divergé.

Vous pouvez vérifier cela en utilisant :
```
git merge-base john_branch_2 paul_branch_2
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-260.png)
_Trouver la base de fusion (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Super, maintenant Git devrait calculer les diffs et générer les patches. Vous pouvez observer les diffs directement :
```
git diff main paul_branch_2
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-261.png)
_La sortie de `git diff main paul_branch_2` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

L'application de ce patch réussira-t-elle ? Eh bien, aucun problème, Git a toutes les lignes de contexte en place.

Demandez à Git d'appliquer ce patch :

```
git diff main paul_branch_2 > paul_branch_2.patch
git apply --index paul_branch_2.patch
```

Et cela a fonctionné, aucun problème du tout.

Maintenant, calculez le diff entre la nouvelle branche de John et la base de fusion. Remarquez que vous n'avez pas commité les changements appliqués, donc `john_branch_2` pointe toujours vers le même commit qu'avant, "Commit 9" :
```
git diff main john_branch_2
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-262.png)
_La sortie de `git diff main john_branch_2` (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

L'application de ce diff fonctionnera-t-elle ?

Eh bien, en effet, oui. Remarquez que même si les numéros de ligne ont changé sur la version actuelle du fichier, grâce aux lignes de contexte, Git est capable de localiser où il doit ajouter ces lignes...

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-263.png)
_Git peut s'appuyer sur les lignes de contexte (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Enregistrez ce patch et appliquez-le ensuite :
```
git diff main john_branch_2 > john_branch_2.patch
git apply --index john_branch_2.patch
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-264.png)
_Appliquer le patch de Paul (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Observez le fichier résultant :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-265.png)
_Le résultat après avoir appliqué le patch de Paul (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Cool, exactement ce que nous voulions 👏🏻
Vous pouvez maintenant créer l'arbre et le commit pertinent :

```
git write-tree
```

N'oubliez pas de spécifier les deux parents :
```
git commit-tree <TREE-ID> -p paul_branch_2 -p john_branch_2 -m "Fusion des nouveaux changements"
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-266.png)
_Création d'un commit de fusion (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Voyez comment j'ai utilisé les noms des branches ici ? Après tout, ce ne sont que des pointeurs vers les commits que nous voulons.

Cool, regardez le journal à partir du nouveau commit :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-270.png)
_L'historique après la création du commit de fusion (Source : [Brief](https://www.youtube.com/watch?v=ZS4stBVdDII&ab_channel=Brief))_

Exactement ce que nous voulions.

Vous pouvez également laisser Git effectuer le travail pour vous. Vous pouvez simplement vérifier `john_branch_2`, que vous n'avez pas déplacé – donc il pointe toujours vers le même commit qu'avant la fusion. Donc tout ce que vous avez à faire est d'exécuter :
```
git merge paul_branch_2
```

Observez l'historique résultant :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-271.png)
_L'historique après avoir laissé Git effectuer la fusion (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Tout comme avant, vous avez un commit de fusion pointant vers "Commit 8" et "Commit 9" comme ses parents. "Commit 9" est le premier parent puisque vous avez fusionné dedans.

Mais cela était encore assez simple... John et Paul ont travaillé sur le même fichier, mais sur des parties très différentes. Vous auriez également pu appliquer directement les changements de Paul à la branche de John. Si vous revenez à la branche de John avant la fusion :

```
git reset --hard HEAD~
```

Et maintenant appliquez les changements de Paul :
```
git apply --index paul_branch_2.patch
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-272.png)
_Application des changements de Paul directement à la branche de John (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Vous obtiendrez le même résultat.

Mais que se passe-t-il lorsque les deux branches incluent des changements sur les mêmes fichiers, aux mêmes endroits ? 🤔

# Cas Plus Avancés de Fusion Git

Que se passerait-il si John et Paul devaient coordonner une nouvelle chanson, et travailler ensemble dessus ?

Dans ce cas, John crée la première version de cette chanson dans la branche `main` :

```
git checkout main
nano everyone.md
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-273.png)
_Le contenu de `everyone.md` avant le premier commit (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Au fait, ce texte est effectivement tiré de la version que John Lennon a enregistrée pour une démo en 1968. Mais ce n'est pas un article sur les Beatles, donc si vous êtes curieux du processus que les Beatles ont suivi en écrivant cette chanson, vous pouvez suivre les liens dans l'annexe ci-dessous.

```
git add everyone.md
git commit -m "Commit 10"
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-275.png)
_Introduction du "Commit 10" (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Maintenant, John et Paul se séparent. Paul crée un nouveau couplet au début :

```
git checkout -b paul_branch_3
nano everyone.md
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-276.png)
_Paul a ajouté un nouveau couplet au début (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

De plus, en parlant avec John, ils ont décidé de changer le mot "feet" en "foot", donc Paul ajoute également ce changement.

Et Paul ajoute et commite ses changements dans le dépôt :
```
git add everyone.md
git commit -m "Commit 11"
```

Vous pouvez observer les changements de Paul, en comparant l'état de cette branche à l'état de la branche `main` :
```
git diff main
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-277.png)
_La sortie de `git diff main` depuis la branche de Paul (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Stockez ce diff dans un fichier patch :
```
git diff main > paul_3.patch
```

Maintenant, retour à `main`...

```
git checkout main
```

John décide d'apporter une autre modification, dans sa propre nouvelle branche :

```
git checkout -b john_branch_3
```

Et il remplace la ligne "Everyone had the boot in" par la ligne "Everyone had a wet dream". De plus, John a changé le mot "feet" en "foot", suite à sa discussion avec Paul.

Observez le diff :
```
git diff main
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-278.png)
_La sortie de `git diff main` depuis la branche de John (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Stockez également cette sortie :
```
git diff main > john_3.patch
```

Maintenant, indexez et commitez :
```
git add everyone.md
git commit -m "Commit 12"
```

Voici notre historique actuel :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-351.png)
_L'historique après l'introduction du "Commit 12" (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Paul a dit à John qu'il avait ajouté un nouveau couplet, donc John aimerait fusionner les changements de Paul.

John peut-il simplement appliquer le patch de Paul ?

Considérez à nouveau le patch :
```
git diff main paul_branch_3
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-277.png)
_La sortie de `git diff main paul_branch_3` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Comme vous pouvez le voir, ce diff repose sur la ligne "Everyone had the boot in", mais cette ligne n'existe plus sur la branche de John. Par conséquent, vous pourriez vous attendre à ce que l'application du patch échoue. Allez-y, essayez :
```
git apply paul_3.patch
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-280.png)
_L'application du patch a échoué (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

En effet, vous pouvez voir qu'il a échoué.

Mais devrait-il vraiment échouer ? 🤔

Comme expliqué précédemment, `git merge` utilise un algorithme de fusion à 3 voies, et cela peut être utile ici. Quelle serait la première étape de cet algorithme ?

Eh bien, d'abord, Git trouverait la base de fusion – c'est-à-dire, l'ancêtre commun de la branche de Paul et de la branche de John. Considérez l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-351.png)
_L'historique après l'introduction du "Commit 12" (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Donc l'ancêtre commun de "Commit 11" et "Commit 12" est "Commit 10". Nous pouvons vérifier cela en exécutant la commande :

```
git merge-base john_branch_3 paul_branch_3
```

Maintenant, nous pouvons prendre les patches que nous avons générés à partir des diffs sur les deux branches, et les appliquer à `main`. Cela fonctionnerait-il ?

Tout d'abord, essayez d'appliquer le patch de John, puis celui de Paul.

Considérez le diff :
```
git diff main john_branch_3
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-278.png)
_La sortie de `git diff main john_branch_3` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Nous pouvons le stocker dans un fichier :
```
git diff main john_branch_3 > john_3.patch
```

Et je veux appliquer ce patch sur `main`, donc :
```
git checkout main
git apply john_3.patch
```

Considérons le résultat :
```
nano everyone.md
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-282.png)
_Le contenu de `everyone.md` après avoir appliqué le patch de John (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

La ligne a changé comme prévu. Bien 😎

Maintenant, Git peut-il appliquer le patch de Paul ? Pour vous rappeler, voici le patch :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-283.png)
_Le contenu du patch de Paul (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Eh bien, Git **ne peut pas** appliquer ce patch, car ce patch suppose que la ligne "Everyone had the boot in" existe. Essayer de l'appliquer est susceptible d'échouer :
```
git apply -v paul_3.branch
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-284.png)
_L'application du patch de Paul a échoué._

Ce que vous avez essayé de faire maintenant, appliquer le patch de Paul sur la branche `main` après avoir appliqué le patch de John, est la même chose que d'être sur `john_branch_3`, et de tenter d'appliquer le patch, c'est-à-dire :

```git checkout john_branch_3
git apply paul_3.patch
```

Que se passerait-il si nous essayions l'autre façon ?

Tout d'abord, nettoyez l'état :
```
git reset --hard
```

Et commencez par la branche de Paul :
```
git checkout paul_branch_3
```

Pouvons-nous appliquer le patch de John ? Pour rappel, voici l'état de `everyone.md` sur cette branche :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-285.png)
_Le contenu de `everyone.md` sur `paul_branch_3` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Et voici le patch de John :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-286.png)
_Le contenu du patch de John (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

L'application du patch de John fonctionnerait-elle ? 🤔
Essayez de répondre vous-même avant de continuer.

Vous pouvez essayer :
```
git apply john_3.patch
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-287.png)
_Git échoue à appliquer le patch de John (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Eh bien, non ! Encore une fois, si vous n'êtes pas sûr de ce qui s'est passé, vous pouvez toujours demander à `git apply` d'être un peu plus verbeux :
```
git apply john_3.patch -v
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-288.png)
_Vous pouvez obtenir plus d'informations en utilisant le flag `-v` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Git recherche "Everyone put the feet down", mais Paul a déjà changé cette ligne pour qu'elle contienne maintenant le mot "foot" au lieu de "feet". Par conséquent, l'application de ce patch échoue.

Remarquez que changer le nombre de lignes de contexte ici (c'est-à-dire, utiliser `git apply` avec le flag `-C`, comme discuté dans [un article précédent](https://www.freecodecamp.org/news/git-diff-and-patch/)) est sans importance – Git est incapable de localiser la ligne réelle que le patch essaie d'effacer.

Mais en fait, Git *peut* faire fonctionner cela, si vous ajoutez simplement un flag à `apply`, lui disant d'effectuer une fusion à 3 voies sous le capot :

```
git apply -3 john_3.patch
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-289.png)
_L'application avec le flag `-3` réussit (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Et considérons le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-290.png)
_Le contenu de `everyone.md` après la fusion (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Exactement ce que nous voulions ! Vous avez le couplet de Paul (marqué dans l'image ci-dessus), et les deux changements de John !

Alors, comment Git a-t-il pu accomplir cela ?

Eh bien, comme je l'ai mentionné, Git a vraiment effectué **une fusion à 3 voies**, et avec cet exemple, ce sera un bon moment pour plonger dans ce que cela signifie réellement.

# Comment Fonctionne l'Algorithme de Fusion à 3 Voies de Git

Revenez à l'état avant d'appliquer ce patch :
```
git reset --hard
```

Vous avez maintenant trois versions : la base de fusion, qui est "Commit 10", la branche de Paul, et la branche de John. En termes généraux, nous pouvons dire qu'il s'agit de la `base de fusion`, du `commit A` et du `commit B`. Remarquez que la `base de fusion` est par définition un ancêtre à la fois du `commit A` et du `commit B`.

Pour effectuer la fusion, Git examine le diff entre les trois versions différentes du fichier en question sur ces trois révisions. Dans votre cas, il s'agit du fichier `everyone.md`, et les révisions sont "Commit 10", la branche de Paul – c'est-à-dire "Commit 11", et la branche de John, c'est-à-dire "Commit 12".

Git prend la décision de fusion en fonction de l'état de chaque ligne dans chacune de ces versions.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-291.png)
_Les trois versions considérées pour la fusion à 3 voies (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Dans le cas où *toutes* les trois versions ne correspondent pas, c'est un conflit. Git peut résoudre beaucoup de ces conflits automatiquement, comme nous allons le voir maintenant.

Considérons des lignes spécifiques.

Les premières lignes ici n'existent que sur la branche de Paul :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-292.png)
_Lignes qui apparaissent uniquement sur la branche de Paul (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Cela signifie que l'état de la branche de John est égal à l'état de la base de fusion. Donc la fusion à 3 voies adopte la version de Paul.

En général, si l'état de la base de fusion est le même que `A`, l'algorithme adopte `B`. La raison est que puisque la base de fusion est l'ancêtre à la fois de `A` et de `B`, Git suppose que cette ligne n'a pas changé dans `A`, et qu'elle *a* changé dans `B`, qui est la version la plus récente pour cette ligne, et devrait donc être prise en compte.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-353.png)
_Si l'état de la base de fusion est le même que `A`, et que cet état est différent de `B`, l'algorithme adopte `B` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Ensuite, vous pouvez voir des lignes où les trois versions sont d'accord – elles existent sur la base de fusion, `A` et `B`, avec des données égales.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-294.png)
_Lignes où les trois versions sont d'accord (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Donc l'algorithme a un choix trivial – prendre simplement cette version.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-355.png)
_Dans le cas où les trois versions sont d'accord, l'algorithme adopte cette version unique (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Dans un exemple précédent, nous avons vu que si la base de fusion et `A` sont d'accord, et que la version de `B` est différente, l'algorithme choisit `B`. Cela fonctionne également dans l'autre sens – par exemple, ici vous avez une ligne qui existe sur la branche de John, différente de celle sur la base de fusion et la branche de Paul.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-296.png)
_Une ligne où la version de Paul correspond à la version de la base de fusion, et John a une version différente (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Par conséquent, la version de John est choisie.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-354.png)
_Si l'état de la base de fusion est le même que `B`, et que cet état est différent de `A`, l'algorithme adopte `A` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_



Considérons maintenant un autre cas, où `A` et `B` sont d'accord sur une ligne, mais la valeur sur laquelle ils sont d'accord est différente de la `base de fusion` – John et Paul ont convenu de changer la ligne "Everyone put their feet down" en "Everyone put their foot down" :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-297.png)
_Une ligne où la version de Paul correspond à la version de John ; pourtant, la base de fusion a une version différente (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Dans ce cas, l'algorithme choisit la version sur `A` et `B`.


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-352.png)
_Dans le cas où `A` et `B` sont d'accord sur une version qui est différente de la version de la base de fusion, l'algorithme choisit la version sur `A` et `B` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Remarquez que ce n'est pas un vote démocratique. Dans le cas précédent, l'algorithme a choisi la version minoritaire, car elle ressemblait à la version la plus récente de cette ligne. Dans ce cas, il *se trouve* choisir la majorité – mais seulement parce que `A` et `B` sont les révisions qui sont d'accord sur la nouvelle version.

La même chose se produirait si nous utilisions `git merge` :

```
git merge john_branch_3
```

Sans spécifier de flags, `git merge` utilisera par défaut une fusion à 3 voies.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-302.png)
_Par défaut, `git merge` utilise un algorithme de fusion à 3 voies (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

L'état de `everyone.md` après avoir exécuté la commande ci-dessus serait le même que le résultat que vous avez obtenu en appliquant les patches avec `git apply -3`.

Si vous considérez l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-303.png)
_L'historique de Git après avoir effectué la fusion (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Vous verrez que le commit de fusion a effectivement deux parents : le premier est "Commit 11", c'est-à-dire, où `paul_branch_3` pointait avant la fusion. Le second est "Commit 12", où `john_branch_3` pointait, et pointe toujours maintenant.

Que se passera-t-il si vous fusionnez maintenant depuis `main` ? C'est-à-dire, basculez vers la branche principale, qui pointe vers "Commit 10" :

```
git checkout main
```

Et ensuite fusionnez la branche de Paul ?

```
git merge paul_branch_3
```

En effet, une avance rapide, comme avant d'exécuter cette commande, `main` était un ancêtre de `paul_branch_3`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-304.png)
_Une fusion par avance rapide (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Donc, il s'agit d'une fusion à 3 voies. En général, si toutes les versions sont d'accord sur une ligne, alors cette ligne est utilisée. Si `A` et la `base de fusion` correspondent, et que `B` a une autre version, `B` est prise. Dans le cas opposé, où la `base de fusion` et `B` correspondent, la version `A` est sélectionnée. Si `A` et `B` correspondent, cette version est prise, que la base de fusion soit d'accord ou non.

Cette description laisse une question ouverte : Que se passe-t-il dans les cas où les trois versions sont en désaccord ?

Eh bien, c'est un conflit que Git ne résout pas automatiquement. Dans ces cas, Git demande l'aide d'un humain.

## Comment Résoudre les Conflits de Fusion

En suivant jusqu'à présent, vous devriez comprendre les bases de `git merge`, et comment Git peut résoudre automatiquement certains conflits. Vous comprenez également quels cas sont résolus automatiquement.

Ensuite, considérons un cas plus avancé.

Disons que Paul et John continuent de travailler sur cette chanson.

Paul crée une nouvelle branche :

```
git checkout -b paul_branch_4
```

Et il décide d'ajouter quelques "Yeah" à la chanson, donc il change ce couplet comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-305.png)
_Les ajouts de Paul (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Donc Paul indexe et commite ces changements :

```git add everyone.md
git commit -m "Commit 13"
```

Paul crée également une autre chanson, `let_it_be.md` et l'ajoute au dépôt :

```
git add let_it_be.md
git commit -m "Commit 14"
```

Voici l'historique :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-356.png)
_L'historique après que Paul a introduit "Commit 14" (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Retour à `main` :

```
git checkout main
```

John crée également une branche :

```
git checkout -b john_branch_4
```

Et John travaille également sur la chanson "Everyone had a hard year", plus tard appelée "I've got a feeling" (encore une fois, ce n'est pas un article sur les Beatles, donc je ne m'étendrai pas sur le sujet ici. Voir l'annexe si vous êtes curieux).

John décide de changer toutes les occurrences de "Everyone" en "Everybody" :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-307.png)
_John change toutes les occurrences de "Everyone" en "Everybody" (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Il indexe et commite cette chanson dans le dépôt :

```
git add everyone.md
git commit -m "Commit 15"
```

Bien. Maintenant, John crée également une autre chanson, `across_the_universe.md`. Il l'ajoute également au dépôt :

```
git add across_the_universe.md
git commit -m "Commit 16"
```

Observez à nouveau l'historique :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-308.png)
_L'historique après que John a introduit "Commit 16" (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Vous pouvez voir que l'historique diverge de `main`, vers deux branches différentes – `paul_branch_4`, et `john_branch_4`.

À ce stade, John aimerait fusionner les changements introduits par Paul.

Que va-t-il se passer ici ?

Rappelez-vous les changements introduits par Paul :
```
git diff main paul_branch_4
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-309.png)
_La sortie de `git diff main paul_branch_4` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Que pensez-vous ? La fusion fonctionnera-t-elle ? 🤔

Essayez-le :
```
git merge paul_branch_4
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-311.png)
_Un conflit de fusion (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Nous avons un conflit ! 🥁

Il semble que Git ne puisse pas fusionner ces branches par lui-même. Vous pouvez obtenir un aperçu de l'état de la fusion, en utilisant `git status` :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-310.png)
_La sortie de `git status` juste après l'opération de `merge` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Les changements que Git n'a eu aucun problème à résoudre sont indexés pour le commit. Et il y a une section séparée pour les "chemins non fusionnés" – ce sont des fichiers avec des conflits que Git n'a pas pu résoudre par lui-même.

Il est temps de comprendre pourquoi et quand ces conflits se produisent, comment les résoudre, et aussi comment Git les gère sous le capot.
Alors alors ! J'espère que vous êtes au moins aussi excité que moi. 😇

Rappelons ce que nous savons sur les fusions à 3 voies :

Tout d'abord, Git recherchera la base de fusion – l'ancêtre commun de `john_branch_4` et `paul_branch_4`. Quel commit serait-ce ?

Correct, ce serait le sommet de la branche `main`, le commit dans lequel nous avons fusionné `john_branch_3` dans `paul_branch_3`.

Encore une fois, si vous n'êtes pas sûr, vous pouvez vérifier cela en exécutant :
```
git merge-base john_branch_4 paul_branch_4
```

Et à l'état actuel, `git status` sait quels fichiers sont indexés et lesquels ne le sont pas.

Considérez le processus pour chaque fichier, qui est le même que l'algorithme de fusion à 3 voies que nous avons considéré par ligne, mais au niveau d'un fichier :

`across_the_universe.md` existe sur la branche de John, mais n'existe pas sur la base de fusion ou sur la branche de Paul. Donc Git choisit d'inclure ce fichier. Puisque vous êtes déjà sur la branche de John et que ce fichier est inclus dans le sommet de cette branche, il n'est pas mentionné par `git status`.

`let_it_be.md` existe sur la branche de Paul, mais n'existe pas sur la base de fusion ou la branche de John. Donc `git merge` "choisit" de l'inclure.

Et pour `everyone.md` ? Eh bien, ici nous avons trois états différents de ce fichier : son état sur la base de fusion, son état sur la branche de John, et son état sur la branche de Paul. Lors de l'exécution d'une `fusion`, Git stocke toutes ces versions dans l'**index**. 

Observons cela en regardant directement l'index avec la commande `git ls-files` :

```
git ls-files -s –abbrev
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-312.png)
_La sortie de `git ls-files -s –abbrev` après l'opération de fusion (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Vous pouvez voir que `everyone.md` a trois entrées différentes. Git attribue à chaque version un numéro qui représente le "stade" du fichier, et il s'agit d'une propriété distincte d'une entrée d'index, aux côtés du nom du fichier et des bits de mode (j'ai couvert l'index dans [un article précédent](https://medium.com/swimm/a-visualized-intro-to-git-internals-objects-and-branches-68df85864037)).

Lorsqu'il n'y a pas de conflit de fusion concernant un fichier, son "stade" est `0`. C'est effectivement l'état pour `across_the_universe.md`, et pour `let_it_be.md`.

Dans un état de conflit, nous avons :

* Stade `1` – qui est la base de fusion.
* Stade `2` – qui est la version "votre". C'est-à-dire, la version du fichier sur la branche dans laquelle vous fusionnez. Dans notre exemple, ce serait `john_branch_4`.
* Stade `3` – qui est la version "leur", également appelée `MERGE_HEAD`. C'est-à-dire, la version sur la branche que vous fusionnez (dans la branche actuelle). Dans notre exemple, c'est `paul_branch_4`.

Pour observer le contenu du fichier dans un stade spécifique, vous pouvez utiliser une commande que j'ai introduite dans [un article précédent](https://medium.com/swimm/getting-hardcore-creating-a-repo-from-scratch-cc747edbb11c), `git cat-file`, et fournir le SHA du blob :

```
git cat-file -p <BLOB_SHA_FOR_STAGE_2>
```


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-313.png)
_Utilisation de `git cat-file` pour présenter le contenu du fichier sur la branche de John, directement à partir de son état dans l'index (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Et en effet, c'est le contenu que nous attendions – de la branche de John, où les lignes commencent par "Everybody" plutôt que "Everyone".

Une astuce sympa qui permet de voir le contenu rapidement sans fournir la valeur SHA-1 du blob, est d'utiliser `git show`, comme ceci :

```
git show :<STAGE>:everyone.md
```

Par exemple, pour obtenir le contenu de la même version que avec `git cat-file -p <BLOB_SHA_FOR_STAGE_2>`, vous pouvez écrire `git show :2:everyone.md`.

Git enregistre les trois états des trois commits dans l'index de cette manière au début de la fusion. Il suit ensuite l'algorithme de fusion à trois voies pour résoudre rapidement les cas simples :

Dans le cas où les trois stades correspondent, alors la sélection est triviale.

Si un côté a fait un changement tandis que l'autre n'a rien fait – c'est-à-dire, le stade 1 correspond au stade 2, alors nous choisissons le stade 3 – ou vice versa. C'est exactement ce qui s'est passé avec `let_it_be.md` et `across_the_universe.md`.

En cas de suppression sur la branche entrante, par exemple, et étant donné qu'il n'y avait pas de changements sur la branche actuelle, nous verrions alors que le stade 1 correspond au stade 2, mais qu'il n'y a pas de stade 3. Dans ce cas, `git merge` supprime le fichier pour la version fusionnée.

Ce qui est vraiment cool ici, c'est que pour la correspondance, Git n'a pas besoin des fichiers réels. Plutôt, il peut s'appuyer sur les valeurs SHA-1 des blobs correspondants. De cette manière, Git peut facilement détecter l'état dans lequel se trouve un fichier.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-352.png)
_Git effectue le même algorithme de fusion à 3 voies au niveau des fichiers (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Cool, donc pour `everyone.md` vous avez ce cas spécial – où le stade 1, le stade 2 et le stade 3 sont tous différents les uns des autres. C'est-à-dire, ils ont des SHA de blob différents. Il est temps d'aller plus loin et de comprendre le conflit de fusion. 😊

Une façon de faire cela serait de simplement utiliser `git diff`. Dans [un article précédent](https://www.freecodecamp.org/news/git-diff-and-patch/), nous avons examiné `git diff` en détail, et vu qu'il montre les différences entre diverses combinaisons de l'arborescence de travail, de l'index ou des commits. 

Mais `git diff` a également un mode spécial pour aider avec les conflits de fusion :

`git diff`

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-314.png)
_La sortie de `git diff` pendant un conflit (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Cette sortie peut être déroutante au premier abord, mais une fois que vous vous y êtes habitué, elle est assez claire. Commençons par la comprendre, puis voyons comment vous pouvez résoudre les conflits avec d'autres outils, plus visuels.

La section en conflit est séparée par les marques "égales" (====), et marquée avec les branches correspondantes. Dans ce contexte, "ours" est la branche actuelle. Dans cet exemple, ce serait `john_branch_4`, la branche vers laquelle `HEAD` pointait lorsque nous avons initié la commande `git merge`. "Theirs" est le `MERGE_HEAD`, la branche que nous fusionnons – dans ce cas, `paul_branch_4`.

Donc `git diff` sans aucun flag spécial montre les changements entre l'arborescence de travail et l'index, qui dans ce cas sont les conflits encore à résoudre. La sortie n'inclut pas les changements indexés, ce qui est très pratique pour résoudre le conflit.

Il est temps de résoudre cela manuellement. Amusant !

Alors, pourquoi est-ce un conflit ?

Pour Git, Paul et John ont apporté des modifications différentes à la même ligne, pour quelques lignes. John l'a changée en une chose, et Paul l'a changée en une autre chose. Git ne peut pas décider laquelle est correcte.

Ce n'est pas le cas pour les dernières lignes, comme la ligne qui était "Everyone had a hard year" sur la base de fusion. Paul n'a pas changé cette ligne, ou les lignes qui l'entourent, donc sa version sur `paul_branch_4`, ou "theirs" dans notre cas, est d'accord avec la merge_base. Pourtant, la version de John, "ours", est différente. Ainsi `git merge` peut facilement décider de prendre cette version.

Mais qu'en est-il des lignes en conflit ?

Dans ce cas, je sais ce que je veux, et c'est en fait une combinaison de ces lignes. Je veux que les lignes commencent par `Everybody`, suivant le changement de John, mais aussi qu'elles incluent les "yeah" de Paul. Alors allez-y et créez la version souhaitée en modifiant `everyone.md` :
`nano everyone.md`

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-315.png)
_Modification du fichier manuellement pour obtenir l'état souhaité (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Pour comparer le fichier résultant à ce que vous aviez dans la branche avant la fusion, vous pouvez exécuter :
```
git diff --ours
```

De même, si vous souhaitez voir comment le résultat de la fusion diffère de la branche que vous avez fusionnée dans notre branche, vous pouvez exécuter :
```
git diff –theirs
```

Vous pouvez même voir comment le résultat est différent des deux côtés en utilisant :
```
git diff –base
```

Vous pouvez maintenant indexer la version corrigée :
```
git add everyone.md
```

Après l'indexation, si vous regardez `git status`, vous ne verrez aucun conflit :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-316.png)
_Après avoir indexé la version corrigée `everyone.md`, il n'y a pas de conflits (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Vous pouvez maintenant simplement utiliser `git commit`, et Git vous présentera un message de commit contenant des détails sur la fusion. Vous pouvez le modifier si vous le souhaitez, ou le laisser tel quel. Peu importe le message de commit, Git créera un "commit de fusion" – c'est-à-dire, un commit avec plus d'un parent. 

Pour valider cela, considérons l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-317.png)
_L'historique après avoir terminé l'opération de fusion (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

`john_branch_4` pointe maintenant vers le nouveau commit de fusion. La branche entrante, "theirs", dans ce cas, `paul_branch_4`, reste où elle était.

# Comment Utiliser VS Code pour Résoudre les Conflits

Je vais vous montrer maintenant comment résoudre le même conflit en utilisant un outil graphique. Pour cet exemple, j'utiliserai VS Code, qui est gratuit et très courant. Il existe de nombreux autres outils, mais le processus est similaire, donc je vais simplement montrer VS Code comme exemple. 

Tout d'abord, revenez à l'état avant la fusion :
```
git reset --hard HEAD~
```

Et essayez de fusionner à nouveau :
```
git merge paul_branch_4
```

Vous devriez être de retour au même statut :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-318.png)
_De retour au statut de conflit (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Voyons comment cela apparaît sur VS Code :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-320.png)
_Résolution de conflit avec VS Code (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

VS Code marque les différentes versions avec "Current Change" – qui est la version "ours", le `HEAD` actuel, et "Incoming Change" pour la branche que nous fusionnons dans la branche active. Vous pouvez accepter l'un des changements (ou les deux) en cliquant sur l'une des options.

Si vous avez cliqué sur `Resolve in Merge editor`, vous obtiendrez une vue plus visuelle de l'état. VS Code montre l'état de chaque ligne :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-321.png)
_Éditeur de fusion de VS Code (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Si vous regardez de près, vous verrez que VS Code montre les changements au sein des mots – par exemple, montrant que "Every**one**" a été changé en "Every**body**", en marquant les parties changées. 

Vous pouvez accepter l'une ou l'autre version, ou vous pouvez accepter une combinaison. Dans ce cas, si vous cliquez sur "Accept Combination", vous obtenez ce résultat :


![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-322.png)
_Éditeur de fusion de VS Code après avoir cliqué sur "Accept Combination" (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

VS Code a fait un très bon travail ! Le même algorithme de fusion à trois voies a été implémenté ici et utilisé au niveau du *mot* plutôt qu'au niveau de la *ligne*. Ainsi, VS Code a pu résoudre ce conflit de manière plutôt impressionnante. Bien sûr, vous pouvez modifier la suggestion de VS Code, mais il a fourni un très bon point de départ.


# Un Outil Puissant de Plus 🧫
Eh bien, c'était la première fois dans toute cette série d'articles sur Git que j'utilise un outil avec une interface graphique. En effet, les interfaces graphiques peuvent être très pratiques pour comprendre ce qui se passe lorsque vous résolvez des conflits de fusion.

Cependant, comme dans de nombreux autres cas, lorsque nous avons besoin des gros canons ou que nous voulons *vraiment* comprendre ce qui se passe, la ligne de commande devient pratique. Alors retournons à la ligne de commande et apprenons un outil qui peut s'avérer utile dans des cas plus compliqués.

Encore une fois, revenez à l'état avant la fusion :
```
git reset --hard HEAD~
```

Et fusionnez :
```
git merge paul_branch_4
```

Et disons, vous n'êtes pas exactement sûr de ce qui s'est passé. Pourquoi y a-t-il un conflit ? Une commande très utile serait :
```
git log -p –merge
```

Pour rappel, `git log` montre l'historique des commits qui sont accessibles depuis `HEAD`. L'ajout de `-p` indique à `git log` d'afficher les commits avec les diffs qu'ils ont introduits. L'option `--merge` fait en sorte que la commande affiche tous les commits contenant des changements pertinents pour tout *fichier non fusionné*, sur l'une ou l'autre branche, avec leurs diffs.

Cela peut vous aider à identifier les changements dans l'historique qui ont conduit aux conflits. Donc dans cet exemple, vous verriez :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-323.png)
_La sortie de `git log -p –merge` (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Le premier commit que nous voyons est "Commit 15", car dans ce commit John a modifié `everyone.md`, un fichier qui a encore des conflits. Ensuite, Git montre "Commit 13", où Paul a changé `everyone.md` :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-324.png)
_La sortie de `git log -p –merge` - suite (Source : [Brief](https://www.youtube.com/watch?v=BCNZ5Uxctuk&t=561s&ab_channel=Brief))_

Remarquez que `git log --merge` n'a pas mentionné les commits précédents qui avaient modifié `everyone.md` avant "Commit 13", car ils n'avaient pas affecté le conflit actuel.

De cette manière, `git log` vous dit tout ce que vous devez savoir pour comprendre le processus qui vous a conduit à l'état de conflit actuel. Cool ! 😎

En utilisant la ligne de commande, vous pouvez également demander à Git de ne prendre qu'un seul côté des changements – soit "ours" soit "theirs", même pour un fichier spécifique. 

Vous pouvez également instruire Git de prendre certaines parties des diffs d'un fichier et d'autres d'un autre fichier. Je fournirai des liens qui décrivent comment faire cela dans la section des ressources supplémentaires ci-dessous. 

Pour la plupart, vous pouvez accomplir cela assez facilement soit manuellement, soit à partir de l'interface utilisateur de votre IDE préféré.

Pour l'instant, il est temps pour un récapitulatif.

# Récapitulatif

Dans ce guide, vous avez obtenu un aperçu approfondi de la fusion avec Git. Vous avez appris que la fusion est le processus de combinaison des changements récents de plusieurs branches en un seul nouveau commit. Le nouveau commit a deux parents – ceux qui étaient les sommets des branches qui ont été fusionnées.

Nous avons considéré une fusion simple par avance rapide, qui est possible lorsqu'une branche a divergé de la branche de base, puis a simplement ajouté des commits au-dessus de la branche de base. 

Nous avons ensuite considéré les fusions à trois voies, et expliqué le processus en trois étapes :

* Tout d'abord, Git localise la base de fusion. Pour rappel, il s'agit du premier commit qui est accessible depuis les deux branches.
* Deuxièmement, Git calcule deux diffs – un diff de la base de fusion à la *première* branche, et un autre diff de la base de fusion à la *deuxième* branche. Git génère des patches basés sur ces diffs.
* Troisièmement et enfin, Git applique les deux patches à la base de fusion en utilisant un algorithme de fusion à 3 voies. Le résultat est l'état du nouveau commit de fusion.

Nous avons approfondi le processus d'une fusion à 3 voies, qu'elle soit au niveau des fichiers ou des blocs. Nous avons considéré quand Git est capable de s'appuyer sur une fusion à 3 voies pour résoudre automatiquement les conflits, et quand il ne peut pas. 

Vous avez vu la sortie de `git diff` lorsque nous sommes dans un état de conflit, et comment résoudre les conflits soit manuellement, soit avec VS Code.

Il y a beaucoup plus à dire sur les fusions – différentes stratégies de fusion, fusions récursives, et ainsi de suite. Pourtant, après ce guide, vous devriez avoir une compréhension solide de ce qu'est une fusion, et de ce qui se passe sous le capot dans la grande majorité des cas.

# **À Propos de l'Auteur**

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la chaîne YouTube Brief [YouTube Channel](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros).

# **Références Supplémentaires**

* [Liste de lecture YouTube sur les Internes de Git – par Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7).
* [Article précédent d'Omer sur les internes de Git.](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/)
* [Article d'Omer sur Git UNDO - réécrire l'historique avec Git](https://medium.com/@Omer_Rosenbaum/git-undo-how-to-rewrite-git-history-with-confidence-d4452e2969c2).
* [https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging).
* [https://blog.plasticscm.com/2010/11/live-to-merge-merge-to-live.html](https://blog.plasticscm.com/2010/11/live-to-merge-merge-to-live.html).
* [https://www.oreilly.com/library/view/git-pocket-guide/9781449327507/ch07.html](https://www.oreilly.com/library/view/git-pocket-guide/9781449327507/ch07.html).
* [https://jwiegley.github.io/git-from-the-bottom-up/1-Repository/4-how-trees-are-made.html](https://jwiegley.github.io/git-from-the-bottom-up/1-Repository/4-how-trees-are-made.html).

# Annexe – Ressources liées aux Beatles

* [https://www.the-paulmccartney-project.com/song/ive-got-a-feeling/](https://www.the-paulmccartney-project.com/song/ive-got-a-feeling/)
* [https://www.cheatsheet.com/entertainment/did-john-lennon-or-paul-mccartney-write-the-classic-a-day-in-the-life.html/](https://www.cheatsheet.com/entertainment/did-john-lennon-or-paul-mccartney-write-the-classic-a-day-in-the-life.html/)
* [http://lifeofthebeatles.blogspot.com/2009/06/ive-got-feeling-lyrics.html](http://lifeofthebeatles.blogspot.com/2009/06/ive-got-feeling-lyrics.html)