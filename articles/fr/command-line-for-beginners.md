---
title: Ligne de commande pour débutants – Comment utiliser le terminal comme un pro
  [Guide complet]
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-04-05T16:45:18.000Z'
originalURL: https://freecodecamp.org/news/command-line-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pixabay-207580.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: shell script
  slug: shell-script
- name: terminal
  slug: terminal
seo_title: Ligne de commande pour débutants – Comment utiliser le terminal comme un
  pro [Guide complet]
seo_desc: 'Hi everyone! In this article we''ll take a good look at the command line
  (also known as the CLI, console, terminal or shell).

  The command line is one of the most useful and efficient tools we have as developers
  and as computer users in general. But us...'
---

Bonjour à tous ! Dans cet article, nous allons examiner de près la ligne de commande (également connue sous le nom de CLI, console, terminal ou shell).

La ligne de commande est l'un des outils les plus utiles et efficaces que nous ayons en tant que développeurs et utilisateurs d'ordinateurs en général. Mais son utilisation peut sembler un peu écrasante et complexe lorsque vous débutez.

Dans cet article, je vais essayer d'expliquer simplement les parties qui composent l'interface de ligne de commande, et les bases de son fonctionnement, afin que vous puissiez commencer à l'utiliser pour vos tâches quotidiennes.

C'est parti ! =D

## Table des matières

* [Différence entre console, terminal, ligne de commande (CLI) et Shell](#heading-difference-entre-console-terminal-ligne-de-commande-cli-et-shell)
    
    * [Console](#heading-console)
        
    * [Terminal](#heading-terminal)
        
    * [Shell](#heading-shell)
        
    * [Ligne de commande (CLI)](#heading-ligne-de-commande-ou-cli-interface-de-ligne-de-commande)
        
* [Pourquoi devrais-je même me soucier d'utiliser le terminal ?](#heading-pourquoi-devrais-je-meme-me-soucier-dutiliser-le-terminal)
    
* [Différents types de shells](#heading-differents-types-de-shells)
    
    * [Un peu d'histoire - Posix](#heading-un-peu-dhistoire-posix)
        
    * [Comment savoir quel shell j'utilise ?](#heading-comment-savoir-quel-shell-jutilise)
        
    * [Quel shell est le meilleur ?](#heading-quel-shell-est-le-meilleur)
        
        * [Un commentaire sur la personnalisation](#heading-un-commentaire-sur-la-personnalisation)
            
* [Commandes les plus courantes et utiles à utiliser](#heading-commandes-les-plus-courantes-et-utiles-a-utiliser)
    
    * [Commandes Git](#heading-commandes-git)
        
* [Notre premier script](#heading-notre-premier-script)
    
* [Conclusion](#heading-conclusion)
    

# Différence entre console, ligne de commande (CLI), terminal et Shell

Je pense qu'un bon point de départ est de savoir exactement ce qu'est la ligne de commande.

Lorsque vous faites référence à cela, vous avez peut-être entendu les termes Terminal, console, ligne de commande, CLI et shell. Les gens utilisent souvent ces mots de manière interchangeable, mais la vérité est qu'ils désignent en réalité des choses différentes.

Distinguer chacun n'est pas nécessairement une connaissance cruciale à avoir, mais cela aidera à clarifier les choses. Alors, expliquons brièvement chacun d'eux.

## Console :

La console est le **dispositif physique** qui vous permet d'interagir avec l'ordinateur.

En anglais simple, c'est votre écran d'ordinateur, votre clavier et votre souris. En tant qu'utilisateur, vous interagissez avec votre ordinateur **via** votre console.

![image_13b2c80d-a2d6-4429-8ca6-f053340897cc](https://www.freecodecamp.org/news/content/images/2022/03/image_13b2c80d-a2d6-4429-8ca6-f053340897cc.png align="left")

## Terminal :

Un terminal est un environnement de saisie et de sortie de texte. C'est un **programme** qui agit comme un **wrapper** et nous permet de saisir des commandes que l'ordinateur traite.

En anglais simple, c'est la "fenêtre" dans laquelle vous saisissez les commandes réelles que votre ordinateur va traiter.

![terminal](https://www.freecodecamp.org/news/content/images/2022/03/terminal.png align="left")

Gardez à l'esprit que le terminal est un programme, comme n'importe quel autre. Et comme n'importe quel programme, vous pouvez l'installer et le désinstaller comme vous le souhaitez. Il est également possible d'avoir de nombreux terminaux installés sur votre ordinateur et d'exécuter celui que vous voulez, quand vous le voulez.

Tous les systèmes d'exploitation sont livrés avec un terminal par défaut installé, mais il existe de nombreuses options parmi lesquelles choisir, chacune avec ses propres fonctionnalités et caractéristiques.

## Shell :

Un shell est un **programme** qui agit comme un interpréteur de ligne de commande. Il **traite les commandes** et **affiche les résultats**. Il interprète et traite les commandes saisies par l'utilisateur.

Comme le terminal, le shell est un programme qui est fourni par défaut dans tous les systèmes d'exploitation, mais peut également être installé et désinstallé par l'utilisateur.

Différents shells viennent avec différentes syntaxes et caractéristiques. Il est également possible d'avoir de nombreux shells installés sur votre ordinateur et d'exécuter chacun d'eux quand vous le souhaitez.

Dans la plupart des systèmes d'exploitation Linux et Mac, le shell par défaut est Bash. Sur Windows, c'est Powershell. D'autres exemples courants de shells sont Zsh et Fish.

Les shells fonctionnent également comme des **langages de programmation**, dans le sens où avec eux nous pouvons construire des **scripts** pour faire exécuter une certaine tâche à notre ordinateur. Les scripts ne sont rien de plus qu'une série d'instructions (commandes) que nous pouvons sauvegarder dans un fichier et exécuter plus tard quand nous le voulons.

Nous allons examiner les scripts plus tard dans cet article. Pour l'instant, gardez simplement à l'esprit que le shell est le programme que votre ordinateur utilise pour "comprendre" et exécuter vos commandes, et que vous pouvez également l'utiliser pour programmer des tâches.

Gardez également à l'esprit que le terminal est le programme dans lequel le shell va s'exécuter. Mais les deux programmes sont indépendants. Cela signifie que je peux avoir n'importe quel shell s'exécuter sur n'importe quel terminal. Il n'y a pas de dépendance entre les deux programmes dans ce sens.

## Ligne de commande ou CLI (interface de ligne de commande) :

La CLI est l'interface dans laquelle nous saisissons des commandes pour que l'ordinateur les traite. En anglais simple, c'est l'espace dans lequel vous saisissez les commandes que l'ordinateur va traiter.

![cli](https://www.freecodecamp.org/news/content/images/2022/03/cli.png align="left")

Cela est pratiquement la même chose que le terminal et, à mon avis, ces termes peuvent être utilisés de manière interchangeable.

Une chose intéressante à mentionner ici est que la plupart des systèmes d'exploitation ont deux types d'interfaces différents :

* La **CLI**, qui prend des commandes comme entrées afin que l'ordinateur exécute des tâches.
    
* L'autre est le **GUI** (interface utilisateur graphique), dans laquelle l'utilisateur peut voir des choses à l'écran et cliquer dessus, et l'ordinateur répondra à ces événements en exécutant la tâche correspondante.
    

# Pourquoi devrais-je même me soucier d'utiliser le terminal ?

Nous venons de mentionner que la plupart des systèmes d'exploitation sont livrés avec un GUI. Donc, si nous pouvons voir des choses à l'écran et cliquer pour faire ce que nous voulons, vous pourriez vous demander pourquoi vous devriez apprendre cette chose compliquée de terminal/cli/shell ?

La première raison est que pour de nombreuses tâches, c'est simplement **plus efficace**. Nous verrons quelques exemples dans un instant, mais il existe de nombreuses tâches où un GUI nécessiterait de nombreux clics dans différentes fenêtres. Mais sur la CLI, ces tâches peuvent être exécutées avec une seule commande.

Dans ce sens, être à l'aise avec la ligne de commande vous aidera à gagner du temps et à pouvoir exécuter vos tâches plus rapidement.

La deuxième raison est que, en utilisant des commandes, vous pouvez facilement **automatiser des tâches**. Comme mentionné précédemment, nous pouvons construire des scripts avec notre shell et les exécuter plus tard quand nous le voulons. Cela est incroyablement utile lorsque nous traitons des tâches répétitives que nous ne voulons pas faire encore et encore.

Juste pour donner quelques exemples, nous pourrions construire un script qui crée un nouveau dépôt en ligne pour nous, ou qui crée une certaine infrastructure sur un fournisseur de cloud pour nous, ou qui exécute une tâche plus simple comme changer notre fond d'écran toutes les heures.

Le scripting est un excellent moyen de gagner du temps avec les tâches répétitives.

La troisième raison est que parfois la CLI sera le **seul moyen** par lequel nous pourrons interagir avec un ordinateur. Prenez, par exemple, le cas où vous devriez interagir avec un serveur de plateforme cloud. Dans la plupart de ces cas, vous n'aurez pas de GUI disponible, juste une CLI pour exécuter des commandes.

Ainsi, être à l'aise avec la CLI vous permettra d'interagir avec des ordinateurs en toutes occasions.

La dernière raison est que cela a l'air cool et c'est amusant. Vous ne voyez pas les hackers de films cliquer autour de leurs ordinateurs, n'est-ce pas ? ;)

# Différents types de shells

Avant de plonger dans les commandes réelles que vous pouvez exécuter dans votre terminal, je pense qu'il est important de reconnaître les différents types de shells disponibles et comment identifier quel shell vous utilisez actuellement.

Différents shells viennent avec différentes syntaxes et différentes fonctionnalités, donc pour savoir exactement quelle commande entrer, vous devez d'abord savoir quel shell vous utilisez.

## Un peu d'histoire – Posix

Pour les shells, il existe une norme commune appelée [**Posix**](https://en.wikipedia.org/wiki/POSIX).

Posix fonctionne pour les shells de manière très similaire à la façon dont ECMAScript fonctionne pour JavaScript. C'est une norme qui dicte certaines caractéristiques et fonctionnalités que tous les shells doivent respecter.

Cette norme a été établie dans les années 1980 et la plupart des shells actuels ont été développés selon cette norme. C'est pourquoi la plupart des shells partagent une syntaxe et des fonctionnalités similaires.

## Comment savoir quel shell j'utilise ?

Pour savoir quel shell vous utilisez actuellement, ouvrez simplement votre terminal et entrez `echo $0`. Cela imprimera le nom du programme en cours d'exécution, qui dans ce cas est le shell réel.

![screenshot-1](https://www.freecodecamp.org/news/content/images/2022/04/screenshot-1.png align="left")

## Quel shell est le meilleur ?

Il n'y a pas BEAUCOUP de différence entre la plupart des shells. Puisque la plupart d'entre eux respectent la même norme, vous constaterez que la plupart d'entre eux fonctionnent de manière similaire.

Il y a quelques différences mineures que vous pourriez vouloir connaître, cependant :

* Comme mentionné, **Bash** est le plus largement utilisé et est installé par défaut sur Mac et Linux.
    
* **Zsh** est très similaire à Bash, mais il a été créé après et vient avec quelques améliorations par rapport à Bash. Si vous souhaitez avoir plus de détails sur ses différences, [voici un article intéressant](https://linuxhint.com/differences_between_bash_zsh/#:~:text=It%20has%20many%20features%20like,by%20default%20with%20Linux%20distribution.) à ce sujet.
    
* **Fish** est un autre shell couramment utilisé qui vient avec quelques fonctionnalités et configurations intégrées telles que l'autocomplétion et la coloration syntaxique. Le problème avec Fish est qu'il n'est pas conforme à Posix, contrairement à Bash et Zsh. Cela signifie que certaines des commandes que vous pourrez exécuter sur Bash et Zsh ne s'exécuteront pas sur Fish et vice versa. Cela rend les scripts Fish moins compatibles avec la plupart des ordinateurs par rapport à Bash et Zsh.
    
* Il existe également d'autres shells comme **Ash** ou **Dash** (la nomenclature rend tout encore plus confus, je sais...) qui sont des versions allégées des shells Posix. Cela signifie qu'ils n'offrent que les fonctionnalités requises dans Posix, et rien d'autre. Alors que Bash et Zsh **ajoutent plus de fonctionnalités** que ce que Posix exige.
    

Le fait que les shells ajoutent plus de fonctionnalités les rend plus faciles et plus conviviaux à utiliser, mais plus lents à exécuter des scripts et des commandes.

Ainsi, une pratique courante consiste à utiliser ces shells "améliorés" comme Bash ou Zsh pour l'interaction générale, et un shell "allégé" comme Ash ou Dash pour exécuter des scripts.

Lorsque nous aborderons le scripting plus tard, nous verrons comment nous pouvons définir quel shell exécutera un script donné.

Si vous êtes intéressé par une comparaison plus détaillée entre ces shells, [voici une vidéo qui l'explique très bien](https://www.youtube.com/watch?v=dRdGq8khTJc):

Si je devais recommander un shell, je recommanderais bash car c'est le plus standard et le plus couramment utilisé. Cela signifie que vous pourrez traduire vos connaissances dans la plupart des environnements.

Mais encore une fois, la vérité est qu'il n'y a pas BEAUCOUP de différence entre la plupart des shells. Donc dans tous les cas, vous pouvez en essayer quelques-uns et voir lequel vous préférez. ;)

### Un commentaire sur la personnalisation

Je viens de mentionner que Fish vient avec une configuration intégrée telle que l'autocomplétion et la coloration syntaxique. Cela est intégré dans Fish, mais dans Bash ou Zsh, vous pouvez également configurer ces fonctionnalités.

Le point est que les shells sont personnalisables. Vous pouvez modifier le fonctionnement du programme, les commandes dont vous disposez, les informations que votre prompt affiche, et plus encore.

Nous ne verrons pas les options de personnalisation en détail ici, mais sachez que lorsque vous installez un shell sur votre ordinateur, certains fichiers seront créés sur votre système. Plus tard, vous pourrez modifier ces fichiers pour personnaliser votre programme.

De plus, il existe de nombreux plugins disponibles en ligne qui vous permettent de personnaliser votre shell de manière plus facile. Vous les installez simplement et obtenez les fonctionnalités que le plugin offre. Certains exemples sont [OhMyZsh](https://ohmyz.sh/) et [Starship](https://starship.rs/).

Ces options de personnalisation sont également valables pour les terminaux.

Ainsi, non seulement vous avez de nombreuses options de shells et de terminaux parmi lesquelles choisir – vous avez également de nombreuses options de configuration pour chaque shell et terminal.

Si vous débutez, toutes ces informations peuvent sembler un peu écrasantes. Mais sachez simplement qu'il existe de nombreuses options disponibles, et que chaque option peut également être personnalisée. C'est tout.

# Commandes les plus courantes et utiles à utiliser

Maintenant que nous avons une base de fonctionnement de la CLI, plongeons dans les commandes les plus utiles que vous pouvez commencer à utiliser pour vos tâches quotidiennes.

Gardez à l'esprit que ces exemples seront basés sur ma configuration actuelle (Bash sur un système d'exploitation Linux). Mais la plupart des commandes devraient s'appliquer à la plupart des configurations de toute façon.

* **Echo** imprime dans le terminal tout paramètre que nous lui passons.
    

```plaintext
echo Hello freeCodeCamp! // Sortie : Hello freeCodeCamp!
```

* **pwd** signifie print working directory et il imprime le "lieu" ou répertoire où nous nous trouvons actuellement dans l'ordinateur.
    

```plaintext
pwd // Sortie : /home/German
```

* **ls** vous présente le contenu du répertoire dans lequel vous vous trouvez actuellement. Il vous présentera à la fois les fichiers et les autres répertoires que contient votre répertoire actuel.
    

Par exemple, voici un répertoire de projet React sur lequel j'ai travaillé récemment :

```plaintext
ls // Sortie :
node_modules  package.json  package-lock.json  public  README.md  src
```

Si vous passez à cette commande le flag ou paramètre `-a`, elle vous montrera également les fichiers ou répertoires cachés. Comme les fichiers `.git` ou `.gitignore`

```plaintext
ls -a // Sortie :
.   .env  .gitignore    package.json       public     src
..  .git  node_modules  package-lock.json  README.md
```

* **cd** est l'abréviation de Change directory et il vous emmènera de votre répertoire actuel à un autre.
    

Alors que je suis dans mon répertoire personnel, je peux entrer `cd Desktop` et il m'emmènera au répertoire Desktop.

Si je veux remonter d'un répertoire, c'est-à-dire aller au répertoire qui contient le répertoire actuel, je peux entrer `cd ..`

Si vous entrez `cd` seul, il vous emmènera directement à votre répertoire personnel.

* **mkdir** signifie make directory et il créera un nouveau répertoire pour vous. Vous devez passer à la commande le paramètre du nom du répertoire.
    

Si je voulais créer un nouveau répertoire appelé "Test", j'entrerais `mkdir test`.

* **rmdir** signifie Remove directory et il fait exactement cela. Il a besoin du paramètre du nom du répertoire comme `mkdir` : `rmdir test`.
    
* **touch** vous permet de créer un fichier vide dans votre répertoire actuel. En tant que paramètres, il prend le nom du fichier, comme `touch test.txt`.
    
* **rm** vous permet de supprimer des fichiers, de la même manière que `rmdir` vous permet de supprimer des répertoires. `rm test.txt`
    
* **cp** vous permet de copier des fichiers ou des répertoires. Cette commande prend deux paramètres : le premier est le fichier ou le répertoire que vous souhaitez copier, et le second est la destination de votre copie (où vous souhaitez copier votre fichier/répertoire).
    

Si je veux faire une copie de mon fichier txt dans le même répertoire, je peux entrer ce qui suit :

```plaintext
cp test.txt testCopy.txt
```

Voyez que le répertoire ne change pas, car pour "destination", j'entre le nouveau nom du fichier.

Si je voulais copier le fichier dans un répertoire différent, mais garder le même nom de fichier, je peux entrer ceci :

```plaintext
cp test.txt ./testFolder/
```

Et si je voulais copier dans un dossier différent en changeant le nom du fichier, bien sûr je peux entrer ceci :

```plaintext
cp test.txt ./testFolder/testCopy.txt
```

* **mv** est l'abréviation de move, et nous permet de déplacer un fichier ou un répertoire d'un endroit à un autre. C'est-à-dire, le créer dans un nouveau répertoire et le supprimer dans le précédent (comme vous pourriez le faire en coupant et en collant).
    

Encore une fois, cette commande prend deux paramètres, le fichier ou le répertoire que nous voulons déplacer et la destination.

```plaintext
mv test.txt ./testFolder/
```

Nous pouvons également changer le nom du fichier dans la même commande si nous le voulons :

```plaintext
mv test.txt ./testFolder/testCopy.txt
```

* **head** vous permet de voir le début d'un fichier ou des données canalisées directement depuis le terminal.
    

```plaintext
head test.txt // Sortie :
this is the beginning of my test file
```

* **tail** fonctionne de la même manière mais il vous montrera la fin du fichier.
    

```plaintext
tail test.txt // Sortie :

this is the end of my test file
```

* Le flag **\--help** peut être utilisé sur la plupart des commandes et il retournera des informations sur la façon d'utiliser cette commande donnée.
    

```plaintext
cd --help // sortie :
cd : cd [-L|[-P [-e]] [-@]] [dir]
Change the shell working directory.
```

Change le répertoire courant en DIR. Le DIR par défaut est la valeur de la variable shell HOME.

La variable CDPATH définit le chemin de recherche pour le répertoire contenant DIR. Les noms de répertoires alternatifs dans CDPATH sont séparés par un deux-points `:`.

Un nom de répertoire nul est le même que le répertoire courant si DIR commence par `...`.

* De manière similaire, la commande **man** retournera des informations sur n'importe quelle commande particulière.
    

```plaintext
    man cp // sortie :

    CP(1)                            User Commands                           CP(1)

    NAME
           cp - copy files and directories

    SYNOPSIS
           cp [OPTION]... [-T] SOURCE DEST
           cp [OPTION]... SOURCE... DIRECTORY
           cp [OPTION]... -t DIRECTORY SOURCE...

    DESCRIPTION
           Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

           Mandatory  arguments  to  long  options are mandatory for short options
           too.

           -a, --archive
                  same as -dR --preserve=all

           --attributes-only
                  don't copy the file data, just the attributes
    ...
```

Vous pouvez même entrer `man bash` et cela retournera un énorme manuel sur tout ce qu'il y a à savoir sur ce shell. ;)

* **code** ouvrira votre éditeur de code par défaut. Si vous entrez la commande seule, elle ouvre simplement l'éditeur avec le dernier fichier/répertoire que vous avez ouvert.
    

Vous pouvez également ouvrir un fichier donné en le passant comme paramètre : `code test.txt`.

Ou ouvrir un nouveau fichier en passant le nouveau nom de fichier : `code thisIsAJsFile.js`.

* **edit** ouvrira des fichiers texte sur votre éditeur de texte de ligne de commande par défaut (qui, si vous êtes sur Mac ou Linux, sera probablement soit Nano soit Vim).
    

Si vous ouvrez votre fichier et ne pouvez pas quitter votre éditeur, regardez d'abord ce mème :

![vimExit](https://www.freecodecamp.org/news/content/images/2022/03/vimExit.png align="left")

Puis tapez `:q!` et appuyez sur Entrée.

Le mème est drôle parce que tout le monde a du mal avec les éditeurs de texte CLI au début, car la plupart des actions (comme quitter l'éditeur) sont effectuées avec des raccourcis clavier. L'utilisation de ces éditeurs est un tout autre sujet, alors allez chercher des tutoriels si vous êtes intéressé à en apprendre plus. ;)

* **ctrl+c** vous permet de quitter le processus actuel que le terminal est en train d'exécuter. Par exemple, si vous créez une application react avec `npx create-react-app` et souhaitez annuler la construction à un moment donné, appuyez simplement sur **ctrl+c** et cela s'arrêtera.
    
* Copier du texte depuis le terminal peut se faire avec **ctrl+shift+c** et coller peut se faire avec **ctrl+shift+v**
    
* **clear** effacera votre terminal de tout contenu précédent.
    
* **exit** fermera votre terminal et (ceci n'est pas une commande mais c'est cool aussi) **ctrl+alt+t** ouvrira un nouveau terminal pour vous.
    
* En appuyant sur les **touches haut et bas**, vous pouvez naviguer à travers les commandes précédentes que vous avez entrées.
    
* En appuyant sur **tab**, vous obtiendrez une autocomplétion basée sur le texte que vous avez écrit jusqu'à présent. En appuyant sur **tab deux fois**, vous obtiendrez des suggestions basées sur le texte que vous avez écrit jusqu'à présent.
    

Par exemple, si j'écris `edit test` et **tab deux fois**, j'obtiens `testFolder/ test.txt`. Si j'écris `edit test.` et appuie sur **tab**, mon texte se complète automatiquement en `edit test.txt`

## Commandes Git

Outre le travail autour du système de fichiers et l'installation/désinstallation de choses, l'interaction avec Git et les dépôts en ligne est probablement l'une des choses les plus courantes que vous allez utiliser le terminal pour en tant que développeur.

C'est beaucoup plus efficace de le faire depuis le terminal que de cliquer, alors examinons les commandes git les plus utiles.

* **git init** créera un nouveau dépôt local pour vous.
    

```plaintext
git init // sortie :
Initialized empty Git repository in /home/German/Desktop/testFolder/.git/
```

* **git add** ajoute un ou plusieurs fichiers à la zone de transit. Vous pouvez soit détailler un fichier spécifique à ajouter à la zone de transit, soit ajouter tous les fichiers modifiés en tapant `git add .`
    
* **git commit** valide vos modifications dans le dépôt. Les validations doivent toujours être accompagnées du flag `-m` et d'un message de validation.
    

```plaintext
git commit -m 'This is a test commit' // sortie :
[master (root-commit) 6101dfe] This is a test commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.js
```

* **git status** vous indique sur quelle branche vous vous trouvez actuellement et si vous avez des modifications à valider ou non.
    

```plaintext
git status  // sortie :
On branch master
nothing to commit, working tree clean
```

* **git clone** vous permet de cloner (copier) un dépôt dans le répertoire où vous vous trouvez actuellement. Gardez à l'esprit que vous pouvez cloner à la fois des dépôts distants (sur GitHub, GitLab, etc.) et des dépôts locaux (ceux qui sont stockés sur votre ordinateur).
    

```plaintext
git clone https://github.com/coccagerman/MazeGenerator.git // sortie :
Cloning into 'MazeGenerator'...
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 15 (delta 1), reused 11 (delta 0), pack-reused 0
Unpacking objects: 100% (15/15), done.
```

* **git remote add origin** est utilisé pour détailler l'URL du dépôt distant que vous allez utiliser pour votre projet. Au cas où vous souhaiteriez la changer à un moment donné, vous pouvez le faire en utilisant la commande `git remote set-url origin`.
    

```plaintext
git remote add origin https://github.com/coccagerman/testRepo.git
```

> Gardez à l'esprit que vous devez d'abord créer votre dépôt distant afin d'obtenir son URL. Nous verrons comment vous pouvez faire cela depuis la ligne de commande avec un petit script plus tard. ;)

* **git remote -v** vous permet de lister le dépôt distant actuel que vous utilisez.
    

```plaintext
git remote -v // sortie :
origin	https://github.com/coccagerman/testRepo.git (fetch)
origin	https://github.com/coccagerman/testRepo.git (push)
```

* **git push** télécharge vos modifications validées vers votre dépôt distant.
    

```plaintext
git push // sortie :
Counting objects: 2, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 266 bytes | 266.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0)
```

* **git branch** liste toutes les branches disponibles sur votre dépôt et vous indique sur quelle branche vous vous trouvez actuellement. Si vous souhaitez créer une nouvelle branche, vous devez simplement ajouter le nom de la nouvelle branche comme paramètre, par exemple `git branch <nom-de-la-branche>`.
    

```plaintext
git branch // sortie :
* main
```

* **git checkout** vous déplace d'une branche à une autre. Il prend votre branche de destination comme paramètre.
    

```plaintext
git checkout newBranch // sortie :
Switched to branch 'newBranch'
```

* **git pull** télécharge (download) le code de votre dépôt distant et le combine avec votre dépôt local. Cela est particulièrement utile lorsque vous travaillez en équipe, lorsque de nombreux développeurs travaillent sur la même base de code. Dans ce cas, chaque développeur télécharge périodiquement depuis le dépôt distant afin de travailler sur une base de code qui inclut les modifications effectuées par tous les autres développeurs.
    

Si un nouveau code est présent dans votre dépôt distant, la commande retournera les fichiers réels qui ont été modifiés lors du téléchargement. Sinon, nous obtenons `Already up to date`.

```plaintext
git pull // sortie :
Already up to date.
```

* **git diff** vous permet de voir les différences entre la branche dans laquelle vous vous trouvez actuellement et une autre.
    

```plaintext
git diff newBranch // sortie :
diff --git a/newFileInNewBranch.js b/newFileInNewBranch.js
deleted file mode 100644
index e69de29..0000000
```

En tant que commentaire à part, lors de la comparaison des différences entre les branches ou les dépôts, des outils visuels comme [Meld](https://meldmerge.org/) sont généralement utilisés. Ce n'est pas que vous ne pouvez pas le visualiser directement dans le terminal, mais ces outils sont excellents pour une visualisation plus claire.

* **git merge** fusionne (combine) la branche dans laquelle vous vous trouvez actuellement avec une autre. Gardez à l'esprit que les modifications ne seront incorporées qu'à la branche dans laquelle vous vous trouvez actuellement, et non à l'autre.
    

```plaintext
git merge newBranch // sortie :
Updating f15cf51..3a3d62f
Fast-forward
 newFileInNewBranch.js | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 newFileInNewBranch.js
```

* **git log** liste tous les commits précédents que vous avez effectués dans le dépôt.
    

```plaintext
git log // sortie :
commit 3a3d62fe7cea7c09403c048e971a5172459d0948 (HEAD -> main, tag: TestTag, origin/main, newBranch)
Author: German Cocca <german.cocca@avature.net>
Date:   Fri Apr 1 18:48:20 2022 -0300

    Added new file

commit f15cf515dd3ec398210108dce092debf26ff9e12
Author: German Cocca <german.cocca@avature.net>
    ...
```

* Le flag **\--help** vous montrera des informations sur une commande donnée, exactement de la même manière qu'il fonctionne avec bash.
    

```plaintext
git diff --help // sortie :
GIT-DIFF(1)                       Git Manual                       GIT-DIFF(1)

NAME
       git-diff - Show changes between commits, commit and working tree, etc

SYNOPSIS
       git diff [options] [<commit>] [--] [<path>...]
       git diff [options] --cached [<commit>] [--] [<path>...]
       ...
```

# Notre premier script

Maintenant, nous sommes prêts à passer à la partie vraiment amusante et géniale de la ligne de commande, le scripting !

Comme je l'ai mentionné précédemment, un script n'est rien de plus qu'une série de commandes ou d'instructions que nous pouvons exécuter à tout moment. Pour expliquer comment nous pouvons en coder un, nous utiliserons un exemple simple qui nous permettra de créer un dépôt github en exécutant une seule commande. ;)

* La première chose à faire est de créer un fichier `.sh`. Vous pouvez le mettre où vous voulez. J'ai appelé le mien `newGhRepo.sh`.
    
* Ensuite, ouvrez-le dans votre éditeur de texte/code de choix.
    
* Sur notre première ligne, nous écrirons ce qui suit : `#! /bin/sh`
    

Cela s'appelle un **shebang**, et sa fonction est de déclarer quel shell va exécuter ce script.

Vous souvenez-vous lorsque nous avons mentionné précédemment que nous pouvons utiliser un shell donné pour l'interaction générale et un autre shell donné pour exécuter un script ? Eh bien, le shebang est l'instruction qui dicte quel shell exécute le script.

Comme mentionné également, nous utilisons un shell "allégé" (également connu sous le nom de shells sh) pour exécuter les scripts car ils sont plus efficaces (bien que la différence puisse être imperceptible pour être honnête, c'est juste une préférence personnelle). Sur mon ordinateur, j'ai dash comme mon shell sh.

Si nous voulions que ce script s'exécute avec bash, le shebang serait `#! /bin/bash`

* Notre ligne suivante sera `repoName=$1`
    

Ici, nous déclarons une **variable** appelée repoName, et nous l'assignons à la valeur du premier paramètre que le script reçoit.

Un **paramètre** est un ensemble de caractères qui est saisi après le script/commande. Comme avec la commande `cd`, nous devons spécifier un paramètre de répertoire afin de changer de répertoire (par exemple : `cd testFolder`).

Une façon dont nous pouvons identifier les paramètres dans un script est d'utiliser le signe dollar et l'ordre dans lequel ce paramètre est attendu.

Si j'attends plus d'un paramètre, je pourrais écrire :

```plaintext
paramOne=$1
paramTwo=$2
paramThree=$3
...
```

* Nous attendons donc le nom du dépôt comme paramètre de notre script. Mais que se passe-t-il si l'utilisateur oublie de le saisir ? Nous devons prévoir cela, donc ensuite nous allons coder une **conditionnelle** qui continue de demander à l'utilisateur de saisir le nom du dépôt jusqu'à ce que ce paramètre soit reçu.
    

Nous pouvons faire cela comme ceci :

```plaintext
while [ -z "$repoName" ]
do
   echo 'Fournissez un nom de dépôt'
   read -r -p $'Nom du dépôt :' repoName
done
```

Ce que nous faisons ici est :

1. Tant que la variable repoName n'est pas assignée (`while [ -z "$repoName" ]`)
    
2. Écrire dans la console ce message (`echo 'Fournissez un nom de dépôt'`)
    
3. Puis lire toute entrée que l'utilisateur fournit et assigner l'entrée à la variable repoName (`read -r -p $'Nom du dépôt :' repoName`)
    

* Maintenant que nous avons notre nom de dépôt en place, nous pouvons créer notre dépôt Git local comme ceci :
    

```plaintext
echo "# $repoName" >> README.md
git init
git add .
git commit -m "First commit"
```

Cela crée un fichier readme et écrit une seule ligne avec le nom du dépôt (`echo "# $repoName" >> README.md`) puis initialise le dépôt git et fait un premier commit.

* Ensuite, il est temps de télécharger notre dépôt sur github. Pour cela, nous allons tirer parti de l'[API github](https://docs.github.com/en/rest/reference/repos) dans la commande suivante :
    

`curl -u coccagerman https://api.github.com/user/repos -d '{"name": "'"$repoName"'", "private":false}'`

**curl** est une commande pour transférer des données depuis ou vers un serveur, en utilisant l'un des nombreux protocoles supportés.

Ensuite, nous utilisons le flag `-u` pour déclarer l'utilisateur pour lequel nous créons le dépôt (`-u coccagerman`).

Ensuite vient le point de terminaison fourni par l'API GitHub (`https://api.github.com/user/repos`)

Et enfin, nous utilisons le flag `-d` pour passer des paramètres à cette commande. Dans ce cas, nous indiquons le nom du dépôt (pour lequel nous utilisons notre variable `repoName`) et définissons l'option `private` à `false`, puisque nous voulons que notre dépôt soit public.

De nombreuses autres options de configuration sont disponibles dans l'API, alors [consultez la documentation](https://docs.github.com/en/rest/reference/repos#create-a-repository-for-the-authenticated-user) pour plus d'informations.

* Après avoir exécuté cette commande, GitHub nous demandera de saisir notre **jeton privé** pour l'authentification.
    

Si vous n'avez pas encore de jeton privé, vous pouvez le générer dans GitHub dans **Paramètres > Paramètres du développeur > Jeton d'accès personnel**

![screenshot](https://www.freecodecamp.org/news/content/images/2022/04/screenshot.png align="left")

![screenshot_1](https://www.freecodecamp.org/news/content/images/2022/04/screenshot_1.png align="left")

![screenshot_2](https://www.freecodecamp.org/news/content/images/2022/04/screenshot_2.png align="left")

* Super, nous avons presque terminé maintenant ! Ce dont nous avons besoin maintenant, c'est l'**URL distante** de notre nouveau dépôt GitHub.
    

Pour l'obtenir, nous allons utiliser curl et l'API GitHub à nouveau, comme ceci :

```plaintext
GIT_URL=$(curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/coccagerman/"$repoName" | jq -r '.clone_url')
```

Ici, nous déclarons une variable appelée `GIT_URL` et nous l'assignons à ce que la commande suivante retourne.

Le flag `-H` définit l'en-tête de notre requête.

Ensuite, nous passons le point de terminaison de l'API GitHub, qui doit contenir notre nom d'utilisateur et le nom du dépôt (`https://api.github.com/repos/coccagerman/"$repoName"`).

Ensuite, nous **pipons** la valeur de retour de notre requête. Piping signifie simplement passer la valeur de retour d'un processus comme valeur d'entrée d'un autre processus. Nous pouvons le faire avec le symbole `|` comme `<process1> | <process2>`.

Et enfin, nous exécutons la commande `jq`, qui est un outil pour traiter les entrées JSON. Ici, nous lui disons d'obtenir la valeur de `.clone_url` qui est là où notre URL git distante sera selon le format de données fourni par l'API GitHub.

* Et comme dernière étape, nous renommons notre branche master en main, ajoutons l'origine distante que nous venons d'obtenir, et poussons notre code vers GitHub ! =D
    

```plaintext
git branch -M main
git remote add origin $GIT_URL
git push -u origin main
```

Notre script complet devrait ressembler à ceci :

```plaintext
#! /bin/sh
repoName=$1

while [ -z "$repoName" ]
do
    echo 'Fournissez un nom de dépôt'
    read -r -p $'Nom du dépôt :' repoName
done

echo "# $repoName" >> README.md
git init
git add .
git commit -m "First commit"

curl -u <yourUserName> https://api.github.com/user/repos -d '{"name": "'"$repoName"'", "private":false}'

GIT_URL=$(curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/<yourUserName>/"$repoName" | jq -r '.clone_url')

git branch -M main
git remote add origin $GIT_URL
git push -u origin main
```

* Maintenant, il est temps de tester notre script ! Pour l'**exécuter**, il y a deux choses que nous pouvons faire.
    

Une option est d'entrer le nom du shell et de passer le fichier comme paramètre, comme : `dash ../ger/code/projects/scripts/newGhRepo.sh`.

Et l'autre est de rendre le fichier **exécutable** en exécutant `chmod u+x ../ger/code/projects/scripts/newGhRepo.sh`.

Ensuite, vous pouvez simplement exécuter le fichier directement en exécutant `../ger/code/projects/scripts/newGhRepo.sh`.

Et c'est tout ! Nous avons notre script opérationnel. Chaque fois que nous avons besoin d'un nouveau dépôt, nous pouvons simplement exécuter ce script depuis n'importe quel répertoire où nous nous trouvons.

Mais il y a quelque chose d'un peu ennuyeux à propos de cela. Nous devons nous souvenir du chemin exact du répertoire du script. Ne serait-ce pas cool d'exécuter le script avec une seule commande qui est toujours la même indépendamment du répertoire où nous nous trouvons ?

Les **alias bash** arrivent pour résoudre notre problème.

Les alias sont un moyen que bash fournit pour créer des noms pour des commandes exactes que nous voulons exécuter.

Pour créer un nouvel alias, nous devons modifier les fichiers de configuration bash dans notre système. Ces fichiers sont normalement situés dans le répertoire personnel. Les alias peuvent être définis dans différents fichiers (principalement `.bashrc` ou `.bash_aliases`).

J'ai un fichier `.bash_aliases` sur mon système, alors éditons celui-ci.

* Dans notre CLI, nous entrons `cd` pour aller dans le répertoire personnel.
    
* Ensuite, nous pouvons entrer `ls -a` pour lister tous les fichiers (y compris les fichiers cachés) et vérifier si nous avons un fichier `.bashrc` ou `.bash_aliases` dans notre système.
    
* Nous ouvrons le fichier avec notre éditeur de texte/code de choix.
    
* Et nous écrivons notre nouvel alias comme ceci : `alias newghrepo="dash /home/German/Desktop/ger/code/projects/scripts/newGhRepo.sh"`
    

Ici, je déclare le nom de l'alias, la commande réelle que je vais entrer pour exécuter le script (`newghrepo`).

Et entre guillemets, définir ce que cet alias va faire (`"dash /home/German/Desktop/ger/code/projects/scripts/newGhRepo.sh"`)

Voyez que je passe le [chemin absolu](https://www.computerhope.com/issues/ch001708.htm) du script, afin que cette commande fonctionne de la même manière peu importe quel est mon répertoire actuel.

Si vous ne savez pas quel est le chemin absolu de votre script, allez dans le répertoire du script sur votre terminal et entrez `readlink -f newGhRepo.sh`. Cela devrait vous retourner le chemin complet. ;)

* Après avoir terminé l'édition, nous sauvegardons notre fichier, redémarrons notre terminal, et voilà ! Maintenant, nous pouvons exécuter notre script en entrant simplement `newghrepo`, peu importe dans quel répertoire nous nous trouvons actuellement. Bien plus rapide que d'ouvrir le navigateur et de cliquer pour créer notre dépôt ! =D
    

J'espère que cela vous donne un petit aperçu du type d'optimisations qui sont possibles avec le scripting. Cela nécessite certainement un peu plus de travail la première fois que vous écrivez, testez et configurez le script. Mais après cela, vous n'aurez plus jamais à effectuer cette tâche manuellement. ;)

# Conclusion

Le terminal peut sembler un endroit intimidant et complexe lorsque vous débutez. Mais cela vaut certainement la peine de consacrer du temps et des efforts à apprendre les tenants et les aboutissants de celui-ci. Les avantages en termes d'efficacité sont trop bons pour être ignorés !

> Si vous êtes intéressé à en apprendre davantage sur le terminal et Bash, Zach Gollwitzer a [une série de cours intensifs géniale sur YouTube](https://www.youtube.com/playlist?list=PLYQSCk-qyTW0d88jNocdi_YIFMA5Fnpug). Il a également d'excellents tutoriels sur d'autres sujets tels que Node et JavaScript, donc je vous recommande de le suivre. ;)

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [linkedin](https://www.linkedin.com/in/germancocca/) ou [twitter](https://twitter.com/CoccaGerman).

À bientôt et à la prochaine ! =D

![8ef61e333efccb5900cd117a4d64e8d3](https://www.freecodecamp.org/news/content/images/2022/04/8ef61e333efccb5900cd117a4d64e8d3.gif align="left")