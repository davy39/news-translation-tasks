---
title: Permissions de fichiers sous Linux – Comment utiliser la commande chmod
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-01-02T22:17:02.000Z'
originalURL: https://freecodecamp.org/news/file-permissions-in-linux-chmod-command-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Banner
seo_title: Permissions de fichiers sous Linux – Comment utiliser la commande chmod
---

File-permission-blog-1.png
tags:
- name: ligne de commande
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Tout comme avec d'autres systèmes d'exploitation, plusieurs utilisateurs peuvent créer des comptes utilisateur et partager la même machine exécutant le système d'exploitation Linux. Mais chaque fois que différents utilisateurs partagent un système, des problèmes de confidentialité peuvent facilement survenir. Le premier utilisateur peut ne pas souhaiter que le prochain utilisateur affiche, modifie ou supprime ses fichiers, par exemple."
---

Tout comme avec d'autres systèmes d'exploitation, plusieurs utilisateurs peuvent créer des comptes utilisateur et partager la même machine exécutant le système d'exploitation Linux.

Mais chaque fois que différents utilisateurs partagent un système, des problèmes de confidentialité peuvent facilement survenir. Le premier utilisateur peut ne pas souhaiter que le prochain utilisateur affiche, modifie ou supprime ses fichiers, par exemple.

Le terminal Linux possède quelques superpouvoirs en matière de gestion des permissions de fichiers. Vous pouvez accorder ou révoquer des permissions pour chaque fichier et répertoire à partir de votre terminal Linux.

## Qu'est-ce que les permissions de fichiers sous Linux ?

Les permissions de fichiers contrôlent les actions qui peuvent être effectuées par quels utilisateurs. Lire, Écrire et Exécuter sont les trois actions possibles pour chaque fichier.

Les utilisateurs sont classés sous trois grandes catégories : Utilisateurs normaux, Groupes et Autres. Linux permet aux utilisateurs de définir des permissions à un niveau très granulaire. Vous pouvez sécuriser votre fichier ou répertoire à chaque emplacement possible d'un système de fichiers.

Cela semble utile, n'est-ce pas ?

Il y a trois commandes importantes que vous utiliserez lors de la gestion des permissions de fichiers :

1. `chmod` (Changer le mode)
2. `chown` (Changer le propriétaire)
3. `chgrp` (Changer le groupe)

Parmi celles-ci, `chmod` est l'une des commandes les plus importantes. Nous allons discuter de la commande `chmod` dans ce tutoriel, et j'aborderai les autres dans les prochains articles.

Plongeons-nous dans la commande `chmod` 🌊.

### Actions que vous pouvez effectuer sur un fichier

Avant de continuer, je veux m'assurer que vous êtes clair sur le fonctionnement des actions Lire, Écrire et Exécuter d'un fichier. Lire et écrire sont assez explicites – ils déterminent si un utilisateur peut lire ou écrire dans un fichier.

Mais, qu'est-ce qu'un fichier exécutable ?

Un fichier est dit exécutable s'il contient une séquence d'instructions pour accomplir quelque chose. Un bon exemple est les fichiers de script (scripts shell).

## Qu'est-ce que la commande `chmod` ?

`chmod` est une commande qui vous permet de changer les permissions d'un fichier ou d'un répertoire pour tous les types d'utilisateurs.

Voici la syntaxe de la commande chmod :

```bash
chmod <Opérations> <Nom de Fichier/Répertoire>
```

Vous pouvez accorder ou révoquer la permission en remplaçant les Opérations dans la commande ci-dessus.

### Quelles sont les opérations que vous pouvez effectuer ?

Les Opérations dans la syntaxe ci-dessus sont divisées en 2 catégories. Explorons-les ci-dessous.

#### Permissions au niveau de l'utilisateur

Ces opérations contrôlent les permissions au niveau de l'utilisateur. Voici les commandes que vous pouvez utiliser :

* `u` – Accorder la permission à un utilisateur
* `g` – Accorder la permission à un groupe (Un groupe d'utilisateurs)
* `o` – Accorder la permission aux autres (ceux qui ne font pas partie des catégories ci-dessus).

**Note :** Si cette option est laissée vide, les permissions seront appliquées à l'utilisateur connecté. La plupart du temps, elle sera laissée vide.

#### Permissions au niveau du fichier

Celles-ci contrôlent les permissions au niveau du fichier.

* `r` – Accorde la permission de lecture
* `w` – Accorde la permission d'écriture
* `x` – Accorde la permission d'exécution

Ces opérations doivent être précédées d'un opérateur '+' ou '-'.

'+' indique l'ajout d'une nouvelle permission, et '-' indique la suppression d'une permission existante.

Voici un exemple :

```bash
chmod +r sample.txt
```

La commande ci-dessus ajoute la permission de lecture pour le fichier `sample.txt`.

Assez simple, n'est-ce pas ? Continuons.

## Comment rendre un fichier exécutable sous Linux

Je peux expliquer cela plus clairement avec un exemple de mon expérience.

Linux est le système d'exploitation par défaut de mon équipe. Nous avons récemment embauché un stagiaire, qui n'a aucune connaissance de Linux mais était curieux d'apprendre et d'explorer. Nous avons commencé à le former en lui demandant d'écrire quelques scripts shell, car la plupart des serveurs exécutent le système d'exploitation Linux. Il a trouvé tout le code sur Internet et l'a copié (nous avons donné une telle tâche intentionnellement).

Il a sauvegardé le fichier mais n'a pas pu exécuter le script. Il ne connaissait pas le problème réel. Il a commencé à supprimer quelques blocs de code et a essayé de l'exécuter encore et encore.

Il a répété l'erreur indiquant "Commande introuvable".

Finalement, il est arrivé à la 1ère ligne. Il a remplacé cette ligne par une instruction d'impression (la commande "echo") et a exécuté le fichier dans l'espoir de voir la sortie. Mais il n'avait toujours pas trouvé cette erreur.

Avec un peu de frustration, il a demandé de l'aide.

Regardons le problème maintenant.

En fait, nous pouvons exécuter les fichiers .sh en les exécutant simplement comme ceci :

```bash
./install.sh
```

Regardons le code à l'intérieur de `install.sh`

```bash
echo "Ceci est un fichier exécutable 🎉"
```

Il a exécuté la même commande mais cela n'a pas fonctionné. Cela est dû au fait que le fichier n'était pas au format exécutable. J'ai donc exécuté la commande magique pour rendre le fichier exécutable :

```bash
chmod +x install.sh
```

![Image](https://lh3.googleusercontent.com/trd4dTKoxhk9Ap9xLifsuo6bD9wj4kc_i5gtDudFLQyU1gNdJLGoLoyCuJLh1FF9Yah-IG43YuR3yrrtJq48xBEYEq0QQkHMFB1n1YBiv-_fWJT95gyihZD0tjAj0ScnEmF33WRFdHJbfzTSpxSnaimyUbHlK9a2hMujE8CeyT4AoliZY5XJ_wKOsIVrPw)
_Commande du terminal pour rendre un fichier exécutable_

Maintenant, il est exécutable. Il m'a regardé comme si j'étais un hacker 😂. Mais en réalité, c'est un concept assez simple et basique.

## Comment supprimer les permissions d'un fichier sous Linux

Je travaille avec mon collègue Divad sur de nombreux projets, et il aime essayer de me tromper. Nous travaillons ensemble sur de nombreux projets de loisirs et nous écrivons souvent des scripts shell pour un déploiement rapide.

Chaque fois qu'il écrit des scripts shell, il supprime toujours toutes les permissions du fichier et pousse les changements vers le dépôt distant. Donc, chaque fois, je dois accorder des permissions en utilisant les commandes ci-dessus pour toute action que je dois effectuer.

Jetons un rapide coup d'œil à la commande qu'il utilise pour supprimer les permissions des fichiers.

Ici, nous avons un fichier nommé `install.sh` qui a toutes les permissions (Lire, Écrire, Exécuter). Supprimons la permission d'exécution pour ce fichier de script.

```bash
chmod -x install.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-136.png)
_Commande du terminal pour supprimer la permission d'exécution d'un fichier_

Vous ne pourrez pas exécuter ce fichier maintenant. Essayer de le faire vous donnera une erreur comme montré dans la capture d'écran ci-dessus.

Supprimons la permission de lecture du fichier.

```bash
chmod -r install.sh
```

D'accord, avec cette commande, nous avons supprimé la permission de lecture. Essayons de lire ce fichier en utilisant Nano (l'éditeur de fichiers pour le terminal Linux). Vous pourrez voir l'erreur "Permission refusée" en bas.

![Image](https://lh4.googleusercontent.com/DHdaIMmV0pcFiMO-9GiLwXbUes8QZs5v6uKDLfuCu9Ltt-0SitENOM8najXPaxMXFJSQAzlI7F1u1p8i6fbqq1timsCoVGVOBdEtzUlybcmoh0W6oHWrIKyUUJr1dOjDZ_vbo0WkGE3fcLa3T7ZfvymVKVZPoKvKrDDH7ZVFSSlyeyQ1ypLixkAdD5uroA)

![Image](https://lh3.googleusercontent.com/iphPcFoH9r0VnGArokWKexbVTzGtMkaOC-EgeXECKqHyE2QJMA49sh5HK_u_ZNKDDKc_hmFPe-dM8VVy0Xu-EKGT1VpBaABcUtPxCEipSvNVhwJQWfxisGBHJbvAcosK3kO8JNsWT9qSl2-7A0cK-A8gHjWIK4cfvNAx4iofZOOPOgevXbR8mVjmDZqk0w)

La même chose s'applique pour supprimer la permission d'écriture du fichier :

```bash
chmod -w install.sh
```

![Image](https://lh5.googleusercontent.com/wVL6XdsMVVBrqw3dnrjELCIsqQyDkxtQWUKcD8HyXAUJktcBQyYAK1Ln-A9P517WW1b8tfm95HGd4NmRuP9fgs9QI6w9ZrR0ZeSNyMpWIlYlGld_Vq1-_m8fDDcV9Et-BJd99Jy3RI2cs6vm26Ywp9IFJzx1su8CGVgoe38-BNJp9qDooZe7XAbqv1S88A)

Vous pouvez réaliser tout ce qui précède ensemble en utilisant la commande suivante :

```bash
chmod -rwx install.sh
```

Ceci est la partie centrale de la gestion des permissions de fichiers sous Linux. N'oubliez pas que nous avons à peine effleuré la surface de ce sujet. Essayez de le comprendre et de jouer avec quelques fichiers d'exemple. Parce que qui sait – à l'avenir, vous pourriez avoir un collègue comme Divad. :)

## Comment ajouter ou supprimer des permissions pour les répertoires (dossiers) sous Linux

Si vous travaillez avec Linux, vous avez peut-être rencontré divers répertoires tels que `/etc`, `/var`, `/opt`, et autres. Mais vous n'êtes peut-être pas conscient de la raison pour laquelle ces répertoires existent.

Il y a une chose en commun pour tous ces dossiers, cependant : vous ne pourrez pas créer un fichier ou un dossier à l'intérieur sans la permission root.

Ce paramètre sera pré-configuré dans votre système lors de l'installation du système d'exploitation Linux.

Mais, vous pourriez vous demander, puis-je restreindre mon dossier dans un répertoire `/home` similaire aux répertoires ci-dessus ? La réponse est oui. Vous pouvez y parvenir en changeant la permission du répertoire en utilisant la commande `chmod`.

Comprenons cela avec un exemple.

J'ai créé un répertoire nommé `locked_directory` et j'ai supprimé la permission de lecture de ce répertoire. Si j'essaie de lire le contenu du dossier en utilisant la commande `ls`, je finirai par voir le message d'erreur "Permission refusée".

```bash
chmod -r locked_directory/
```

![Image](https://lh5.googleusercontent.com/JfC_fUvfsYzwm23cEaE6ThbFRGdY-tazuXBYIxBdunGsSSema2yGIFkJrLtw0rksPpG4iSUiBqjm9Uu5bEIuTasDyNm_zX0kLAqA3Ncv30FHcmSaXe_XbOzBdIBtg4hVI9kuIwPnRIYhdBZpsfXIaPPnVGUwBP5cwvfWpFn2OPjQfjjiIkkd3rrz0w465A)
_Commande `chmod` pour supprimer la permission de lecture d'un répertoire_

Mais, saviez-vous que je peux créer un autre répertoire à l'intérieur de `locked_directory` nommé `dir1` et lire les fichiers et dossiers dans `dir1` ?

![Image](https://lh6.googleusercontent.com/FMLRcjtvY-M1YVSANwmgdzdDwBJ9lrv4V7dLREva9RRUmal7PG8Q5p-l4XZMCi3zIznvSqIKpr68PwGlcripbREffgPzpmqOJ09OR-CvBEGrncBxYX9c9OTe0kq5-xL9rsGP1xQDO_sZP9iXPmHKpXFukFhTIYlXaFRnoHvdCRYA1FJDHcvXmFqP8dmshA)

Alors, quel est le but de la commande que nous venons d'exécuter ? Supprimer la permission de lecture sur le parent devrait également supprimer la même chose sur les répertoires enfants, n'est-ce pas ?

Eh bien. C'est exactement ce que je vous ai dit plus tôt. Linux gère un niveau très granulaire de permissions de fichiers.

Si vous souhaitez appliquer les permissions au répertoire parent et à tous ses répertoires enfants, vous devez passer un drapeau exclusif avec la commande `chmod`.

Ce drapeau est `-R`. Il signifie essentiellement appliquer les mêmes permissions de manière récursive à tous les sous-répertoires (répertoires enfants). Ainsi, cette permission s'appliquera à l'enfant final d'un fichier/répertoire.

Voici la syntaxe pour cela :

```bash
sudo chmod -R <permission> <nomdefichier>
```

N'oubliez pas que l'exécution de la commande pour effectuer une opération récursive nécessite une permission root. Vous devez donc ajouter `sudo` au début de cette commande. Voici à quoi cela ressemble :

```bash
sudo chmod -R -r locked_directory
```

![Image](https://lh3.googleusercontent.com/GZGisVgUxcZjYduKGlOaYHUaTRTgI7tf3nNzdpxL8QZvDDYV_PLgwaFipmbfxzDlziG_Gy7f5Gyeibc_E7IhGvEOmReUKUe3t7yYMXZKDsRnXcxivbepHpqww3y2YSLSyjvi83i_c5Z1rgQbc_ku-Bz5hy8lMl8idzg4MtfYtEZymPFTZBNceq9xgH79ZQ)
_Commande du terminal pour supprimer la permission de lecture d'un répertoire de manière récursive_

À partir de la capture d'écran ci-dessus, vous pouvez voir que l'essai de visualisation des fichiers du répertoire enfant a échoué après avoir supprimé la permission de lecture de manière récursive à partir du répertoire parent.

## Une autre façon de gérer les permissions de fichiers sous Linux

Alternativement, vous pouvez utiliser la représentation octale pour contrôler les permissions de fichiers.

Nous pouvons utiliser des nombres pour représenter les permissions de fichiers (la méthode la plus couramment utilisée pour définir les permissions). Lorsque vous changez les permissions en utilisant le mode octal, vous représentez les permissions pour chaque triplet en utilisant un nombre (4, 2, 1, ou une combinaison de 4, 2 et 1).

Regardons la syntaxe pour utiliser le mode octal :

```bash
chmod <utilisateur><groupe><autres> install.sh
```

Voici un exemple de mode octal :

```bash
chmod 777 install.sh
```

### Comment puis-je supprimer les permissions en utilisant le mode octal ?

Nous pouvons utiliser `0` pour supprimer les permissions d'un fichier. Voici un exemple :

```bash
chmod 000 install.sh
```

<table class=""><thead></thead><tbody><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Accès</strong></td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Mode Symbolique</strong></td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Mode Octal</strong></td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Lire</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">r</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">4</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Écrire</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">w</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">2</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Exécuter</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">x</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">1</td></tr></tbody><tfoot></tfoot></table>

Le tableau montre le code octal pour chaque permission de fichier :

<table class=""><thead></thead><tbody><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Accès</strong></td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Mode Symbolique</strong><br data-rich-text-line-break="true"><strong>Exemple :</strong>u+rwx,g+rw,o+r</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true"><strong>Mode Octal</strong><br data-rich-text-line-break="true"><strong>Exemple :</strong>764 (Utilisateur, Groupe, Autres)</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Utilisateur</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">u</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">&lt;première place&gt;</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Groupe</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">g</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">&lt;place du milieu&gt;</td></tr><tr><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">Autres</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">o</td><td role="textbox" aria-multiline="true" aria-label="Body cell text" class="block-editor-rich-text__editable wp-block-table__cell-content rich-text" style="white-space: pre-wrap; min-width: 1px;" contenteditable="true">&lt;dernière place&gt;</td></tr></tbody><tfoot></tfoot></table>

Vous pourriez être confus 😖. Lisez la suite pour comprendre clairement.

Considérons un scénario.

Vous souhaitez accorder des permissions de lecture, d'écriture et d'exécution aux utilisateurs et une permission de lecture seule pour les groupes et les autres pour le fichier `install.sh`.

Voyons comment faire cela en utilisant les deux méthodes ci-dessus.

### Comment gérer les permissions en mode symbolique

```bash
chmod u+rwx,go+r install.sh
```

Démontons chaque partie et essayons de les comprendre :

* `u+rwx` représente l'ajout des permissions de lecture, d'écriture et d'exécution pour les utilisateurs
* `go+r` représente l'ajout de la permission de lecture pour les groupes et les autres

### Comment gérer les permissions en mode octal

```bash
 chmod 744 install.sh
```

Démontons chacun de ces nombres et essayons de les comprendre :

* Le premier nombre (7) représente la permission pour un utilisateur : 7 = ( 4 (`lecture`) +2 (`écriture`) +1(`exécution`) )
* Le deuxième nombre (4) représente les permissions pour un groupe : 4 (`lecture`)
* Le troisième nombre (4) représente les permissions pour les autres : 4 (`lecture`)

## Quel mode est le meilleur ?

Il s'avère que le mode symbolique est plus puissant que le mode octal.

La raison est que, dans le mode symbolique, nous pouvons masquer les bits de permission que nous voulons changer. Mais dans le mode octal, les modes de permission sont absolus et ne peuvent pas être utilisés pour changer des bits individuels.

## Comment trouver les permissions d'un fichier

Nous pouvons trouver les permissions existantes d'un fichier en utilisant la commande ls.

J'espère que vous connaissez tous la commande `ls`. L'ajout du drapeau `-l` et du nom de fichier avec la commande `ls` montre quelques informations supplémentaires sur le fichier, y compris les permissions.

```bash
ls -l install.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-137.png)
_Commande du terminal pour voir la permission existante d'un fichier_

Regardez la première partie de la sortie (`-rwxrwxrwx`) de la capture d'écran ci-dessus. Explorons ce que cela signifie :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/permissions-1.png)
_Description de la sortie des permissions existantes_

Le premier caractère indique le type d'entrée.

* "-" indique un fichier
* "d" indique un répertoire
* "i" indique un lien (un lien symbolique, qui est un raccourci vers un fichier/répertoire)

Vous regroupez l'ensemble suivant de lettres, à un maximum de 3 pour chaque groupe. Ces groupes représentent les permissions correspondantes pour l'utilisateur, le groupe et les autres.

## Conclusion

Dans cet article, vous avez appris à gérer les permissions de base des fichiers et des dossiers.

J'espère que vous avez apprécié la lecture de ce tutoriel. J'ai une demande à faire à tous : essayez-le vous-même avec des scénarios compliqués comme avoir des permutations et des combinaisons de permissions 😂. Cela sera définitivement utile dans toute votre carrière.

Abonnez-vous à ma newsletter en visitant mon [site](https://5minslearn.gogosoon.com/) et jetez également un coup d'œil à la liste consolidée de tous mes blogs.

Santé !