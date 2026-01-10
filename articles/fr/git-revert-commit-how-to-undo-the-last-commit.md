---
title: Conclusion
date: '2021-08-31T20:20:41.000Z'
author: Ilenia Magoni
authorURL: https://www.freecodecamp.org/news/author/uccellino95/
originalURL: https://freecodecamp.org/news/git-revert-commit-how-to-undo-the-last-commit
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-siegfried-poepperl-8778445--1-.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_desc: 'Say you''re working on your code in Git and something didn''t go as planned.
  So now you need to revert your last commit. How do you do it? Let''s find out!

  There are two possible ways to undo your last commit. We''ll look at both of them
  in this article....'
---


Supposons que vous travailliez sur votre code dans Git et que quelque chose ne se soit pas passé comme prévu. Vous devez maintenant annuler votre dernier commit. Comment faire ? Découvrons-le !

<!-- more -->

Il existe deux façons possibles d'annuler votre dernier commit. Nous allons examiner les deux dans cet article.

## La commande `revert`

La commande `revert` créera un commit qui annule les modifications du commit ciblé. Vous pouvez l'utiliser pour annuler le dernier commit comme ceci :

```
git revert <commit to revert>
```

Vous pouvez trouver le nom du commit que vous souhaitez annuler en utilisant `[git log](https://www.freecodecamp.org/news/git-log-command/)`. Le premier commit qui y est décrit est le dernier commit créé. Vous pouvez ensuite copier le nom alphanumérique à partir de là et l'utiliser dans la commande `revert`.

![Un diagramme montrant que la commande git revert crée un nouveau commit pour annuler les modifications précédentes.](https://www.freecodecamp.org/news/content/images/2021/08/image-117.png) _Dans cette image, chaque cercle représente un commit._

## La commande `reset`

Vous pouvez également utiliser la commande `reset` pour annuler votre dernier commit. Mais attention – elle modifiera l'historique des commits, vous devriez donc l'utiliser rarement. Elle déplacera le HEAD, la branche de travail, vers le commit indiqué, et supprimera tout ce qui suit :

```
git reset --soft HEAD~1
```

L'option `--soft` signifie que vous ne perdrez pas les modifications non commitées que vous pourriez avoir.

![Un diagramme montrant que git reset --soft modifiera votre historique de commits, mais conservera toutes les modifications non indexées que vous avez.](https://www.freecodecamp.org/news/content/images/2022/08/git-reset-soft.png) _Dans cette image, chaque cercle représente un commit._

Si vous souhaitez revenir au dernier commit et également supprimer toutes les modifications non indexées (unstaged), vous pouvez utiliser l'option `--hard` :

```
git reset --hard HEAD~1
```

Cela annulera le dernier commit, mais aussi toutes les modifications non commitées.

![Un diagramme montrant que git reset --hard modifiera votre historique de commits, mais supprimera également toutes les modifications non indexées que vous avez.](https://www.freecodecamp.org/news/content/images/2021/08/image-112.png) _Dans cette image, chaque cercle représente un commit._

## Devriez-vous utiliser `reset` ou `revert` dans Git ?

Vous ne devriez réellement utiliser `reset` que si le commit à réinitialiser n'existe que localement. Cette commande modifie l'historique des commits et pourrait écraser un historique dont dépendent les membres de l'équipe distante.

`revert` crée à la place un _nouveau commit_ qui annule les modifications. Ainsi, si le commit à annuler a déjà été poussé vers un dépôt partagé, il est préférable d'utiliser `revert` car il n'écrase pas l'historique des commits.

# Conclusion

Vous avez appris deux façons d'annuler le dernier commit ainsi que le moment idéal pour utiliser l'une plutôt que l'autre.

Désormais, si vous remarquez que votre dernier commit introduit un bug ou n'aurait pas dû être commité, vous savez comment corriger cela !