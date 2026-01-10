---
title: Le guide ultime de Git Merge et Git Rebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-26T18:08:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-git-merge-and-git-rebase
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f05740569d1a4ca4068.jpg
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: version control
  slug: version-control
seo_title: Le guide ultime de Git Merge et Git Rebase
seo_desc: 'Welcome to our ultimate guide to the git merge and git rebase commands.
  This tutorial will teach you everything you need to know about combining multiple
  branches with Git.

  Git Merge

  The git merge command will merge any changes that were made to the ...'
---

Bienvenue dans notre guide ultime des commandes `git merge` et `git rebase`. Ce tutoriel vous apprendra tout ce que vous devez savoir sur la combinaison de plusieurs branches avec Git.

## Git Merge

La commande `git merge` fusionnera tous les changements apportés à la base de code sur une branche séparée vers votre branche actuelle en tant que nouveau commit.

La syntaxe de la commande est la suivante :

```shell
git merge NOM-DE-LA-BRANCHE
```

Par exemple, si vous travaillez actuellement dans une branche nommée `dev` et que vous souhaitez fusionner les nouveaux changements apportés dans une branche nommée `new-features`, vous exécuterez la commande suivante :

```shell
git merge new-features
```

**Note :** Si des changements non validés existent sur votre branche actuelle, Git ne vous permettra pas de fusionner tant que tous les changements dans votre branche actuelle n'auront pas été validés. Pour gérer ces changements, vous pouvez soit :

Créer une nouvelle branche et valider les changements

```shell
git checkout -b nouveau-nom-de-branche
git add .
git commit -m "<votre message de commit>"
```

Les mettre de côté

```shell
git stash               # les ajouter à la stash
git merge new-features  # effectuer votre fusion
git stash pop           # récupérer les changements dans votre arbre de travail
```

Abandonner tous les changements

```shell
git reset --hard        # supprime tous les changements en attente
```

## Git Rebase

Le rebase d'une branche dans Git est une manière de déplacer l'intégralité d'une branche vers un autre point de l'arbre. L'exemple le plus simple est de déplacer une branche plus haut dans l'arbre. Supposons que nous avons une branche qui a divergé de la branche master au point A :

```text
        /o-----o---o--o-----o--------- branche
--o-o--A--o---o---o---o----o--o-o-o--- master
```

Lorsque vous rebasez, vous pouvez la déplacer comme ceci :

```text
                                   /o-----o---o--o-----o------ branche
--o-o--A--o---o---o---o----o--o-o-o master
```

Pour rebasez, assurez-vous d'avoir tous les commits que vous souhaitez inclure dans le rebase dans votre branche master. Passez à la branche que vous souhaitez rebasez et tapez `git rebase master` (où master est la branche sur laquelle vous souhaitez rebasez).

Il est également possible de rebasez sur une branche différente, de sorte que, par exemple, une branche basée sur une autre branche (appelons-la feature) soit rebasez sur master :

```text
                            /---o-o branche
           /---o-o-o-o---o--o------ feature
----o--o-o-A----o---o--o-o-o--o--o- master
```

Après `git rebase master branch` ou `git rebase master` lorsque vous avez passé à la branche, vous obtiendrez :

```text
           /---o-o-o-o---o--o------ feature
----o--o-o-A----o---o--o-o-o--o--o- master
                                  \---o-o branche
```

### Git rebase interactif dans la console

Pour utiliser `git rebase` dans la console avec une liste de commits que vous pouvez choisir, modifier ou supprimer dans le rebase :

* Entrez `git rebase -i HEAD~5` avec le dernier nombre étant le nombre de commits à partir du plus récent vers l'arrière que vous souhaitez examiner.
* Dans vim, appuyez sur `esc`, puis `i` pour commencer à éditer le test.
* Sur le côté gauche, vous pouvez remplacer le `pick` par l'une des commandes ci-dessous. Si vous souhaitez fusionner un commit dans un précédent et supprimer le message de commit, entrez `f` à la place du `pick` du commit.
* Sauvegardez et quittez votre éditeur de texte.
* Lorsque le rebase est arrêté, faites les ajustements nécessaires, puis utilisez `git rebase --continue` jusqu'à ce que le rebase soit réussi.
* Si le rebase est réussi, vous devez forcer la poussée de vos changements avec `git push -f` pour ajouter la version rebasez à votre dépôt distant.
* En cas de conflit de fusion, il existe plusieurs façons de le résoudre. Une méthode consiste à ouvrir les fichiers dans un éditeur de texte et à supprimer les parties du code que vous ne souhaitez pas. Ensuite, utilisez `git add <nom-du-fichier>` suivi de `git rebase --continue`. Vous pouvez sauter le commit en conflit en entrant `git rebase --skip`, ou arrêter le rebase en exécutant `git rebase --abort` dans votre console.

```text
pick 452b159 <message pour ce commit>
pick 7fd4192 <message pour ce commit>
pick c1af3e5 <message pour ce commit>
pick 5f5e8d3 <message pour ce commit>
pick 5186a9f <message pour ce commit>

# Rebase 0617e63..5186a9f sur 0617e63 (30 commandes)
#
# Commandes :
# p, pick = utiliser le commit
# r, reword = utiliser le commit, mais s'arrêter pour éditer le message de commit.
# e, edit = utiliser le commit, mais s'arrêter pour modifier ou ajouter un commit.
# s, squash = utiliser le commit, fusionner dans le commit précédent et s'arrêter pour éditer le message de commit.
# f, fixup = comme "squash", mais supprimer le message de log de ce commit et donc ne pas s'arrêter.
# x, exec = exécuter la commande (le reste de la ligne) en utilisant le shell
# d, drop = supprimer le commit
#
# Ces lignes peuvent être réorganisées ; elles sont exécutées de haut en bas.
#
# Si vous supprimez une ligne ici, CE COMMIT SERA PERDU.
#
# Cependant, si vous supprimez tout, le rebase sera annulé.
#
# Notez que les commits vides sont commentés
```

## Conflits de fusion

Un conflit de fusion se produit lorsque vous effectuez des commits sur des branches séparées qui modifient la même ligne de manière conflictuelle. Si cela se produit, Git ne saura pas quelle version du fichier conserver et affichera un message d'erreur similaire à ce qui suit :

```shell
CONFLICT (content): Merge conflict in résumé.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Si vous regardez le fichier `résumé.txt` dans votre éditeur de code, vous pouvez voir où le conflit a eu lieu :

```shell
<<<<<<< HEAD
Address: 808 South Street
=======
Address: 505 North Street
>>>>>>> updated_address
```

Git a ajouté quelques lignes supplémentaires au fichier :

* `<<<<<<< HEAD`
* `=======`
* `>>>>>>> updated_address`

Considérez `=======` comme la ligne de division du conflit. Tout ce qui se trouve entre `<<<<<<< HEAD` et `=======` est le contenu de la branche actuelle vers laquelle le ref HEAD pointe. D'autre part, tout ce qui se trouve entre `=======` et `>>>>>>> updated_address` est le contenu de la branche en cours de fusion, `updated_address`.

## Git Merge vs Git Rebase

Les commandes `git merge` et `git rebase` sont très utiles, et l'une n'est pas meilleure que l'autre. Cependant, il existe des différences très importantes entre les deux commandes que vous et votre équipe devez prendre en considération.

Chaque fois que `git merge` est exécuté, un commit de fusion supplémentaire est créé. Chaque fois que vous travaillez dans votre dépôt local, avoir trop de commits de fusion peut rendre l'historique des commits confus. Une façon d'éviter le commit de fusion est d'utiliser `git rebase` à la place.

`git rebase` est une fonctionnalité très puissante. Cela dit, elle est également **risquée** si elle n'est pas utilisée de la bonne manière. `git rebase` modifie l'historique des commits, alors utilisez-la avec précaution. Si le rebase est effectué dans le dépôt distant, cela peut créer beaucoup de problèmes lorsque d'autres développeurs essaient de tirer les derniers changements de code du dépôt distant. N'oubliez pas de n'exécuter `git rebase` que dans un dépôt local.

C'est tout ce que vous devez savoir pour fusionner et rebasez avec les meilleurs.