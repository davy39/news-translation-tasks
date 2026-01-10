---
title: Git Diff et Patch – Guide Complet pour les Développeurs
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2023-02-21T21:42:37.000Z'
originalURL: https://freecodecamp.org/news/git-diff-and-patch
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Git-Diff-and-Patch-for-Developers-Book-Cover--1-.png
tags:
- name: Git
  slug: git
- name: handbook
  slug: handbook
- name: version control
  slug: version-control
seo_title: Git Diff et Patch – Guide Complet pour les Développeurs
seo_desc: 'Many of the interesting processes in Git like merging, rebasing, or even
  committing are based on diffs and patches.

  Developers work with diffs all the time, whether using Git directly or relying on
  the IDE''s diff view. In this post, you will learn wh...'
---

De nombreux processus intéressants dans Git, comme la fusion, le rebasage, ou même la validation, sont basés sur les diffs et les patches.

Les développeurs travaillent avec des diffs tout le temps, qu'ils utilisent Git directement ou qu'ils s'appuient sur la vue de diff de l'IDE. Dans cet article, vous apprendrez ce que sont les diffs et les patches Git, leur structure, et comment appliquer des patches.

Dans [un article précédent](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/), vous avez appris les objets Git. Plus précisément, nous avons discuté qu'un commit est un instantané de l'arborescence de travail à un certain moment, en plus de certaines métadonnées.

Pourtant, il est vraiment difficile de comprendre les commits individuels en regardant l'ensemble de l'arborescence de travail. Plutôt, il est plus utile de regarder comment un commit diffère de son commit parent, c'est-à-dire, la **diff** entre ces commits.

Alors, que veux-je dire quand je dis `diff` ? Commençons par un peu d'histoire.

# Histoire de Git Diff 
ud83d
udcd6

Le `diff` de Git est basé sur l'utilitaire diff des systèmes UNIX. `diff` a été développé au début des années 1970 sur le système d'exploitation Unix. La première version publiée est sortie avec la 5ème édition d'Unix en 1974.

`git diff` est une commande qui prend deux entrées et calcule la différence entre elles. Les entrées peuvent être des commits, mais aussi des fichiers, et même des fichiers qui n'ont jamais été introduits dans le dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-214.png)
_Git diff prend deux entrées, qui peuvent être des commits ou des fichiers (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

C'est important – `git diff` calcule la différence entre deux chaînes de caractères, qui la plupart du temps se trouvent être du code, mais pas nécessairement.

# **Passons à la pratique 
ud83d
de4c
ud83c
udffb**

Vous êtes encouragé à exécuter les commandes vous-même tout en lisant cet article.

Considérez ce fichier texte très court, appelé `file.txt` sur ma machine, qui se compose de 6 lignes :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-158.png)
_`file.txt` se compose de 6 lignes (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Maintenant, modifiez ce fichier un peu. Supprimez la deuxième ligne, et insérez une nouvelle ligne comme quatrième ligne. Ajoutez un `!` à la fin de la dernière ligne, pour obtenir ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-159.png)
_Après avoir modifié `file.txt`, nous obtenons différentes 6 lignes (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Enregistrez ce fichier avec un nouveau nom, disons `new_file.txt`.

Maintenant, nous pouvons exécuter `git diff` pour calculer la différence entre les fichiers comme suit :

`git diff --no-index file.txt new_file.txt`
(Je vais expliquer l'option `--no-index` de cette commande plus tard.)

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-160.png)
_La sortie de `git diff` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Ainsi, la sortie de `git diff` montre beaucoup de choses.

Pour l'instant, concentrez-vous sur la partie commençant par `This is a simple line`. Vous pouvez voir que la ligne ajoutée (`// new test`) est précédée d'un signe `+`. La ligne supprimée est précédée d'un signe `-`.

Intéressamment, notez que Git considère une ligne modifiée comme une séquence de deux changements - effacer une ligne et ajouter une nouvelle ligne à la place. Ainsi, le patch inclut la suppression de la dernière ligne, et l'ajout d'une nouvelle ligne qui est égale à cette ligne, avec l'ajout d'un `!`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-165.png)
_Les lignes d'addition sont précédées par `+`, les lignes de suppression par `-`, et les lignes de modification sont des séquences de suppressions et d'additions (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Les termes `patch` et `diff` sont souvent utilisés de manière interchangeable, bien qu'il y ait une distinction, au moins historiquement.

Un `diff` montre les différences entre deux fichiers, ou instantanés, et peut être assez minimal. Un `patch` est une extension d'un `diff`, augmentée avec des informations supplémentaires telles que les lignes de contexte et les noms de fichiers, ce qui permet de l'appliquer plus largement. C'est un document texte qui décrit comment modifier un fichier ou une base de code existante.

De nos jours, le programme diff Unix, et `git diff`, peuvent produire des patches de divers types.

Un `patch` est une représentation compacte des différences entre deux fichiers. Il décrit comment transformer un fichier en un autre.

C'est-à-dire, si vous appliquez les "instructions" produites par `git diff` sur `file.txt` – c'est-à-dire, supprimer la deuxième ligne, insérer `// new text` comme quatrième ligne, et ajouter un autre `!` à la dernière ligne – vous obtiendriez le contenu de `new_file.txt`.

Une autre chose importante à noter est qu'un patch est asymétrique : le patch de `file.txt` à `new_file.txt` n'est pas le même que le patch pour l'autre direction.

Ainsi, dans cet exemple, générer un `patch` entre `new_file.txt` et `file.txt`, dans cet ordre, signifierait exactement les instructions opposées à celles d'avant - ajouter la deuxième ligne au lieu de la supprimer, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-167.png)
_Un `patch` se compose d'instructions asymétriques pour passer d'un fichier à un autre (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Essayez-le :
`git diff --no-index new_file.txt file.txt`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-169.png)
_L'exécution de `git diff` dans le sens inverse produit les instructions inverses - ajouter une ligne au lieu de la supprimer, et ainsi de suite (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Le format `patch` utilise le contexte, ainsi que les numéros de ligne, pour localiser les régions de fichier différentes. Cela permet à un `patch` d'être appliqué à une version quelque peu antérieure ou ultérieure du premier fichier que celle à partir de laquelle il a été dérivé, tant que le programme d'application peut encore localiser le contexte du changement.

## La Structure d'un Diff 
ud83d
uddd0d

Il est temps de plonger plus profondément 
ud83d
de0e.

Générez un diff de `file.txt` à `new_file.txt` à nouveau, et examinez la sortie plus attentivement :

`git diff --no-index file.txt new_file.txt`

La première ligne introduit les fichiers comparés. Git donne toujours à un fichier le nom `a`, et à l'autre le nom `b`. Donc dans ce cas, `file.txt` est appelé `a`, tandis que `new_file.txt` est appelé `b`.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-170.png)
_La première ligne de la sortie de `diff` introduit les fichiers étant comparés (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Ensuite, la deuxième ligne, commençant par `index`, inclut les SHAs de blob de ces fichiers. Donc même si dans notre cas ils ne sont même pas stockés dans un dépôt Git, Git montre leurs valeurs SHA-1 correspondantes.

Si vous avez besoin d'un rappel sur les blobs en particulier et les objets Git en général, consultez [cet article](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/).

La troisième valeur dans cette ligne, `100644`, est les "bits de mode", indiquant qu'il s'agit d'un fichier "régulier" : non exécutable et non un lien symbolique.

L'utilisation de deux points (`..`) ici entre les SHAs de blob est simplement comme séparateur (contrairement à d'autres cas où il est utilisé dans Git).

D'autres lignes d'en-tête peuvent indiquer les anciens et nouveaux bits de mode s'ils ont changé, les anciens et nouveaux noms de fichiers si le fichier était renommé, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-171.png)
_La deuxième ligne de la sortie de `diff` inclut les SHAs de blob des fichiers comparés, ainsi que les bits de mode (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Les SHAs de blob (également appelés "IDs de blob") sont utiles si ce patch est ensuite appliqué par Git au même projet et qu'il y a des conflits lors de son application.

Après les IDs de blob, nous avons deux lignes : une commençant par des signes `-`, et l'autre par des signes `+`. Il s'agit de l'en-tête traditionnel "unified diff", montrant à nouveau les fichiers comparés et la direction des changements : les signes `-` montrent les lignes dans la version A mais manquantes dans la version B, et les signes `+`, les lignes manquantes dans la version A mais présentes dans la version B.

Si le patch concernait ce fichier ajouté ou supprimé dans son intégralité, alors l'un de ceux-ci serait `/dev/null` pour signaler cela.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-172.png)
_Les signes `-` montrent les lignes dans la version A mais manquantes dans la version B ; et les signes `+`, les lignes manquantes dans la version A mais présentes dans la version B (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Considérez le cas où nous supprimons un fichier :
`rm file.txt`

Et ensuite nous utilisons `git diff` :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-173.png)
_La sortie de `diff` pour un fichier supprimé (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

La version A, représentant l'état de l'index, est actuellement `file.txt`, comparée au répertoire de travail où ce fichier n'existe pas, donc c'est `/dev/null`. Toutes les lignes sont précédées de signes `-` car elles n'existent que dans la version A.

Revenons au diff précédent :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-174.png)
_La sortie de `diff` inclut des sections de changements appelées "hunks" ou "chunks" (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Après cet en-tête de diff unifié, nous arrivons à la partie principale du diff, constituée de "sections de différence", également appelées "hunks" ou "chunks" dans Git.

Notez que ces termes sont utilisés de manière interchangeable, et vous pouvez tomber sur l'un ou l'autre dans la documentation et les tutoriels de Git, ainsi que dans le code source de Git.

Chaque hunk commence par une seule ligne, commençant par deux signes `@`. Ces signes sont suivis d'au plus quatre nombres, puis d'un en-tête pour le chunk - qui est une supposition éclairée par Git qui fonctionne parfois bien.

Habituellement, il inclura le début d'une fonction ou d'une classe, lorsque cela est possible. Dans cet exemple, il n'inclut rien car il s'agit d'un fichier texte, alors considérons un autre exemple pour un moment :

`git diff --no-index example.py example_changed.py`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-175.png)
_Lorsque cela est possible, Git inclut un en-tête pour chaque hunk, par exemple une définition de fonction ou de classe (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Dans l'image ci-dessus, l'en-tête du hunk inclut le début de la fonction qui contient les lignes modifiées - `def example_function(x)`.

Revenons à notre exemple précédent alors :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-174.png)
_Retour au `diff` précédent (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Après les deux signes `@`, vous pouvez trouver quatre nombres.

Les premiers nombres sont précédés d'un signe `-` car ils se réfèrent au `fichier A`. Le premier nombre représente le numéro de ligne correspondant à la première ligne dans le `fichier A` auquel ce hunk se réfère. Dans l'exemple ci-dessus, il est `1`, ce qui signifie que la ligne `This is a simple file` correspond au numéro de ligne `1` dans la version `fichier A`.

Ce nombre est suivi d'une virgule (`,`), puis du nombre de lignes dont ce chunk se compose dans le `fichier A`. Ce nombre inclut toutes les lignes de contexte (les lignes précédées d'un espace dans le diff), ou les lignes marquées avec un signe `-`, car elles font partie du `fichier A`, mais pas les lignes marquées avec un signe `+`, car elles n'existent pas dans le `fichier A`.

Dans l'exemple ci-dessus, ce nombre est `6`, comptant la ligne de contexte `This is a simple file`, la ligne `-` `It has a nice poem:`, puis les trois lignes de contexte, et enfin `Are belong to you`.

Comme vous pouvez le voir, les lignes commençant par un caractère d'espace sont des lignes de contexte, ce qui signifie qu'elles apparaissent comme indiqué dans les deux `fichier A` et `fichier B`.

Ensuite, nous avons un signe `+` pour marquer les deux nombres qui se réfèrent au `fichier B`. D'abord, le numéro de ligne correspondant à la première ligne dans le `fichier B`, suivi du nombre de lignes dont ce chunk se compose - dans le `fichier B`.

Ce nombre inclut toutes les lignes de contexte, ainsi que les lignes marquées avec le signe `+`, car elles font partie du `fichier B`, mais pas les lignes marquées avec un signe `-`.

Après l'en-tête du chunk, nous obtenons les lignes réelles - soit de contexte, `-` ou `+` lignes.

Typiquement et par défaut, un hunk commence et se termine par trois lignes de contexte, au cas où il y aurait bien sûr trois lignes avant et après les lignes modifiées dans le fichier source.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-176.png)
_Le format de patch par `git diff` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

## Comment Produire des diffs 
ud83d
udcf2

L'exemple ci-dessus montre un diff entre les deux fichiers exactement. Un seul fichier de patch peut contenir les différences pour n'importe quel nombre de fichiers, et `git diff` produit des diffs pour tous les fichiers modifiés dans le dépôt en un seul patch.

Souvent, vous verrez la sortie de `git diff` montrant deux versions du *même* fichier et la différence entre elles.

Pour démontrer, considérons ce autre dépôt :

`cd ~/brief-example`

À l'état actuel, le répertoire actif est un dépôt Git, avec un statut propre :

`git status`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-177.png)
_Dans un autre dépôt avec un statut propre (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Prenez un fichier existant, comme celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-178.png)
_Un exemple de fichier - `my_file.py` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Et changez l'une de ses lignes. Par exemple, considérons la deuxième ligne :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-179.png)
_Le contenu de `my_file.py` après avoir modifié la deuxième ligne (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Et exécutez `git diff` :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-180.png)
_La sortie de `git diff` pour `my_file.py` après l'avoir changé (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

La sortie de `git diff` montre la différence entre la version de `my_file.py` dans la zone de staging, qui dans ce cas est la même que le dernier commit (`HEAD`), et dans le répertoire de travail.

J'ai couvert les termes "répertoire de travail", "zone de staging", et "commit" dans [un article précédent](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/), alors consultez-le au cas où vous l'auriez manqué ou si vous souhaitez rafraîchir votre mémoire.

Comme [un rappel](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/), les termes "zone de staging" et "index" sont interchangeables, et les deux sont largement utilisés.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-182.png)
_À cet état, le statut du répertoire de travail est le même que le statut de l'index et celui de `HEAD`. (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Donc, pour voir la différence entre le répertoire de travail et la zone de staging, utilisez `git diff`, sans aucun drapeau supplémentaire.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-181.png)
_Sans options, `git diff` montre la différence entre la zone de staging (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Comme vous pouvez le voir, `git diff` liste ici à la fois `file A` et `file B` pointant vers `my_file.py`. Donc `file A` ici se réfère à la version de `my_file.py` dans la zone de staging, tandis que `file B` se réfère à sa version dans le répertoire de travail.

Notez que si vous modifiez `my_file.py` dans un éditeur de texte, et que vous n'enregistrez pas le fichier, alors `git diff` ne sera pas au courant des changements que vous avez faits, car ils n'ont pas été enregistrés dans le répertoire de travail.

Il y a quelques options que nous pouvons fournir à `git diff` pour obtenir le diff entre le répertoire de travail et un commit spécifique, ou entre la zone de staging et le dernier commit, ou entre deux commits et ainsi de suite.

Tout d'abord, créez un nouveau fichier, `new_file.txt`, et enregistrez-le. Actuellement, le fichier est dans le répertoire de travail, et il est en fait non suivi dans Git.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-183.png)
_Un simple nouveau fichier enregistré sous `new_file.txt` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Maintenant, indexez et validez ce fichier :
`git add new_file.txt`
`git commit -m "new file!"`

Maintenant, l'état de `HEAD` est le même que l'état de la zone de staging, ainsi que de l'arborescence de travail :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-184.png)
_L'état de `HEAD` est le même que celui de l'index et du répertoire de travail (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Ensuite, modifiez `new_file.txt`, en ajoutant une nouvelle ligne au début et une autre nouvelle ligne à la fin :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-185.png)
_Modification de `new_file.txt` en ajoutant une ligne au début et une autre à la fin (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

En conséquence, l'état est le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-186.png)
_Après l'enregistrement, l'état dans le répertoire de travail est différent de celui de l'index ou de `HEAD` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Une astuce intéressante serait d'utiliser `git add -p`, qui vous permet de diviser les changements même au sein d'un fichier, et de considérer ceux que vous souhaitez indexer.

Ainsi, dans ce cas, ajoutez la première ligne à l'index, mais pas la dernière ligne. Pour ce faire, vous pouvez diviser le hunk en utilisant `s`, puis accepter d'indexer le premier hunk (en utilisant `y`), et pas la deuxième partie (en utilisant `n`).

Si vous n'êtes pas sûr de ce que chaque lettre signifie, vous pouvez toujours utiliser `?` et Git vous le dira.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-187.png)
_En utilisant `git add -p`, vous pouvez indexer uniquement le premier changement (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Ainsi, maintenant l'état dans `HEAD` est sans aucune de ces nouvelles lignes. Dans la zone de staging, nous avons la première ligne mais pas la dernière ligne, et dans le répertoire de travail, nous avons les deux nouvelles lignes.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-189.png)
_L'état après avoir indexé uniquement la première ligne (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Si vous utilisez `git diff`, que se passera-t-il ?

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-188.png)
_`git diff` montre la différence entre l'index et le répertoire de travail (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Eh bien, comme indiqué précédemment, vous obtenez le diff entre la zone de staging et l'arborescence de travail.

Que se passe-t-il si vous voulez obtenir le diff entre `HEAD` et la zone de staging ? Pour cela, vous pouvez utiliser `git diff --cached` :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-190.png)
_`git diff --cached` montre la différence entre `HEAD` et l'index (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Et que se passe-t-il si nous voulons la différence entre `HEAD` et l'arborescence de travail ? Pour cela, nous pouvons exécuter `git diff HEAD` :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-191.png)
_`git diff HEAD` montre la différence entre `HEAD` et le répertoire de travail (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Pour résumer les différentes options de `git diff`, voyez ce diagramme auquel vous pouvez vous référer lorsque nécessaire :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-192.png)
_Différentes options pour `git diff` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Pour rappel, au début de cet article, vous avez utilisé `git diff --no-index`. Avec l'option `--no-index`, vous pouvez comparer deux fichiers qui ne font pas partie du dépôt - ou de toute zone de staging.

Maintenant, validez les changements que vous avez dans la zone de staging :

`git commit -m "added a first line"`

Pour observer le diff entre ce commit et son commit parent, vous pouvez exécuter la commande suivante :

`git diff HEAD~1 HEAD`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-194.png)
_La sortie de `git diff HEAD~1 HEAD` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Au fait, nous pouvons omettre le `1` ci-dessus et écrire `HEAD~`, et obtenir le même résultat. Utiliser `1` est la manière explicite de dire que vous faites référence au premier parent du commit.

Notez que l'écriture du commit parent ici, `HEAD~1`, en premier résulte en un diff montrant comment passer du commit parent au commit actuel. Bien sûr, je pourrais également générer le diff inverse en écrivant :

`git diff HEAD HEAD~1`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-195.png)
_La sortie de `git diff HEAD HEAD~1` génère le patch inverse (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-196.png)
_Les différentes options pour `git diff` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Un moyen court de voir le diff entre un commit et son parent est d'utiliser `git show`, par exemple :

`git show HEAD`

C'est la même chose que d'écrire :

`git diff HEAD~ HEAD`

Nous pouvons maintenant mettre à jour notre diagramme :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-197.png)
_Le contenu de `new_file.txt` après avoir utilisé `git reset --hard HEAD~1` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Comme [un rappel](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/), les commits Git sont des instantanés - de l'ensemble du répertoire de travail du dépôt, à un certain moment. Pourtant, il est parfois peu utile de considérer un commit comme un instantané complet, mais plutôt par les changements que ce commit spécifique a introduits. En d'autres termes, par le **diff** entre un commit parent et le commit suivant.

Il est toujours important de se rappeler que Git stocke les instantanés complets, et que le diff est généré dynamiquement à partir des données d'instantané - en comparant les arbres racine du commit et de son parent.

Bien sûr, Git peut comparer n'importe quels deux instantanés dans le temps, pas seulement des commits adjacents, et également générer un diff de fichiers non inclus dans un dépôt.

## Comment Appliquer des Patches 
ud83d
udcaa

En utilisant `git diff`, vous pouvez voir le patch, et vous pouvez ensuite appliquer ce patch en utilisant `git apply`.

### Note historique 
ud83d
udcd4

En fait, le partage de patches était autrefois le principal moyen de partager du code dans les premiers jours de l'open source. Mais maintenant - pratiquement tous les projets sont passés au partage direct de commits Git via des pull requests (appelées "merge requests" sur certaines plateformes).

Le plus gros problème avec l'utilisation de patches est qu'il est difficile d'appliquer un patch lorsque votre répertoire de travail ne correspond pas au commit précédent de l'expéditeur.

La perte de l'historique des commits rend difficile la résolution des conflits. Vous comprendrez mieux cela en plongeant plus profondément dans le processus de `git apply`.

### Une application simple

Que signifie appliquer un patch ? Il est temps de l'essayer !

Prenez la sortie de `git diff` :

`git diff HEAD~1 HEAD`

Et stockez-la dans un fichier :

`git diff HEAD~1 HEAD > my_patch.patch`

Et `reset` pour annuler le dernier commit :

`git reset --hard HEAD~1`

Si vous n'êtes pas complètement à l'aise avec `git reset`, consultez [un article précédent qui le couvrait en profondeur](https://www.freecodecamp.org/news/save-the-day-with-git-reset/). En bref, il nous permet de "réinitialiser" l'état de l'endroit où `HEAD` pointe, ainsi que l'état de l'index et du répertoire de travail.

Dans l'exemple ci-dessus, ils sont tous définis à l'état de `HEAD~1`, ou `Commit 3` dans le diagramme.

Ainsi, après avoir exécuté la commande de réinitialisation, le contenu du fichier est le suivant :

`nano new_file.txt`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-198.png)
_Le patch que vous êtes sur le point d'appliquer, tel que généré par `git diff` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Et nous allons appliquer ce patch :

`nano my_patch.patch`

Ce patch indique à git de trouver les lignes :

```txt
This is a new file
With new content!
```

Qui étaient les lignes `1` et `2`, et d'ajouter une ligne `START` juste au-dessus d'elles.

Exécutez cette commande pour appliquer le patch :

`git apply my_patch.patch`

Et en conséquence, vous obtenez cette version de votre fichier, exactement comme le commit que vous avez créé auparavant :

`nano new_file.txt`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-199.png)
_Le contenu de `new_file.txt` après avoir appliqué le patch (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

## Comprendre les Lignes de Contexte 
ud83e
uddd1
ud83c
udffb
ud83c
udfeb

Pour comprendre l'importance des lignes de contexte, considérons un scénario plus avancé. Que se passe-t-il si les numéros de ligne ont changé depuis que vous avez créé le fichier de patch ? 
ud83e
uddd14

Pour tester, commencez par créer un autre fichier :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-201.png)
_Création d'un autre fichier - `another_file.txt` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Indexez et validez ce fichier :

`git add another_file.txt`

`git commit -m "another file"`

Maintenant, changez ce fichier en ajoutant une nouvelle ligne, et en effaçant également la ligne avant la dernière :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-202.png)
_Changements apportés à `another_file.txt` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Observez la différence entre la version originale du fichier et la version incluant vos changements :

`git diff -- another_file.txt`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-203.png)
_La sortie pour `git diff -- another_file.txt` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

(Utiliser `-- another_file.txt` indique à Git d'exécuter la commande `diff`, en prenant en considération uniquement `another_file.txt`, afin que vous n'obteniez pas le diff pour d'autres fichiers.)

Stockez ce diff dans un fichier de patch :

`git diff -- another_file.txt > new_patch.patch`

Maintenant, réinitialisez votre état à celui avant d'introduire les changements :
`git reset --hard`

Si vous deviez appliquer `new_patch.patch` maintenant, cela fonctionnerait simplement. Considérez un cas plus intéressant.

Modifiez `another_file.txt` à nouveau en ajoutant une nouvelle ligne au début :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-209.png)
_Ajout d'une nouvelle ligne au début de `another_file.txt` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

En conséquence, les numéros de ligne sont différents de la version originale où le patch a été créé. Considérez le patch que vous avez créé auparavant :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-210.png)
_`new_patch.patch` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Il suppose que la ligne `So this is a file` est la première ligne dans `another_file.txt`, ce qui n'est plus le cas. Donc... `git apply` fonctionnera-t-il ?

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-211.png)
_`git apply` n'applique pas le patch (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Eh bien, non. Le patch ne s'applique pas. Mais pourquoi ? Est-ce vraiment à cause du changement dans les numéros de ligne ?

Pour mieux comprendre le processus que Git effectue, vous pouvez ajouter l'option `--verbose` à `git apply`, comme ceci :

`git apply --verbose new_patch.patch`

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-213.png)
_`git apply --verbose` montre le processus que Git suit pour appliquer le patch (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Il semble que Git ait recherché l'ensemble du contenu du fichier, spécifiquement, y compris la ligne `So we are writing an example`, qui n'existe plus dans le fichier. Comme Git ne peut pas trouver cette ligne, il ne peut pas appliquer le patch.

Pourquoi Git recherche-t-il l'ensemble du fichier ? Par défaut, Git recherche `3` lignes de contexte avant et après chaque changement introduit dans le patch. Si vous prenez trois lignes avant et après la ligne ajoutée, et trois lignes avant et après la ligne supprimée (en fait seulement une ligne après, car aucune autre ligne n'existe) - vous obtenez l'ensemble du fichier.

Vous pouvez demander à Git de s'appuyer sur moins de lignes de contexte, en utilisant l'argument `-C`. Par exemple, pour demander à Git de rechercher `1` ligne du contexte environnant, exécutez la commande suivante :

`git apply -C1 new_patch.patch`

Le patch s'applique proprement ! 
ud83c
udf89

Pourquoi cela ? Considérez à nouveau le patch :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-210.png)
_`new_patch.patch` (Source : [Brief](https://www.youtube.com/watch?v=eG9oAroMcPk))_

Lors de l'application du patch avec l'option `-C1`, Git recherche les lignes :

```text
It has some really nice lines
Like this one
```

afin d'ajouter la ligne `!!!This is the new line I am adding!!!` entre ces deux lignes. Ces lignes existent (et, surtout, elles apparaissent l'une juste après l'autre). Donc Git peut ajouter la ligne entre elles avec succès, même si les numéros de ligne ont changé.

De même, Git rechercherait les lignes :

```text
And we are now learning about Git
So we are writing an example
Git is lovely!
```

Comme Git peut trouver ces lignes, Git peut effacer celle du milieu.

Si nous avions changé l'une de ces lignes, par exemple, changé `And we are now learning about Git` en `And we are now learning about patches in Git`, alors Git ne pourrait pas trouver la chaîne ci-dessus, et ainsi le patch ne s'appliquerait pas.

# Récapitulatif

Dans cet article, vous avez appris ce qu'est un diff, et la différence entre un diff et un patch. Vous avez appris comment générer divers patches en utilisant différentes options pour `git diff`.

Vous avez également appris à quoi ressemble la sortie de `git diff`, et comment elle est construite. En fin de compte, vous avez appris comment les patches sont appliqués, et spécifiquement l'importance du contexte.

Comprendre les diffs est une étape majeure pour comprendre de nombreux autres processus dans Git - par exemple, la fusion ou le rebasage.

Dans les tutoriels futurs, vous utiliserez vos connaissances de cet article pour plonger dans ces autres domaines de Git.

# À propos de l'Auteur

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la chaîne YouTube [Brief](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros).

# Références supplémentaires

* [Liste de lecture YouTube sur les Internes de Git par Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7).
* [Article précédent d'Omer sur les internes de Git.](https://www.freecodecamp.org/news/git-internals-objects-branches-create-repo/)