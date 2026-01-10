---
title: Comment utiliser les branches dans Git – le guide ultime
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-28T16:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-branches-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/header-image@2080x1090-1.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: version control
  slug: version-control
seo_title: Comment utiliser les branches dans Git – le guide ultime
seo_desc: 'By Tobias Günther

  Branches are one of the core concepts in Git. And there''s an endless amount of
  things you can do with them. You can create and delete them, rename and publish
  them, switch and compare them... and so much more.

  My intention with this...'
---

Par Tobias Günther

Les branches sont l'un des concepts fondamentaux de Git. Et il existe une infinité de choses que vous pouvez faire avec elles. Vous pouvez les créer et les supprimer, les renommer et les publier, basculer entre elles et les comparer... et bien plus encore.

Mon intention avec cet article est de créer un aperçu complet des choses que vous pouvez faire avec les branches dans Git. Je ne voulais pas produire un article de la longueur d'un livre, donc je ne vais pas entrer dans les détails pour toutes les actions. Mais je vais fournir des liens si vous souhaitez en savoir plus.

Voici un aperçu de ce que nous allons couvrir :

* Comment créer des branches
* Comment renommer des branches
* Comment basculer entre les branches
* Comment publier des branches
* Comment suivre des branches
* Comment supprimer des branches
* Comment fusionner des branches
* Comment rebaser des branches
* Comment comparer des branches

## Comment créer une branche dans Git

Avant de pouvoir travailler avec des branches, vous devez en avoir dans votre dépôt. Commençons donc par parler de la création de branches :

```git / cli
$ git branch <nom-nouvelle-branche>
```

Lorsque vous fournissez simplement un nom à la commande `git branch`, Git supposera que vous souhaitez démarrer votre nouvelle branche basée sur la révision actuellement extraite. Si vous souhaitez que votre nouvelle branche commence à une révision _spécifique_, vous pouvez simplement ajouter le hash SHA-1 de la révision :

```git / cli
$ git branch <nom-nouvelle-branche> 89a2faad
```

Il va sans dire que vous ne pouvez créer de nouvelles branches que dans votre dépôt local. La "création" de branches dans un dépôt distant se fait en publiant une branche locale _existante_ - ce dont nous parlerons plus tard.

## Comment renommer une branche dans Git

Faire une faute de frappe dans le nom d'une branche ou simplement changer d'avis après coup est trop facile. C'est pourquoi Git facilite le renommage d'une branche locale. Si vous souhaitez renommer votre branche HEAD actuelle, vous pouvez utiliser la commande suivante :

```git / cli
$ git branch -m <nouveau-nom>
```

Au cas où vous souhaiteriez renommer une autre branche locale (qui n'est PAS actuellement extraite), vous devrez fournir l'ancien _et_ le nouveau nom :

```git / cli
$ git branch -m <ancien-nom> <nouveau-nom>
```

Ces commandes, encore une fois, sont utilisées pour travailler avec des branches locales. Si vous souhaitez renommer une branche distante, les choses sont un peu plus compliquées - car Git ne vous permet pas de renommer des branches distantes.

En pratique, le renommage d'une branche distante peut être fait en supprimant l'ancienne et en poussant ensuite la nouvelle depuis votre dépôt local :

```git / cli
# Tout d'abord, supprimez la branche actuelle / ancienne :
$ git push origin --delete <ancien-nom>

# Ensuite, poussez simplement la nouvelle branche locale avec le nom correct :
$ git push -u origin <nouveau-nom>
```

Si vous utilisez un [client Git desktop comme Tower](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=working-with-branches-in-git), vous ne serez pas ennuyé avec ces détails : vous pouvez simplement renommer les branches locales et distantes à partir d'un menu contextuel (pas besoin de supprimer et de repousser quoi que ce soit) :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/tower_rename-branch.gif)

## Comment basculer entre les branches dans Git

La branche actuelle (également appelée branche HEAD) définit le contexte dans lequel vous travaillez actuellement. En d'autres termes : la branche HEAD actuelle est l'endroit où les nouveaux commits seront créés.

Cela dit, il est logique que le _changement_ de la branche actuellement active soit l'une des actions les plus utilisées que tout développeur effectue lorsqu'il travaille avec des branches.

Et puisque le changement de branches est également appelé "extraction" de branches, vous ne serez pas surpris d'apprendre la commande utilisée pour faire cela :

```git / cli
$ git checkout <autre-branche>
```

Cependant, parce que la commande `git checkout` a tant de devoirs différents, la communauté Git (assez récemment) a introduit une nouvelle commande que vous pouvez maintenant également utiliser pour changer la branche HEAD actuelle :

```git / cli
$ git switch <autre-branche>
```

Je pense qu'il est très logique de s'éloigner de la commande `checkout` - parce qu'elle est utilisée pour effectuer tant d'actions différentes - et de passer plutôt à la nouvelle commande `switch`, qui est absolument sans ambiguïté sur ce qu'elle fait.

## Comment publier une branche dans Git

Comme je l'ai déjà dit dans la section sur la "création de branches" ci-dessus, il n'est pas possible de _créer_ une nouvelle branche sur un dépôt distant.

Ce que nous pouvons faire, cependant, c'est _publier une branche locale existante_ sur un dépôt distant. Nous pouvons "télécharger" ce que nous avons localement vers le dépôt distant et ainsi le partager avec notre équipe :

```git / cli
$ git push -u origin <branche-locale>
```

La commande, dans l'ensemble, n'est probablement pas une grande surprise pour vous. Mais un paramètre, le drapeau `-u`, mérite d'être expliqué - ce que je ferai dans la section suivante.

Mais pour vous donner la version courte ici : il indique à Git d'établir une "connexion de suivi" qui rendra les opérations de poussée et de tirage beaucoup plus faciles à l'avenir.

## Comment suivre des branches dans Git

Par défaut, les branches locales et distantes n'ont rien à voir les unes avec les autres. Elles sont stockées et gérées comme des objets indépendants dans Git.

Mais dans la vie réelle, bien sûr, les branches locales et distantes ont souvent _une relation_ les unes avec les autres. Par exemple, une branche distante est souvent quelque chose comme le "homologue" d'une branche locale.

Une telle relation peut être modélisée dans Git : une branche (généralement une branche locale) peut "suivre" une autre (généralement une branche distante).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/tracking-ahead-behind.gif)

Une fois qu'une telle relation de suivi a été établie, plusieurs choses deviendront beaucoup plus faciles : notamment, lors de la poussée ou du tirage, vous pouvez simplement utiliser les commandes vanilla sans aucun paramètre supplémentaire (par exemple, un simple `git push`).

La connexion de suivi aide Git à remplir les blancs - quelle branche sur quel dépôt distant vous souhaitez pousser, par exemple.

Vous avez déjà lu une façon d'établir une telle connexion de suivi : utiliser `git push` avec l'option `-u` lors de la publication d'une branche locale pour la première fois fait exactement cela. Après cela, vous pouvez simplement utiliser `git push` sans mentionner le dépôt distant ou la branche cible.

Cela fonctionne également dans l'autre sens : lors de la création d'une branche locale qui doit être basée sur une branche distante. En d'autres termes, lorsque vous souhaitez _suivre_ une branche distante :

```git / cli
$ git branch --track <nouvelle-branche> origin/<branche-base>
```

Alternativement, vous pourriez également utiliser la commande `git checkout` pour y parvenir. Si vous souhaitez nommer la branche locale d'après la branche distante, vous n'avez qu'à spécifier le nom de la branche distante :

```git / cli
$ git checkout --track origin/<branche-base>
```

Si vous souhaitez en savoir plus sur ce sujet, consultez cet [article sur les "Relations de suivi dans Git"](https://www.git-tower.com/learn/git/faq/track-remote-upstream-branch/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=working-with-branches-in-git).

## Comment supprimer une branche dans Git

Toutes les branches ne sont pas destinées à vivre éternellement. En fait, la plupart des branches dans un dépôt seront de courte durée. Donc, si vous souhaitez faire un peu de ménage, voici comment supprimer une branche locale :

```git / cli
$ git branch -d <nom-branche>
```

Notez que vous pourriez également avoir besoin de l'option `-f` si vous essayez de supprimer une branche qui contient des changements non fusionnés. Utilisez cette option avec précaution car elle facilite la perte de données !

Pour supprimer une branche distante, nous ne pouvons pas utiliser la commande `git branch`. Au lieu de cela, `git push` fera l'affaire, en utilisant le drapeau `--delete` :

```git / cli
$ git push origin --delete <nom-branche>
```

Lors de la suppression d'une branche, gardez à l'esprit que vous devez vérifier si vous devez également supprimer sa branche homologue.

Par exemple, si vous venez de supprimer une branche de fonctionnalité distante, il peut être judicieux de supprimer également sa branche de suivi locale. De cette façon, vous vous assurez de ne pas être laissé avec beaucoup de branches obsolètes - et un dépôt Git désordonné.

## Comment fusionner des branches dans Git

La fusion est probablement le moyen le plus populaire d'intégrer des changements. Elle vous permet d'apporter tous les nouveaux commits d'une autre branche dans votre branche HEAD actuelle.

L'une des grandes choses à propos de Git est que la fusion de branches est si simple et sans stress. Elle nécessite seulement deux étapes :

```git / cli
# (1) Extrayez la branche qui doit recevoir les changements
$ git switch main
	
# (2) Exécutez la commande "merge" avec le nom de la branche qui contient les changements souhaités
$ git merge feature/formulaire-contact
```

Souvent, le résultat d'une fusion sera un nouveau commit séparé, le soi-disant "commit de fusion". C'est là que Git combine les changements entrants. Vous pouvez le considérer comme un nœud qui connecte deux branches.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/merge-commit.png)

Il y a, bien sûr, beaucoup plus à dire sur `git merge`. Voici quelques ressources gratuites qui vous aident à en savoir plus :

* [Comment annuler une fusion dans Git](https://www.git-tower.com/learn/git/faq/undo-git-merge/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=working-with-branches-in-git)
* [Comment corriger et résoudre les conflits de fusion](https://www.git-tower.com/learn/git/faq/solve-merge-conflicts/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=working-with-branches-in-git)
* [Un aperçu de "git merge"](https://www.git-tower.com/learn/git/commands/git-merge/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=working-with-branches-in-git)

## Comment rebaser des branches dans Git

Une alternative pour intégrer des commits d'une autre branche est d'utiliser `rebase`. Et je suis très prudent pour l'appeler une méthode "alternative" : ce n'est ni mieux ni pire, mais simplement différent.

Si et quand vous utilisez rebase dépend principalement de la préférence personnelle et des conventions de votre équipe. Certaines équipes adorent rebase, d'autres préfèrent merge.

Pour illustrer les différences entre merge et rebase, jetez un œil aux illustrations suivantes. En utilisant `git merge`, le résultat de notre intégration de _branch-B_ dans _branch-A_ ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/end-situation-merge-commit.gif)

En utilisant `git rebase`, en revanche, le résultat final sera assez différent - surtout parce qu'aucun commit de fusion séparé ne sera créé. En utilisant rebase, il semble que votre historique de développement se soit déroulé en ligne droite :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/end-situation-rebase.gif)

Démarrer le processus réel est assez simple :

```git / cli
# (1) Extrayez la branche qui doit recevoir les changements
$ git switch feature/formulaire-contact
	
# (2) Exécutez la commande "rebase" avec le nom de la branche qui contient les changements souhaités
$ git rebase main

```

Pour une compréhension plus approfondie de rebase, je recommande l'article ["Utiliser git rebase au lieu de git merge"](https://www.git-tower.com/learn/git/faq/rebase/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=working-with-branches-in-git).

## Comment comparer des branches dans Git

Dans certaines situations, il peut être très utile de comparer deux branches. Par exemple, avant de décider d'intégrer ou de supprimer une branche, il est intéressant de voir comment elle diffère d'une autre branche. Contient-elle de nouveaux commits ? Et si oui : sont-ils précieux ?

Pour voir quels commits sont dans branch-B mais pas dans branch-A, vous pouvez utiliser la commande `git log` avec la syntaxe à double point :

```git / cli
$ git log branch-A..branch-B
```

Bien sûr, vous pourriez également utiliser cela pour comparer vos états locaux et distants en écrivant quelque chose comme `git log main..origin/main`.

Si, au lieu des _commits_, vous préférez voir les _changements réels_ qui composent ces différences, vous pouvez utiliser la commande `git diff` :

```git / cli
$ git diff branch-A..branch-B
```

## Comment devenir plus productif avec Git

Travailler avec des branches dans Git a de nombreuses facettes ! Mais cela est vrai pour Git en général : il y a une tonne de fonctionnalités puissantes que de nombreux développeurs ne connaissent pas ou ne peuvent pas utiliser de manière productive.

De l'interactive rebase aux sous-modules et du reflog à l'historique des fichiers : il est payant d'apprendre ces fonctionnalités avancées - en devenant plus productif et en faisant moins d'erreurs.

Un sujet particulièrement utile est d'apprendre à **annuler les erreurs avec Git**. Si vous souhaitez approfondir comment vous pouvez sauver votre cou des erreurs inévitables, consultez [cette vidéo sur l'annulation des erreurs dans Git](https://www.freecodecamp.org/news/how-to-undo-mistakes-with-git/).

Amusez-vous à devenir un meilleur programmeur !

## À propos de l'auteur

[Tobias Günther](https://twitter.com/gntr) est le cofondateur de [Tower](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=working-with-branches-in-git), le populaire client Git desktop qui aide plus de 100 000 développeurs à travers le monde à être plus productifs avec Git.