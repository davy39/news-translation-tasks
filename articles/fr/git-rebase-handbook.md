---
title: Le Guide Git Rebase – Un Guide Définitif pour le Rebasing
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2023-07-03T13:56:34.000Z'
originalURL: https://freecodecamp.org/news/git-rebase-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/The-Git-Rebase-Handbook-Book-Cover--1-.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Le Guide Git Rebase – Un Guide Définitif pour le Rebasing
seo_desc: "One of the most powerful tools a developer can have in their toolbox is\
  \ git rebase. Yet it is notorious for being complex and misunderstood. \nThe truth\
  \ is, if you understand what it actually does, git rebase is a very elegant, and\
  \ straightforward too..."
---

L'un des outils les plus puissants qu'un développeur peut avoir dans sa boîte à outils est `git rebase`. Pourtant, il est notoire pour être complexe et mal compris. 

La vérité est que, si vous comprenez ce qu'il fait _réellement_, `git rebase` est un outil très élégant et simple pour accomplir tant de choses différentes dans Git.

Dans les articles précédents, vous avez compris [ce que sont les diffs Git](https://www.freecodecamp.org/news/git-diff-and-patch/), [ce qu'est une fusion](https://www.freecodecamp.org/news/the-definitive-guide-to-git-merge/), et [comment Git résout les conflits de fusion](https://www.freecodecamp.org/news/the-definitive-guide-to-git-merge/). Dans cet article, vous comprendrez ce qu'est le rebase Git, pourquoi il est différent de la fusion, et comment rebaser avec confiance 🧑🏽‍💻

## Notes avant de commencer

1. J'ai également créé une vidéo couvrant le contenu de cet article. Si vous souhaitez la regarder en parallèle de la lecture, vous pouvez la trouver [ici](https://youtu.be/3VFsitGUB3s).
2. Si vous souhaitez jouer avec le dépôt que j'ai utilisé et essayer les commandes vous-même, vous pouvez obtenir le dépôt [ici](https://github.com/Omerr/rebase_playground).
3. Je travaille sur un livre sur Git ! Êtes-vous intéressé à lire les versions initiales et à fournir des commentaires ? Envoyez-moi un email : [gitting.things@gmail.com](https://www.freecodecamp.org/news/p/2e1fc200-f447-4f55-b0a3-73ef790a2190/gitting.things@gmail.com)

D'accord, êtes-vous prêt ?

# Récapitulatif court - Qu'est-ce que la fusion Git ? 🧑🏽‍💻

Sous le capot, `git rebase` et `git merge` sont des choses très, très différentes. Alors pourquoi les gens les comparent-ils tout le temps ?

La raison est leur utilisation. Lorsque vous travaillez avec Git, vous travaillez généralement dans différentes branches et introduisez des changements dans ces branches. 

Dans [un tutoriel précédent](https://www.freecodecamp.org/news/the-definitive-guide-to-git-merge/#howgits3waymergealgorithmworks), j'ai donné un exemple où John et Paul (des Beatles) co-écrivaient une nouvelle chanson. Ils ont commencé à partir de la branche `main`, puis chacun a divergé, modifié les paroles et validé leurs changements. 

Ensuite, les deux ont voulu intégrer leurs changements, ce qui est quelque chose qui arrive très fréquemment lorsque vous travaillez avec Git.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-197.png)
_Un historique divergent - `paul_branch` et `john_branch` ont divergé de `main` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Il existe deux principales façons d'intégrer les changements introduits dans différentes branches dans Git, ou en d'autres termes, différents commits et historiques de commits. Ce sont la fusion et le rebase.

[Dans un tutoriel précédent](https://www.freecodecamp.org/news/the-definitive-guide-to-git-merge/), nous avons bien appris à connaître `git merge`. Nous avons vu que lors de l'exécution d'une fusion, nous créons un **commit de fusion** – où le contenu de ce commit est une combinaison des deux branches, et il a également deux parents, un dans chaque branche.

Donc, disons que vous êtes sur la branche `john_branch` (en supposant l'historique représenté dans le dessin ci-dessus), et que vous exécutez `git merge paul_branch`. Vous obtiendrez cet état – où sur `john_branch`, il y a un nouveau commit avec deux parents. Le premier sera le commit sur la branche `john_branch` où `HEAD` pointait avant d'effectuer la fusion, dans ce cas - "Commit 6". Le second sera le commit pointé par `paul_branch`, "Commit 9".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-196.png)
_Le résultat de l'exécution de `git merge paul_branch` : un nouveau Commit de Fusion avec deux parents (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Regardez à nouveau le graphique d'historique : vous avez créé un historique **divergent**. Vous pouvez réellement voir où il a bifurqué et où il a fusionné à nouveau.

Ainsi, lorsque vous utilisez `git merge`, vous ne réécrivez pas l'historique – mais plutôt, vous ajoutez un commit à l'historique existant. Et spécifiquement, un commit qui crée un historique divergent.

# En quoi `git rebase` est-il différent de `git merge` ? 🧑🏽‍💻

Lorsque vous utilisez `git rebase`, quelque chose de différent se produit. 🤑

Commençons par le tableau général : si vous êtes sur `paul_branch`, et que vous utilisez `git rebase john_branch`, Git va à l'ancêtre commun de la branche de John et de la branche de Paul. Ensuite, il prend les patches introduits dans les commits sur la branche de Paul, et applique ces changements à la branche de John. 

Ainsi, ici, vous utilisez `rebase` pour prendre les changements qui ont été validés sur une branche – la branche de Paul – et les rejouer sur une autre branche, `john_branch`.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-198.png)
_Le résultat de l'exécution de `git rebase john_branch` : les commits sur `paul_branch` ont été "rejoués" au-dessus de `john_branch` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Attendez, que signifie cela ? 🧑🏽‍💻

Nous allons maintenant prendre cela bit par bit pour nous assurer que vous comprenez pleinement ce qui se passe sous le capot 😊

# `cherry-pick` comme base pour le rebase

Il est utile de penser au rebase comme effectuant `git cherry-pick` – une commande qui prend un commit, calcule le _patch_ que ce commit introduit en calculant la différence entre le commit parent et le commit lui-même, puis `cherry-pick` "rejoue" cette différence.

Faisons cela manuellement.

Si nous regardons la différence introduite par "Commit 5" en effectuant `git diff main <SHA_OF_COMMIT_5>` :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-199.png)
_Exécution de `git diff` pour observer le patch introduit par "Commit 5" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

(Si vous souhaitez jouer avec le dépôt que j'ai utilisé et essayer les commandes vous-même, vous pouvez obtenir le dépôt [ici](https://github.com/Omerr/rebase_playground)).

Vous pouvez voir que dans ce commit, John a commencé à travailler sur une chanson appelée "Lucy in the Sky with Diamonds" :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-200.png)
_La sortie de `git diff` - le patch introduit par "Commit 5" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Pour rappel, vous pouvez également utiliser la commande `git show` pour obtenir la même sortie :

```
git show <SHA_OF_COMMIT_5>
```

Maintenant, si vous `cherry-pick` ce commit, vous introduirez ce changement spécifiquement, sur la branche active. Passez d'abord à `main` :

`git checkout main` (ou `git switch main`)

Et créez une autre branche, juste pour être clair :

`git checkout -b my_branch` (ou `git switch -c my_branch`)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-201.png)
_Création de `my_branch` qui bifurque de `main` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Et `cherry-pick` ce commit :

```
git cherry-pick <SHA_OF_COMMIT_5>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-202.png)
_Utilisation de `cherry-pick` pour appliquer les changements introduits dans "Commit 5" sur `main` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Consultez le journal (sortie de `git lol`) :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-205.png)
_La sortie de `git lol` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

(`git lol` est un alias que j'ai ajouté à Git pour voir visuellement l'historique de manière graphique. Vous pouvez le trouver [ici](https://gist.github.com/Omerr/8134a61b56ca82dd90e546e7ef04eb77)).

Il semble que vous ayez _copié-collé_ "Commit 5". Rappelez-vous que même s'il a le même message de commit, et introduit les mêmes changements, et même pointe vers le même objet arbre que le "Commit 5" original dans ce cas – il s'agit toujours d'un objet commit différent, car il a été créé avec un horodatage différent.

En regardant les changements, en utilisant `git show HEAD` :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-204.png)
_La sortie de `git show HEAD` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Ils sont les mêmes que ceux de "Commit 5".

Et bien sûr, si vous regardez le fichier (par exemple, en utilisant `nano lucy_in_the_sky_with_diamonds.md`), il sera dans le même état qu'après le "Commit 5" original.

Cool ! 😊

D'accord, vous pouvez maintenant supprimer la nouvelle branche pour qu'elle n'apparaisse plus dans votre historique à chaque fois :

```
git checkout main
git branch -D my_branch
```

## Au-delà de `cherry-pick` – Comment utiliser `git rebase`

Vous pouvez considérer `git rebase` comme un moyen d'effectuer plusieurs `cherry-pick` les uns après les autres – c'est-à-dire, de "rejouer" plusieurs commits. Ce n'est pas la seule chose que vous pouvez faire avec `rebase`, mais c'est un bon point de départ pour notre explication.

Il est temps de jouer avec `git rebase` ! 👏🏽👏🏽

Auparavant, vous avez fusionné `paul_branch` dans `john_branch`. Que se passerait-il si vous _rebasiez_ `paul_branch` sur `john_branch` ? Vous obtiendriez un historique très différent.

En essence, cela semblerait comme si nous avions pris les changements introduits dans les commits sur `paul_branch`, et les avions rejoués sur `john_branch`. Le résultat serait un historique **linéaire**.

Pour comprendre le processus, je vais fournir une vue d'ensemble de haut niveau, puis approfondir chaque étape. Le processus de rebasage d'une branche sur une autre branche est le suivant :

1. Trouver l'ancêtre commun.
2. Identifier les commits à "rejouer".
3. Pour chaque commit `X`, calculer `diff(parent(X), X)`, et le stocker comme un `patch(X)`.
4. Déplacer `HEAD` vers la nouvelle base.
5. Appliquer les patches générés dans l'ordre sur la branche cible. Chaque fois, créer un nouvel objet commit avec le nouvel état.

Le processus de création de nouveaux commits avec les mêmes changements que les existants est également appelé **"rejouer"** ces commits, un terme que nous avons déjà utilisé.

# **Il est temps de passer à la pratique avec Rebase👍🏽**

Commencez par la branche de Paul :

```
git checkout paul_branch
```

Voici l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-206.png)
_Historique des commits avant d'effectuer `git rebase` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Et maintenant, la partie excitante :

```
git rebase john_branch
```

Et observez l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-207.png)
_L'historique après le rebasage (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

(`gg` est un alias pour un outil externe que j'ai introduit [dans la vidéo](https://youtu.be/3VFsitGUB3s)).

Ainsi, alors qu'avec `git merge` vous avez ajouté à l'historique, avec `git rebase` vous **réécrivez l'historique**. Vous créez de **nouveaux** objets commit. De plus, le résultat est un graphique d'historique linéaire – plutôt qu'un graphique divergent.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-209.png)
_L'historique après le rebasage (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

En essence, nous avons "copié" les commits qui étaient sur `paul_branch` et introduits après "Commit 4", et "collés" au-dessus de `john_branch`.

La commande s'appelle "rebase", car elle change le commit de base de la branche à partir de laquelle elle est exécutée. C'est-à-dire, dans votre cas, avant d'exécuter `git rebase`, la base de `paul_branch` était "Commit 4" – car c'est là que la branche est "née" (à partir de `main`). Avec `rebase`, vous avez demandé à Git de lui donner une autre base – c'est-à-dire, de faire semblant qu'elle était née de "Commit 6".

Pour ce faire, Git a pris ce qui était "Commit 7", et a "rejoué" les changements introduits dans ce commit sur "Commit 6", puis a créé un nouvel objet commit. Cet objet diffère du "Commit 7" original sur trois aspects :

1. Il a un horodatage différent.
2. Il a un commit parent différent – "Commit 6" plutôt que "Commit 4".
3. L'[objet arbre](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/) qu'il pointe est différent - car les changements ont été introduits dans l'arbre pointé par "Commit 6", et non l'arbre pointé par "Commit 4".

Remarquez le dernier commit ici, "Commit 9'". Le snapshot qu'il représente (c'est-à-dire l'[arbre](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/) qu'il pointe) est exactement le même arbre que vous obtiendriez en fusionnant les deux branches. L'état des fichiers dans votre dépôt Git serait **le même** que si vous aviez utilisé `git merge`. Seule l'historique est différente, et bien sûr les objets commit.

Maintenant, vous pouvez simplement utiliser :

```
git checkout main
git merge paul_branch
```

Hmm.... Que se passerait-il si vous exécutiez cette dernière commande ? 🧑🏽‍💻 Considérez à nouveau l'historique des commits, après avoir basculé sur `main` :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-210.png)
_L'historique après le rebasage et le basculement sur `main` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Que signifierait fusionner `main` et `paul_branch` ?

En effet, Git peut simplement effectuer une fusion par avance rapide, car l'historique est complètement linéaire (si vous avez besoin d'un rappel sur les fusions par avance rapide, consultez [cet article](https://www.freecodecamp.org/news/the-definitive-guide-to-git-merge/#timetogethandson)). En conséquence, `main` et `paul_branch` pointent maintenant vers le même commit :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-211.png)
_Le résultat d'une fusion par avance rapide (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

# Rebasing avancé dans Git🧑🏽‍💻

Maintenant que vous comprenez les bases du rebase, il est temps de considérer des cas plus avancés, où des commutateurs et des arguments supplémentaires pour la commande `rebase` seront utiles.

Dans l'exemple précédent, lorsque vous avez simplement dit `rebase` (sans commutateurs supplémentaires), Git a rejoué tous les commits de l'ancêtre commun à la pointe de la branche actuelle.

Mais le rebase est une super-puissance, c'est une commande toute-puissante capable de... eh bien, réécrire l'historique. Et il peut être utile si vous souhaitez modifier l'historique pour le rendre conforme à vos besoins.

Annulez la dernière fusion en faisant pointer `main` à nouveau sur "Commit 4" :

```
git reset --hard <ORIGINAL_COMMIT 4>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-238.png)
_"Annulation" de la dernière opération de fusion (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Et annulez le rebasage en utilisant :

```
git checkout paul_branch
git reset --hard <ORIGINAL_COMMIT 9>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-239.png)
_"Annulation" de l'opération de rebase (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Remarquez que vous avez obtenu exactement le même historique que vous aviez avant :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-240.png)
_Visualisation de l'historique après "annulation" de l'opération de rebase (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Pour être clair, "Commit 9" ne disparaît pas simplement lorsqu'il n'est plus accessible depuis le `HEAD` actuel. Plutôt, il est toujours stocké dans la base de données des objets. Et comme vous avez utilisé `git reset` pour changer `HEAD` pour pointer vers ce commit, vous avez pu le récupérer, ainsi que ses commits parents puisqu'ils sont également stockés dans la base de données. Plutôt cool, non ? 😊

D'accord, visualisez rapidement les changements que Paul a introduits :

```
git show HEAD
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-241.png)
_`git show HEAD` montre le patch introduit par "Commit 9" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Continuez à remonter dans le graphe des commits :

```
git show HEAD~
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-242.png)
_`git show HEAD~` (identique à `git show HEAD~1`) montre le patch introduit par "Commit 8" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Et un commit plus loin :

```
git show HEAD~2
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-243.png)
_`git show HEAD~2` montre le patch introduit par "Commit 7" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Donc, ces changements sont bien, mais peut-être que Paul ne veut pas ce genre d'historique. Plutôt, il veut que cela semble comme s'il avait introduit les changements dans "Commit 7" et "Commit 8" en un seul commit.

Pour cela, vous pouvez utiliser un rebase **interactif**. Pour ce faire, nous ajoutons le commutateur `-i` (ou `--interactive`) à la commande `rebase` :

```
git rebase -i <SHA_OF_COMMIT_4>
```

Ou, puisque `main` pointe vers "Commit 4", nous pouvons simplement exécuter :

```
git rebase -i main
```

En exécutant cette commande, vous dites à Git d'utiliser une nouvelle base, "Commit 4". Vous demandez donc à Git de revenir à tous les commits qui ont été introduits après "Commit 4" et qui sont accessibles depuis le `HEAD` actuel, et de rejouer ces commits.

Pour chaque commit qui est rejoué, Git nous demande ce que nous aimerions faire avec :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-250.png)
_`git rebase -i main` vous invite à sélectionner ce que vous voulez faire avec chaque commit (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Dans ce contexte, il est utile de penser à un commit comme à un patch. C'est-à-dire, "Commit 7" comme dans "le patch que "Commit 7" a introduit sur son parent".

Une option est d'utiliser `pick`. C'est le comportement par défaut, qui indique à Git de rejouer les changements introduits dans ce commit. Dans ce cas, si vous le laissez tel quel – et `pick` tous les commits – vous obtiendrez le même historique, et Git ne créera même pas de nouveaux objets commit.

Une autre option est `squash`. Un commit _squashed_ aura son contenu "plié" dans le contenu du commit qui le précède. Donc dans notre cas, Paul aimerait squasher "Commit 8" dans "Commit 7" :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-251.png)
_Squash de "Commit 8" dans "Commit 7" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Comme vous pouvez le voir, `git rebase -i` fournit des options supplémentaires, mais nous n'entrerons pas dans tous les détails dans cet article. Si vous laissez le rebase s'exécuter, vous serez invité à sélectionner un message de commit pour le nouveau commit créé (c'est-à-dire, celui qui introduit les changements des deux "Commit 7" et "Commit 8") :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-252.png)
_Fournir le message de commit : `Commits 7+8` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Et regardez l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-253.png)
_L'historique après le rebase interactif (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Exactement comme nous le voulions ! Nous avons sur `paul_branch` "Commit 9" (bien sûr, c'est un objet différent du "Commit 9" original). Celui-ci pointe vers "Commits 7+8", qui est un seul commit introduisant les changements des deux "Commit 7" et "Commit 8" originaux. Le parent de ce commit est "Commit 4", où `main` pointe. Vous avez `john_branch`.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-254.png)
_L'historique après le rebase interactif - visualisé (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Oh wow, ce n'est pas cool ? 😊

`git rebase` vous donne un contrôle illimité sur la forme de n'importe quelle branche. Vous pouvez l'utiliser pour réorganiser les commits, ou pour supprimer des changements incorrects, ou modifier un changement rétrospectivement. Alternativement, vous pourriez peut-être déplacer la base de votre branche sur un autre commit, n'importe quel commit que vous souhaitez.

## Comment utiliser le commutateur `--onto` de `git rebase`

Considérons un autre exemple. Allez à `main` à nouveau :

```
git checkout main
```

Et supprimez les pointeurs vers `paul_branch` et `john_branch` pour ne plus les voir dans le graphe des commits :

```
git branch -D paul_branch
git branch -D john_branch
```

Et maintenant, créez une branche à partir de `main` vers une nouvelle branche :

```
git checkout -b new_branch
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-255.png)
_Création de `new_branch` qui diverge de `main` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-256.png)
_Un historique propre avec `new_branch` qui diverge de `main` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Maintenant, ajoutez quelques changements ici et validez-les :

```
nano code.py
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-257.png)
_Ajout de la fonction `new_branch` à `code.py` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

```
git add code.py
git commit -m "Commit 10"
```

Retournez à `main` :

```
git checkout main
```

Et introduisez un autre changement :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-258.png)
_Ajout d'une docstring au début du fichier (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Il est temps de préparer et de valider ces changements :

```
git add code.py
git commit -m "Commit 11"
```

Et encore un autre changement :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-259.png)
_Ajout de `@Author` à la docstring (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Validez également ce changement :

```
git add code.py
git commit -m "Commit 12"
```

Oh attendez, maintenant je réalise que je voulais que vous fassiez les changements introduits dans "Commit 11" dans le cadre de `new_branch`. Ugh. Que pouvez-vous faire ? 🧑🏽‍💻

Considérez l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-260.png)
_L'historique après l'introduction de "Commit 12" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Ce que je veux, c'est que, au lieu d'avoir "Commit 10" résider uniquement sur la branche `main`, je veux qu'il soit à la fois sur la branche `main` ainsi que sur la branche `new_branch`. Visuellement, je voudrais le déplacer vers le bas du graphe ici :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-261.png)
_Visuellement, je veux que vous "poussiez" "Commit 10" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Pouvez-vous voir où je veux en venir ? 😊

Eh bien, comme nous le comprenons, le rebase nous permet de _rejouer_ les changements introduits dans `new_branch`, ceux introduits dans "Commit 10", comme s'ils avaient été initialement effectués sur "Commit 11", plutôt que sur "Commit 4".

Pour ce faire, vous pouvez utiliser d'autres arguments de `git rebase`. Vous direz à Git que vous voulez prendre tout l'historique introduit entre l'ancêtre commun de `main` et `new_branch`, qui est "Commit 4", et avoir la nouvelle base pour cet historique être "Commit 11". Pour ce faire, utilisez :

```
git rebase --onto <SHA_OF_COMMIT_11> main new_branch
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-262.png)
_L'historique avant et après le rebase, "Commit 10" a été "poussé" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Et regardez notre bel historique ! 😊

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-263.png)
_L'historique avant et après le rebase, "Commit 10" a été "poussé" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Considérons un autre cas.

Disons que j'ai commencé à travailler sur une branche, et par erreur j'ai commencé à travailler à partir de `feature_branch_1`, plutôt que de `main`.

Donc pour émuler cela, créez `feature_branch_1` :

```
git checkout main
git checkout -b feature_branch_1
```

Et effacez `new_branch` pour ne plus le voir dans le graphe :

```
git branch -D new_branch
```

Créez un fichier Python simple appelé `1.py` :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-264.png)
_Un nouveau fichier, `1.py`, avec `print('Hello world!')` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Préparez et validez ce fichier :

```
git add 1.py
git commit -m "Commit 13"
```

Maintenant, bifurquez (par erreur) à partir de `feature_branch_1` :

```
git checkout -b feature_branch_2
```

Et créez un autre fichier, `2.py` :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-265.png)
_Création de `2.py` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Préparez et validez également ce fichier :

```
git add 2.py
git commit -m "Commit 14"
```

Et introduisez un peu plus de code dans `2.py` :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-266.png)
_Modification de `2.py` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Préparez et validez également ces changements :

```
git add 2.py
git commit -m "Commit 15"
```

Jusqu'à présent, vous devriez avoir cet historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-267.png)
_L'historique après l'introduction de "Commit 15" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Retournez à `feature_branch_1` et modifiez `1.py` :

```
git checkout feature_branch_1
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-268.png)
_Modification de `1.py` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Maintenant, préparez et validez :

```
git add 1.py
git commit -m "Commit 16"
```

Votre historique devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-270.png)
_L'historique après l'introduction de "Commit 16" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Disons maintenant que vous réalisez que vous avez fait une erreur. Vous vouliez en fait que `feature_branch_2` naisse de la branche `main`, plutôt que de `feature_branch_1`.

Comment pouvez-vous y parvenir ? 🧑🏽‍💻

Essayez d'y réfléchir en fonction du graphe d'historique et de ce que vous avez appris sur le drapeau `--onto` pour la commande `rebase`.

Eh bien, vous voulez "remplacer" le parent de votre premier commit sur `feature_branch_2`, qui est "Commit 14", pour qu'il soit au-dessus de la branche `main`, dans ce cas, "Commit 12", plutôt que le début de `feature_branch_1`, dans ce cas, "Commit 13". Donc encore une fois, vous allez créer une _nouvelle base_, cette fois pour le premier commit sur `feature_branch_2`.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-271.png)
_Vous voulez déplacer "Commit 14" et "Commit 15" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Comment feriez-vous cela ?

D'abord, basculez vers `feature_branch_2` :

```
git checkout feature_branch_2
```

Et maintenant vous pouvez utiliser :

```
git rebase --onto main <SHA_OF_COMMIT_13>
```

En conséquence, vous avez `feature_branch_2` basé sur `main` plutôt que sur `feature_branch_1` :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-272.png)
_L'historique des commits après avoir effectué le rebase (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

La syntaxe de la commande est :

```
git rebase --onto <new_parent> <old_parent>
```

## Comment rebaser sur une seule branche

Vous pouvez également utiliser `git rebase` tout en regardant l'historique d'une seule branche.

Voyons si vous pouvez m'aider ici.

Disons que j'ai travaillé à partir de `feature_branch_2`, et spécifiquement édité le fichier `code.py`. J'ai commencé par changer toutes les chaînes pour qu'elles soient entourées de guillemets doubles plutôt que de guillemets simples :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-273.png)
_Changement de `'` en `"` dans `code.py` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Ensuite, j'ai préparé et validé :

```
git add code.py
git commit -m "Commit 17"
```

J'ai ensuite décidé d'ajouter une nouvelle fonction au début du fichier :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-274.png)
_Ajout de la fonction `another_feature` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Encore une fois, j'ai préparé et validé :

```
git add code.py
git commit -m "Commit 18"
```

Et maintenant, je me suis rendu compte que j'avais en fait oublié de changer les guillemets simples en guillemets doubles entourant le `__main__` (comme vous l'avez peut-être remarqué), alors je l'ai fait aussi :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-275.png)
_Changement de `'__main__'` en `"__main__"` (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Bien sûr, j'ai préparé et validé ce changement :

```
git add code.py
git commit -m "Commit 19"
```

Maintenant, considérez l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-276.png)
_L'historique des commits après l'introduction de "Commit 19" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Ce n'est pas vraiment beau, n'est-ce pas ? Je veux dire, j'ai deux commits qui sont liés l'un à l'autre, "Commit 17" et "Commit 19" (transformant les `'` en `"`), mais ils sont séparés par le "Commit 18" sans rapport (où j'ai ajouté une nouvelle fonction). Que pouvons-nous faire ? 🧑🏽‍💻 Pouvez-vous m'aider ?

Intuitivement, je veux éditer l'historique ici :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-277.png)
_Ce sont les commits que je veux éditer (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Alors, que feriez-vous ?

Vous avez raison ! 👏🏽

Je peux rebaser l'historique de "Commit 17" à "Commit 19", sur "Commit 15". Pour ce faire :

```
git rebase --interactive --onto <SHA_OF_COMMIT_15> <SHA_OF_COMMIT_15>
```

Remarquez que j'ai spécifié "Commit 15" comme le début de la plage de commits, en excluant ce commit. Et je n'ai pas eu besoin de spécifier explicitement `HEAD` comme dernier paramètre.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-279.png)
_Utilisation de `rebase --onto` sur une seule branche (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Après avoir suivi vos conseils et exécuté la commande `rebase` (merci ! 😊) j'obtiens l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-280.png)
_Rebase interactif (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Alors, que ferais-je ? Je veux mettre "Commit 19" _avant_ "Commit 18", pour qu'il vienne juste après "Commit 17". Je peux aller plus loin et les fusionner ensemble, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-281.png)
_Rebase interactif - changement de l'ordre des commits et fusion (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Maintenant, lorsque je suis invité à fournir un message de commit, je peux fournir le message "Commit 17+19" :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-282.png)
_Fournir un message de commit (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Et maintenant, voyez notre bel historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-283.png)
_L'historique résultant (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Merci encore ! 👍🏽

# Plus de cas d'utilisation de Rebase + Plus de Pratique

J'espère que vous vous sentez maintenant à l'aise avec la syntaxe de rebase. La meilleure façon de vraiment le comprendre est de considérer divers cas et de trouver comment les résoudre vous-même. 

Avec les cas d'utilisation à venir, je vous suggère fortement d'arrêter de lire après que j'ai introduit chaque cas d'utilisation, puis d'essayer de le résoudre par vous-même.

## Comment Exclure des Commits 

Disons que vous avez cet historique sur un autre dépôt :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-284.png)
_Un autre historique de commits (Source : [Brief](https://youtu.be/3VFsitGUB3s))_



Avant de jouer avec, stockez une étiquette sur "Commit F" pour pouvoir y revenir plus tard :

```
git tag original_commit_f
```

Maintenant, vous ne voulez pas que les changements dans "Commit C" et "Commit D" soient inclus. Vous pourriez utiliser un rebase interactif comme avant et supprimer leurs changements. Ou, vous pourriez utiliser à nouveau `git rebase --onto`. Comment utiliseriez-vous `--onto` afin de "supprimer" ces deux commits ?

Vous pouvez rebaser `HEAD` sur "Commit B", où l'ancien parent était en fait "Commit D", et maintenant il devrait être "Commit B". Considérez à nouveau l'historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-284.png)
_L'historique à nouveau (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Rebaser de sorte que "Commit B" soit la base de "Commit E", signifie "déplacer" à la fois "Commit E" et "Commit F", et leur donner une autre _base_ – "Commit B". Pouvez-vous trouver la commande vous-même ?

```
git rebase --onto <SHA_OF_COMMIT_B> <SHA_OF_COMMIT_D> HEAD
```

Remarquez que l'utilisation de la syntaxe ci-dessus ne déplacerait pas `main` pour pointer vers le nouveau commit, donc le résultat est un `HEAD` "détaché". Si vous utilisez `gg` ou un autre outil qui affiche l'historique accessible depuis les branches, cela pourrait vous induire en erreur :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-285.png)
_Rebasage avec `--onto` entraîne un `HEAD` détaché (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Mais si vous utilisez simplement `git log` (ou mon alias `git lol`), vous verrez l'historique souhaité :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-286.png)
_L'historique résultant (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Je ne sais pas pour vous, mais ces genres de choses me rendent vraiment heureux. 😊😊

Au fait, vous pourriez omettre `HEAD` de la commande précédente car c'est la valeur par défaut pour le troisième paramètre. Donc simplement utiliser :

```
git rebase --onto <SHA_OF_COMMIT_B> <SHA_OF_COMMIT_D>
```

Aurait le même effet. Le dernier paramètre indique en fait à Git où se termine la séquence actuelle de commits à rebaser. Donc la syntaxe de `git rebase --onto` avec trois arguments est :

```
git rebase --onto <new_parent> <old_parent> <until>
```

## Comment déplacer des commits entre les branches

Donc, disons que nous arrivons au même historique que précédemment :

```
git checkout original_commit_f
```

Et maintenant, je veux seulement "Commit E", pour qu'il soit sur une branche basée sur "Commit B". C'est-à-dire, je veux avoir une nouvelle branche, bifurquant de "Commit B", avec seulement "Commit E".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-287.png)
_L'historique actuel, en considérant "Commit E" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Alors, que signifie cela en termes de rebase ? Considérez l'image ci-dessus. Quel commit (ou commits) devrais-je rebaser, et quel commit serait la nouvelle base ?

Je sais que je peux compter sur vous ici 😊

Ce que je veux, c'est prendre "Commit E", et ce commit seulement, et changer sa base pour qu'elle soit "Commit B". En d'autres termes, _rejouer_ les changements introduits dans "Commit E" sur "Commit B".

Pouvez-vous appliquer cette logique à la syntaxe de `git rebase` ?

Le voici (cette fois j'écris `<COMMIT_B>` au lieu de `<SHA_OF_COMMIT_B>`, pour plus de concision) :

```
git rebase --onto <COMMIT_B> <COMMIT_D> <COMMIT_E>
```

Maintenant l'historique ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-288.png)
_L'historique après le rebase (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Génial !

# Une Note sur les Conflits

Notez que lors de l'exécution d'un rebase, vous pouvez rencontrer des conflits tout comme lors de la fusion. Vous pouvez avoir des conflits car lors du rebase, vous essayez d'appliquer des patches sur une base différente, peut-être où les patches ne s'appliquent pas.

Par exemple, considérons à nouveau le dépôt précédent, et spécifiquement, le changement introduit dans "Commit 12", pointé par `main` :

```
git show main
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-289.png)
_Le patch introduit dans "Commit 12" (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

J'ai déjà couvert le format de `git diff` en détail dans [un article précédent](https://www.freecodecamp.org/news/git-diff-and-patch/), mais pour un rappel rapide, ce commit indique à Git d'ajouter une ligne après les deux lignes de contexte :

```
```
This is a sample file
```

Et avant ces trois lignes de contexte :

```
```
def new_feature():
  print('new feature')
```

Disons que vous essayez de rebaser "Commit 12" sur un autre commit. Si, pour une raison quelconque, ces lignes de contexte n'existent pas telles qu'elles sont dans le patch sur le commit sur lequel vous rebaser _onto_, alors vous aurez un conflit. Pour en savoir plus sur les conflits et comment les résoudre, voir [ce guide](https://www.freecodecamp.org/news/the-definitive-guide-to-git-merge/).

# Zoom Arrière pour la Vue d'Ensemble

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-290.png)
_Comparaison de rebase et merge (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Au début de ce guide, j'ai commencé par mentionner la similitude entre `git merge` et `git rebase` : tous deux sont utilisés pour intégrer les changements introduits dans différents historiques. 

Mais, comme vous le savez maintenant, ils sont très différents dans leur fonctionnement. Alors que la fusion résulte en un historique divergent, le rebase résulte en un historique linéaire. Les conflits sont possibles dans les deux cas. Et il y a une autre colonne décrite dans le tableau ci-dessus qui nécessite une attention particulière.

Maintenant que vous savez ce qu'est "Git rebase", et comment utiliser le rebase interactif ou `rebase --onto`, comme je l'espère vous en conviendrez, `git rebase` est un outil super puissant. Pourtant, il a un énorme inconvénient par rapport à la fusion.

Git rebase modifie l'historique.

Cela signifie que vous ne devriez **pas** rebaser les commits qui existent en dehors de votre copie locale du dépôt, et sur lesquels d'autres personnes peuvent avoir basé leurs commits.

En d'autres termes, si les seuls commits en question sont ceux que vous avez créés localement – allez-y, utilisez rebase, faites-en ce que vous voulez.

Mais si les commits ont été poussés, cela peut entraîner un énorme problème – car quelqu'un d'autre peut dépendre de ces commits, que vous réécrivez ensuite, et alors vous et eux aurez différentes versions du dépôt. 

Cela est différent de `merge` qui, comme nous l'avons vu, ne modifie pas l'historique.

Par exemple, considérons le dernier cas où nous avons rebasé et obtenu cet historique :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-288.png)
_L'historique après le rebase (Source : [Brief](https://youtu.be/3VFsitGUB3s))_

Maintenant, supposons que j'ai déjà poussé cette branche vers le dépôt distant. Et après avoir poussé la branche, un autre développeur l'a tirée et a bifurqué à partir de "Commit C". L'autre développeur ne savait pas que pendant ce temps, je rebasais localement ma branche, et que je la pousserais à nouveau plus tard.

Cela entraîne une incohérence : l'autre développeur travaille à partir d'un commit qui n'est plus disponible sur ma copie du dépôt.

Je ne vais pas m'étendre sur ce que cela provoque exactement dans ce guide, car mon message principal est que vous devriez définitivement éviter de tels cas. Si vous êtes intéressé par ce qui se passerait réellement, je laisserai un lien vers une ressource utile ci-dessous. Pour l'instant, résumons ce que nous avons couvert.

# Récapitulatif

Dans ce tutoriel, vous avez appris `git rebase`, un outil super-puissant pour réécrire l'historique dans Git. Vous avez considéré quelques cas d'utilisation où `git rebase` peut être utile, et comment l'utiliser avec un, deux ou trois paramètres, avec et sans le commutateur `--onto`.

J'espère avoir réussi à vous convaincre que `git rebase` est puissant – mais aussi qu'il est assez simple une fois que vous avez compris l'essentiel. C'est un outil pour "copier-coller" des commits (ou, plus précisément, des patches). Et c'est un outil utile à avoir dans votre boîte à outils.

# Références supplémentaires

* [Liste de lecture YouTube sur les internes de Git – par Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7) (ma chaîne YouTube).
* [Article précédent d'Omer sur les internes de Git.](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/)
* [Tutoriel d'Omer sur Git UNDO - réécrire l'historique avec Git](https://medium.com/@Omer_Rosenbaum/git-undo-how-to-rewrite-git-history-with-confidence-d4452e2969c2).
* [Documentation Git sur le rebasage](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
* [Branchement et la puissance du rebase](https://jwiegley.github.io/git-from-the-bottom-up/1-Repository/7-branching-and-the-power-of-rebase.html)
* [Rebasage interactif](https://jwiegley.github.io/git-from-the-bottom-up/1-Repository/8-interactive-rebasing.html)
* [Git rebase --onto](https://womanonrails.com/git-rebase-onto)

# **À propos de l'Auteur**

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la [Chaîne YouTube Brief](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros).