---
title: Le manuel des commandes Linux – Apprendre les commandes Linux pour débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2020-11-03T21:24:38.000Z'
originalURL: https://freecodecamp.org/news/the-linux-commands-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/cover-1.jpg
tags:
- name: Linux
  slug: linux
- name: unix
  slug: unix
seo_title: Le manuel des commandes Linux – Apprendre les commandes Linux pour débutants
seo_desc: 'This Linux Command Handbook will cover 60 core Bash commands you will need
  as a developer. Each command includes example code and tips for when to use it.

  This Linux Command Handbook follows the 80/20 rule: you''ll learn 80% of a topic
  in around 20% o...'
---

Ce manuel des commandes Linux couvrira 60 commandes Bash principales dont vous aurez besoin en tant que développeur. Chaque commande inclut des exemples de code et des conseils sur le moment de l'utiliser.

Ce manuel des commandes Linux suit la règle 80/20 : vous apprendrez 80 % d'un sujet en environ 20 % du temps que vous passez à l'étudier.

Je trouve que cette approche vous donne un aperçu bien équilibré. 

Ce manuel n'essaie pas de couvrir tout ce qui concerne Linux et ses commandes. Il se concentre sur les petites commandes principales que vous utiliserez 80 % ou 90 % du temps, et essaie de simplifier l'utilisation des plus complexes.

Toutes ces commandes fonctionnent sur Linux, macOS, WSL, et partout où vous avez un environnement UNIX.

J'espère que le contenu de ce manuel vous aidera à atteindre ce que vous voulez : **devenir à l'aise avec Linux**.

Vous pouvez mettre cette page en favoris dans votre navigateur afin de pouvoir vous référer à ce manuel à l'avenir.

Et vous pouvez [télécharger ce manuel au format PDF / ePUB / Mobi gratuitement](https://flaviocopes.com/page/linux-commands-handbook/).

Profitez-en !

## Table des matières

- [Introduction à Linux et aux shells](#heading-introduction-a-linux-et-aux-shells)
- [La commande Linux `man`](#heading-la-commande-linux-man)
- [La commande Linux `ls`](#heading-la-commande-linux-ls)
- [La commande Linux `cd`](#heading-la-commande-linux-cd)
- [La commande Linux `pwd`](#heading-la-commande-linux-pwd)
- [La commande Linux `mkdir`](#heading-la-commande-linux-mkdir)
- [La commande Linux `rmdir`](#heading-la-commande-linux-rmdir)
- [La commande Linux `mv`](#heading-la-commande-linux-mv)
- [La commande Linux `cp`](#heading-la-commande-linux-cp)
- [La commande Linux `open`](#heading-la-commande-linux-open)
- [La commande Linux `touch`](#heading-la-commande-linux-touch)
- [La commande Linux `find`](#heading-la-commande-linux-find)
- [La commande Linux `ln`](#heading-la-commande-linux-ln)
- [La commande Linux `gzip`](#heading-la-commande-linux-gzip)
- [La commande Linux `gunzip`](#heading-la-commande-linux-gunzip)
- [La commande Linux `tar`](#heading-la-commande-linux-tar)
- [La commande Linux `alias`](#heading-la-commande-linux-alias)
- [La commande Linux `cat`](#heading-la-commande-linux-cat)
- [La commande Linux `less`](#heading-la-commande-linux-less)
- [La commande Linux `tail`](#heading-la-commande-linux-tail)
- [La commande Linux `wc`](#heading-la-commande-linux-wc)
- [La commande Linux `grep`](#heading-la-commande-linux-grep)
- [La commande Linux `sort`](#heading-la-commande-linux-sort)
- [La commande Linux `uniq`](#heading-la-commande-linux-uniq)
- [La commande Linux `diff`](#heading-la-commande-linux-diff)
- [La commande Linux `echo`](#heading-la-commande-linux-echo)
- [La commande Linux `chown`](#heading-la-commande-linux-chown)
- [La commande Linux `chmod`](#heading-la-commande-linux-chmod)
- [La commande Linux `umask`](#heading-la-commande-linux-umask)
- [La commande Linux `du`](#heading-la-commande-linux-du)
- [La commande Linux `df`](#heading-la-commande-linux-df)
- [La commande Linux `basename`](#heading-la-commande-linux-basename)
- [La commande Linux `dirname`](#heading-la-commande-linux-dirname)
- [La commande Linux `ps`](#heading-la-commande-linux-ps)
- [La commande Linux `top`](#heading-la-commande-linux-top)
- [La commande Linux `kill`](#heading-la-commande-linux-kill)
- [La commande Linux `killall`](#heading-la-commande-linux-killall)
- [La commande Linux `jobs`](#heading-la-commande-linux-jobs)
- [La commande Linux `bg`](#heading-la-commande-linux-bg)
- [La commande Linux `fg`](#heading-la-commande-linux-fg)
- [La commande Linux `type`](#heading-la-commande-linux-type)
- [La commande Linux `which`](#heading-la-commande-linux-which)
- [La commande Linux `nohup`](#heading-la-commande-linux-nohup)
- [La commande Linux `xargs`](#heading-la-commande-linux-xargs)
- [La commande Linux `vim`](#heading-la-commande-linux-vim)
- [La commande Linux `emacs`](#heading-la-commande-linux-emacs)
- [La commande Linux `nano`](#heading-la-commande-linux-nano)
- [La commande Linux `whoami`](#heading-la-commande-linux-whoami)
- [La commande Linux `who`](#heading-la-commande-linux-who)
- [La commande Linux `su`](#heading-la-commande-linux-su)
- [La commande Linux `sudo`](#heading-la-commande-linux-sudo)
- [La commande Linux `passwd`](#heading-la-commande-linux-passwd)
- [La commande Linux `ping`](#heading-la-commande-linux-ping)
- [La commande Linux `traceroute`](#heading-la-commande-linux-traceroute)
- [La commande Linux `clear`](#heading-la-commande-linux-clear)
- [La commande Linux `history`](#heading-la-commande-linux-history)
- [La commande Linux `export`](#heading-la-commande-linux-export)
- [La commande Linux `crontab`](#heading-la-commande-linux-crontab)
- [La commande Linux `uname`](#heading-la-commande-linux-uname)
- [La commande Linux `env`](#heading-la-commande-linux-env)
- [La commande Linux `printenv`](#heading-la-commande-linux-printenv)
- [Conclusion](#heading-conclusion)

## Introduction à Linux et aux shells
### Qu'est-ce que Linux ?

Linux est un système d'exploitation, comme macOS ou Windows.

C'est aussi le système d'exploitation Open Source le plus populaire, et il vous offre beaucoup de liberté.

Il alimente la grande majorité des serveurs qui composent l'Internet. C'est la base sur laquelle tout est construit. Mais pas seulement cela. Android est basé sur (une version modifiée de) Linux.

Le "cœur" de Linux (appelé un *noyau*) est né en 1991 en Finlande, et il a parcouru un long chemin depuis ses modestes débuts. Il est devenu le noyau du système d'exploitation GNU, créant le duo GNU/Linux.

Il y a une chose que les corporations comme Microsoft, Apple et Google ne pourront jamais offrir : la liberté de faire ce que vous voulez avec votre ordinateur.

Elles vont en fait dans la direction opposée, construisant des jardins clos, surtout sur le côté mobile.

Linux est la liberté ultime. 

Il est développé par des bénévoles, certains payés par des entreprises qui en dépendent, d'autres indépendamment. Mais il n'y a pas une seule entreprise commerciale qui puisse dicter ce qui entre dans Linux, ou les priorités du projet.

Vous pouvez également utiliser Linux comme votre ordinateur de tous les jours. J'utilise macOS parce que j'apprécie vraiment les applications et le design (et j'étais aussi un développeur d'applications iOS et Mac). Mais avant d'utiliser macOS, j'utilisais Linux comme système d'exploitation principal de mon ordinateur.

Personne ne peut dicter quelles applications vous pouvez exécuter, ou "appeler à la maison" avec des applications qui vous traquent, votre position, et plus encore.

Linux est également spécial car il n'y a pas seulement "un Linux", comme c'est le cas avec Windows ou macOS. Au lieu de cela, nous avons des **distributions**.

Une "distro" est créée par une entreprise ou une organisation et regroupe le noyau Linux avec des programmes et des outils supplémentaires. 

Par exemple, vous avez Debian, Red Hat et Ubuntu, probablement les distributions les plus populaires. 

Mais beaucoup, beaucoup d'autres existent. Vous pouvez créer votre propre distribution, aussi. Mais le plus probablement, vous utiliserez une distribution populaire qui a beaucoup d'utilisateurs et une communauté de personnes autour d'elle. Cela vous permet de faire ce que vous devez faire sans perdre trop de temps à réinventer la roue et à trouver des réponses à des problèmes courants.

Certains ordinateurs de bureau et portables sont livrés avec Linux préinstallé. Ou vous pouvez l'installer sur votre ordinateur basé sur Windows, ou sur un Mac.

Mais vous n'avez pas besoin de perturber votre ordinateur existant juste pour avoir une idée de comment Linux fonctionne. 

Je n'ai pas d'ordinateur Linux.

Si vous utilisez un Mac, vous devez simplement savoir que sous le capot, macOS est un système d'exploitation UNIX. Il partage beaucoup des mêmes idées et logiciels qu'un système GNU/Linux utilise, car GNU/Linux est une alternative libre à UNIX.

> [UNIX](https://en.wikipedia.org/wiki/Unix) est un terme générique qui regroupe de nombreux systèmes d'exploitation utilisés dans les grandes entreprises et institutions, à partir des années 70

Le terminal macOS vous donne accès aux mêmes commandes exactes que je vais décrire dans le reste de ce manuel.

Microsoft a un [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) officiel que vous pouvez (et devriez !) installer sur Windows. Cela vous donnera la possibilité d'exécuter Linux de manière très facile sur votre PC.

Mais la grande majorité du temps, vous exécuterez un ordinateur Linux dans le cloud via un VPS (Virtual Private Server) comme DigitalOcean.

### Qu'est-ce qu'un shell Linux ?

Un shell est un interpréteur de commandes qui expose une interface à l'utilisateur pour travailler avec le système d'exploitation sous-jacent.

Il vous permet d'exécuter des opérations en utilisant du texte et des commandes, et il fournit aux utilisateurs des fonctionnalités avancées comme la possibilité de créer des scripts.

C'est important : les shells vous permettent de réaliser des choses de manière plus optimisée qu'une interface graphique (GUI) ne pourrait jamais vous le permettre. Les outils en ligne de commande peuvent offrir de nombreuses options de configuration différentes sans être trop complexes à utiliser.

Il existe de nombreux types de shells différents. Cet article se concentre sur les shells Unix, ceux que vous trouverez couramment sur les ordinateurs Linux et macOS.

De nombreux types de shells différents ont été créés pour ces systèmes au fil du temps, et quelques-uns dominent l'espace : Bash, Csh, Zsh, Fish et bien d'autres !

Tous les shells proviennent du Bourne Shell, appelé `sh`. "Bourne" parce que son créateur était Steve Bourne.

Bash signifie *Bourne-again shell*. `sh` était propriétaire et non open source, et Bash a été créé en 1989 pour créer une alternative libre pour le projet GNU et la Free Software Foundation. Puisque les projets devaient payer pour utiliser le Bourne shell, Bash est devenu très populaire.

Si vous utilisez un Mac, essayez d'ouvrir votre terminal Mac. Par défaut, il exécute ZSH (ou, avant Catalina, Bash).

Vous pouvez configurer votre système pour exécuter n'importe quel type de shell – par exemple, j'utilise le shell Fish.

Chaque shell individuel a ses propres fonctionnalités et usages avancés uniques, mais ils partagent tous une fonctionnalité commune : ils peuvent vous permettre d'exécuter des programmes, et ils peuvent être programmés.

Dans le reste de ce manuel, nous verrons en détail les commandes les plus courantes que vous utiliserez.

## La commande Linux `man`

  
La première commande que je vais introduire vous aidera à comprendre toutes les autres commandes.

Chaque fois que je ne sais pas comment utiliser une commande, je tape `man <commande>` pour obtenir le manuel :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-07-04-at-18.42.40.png)

C'est une page de manuel (de __manuel__). Les pages de manuel sont un outil essentiel à apprendre en tant que développeur. Elles contiennent tellement d'informations que parfois c'est presque trop.  
La capture d'écran ci-dessus est juste 1 des 14 écrans d'explication pour la commande `ls`.

La plupart du temps, lorsque j'ai besoin d'apprendre une commande rapidement, j'utilise ce site appelé **tldr pages** : [https://tldr.sh](https://tldr.sh/). C'est une commande que vous pouvez installer, que vous exécutez ensuite comme ceci : `tldr <commande>`. Elle vous donne un aperçu très rapide d'une commande, avec quelques exemples pratiques de scénarios d'utilisation courants :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.35.41.png)

Ce n'est pas un substitut à `man`, mais un outil pratique pour éviter de se perdre dans la grande quantité d'informations présentes dans une page `man`. Ensuite, vous pouvez utiliser la page `man` pour explorer toutes les différentes options et paramètres que vous pouvez utiliser sur une commande.

## La commande Linux `ls`


À l'intérieur d'un dossier, vous pouvez lister tous les fichiers que le dossier contient en utilisant la commande `ls` :

```bash
ls
```

Si vous ajoutez un nom de dossier ou un chemin, il imprimera le contenu de ce dossier :

```bash
ls /bin
```

![Screenshot-2019-02-09-at-18.50.14](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-09-at-18.50.14.png)

`ls` accepte beaucoup d'options. Une de mes combinaisons préférées est `-al`. Essayez-la :

```bash
ls -al /bin
```

![Screenshot-2019-02-09-at-18.49.52](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-09-at-18.49.52.png)

Comparé à la commande `ls` simple, cela retourne beaucoup plus d'informations.

Vous avez, de gauche à droite :

- les permissions du fichier (et si votre système supporte les ACL, vous obtenez un indicateur ACL également)
- le nombre de liens vers ce fichier
- le propriétaire du fichier
- le groupe du fichier
- la taille du fichier en octets
- la date et l'heure de la dernière modification du fichier
- le nom du fichier

Cet ensemble de données est généré par l'option `l`. L'option `a` affiche également les fichiers cachés.

Les fichiers cachés sont des fichiers qui commencent par un point (`.`).


## La commande Linux `cd`

Une fois que vous avez un dossier, vous pouvez vous y déplacer en utilisant la commande `cd`. `cd` signifie **c**hanger de **d**ossier. Vous l'invoquez en spécifiant un dossier dans lequel vous déplacer. Vous pouvez spécifier un nom de dossier, ou un chemin complet.

Exemple :

```bash
mkdir fruits
cd fruits
```

Vous êtes maintenant dans le dossier `fruits`.

Vous pouvez utiliser le chemin spécial `..` pour indiquer le dossier parent :

```bash
cd .. #retour au dossier personnel
```

Le caractère # indique le début du commentaire, qui dure pour toute la ligne après qu'il est trouvé.

Vous pouvez l'utiliser pour former un chemin :

```bash
mkdir fruits
mkdir cars
cd fruits
cd ../cars
```

Il y a un autre indicateur de chemin spécial qui est `.`, et indique le dossier **courant**. 

Vous pouvez également utiliser des chemins absolus, qui commencent à partir du dossier racine `/` :

```bash
cd /etc
```

## La commande Linux `pwd`

Chaque fois que vous vous sentez perdu dans le système de fichiers, appelez la commande `pwd` pour savoir où vous êtes :

```bash
pwd
```

Elle imprimera le chemin du dossier courant.

## La commande Linux `mkdir`


Vous créez des dossiers en utilisant la commande `mkdir` :

```bash
mkdir fruits
```

Vous pouvez créer plusieurs dossiers avec une seule commande :

```bash
mkdir dogs cars
```

Vous pouvez également créer plusieurs dossiers imbriqués en ajoutant l'option `-p` :

```bash
mkdir -p fruits/apples
```

Les options dans les commandes UNIX prennent couramment cette forme. Vous les ajoutez juste après le nom de la commande, et elles changent la manière dont la commande se comporte. Vous pouvez souvent combiner plusieurs options, aussi.

Vous pouvez trouver quelles options une commande supporte en tapant `man <nomdelacommande>`. Essayez maintenant avec `man mkdir` par exemple (appuyez sur la touche `q` pour quitter la page de manuel). Les pages de manuel sont l'aide intégrée incroyable pour UNIX.


## La commande Linux `rmdir`

Tout comme vous pouvez créer un dossier en utilisant `mkdir`, vous pouvez supprimer un dossier en utilisant `rmdir` :

```bash
mkdir fruits
rmdir fruits
```

Vous pouvez également supprimer plusieurs dossiers à la fois :

```bash
mkdir fruits cars
rmdir fruits cars
```

Le dossier que vous supprimez doit être vide.

Pour supprimer des dossiers avec des fichiers à l'intérieur, nous utiliserons la commande plus générique `rm` qui supprime les fichiers et les dossiers, en utilisant l'option `-rf` :

```bash
rm -rf fruits cars
```

Soyez prudent car cette commande ne demande pas de confirmation et elle supprimera immédiatement tout ce que vous lui demandez de supprimer.

Il n'y a pas de **corbeille** lors de la suppression de fichiers depuis la ligne de commande, et la récupération de fichiers perdus peut être difficile.

## La commande Linux `mv`


Une fois que vous avez un fichier, vous pouvez le déplacer en utilisant la commande `mv`. Vous spécifiez le chemin actuel du fichier, et son nouveau chemin :

```bash
touch test
mv pear new_pear
```

Le fichier `pear` est maintenant déplacé vers `new_pear`. C'est ainsi que vous **renommez** les fichiers et les dossiers.

Si le dernier paramètre est un dossier, le fichier situé au premier chemin de paramètre va être déplacé dans ce dossier. Dans ce cas, vous pouvez spécifier une liste de fichiers et ils seront tous déplacés dans le chemin de dossier identifié par le dernier paramètre :

```bash
touch pear
touch apple
mkdir fruits
mv pear apple fruits #pear et apple déplacés dans le dossier fruits
```

## La commande Linux `cp`


Vous pouvez copier un fichier en utilisant la commande `cp` :

```bash
touch test
cp apple another_apple
```

Pour copier des dossiers, vous devez ajouter l'option `-r` pour copier récursivement tout le contenu du dossier :

```bash
mkdir fruits
cp -r fruits cars
```

## La commande Linux `open`


La commande `open` vous permet d'ouvrir un fichier en utilisant cette syntaxe :

```bash
open <nomdefichier>
```

Vous pouvez également ouvrir un répertoire, ce qui sur macOS ouvre l'application Finder avec le répertoire courant ouvert :

```bash
open <nomderepertoire>
```

Je l'utilise tout le temps pour ouvrir le répertoire courant :

```bash
open .
```

> Le symbole spécial `.` pointe vers le répertoire courant, comme `..` pointe vers le répertoire parent

La même commande peut également être utilisée pour exécuter une application :

```bash
open <nomdelapplication>
```

## La commande Linux `touch`


Vous pouvez créer un fichier vide en utilisant la commande `touch` :

```bash
touch apple
```

Si le fichier existe déjà, il ouvre le fichier en mode écriture, et la date de modification du fichier est mise à jour.


## La commande Linux `find`


La commande `find` peut être utilisée pour trouver des fichiers ou des dossiers correspondant à un motif de recherche particulier. Elle recherche de manière récursive.

Apprenons comment l'utiliser par l'exemple.

Trouver tous les fichiers sous l'arborescence actuelle qui ont l'extension `.js` et imprimer le chemin relatif de chaque fichier qui correspond :

```bash
find . -name '*.js'
```

Il est important d'utiliser des guillemets autour des caractères spéciaux comme `*` pour éviter que le shell les interprète.

Trouver les répertoires sous l'arborescence actuelle correspondant au nom "src" :

```bash
find . -type d -name src
```

Utilisez `-type f` pour rechercher uniquement des fichiers, ou `-type l` pour rechercher uniquement des liens symboliques.

`-name` est sensible à la casse. Utilisez `-iname` pour effectuer une recherche insensible à la casse.

Vous pouvez rechercher sous plusieurs arborescences racines :

```bash
find folder1 folder2 -name filename.txt
```

Trouver les répertoires sous l'arborescence actuelle correspondant au nom "node_modules" ou 'public' :

```bash
find . -type d -name node_modules -or -name public
```

Vous pouvez également exclure un chemin en utilisant `-not -path` :

```bash
find . -type d -name '*.md' -not -path 'node_modules/*'
```

Vous pouvez rechercher des fichiers qui contiennent plus de 100 caractères (octets) :

```bash
find . -type f -size +100c
```

Rechercher des fichiers plus grands que 100 Ko mais plus petits que 1 Mo :

```bash
find . -type f -size +100k -size -1M
```

Rechercher des fichiers modifiés il y a plus de 3 jours :

```bash
find . -type f -mtime +3
```

Rechercher des fichiers modifiés dans les dernières 24 heures :

```bash
find . -type f -mtime -1
```

Vous pouvez supprimer tous les fichiers correspondant à une recherche en ajoutant l'option `-delete`. Cela supprime tous les fichiers modifiés dans les dernières 24 heures :

```bash
find . -type f -mtime -1 -delete
```

Vous pouvez exécuter une commande sur chaque résultat de la recherche. Dans cet exemple, nous exécutons `cat` pour imprimer le contenu du fichier :

```bash
find . -type f -exec cat {} \;
```

Remarquez le `\;` final. `{}` est rempli avec le nom du fichier au moment de l'exécution.


## La commande Linux `ln`


La commande `ln` fait partie des commandes du système de fichiers Linux.

Elle est utilisée pour créer des liens. Qu'est-ce qu'un lien ? C'est comme un pointeur vers un autre fichier, ou un fichier qui pointe vers un autre fichier. Vous êtes peut-être familier avec les raccourcis Windows. Ils sont similaires.

Nous avons 2 types de liens : les **liens physiques** et les **liens symboliques**.

#### Liens physiques

Les liens physiques sont rarement utilisés. Ils ont quelques limitations : vous ne pouvez pas lier vers des répertoires, et vous ne pouvez pas lier vers des systèmes de fichiers externes (disques).

Un lien physique est créé en utilisant la syntaxe suivante :

```bash
ln <original> <lien>
```

Par exemple, disons que vous avez un fichier appelé recipes.txt. Vous pouvez créer un lien physique vers celui-ci en utilisant :

```bash
ln recipes.txt newrecipes.txt
```

Le nouveau lien physique que vous avez créé est indistinguishable d'un fichier régulier :

![Screen-Shot-2020-09-02-at-11.26.21](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-02-at-11.26.21.png)

Maintenant, chaque fois que vous éditez l'un de ces fichiers, le contenu sera mis à jour pour les deux.

Si vous supprimez le fichier original, le lien contiendra toujours le contenu du fichier original, car celui-ci n'est pas supprimé tant qu'il y a un lien physique pointant vers lui.

![Screen-Shot-2020-09-02-at-11.26.07](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-02-at-11.26.07.png)

#### Liens symboliques

Les liens symboliques sont différents. Ils sont plus puissants car vous pouvez lier vers d'autres systèmes de fichiers et vers des répertoires. Mais gardez à l'esprit que lorsque l'original est supprimé, le lien sera rompu.

Vous créez des liens symboliques en utilisant l'option `-s` de `ln` :

```bash
ln -s <original> <lien>
```

Par exemple, disons que vous avez un fichier appelé recipes.txt. Vous pouvez créer un lien symbolique vers celui-ci en utilisant :

```bash
ln -s recipes.txt newrecipes.txt
```

Dans ce cas, vous pouvez voir qu'il y a un indicateur spécial `l` lorsque vous listez le fichier en utilisant `ls -al`. Le nom du fichier a un `@` à la fin, et il est également coloré différemment si vous avez les couleurs activées :

![Screen-Shot-2020-09-02-at-11.27.18](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-02-at-11.27.18.png)
Maintenant, si vous supprimez le fichier original, les liens seront rompus, et le shell vous dira "No such file or directory" si vous essayez d'y accéder :

![Screen-Shot-2020-09-02-at-11.27.03](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-02-at-11.27.03.png)

## La commande Linux `gzip`


Vous pouvez compresser un fichier en utilisant le protocole de compression gzip nommé [LZ77](https://en.wikipedia.org/wiki/LZ77_and_LZ78) en utilisant la commande `gzip`.

Voici l'utilisation la plus simple :

```bash
gzip filename
```

Cela compressera le fichier, et ajoutera une extension `.gz` à celui-ci. Le fichier original est supprimé. 

Pour éviter cela, vous pouvez utiliser l'option `-c` et utiliser la redirection de sortie pour écrire la sortie dans le fichier `filename.gz` :

```bash
gzip -c filename > filename.gz
```

> L'option `-c` spécifie que la sortie ira vers le flux de sortie standard, laissant le fichier original intact.

Ou vous pouvez utiliser l'option `-k` :

```bash
gzip -k filename
```

Il existe divers niveaux de compression. Plus la compression est élevée, plus il faudra de temps pour compresser (et décompresser). Les niveaux vont de 1 (le plus rapide, la pire compression) à 9 (le plus lent, la meilleure compression), et le défaut est 6.

Vous pouvez choisir un niveau spécifique avec l'option `-<NUMBER>` :

```bash
gzip -1 filename
```

Vous pouvez compresser plusieurs fichiers en les listant :

```bash
gzip filename1 filename2
```

Vous pouvez compresser tous les fichiers dans un répertoire, de manière récursive, en utilisant l'option `-r` :

```bash
gzip -r a_folder
```

L'option `-v` imprime les informations de pourcentage de compression. Voici un exemple de son utilisation avec l'option `-k` (keep) :

![Screen-Shot-2020-09-09-at-15.55.42](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-15.55.42.png)
`gzip` peut également être utilisé pour décompresser un fichier, en utilisant l'option `-d` :

```bash
gzip -d filename.gz
```

## La commande Linux `gunzip`


La commande `gunzip` est essentiellement équivalente à la commande `gzip`, sauf que l'option `-d` est toujours activée par défaut.

La commande peut être invoquée de cette manière :

```bash
gunzip filename.gz
```

Cela décompressera le fichier et supprimera l'extension `.gz`, en plaçant le résultat dans le fichier `filename`. Si ce fichier existe, il l'écrasera.

Vous pouvez extraire vers un nom de fichier différent en utilisant la redirection de sortie avec l'option `-c` :

```bash
gunzip -c filename.gz > anotherfilename
```

## La commande Linux `tar`


La commande `tar` est utilisée pour créer une archive, en regroupant plusieurs fichiers dans un seul fichier.

Son nom vient du passé et signifie _archive sur bande_ (à l'époque où les archives étaient stockées sur des bandes).

Cette commande crée une archive nommée `archive.tar` avec le contenu de `file1` et `file2` :

```bash
tar -cf archive.tar file1 file2
```

> L'option `c` signifie _créer_. L'option `f` est utilisée pour écrire l'archive dans un fichier.

Pour extraire des fichiers d'une archive dans le dossier courant, utilisez :

```bash
tar -xf archive.tar
```

> l'option `x` signifie _extraire_.

Et pour les extraire dans un répertoire spécifique, utilisez :

```bash
tar -xf archive.tar -C directory
```

Vous pouvez également simplement lister les fichiers contenus dans une archive :

![Screen-Shot-2020-09-09-at-16.56.33](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-16.56.33.png)
`tar` est souvent utilisé pour créer une **archive compressée**, en compressant l'archive avec gzip.

Cela se fait en utilisant l'option `z` :

```bash
tar -czf archive.tar.gz file1 file2
```

C'est comme créer une archive tar, puis exécuter `gzip` dessus.

Pour décompresser une archive gzippée, vous pouvez utiliser `gunzip`, ou `gzip -d`, puis la décompresser. Mais `tar -xf` reconnaîtra qu'il s'agit d'une archive gzippée, et le fera pour vous :

```bash
tar -xf archive.tar.gz
```

## La commande Linux `alias`

Il est courant d'exécuter toujours un programme avec un ensemble d'options que vous aimez utiliser.

Par exemple, prenez la commande `ls`. Par défaut, elle imprime très peu d'informations :

![Screen-Shot-2020-09-03-at-15.21.00](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.21.00.png)

Mais si vous utilisez l'option `-al`, elle imprimera quelque chose de plus utile, y compris la date de modification du fichier, la taille, le propriétaire et les permissions. Elle listera également les fichiers cachés (fichiers commençant par un `.`) :

![Screen-Shot-2020-09-03-at-15.21.08](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.21.08.png)

Vous pouvez créer une nouvelle commande, par exemple j'aime l'appeler `ll`, qui est un alias pour `ls -al`.

Vous le faites comme ceci :

```bash
alias ll='ls -al'
```

Une fois que vous l'avez fait, vous pouvez appeler `ll` comme si c'était une commande UNIX régulière :

![Screen-Shot-2020-09-03-at-15.22.51](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.22.51.png)

Maintenant, appeler `alias` sans aucune option listera les alias définis :

![Screen-Shot-2020-09-03-at-15.30.19](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.30.19.png)
L'alias fonctionnera jusqu'à la fermeture de la session du terminal.

Pour le rendre permanent, vous devez l'ajouter à la configuration du shell. Cela pourrait être `~/.bashrc` ou `~/.profile` ou `~/.bash_profile` si vous utilisez le shell Bash, selon le cas d'utilisation.

Faites attention aux guillemets si vous avez des variables dans la commande : si vous utilisez des guillemets doubles, la variable est résolue au moment de la définition. Si vous utilisez des guillemets simples, elle est résolue au moment de l'invocation. Ces deux cas sont différents :

```bash
alias lsthis="ls $PWD"
alias lscurrent='ls $PWD'
```

\$PWD fait référence au dossier courant dans lequel se trouve le shell. Si vous naviguez maintenant vers un nouveau dossier, `lscurrent` liste les fichiers dans le nouveau dossier, tandis que `lsthis` liste toujours les fichiers dans le dossier où vous étiez lorsque vous avez défini l'alias.


## La commande Linux `cat`


Similaire à [`tail`](https://www.freecodecamp.org/news/unix-command-tail/) à certains égards, nous avons `cat`. Sauf que `cat` peut également ajouter du contenu à un fichier, ce qui le rend super puissant.

Dans son utilisation la plus simple, `cat` imprime le contenu d'un fichier vers la sortie standard :

```bash
cat file
```

Vous pouvez imprimer le contenu de plusieurs fichiers :

```bash
cat file1 file2
```

et en utilisant l'opérateur de redirection de sortie `>` vous pouvez concaténer le contenu de plusieurs fichiers dans un nouveau fichier :

```bash
cat file1 file2 > file3
```

En utilisant `>>` vous pouvez ajouter le contenu de plusieurs fichiers dans un nouveau fichier, en le créant s'il n'existe pas :

```bash
cat file1 file2 >> file3
```

Lorsque vous regardez des fichiers de code source, il est utile de voir les numéros de ligne. Vous pouvez faire en sorte que `cat` les imprime en utilisant l'option `-n` :

```bash
cat -n file1
```

Vous pouvez ajouter un numéro uniquement aux lignes non vides en utilisant `-b`, ou vous pouvez également supprimer toutes les lignes vides multiples en utilisant `-s`.

`cat` est souvent utilisé en combinaison avec l'opérateur pipe `|` pour alimenter le contenu d'un fichier en entrée d'une autre commande : `cat file1 | anothercommand`.

## La commande Linux `less`


La commande `less` est une commande que j'utilise beaucoup. Elle vous montre le contenu stocké à l'intérieur d'un fichier, dans une interface agréable et interactive.

Utilisation : `less <nomdefichier>`.

![Screenshot-2019-02-10-at-09.11.05](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-09.11.05.png)

Une fois que vous êtes dans une session `less`, vous pouvez quitter en appuyant sur `q`.

Vous pouvez naviguer dans le contenu du fichier en utilisant les touches `haut` et `bas`, ou en utilisant la `barre d'espace` et `b` pour naviguer page par page. Vous pouvez également sauter à la fin du fichier en appuyant sur `G` et revenir au début en appuyant sur `g`.

Vous pouvez rechercher du contenu à l'intérieur du fichier en appuyant sur `/` et en tapant un mot à rechercher. Cela recherche _vers l'avant_. Vous pouvez rechercher vers l'arrière en utilisant le symbole `?` et en tapant un mot.

Cette commande visualise simplement le contenu du fichier. Vous pouvez ouvrir directement un éditeur en appuyant sur `v`. Il utilisera l'éditeur système, qui dans la plupart des cas est `vim`.

Appuyer sur la touche `F` entre en _mode suivi_, ou _mode surveillance_. Lorsque le fichier est modifié par quelqu'un d'autre, comme depuis un autre programme, vous pouvez voir les modifications _en direct_. 

Cela ne se produit pas par défaut, et vous ne voyez que la version du fichier au moment où vous l'avez ouvert. Vous devez appuyer sur `ctrl-C` pour quitter ce mode. Dans ce cas, le comportement est similaire à l'exécution de la commande `tail -f <nomdefichier>`.

Vous pouvez ouvrir plusieurs fichiers, et naviguer à travers eux en utilisant `:n` (pour aller au fichier suivant) et `:p` (pour aller au fichier précédent).

## La commande Linux `tail`

Le meilleur cas d'utilisation de tail, à mon avis, est lorsqu'elle est appelée avec l'option `-f`. Elle ouvre le fichier à la fin, et surveille les changements de fichier. 

Chaque fois qu'il y a du nouveau contenu dans le fichier, il est imprimé dans la fenêtre. C'est idéal pour surveiller les fichiers de log, par exemple :

```bash
tail -f /var/log/system.log
```

Pour sortir, appuyez sur `ctrl-C`.

Vous pouvez imprimer les 10 dernières lignes d'un fichier :

```bash
tail -n 10 <nomdefichier>
```

Vous pouvez imprimer tout le contenu du fichier à partir d'une ligne spécifique en utilisant `+` avant le numéro de ligne :

```bash
tail -n +10 <nomdefichier>
```

`tail` peut faire beaucoup plus et comme toujours mon conseil est de vérifier `man tail`.

## La commande Linux `wc`

La commande `wc` nous donne des informations utiles sur un fichier ou une entrée qu'elle reçoit via des pipes.

```bash
echo test >> test.txt
wc test.txt
1       1       5 test.txt
```

Exemple via des pipes, nous pouvons compter la sortie de l'exécution de la commande `ls -al` :

```bash
ls -al | wc
6      47     284
```

La première colonne retournée est le nombre de lignes. La deuxième est le nombre de mots. La troisième est le nombre d'octets.

Nous pouvons lui dire de simplement compter les lignes :

```bash
wc -l test.txt
```

ou simplement les mots :

```bash
wc -w test.txt
```

ou simplement les octets :

```bash
wc -c test.txt
```

Les octets dans les jeux de caractères ASCII équivalent à des caractères. Mais avec les jeux de caractères non ASCII, le nombre de caractères peut différer car certains caractères peuvent prendre plusieurs octets (par exemple, cela se produit en Unicode).

Dans ce cas, le drapeau `-m` vous aidera à obtenir la valeur correcte :

```bash
wc -m test.txt
```

## La commande Linux `grep`

La commande `grep` est un outil très utile. Lorsque vous la maîtrisez, elle vous aidera énormément dans votre codage quotidien.

> Si vous vous demandez, `grep` signifie _global regular expression print_.

Vous pouvez utiliser `grep` pour rechercher dans des fichiers, ou le combiner avec des pipes pour filtrer la sortie d'une autre commande.

Par exemple, voici comment nous pouvons trouver les occurrences de la ligne `document.getElementById` dans le fichier `index.md` :

```bash
grep -n document.getElementById index.md
```

![Screen-Shot-2020-09-04-at-09.42.10](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-09.42.10.png)

En utilisant l'option `-n`, elle affichera les numéros de ligne :

```bash
grep -n document.getElementById index.md
```

![Screen-Shot-2020-09-04-at-09.47.04](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-09.47.04.png)

Une chose très utile est de dire à grep d'imprimer 2 lignes avant et 2 lignes après la ligne correspondante pour vous donner plus de contexte. Cela se fait en utilisant l'option `-C`, qui accepte un nombre de lignes :

```bash
grep -nC 2 document.getElementById index.md
```

![Screen-Shot-2020-09-04-at-09.44.35](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-09.44.35.png)

La recherche est sensible à la casse par défaut. Utilisez le drapeau `-i` pour la rendre insensible à la casse.

Comme mentionné, vous pouvez utiliser grep pour filtrer la sortie d'une autre commande. Nous pouvons reproduire la même fonctionnalité que ci-dessus en utilisant :

```bash
less index.md | grep -n document.getElementById
```
![Screen-Shot-2020-09-04-at-09.43.15](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-09.43.15.png)

La chaîne de recherche peut être une expression régulière, et cela rend `grep` très puissant.

Une autre chose que vous pourriez trouver très utile est d'inverser le résultat, en excluant les lignes qui correspondent à une chaîne particulière, en utilisant l'option `-v` :

![Screen-Shot-2020-09-04-at-09.42.04](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-09.42.04.png)


## La commande Linux `sort`


Supposons que vous avez un fichier texte qui contient les noms de chiens :

![Screen-Shot-2020-09-07-at-07.56.28](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.56.28.png)

Cette liste n'est pas ordonnée.

La commande `sort` vous aide à les trier par nom :

![Screen-Shot-2020-09-07-at-07.57.08](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.57.08.png)

Utilisez l'option `r` pour inverser l'ordre :

![Screen-Shot-2020-09-07-at-07.57.28](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.57.28.png)

Le tri est par défaut sensible à la casse et alphabétique. Utilisez l'option `--ignore-case` pour trier de manière insensible à la casse, et l'option `-n` pour trier en utilisant un ordre numérique.

Si le fichier contient des lignes en double :

![Screen-Shot-2020-09-07-at-07.59.03](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.59.03.png)

Vous pouvez utiliser l'option `-u` pour les supprimer :

![Screen-Shot-2020-09-07-at-07.59.16](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.59.16.png)

`sort` ne fonctionne pas seulement sur les fichiers, comme beaucoup de commandes UNIX le font – il fonctionne également avec les pipes. Vous pouvez donc l'utiliser sur la sortie d'une autre commande. Par exemple, vous pouvez ordonner les fichiers retournés par `ls` avec :

```bash
ls | sort
```

`sort` est très puissant et a beaucoup plus d'options, que vous pouvez explorer en appelant `man sort`.

![Screen-Shot-2020-09-07-at-08.01.27](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.01.27.png)


## La commande Linux `uniq`


`uniq` est une commande qui vous aide à trier les lignes de texte.

Vous pouvez obtenir ces lignes à partir d'un fichier, ou en utilisant des pipes à partir de la sortie d'une autre commande :

```bash
uniq dogs.txt

ls | uniq
```

Vous devez considérer cette chose clé : `uniq` ne détectera que les lignes en double adjacentes.

Cela implique que vous l'utiliserez probablement avec `sort` :

```bash
sort dogs.txt | uniq
```

La commande `sort` a sa propre façon de supprimer les doublons avec l'option `-u` (_unique_). Mais `uniq` a plus de puissance.

Par défaut, elle supprime les lignes en double :

![Screen-Shot-2020-09-07-at-08.39.35](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.39.35.png)

Vous pouvez lui dire d'afficher uniquement les lignes en double, par exemple, avec l'option `-d` :

```bash
sort dogs.txt | uniq -d
```

![Screen-Shot-2020-09-07-at-08.36.50](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.36.50.png)

Vous pouvez utiliser l'option `-u` pour n'afficher que les lignes non dupliquées :

![Screen-Shot-2020-09-07-at-08.38.50](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.38.50.png)

Vous pouvez compter les occurrences de chaque ligne avec l'option `-c` :

![Screen-Shot-2020-09-07-at-08.37.15](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.37.15.png)

Utilisez la combinaison spéciale :

```bash
sort dogs.txt | uniq -c | sort -nr
```

pour ensuite trier ces lignes par les plus fréquentes :

![Screen-Shot-2020-09-07-at-08.37.49](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.37.49.png)


## La commande Linux `diff`

`diff` est une commande pratique. Supposons que vous avez 2 fichiers, qui contiennent presque les mêmes informations, mais vous ne trouvez pas la différence entre les deux.

`diff` traitera les fichiers et vous dira quelle est la différence.

Supposons que vous avez 2 fichiers : `dogs.txt` et `moredogs.txt`. La différence est que `moredogs.txt` contient un nom de chien supplémentaire :

![Screen-Shot-2020-09-07-at-08.55.18](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.55.18.png)

`diff dogs.txt moredogs.txt` vous dira que le deuxième fichier a une ligne supplémentaire, la ligne 3 avec la ligne `Vanille` :

![Screen-Shot-2020-09-07-at-08.56.05](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.56.05.png)

Si vous inversez l'ordre des fichiers, il vous dira que le deuxième fichier manque la ligne 3, dont le contenu est `Vanille` :

![Screen-Shot-2020-09-07-at-08.56.10](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.56.10.png)

En utilisant l'option `-y`, vous comparerez les 2 fichiers ligne par ligne :

![Screen-Shot-2020-09-07-at-08.57.56](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.57.56.png)

L'option `-u` cependant sera plus familière pour vous, car c'est la même utilisée par le système de contrôle de version Git pour afficher les différences entre les versions :

![Screen-Shot-2020-09-07-at-08.58.23](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-08.58.23.png)

Comparer des répertoires fonctionne de la même manière. Vous devez utiliser l'option `-r` pour comparer de manière récursive (en allant dans les sous-répertoires) :

![Screen-Shot-2020-09-07-at-09.01.07](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-09.01.07.png)

Au cas où vous seriez intéressé par les fichiers qui diffèrent, plutôt que par le contenu, utilisez les options `r` et `q` :

![Screen-Shot-2020-09-07-at-09.01.30](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-09.01.30.png)

Il existe de nombreuses autres options que vous pouvez explorer dans la page de manuel en exécutant `man diff` :

![Screen-Shot-2020-09-07-at-09.02.32](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-09.02.32.png)

## La commande Linux `echo`


La commande `echo` fait un travail simple : elle imprime à la sortie l'argument qui lui est passé.

Cet exemple :

```bash
echo "hello"
```

imprimera `hello` dans le terminal.

Nous pouvons ajouter la sortie à un fichier :

```bash
echo "hello" >> output.txt
```

Nous pouvons interpoler des variables d'environnement :

```bash
echo "The path variable is $PATH"
```

![Screen-Shot-2020-09-03-at-15.44.33](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.44.33.png)

Attention, les caractères spéciaux doivent être échappés avec un antislash `\`. Par exemple, le `$` :

![Screen-Shot-2020-09-03-at-15.51.18](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.51.18.png)
Ce n'est que le début. Nous pouvons faire des choses sympas lorsqu'il s'agit d'interagir avec les fonctionnalités du shell.

Nous pouvons afficher les fichiers dans le dossier courant :

```bash
echo *
```

Nous pouvons afficher les fichiers dans le dossier courant qui commencent par la lettre `o` :

```bash
echo o*
```

Toute commande Bash valide (ou tout shell que vous utilisez) et fonctionnalité peut être utilisée ici.

Vous pouvez imprimer le chemin de votre dossier personnel :

```bash
echo ~
```

![Screen-Shot-2020-09-03-at-15.46.36](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.46.36.png)

Vous pouvez également exécuter des commandes, et imprimer le résultat dans la sortie standard (ou dans un fichier, comme vous l'avez vu) :

```bash
echo $(ls -al)
```

![Screen-Shot-2020-09-03-at-15.48.55](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.48.55.png)

Notez que les espaces ne sont pas préservés par défaut. Vous devez envelopper la commande dans des guillemets doubles pour le faire :

![Screen-Shot-2020-09-03-at-15.49.53](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.49.53.png)

Vous pouvez générer une liste de chaînes, par exemple des plages :

```bash
echo {1..5}
```

![Screen-Shot-2020-09-03-at-15.47.19](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-15.47.19.png)


## La commande Linux `chown`

Chaque fichier/répertoire dans un système d'exploitation comme Linux ou macOS (et chaque système UNIX en général) a un **propriétaire**.

Le propriétaire d'un fichier peut tout faire avec celui-ci. Il peut décider du sort de ce fichier.

Le propriétaire (et l'utilisateur `root`) peut également changer le propriétaire pour un autre utilisateur, en utilisant la commande `chown` :

```bash
chown <propriétaire> <fichier>
```

Comme ceci :

```bash
chown flavio test.txt
```

Par exemple, si vous avez un fichier qui appartient à `root`, vous ne pouvez pas écrire dessus en tant qu'autre utilisateur :

![Screen-Shot-2020-09-03-at-18.40.49](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.40.49.png)

Vous pouvez utiliser `chown` pour transférer la propriété à vous :

![Screen-Shot-2020-09-03-at-18.40.58](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.40.58.png)
Il est plutôt courant de devoir changer le propriétaire d'un répertoire, et récursivement tous les fichiers contenus, plus tous les sous-répertoires et les fichiers contenus dans ceux-ci, aussi.

Vous pouvez le faire en utilisant le drapeau `-R` :

```bash
chown -R <propriétaire> <fichier>
```

Les fichiers/répertoires n'ont pas seulement un propriétaire, ils ont aussi un **groupe**. À travers cette commande, vous pouvez changer cela simultanément lorsque vous changez le propriétaire :

```bash
chown <propriétaire>:<groupe> <fichier>
```

Exemple :

```bash
chown flavio:users test.txt
```

Vous pouvez également simplement changer le groupe d'un fichier en utilisant la commande `chgrp` :

```bash
chgrp <groupe> <nomdefichier>
```

## La commande Linux `chmod`

Chaque fichier dans les systèmes d'exploitation Linux / macOS (et les systèmes UNIX en général) a 3 permissions : lire, écrire et exécuter.

Allez dans un dossier, et exécutez la commande `ls -al`.

![Screen-Shot-2020-09-03-at-18.49.22](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.49.22.png)
Les chaînes étranges que vous voyez sur chaque ligne de fichier, comme `drwxr-xr-x`, définissent les permissions du fichier ou du dossier.

Décortiquons cela.

La première lettre indique le type de fichier :

- `-` signifie qu'il s'agit d'un fichier normal
- `d` signifie qu'il s'agit d'un répertoire
- `l` signifie qu'il s'agit d'un lien

Ensuite, vous avez 3 ensembles de valeurs :

- Le premier ensemble représente les permissions du **propriétaire** du fichier
- Le deuxième ensemble représente les permissions des membres du **groupe** auquel le fichier est associé
- Le troisième ensemble représente les permissions de **tous les autres**

Ces ensembles sont composés de 3 valeurs. `rwx` signifie que cette _persona_ spécifique a les permissions de lecture, d'écriture et d'exécution. Tout ce qui est retiré est remplacé par un `-`, ce qui vous permet de former diverses combinaisons de valeurs et de permissions relatives : `rw-`, `r--`, `r-x`, et ainsi de suite.

Vous pouvez changer les permissions données à un fichier en utilisant la commande `chmod`.

`chmod` peut être utilisé de 2 manières. La première consiste à utiliser des arguments symboliques, la seconde à utiliser des arguments numériques. Commençons d'abord par les symboles, qui sont plus intuitifs.

Vous tapez `chmod` suivi d'un espace, et d'une lettre :

- `a` signifie _tous_
- `u` signifie _utilisateur_
- `g` signifie _groupe_
- `o` signifie _autres_

Ensuite, vous tapez soit `+` soit `-` pour ajouter une permission, ou pour la supprimer. Ensuite, vous entrez un ou plusieurs symboles de permission (`r`, `w`, `x`).

Tout cela est suivi du nom du fichier ou du dossier.

Voici quelques exemples :

```bash
chmod a+r filename #tout le monde peut maintenant lire
chmod a+rw filename #tout le monde peut maintenant lire et écrire
chmod o-rwx filename #les autres (ni le propriétaire, ni dans le même groupe que le fichier) ne peuvent pas lire, écrire ou exécuter le fichier
```

Vous pouvez appliquer les mêmes permissions à plusieurs personas en ajoutant plusieurs lettres avant le `+`/`-` :

```bash
chmod og-r filename #les autres et le groupe ne peuvent plus lire
```

Au cas où vous éditez un dossier, vous pouvez appliquer les permissions à chaque fichier contenu dans ce dossier en utilisant le drapeau `-r` (récursif).

Les arguments numériques sont plus rapides mais je les trouve difficiles à retenir lorsque vous ne les utilisez pas tous les jours. Vous utilisez un chiffre qui représente les permissions de la persona. Cette valeur numérique peut être au maximum de 7, et elle est calculée de cette manière :

- `1` si elle a la permission d'exécution
- `2` si elle a la permission d'écriture
- `4` si elle a la permission de lecture

Cela nous donne 4 combinaisons :

- `0` aucune permission
- `1` peut exécuter
- `2` peut écrire
- `3` peut écrire, exécuter
- `4` peut lire
- `5` peut lire, exécuter
- `6` peut lire, écrire
- `7` peut lire, écrire et exécuter

Nous les utilisons par paires de 3, pour définir les permissions de tous les 3 groupes ensemble :

```bash
chmod 777 filename
chmod 755 filename
chmod 644 filename
```

## La commande Linux `umask`

Lorsque vous créez un fichier, vous n'avez pas à décider des permissions à l'avance. Les permissions ont des valeurs par défaut.

Ces valeurs par défaut peuvent être contrôlées et modifiées en utilisant la commande `umask`.

Taper `umask` sans arguments vous montrera le umask actuel, dans ce cas `0022` :

![Screen-Shot-2020-09-04-at-09.04.19](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-09.04.19.png)

Que signifie `0022` ? C'est une valeur octale qui représente les permissions.

Une autre valeur courante est `0002`.

Utilisez `umask -S` pour voir une notation lisible par l'homme :

![Screen-Shot-2020-09-04-at-09.08.18](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-09.08.18.png)
Dans ce cas, l'utilisateur (`u`), propriétaire du fichier, a les permissions de lecture, d'écriture et d'exécution sur les fichiers.

Les autres utilisateurs appartenant au même groupe (`g`) ont les permissions de lecture et d'exécution, de même que tous les autres utilisateurs (`o`).

Dans la notation numérique, nous modifions généralement les 3 derniers chiffres.

Voici une liste qui donne un sens au nombre :

- `0` lire, écrire, exécuter
- `1` lire et écrire
- `2` lire et exécuter
- `3` lire seulement
- `4` écrire et exécuter
- `5` écrire seulement
- `6` exécuter seulement
- `7` aucune permission

Notez que cette notation numérique diffère de celle que nous utilisons dans `chmod`.

Nous pouvons définir une nouvelle valeur pour le masque en définissant la valeur au format numérique :

```bash
umask 002
```

ou vous pouvez changer la permission d'un rôle spécifique :

```bash
umask g+r
```


## La commande Linux `du`

La commande `du` calculera la taille d'un répertoire dans son ensemble :

```bash
du
```

![Screen-Shot-2020-09-04-at-08.11.30](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-08.11.30.png)

Le nombre `32` ici est une valeur exprimée en octets.

L'exécution de `du *` calculera la taille de chaque fichier individuellement :

![Screen-Shot-2020-09-04-at-08.12.35](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-08.12.35.png)

Vous pouvez configurer `du` pour afficher les valeurs en mégaoctets en utilisant `du -m`, et en gigaoctets en utilisant `du -g`.

L'option `-h` affichera une notation lisible par l'homme pour les tailles, en s'adaptant à la taille :

![Screen-Shot-2020-09-04-at-08.14.40](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-08.14.40.png)

L'ajout de l'option `-a` imprimera la taille de chaque fichier dans les répertoires, également :

![Screen-Shot-2020-09-04-at-08.20.12](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-08.20.12.png)

Une chose pratique est de trier les répertoires par taille :

```bash
du -h <répertoire> | sort -nr
```

et ensuite rediriger vers `head` pour obtenir uniquement les 10 premiers résultats :

![Screen-Shot-2020-09-04-at-08.22.25](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-08.22.25.png)


## La commande Linux `df`

La commande `df` est utilisée pour obtenir des informations sur l'utilisation du disque.

Sa forme de base imprimera des informations sur les volumes montés :

![Screen-Shot-2020-09-08-at-08.40.39](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-08-at-08.40.39.png)

L'utilisation de l'option `-h` (`df -h`) affichera ces valeurs dans un format lisible par l'homme :

![Screen-Shot-2020-09-08-at-08.40.50](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-08-at-08.40.50.png)

Vous pouvez également spécifier un nom de fichier ou de répertoire pour obtenir des informations sur le volume spécifique sur lequel il se trouve :

![Screen-Shot-2020-09-08-at-08.41.27](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-08-at-08.41.27.png)


## La commande Linux `basename`

Supposons que vous avez un chemin vers un fichier, par exemple `/Users/flavio/test.txt`.

En exécutant

```bash
basename /Users/flavio/test.txt
```

vous obtiendrez la chaîne `test.txt` :

![Screen-Shot-2020-09-10-at-08.27.52](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-10-at-08.27.52.png)

Si vous exécutez `basename` sur une chaîne de chemin qui pointe vers un répertoire, vous obtiendrez le dernier segment du chemin. Dans cet exemple, `/Users/flavio` est un répertoire :

![Screen-Shot-2020-09-10-at-08.28.11](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-10-at-08.28.11.png)


## La commande Linux `dirname`

Supposons que vous avez un chemin vers un fichier, par exemple `/Users/flavio/test.txt`.

En exécutant

```bash
dirname /Users/flavio/test.txt
```

vous obtiendrez la chaîne `/Users/flavio` :

![Screen-Shot-2020-09-10-at-08.31.08-1](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-10-at-08.31.08-1.png)

## La commande Linux `ps`

Votre ordinateur exécute des tonnes de processus différents en permanence.

Vous pouvez les inspecter tous en utilisant la commande `ps` :

![Screen-Shot-2020-09-02-at-12.25.08](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-02-at-12.25.08.png)

C'est la liste des processus initiés par l'utilisateur actuellement en cours d'exécution dans la session actuelle.

Ici, j'ai quelques instances du shell `fish`, principalement ouvertes par VS Code à l'intérieur de l'éditeur, et une instance de Hugo exécutant l'aperçu de développement d'un site.

Ce ne sont que les commandes assignées à l'utilisateur actuel. Pour lister **tous** les processus, nous devons passer quelques options à `ps`.

La plus courante que j'utilise est `ps ax` :

![Screen-Shot-2020-09-02-at-12.26.00](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-02-at-12.26.00.png)

> L'option `a` est utilisée pour lister également les processus des autres utilisateurs, pas seulement les vôtres. `x` montre les processus non liés à un terminal (non initiés par les utilisateurs via un terminal).

Comme vous pouvez le voir, les commandes les plus longues sont coupées. Utilisez la commande `ps axww` pour continuer la liste des commandes sur une nouvelle ligne au lieu de la couper :

![Screen-Shot-2020-09-02-at-12.30.22](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-02-at-12.30.22.png)

> Nous devons spécifier `w` 2 fois pour appliquer ce paramètre (ce n'est pas une faute de frappe).

Vous pouvez rechercher un processus spécifique en combinant `grep` avec un pipe, comme ceci :

```bash
ps axww | grep "Visual Studio Code"
```

![Screen-Shot-2020-09-02-at-12.33.45](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-02-at-12.33.45.png)
Les colonnes retournées par `ps` représentent certaines informations clés.

La première information est `PID`, l'identifiant du processus. C'est la clé lorsque vous voulez référencer ce processus dans une autre commande, par exemple pour le tuer.

Ensuite, nous avons `TT` qui nous indique l'identifiant du terminal utilisé.

Ensuite, `STAT` nous indique l'état du processus :

`I` un processus qui est inactif (en sommeil depuis plus de 20 secondes environ)
`R` un processus exécutable
`S` un processus qui est en sommeil depuis moins de 20 secondes environ
`T` un processus arrêté
`U` un processus en attente ininterruptible
`Z` un processus mort (un _zombie_)

Si vous avez plus d'une lettre, la deuxième représente des informations supplémentaires, qui peuvent être très techniques.

Il est courant d'avoir `+` qui indique que le processus est au premier plan dans son terminal. `s` signifie que le processus est un [leader de session](https://unix.stackexchange.com/questions/18166/what-are-session-leaders-in-ps).

`TIME` nous indique depuis combien de temps le processus est en cours d'exécution.


## La commande Linux `top`

La commande `top` est utilisée pour afficher des informations dynamiques en temps réel sur les processus en cours d'exécution dans le système.

C'est vraiment pratique pour comprendre ce qui se passe.

Son utilisation est simple – vous tapez simplement `top`, et le terminal sera entièrement immergé dans cette nouvelle vue :

![Screen-Shot-2020-09-03-at-11.39.53](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-11.39.53.png)
Le processus est de longue durée. Pour quitter, vous pouvez taper la lettre `q` ou `ctrl-C`.

Il y a beaucoup d'informations qui nous sont données : le nombre de processus, combien sont en cours d'exécution ou en sommeil, la charge du système, l'utilisation du CPU, et bien plus encore.

En dessous, la liste des processus utilisant le plus de mémoire et de CPU est constamment mise à jour.

Par défaut, comme vous pouvez le voir dans la colonne `%CPU` mise en évidence, ils sont triés par le CPU utilisé.

Vous pouvez ajouter un drapeau pour trier les processus par mémoire utilisée :

```bash
top -o mem
```

## La commande Linux `kill`

Les processus Linux peuvent recevoir des **signaux** et réagir à ceux-ci.

C'est une façon dont nous pouvons interagir avec les programmes en cours d'exécution.

Le programme `kill` peut envoyer une variété de signaux à un programme.

Il n'est pas seulement utilisé pour terminer un programme, comme le suggère le nom, mais c'est son travail principal.

Nous l'utilisons de cette manière :

```bash
kill <PID>
```

Par défaut, cela envoie le signal `TERM` à l'identifiant de processus spécifié.

Nous pouvons utiliser des drapeaux pour envoyer d'autres signaux, y compris :

```bash
kill -HUP <PID>
kill -INT <PID>
kill -KILL <PID>
kill -TERM <PID>
kill -CONT <PID>
kill -STOP <PID>
```

`HUP` signifie **hang up**. Il est envoyé automatiquement lorsqu'une fenêtre de terminal qui a démarré un processus est fermée avant la terminaison du processus.

`INT` signifie **interrupt**, et il envoie le même signal utilisé lorsque nous appuyons sur `ctrl-C` dans le terminal, ce qui termine généralement le processus.

`KILL` n'est pas envoyé au processus, mais au noyau du système d'exploitation, qui arrête et termine immédiatement le processus.

`TERM` signifie **terminate**. Le processus le recevra et se terminera lui-même. C'est le signal par défaut envoyé par `kill`.

`CONT` signifie **continue**. Il peut être utilisé pour reprendre un processus arrêté.

`STOP` n'est pas envoyé au processus, mais au noyau du système d'exploitation, qui arrête immédiatement (mais ne termine pas) le processus.

Vous pourriez voir des nombres utilisés à la place, comme `kill -1 <PID>`. Dans ce cas,

`1` correspond à `HUP`.
`2` correspond à `INT`.
`9` correspond à `KILL`.
`15` correspond à `TERM`.
`18` correspond à `CONT`.
`15` correspond à `STOP`.

## La commande Linux `killall`

Similaire à la commande `kill`, `killall` enverra le signal à plusieurs processus à la fois au lieu d'envoyer un signal à un identifiant de processus spécifique.

Voici la syntaxe :

```bash
killall <nom>
```

où `nom` est le nom d'un programme. Par exemple, vous pouvez avoir plusieurs instances du programme `top` en cours d'exécution, et `killall top` les terminera toutes.

Vous pouvez spécifier le signal, comme avec `kill` (et vérifier le tutoriel `kill` pour en savoir plus sur les types spécifiques de signaux que nous pouvons envoyer), par exemple :

```bash
killall -HUP top
```

## La commande Linux `jobs`

Lorsque nous exécutons une commande sous Linux / macOS, nous pouvons la configurer pour qu'elle s'exécute en arrière-plan en utilisant le symbole `&` après la commande.

Par exemple, nous pouvons exécuter `top` en arrière-plan :

```bash
top &
```

C'est très pratique pour les programmes de longue durée.

Nous pouvons revenir à ce programme en utilisant la commande `fg`. Cela fonctionne bien si nous n'avons qu'un seul travail en arrière-plan, sinon nous devons utiliser le numéro de travail : `fg 1`, `fg 2` et ainsi de suite.

Pour obtenir le numéro de travail, nous utilisons la commande `jobs`.

Supposons que nous exécutons `top &` puis `top -o mem &`, donc nous avons 2 instances de top en cours d'exécution. `jobs` nous dira ceci :

![Screen-Shot-2020-09-03-at-11.49.42](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-11.49.42.png)
Maintenant, nous pouvons revenir à l'un de ceux-ci en utilisant `fg <jobid>`. Pour arrêter le programme à nouveau, nous pouvons appuyer sur `cmd-Z`.

L'exécution de `jobs -l` imprimera également l'identifiant de processus de chaque travail.


## La commande Linux `bg`

Lorsque vous exécutez une commande, vous pouvez la suspendre en utilisant `ctrl-Z`.

La commande s'arrêtera immédiatement, et vous reviendrez au terminal shell.

Vous pouvez reprendre l'exécution de la commande en arrière-plan, afin qu'elle continue de s'exécuter mais qu'elle ne vous empêche pas de faire d'autres travaux dans le terminal.

Dans cet exemple, j'ai 2 commandes arrêtées :

![Screen-Shot-2020-09-03-at-16.06.18](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-16.06.18.png)
Je peux exécuter `bg 1` pour reprendre en arrière-plan l'exécution du travail #1.

J'aurais également pu dire `bg` sans aucune option, car par défaut il choisit le travail #1 dans la liste.

## La commande Linux `fg`

Lorsque vous exécutez une commande en arrière-plan, parce que vous l'avez démarrée avec `&` à la fin (exemple : `top &` ou parce que vous l'avez mise en arrière-plan avec la commande `bg`), vous pouvez la mettre au premier plan en utilisant `fg`.

L'exécution de

```bash
fg
```

reprendra au premier plan le dernier travail qui a été suspendu.

Vous pouvez également spécifier quel travail vous souhaitez reprendre au premier plan en passant le numéro de travail, que vous pouvez obtenir en utilisant la commande `jobs`.

![Screen-Shot-2020-09-03-at-16.12.46](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-16.12.46.png)

L'exécution de `fg 2` reprendra le travail #2 :

![Screen-Shot-2020-09-03-at-16.12.54](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-16.12.54.png)


## La commande Linux `type`

Une commande peut être de l'un de ces 4 types :

- un exécutable
- un programme intégré au shell
- une fonction shell
- un alias

La commande `type` peut aider à déterminer cela, au cas où nous voulons le savoir ou sommes simplement curieux. Elle vous dira comment la commande sera interprétée.

La sortie dépendra du shell utilisé. Voici Bash :

![Screen-Shot-2020-09-03-at-16.32.50](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-16.32.50.png)

Voici Zsh :

![Screen-Shot-2020-09-03-at-16.32.57](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-16.32.57.png)

Voici Fish :

![Screen-Shot-2020-09-03-at-16.33.06](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-16.33.06.png)
L'une des choses les plus intéressantes ici est que pour les alias, elle vous dira ce qu'il alias. Vous pouvez voir l'alias `ll`, dans le cas de Bash et Zsh, mais Fish le fournit par défaut, donc il vous dira qu'il s'agit d'une fonction shell intégrée.


## La commande Linux `which`

Supposons que vous avez une commande que vous pouvez exécuter, car elle est dans le chemin du shell, mais vous voulez savoir où elle est située.

Vous pouvez le faire en utilisant `which`. La commande retournera le chemin vers la commande spécifiée :

![Screen-Shot-2020-09-03-at-17.22.47](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-17.22.47.png)
`which` ne fonctionnera que pour les exécutables stockés sur le disque, pas pour les alias ou les fonctions shell intégrées.

## La commande Linux `nohup`

Parfois, vous devez exécuter un processus de longue durée sur une machine distante, puis vous devez vous déconnecter.

Ou vous voulez simplement empêcher la commande d'être interrompue s'il y a un problème de réseau entre vous et le serveur.

La façon de faire en sorte qu'une commande s'exécute même après vous être déconnecté ou avoir fermé la session sur un serveur est d'utiliser la commande `nohup`.

Utilisez `nohup <commande>` pour permettre au processus de continuer à fonctionner même après vous être déconnecté.

## La commande Linux `xargs`

La commande `xargs` est utilisée dans un shell UNIX pour convertir l'entrée de l'entrée standard en arguments pour une commande.

En d'autres termes, grâce à l'utilisation de `xargs`, la sortie d'une commande est utilisée comme entrée d'une autre commande.

Voici la syntaxe que vous utiliserez :

```bash
commande1 | xargs commande2
```

Nous utilisons un pipe (`|`) pour passer la sortie à `xargs`. Cela prendra soin d'exécuter la commande `commande2`, en utilisant la sortie de `commande1` comme ses arguments.

Faisons un exemple simple. Vous voulez supprimer certains fichiers spécifiques d'un répertoire. Ces fichiers sont listés à l'intérieur d'un fichier texte.

Nous avons 3 fichiers : `file1`, `file2`, `file3`.

Dans `todelete.txt`, nous avons une liste de fichiers que nous voulons supprimer, dans cet exemple `file1` et `file3` :

![Screen-Shot-2020-09-08-at-07.45.28](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-08-at-07.45.28.png)

Nous allons canaliser la sortie de `cat todelete.txt` vers la commande `rm`, via `xargs`.

De cette manière :

```bash
cat todelete.txt | xargs rm
```

C'est le résultat, les fichiers que nous avons listés sont maintenant supprimés :

![Screen-Shot-2020-09-08-at-07.46.39](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-08-at-07.46.39.png)

La façon dont cela fonctionne est que `xargs` exécutera `rm` 2 fois, une pour chaque ligne retournée par `cat`.

C'est l'utilisation la plus simple de `xargs`. Il existe plusieurs options que nous pouvons utiliser.

L'une des plus utiles, à mon avis (surtout lorsque l'on commence à apprendre `xargs`), est `-p`. L'utilisation de cette option fera en sorte que `xargs` imprime une invite de confirmation avec l'action qu'il va entreprendre :

![Screen-Shot-2020-09-08-at-08.19.09](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-08-at-08.19.09.png)

L'option `-n` vous permet de dire à `xargs` d'effectuer une itération à la fois, afin que vous puissiez les confirmer individuellement avec `-p`. Ici, nous disons à `xargs` d'effectuer une itération à la fois avec `-n1` :

![Screen-Shot-2020-09-08-at-08.32.58](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-08-at-08.32.58.png)

L'option `-I` est une autre option largement utilisée. Elle vous permet d'obtenir la sortie dans un espace réservé, puis vous pouvez faire diverses choses.

L'une d'entre elles est d'exécuter plusieurs commandes :

```bash
commande1 | xargs -I % /bin/bash -c 'commande2 %; commande3 %'
```

![Screen-Shot-2020-09-08-at-08.35.37](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-08-at-08.35.37.png)
> Vous pouvez échanger le symbole `%` que j'ai utilisé ci-dessus avec n'importe quoi d'autre – c'est une variable.


## La commande Linux `vim`

`vim` est un éditeur de fichiers **très** populaire, surtout parmi les programmeurs. Il est activement développé et fréquemment mis à jour, et il y a une grande communauté autour de lui. Il y a même une [conférence Vim](https://vimconf.org/) !

`vi` dans les systèmes modernes est juste un alias pour `vim`, ce qui signifie `vi` i`m`proved.

Vous le démarrez en exécutant `vi` sur la ligne de commande.

![Screenshot-2019-02-10-at-11.44.36](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-11.44.36.png)

Vous pouvez spécifier un nom de fichier au moment de l'invocation pour éditer ce fichier spécifique :

```bash
vi test.txt
```

![Screenshot-2019-02-10-at-11.36.21](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-11.36.21.png)

Vous devez savoir que Vim a 2 modes principaux :

- le mode _commande_ (ou _normal_)
- le mode _insertion_

Lorsque vous démarrez l'éditeur, vous êtes en mode commande. Vous ne pouvez pas entrer de texte comme vous vous y attendez avec un éditeur basé sur une interface graphique. Vous devez entrer en **mode insertion**. 

Vous pouvez le faire en appuyant sur la touche `i`. Une fois que vous le faites, le mot `-- INSERT --` apparaît en bas de l'éditeur :

![Screenshot-2019-02-10-at-11.47.39](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-11.47.39.png)

Maintenant, vous pouvez commencer à taper et remplir l'écran avec le contenu du fichier :

![Screenshot-2019-02-10-at-11.48.39](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-11.48.39.png)

Vous pouvez vous déplacer dans le fichier avec les touches fléchées, ou en utilisant les touches `h` - `j` - `k` - `l`. `h-l` pour gauche-droite, `j-k` pour bas-haut.

Une fois que vous avez terminé l'édition, vous pouvez appuyer sur la touche `esc` pour quitter le mode insertion et revenir au **mode commande**.

![Screenshot-2019-02-10-at-11.48.44](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-11.48.44.png)
À ce stade, vous pouvez naviguer dans le fichier, mais vous ne pouvez pas ajouter de contenu (et faites attention aux touches que vous appuyez, car elles pourraient être des commandes).

Une chose que vous pourriez vouloir faire maintenant est **sauvegarder le fichier**. Vous pouvez le faire en appuyant sur `:` (deux-points), puis `w`.

Vous pouvez **sauvegarder et quitter** en appuyant sur `:` puis `w` et `q` : `:wq`

Vous pouvez **quitter sans sauvegarder** en appuyant sur `:` puis `q` et `!` : `:q!`

Vous pouvez **annuler** et éditer en allant en mode commande et en appuyant sur `u`. Vous pouvez **rétablir** (annuler une annulation) en appuyant sur `ctrl-r`.

Ce sont les bases du travail avec Vim. À partir de là commence un terrier de lapin dans lequel nous ne pouvons pas entrer dans cette petite introduction.

Je ne mentionnerai que ces commandes qui vous permettront de commencer à éditer avec Vim :

- appuyer sur la touche `x` supprime le caractère actuellement mis en surbrillance
- appuyer sur `A` va à la fin de la ligne actuellement sélectionnée
- appuyer sur `0` pour aller au début de la ligne
- aller au premier caractère d'un mot et appuyer sur `d` suivi de `w` pour supprimer ce mot. Si vous le suivez avec `e` au lieu de `w`, l'espace blanc avant le mot suivant est préservé
- utiliser un nombre entre `d` et `w` pour supprimer plus d'un mot, par exemple utiliser `d3w` pour supprimer 3 mots vers l'avant
- appuyer sur `d` suivi de `d` pour supprimer une ligne entière. Appuyer sur `d` suivi de `$` pour supprimer toute la ligne à partir de l'endroit où se trouve le curseur, jusqu'à la fin

Pour en savoir plus sur Vim, je peux recommander le [FAQ Vim](https://vimhelp.org/vim_faq.txt.html). Vous pouvez également exécuter la commande `vimtutor`, qui devrait déjà être installée dans votre système et qui vous aidera grandement à commencer votre exploration de `vim`.

## La commande Linux `emacs`

`emacs` est un éditeur génial et il est historiquement considéré comme _l'_éditeur pour les systèmes UNIX. Famously, les guerres de flammes et les discussions animées `vi` vs `emacs` ont causé de nombreuses heures improductives pour les développeurs du monde entier.

`emacs` est très puissant. Certaines personnes l'utilisent toute la journée comme une sorte de système d'exploitation (https://news.ycombinator.com/item?id=19127258). Nous allons juste parler des bases ici.

Vous pouvez ouvrir une nouvelle session emacs simplement en invoquant `emacs` :

![Screenshot-2019-02-10-at-12.14.18](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-12.14.18.png)

> Utilisateurs de macOS, arrêtez-vous un instant maintenant. Si vous êtes sur Linux, il n'y a pas de problèmes, mais macOS ne livre pas d'applications utilisant GPLv3, et chaque commande UNIX intégrée qui a été mise à jour vers GPLv3 n'a pas été mise à jour. 
> 
> Bien qu'il y ait un petit problème avec les commandes que j'ai listées jusqu'à présent, dans ce cas, utiliser une version d'emacs de 2007 n'est pas exactement la même chose que d'utiliser une version avec 12 ans d'améliorations et de changements. 
> 
> Ce n'est pas un problème avec Vim, qui est à jour. Pour corriger cela, exécutez `brew install emacs` et l'exécution de `emacs` utilisera la nouvelle version de Homebrew (assurez-vous d'avoir [Homebrew](https://flaviocopes.com/homebrew/) installé).

Vous pouvez également éditer un fichier existant en appelant `emacs <nomdefichier>` :

![Screenshot-2019-02-10-at-13.12.49](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-13.12.49.png)

Vous pouvez maintenant commencer à éditer. Une fois que vous avez terminé, appuyez sur `ctrl-x` suivi de `ctrl-w`. Vous confirmez le dossier :

![Screenshot-2019-02-10-at-13.14.29](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-13.14.29.png)

et Emacs vous dit que le fichier existe, vous demandant s'il doit l'écraser :

![Screenshot-2019-02-10-at-13.14.32](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-13.14.32.png)

Répondez `y`, et vous obtenez une confirmation de succès :

![Screenshot-2019-02-10-at-13.14.35](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-13.14.35.png)
Vous pouvez quitter Emacs en appuyant sur `ctrl-x` suivi de `ctrl-c`.
Ou `ctrl-x` suivi de `c` (en gardant `ctrl` enfoncé).

Il y a beaucoup de choses à savoir sur Emacs, certainement plus que je ne suis capable d'écrire dans cette petite introduction. Je vous encourage à ouvrir Emacs et à appuyer sur `ctrl-h` `r` pour ouvrir le manuel intégré et `ctrl-h` `t` pour ouvrir le tutoriel officiel.


## La commande Linux `nano`

`nano` est un éditeur convivial pour les débutants.

Exécutez-le en utilisant `nano <nomdefichier>`.

Vous pouvez taper directement des caractères dans le fichier sans vous soucier des modes.

Vous pouvez quitter sans éditer en utilisant `ctrl-X`. Si vous avez édité le tampon de fichier, l'éditeur vous demandera confirmation et vous pourrez sauvegarder les modifications, ou les ignorer. 

L'aide en bas de l'écran vous montre les commandes clavier qui vous permettent de travailler avec le fichier :

![Screenshot-2019-02-10-at-11.03.51](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2019-02-10-at-11.03.51.png)
`pico` est plus ou moins le même, bien que `nano` soit la version GNU de `pico` qui à un moment donné dans l'histoire n'était pas open source. Le clone `nano` a été fait pour satisfaire les exigences de licence du système d'exploitation GNU.


## La commande Linux `whoami`


Tapez `whoami` pour imprimer le nom d'utilisateur actuellement connecté à la session de terminal :

![Screen-Shot-2020-09-03-at-18.08.05](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.08.05.png)
> Remarque : ceci est différent de la commande `who am i`, qui imprime plus d'informations



## La commande Linux `who`

La commande `who` affiche les utilisateurs connectés au système.

Sauf si vous utilisez un serveur auquel plusieurs personnes ont accès, il est probable que vous serez le seul utilisateur connecté, plusieurs fois :

![Screen-Shot-2020-09-03-at-18.03.05](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.03.05.png)

Pourquoi plusieurs fois ? Parce que chaque shell ouvert comptera comme un accès.

Vous pouvez voir le nom du terminal utilisé, et l'heure/le jour où la session a été démarrée.

Les drapeaux `-aH` indiqueront à `who` d'afficher plus d'informations, y compris le temps d'inactivité et l'identifiant de processus du terminal :

![Screen-Shot-2020-09-03-at-18.05.29](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.05.29.png)

La commande spéciale `who am i` listera les détails de la session de terminal actuelle :

![Screen-Shot-2020-09-03-at-18.06.35](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.06.35.png)

![Screen-Shot-2020-09-03-at-18.07.30](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.07.30.png)


## La commande Linux `su`

Alors que vous êtes connecté au shell du terminal avec un utilisateur, vous pourriez avoir besoin de passer à un autre utilisateur.

Par exemple, vous êtes connecté en tant que root pour effectuer une maintenance, mais ensuite vous voulez passer à un compte utilisateur.

Vous pouvez le faire avec la commande `su` :

```bash
su <nomdutilisateur>
```

Par exemple : `su flavio`.

Si vous êtes connecté en tant qu'utilisateur, exécuter `su` sans rien d'autre vous demandera d'entrer le mot de passe de l'utilisateur `root`, car c'est le comportement par défaut.

![Screen-Shot-2020-09-03-at-18.18.09](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.18.09.png)
`su` démarrera un nouveau shell en tant qu'autre utilisateur.

Lorsque vous avez terminé, taper `exit` dans le shell fermera ce shell, et vous ramènera au shell de l'utilisateur actuel.


## La commande Linux `sudo`

`sudo` est couramment utilisé pour exécuter une commande en tant que root.

Vous devez être autorisé à utiliser `sudo`, et une fois que vous l'êtes, vous pouvez exécuter des commandes en tant que root en entrant le mot de passe de votre utilisateur (_pas_ le mot de passe de l'utilisateur root).

Les permissions sont hautement configurables, ce qui est idéal surtout dans un environnement serveur multi-utilisateurs. Certains utilisateurs peuvent se voir accorder l'accès à l'exécution de commandes spécifiques via `sudo`.

Par exemple, vous pouvez éditer un fichier de configuration système :

```bash
sudo nano /etc/hosts
```

ce qui échouerait autrement à sauvegarder puisque vous n'avez pas les permissions
pour cela.

Vous pouvez exécuter `sudo -i` pour démarrer un shell en tant que root :

![Screen-Shot-2020-09-03-at-18.25.50](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.25.50.png)

Vous pouvez utiliser `sudo` pour exécuter des commandes en tant que n'importe quel utilisateur. `root` est le défaut, mais utilisez l'option `-u` pour spécifier un autre utilisateur :

```bash
sudo -u flavio ls /Users/flavio
```

## La commande Linux `passwd`

Les utilisateurs sous Linux ont un mot de passe attribué. Vous pouvez changer le mot de passe en utilisant la commande `passwd`.

Il y a deux situations ici.

La première est lorsque vous voulez changer votre mot de passe. Dans ce cas, vous tapez :

```bash
passwd
```

et une invite interactive vous demandera l'ancien mot de passe, puis elle vous demandera le nouveau :

![Screen-Shot-2020-09-04-at-07.32.05](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-07.32.05.png)

Lorsque vous êtes `root` (ou avez des privilèges de superutilisateur), vous pouvez définir le nom d'utilisateur pour lequel vous voulez changer le mot de passe :

```bash
passwd <nomdutilisateur> <nouveaumotdepasse>
```

Dans ce cas, vous n'avez pas besoin d'entrer l'ancien.


## La commande Linux `ping`

La commande `ping` envoie une requête à un hôte réseau spécifique, sur le réseau local ou sur Internet.

Vous l'utilisez avec la syntaxe `ping <hôte>` où `<hôte>` pourrait être un nom de domaine, ou une adresse IP.

Voici un exemple de ping vers `google.com` :

![Screen-Shot-2020-09-09-at-15.21.46](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-15.21.46.png)
La commande envoie une requête au serveur, et le serveur retourne une réponse.

`ping` continue d'envoyer la requête chaque seconde, par défaut. Il continuera à s'exécuter jusqu'à ce que vous l'arrêtiez avec `ctrl-C`, sauf si vous passez le nombre de fois que vous voulez essayer avec l'option `-c` : `ping -c 2 google.com`.

Une fois `ping` arrêté, il imprimera quelques statistiques sur les résultats : le pourcentage de paquets perdus, et des statistiques sur les performances du réseau.

Comme vous pouvez le voir, l'écran imprime l'adresse IP de l'hôte, et le temps qu'il a fallu pour obtenir la réponse.

Tous les serveurs ne supportent pas le ping, au cas où la requête expire :

![Screen-Shot-2020-09-09-at-15.21.27](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-15.21.27.png)

Parfois, cela est fait exprès, pour "cacher" le serveur, ou simplement pour réduire la charge. Les paquets de ping peuvent également être filtrés par les pare-feux.

`ping` fonctionne en utilisant le **protocole ICMP** (_Internet Control Message Protocol_), un protocole de couche réseau comme TCP ou UDP.

La requête envoie un paquet au serveur avec le message `ECHO_REQUEST`, et le serveur retourne un message `ECHO_REPLY`. Je ne vais pas entrer dans les détails, mais c'est le concept de base.

Pinguer un hôte est utile pour savoir si l'hôte est joignable (en supposant qu'il implémente le ping), et à quelle distance il se trouve en termes de temps qu'il faut pour revenir vers vous. 

Généralement, plus le serveur est proche géographiquement, moins il faudra de temps pour revenir vers vous. De simples lois physiques causent une distance plus longue pour introduire plus de délai dans les câbles.

## La commande Linux `traceroute`

Lorsque vous essayez d'atteindre un hôte sur Internet, vous passez par votre routeur domestique. Ensuite, vous atteignez le réseau de votre FAI, qui à son tour passe par son propre routeur réseau amont, et ainsi de suite, jusqu'à ce que vous atteigniez enfin l'hôte.

Avez-vous déjà voulu savoir par quelles étapes passent vos paquets pour faire cela ?

La commande `traceroute` est faite pour cela.

Vous invoquez

```bash
traceroute <hôte>
```

et elle recueillera (lentement) toutes les informations pendant que le paquet voyage.

Dans cet exemple, j'ai essayé d'atteindre mon blog avec `traceroute flaviocopes.com` :

![Screen-Shot-2020-09-09-at-16.32.01](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-16.32.01.png)

Tous les routeurs parcourus ne nous retournent pas d'informations. Dans ce cas, `traceroute` imprime `* * *`. Sinon, nous pouvons voir le nom d'hôte, l'adresse IP, et un indicateur de performance.

Pour chaque routeur, nous pouvons voir 3 échantillons, ce qui signifie que traceroute essaie par défaut 3 fois de vous donner une bonne indication du temps nécessaire pour l'atteindre. 

C'est pourquoi cela prend autant de temps pour exécuter `traceroute` par rapport à simplement faire un `ping` vers cet hôte.

Vous pouvez personnaliser ce nombre avec l'option `-q` :

```bash
traceroute -q 1 flaviocopes.com
```

![Screen-Shot-2020-09-09-at-16.36.07](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-16.36.07.png)

## La commande Linux `clear`

Tapez `clear` pour effacer toutes les commandes précédentes qui ont été exécutées dans le terminal actuel.

L'écran sera effacé et vous ne verrez que l'invite en haut :

![Screen-Shot-2020-09-03-at-18.10.32](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-03-at-18.10.32.png)
> Remarque : cette commande a un raccourci pratique : `ctrl-L`

Une fois que vous avez fait cela, vous perdrez l'accès au défilement pour voir la sortie des commandes précédentes entrées.

Vous pourriez donc vouloir utiliser `clear -x` à la place, qui efface toujours l'écran, mais vous permet de revenir en arrière pour voir le travail précédent en faisant défiler vers le haut.

## La commande Linux `history`

Chaque fois que vous exécutez une commande, elle est mémorisée dans l'historique.

Vous pouvez afficher tout l'historique en utilisant :

```bash
history
```

Cela montre l'historique avec des numéros :

![Screen-Shot-2020-09-04-at-08.03.10](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-08.03.10.png)

Vous pouvez utiliser la syntaxe `!<numéro de commande>` pour répéter une commande stockée dans l'historique. Dans l'exemple ci-dessus, taper `!121` répétera la commande `ls -al | wc -l`.

Généralement, les 500 dernières commandes sont stockées dans l'historique.

Vous pouvez combiner cela avec `grep` pour trouver une commande que vous avez exécutée :

```bash
history | grep docker
```

![Screen-Shot-2020-09-04-at-08.04.50](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-04-at-08.04.50.png)
Pour effacer l'historique, exécutez `history -c`.


## La commande Linux `export`

La commande `export` est utilisée pour exporter des variables vers des processus enfants.

Que signifie cela ?

Supposons que vous avez une variable TEST définie de cette manière :

```bash
TEST="test"
```

Vous pouvez imprimer sa valeur en utilisant `echo $TEST` :

![Screen-Shot-2020-09-09-at-17.32.49](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-17.32.49.png)

Mais si vous essayez de définir un script Bash dans un fichier `script.sh` avec la commande ci-dessus :

![Screen-Shot-2020-09-09-at-17.35.23](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-17.35.23.png)

Ensuite, lorsque vous définissez `chmod u+x script.sh` et que vous exécutez ce script avec `./script.sh`, la ligne `echo $TEST` n'imprimera rien !

C'est parce que dans Bash, la variable `TEST` a été définie localement au shell. Lors de l'exécution d'un script shell ou d'une autre commande, un sous-shell est lancé pour l'exécuter, qui ne contient pas les variables locales du shell actuel.

Pour rendre la variable disponible là-bas, nous devons définir `TEST` non de cette manière :

```bash
TEST="test"
```

mais de cette manière :

```bash
export TEST="test"
```

Essayez cela, et l'exécution de `./script.sh` devrait maintenant imprimer "test" :

![Screen-Shot-2020-09-09-at-17.37.56](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-17.37.56.png)
Parfois, vous devez ajouter quelque chose à une variable. Cela est souvent fait avec la variable `PATH`. Vous utilisez cette syntaxe :

```bash
export PATH=$PATH:/new/path
```

Il est courant d'utiliser `export` lorsque vous créez de nouvelles variables de cette manière. Mais vous pouvez également l'utiliser lorsque vous créez des variables dans les fichiers de configuration `.bash_profile` ou `.bashrc` avec Bash, ou dans `.zshenv` avec Zsh.

Pour supprimer une variable, utilisez l'option `-n` :

```bash
export -n TEST
```

Appeler `export` sans aucune option listera toutes les variables exportées.


## La commande Linux `crontab`

Les tâches Cron sont des tâches qui sont planifiées pour s'exécuter à des intervalles spécifiques. Vous pouvez avoir une commande qui effectue quelque chose toutes les heures, ou tous les jours, ou toutes les 2 semaines. Ou les week-ends. 

Elles sont très puissantes, surtout lorsqu'elles sont utilisées sur des serveurs pour effectuer des maintenances et des automatisations.

La commande `crontab` est le point d'entrée pour travailler avec les tâches cron.

La première chose que vous pouvez faire est d'explorer quelles tâches cron sont définies par vous :

```bash
crontab -l
```

Vous n'en avez peut-être aucune, comme moi :

![Screen-Shot-2020-09-09-at-17.54.31](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-17.54.31.png)

Exécutez

```bash
crontab -e
```

pour éditer les tâches cron, et en ajouter de nouvelles.

Par défaut, cela s'ouvre avec l'éditeur par défaut, qui est généralement `vim`. Je préfère `nano`. Vous pouvez utiliser cette ligne pour utiliser un éditeur différent :

```bash
EDITOR=nano crontab -e
```

Maintenant, vous pouvez ajouter une ligne pour chaque tâche cron.

La syntaxe pour définir les tâches cron est un peu effrayante. C'est pourquoi j'utilise généralement un site web pour m'aider à la générer sans erreurs : <https://crontab-generator.org/>

![Screen-Shot-2020-09-09-at-18.03.57](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-18.03.57.png)

Vous choisissez un intervalle de temps pour la tâche cron, et vous tapez la commande à exécuter.

J'ai choisi d'exécuter un script situé dans `/Users/flavio/test.sh` toutes les 12 heures. Voici la ligne crontab dont j'ai besoin pour l'exécuter :

```txt
* */12 * * * /Users/flavio/test.sh >/dev/null 2>&1
```

J'exécute `crontab -e` :

```bash
EDITOR=nano crontab -e
```

et j'ajoute cette ligne, puis j'appuie sur `ctrl-X` et j'appuie sur `y` pour sauvegarder.

Si tout se passe bien, la tâche cron est configurée :

![Screen-Shot-2020-09-09-at-18.06.19](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-18.06.19.png)

Une fois cela fait, vous pouvez voir la liste des tâches cron actives en exécutant :

```bash
crontab -l
```

![Screen-Shot-2020-09-09-at-18.07.00](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-18.07.00.png)

Vous pouvez supprimer une tâche cron en exécutant `crontab -e` à nouveau, en supprimant la ligne et en quittant l'éditeur :

![Screen-Shot-2020-09-09-at-18.07.40](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-18.07.40.png)

![Screen-Shot-2020-09-09-at-18.07.49](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-09-at-18.07.49.png)


## La commande Linux `uname`

Appeler `uname` sans aucune option retournera le nom de code du système d'exploitation :

![Screen-Shot-2020-09-07-at-07.37.41](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.37.41.png)

L'option `m` affiche le nom du matériel (`x86_64` dans cet exemple) et l'option `p` imprime le nom de l'architecture du processeur (`i386` dans cet exemple) :

![Screen-Shot-2020-09-07-at-07.37.51](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.37.51.png)

L'option `s` imprime le nom du système d'exploitation. `r` imprime la version, et `v` imprime la version :

![Screen-Shot-2020-09-07-at-07.37.56](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.37.56.png)

L'option `n` imprime le nom de réseau du nœud :

![Screen-Shot-2020-09-07-at-07.38.01](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.38.01.png)

L'option `a` imprime toutes les informations disponibles :

![Screen-Shot-2020-09-07-at-07.38.06](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-07-at-07.38.06.png)

Sur macOS, vous pouvez également utiliser la commande `sw_vers` pour imprimer plus d'informations sur le système d'exploitation macOS. Notez que cela diffère de la version de Darwin (le noyau), qui ci-dessus est `19.6.0`.

> Darwin est le nom du noyau de macOS. Le noyau est le "cœur" du système d'exploitation, tandis que le système d'exploitation dans son ensemble est appelé macOS. Dans Linux, Linux est le noyau, et GNU/Linux serait le nom du système d'exploitation (bien que nous l'appelions tous "Linux").


## La commande Linux `env`

La commande `env` peut être utilisée pour passer des variables d'environnement sans les définir sur l'environnement extérieur (le shell actuel).

Supposons que vous voulez exécuter une application Node.js et définir la variable `USER` pour celle-ci.

Vous pouvez exécuter

```bash
env USER=flavio node app.js
```

et la variable d'environnement `USER` sera accessible depuis l'application Node.js via l'interface Node `process.env`.

Vous pouvez également exécuter la commande en effaçant toutes les variables d'environnement déjà définies, en utilisant l'option `-i` :

```bash
env -i node app.js
```

Dans ce cas, vous obtiendrez une erreur disant `env: node: No such file or directory` parce que la commande `node` n'est pas accessible, car la variable `PATH` utilisée par le shell pour rechercher des commandes dans les chemins communs n'est pas définie.

Vous devez donc passer le chemin complet vers le programme `node` :

```bash
env -i /usr/local/bin/node app.js
```

Essayez avec un simple fichier `app.js` avec ce contenu :

```js
console.log(process.env.NAME)
console.log(process.env.PATH)
```

Vous verrez la sortie comme

```
undefined
undefined
```

Vous pouvez passer une variable d'environnement :

```bash
env -i NAME=flavio node app.js
```

et la sortie sera

```
flavio
undefined
```

Supprimer l'option `-i` rendra `PATH` disponible à nouveau à l'intérieur du programme :

![Screen-Shot-2020-09-10-at-16.55.17](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-10-at-16.55.17.png)

La commande `env` peut également être utilisée pour imprimer toutes les variables d'environnement. Si elle est exécutée sans options :

```bash
env
```

elle retournera une liste des variables d'environnement définies, par exemple :

```txt
HOME=/Users/flavio
LOGNAME=flavio
PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin
PWD=/Users/flavio
SHELL=/usr/local/bin/fish
```

Vous pouvez également rendre une variable inaccessible à l'intérieur du programme que vous exécutez, en utilisant l'option `-u`. Par exemple, ce code supprime la variable `HOME` de l'environnement de la commande :

```bash
env -u HOME node app.js
```


## La commande Linux `printenv`

Voici un guide rapide de la commande `printenv`, utilisée pour imprimer les valeurs des variables d'environnement

Dans n'importe quel shell, il y a un bon nombre de variables d'environnement, définies soit par le système, soit par vos propres scripts shell et configurations.

Vous pouvez les imprimer toutes dans le terminal en utilisant la commande `printenv`. La sortie sera quelque chose comme ceci :

```txt
HOME=/Users/flavio
LOGNAME=flavio
PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin
PWD=/Users/flavio
SHELL=/usr/local/bin/fish
```

avec quelques lignes supplémentaires, généralement.

Vous pouvez ajouter un nom de variable en tant que paramètre, pour n'afficher que la valeur de cette variable :

```bash
printenv PATH
```

![Screen-Shot-2020-09-10-at-16.31.20](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-10-at-16.31.20.png)


## Conclusion

Merci beaucoup d'avoir lu ce manuel.

J'espère qu'il vous inspirera à en apprendre davantage sur Linux et ses capacités. Ce sont des connaissances intemporelles qui ne seront pas dépassées de sitôt.

N'oubliez pas que vous pouvez [télécharger ce manuel au format PDF / ePUB / Mobi](https://flaviocopes.com/page/linux-commands-handbook/) si vous le souhaitez !

Je **publie des tutoriels de programmation** tous les jours sur mon site web [flaviocopes.com](https://flaviocopes.com) si vous voulez consulter plus de contenu génial comme celui-ci.

Vous pouvez me joindre sur Twitter [@flaviocopes](https://twitter.com/flaviocopes).