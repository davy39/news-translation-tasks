---
title: Astuces en ligne de commande pour gérer votre dépôt open source désordonné
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-02-21T01:56:00.000Z'
originalURL: https://freecodecamp.org/news/command-line-tricks-for-managing-your-messy-open-source-repository
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/7E334F85-E7BB-47E3-B886-77F35E3D20DC.png
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Git
  slug: git
- name: open source
  slug: open-source
seo_title: Astuces en ligne de commande pour gérer votre dépôt open source désordonné
seo_desc: 'Effective collaboration, especially in open source software development,
  starts with effective organization. To make sure that nothing gets missed, the general
  rule, “one issue, one pull request” is a nice rule of thumb.

  Instead of opening an issue w...'
---

Une collaboration efficace, surtout dans le développement de logiciels open source, commence par une organisation efficace. Pour s'assurer que rien n'est oublié, la règle générale, « un problème, une pull request » est une bonne règle de base.

Au lieu d'ouvrir un problème avec un large périmètre comme « Corriger tous les liens brisés dans la documentation », les projets open source auront plus de chances d'attirer des contributeurs avec plusieurs problèmes plus petits et plus gérables.

Dans l'exemple précédent, vous pourriez limiter les liens brisés par section ou par page. Cela permet à plus de contributeurs de sauter et de consacrer de petites fenêtres de leur temps, plutôt que d'attendre qu'une seule personne prenne en charge un effort de contribution plus grand et plus fastidieux.

Les problèmes de plus petite envergure aident également les mainteneurs de projets à voir où le travail a été terminé et où il ne l'a pas été. Cela réduit les chances qu'une partie du problème soit oubliée, supposée être terminée, et conduise plus tard à des bugs ou à des vulnérabilités de sécurité.

C'est très bien. Mais que faire si vous avez déjà ouvert plusieurs problèmes de grande envergure, que certaines PR ont déjà été soumises ou fusionnées, et que vous n'avez actuellement aucune idée de l'endroit où le travail a commencé ou s'est arrêté ?

Il va falloir un peu de tri pour remettre l'état de votre projet sous contrôle. Heureusement, il existe un certain nombre d'outils en ligne de commande pour vous aider à scanner, trier et comprendre un dépôt désordonné. Voici une petite sélection de ceux que j'utilise.

## Recherche et remplacement interactifs avec `vim`

Vous pouvez ouvrir un fichier dans Vim, puis rechercher et remplacer de manière interactive avec :

```vim
:%s/\<word\>/newword/gc
```

Le `%` indique de chercher dans toutes les lignes du fichier courant, `s` est pour substituer, `\<word\>` correspond au mot entier, et le `g` pour « global » est pour chaque occurrence. Le `c` à la fin vous permettra de visualiser et de confirmer chaque changement avant qu'il ne soit effectué. Vous pouvez l'exécuter automatiquement, et beaucoup plus rapidement, sans `c`, mais vous vous exposez au risque de compliquer les choses si vous avez fait une erreur de correspondance de motif.

## Trouver les liens morts dans les fichiers Markdown avec un module node

Le module node [markdown-link-check](https://github.com/tcort/markdown-link-check) a un excellent [CLI buddy](https://github.com/tcort/markdown-link-check#command-line-tool).

Je l'utilise si souvent que je l'ai transformé en [fonction alias Bash](https://victoria.dev/blog/how-to-do-twice-as-much-with-half-the-keystrokes-using-.bashrc/#bash-functions). Pour faire de même, ajoutez ceci à votre `.bashrc` :

```sh
# Vérification des liens Markdown dans un dossier, récursif
function mlc () {
    find $1 -name \*.md -exec markdown-link-check -p {} \;
}
```

Puis exécutez avec `mlc <filename>`.

## Lister les sous-répertoires avec ou sans dépôt git avec `find`

Imprimer tous les sous-répertoires qui sont des dépôts git, ou en d'autres termes, qui ont un `.git` :

```sh
find . -maxdepth 1 -type d -exec test -e '{}/.git' ';' -printf "est un dépôt git : %p\n"
```

Pour imprimer tous les sous-répertoires qui ne sont pas des dépôts git, négociez le test avec `!` :

```sh
find . -maxdepth 1 -type d -exec test '!' -e '{}/.git' ';' -printf "n'est pas un dépôt git : %p\n"
```

## Cloner plusieurs dépôts git à partir d'une liste avec `xargs`

J'ai initialement utilisé cela dans le cadre de la [re-création automatique de mon ordinateur portable avec des scripts Bash](https://victoria.dev/blog/how-to-set-up-a-fresh-ubuntu-desktop-using-only-dotfiles-and-bash-scripts/), mais c'est assez pratique lorsque vous travaillez avec des instances cloud ou des Dockerfiles.

Étant donné un fichier, `repos.txt` avec un lien SSH de dépôt sur chaque ligne (et vos clés SSH configurées), exécutez :

```sh
xargs -n1 git clone < repos.txt
```

Si vous souhaitez cloner et pousser plusieurs dépôts, j'ai précédemment écrit sur [comment utiliser une commande Bash pour gérer vos dépôts](https://victoria.dev/blog/how-to-write-bash-one-liners-for-cloning-and-managing-github-and-gitlab-repositories/).

## Lister les problèmes par numéro avec `jot`

Je suis co-auteur et mainteneur du dépôt [OWASP Web Security Testing Guide](https://github.com/OWASP/wstg/) où j'ai récemment pris un grand problème (oui, c'était « Corriger tous les liens brisés dans la documentation » - comment l'auriez-vous deviné ?) et je l'ai divisé en plusieurs problèmes plus petits et plus gérables. Un total de trente-sept problèmes plus petits et plus gérables.

Je voulais énumérer tous les problèmes que le problème original est devenu, mais l'idée de taper trente-sept numéros de problème (#275 à #312) semblait horriblement fastidieuse et chronophage. Donc, en bon programmeur, j'ai passé le même temps que j'aurais utilisé pour taper tous ces numéros et j'ai conçu un moyen de l'automatiser à la place.

L'utilitaire `jot` (`apt install athena-jot`) est un petit outil qui est d'une grande aide lorsque vous voulez imprimer des nombres. Il suffit de lui dire combien vous en voulez, et où commencer et arrêter.

```sh
# jot [ reps [ begin [ end ] ] ]
jot 37 275 312
```

Cela imprime chaque nombre, inclusivement, de 275 à 312 sur une nouvelle ligne. Pour transformer ces nombres en notations de numéros de problème que GitHub et de nombreuses autres plateformes reconnaissent et transforment automatiquement en liens, vous pouvez rediriger la sortie vers `awk`.

```sh
jot 37 275 312 | awk '{printf "#"$0", "}'

#275, #276, #277, #278, #279, #280, #281, #282, #283, #284, #285, #286, #287, #288, #289, #290, #291, #292, #293, #295, #296, #297, #298, #299, #300, #301, #302, #303, #304, #305, #306, #307, #308, #309, #310, #311, #312
```

Vous pouvez également utiliser `jot` pour générer des données aléatoires ou redondantes, principalement à des fins de développement ou de test.

## Organisation open source alimentée par la CLI

Un dépôt open source bien organisé est un projet open source bien maintenu. Enregistrez cet article pour référence pratique, et utilisez vos nouveaux superpouvoirs CLI pour le bien ! 💡