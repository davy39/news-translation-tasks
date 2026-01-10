---
title: 'Secrets Git : 7 commandes que vous ne connaissez peut-être pas'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-21T17:56:21.000Z'
originalURL: https://freecodecamp.org/news/7-git-commands-you-might-not-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/header-image@1000x420.sketch.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: version control
  slug: version-control
seo_title: 'Secrets Git : 7 commandes que vous ne connaissez peut-être pas'
seo_desc: "By Tobias Günther\nOver the last couple years, Git has become a default\
  \ part of almost every developer's knowledge stack. But even though Git is so well-known,\
  \ there are many Git commands that are not. \nIn this short post, I'd like to show\
  \ you seven l..."
---

Par Tobias Günther

Au cours des dernières années, Git est devenu une partie par défaut de la stack de connaissances de presque tous les développeurs. Mais même si Git est si bien connu, il existe de nombreuses commandes Git qui ne le sont pas.

Dans ce court article, je souhaite vous montrer sept petites commandes qui peuvent vous aider à devenir plus productif et plus à l'aise avec Git. Plongeons-nous dans le sujet.

## Découvrir ce qui a changé dans un fichier

Rester à jour peut être difficile – surtout si de nombreuses personnes travaillent sur la même base de code.

Pour vous aider à comprendre exactement comment (ainsi que quand et par qui) un fichier a été modifié, vous pouvez utiliser la bonne vieille commande `git log` – mais avec une petite touche :

```cli
$ git log --since="3 weeks" -p index.html

```

L'utilisation de "-p" garantit que vous voyez les changements réels sous forme de diffs (et pas seulement les métadonnées du commit). Et l'option "--since" vous aide à vous concentrer sur une période récente.

## Annuler votre dernier commit avec style

Parfois, nous pensons qu'un ensemble de changements est prêt à être commit – mais juste après avoir fait le commit, nous nous rendons compte que nous avons été trop rapides.

Des changements pourraient manquer, nous aurions pu nous tromper de branche, ou une multitude d'autres problèmes pourraient survenir...

La seule chose qui est certaine : nous aimerions annuler ce dernier commit et récupérer nos changements dans notre Copie de Travail !

Nous pouvons utiliser la commande `git reset` avec un ensemble spécial d'options :

```cli
$ git reset --mixed HEAD~1

```

L'option "--mixed" garantit que les changements contenus dans les commits étant réinitialisés ne sont PAS supprimés. Au lieu de cela, ils sont conservés en tant que changements locaux dans la Copie de Travail.

L'utilisation de la notation "HEAD~1" est un excellent raccourci pour spécifier "le commit avant le dernier" – ce qui est exactement ce que nous voulons pour annuler le tout dernier commit.

N'hésitez pas à lire plus sur ce sujet dans [comment annuler le dernier commit](https://www.git-tower.com/learn/git/faq/undo-last-commit?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands).

## Découvrir comment un fichier est différent dans une autre branche

Après avoir apporté des modifications à un fichier dans une branche de fonctionnalité, vous pourriez vouloir le comparer à son apparence sur une autre branche. Pour prendre un exemple concret, disons...

* vous êtes actuellement sur la branche "feature/login" et...
* vous voulez comprendre comment le fichier "myFile.txt" ici...
* est différent de sa version sur la branche "develop".

La commande `git diff` peut faire cela si vous fournissez les paramètres suivants :

```cli
$ git diff develop -- myFile.txt

```

Vous verrez alors un diff clair et net qui montre comment votre fichier diffère de sa version sur l'autre branche.

## Utiliser "switch" au lieu de "checkout"

La commande `git checkout` a une multitude de tâches et de significations différentes. C'est pourquoi, assez récemment, la communauté Git a décidé de publier une nouvelle commande : `git switch`. Comme son nom l'indique, elle a été conçue spécifiquement pour la tâche de changer de branches :

```cli
$ git switch develop

```

Comme vous pouvez le voir, son utilisation est très simple et similaire à "git checkout". Mais l'énorme avantage par rapport à la commande "checkout" est que "switch" n'a pas un million d'autres significations et capacités.

Comme il s'agit d'un membre assez nouveau de la famille des commandes Git, vous devriez vérifier si votre installation Git l'inclut déjà.

## Basculer entre deux branches

Dans certains scénarios, il peut être nécessaire pour vous de basculer plusieurs fois entre deux branches. Au lieu d'écrire toujours les noms des branches en entier, vous pouvez simplement utiliser le raccourci suivant :

```cli
$ git switch -

```

En utilisant le caractère tiret comme seul paramètre, la commande "git switch" basculera vers la branche active précédemment. Comme mentionné, cela peut être très pratique si vous devez basculer plusieurs fois entre deux branches.

## Utiliser "git restore" pour annuler les changements locaux

Jusqu'à récemment, vous deviez utiliser une forme de `git checkout` ou `git reset` lorsque vous vouliez annuler des changements locaux.

Mais avec la commande (relativement nouvelle) `git restore`, nous avons maintenant une commande qui a été conçue exactement à cet effet. Cela la distingue de "checkout" et "reset", car ces commandes ont de nombreux autres cas d'utilisation.

Voici un aperçu rapide des choses les plus importantes que vous pouvez faire avec "git restore" :

```cli
# Désindexer un fichier, mais laisser ses changements réels intacts
$ git restore --staged myFile.txt

# Supprimer vos changements locaux dans un certain fichier
$ git restore myFile.txt

# Annuler tous les changements locaux dans la copie de travail (soyez prudent)
$ git restore .

```

## Restaurer une version historique d'un fichier

La commande `git restore` offre une autre option très utile appelée "--source". Avec l'aide de cette option, vous pouvez facilement restaurer n'importe quelle version précédente d'un fichier spécifique :

```cli
$ git restore --source 6bcf266b index.html

```

Vous mentionnez simplement le hash de révision de la version que vous souhaitez restaurer (et le nom du fichier, bien sûr).

Si vous avez besoin d'aide pour trouver la bonne révision, vous pouvez utiliser un [client Git de bureau comme Tower](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands) : avec une fonctionnalité comme son "Historique de fichier", vous pouvez facilement inspecter uniquement les changements qui se sont produits dans un certain fichier – et ensuite sélectionner une révision à restaurer.

## Découvrir la puissance de Git

Bien que Git soit si bien connu de nos jours, une grande partie de sa puissance reste encore inconnue du public. Il est vrai que vous pouvez "survivre" avec seulement une poignée de commandes comme commit, push et pull. Mais c'est comme conduire une Ferrari uniquement en première vitesse !

Si vous êtes prêt à plonger un peu plus profond, vous découvrirez certaines des fonctionnalités les plus puissantes de Git. Et celles-ci ont le potentiel non seulement de vous rendre plus productif, mais aussi – en fin de compte – un meilleur développeur !

Si vous voulez en savoir plus sur Git, je vous recommande de consulter les ressources gratuites suivantes :

* [The First Aid Kit for Git](https://www.git-tower.com/learn/git/first-aid-kit/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands) : Apprenez à annuler et à récupérer des erreurs dans Git avec une série de vidéos très courtes et simples.
* [The Git Cheat Sheet](https://www.git-tower.com/learn/cheat-sheets/git/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands) : Une feuille de triche populaire pour toujours avoir les commandes les plus importantes à portée de main.

## À propos de l'auteur

[Tobias Günther](https://twitter.com/gntr) est le PDG de [Tower](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=7-little-know-git-commands), le client Git de bureau populaire qui aide plus de 100 000 développeurs à travers le monde à être plus productifs avec Git.