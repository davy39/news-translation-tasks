---
title: Le Guide Ultime de la Ligne de Commande Linux - Tutoriel Complet sur Bash
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-19T17:49:00.000Z'
originalURL: https://freecodecamp.org/news/linux-command-line-bash-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f2f740569d1a4ca4141.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Le Guide Ultime de la Ligne de Commande Linux - Tutoriel Complet sur Bash
seo_desc: 'Welcome to our ultimate guide to the Linux Command Line. This tutorial
  will show you some of the key Linux command line technologies and introduce you
  to the Bash scripting language.

  What is Bash?

  Bash (short for Bourne Again SHell) is a Unix shell, ...'
---

Bienvenue dans notre guide ultime de la ligne de commande Linux. Ce tutoriel vous présentera certaines des technologies clés de la ligne de commande Linux et vous initiera au langage de script Bash.

## **Qu'est-ce que Bash ?**

[Bash](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/) (abréviation de Bourne Again SHell) est un shell Unix et un interpréteur de langage de commande. Un shell est simplement un processeur de macros qui exécute des commandes. C'est le shell le plus largement utilisé, inclus par défaut dans la plupart des distributions Linux, et un successeur du shell Korn (ksh) et du shell C (csh).

De nombreuses choses qui peuvent être faites sur un système d'exploitation Linux peuvent être réalisées via la ligne de commande. Voici quelques exemples :

* Éditer des fichiers
* Ajuster le volume du système d'exploitation
* Récupérer des pages web depuis Internet
* Automatiser le travail que vous faites chaque jour

Vous pouvez en savoir plus sur bash [ici](https://www.gnu.org/software/bash/), via la [Documentation GNU](https://www.gnu.org/software/bash/manual/html_node/index.html#SEC_Contents), et via le [guide tldp](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html#toc10).

## **Utilisation de bash sur la ligne de commande (Linux, OS X)**

Vous pouvez commencer à utiliser bash sur la plupart des systèmes d'exploitation Linux et OS X en ouvrant un terminal. Considérons un simple exemple "Hello World". Ouvrez votre terminal et écrivez la ligne suivante (tout ce qui suit le signe $) :

```text
zach@marigold:~$ echo "Hello world!"
Hello world!
```

Comme vous pouvez le voir, nous avons utilisé la commande echo pour imprimer la chaîne "Hello world!" dans le terminal.

## **Écrire un script bash**

Vous pouvez également mettre toutes vos commandes bash dans un fichier .sh et les exécuter depuis la ligne de commande. Supposons que vous avez un script bash avec le contenu suivant :

```text
#!/bin/bash
echo "Hello world!"
```

Il est important de noter que la première ligne du script commence par `#!`. C'est une directive spéciale que Unix traite différemment.

#### **Pourquoi avons-nous utilisé #!/bin/bash au début du fichier de script ?**

C'est parce qu'il est conventionnel de faire savoir à l'interpréteur de shell interactif quel type d'interpréteur exécuter pour le programme qui suit. La première ligne indique à Unix que le fichier doit être exécuté par /bin/bash. C'est l'emplacement standard du shell Bourne sur presque tous les systèmes Unix. Ajouter #!/bin/bash comme première ligne de votre script indique au système d'exploitation d'invoquer le shell spécifié pour exécuter les commandes qui suivent dans le script. `#!` est souvent appelé "hash-bang", "she-bang" ou "sha-bang". Bien qu'il ne soit exécuté que si vous exécutez votre script en tant qu'exécutable. Par exemple, lorsque vous tapez `./scriptname.extension`, il regardera la première ligne pour trouver l'interpréteur, alors que l'exécution du script en tant que `bash scriptname.sh` ignore la première ligne.

Vous pourriez alors exécuter le script comme suit : Pour rendre le fichier exécutable, vous devez appeler cette commande sous sudo chmod +x "nomdefichier".

```text
zach@marigold:~$ ./myBashScript.sh
Hello world!
```

Le script ne contient que deux lignes. La première indique quel interpréteur utiliser pour exécuter le fichier (dans ce cas, bash). La deuxième ligne est la commande que nous voulons utiliser, echo, suivie de ce que nous voulons imprimer, à savoir "Hello World".

Parfois, le script ne sera pas exécuté et la commande ci-dessus retournera une erreur. Cela est dû aux permissions définies sur le fichier. Pour éviter cela, utilisez :

```text
zach@marigold:~$ chmod u+x myBashScript.sh
```

Puis exécutez le script.

## **Ligne de Commande Linux : Bash Cat**

Cat est l'une des commandes les plus fréquemment utilisées dans les systèmes d'exploitation Unix.

Cat est utilisé pour lire un fichier séquentiellement et l'imprimer sur la sortie standard. Le nom est dérivé de sa fonction de con**cat**énation de fichiers.

### **Utilisation**

```bash
cat [options] [file_names]
```

Options les plus utilisées :

* `-b`, numérote les lignes de sortie non vides
* `-n`, numérote toutes les lignes de sortie
* `-s`, supprime les lignes vides adjacentes multiples
* `-v`, affiche les caractères non imprimables, à l'exception des tabulations et du caractère de fin de ligne

### **Exemple**

Affiche dans le terminal le contenu de file.txt :

```bash
cat file.txt
```

Concatène le contenu des deux fichiers et affiche le résultat dans le terminal :

```bash
cat file1.txt file2.txt
```

## Ligne de Commande Linux : Bash cd

**Change de Répertoire** vers le chemin spécifié, par exemple `cd projects`.

Il existe quelques arguments vraiment utiles pour aider cela :

* `.` fait référence au répertoire courant, comme `./projects`
* `..` peut être utilisé pour remonter d'un dossier, utilisez `cd ..`, et peut être combiné pour remonter de plusieurs niveaux `../../my_folder`
* `/` est la racine de votre système pour atteindre les dossiers principaux, comme `system`, `users`, etc.
* `~` est le répertoire personnel, généralement le chemin `/users/username`. Revenez aux dossiers référencés par rapport à ce chemin en l'incluant au début de votre chemin, par exemple `~/projects`.

## Ligne de Commande Linux : Bash head

Head est utilisé pour imprimer les dix premières lignes (par défaut) ou tout autre nombre spécifié d'un fichier ou de fichiers. Cat est utilisé pour lire un fichier séquentiellement et l'imprimer sur la sortie standard.   

Il imprime tout le contenu du fichier entier. - ce n'est pas toujours nécessaire, peut-être voulez-vous simplement vérifier le contenu d'un fichier pour voir s'il est le bon, ou vérifier qu'il n'est effectivement pas vide. La commande head vous permet de voir les N premières lignes d'un fichier.

Si plus d'un fichier est appelé, les dix premières lignes de chaque fichier sont affichées, sauf si un nombre spécifique de lignes est précisé. Choisir d'afficher l'en-tête du fichier est optionnel en utilisant l'option ci-dessous.

### **Utilisation**

```bash
head [options] [file_name(s)]
```

Options les plus utilisées :

* `-n N`, imprime les N premières lignes du ou des fichiers
* `-q`, n'imprime pas les en-têtes des fichiers
* `-v`, imprime toujours les en-têtes des fichiers

### **Exemple**

```bash
head file.txt
```

Imprime dans le terminal les dix premières lignes de file.txt (par défaut)

```bash
head -n 7 file.txt
```

Imprime dans le terminal les sept premières lignes de file.txt

```bash
head -q -n 5 file1.txt file2.txt
```

Imprime dans le terminal les 5 premières lignes de file1.txt, suivies des 5 premières lignes de file2.txt

Ligne de Commande Linux : Bash ls

`ls` est une commande sur les systèmes d'exploitation de type Unix pour lister le contenu d'un répertoire, par exemple les noms de dossiers et de fichiers.

### **Utilisation**

```bash
ls [options] [file_names]
```

Options les plus utilisées :

* `-a`, tous les fichiers et dossiers, y compris ceux qui sont cachés et commencent par un `.`
* `-l`, Liste au format long
* `-G`, active la sortie colorisée.

### **Exemple :**

Lister les fichiers dans `freeCodeCamp/guide/`

```bash
ls                                                                 master
CODE_OF_CONDUCT.md bin                package.json       utils
CONTRIBUTING.md    gatsby-browser.js  plugins            yarn.lock
LICENSE.md         gatsby-config.js   src
README.md          gatsby-node.js     static
assets             gatsby-ssr.js      translations
```

## Ligne de Commande Linux : Bash man

Man, l'abréviation de **man**uel, est une commande bash utilisée pour afficher les pages de manuel de référence en ligne de la commande donnée.

Man affiche la page de manuel relative (abréviation de **man**uel **page**) de la commande donnée.

### **Utilisation**

```bash
man [options] [command]
```

Options les plus utilisées :

* `-f`, imprime une courte description de la commande donnée
* `-a`, affiche, successivement, toutes les pages de manuel d'introduction disponibles contenues dans le manuel

### **Exemple**

Affiche la page de manuel de ls :

```bash
man ls
```

## Ligne de Commande Linux : Bash mv

**Déplace des fichiers et des dossiers.**

```text
mv source target
mv source ... directory
```

Le premier argument est le fichier que vous souhaitez déplacer, et le second est l'emplacement où le déplacer.

Options couramment utilisées :

* `-f` pour forcer le déplacement et écraser les fichiers sans vérifier avec l'utilisateur.
* `-i` pour demander confirmation avant d'écraser les fichiers.

C'est tout. Allez de l'avant et utilisez Linux.