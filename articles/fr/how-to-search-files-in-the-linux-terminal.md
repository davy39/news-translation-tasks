---
title: Comment rechercher des fichiers efficacement dans le terminal Linux
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-02-09T22:45:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-files-in-the-linux-terminal
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/BB
seo_title: Comment rechercher des fichiers efficacement dans le terminal Linux
---

Comment-rechercher-des-fichiers-efficacement-dans-linux.png
tags:
- name: Linux
  slug: linux
- name: recherche
  slug: recherche
seo_title: null
seo_desc: 'Avez-vous déjà été frustré de rechercher des fichiers manuellement sur votre ordinateur ?
  Si vous êtes un développeur ou un ingénieur DevOps travaillant sur des serveurs Linux sans GUI, il
  sera difficile de naviguer d'avant en arrière pour trouver des fichiers.

  Beaucoup de gens ne connaissent pas la puissance des terminaux Linux. Linux dispose d'une ligne de commande incroyablement puissante qui vous permet de rechercher des fichiers et des répertoires en une fraction de seconde. 

Que vous soyez débutant ou expert, et si vous cherchez à améliorer vos compétences en gestion de fichiers, vous êtes arrivé au bon endroit. Cet article vous aidera à comprendre les bases de la commande **find** la plus couramment utilisée dans Linux.

## Qu'est-ce que la commande `find` dans Linux ?

La commande `find` vous permet de rechercher des fichiers et des répertoires sur votre ordinateur. Elle ajoute la flexibilité de rechercher des fichiers dans un répertoire spécifique ou récursivement à travers tous les sous-répertoires.

Explorons la puissance de la commande `find`

## Comment rechercher un fichier par nom

Supposons que vous avez enregistré un fichier appelé `hello_world.html` quelque part et que vous ne vous souvenez même pas du nom du répertoire. Mais votre patron vous demande de lui envoyer le fichier immédiatement.

Habituellement, si vous avez oublié où vous avez stocké un fichier, vous commenceriez par parcourir dossier après dossier et vérifier si le fichier existe. 

C'est là que la commande `find` fait un excellent travail. Au lieu de rechercher le fichier manuellement sur votre ordinateur, vous pouvez utiliser la commande `find` pour automatiser le processus.

En passant le nom du fichier en utilisant le flag `-name`, la commande `find` recherche et retourne l'emplacement du fichier.

```bash
find -name <nom_du_fichier>
```

![Image](https://lh4.googleusercontent.com/hUG1ogKlPIlvUZZiCIOBO4x1ZTlGAujhGTe2v-KevAi3zU3z-ZuBA0VJvMWht0V-7cLha4beNzMIkENiN0ZiYZfa8Pc0O-XJMzmbfftY_bo9Csrz-4-7dvwJFgC59G94A2GbFpPTkfU6rxL9MrSOCVI)
_Commande terminal pour rechercher un fichier par nom_

Mais rappelez-vous que le flag `-name` effectue une recherche sensible à la casse. Si vous souhaitez effectuer une recherche insensible à la casse, vous pouvez utiliser le flag `-iname` à la place.

```bash
find -iname <nom_du_fichier>
```

![Image](https://lh4.googleusercontent.com/Gxuso3qZslePPLMxKDtBuQWwQiliDpU2pHAzRTdiRob2OBKrdN1oWA_rTwe2thYiHeUmRo8SBNE2QR6G2kmdDlKhX14wFd9fYmfppZVQNprUHaGMWLB_GgGVSq7l4DQyP2STSFZcx0Rt5B6thvM7T3Y)
_Commande terminal pour effectuer une recherche sensible à la casse_

Vous pouvez également utiliser la commande `find` comme alternative à la commande `ls` dans certains cas. Supposons que vous devez trouver tous les fichiers se terminant par l'extension `.txt`. Vous pouvez le faire avec la commande `find` en utilisant le motif regex (`*.txt`).

```bash
find /chemin/vers/recherche -name "*.txt"
```

![Image](https://lh3.googleusercontent.com/xtbCKd-v83ytN4mnr35RbiWCgJuEiAt9LBO_Qq2IDwRPJaQWRfzBUe5YY63JEcLHS344TvGWRzK139n93upgh1ALKgRavsWwNe0iTh772rhGZwFXcpP5eyGz_iI6XPHuDK55Ch93rNe70fSIyJJcMmw)
_Commande terminal affichant la recherche de fichiers par correspondance de motif_

Cette commande listera tous les fichiers `.txt` dans votre répertoire actuel et ses sous-répertoires. 

Pour trouver les fichiers `.txt` dans un répertoire et sous-répertoire particulier, vous pouvez remplacer `/chemin/vers/recherche` par le chemin de votre répertoire.

## Comment trouver un répertoire dans Linux

La recherche d'un répertoire est possible en passant `d` au paramètre `-type` dans la commande `find`.

```bash
find /chemin/vers/recherche -type d
```

![Image](https://lh5.googleusercontent.com/qmKtQotgBftOfU_pII8GV8gsYJqynmXvaqQIU0VrBOwdcWGwH95R-CQX4rxR3e_xQYyRm5D3bt6f7t0U9DwBHBthlzFnmbtTyvG4MWWMSsOt09zMCTk_ZVcZGUe9NGymbIYf74ELv_7A7yOwY8Hcn0Q)
_Commande terminal pour rechercher un répertoire en utilisant la commande `find`_

Dans la capture d'écran ci-dessus, nous recherchons un répertoire nommé `zip` à partir de notre répertoire actuel.

De même, l'option `-type` accepte d'autres options de paramètre pour simplifier notre processus de recherche.

* `f` trouve la liste des fichiers réguliers
* `b` trouve la liste des périphériques de bloc
* `c` trouve la liste des périphériques de caractère
* `l` trouve la liste des liens symboliques
* `s` trouve la liste des sockets
* `p` trouve les tubes nommés

## Comment rechercher un fichier par taille dans Linux

L'ajout de l'option `-size` avec la commande `find` vous aide à trouver des fichiers en fonction de leur taille. Ajoutez un `+` ou `-` à la taille pour représenter respectivement plus grand que et plus petit que.

```bash
find /chemin/vers/recherche -size <taille_du_fichier>
```

![Image](https://lh6.googleusercontent.com/5_gYC6AREIU77iDWAOY3uqfyCEPpICXenMzpxMv15oaOyNg2t4QhtH862wZeIRH3IgWxX1MJYwAOMGQZVeerY6HeNYjcmB_bdMiqPnoAsSyQ5JjQ75DqmCOsbcLQ8AeMk31MQb9Z1aC0Q-1CznPNRn8)
_Commande terminal pour rechercher des fichiers par taille_

Dans la capture d'écran ci-dessus, nous recherchons tous les fichiers dont la taille est supérieure à 1 Go.

Vous pouvez également rechercher tous les fichiers qui se situent dans une plage de taille spécifique.

Par exemple, si vous voulez trouver tous les fichiers qui sont supérieurs à 50 Mo et inférieurs à 100 Mo, vous pouvez exécuter la commande suivante :

```bash
find /chemin/vers/recherche -size +50M -size -100M
```

![Image](https://lh6.googleusercontent.com/KylER-ErURtFf22PtpPhqT8yQofvlaA6s7XhP8FdHo4KqLTXYsDY5EL3LhVoyZKrHJGMHYWJ6CheD2PiaS_ynX_x-Ziho5eqK8YbEAqdAVvugE0RUWuOPvuwrUddCIw4TnoqLZDSI2qRak1kdDF6o40)
_Commande terminal pour rechercher des fichiers dans une plage_

Vous pouvez spécifier la taille dans votre notation préférée. Voici quelques-unes des notations disponibles :

1. K représente Ko
2. M représente Mo
3. G représente Go
4. b représente les octets
5. c représente les blocs

## Comment rechercher un fichier en fonction de la date de modification

Chaque fichier a une date de création et une date de dernière mise à jour qui lui sont associées. Supposons que vous avez des milliers de fichiers dans votre répertoire. Vous avez modifié un fichier il y a quelques jours et vous avez oublié son nom. Vous êtes sûr d'avoir modifié seulement quelques fichiers après cela. 

Dans de tels cas, vous pouvez trouver tous les fichiers qui ont été modifiés au cours des 7 derniers jours. Cela limite votre recherche de 1000+ fichiers à une quantité plus gérable. Vous serez en mesure de trouver le fichier que vous avez modifié en quelques secondes après avoir exécuté la commande.

Cela est possible en passant le paramètre `-mtime` avec la commande `find`.

```
find /chemin/vers/recherche -mtime <-nombre_de_jours_ecoules>
```

![Image](https://lh3.googleusercontent.com/EOsirsBvBa83A2NeK1qGZ8g_FLriAngr4yso3nhOpuwT18zrkur92GKfMBfr8nA8ULrgdWvREvzJfSznVecNXZXONs3JXdG3gJFoqZ7PcqFmZe3T2IS0ka-bkSajpj3aXunMvTYYPZkLl4YjkYzx_1Y)
_Commande terminal pour rechercher un fichier en fonction de la date de modification_

Supposons un autre scénario, où la date d'aujourd'hui est le 10 février 2023. Vous avez modifié un fichier avant le 3 février 2023. Après le 3 février 2023, vous avez modifié beaucoup de fichiers. Vous devez trouver le fichier que vous avez modifié avant le 3 février 2023. Donc, en gros, vous avez besoin des fichiers qui ont été modifiés avant le 3 février 2023.

Scénario étrange, n'est-ce pas ?

Mais, vous pouvez également exécuter cette requête en utilisant la commande `find`. Vous pouvez y parvenir en échangeant le signe négatif (-) avec le signe positif (+).

Voici la commande modifiée pour vous :

```bash
find /chemin/vers/recherche -mtime +7
```

## Comment exécuter une commande sur des fichiers filtrés à partir de la commande `find`

Cette question peut vous confondre. Avant de révéler la réponse, comprenons clairement la question avec un scénario réel. 

Supposons que vous avez 1000 fichiers dans un répertoire, et l'exécution de la commande `find` retourne 20 fichiers correspondants. Vous voulez déplacer ces 20 fichiers dans un répertoire différent. Comment pouvez-vous y parvenir ?

En termes simples, nous devons exécuter une commande sur chacun des fichiers filtrés.

Vous pouvez le faire en passant l'option `-exec` avec la commande `find`.

L'option `-exec` exécute une commande sur chaque fichier trouvé dans la recherche. L'option `-exec` est suivie d'une commande et de ses arguments, les symboles `{}` représentant le chemin du fichier en cours de traitement.

Pour représenter la fin de la commande `-exec`, nous devons ajouter `\;` (une barre oblique inverse et un point-virgule).

Voici la syntaxe :

```bash
find /chemin/vers/recherche -name  -exec  {}  \;
```

Essayons de déplacer les fichiers filtrés du répertoire `5minslearn` vers le répertoire `zip`.

Voici la commande :

```
find ./5minslearn -name "*.zip" -exec mv {} ./5minslearn/zip \;
```

![Image](https://lh5.googleusercontent.com/Oysc8VJqcheOL0uSk9t18SM1BBckLmZ1Sfs026TByvdQcHNFVDGssztFu13rHi0waaOUXCuKx1rsHbyWCXr190agnVEKZA3rMexuSH_m6myz38JhQ563hNLBKfTBOMklTt-aH5dd05CfXCVwKG0yiZI)

Cette commande recherche tous les fichiers se terminant par `.zip` dans le répertoire `./5minslearn` et déplace ensuite chaque fichier vers le répertoire `./5minslearn/zip`.

L'option `-exec` vous permet d'effectuer une large gamme d'opérations sur les fichiers trouvés. Vous pouvez remplacer la commande de déplacement de l'exemple ci-dessus par une commande de copie, de suppression ou même de changement de permission de fichier.

## Comment exécuter une commande sur des fichiers filtrés avec une confirmation

La plupart des gens préféreront utiliser cela s'ils ne sont pas sûrs d'appliquer l'opération sur chaque fichier. 

L'option `-ok` est similaire à l'option **`-exec`** sauf qu'elle demandera une confirmation avant d'exécuter l'opération sur chaque fichier. Cette commande est super utile pour examiner les fichiers qui seront affectés avant d'exécuter l'opération spécifique. Vous avez également la possibilité de refuser si vous n'êtes pas sûr ou ne souhaitez pas appliquer la commande.

Par exemple, cette fois, essayons de déplacer les fichiers `.txt` vers l'autre répertoire.

```bash
find /chemin/vers/recherche -name "*.txt" -ok mv {} /chemin/vers/destination \;
```

![Image](https://lh3.googleusercontent.com/LR9SFYz9f90xR6_aMS_VKEQa7IS9cecwEAMRkNh5KJ1JSMaQCx0cIe-5XOonpOOdELbnU8549XkQ-HfYCQEoG9Epn8F89cA86o3BRFTR9cJtOLM7GgvKpWMNpkutX89sRtWs96wZ0pz-JHZTSGFBrq0)
_Commande terminal pour déplacer les fichiers filtrés avec une confirmation_

La commande ci-dessus recherche tous les fichiers avec une extension `.txt` dans le répertoire `./5minslearn` et demande ensuite à l'utilisateur de confirmer avant de déplacer chaque fichier vers le répertoire `./5minslearn/text_files`.

Pour approuver l'opération, entrez `yes` et `no` pour refuser l'opération et passer au fichier suivant. 

L'option `-ok` est utile lorsque vous voulez être prudent avec les fichiers que vous modifiez, car elle vous permet d'inspecter chaque fichier et son emplacement avant d'exécuter la commande spécifiée.

## Comment trouver un fichier avec des informations détaillées

L'option `-ls` dans la commande find est utilisée pour afficher des informations sur les fichiers trouvés dans la recherche, au format de la commande ls. Cette option fournit des informations détaillées sur les fichiers, telles que leurs permissions, propriétaire, taille et date de dernière modification. 

```
find /chemin/vers/recherche -name "*.<extension-de-fichier>" -ls
```

![Image](https://lh4.googleusercontent.com/RYVzpx-YYKuOUhg_lD7RmNKk-PtGodtMIVwL482R6xvItZ40y3dJLdmDCHWEV6EG1kPVfe4NVt3lHgdnzjvr3RD2xs51Sy4NoV584BxhuJCCIO7dGW1x9IXKD8sGEYkZJ6UDcOenwX3F35o2on68SPk)
_Commande terminal pour lister les fichiers au format de la commande `ls`_

## Comment trouver et supprimer des fichiers

Avez-vous déjà eu besoin de trouver des fichiers et de les supprimer de votre ordinateur ? L'option `-delete` dans la commande find fait cela pour vous. Elle vous permet de supprimer des fichiers qui correspondent aux critères spécifiés.

```bash
find . -name "*.<extension>" -delete
```

![Image](https://lh3.googleusercontent.com/W2DQEoEcNi0897Z99NPHyhx6RTPpO1hL0AVCAGCuKdabq8_eXbFtsL2BJdLn6MCqdYXTa7veSRhDj9gTU7Rbbz0vNoIbxF_N_IXmR45IHgH3DMXSnMBRPtLjIKK-G9af5FncqC2s28zqBfP6kcinXqY)

Dans l'exemple ci-dessus, vous pouvez voir que la commande find a supprimé les fichiers avec l'extension `.html`

Note : Cette opération est irréversible. Soyez sûr à 100 % lorsque vous exécutez l'opération de suppression.

Je vous conseillerais d'exécuter la commande `find` sans le flag `-delete` au début et de vous assurer que seuls les fichiers qui doivent être supprimés sont affichés. Une fois que vous êtes sûr, vous pouvez exécuter la même commande en ajoutant le flag `-delete`.

## Conclusion

Dans cet article, vous avez appris comment rechercher des fichiers efficacement en utilisant votre terminal Linux. 

Ce sont des options très basiques dans la commande find que je pense que chaque développeur devrait connaître. Je crois que maîtriser les fondamentaux est la première étape pour devenir plus avancé avec Linux. J'ai couvert les bases dans tous mes blogs pour vous aider à créer une base solide. 

Pour en savoir plus sur Linux, abonnez-vous à ma newsletter par email sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_find_command) et suivez-moi sur les réseaux sociaux.