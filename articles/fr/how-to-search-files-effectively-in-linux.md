---
title: Comment rechercher des fichiers efficacement dans le terminal Linux – Guide
  avancé
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-03-06T14:58:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-files-effectively-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/11.-Part-2--How-to-search-files-effectively-in-linux.png
tags:
- name: Linux
  slug: linux
seo_title: Comment rechercher des fichiers efficacement dans le terminal Linux – Guide
  avancé
seo_desc: "Hello everyone! Thanks for your great feedback on my tutorial about the\
  \ basics of the find command. After reading it, many people requested that I write\
  \ a more advanced version about the find command. \nWell, here it is! Now, it's\
  \ time to take your sk..."
---

Bonjour à tous ! Merci pour vos excellents retours sur mon tutoriel concernant les [bases de la commande `find`](https://www.freecodecamp.org/news/how-to-search-files-in-the-linux-terminal/). Après l'avoir lu, beaucoup de personnes ont demandé que j'écrive une version plus avancée sur la commande `find`.

Eh bien, la voici ! Maintenant, il est temps de passer vos compétences au niveau supérieur. Dans cet article, explorons la version plus avancée de la commande `find`.

Si vous découvrez la commande `find` pour la première fois, j'ai couvert les bases de la recherche de fichiers et exploré quelques commandes puissantes pour rechercher des fichiers rapidement sous Linux dans mon précédent tutoriel. Si vous ne l'avez pas lu et n'êtes pas encore familier avec `find`, je vous recommande vivement de [le parcourir](https://www.freecodecamp.org/news/how-to-search-files-in-the-linux-terminal/) et de revenir ici ensuite.

# Comment rechercher des fichiers appartenant à un utilisateur

La commande `find` accepte un argument spécial appelé user que vous pouvez utiliser pour filtrer les fichiers appartenant à un utilisateur.

La syntaxe ressemble à ceci :

```bash
find [path] -user [username] [options]
```

Supposons que vous souhaitiez rechercher tous les fichiers qui m'appartiennent (mon nom d'utilisateur sur cet ordinateur portable est `aruna`). Vous pouvez le faire en utilisant la commande suivante :

```bash
find ./5minslearn/ -user aruna
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-37.png)
_Rechercher des fichiers appartenant à un utilisateur_

La commande ci-dessus listera tous les fichiers appartenant à l'utilisateur `aruna` dans le répertoire `5minslearn`.

Vous avez peut-être remarqué les `[options]` ajoutées à la fin de la syntaxe. Cela signifie simplement que vous pouvez ajouter n'importe quels arguments suivants pour rendre votre recherche un peu plus efficace.

Par exemple, essayons de filtrer uniquement les répertoires qui m'appartiennent. Pour filtrer les répertoires, vous devez ajouter l'option `-type`. Voici la commande pour cela :

```bash
find ./5minslearn/ -type d -user aruna
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-38.png)
_Trouver les répertoires créés par un utilisateur_

D'après la capture d'écran ci-dessus, vous pouvez voir que cette commande liste tous les répertoires et sous-répertoires qui m'appartiennent à l'intérieur du répertoire `5minslearn`.

# Comment rechercher des fichiers ayant des permissions spécifiques

En utilisant l'argument `-perm`, vous pouvez rechercher des fichiers ayant une permission spécifique.

Voici la syntaxe :

```bash
find [path] -perm [permissions] [options]
```

Par exemple, supposons que vous souhaitiez rechercher tous les fichiers ayant une permission en lecture seule dans le répertoire courant. Le code pour les fichiers en lecture seule est `400`.

**Note :** Si vous ne savez pas comment ce code (`400`) est généré et que vous êtes curieux de le savoir, veuillez vous référer à la section `Comment puis-je supprimer des permissions en utilisant le mode octal ?` de mon blog sur les [Permissions de fichiers Linux](https://www.freecodecamp.org/news/file-permissions-in-linux-chmod-command-explained/).

```bash
find . -perm 400
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-39.png)
_Trouver des fichiers avec une permission en lecture seule_

J'ai créé ce fichier `welcome.txt` avec une permission en lecture seule il y a longtemps. Vous pouvez voir sur la capture d'écran ci-dessus que la commande `find` l'a identifié parfaitement.

Je voudrais partager une expérience étrange que j'ai vécue dans ma carrière.

Je travaillais sur un projet contenant un grand nombre de fichiers minifiés (environ 200+). Parmi ceux-ci, je devais trouver tous les fichiers qui n'avaient pas de permission en lecture seule. J'étais assez sûr que ce serait si peu que je pourrais les compter sur les doigts d'une main.

Examiner plus de 200 fichiers pour trouver un maximum de 5 fichiers est un processus chronophage. J'ai donc décidé de trouver une alternative.

J'ai recherché sur Google et j'ai été surpris par le résultat.

J'ai appris que je pouvais faire cela en ajoutant simplement un drapeau `-not` avec la commande `-perm`. Voici la commande pour vous :

```bash
find . -not -perm 400
```

La commande listera tous les fichiers dans le répertoire courant qui n'ont pas de permission en lecture seule.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-40.png)
_Trouver tous les fichiers qui n'ont pas de permission en lecture seule_

L'avantage supplémentaire est que vous pouvez ajouter ce drapeau `-not` avant n'importe quelle option dans la commande `find` pour trouver l'inverse de la requête de recherche.

Voici un autre exemple pour vous :

```bash
find . -not -type f
```

L'exécution de la commande ci-dessus listera tous les éléments qui ne sont pas des fichiers (répertoires, liens symboliques, etc.) dans le répertoire courant.

# Comment rechercher des fichiers appartenant à un groupe particulier

Comme nous l'avons vu dans mon précédent tutoriel sur les permissions de fichiers, il peut y avoir plusieurs personnes qui partagent une machine commune pour leur travail. Elles sont regroupées en tant que Développeurs, QA, et autres.

Alors, que faire si vous souhaitez trouver tous les fichiers que les personnes du groupe `Developers` peuvent voir ? C'est difficile, n'est-ce pas ?

Mais ne vous inquiétez pas. Voici une alternative simple en utilisant la commande `find`.

En utilisant l'argument `-group` dans la commande `find`, vous pouvez rechercher tous les fichiers appartenant à un groupe.

La syntaxe est :

```
find [path] -group [groupname] [options]
```

J'ai un groupe avec mon nom sur ma machine. Essayons de trouver tous les fichiers appartenant à mon groupe.

```bash
find . -group aruna
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-41.png)
_Commande find pour lister tous les fichiers appartenant à un groupe_

Vous pouvez également combiner l'option `-group` avec d'autres options de la commande `find` pour affiner votre recherche.

Par exemple, vous pouvez combiner l'option `-group` avec l'option `-perm` pour rechercher des fichiers appartenant à un groupe et ayant des permissions spécifiques.

```bash
find . -group aruna -perm 400
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-42.png)
_Trouver tous les fichiers appartenant à un groupe avec des permissions en lecture seule_

La commande ci-dessus listera tous les fichiers en lecture seule appartenant au groupe `aruna`.

De même, comme je l'ai mentionné précédemment, vous pouvez également combiner l'option `-group` avec l'option `-not` pour trouver des fichiers qui n'appartiennent pas à un groupe particulier.

Essayons de trouver les fichiers qui n'appartiennent pas au groupe `sudo`.

```bash
find . -not -group sudo
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-43.png)
_Trouver des fichiers qui n'appartiennent pas au groupe `sudo`_

# Comment trouver des fichiers récemment modifiés

L'option `-newer` dans la commande find recherche les fichiers modifiés après la dernière modification du fichier donné.

La syntaxe ressemble à ceci :

```bash
find [path] -newer [reference_file]
```

Par exemple, si vous souhaitez rechercher tous les fichiers modifiés après le fichier `notes.txt`, vous pouvez utiliser la commande suivante :

```
find . -newer notes.txt
```

Cette commande recherchera tous les fichiers dans le répertoire courant qui ont été récemment modifiés après le fichier `notes.txt`.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-44.png)
_Trouver des fichiers récemment modifiés_

# Comment rechercher des fichiers qui ont été accès il y a quelques minutes

Pour rechercher des fichiers qui ont été accès il y a quelques minutes, vous pouvez utiliser l'argument `-amin`. Cet argument acceptera le nombre de minutes (`n`) et trouvera tous les fichiers qui ont été accès `n` minutes auparavant.

La syntaxe est :

```
find [path] -amin [n] [options]
```

Par exemple, essayons de trouver les fichiers qui ont été accès au cours des 30 dernières minutes :

```
find . -amin -30
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-45.png)
_Trouver tous les fichiers qui ont été accès au cours des 30 dernières minutes_

J'espère que vous avez remarqué le signe négatif (moins) avant le nombre. Il indique que le fichier a été accès dans le passé.

# Comment rechercher tous les fichiers vides

Vous pouvez utiliser le drapeau `-empty` dans la commande find pour rechercher des fichiers et des répertoires qui sont vides.

Voici la syntaxe :

```
find [path] -empty [options]
```

Pour rechercher tous les fichiers et répertoires vides, vous pouvez utiliser la commande suivante :

```
find . -empty
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-46.png)
_Trouver tous les fichiers et répertoires vides_

Pour rechercher uniquement les répertoires vides, vous pouvez combiner l'option `-empty` avec l'option `-type` :

```
find . -type d -empty
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-47.png)
_Trouver tous les répertoires vides_

Cette commande listera tous les répertoires vides dans le répertoire courant.

Le drapeau `-empty` peut être combiné avec le drapeau `-delete` pour supprimer tous les fichiers et dossiers vides.

# Comment trouver des fichiers correspondant à une expression régulière spécifique

L'argument `-regex` vous permet d'appliquer un filtre en utilisant des expressions régulières (RegEx).

La syntaxe ressemble à ceci :

```
find [path] -regex [expression] [options]
```

Par exemple, supposons que vous souhaitiez rechercher les fichiers dont les noms commencent par la lettre `w`. Vous pouvez utiliser la commande suivante pour cela :

```
find . -regex "./w.*"
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-48.png)
_Trouver tous les fichiers correspondant à l'expression régulière spécifiée_

# Conclusion

Dans cet article, vous avez appris quelques astuces avancées pour rechercher des fichiers efficacement et effectuer diverses opérations sur eux.

Je vous recommande d'apprendre la commande find en l'essayant. Imaginez quelques scénarios vous-même et essayez de trouver les fichiers en utilisant les techniques que vous avez apprises.

Voici quelques scénarios pour vous :

* Trouver et supprimer des fichiers se terminant par `.txt`
* Trouver des fichiers qui ne vous appartiennent pas
* Trouver des fichiers qui ne correspondent pas à un motif
* Trouver tous les fichiers commençant par `log-` et ayant une taille comprise entre 50 Mo et 100 Mo
* Trouver tous les fichiers appartenant à un groupe et ayant été accès il y a 10 minutes

J'espère que vous avez apprécié la lecture de cet article !

Pour lire d'autres blogs intéressants, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_advanced_find_command_part_2) et suivez-moi sur les réseaux sociaux.