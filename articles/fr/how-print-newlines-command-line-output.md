---
title: Comment imprimer des sauts de ligne dans la sortie de la ligne de commande
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-12-05T14:02:00.000Z'
originalURL: https://freecodecamp.org/news/how-print-newlines-command-line-output
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/cover.png
tags:
- name: Bash
  slug: bash
- name: c programming
  slug: c-programming
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: terminal
  slug: terminal
seo_title: Comment imprimer des sauts de ligne dans la sortie de la ligne de commande
seo_desc: Surprisingly, getting computers to give humans readable output is no easy
  feat. With the introduction of standard streams and specifically standard output,
  programs gained a way to talk to each other using plain text streams. But humanizing
  and displ...
---

De manière surprenante, faire en sorte que les ordinateurs fournissent une sortie lisible par les humains n'est pas une tâche facile. Avec l'introduction des [flux standard](https://en.wikipedia.org/wiki/Standard_streams) et spécifiquement de la sortie standard, les programmes ont gagné un moyen de communiquer entre eux en utilisant des flux de texte brut. Mais humaniser et afficher stdout est une autre affaire. La technologie tout au long de l'ère informatique a tenté de résoudre ce problème, depuis l'utilisation de [caractères ASCII dans les affichages vidéo des ordinateurs](https://en.wikipedia.org/wiki/Computer_terminal#Early_VDUs) jusqu'aux commandes shell modernes comme `echo` et `printf`.

Ces avancées n'ont pas été sans heurts. La tâche d'imprimer une sortie dans un terminal est semée d'embûches pour les programmeurs, comme en témoigne la tâche trompeusement non triviale d'expansion d'une [séquence d'échappement](https://en.wikipedia.org/wiki/Escape_sequence) pour imprimer des sauts de ligne. L'expansion du placeholder `\n` peut être accomplie de multiples façons, chacune avec son propre historique et ses complications.

## Utilisation de `echo`

Depuis son apparition dans [Multics](https://en.wikipedia.org/wiki/Multics) jusqu'à son ubiquité dans les systèmes modernes de type Unix, `echo` reste un outil familier pour faire dire à votre terminal « Hello world! ». Malheureusement, les implémentations inconsistantes à travers les systèmes d'exploitation rendent son utilisation délicate. Alors que `echo` sur certains systèmes développera automatiquement les séquences d'échappement, [d'autres](https://man.cat-v.org/unix_8th/1/echo) nécessitent une option `-e` pour faire de même :

```sh
echo "the study of European nerves is \neurology"
# the study of European nerves is \neurology

echo -e "the study of European nerves is \neurology"
# the study of European nerves is 
# eurology
```

En raison de ces incohérences dans les implémentations, `echo` est considéré comme non portable. De plus, son utilisation en conjonction avec des entrées utilisateur est relativement facile à corrompre via une [attaque par injection de shell](https://en.wikipedia.org/wiki/Code_injection#Shell_injection) utilisant des substitutions de commandes.

Dans les systèmes modernes, il est conservé uniquement pour fournir une compatibilité avec les nombreux programmes qui l'utilisent encore. La [spécification POSIX recommande](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/echo.html#tag_20_37_16) l'utilisation de `printf` dans les nouveaux programmes.

## Utilisation de `printf`

Depuis la 4ème [Édition](https://en.wikipedia.org/wiki/Research_Unix#Versions) Unix, la commande portable [`printf`](https://en.wikipedia.org/wiki/Printf_(Unix)) est essentiellement le nouveau et meilleur `echo`. Elle permet d'utiliser des [spécificateurs de format](https://en.wikipedia.org/wiki/Printf_format_string#Format_placeholder_specification) pour humaniser l'entrée. Pour interpréter les séquences d'échappement avec des barres obliques inverses, utilisez `%b`. La séquence de caractères `\n` garantit que la sortie se termine par un saut de ligne :

```sh
printf "%b\n" "Many females in Oble are \noblewomen"
# Many females in Oble are 
# oblewomen
```

Bien que `printf` ait d'autres options qui en font un remplacement bien plus puissant de `echo`, cet utilitaire n'est pas infaillible et peut être vulnérable à une attaque par [chaîne de format non contrôlée](https://en.wikipedia.org/wiki/Uncontrolled_format_string). Il est important pour les programmeurs de s'assurer qu'ils [gèrent soigneusement les entrées utilisateur](https://victoria.dev/blog/sql-injection-and-xss-what-white-hat-hackers-know-about-trusting-user-input/).

## Mettre des sauts de ligne dans des variables

Dans un effort pour améliorer la portabilité parmi les compilateurs, le [Standard ANSI C](https://en.wikipedia.org/wiki/ANSI_C) a été établi en 1983. Avec [les guillemets ANSI-C](https://www.gnu.org/software/bash/manual/html_node/ANSI_002dC-Quoting.html#ANSI_002dC-Quoting) utilisant `$'...'`, les [séquences d'échappement](https://en.wikipedia.org/wiki/Escape_sequences_in_C#Table_of_escape_sequences) sont remplacées dans la sortie selon la norme.

Cela nous permet de stocker des chaînes avec des sauts de ligne dans des variables qui sont imprimées avec les sauts de ligne interprétés. Vous pouvez faire cela en définissant la variable, puis en l'appelant avec `printf` en utilisant `$` :

```sh
puns=$'\number\narrow\nether\nice'

printf "%b\n" "These words started with n but don't make $puns"

# These words started with n but don't make 
# umber
# arrow
# ether
# ice
```

La variable développée est entre guillemets simples, ce qui est passé littéralement à `printf`. Comme toujours, il est important de gérer correctement l'entrée.

## Tour bonus : l'expansion des paramètres de shell

Dans mon article expliquant [Bash et les accolades](https://victoria.dev/blog/bash-and-shell-expansions-lazy-list-making/), j'ai couvert la magie de [l'expansion des paramètres de shell](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html). Nous pouvons utiliser une expansion, `${parameter@operator}`, pour interpréter les séquences d'échappement, aussi. Nous utilisons le spécificateur `%s` de `printf` pour imprimer en tant que chaîne, et l'opérateur `E` développera correctement les séquences d'échappement dans notre variable :

```sh
printf "%s\n" ${puns@E}

# umber
# arrow
# ether
# ice
```

## Le défi continu de parler en humain

L'[interpolation de chaînes](https://en.wikipedia.org/wiki/String_interpolation) continue d'être un problème épineux pour les programmeurs. En plus de faire en sorte que les langages et les shells s'accordent sur la signification de certains placeholders, l'utilisation correcte des séquences d'échappement nécessite un œil attentif aux détails.

Une mauvaise interpolation de chaînes peut conduire à une sortie ridicule, ainsi qu'introduire des vulnérabilités de sécurité, telles que celles provenant d'[attaques par injection](https://en.wikipedia.org/wiki/Code_injection). Jusqu'à ce que la prochaine évolution du terminal nous fasse communiquer en emojis, nous ferions mieux de prêter attention lors de l'impression de la sortie pour les humains.