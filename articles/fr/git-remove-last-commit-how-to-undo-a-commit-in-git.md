---
title: Supprimer le dernier commit Git – Comment annuler un commit dans Git
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-09-21T17:42:10.000Z'
originalURL: https://freecodecamp.org/news/git-remove-last-commit-how-to-undo-a-commit-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-andrew-neel-2312369.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Supprimer le dernier commit Git – Comment annuler un commit dans Git
seo_desc: 'Git is a powerful tool and the most popular version control system. It
  is how developers and technical teams collaborate and work together on projects.

  But what happens when you accidentally commit a file and realize that you shouldn''t
  have done that...'
---

Git est un outil puissant et le système de contrôle de version le plus populaire. C'est ainsi que les développeurs et les équipes techniques collaborent et travaillent ensemble sur des projets.

Mais que se passe-t-il lorsque vous commitez accidentellement un fichier et réalisez que vous n'auriez pas dû le faire parce que ce fichier contient une erreur ?

Il n'y a pas lieu de s'inquiéter car Git vous permet d'annuler vos erreurs et de revenir à une version antérieure de votre projet.

L'une des fonctionnalités les plus utiles de Git est la capacité d'annuler les modifications que vous apportez à un projet au fil du temps.

Dans cet article, vous apprendrez comment annuler des modifications dans Git en fonction de l'état de votre dépôt Git.

Voici ce que nous allons aborder :

1. [Comment annuler les modifications locales non indexées (unstaged)](#non-indexees)
2. [Comment annuler les modifications locales indexées (staged)](#indexees)
3. [Comment annuler les modifications locales commitées](#commitees-locales)
4. [Comment annuler les modifications publiques commitées](#commitees-publiques)

## Comment annuler les modifications locales non indexées dans Git <a name="non-indexees"></a>

Supposons que vous travailliez sur votre machine locale. Vous avez effectué et enregistré des modifications dans un fichier localement, mais vous souhaitez les ignorer.

Lorsque vous n'avez pas encore indexé ces modifications, vous n'avez pas utilisé la commande `git add`.

Dans ce cas, vous devez utiliser la commande `git restore`.

Plus précisément, la commande `git restore` ressemblera à ceci :

```git
git restore nom_du_fichier
```

Disons, par exemple, que vous avez un fichier `README.md` et que vous avez accidentellement écrit et enregistré du texte que vous voulez supprimer.

Vous pouvez d'abord utiliser la commande `git status` pour voir l'état de votre dépôt Git.

Cette commande confirmera que le fichier n'est pas indexé (ce qui signifie que vous n'avez pas encore utilisé `git add`), et vous permettra de voir les fichiers que vous pourriez vouloir annuler :

```git
# Sur la branche main
# Votre branche est à jour avec 'origin/main'.
#
# Modifications qui ne sont pas indexées pour le commit :
#   (utilisez "git add <fichier>..." pour mettre à jour ce qui sera commité)
#   (utilisez "git restore <fichier>..." pour abandonner les modifications dans le répertoire de travail)
#	modifié :   README.md
#
# aucune modification ajoutée au commit (utilisez "git add" et/ou "git commit -a")
```

Voici comment vous annuleriez les modifications dans le fichier `README.md` :

```git
git restore README.md
```

Vous pouvez ensuite utiliser à nouveau `git status` pour vérifier l'état du dépôt :

```git
# Sur la branche main
# Votre branche est à jour avec 'origin/main'.
#
# rien à commiter, la copie de travail est propre
```

Maintenant, vous avez réussi à abandonner vos modifications les plus récentes et à revenir à la dernière version commitée de votre projet.

## Comment annuler les modifications locales indexées dans Git <a name="indexees"></a>

Un fichier est indexé (staged) lorsque vous avez utilisé la commande `git add`.

Supposons donc que vous ayez apporté des modifications au fichier `README.md` localement, que vous ayez utilisé la commande `git add` pour indexer les modifications, puis que vous réalisiez que le texte contient des erreurs.

Tout d'abord, lancez `git status` pour vous assurer que vous avez indexé le fichier (ce qui signifie que vous avez utilisé `git add`) :

```git
# Sur la branche main
# Votre branche est à jour avec 'origin/main'.
#
# Modifications qui seront commitées :
#   (utilisez "git restore --staged <fichier>..." pour désindexer)
#	modifié :   README.md
```

Comme vous pouvez le voir par la sortie de `git status`, vous pouvez utiliser la commande suivante pour annuler vos modifications :

```git
git restore --staged nom_du_fichier
```

Cette commande désindexera le fichier indexé, mais conservera vos modifications.

Lançons à nouveau `git status` :

```git
# Sur la branche main
# Votre branche est à jour avec 'origin/main'.
#
# Modifications qui ne sont pas indexées pour le commit :
#   (utilisez "git add <fichier>..." pour mettre à jour ce qui sera commité)
#   (utilisez "git restore <fichier>..." pour abandonner les modifications dans le répertoire de travail)
#	modifié :   README.md
#
# aucune modification ajoutée au commit (utilisez "git add" et/ou "git commit -a")
```

Maintenant, pour abandonner les modifications que vous avez apportées et restaurer le contenu original du fichier, utilisez :

```git
git restore README.md 
```

Et lançons `git status` une dernière fois :

```git
# Sur la branche main
# Votre branche est à jour avec 'origin/main'.
#
# rien à commiter, la copie de travail est propre
```

Désormais, les modifications que vous avez apportées ont disparu et le fichier est revenu à la version commitée actuelle.

## Comment annuler les modifications locales commitées dans Git <a name="commitees-locales"></a>

Supposons que vous ayez apporté des modifications à un fichier, que vous l'ayez indexé avec la commande `git add`, et que vous l'ayez commité avec la commande `git commit`.

Cela signifie que le Commit n'existe que localement et n'a pas encore été poussé (push) vers un dépôt distant.

Tout d'abord, utilisez `git status` pour vérifier que vous avez commité le fichier :

```git
# Sur la branche main
# Votre branche est en avance sur 'origin/main' de 1 commit.
#   (utilisez "git push" pour publier vos commits locaux)
#
# rien à commiter, la copie de travail est propre
```

Ensuite, si vous voulez annuler votre dernier Commit local, utilisez la commande `git log` :

Le dernier Commit aura un hash de commit (une longue série de chiffres et de caractères) et un `(HEAD -> main)` à la fin – c'est le Commit que vous cherchez à annuler.

Le deuxième Commit en partant de la fin a un hash de commit et un `(origin/main)` à la fin – c'est le Commit que vous voulez garder et celui que vous avez poussé vers le dépôt distant.

Après cela, utilisez la commande suivante pour annuler le Commit :

```git
git reset --soft HEAD~
```

Maintenant, utilisons à nouveau `git log`.

Vous devriez voir le hash du commit, et un `(HEAD -> main, origin/main)` à la fin.

Le dernier Commit que vous avez fait ne fait plus partie de l'historique du dépôt et a été supprimé.

La commande ci-dessus a tout restauré à la version du fichier antérieure à ce Commit accidentel ou erroné et est revenue en arrière d'un Commit.

Vérifions à nouveau `git status` :

```git
# Sur la branche main
# Votre branche est à jour avec 'origin/main'.
#
# Modifications qui seront commitées :
#   (utilisez "git restore --staged <fichier>..." pour désindexer)
#	modifié :   README.md
```

Gardez à l'esprit que bien que la commande `git reset --soft HEAD~` ait annulé votre dernier Commit, elle a conservé les modifications que vous avez apportées.

## Comment annuler les modifications publiques commitées dans Git <a name="commitees-publiques"></a>

Que se passe-t-il si vous avez apporté des modifications à un fichier, que vous l'avez indexé avec `git add`, commité avec `git commit`, et poussé vers un dépôt distant avec `git push` – mais que vous réalisez ensuite que vous n'auriez pas dû commiter ce fichier en premier lieu ?

Que faites-vous alors ?

Tout d'abord, utilisez `git status` pour vérifier l'état du dépôt Git :

```git
# Sur la branche main
# Votre branche est à jour avec 'origin/main'.
#
# rien à commiter, la copie de travail est propre
```

Dans la section ci-dessus, vous avez vu que chaque Commit possède un hash de commit, qui est une longue série de chiffres et de caractères.

Pour voir la version courte du hash de commit, utilisez la commande suivante :

```git
git log --oneline
```

Avec la commande `git log`, vous pouvez également vérifier quel Commit vous souhaitez annuler.

Disons que votre dernier Commit a un hash de commit `cc3bbf7`, suivi de `(HEAD -> main, origin/main)`, et un message de commit tel que "commit README.md file".

Pour annuler ce Commit spécifique, utilisez la commande suivante :

```git
git revert cc3bbf7 --no-edit
```

La commande ci-dessus annulera les modifications en créant un nouveau Commit et en remettant ce fichier dans son état précédent, comme s'il n'avait jamais changé.

Enfin, utilisez `git push` pour pousser la modification vers la branche distante.

Une fois cela fait, vous verrez que le message de commit sera le même que le précédent mais précédé du mot `revert`, comme 
'Revert "commit README.md file"'.

Gardez à l'esprit que l'historique des commits affichera les deux commits séparément :

```git
Revert "commit README.md file"
@john-doe
john-doe a commité il y a 9 minutes

commit README.md file
@john-doe
john-doe a commité il y a 16 minutes 
```

## Conclusion

Et voilà – vous savez maintenant comment annuler des modifications dans Git.

Pour en savoir plus sur Git, consultez les ressources gratuites suivantes :

- [Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)
- [Git for Professionals Tutorial - Tools & Concepts for Mastering Version Control with Git](https://www.youtube.com/watch?v=Uszj_k0DGsg)
- [Advanced Git Tutorial - Interactive Rebase, Cherry-Picking, Reflog, Submodules and more](https://www.youtube.com/watch?v=qsTthZi23VE)

Merci de votre lecture et bon codage ! ✨