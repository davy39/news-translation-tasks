---
title: Commande Chmod – Comment modifier les permissions de fichiers sous Linux
subtitle: ''
author: Daniel Rosa
co_authors: []
series: null
date: '2022-03-21T15:33:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-file-permissions-with-the-chmod-command-on-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-artem-beliaikin-912005.jpg
tags:
- name: Linux
  slug: linux
seo_title: Commande Chmod – Comment modifier les permissions de fichiers sous Linux
seo_desc: "One of the first commands I learned on Linux was the touch command that\
  \ creates a file using the command line. \nIf you ever try to create, for instance,\
  \ a text file, all you have to do is type touch filename.txt, press Enter, and the\
  \ file is created ..."
---

L'une des premières commandes que j'ai apprises sur Linux était la commande `touch`, qui permet de créer un fichier via la ligne de commande.

Si vous essayez de créer, par exemple, un fichier texte, il vous suffit de taper `touch nomdufichier.txt`, d'appuyer sur Entrée, et le fichier est créé pour vous dans le répertoire où vous vous trouvez. Vous pouvez ensuite y écrire ce que vous voulez en utilisant l'éditeur de fichiers de votre choix.

Cependant, lorsqu'il s'agit de créer des scripts, les choses peuvent devenir un peu plus compliquées. Pourquoi donc ?

Laissez-moi essayer de vous montrer cela avec un autre exemple. Supposons que vous vouliez créer un script en utilisant touch. Tapez `touch exemple.sh`, appuyez sur Entrée, et voilà. Une fois de plus, vous pouvez écrire dedans en utilisant un éditeur de fichiers.

Une fois que tout est prêt, il ne reste plus qu'à le tester. Vous tapez `./sample.sh` et appuyez sur Entrée pour voir votre script en action et... mais quel est ce message ?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-from-2022-03-20-13-58-39.png)

## Pourquoi avons-nous besoin de permissions ?

Je suis l'administrateur ! Comment se fait-il que je n'aie pas la permission d'exécuter un script que j'ai écrit moi-même il y a quelques secondes ?

Il y a en fait une raison à cela – et, pour être honnête, la plupart des utilisateurs devraient en être reconnaissants, car ne pas pouvoir exécuter de scripts sans savoir ce que l'on fait empêche souvent de mettre son système en danger.

Discutons d'abord rapidement des permissions. Nous verrons ensuite comment les modifier.

Afin d'obtenir plus d'informations sur votre fichier, nous utiliserons la commande qui liste les fichiers d'un répertoire : `ls`.

Après avoir tapé `ls` et appuyé sur Entrée, voici ce que nous obtenons dans la ligne de commande :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-from-2022-03-20-14-05-58.png)

Elle liste tous les fichiers visibles dans le répertoire où vous vous trouvez actuellement. En y ajoutant l'option `-l`, elle vous fournit plus d'informations sur les fichiers du répertoire. Voici le résultat lorsque nous tapons `ls -l` et appuyons sur Entrée :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-from-2022-03-20-14-08-00.png)

Nous voyons le(s) même(s) fichier(s), mais avec beaucoup d'informations devant. Pour commencer, nous avons une séquence de dix tirets et lettres qui peuvent sembler dénués de sens au premier abord. Il s'agit en fait de la cartographie des permissions de votre fichier.

Le premier caractère peut être un tiret (`-`, pour un fichier ordinaire), un `d` (pour un répertoire), ou un `l` (pour un lien symbolique). Par souci de simplicité, je me concentrerai sur les fichiers simples, bien que les permissions soient valables pour tous ces types de fichiers/dossiers.

Après le premier caractère, les 9 autres peuvent être divisés en groupes de trois. Le premier trio montre les permissions pour l'utilisateur actuel. Le suivant montre les permissions pour ce groupe. Les trois derniers sont les permissions pour tous les utilisateurs qui n'entrent pas dans cette catégorie.

Pour notre explication, concentrons-nous sur les trois premières permissions, puisque nous ne allons pas changer de groupe ou quoi que ce soit de ce genre.

Le premier trio indique `rw-`.

Il est temps de comprendre ce que c'est. Il y a trois choses que vous pouvez normalement faire avec un fichier : le lire, y écrire et l'exécuter. C'est, fondamentalement, ce que ces lettres signifient.

Le premier `r` signifie la permission de lecture. Ensuite, nous avons `w` pour la permission d'écriture. Enfin, un tiret, ce qui signifie que ce qui devrait être là ne l'est pas. Ce qui devrait être là est un `x`, signifiant eXécutable.

Donc, en parlant de l'utilisateur actuel (moi), les permissions que j'ai pour ce fichier sont les permissions de lecture et d'écriture. Je ne peux cependant pas exécuter le fichier `sample.sh`. C'est pourquoi, en essayant d'exécuter le fichier, j'ai reçu ce message "permission denied" (permission refusée).

Comment puis-je alors exécuter ce fichier ? C'est là que la commande `chmod` entre en jeu.

## Que fait chmod ?

Eh bien, je mentionne les "permissions" depuis le début de l'article. Développons un peu cette explication pour dire qu'il s'agit de "permissions d'accéder à un fichier dans un certain _mode_". Cela signifie que `r` dénote la permission d'accéder au fichier en mode lecture, `w` dénote la permission d'accéder au fichier en mode écriture, et `x` dénote la permission d'accéder au fichier en mode exécutable.

Pourquoi est-ce que je vous dis cela ? À cause de la commande dont traite cet article. `chmod` signifie "change mode" (changer de mode). En d'autres termes, lorsque vous utilisez cette commande, vous changez le mode d'un fichier pour le mode que vous souhaitez utiliser.

## Comment utiliser les opérateurs avec `chmod`

Il est nécessaire d'utiliser un _opérateur_ avec la commande chmod. Il sert à spécifier le type de modification que vous souhaitez apporter aux permissions.

Par exemple, `+` est l'opérateur que vous utilisez pour ajouter une permission à celles que le fichier possède déjà. `-` supprime une permission de la liste. Il existe également l'opérateur `=`, qui réinitialise les permissions afin que vous puissiez les définir à nouveau.

Dans notre cas, en tapant `chmod -w sample.sh`, ce que je demande à la commande de faire est de supprimer la permission d'écriture. Donc, ce que je devrais faire pour ajouter la permission d'exécution est de taper `chmod +x sample.sh`.

Si j'essaie maintenant d'exécuter le fichier, tout ce que j'ai mis dans le script va maintenant être exécuté.

En utilisant `ls -l`, voici ce que j'aurais maintenant.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-from-2022-03-20-14-12-03.png)

## Qui obtient la permission ?

Une autre chose qui mérite d'être soulignée est de savoir qui obtient cette permission. Vous verrez que le "x" est donné à tous les utilisateurs : propriétaire du fichier, groupe et autres. Si ce n'est pas ce que vous recherchez, c'est peut-être une bonne chose de supprimer à nouveau la permission d'exécution avec `chmod -x sample.sh`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-from-2022-03-20-14-16-11.png)

Afin d'activer la permission uniquement pour le propriétaire du fichier (moi, dans ce cas), nous devrions ajouter un "u" avant le "+x", comme ceci :

`chmod u+x sample.sh`

En tapant `ls -l`, voici ce que vous avez :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-from-2022-03-20-14-18-22.png)

Si vous vouliez donner la permission à la fois au propriétaire et à son groupe, alors la commande serait `chmod ug+x sample.sh`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-from-2022-03-20-14-20-25.png)

Génial ! Je pense que cela couvre ce que je voulais vous montrer. Il y a d'autres choses qui pourraient vous intéresser, comme comment utiliser chmod avec des valeurs octales ou binaires pour représenter les permissions. Mais ce sont des modes que nous utilisons pour obtenir les mêmes résultats et je pense que les lettres sont un moyen plus facile d'y parvenir.

Au cas où vous voudriez plus d'informations sur la commande, une chose que vous pouvez faire est de taper `chmod --help`, ce qui vous donnera un aperçu de ce que la commande peut faire. Une description encore plus détaillée peut être obtenue en tapant `man chmod`.

J'espère que cet article vous a été utile. Pour plus d'articles sur les commandes Linux, consultez [freecodecamp.org/news](https://www.freecodecamp.org/news).

Bon code ! 😃