---
title: Git Pull Force – Comment écraser les modifications locales avec Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T19:01:22.000Z'
originalURL: https://freecodecamp.org/news/git-pull-force-how-to-overwrite-local-changes-with-git
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99a5740569d1a4ca20f0.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: version control
  slug: version-control
seo_title: Git Pull Force – Comment écraser les modifications locales avec Git
seo_desc: 'By Piotr Gaczkowski

  When you learn to code, sooner or later you''ll also learn about Version Control
  Systems. And while there are many competing tools in this space, one of them is
  the de facto standard used by almost everyone in the industry. It''s so...'
---

Par Piotr Gaczkowski

Lorsque vous apprenez à coder, tôt ou tard vous apprendrez également les systèmes de contrôle de version. Et bien qu'il existe de nombreux outils concurrents dans ce domaine, l'un d'eux est le standard de facto utilisé par presque tout le monde dans l'industrie. Il est si populaire que des entreprises utilisent son nom dans leur marque. Nous parlons bien sûr de Git.

Bien que Git soit un outil puissant, sa puissance est bien cachée. Il y a quelques concepts essentiels que vous devez comprendre pour devenir vraiment compétent avec Git. La bonne nouvelle est que, une fois que vous les aurez appris, vous ne rencontrerez presque jamais de problèmes dont vous ne pourrez pas vous sortir.

# Le flux de travail typique

Dans un flux de travail Git typique, vous utiliserez un dépôt local, un dépôt distant et une ou plusieurs branches. Les dépôts stockent toutes les informations sur le projet, y compris son historique complet et toutes les branches. Une branche est essentiellement une collection de modifications menant d'un projet vide à l'état actuel.

Après avoir cloné un dépôt, vous travaillez sur votre copie locale et introduisez de nouvelles modifications. Jusqu'à ce que vous poussiez les modifications locales vers le dépôt distant, tout votre travail est disponible uniquement sur votre machine.

Lorsque vous terminez une tâche, il est temps de synchroniser avec le dépôt distant. Vous souhaitez tirer les modifications distantes pour suivre l'avancement du projet, et vous souhaitez pousser les modifications locales pour partager votre travail avec les autres.

# Modifications locales

Tout va bien lorsque vous et le reste de votre équipe travaillez sur des fichiers totalement séparés. Quoi qu'il arrive, vous ne vous marcherez pas sur les pieds.

Cependant, il arrive que vous et vos coéquipiers introduisiez simultanément des modifications au même endroit. Et c'est généralement là que les problèmes commencent.

Avez-vous déjà exécuté `git pull` pour voir l'erreur redoutée `error: Your local changes to the following files would be overwritten by merge:` ? Tôt ou tard, tout le monde rencontre ce problème.

Ce qui est plus déroutant ici, c'est que vous ne voulez pas fusionner quoi que ce soit, juste tirer, n'est-ce pas ? En fait, pull est un peu plus compliqué que vous ne le pensiez.

# Comment fonctionne exactement Git Pull ?

Pull n'est pas une seule opération. Il consiste à récupérer les données du serveur distant puis à fusionner les modifications avec le dépôt local. Ces deux opérations peuvent être effectuées manuellement si vous le souhaitez :

```bash
git fetch
git merge origin/$CURRENT_BRANCH
```

La partie `origin/$CURRENT_BRANCH` signifie que :

* Git fusionnera les modifications du dépôt distant nommé `origin` (celui que vous avez cloné)
* qui ont été ajoutées à la `$CURRENT_BRANCH`
* qui ne sont pas déjà présentes dans votre branche locale extraite

Puisque Git n'effectue des fusions que lorsqu'il n'y a pas de modifications non validées, chaque fois que vous exécutez `git pull` avec des modifications non validées pourrait vous causer des ennuis. Heureusement, il existe des moyens de sortir des ennuis en un seul morceau !

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-167.png)
_Photo par [Unsplash](https://unsplash.com/@sneakyelbow?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Sneaky Elbow</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

# Différentes approches

Lorsque vous avez des modifications locales non validées et que vous souhaitez toujours tirer une nouvelle version du serveur distant, votre cas d'utilisation tombe généralement dans l'un des scénarios suivants. Soit :

* vous ne vous souciez pas des modifications locales et souhaitez les écraser,
* vous vous souciez beaucoup des modifications et aimeriez les appliquer après les modifications distantes,
* vous souhaitez télécharger les modifications distantes mais ne pas les appliquer tout de suite

Chaque approche nécessite une solution différente.

### Vous ne vous souciez pas des modifications locales

Dans ce cas, vous souhaitez simplement abandonner toutes les modifications locales non validées. Peut-être avez-vous modifié un fichier pour expérimenter, mais vous n'avez plus besoin de la modification. Tout ce qui vous importe est d'être à jour avec l'amont.

Cela signifie que vous ajoutez une étape supplémentaire entre la récupération des modifications distantes et leur fusion. Cette étape réinitialisera la branche à son état non modifié, permettant ainsi à `git merge` de fonctionner.

```bash
git fetch
git reset --hard HEAD
git merge origin/$CURRENT_BRANCH
```

Si vous ne souhaitez pas taper le nom de la branche à chaque fois que vous exécutez cette commande, Git dispose d'un raccourci pratique pointant vers la branche amont : `@{u}`. Une branche amont est la branche dans le dépôt distant vers laquelle vous poussez et depuis laquelle vous récupérez.

Voici à quoi ressembleraient les commandes ci-dessus avec le raccourci :

```bash
git fetch
git reset --hard HEAD
git merge '@{u}'
```

Nous mettons le raccourci entre guillemets dans l'exemple pour empêcher le shell de l'interpréter.

### Vous vous souciez beaucoup des modifications locales

Lorsque vos modifications non validées sont importantes pour vous, il y a deux options. Vous pouvez les valider puis effectuer `git pull`, ou vous pouvez les mettre de côté.

Mettre de côté signifie mettre les modifications de côté pour un moment afin de les ramener plus tard. Pour être plus précis, `git stash` crée un commit qui n'est pas visible sur votre branche actuelle, mais qui est toujours accessible par Git.

Pour ramener les modifications enregistrées dans le dernier stash, vous utilisez la commande `git stash pop`. Après avoir appliqué avec succès les modifications mises de côté, cette commande supprime également le commit de stash car il n'est plus nécessaire.

Le flux de travail pourrait alors ressembler à ceci :

```bash
git fetch
git stash
git merge '@{u}'
git stash pop
```

Par défaut, les modifications du stash deviendront indexées. Si vous souhaitez les désindexer, utilisez la commande `git restore --staged` (si vous utilisez Git plus récent que 2.25.0).

### Vous souhaitez simplement télécharger les modifications distantes

Le dernier scénario est un peu différent des précédents. Supposons que vous êtes au milieu d'un refactoring très désordonné. Ni perdre les modifications ni les mettre de côté n'est une option. Pourtant, vous souhaitez toujours avoir les modifications distantes disponibles pour exécuter `git diff` contre elles.

Comme vous l'avez probablement compris, le téléchargement des modifications distantes ne nécessite pas du tout `git pull` ! `git fetch` suffit.

Une chose à noter est que, par défaut, `git fetch` ne vous apportera que les modifications de la branche actuelle. Pour obtenir toutes les modifications de toutes les branches, utilisez `git fetch --all`. Et si vous souhaitez nettoyer certaines des branches qui n'existent plus dans le dépôt distant, `git fetch --all --prune` fera le nettoyage !

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-166.png)
_Photo par [Unsplash](https://unsplash.com/@lenin33?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Lenin Estrada</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

# Un peu d'automatisation

Avez-vous entendu parler de Git Config ? C'est un fichier où Git stocke tous les paramètres configurés par l'utilisateur. Il réside dans votre répertoire personnel : soit sous `~/.gitconfig` soit sous `~/.config/git/config`. Vous pouvez l'éditer pour ajouter quelques alias personnalisés qui seront compris comme des commandes Git.

Par exemple, pour avoir un raccourci équivalent à `git diff --cached` (qui montre la différence entre la branche actuelle et les fichiers indexés), vous ajouteriez la section suivante :

```
[alias]
  dc = diff --cached
```

Après cela, vous pouvez exécuter `git dc` chaque fois que vous souhaitez examiner les modifications. En procédant ainsi, nous pouvons configurer quelques alias liés aux cas d'utilisation précédents.

```
[alias]
  pull_force = !"git fetch --all; git reset --hard HEAD; git merge @{u}"
  pf = pull_force
  pull_stash = !"git fetch --all; git stash; git merge @{u}; git stash pop"
```

De cette manière, l'exécution de `git pull_force` écrasera les modifications locales, tandis que `git pull_stash` les préservera.

# L'autre Git Pull Force

Les esprits curieux ont peut-être déjà découvert qu'il existe une chose appelée `git pull --force`. Cependant, c'est une bête très différente de ce qui est présenté dans cet article.

Cela peut sembler quelque chose qui nous aiderait à écraser les modifications locales. Au lieu de cela, il nous permet de récupérer les modifications d'une branche distante vers une branche locale différente. `git pull --force` ne modifie que le comportement de la partie récupération. Il est donc équivalent à `git fetch --force`.

Comme `git push`, `git fetch` nous permet de spécifier quelles branches locales et distantes nous voulons utiliser. `git fetch origin/feature-1:my-feature` signifiera que les modifications de la branche `feature-1` du dépôt distant se retrouveront visibles sur la branche locale `my-feature`. Lorsqu'une telle opération modifie l'historique existant, elle n'est pas autorisée par Git sans un paramètre `--force` explicite.

Tout comme `git push --force` permet d'écraser les branches distantes, `git fetch --force` (ou `git pull --force`) permet d'écraser les branches locales. Il est toujours utilisé avec les branches source et destination mentionnées en tant que paramètres. Une approche alternative pour écraser les modifications locales en utilisant `git --pull force` pourrait être `git pull --force "@{u}:HEAD"`.

# Conclusion

Le monde de Git est vaste. Cet article n'a couvert qu'une des facettes de la maintenance des dépôts : l'incorporation de modifications distantes dans un dépôt local. Même ce scénario quotidien nous a obligés à regarder un peu plus en profondeur les mécanismes internes de cet outil de contrôle de version.

Apprendre des cas d'utilisation réels vous aide à mieux comprendre comment Git fonctionne sous le capot. Cela, à son tour, vous donnera un sentiment de puissance chaque fois que vous vous mettrez dans le pétrin. Nous le faisons tous de temps en temps.