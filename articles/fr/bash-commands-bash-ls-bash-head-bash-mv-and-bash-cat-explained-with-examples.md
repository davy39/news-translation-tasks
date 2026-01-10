---
title: 'Commandes Bash : Bash ls, Bash head, Bash mv et Bash cat expliquées avec des
  exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T22:27:00.000Z'
originalURL: https://freecodecamp.org/news/bash-commands-bash-ls-bash-head-bash-mv-and-bash-cat-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e1a740569d1a4ca3b5c.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: 'Commandes Bash : Bash ls, Bash head, Bash mv et Bash cat expliquées avec
  des exemples'
seo_desc: 'Bash ls

  ls is a command on Unix-like operating systems to list contents of a directory,
  for example folder and file names.

  Usage

  cat [options] [file_names]


  Most used options:


  -a, all files and folders, including ones that are hidden and start with ...'
---

## **Bash ls**

`ls` est une commande sur les systèmes d'exploitation de type Unix pour lister le contenu d'un répertoire, par exemple les noms de dossiers et de fichiers.

### **Utilisation**

```bash
ls [options] [noms_de_fichiers]
```

Options les plus utilisées :

* `-a`, tous les fichiers et dossiers, y compris ceux qui sont cachés et commencent par un `.`
* `-l`, liste tous les fichiers au format long
* `-G`, active la sortie colorisée

### **Exemple :**

Lister les fichiers dans `freeCodeCamp/guide/`

Après avoir cloné le dépôt principal [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp), voici la sortie après avoir exécuté `ls` dans le répertoire `freeCodeCamp` :

```bash
api-server                 docker-compose.yml  public
change_volumes_owner.sh    Dockerfile.tests    README.md
client                     docs                sample.env
CODE_OF_CONDUCT.md         HoF.md              search-indexing
config                     lerna.json          SECURITY.md
CONTRIBUTING.md            LICENSE.md          server
curriculum                 node_modules        tools
docker-compose-shared.yml  package.json        utils
docker-compose.tests.yml   package-lock.json
```

## Plus de commandes bash

### Bash Head

`head` est utilisé pour afficher les dix premières lignes (par défaut) ou tout autre nombre spécifié d'un fichier ou de fichiers. `cat`, en revanche, est utilisé pour lire un fichier séquentiellement et l'afficher sur la sortie standard (c'est-à-dire qu'il affiche l'intégralité du contenu du fichier).

Ce n'est pas toujours nécessaire, cependant – peut-être voulez-vous simplement vérifier le contenu d'un fichier pour voir s'il est le bon, ou vérifier qu'il n'est effectivement pas vide. La commande `head` vous permet de voir les N premières lignes d'un fichier.

Si plus d'un fichier est appelé, alors les dix premières lignes de chaque fichier sont affichées, sauf si un nombre spécifique de lignes est spécifié. Choisir d'afficher l'en-tête du fichier est optionnel en utilisant l'option ci-dessous.

### **Utilisation**

```bash
head [options] [nom_de_fichier(s)]
```

Options les plus utilisées :

* `-n N`, affiche les N premières lignes du ou des fichiers
* `-q`, n'affiche pas les en-têtes des fichiers
* `-v`, affiche toujours les en-têtes des fichiers

### **Exemple**

```bash
head file.txt
```

Affiche les dix premières lignes de file.txt (par défaut)

```bash
head -n 7 file.txt
```

Affiche les sept premières lignes de file.txt

```bash
head -q -n 5 file1.txt file2.txt
```

Affiche les 5 premières lignes de file1.txt, suivies des 5 premières lignes de file2.txt

## **Bash mv**

Cette commande bash déplace des fichiers et des dossiers.

```text
mv source cible
mv source ... répertoire
```

Le premier argument est le fichier que vous souhaitez déplacer, et le second est l'emplacement où le déplacer.

Options couramment utilisées :

* `-f` pour forcer le déplacement et écraser les fichiers sans demander confirmation à l'utilisateur.
* `-i` pour demander confirmation avant d'écraser les fichiers.

## **Bash Cat**

`cat` est l'une des commandes les plus fréquemment utilisées dans les systèmes d'exploitation Unix.

`cat` est utilisé pour lire un fichier séquentiellement et l'afficher sur la sortie standard. Le nom vient de la manière dont il peut con**cat**éner les fichiers.

### **Utilisation**

```bash
cat [options] [noms_de_fichiers]
```

Options les plus utilisées :

* `-b`, numérote les lignes de sortie non vides
* `-n`, numérote toutes les lignes de sortie
* `-s`, supprime les lignes vides adjacentes multiples
* `-v`, affiche les caractères non imprimables, à l'exception des tabulations et du caractère de fin de ligne

### **Exemple**

Afficher le contenu de file.txt :

```bash
cat file.txt
```

Concaténer le contenu des deux fichiers et afficher le résultat dans le terminal :

```bash
cat file1.txt file2.txt
```

## Plus d'informations sur Bash :

### Qu'est-ce que Bash ?

[Bash](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/) (abréviation de Bourne Again SHell) est un shell Unix et un interpréteur de langage de commande. Un shell est simplement un processeur de macros qui exécute des commandes. C'est le shell le plus largement utilisé, fourni par défaut pour la plupart des distributions Linux, et un successeur du Korn shell (ksh) et du C shell (csh).

De nombreuses choses qui peuvent être faites dans l'interface graphique d'un système d'exploitation Linux peuvent être faites via la ligne de commande. Voici quelques exemples :

* Éditer des fichiers
* Ajuster le volume du système d'exploitation
* Récupérer des pages web depuis Internet
* Automatiser le travail que vous faites tous les jours

Vous pouvez en savoir plus sur bash [ici](https://www.gnu.org/software/bash/), via la [Documentation GNU](https://www.gnu.org/software/bash/manual/html_node/index.html#SEC_Contents), et via le [guide tldp](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html#toc10).

## **Utilisation de bash sur la ligne de commande (Linux, OS X)**

Vous pouvez commencer à utiliser bash sur la plupart des systèmes d'exploitation Linux et OS X en ouvrant un terminal. Considérons un simple exemple hello world. Ouvrez votre terminal et écrivez la ligne suivante (tout ce qui suit le signe $) :

```text
zach@marigold:~$ echo "Hello world!"
Hello world!
```

Comme vous pouvez le voir, nous avons utilisé la commande echo pour afficher la chaîne « Hello world! » dans le terminal.

## **Écrire un script bash**

Vous pouvez également mettre toutes vos commandes bash dans un fichier .sh et les exécuter depuis la ligne de commande. Supposons que vous avez un script bash avec le contenu suivant :

```text
#!/bin/bash
echo "Hello world!"
```

Ce script ne contient que deux lignes. La première indique quel interpréteur utiliser pour exécuter le fichier (dans ce cas, bash). La deuxième ligne est la commande que nous voulons utiliser, `echo`, suivie de ce que nous voulons afficher, ici, "Hello world!"

Il est intéressant de noter que la première ligne du script commence par `#!`. Il s'agit d'une directive spéciale que Unix traite différemment.

#### **Pourquoi avons-nous utilisé #!/bin/bash au début du fichier de script ?**

C'est parce que c'est une convention pour faire savoir à l'interpréteur interactif quel type d'interpréteur exécuter pour le programme qui suit.

La première ligne indique au système d'exploitation que le fichier doit être exécuté par le programme situé à `/bin/bash`, l'emplacement standard du Bourne shell sur presque tous les systèmes Unix ou de type Unix. En ajoutant `#!/bin/bash` au début du script, cela indique au système d'exploitation d'utiliser le shell à ce chemin spécifique pour exécuter toutes les commandes suivantes dans le script.

`#!` est connu sous de nombreux noms tels que "hash-bang", "she-bang", "sha-bang", ou "crunch-bang". Notez que cette première ligne n'est prise en compte que si le script est un exécutable.

Par exemple, si `myBashScript.sh` est exécutable, la commande `./myBashScript.sh` amènera le système d'exploitation à regarder la première ligne pour déterminer quel interpréteur utiliser. Dans ce cas, ce serait `#!/bin/bash`.

D'autre part, si vous exécutez `bash myBashScript.sh`, alors la première ligne est ignorée puisque le système d'exploitation sait déjà utiliser bash.

Pour rendre `myBashScript.sh` exécutable, exécutez simplement `sudo chmod +x myBashScript.sh`. Ensuite, exécutez la commande suivante pour exécuter le script :

```text
zach@marigold:~$ ./myBashScript.sh
Hello world!
```

Parfois, le script ne sera pas exécuté et la commande ci-dessus retournera une erreur. Cela est dû aux permissions définies sur le fichier. Pour éviter cela, utilisez :

```text
zach@marigold:~$ chmod u+x myBashScript.sh
```

Puis exécutez le script.