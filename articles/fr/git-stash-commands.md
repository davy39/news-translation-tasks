---
title: Comment utiliser la commande Git Stash
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-11T15:05:10.000Z'
originalURL: https://freecodecamp.org/news/git-stash-commands
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/stahs-1.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment utiliser la commande Git Stash
seo_desc: 'By Preethi⚡

  Let''s say you''re working on a serious feature of a branch in Git – like revamping
  the hero section of your marketing page. You''ll want to start doing experiments
  in your Revamp/Marketing-page-hero-section branch without screwing up master...'
---

Par Preethi⚡

Imaginons que vous travaillez sur une fonctionnalité importante d'une branche dans Git – comme la refonte de la section héroïque de votre page marketing. Vous allez vouloir commencer à faire des expériences dans votre branche `Refonte/Section-héroïque-page-marketing` sans tout casser dans la branche `master` ou `main`.

Puis soudain, vous recevez un appel de votre collègue pour corriger des bugs sur la branche `page-de-connexion`. C'est un problème sérieux. Vous essayez donc de basculer vers la branche `page-de-connexion` en utilisant `git switch page-de-connexion` ou `git checkout page-de-connexion`.

Si vous changez de branche avec des modifications indexées et non indexées, vous pourriez rencontrer l'un des scénarios suivants :

Premièrement, lors du passage à la branche `page-de-connexion`, les modifications indexées et non indexées de la branche `Refonte/Section-héroïque-page-marketing` vous suivront vers la branche `page-de-connexion`.

La branche `Refonte/Section-héroïque-page-marketing` contient certaines modifications indexées et non indexées sur `index.html`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/stash-1.png)

Si nous basculons vers la branche `page-de-connexion`, les modifications indexées et non indexées de la branche `Refonte/Section-héroïque-page-marketing` viennent également dans `page-de-connexion`.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/stash-1-1.png)

Cela salit la branche `page-de-connexion`.

Ensuite, parfois Git ne vous permet pas de changer de branche sans valider ces modifications. Cela est dû au fait que vous pourriez perdre les modifications apportées dans votre branche actuelle ou qu'elles pourraient entrer en conflit avec la branche de destination (`page-de-connexion`). Quelle que soit la raison, nous ne pouvons pas changer de branche sans valider ou masquer les modifications.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/error.png)

En même temps, vous ne pouvez pas valider la branche de fonctionnalité à moitié terminée.

Pour vous aider, vous pouvez utiliser **Git stashing**. Stash signifie stocker (les modifications) en toute sécurité dans un endroit caché (la pile de stash).

Masquer les modifications indexées ou non indexées du répertoire de travail actuel ou les fichiers non suivis, puis les stocker dans la pile de stash, revient le répertoire de travail actuel au dernier commit.

C'est une bonne nouvelle, n'est-ce pas ? Mettons les mains dans le cambouis avec les commandes de stash.

## **Table des matières**

* [Comment masquer vos modifications 🧐](#heading-comment-masquer-vos-modifications)
* [Comment masquer les fichiers non suivis❓](#heading-comment-masquer-les-fichiers-non-suivis)
* [Comment lister les stashes 📃](#heading-comment-lister-les-stashes)
* [Comprendre le format du stash](#heading-comprendre-le-format-du-stash)
* [Comment afficher le dernier stash 📺](#heading-comment-afficher-le-dernier-stash)
* [Comment afficher un stash individuel 📺](#heading-comment-afficher-un-stash-individuel)
* [Comment appliquer le stash 💥](#heading-comment-appliquer-le-stash)
* [Comment supprimer un stash ☠️](#heading-comment-supprimer-un-stash)
* [Comment créer une branche à partir d'un stash](#heading-comment-creer-une-branche-a-partir-dun-stash)

## Comment masquer vos modifications 🧐

Vous pouvez utiliser l'une des commandes suivantes pour **masquer vos modifications indexées et non indexées dans la pile de stash**. Cela annule les choses jusqu'au dernier commit et ne supprime pas les modifications, qui sont stockées dans la pile de stash.

```
git stash
```

ou

```
git stash save
```

## Comment masquer les fichiers non suivis❓

Vous voulez masquer vos fichiers non suivis dans la pile de stash ? Utilisez simplement le drapeau `--include-untracked` à la fin de la commande.

```
git stash --include-untracked
```

ou utilisez `-u` à la fin de la commande :

```
git stash -u
```

## Comment lister les stashes 📃

Utilisez la commande suivante pour lister tous les stashes stockés dans la pile de stash :

```
git stash list
```

Lister les stashes comme ci-dessous,

![Image](https://www.freecodecamp.org/news/content/images/2022/04/list-1.png)

* Les derniers stashes (stash@{0}) seront en haut de la pile.
* Les anciens stashes (stash@{1}) seront en bas de la pile.

## Comprendre le format du stash

La commande stash liste les stashes dans le format suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/stash-list.jpg)
_Un seul format de stash_

Si vous n'êtes pas tout à fait sûr de ce que cela signifie 😅, ce n'est pas grave. Explorons certains des termes de la liste de stash :

* **`Stash@{0}`** – ceci est simplement une référence de stash. Elle fait référence au stash particulier. Par défaut, `Stash@{0}` est toujours le dernier stash.

*Note : Les stashes numérotés plus haut comme stash@{3} sont des stashes plus anciens. Les derniers stashes ont toujours le numéro le plus bas.*

* **`WIP On fake`** – *fake* est simplement un nom de branche comme toute autre branche et WIP signifie Work In Progress. "_WIP on fake_" signifie que `stash@{0}` a été créé sur la branche "fake".
* **`fc99b30 add head line`** – *fc99b30* est un hash de commit et *add head line* est un message de commit. Au moment de la création du stash, *fc99b30 add head line* est le dernier commit.

## Comment afficher le dernier stash 📺

Peut-être avez-vous plusieurs stashes dans votre pile de stash et vous ne pouvez pas dire quelle référence de stash contient quelles modifications.

Ainsi, avant d'appliquer des stashes sur la branche de travail actuelle, vous pouvez confirmer et afficher les modifications enregistrées dans le stash avec la commande suivante :

```
git stash show
```

Par défaut, `git stash show` affiche les modifications enregistrées dans le **dernier** stash (stash@{0}) au format `--stat`.

Le format `--stat` montre uniquement combien de lignes vous avez ajoutées et supprimées dans chacun des fichiers modifiés.

```
readme.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Si vous voulez afficher les modifications enregistrées du dernier stash en **vue patch**, utilisez le drapeau `-p` à la fin de la commande, comme ceci :

```
git stash show -p
```

Si vous voulez également afficher les **fichiers non suivis**, utilisez le drapeau `-u`.

```
git stash show -u

```

ou vous pouvez utiliser le drapeau `--include-untracked` comme ceci :

```
git stash show --include-untracked
```

Vous pouvez afficher les fichiers non suivis avec le **format patch** :

```
git stash show -p -u
```

Vous pouvez également afficher **uniquement** les fichiers non suivis avec le format patch comme ceci :

```
git stash show -p --only-untracked
```

Wow, vous avez déjà appris 10+ commandes de stash 🎉🎉

Regardons quelques autres pour que vous puissiez tirer le meilleur parti du stash.

## Comment afficher un stash individuel 📺

Vous pouvez afficher les modifications enregistrées d'un stash individuel en utilisant la **référence de stash**.

```
git stash show stash@{1}

```

Pour le format patch, vous avez deviné juste 👏🏽👏🏽 – utilisez le drapeau `-p`.

```
git stash show stash@{1} -p

```

Vous voulez afficher un stash avec des fichiers non suivis ? Utilisez cette commande :

```
git stash show stash@{1} -u

```

ou celle-ci :

```
git stash show stash@{1} --include-untracked

```

Alors que vous pouvez faire ceci pour afficher uniquement les fichiers non suivis :

```
git stash show stash@{1} --only-untracked
```

## Comment appliquer le stash 💥

Pour appliquer les modifications enregistrées de votre dernier stash sur la branche de travail actuelle ainsi que supprimer ce stash de la pile de stash, exécutez cette commande :

```
git stash pop

```

*Note : Nous pouvons appliquer des stashes sur n'importe quelle branche. Ce n'est pas spécifique à la branche où le stash a été créé.*

Vous pouvez également appliquer le dernier stash sans supprimer le stash de la pile de stash comme ceci :

```
git stash apply

```

Vous pouvez appliquer un stash précédent en utilisant la référence de stash :

```
git stash apply stash@{3}
```

## Comment supprimer un stash ☠️

Vous voulez effacer tous les stashes de la pile de stash ? Utilisez cette commande :

```
git stash clear

```

Vous voulez supprimer un stash particulier ? Oui ! vous avez raison – vous utilisez la référence de stash :

```
git stash drop stash@{2}
```

## Comment créer une branche à partir d'un stash

![Image](https://www.freecodecamp.org/news/content/images/2022/03/branch-stash.png)

Oui, vous pouvez créer une nouvelle branche à partir de votre dernier stash. Utilisez simplement cette commande :

```
git stash branch <nom_de_la_branche>

```

Par exemple,

```
git stash branch demo

```

Si vous voulez créer une branche à partir d'un stash précédent, c'est également possible en utilisant la référence de stash :

```
git stash branch <nom_de_la_branche> stash@{révision}
```

Par exemple,

```
git stash branch purple stash@{3}
```

## Conclusion

Un si long voyage – mais il y avait beaucoup à couvrir. Si vous ne pouvez pas vous souvenir de chaque commande, ce n'est pas grave. Plus vous utilisez souvent ces commandes, plus vous vous en souviendrez facilement. Vous pouvez vous référer à mon [**guide de référence rapide des commandes git stash**](https://gist.github.com/Preethi-Dev/fa8ae46a75761356dc1fa711376c8345) pour une référence rapide.

J'espère qu'aujourd'hui vous avez saisi de nombreuses nouvelles choses sur git stash. Il est temps de se détendre et de prendre un café ou un thé ☕. Faites-moi savoir si vous avez des questions !