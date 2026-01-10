---
title: Le Scripting Shell pour les Débutants – Comment Écrire des Scripts Bash sous
  Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-31T19:26:38.000Z'
originalURL: https://freecodecamp.org/news/shell-scripting-crash-course-how-to-write-bash-scripts-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/remove-key-val.gif
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: shell script
  slug: shell-script
seo_title: Le Scripting Shell pour les Débutants – Comment Écrire des Scripts Bash
  sous Linux
seo_desc: 'Shell scripting is an important part of process automation in Linux. Scripting
  helps you write a sequence of commands in a file and then execute them.

  This saves you time because you don''t have to write certain commands again and
  again. You can perfo...'
---

Le scripting shell est un élément important de l'automatisation des processus sous Linux. Le scripting vous aide à écrire une séquence de commandes dans un fichier puis à les exécuter.

Cela vous fait gagner du temps car vous n'avez pas à écrire certaines commandes à plusieurs reprises. Vous pouvez effectuer des tâches quotidiennes efficacement et même les planifier pour une exécution automatique.

Vous pouvez également configurer certains scripts pour qu'ils s'exécutent au démarrage, par exemple pour afficher un message particulier lors du lancement d'une nouvelle session ou pour définir certaines variables d'environnement.

Les applications et les utilisations du scripting sont nombreuses, alors plongeons dans le vif du sujet.

Dans cet article, vous apprendrez :

1. Qu'est-ce qu'un shell bash ?
    
2. Qu'est-ce qu'un script bash et comment l'identifier ?
    
3. Comment créer votre premier script bash et l'exécuter.
    
4. La syntaxe de base du scripting shell.
    
5. Comment voir les scripts planifiés d'un système.
    
6. Comment automatiser des scripts en les planifiant via des tâches cron.
    

La meilleure façon d'apprendre est de pratiquer. Je vous encourage vivement à suivre en utilisant [Replit](https://replit.com/~). Vous pouvez accéder à un shell Linux fonctionnel en quelques minutes.

## Introduction au Shell Bash

La ligne de commande Linux est fournie par un programme appelé le shell. Au fil des ans, le programme shell a évolué pour proposer diverses options.

Différents utilisateurs peuvent être configurés pour utiliser différents shells. Mais la plupart des utilisateurs préfèrent s'en tenir au shell par défaut actuel. Le shell par défaut pour de nombreuses distributions Linux est le GNU Bourne-Again Shell (bash). Bash a succédé au shell Bourne (`sh`).

Lorsque vous lancez le shell pour la première fois, il utilise un script de démarrage situé dans le fichier `.bashrc` ou `.bash_profile` qui vous permet de personnaliser le comportement du shell.

Lorsqu'un shell est utilisé de manière interactive, il affiche un `$` lorsqu'il attend une commande de l'utilisateur. C'est ce qu'on appelle l'invite du shell (shell prompt).

`[username@host ~]$`

Si le shell s'exécute en tant que root, l'invite est changée en `#`. L'invite du shell du superutilisateur ressemble à ceci :

`[root@host ~]#`

Bash est très puissant car il peut simplifier certaines opérations difficiles à accomplir efficacement avec une interface graphique (GUI). N'oubliez pas que la plupart des serveurs n'ont pas de GUI, et il est préférable d'apprendre à utiliser les pouvoirs d'une interface de ligne de commande (CLI).

## Qu'est-ce qu'un Script Bash ?

Un script bash est une série de commandes écrites dans un fichier. Celles-ci sont lues et exécutées par le programme bash. Le programme s'exécute ligne par ligne.

Par exemple, vous pouvez naviguer vers un certain chemin, créer un dossier et lancer un processus à l'intérieur en utilisant la ligne de commande.

Vous pouvez effectuer la même séquence d'étapes en enregistrant les commandes dans un script bash et en l'exécutant. Vous pouvez exécuter le script autant de fois que vous le souhaitez.

## Comment Identifier un Script Bash ?

### Extension de fichier en `.sh`.

Par convention de nommage, les scripts bash se terminent par un `.sh`. Cependant, les scripts bash peuvent parfaitement s'exécuter sans l'extension `sh`.

### Les scripts commencent par un bash bang.

Les scripts sont également identifiés par un `shebang`. Le shebang est une combinaison de `bash #` et `bang !` suivie du chemin du shell bash. C'est la première ligne du script. Le shebang indique au shell de l'exécuter via le shell bash. Le shebang est simplement un chemin absolu vers l'interpréteur bash.

Voici un exemple de l'instruction shebang.

```bash
#! /bin/bash
```

Le chemin du programme bash peut varier. Nous verrons plus tard comment l'identifier.

### Droits d'exécution

Les scripts ont des droits d'exécution pour l'utilisateur qui les exécute.

Un droit d'exécution est représenté par `x`. Dans l'exemple ci-dessous, mon utilisateur a les droits `rwx` (lecture, écriture, exécution) pour le fichier `test_script.sh`

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-98.png align="left")

### Couleur du fichier

Les scripts exécutables apparaissent dans une couleur différente du reste des fichiers et dossiers.

Dans mon cas, les scripts avec des droits d'exécution apparaissent en vert.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-99.png align="left")

## Comment Créer votre Premier Script Bash

Créons un script simple en bash qui affiche `Hello World`.

### Créer un fichier nommé hello\_world.sh

```bash
touch hello_world.sh
```

### Trouver le chemin de votre shell bash.

```bash
which bash
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-100.png align="left")

Dans mon cas, le chemin est `/usr/bin/bash` et je l'inclurai dans le shebang.

### Écrire la commande.

Nous allons utiliser `echo` pour afficher "hello world" dans la console.

Notre script ressemblera à ceci :

```bash
#! /usr/bin/bash
echo "Hello World"
```

Modifiez le fichier `hello_world.sh` à l'aide d'un éditeur de texte de votre choix et ajoutez-y les lignes ci-dessus.

### Donner les droits d'exécution à votre utilisateur.

Modifiez les permissions du fichier et autorisez l'exécution du script en utilisant la commande ci-dessous :

```bash
chmod u+x hello_world.sh
```

`chmod` modifie les droits existants d'un fichier pour un utilisateur particulier. Nous ajoutons `+x` à l'utilisateur `u`.

### Exécuter le script.

Vous pouvez exécuter le script des manières suivantes :

`./hello_world.sh`

`bash hello_world.sh`.

**Voici le résultat :**

![Deux façons d'exécuter des scripts](https://www.freecodecamp.org/news/content/images/2022/03/image-160.png align="left")

*Deux façons d'exécuter des scripts*

## La Syntaxe de Base du Scripting Bash

Comme tout autre langage de programmation, le scripting bash suit un ensemble de règles pour créer des programmes compréhensibles par l'ordinateur. Dans cette section, nous allons étudier la syntaxe du scripting bash.

### Comment définir des variables

Nous pouvons définir une variable en utilisant la syntaxe `nom_variable=valeur`. Pour obtenir la valeur de la variable, ajoutez `$` avant la variable.

```bash
#!/bin/bash
# Un exemple simple de variable
greeting=Hello
name=Tux
echo $greeting $name
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-104.png align="left")

Tux est aussi le nom de la mascotte de Linux, le manchot.

![Salut, je suis Tux.](https://www.freecodecamp.org/news/content/images/2022/03/image-119.png align="left")

*Salut, je suis Tux.*

### Expressions Arithmétiques

Voici les opérateurs supportés par bash pour les calculs mathématiques :

| Opérateur | Utilisation |
| --- | --- |
| + | addition |
| \- | soustraction |
| \* | multiplication |
| / | division |
| \*\* | exponentiation |
| % | modulo |

Voyons quelques exemples.

![Notez les espaces, ils font partie de la syntaxe](https://www.freecodecamp.org/news/content/images/2022/03/image-108.png align="left")

*Notez les espaces, ils font partie de la syntaxe*

Les expressions numériques peuvent également être calculées et stockées dans une variable en utilisant la syntaxe ci-dessous :

`var=$((expression))`

Essayons un exemple.

```bash
#!/bin/bash

var=$((3+9))
echo $var
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-109.png align="left")

Les fractions ne sont pas calculées correctement avec les méthodes ci-dessus et sont tronquées.

Pour les **calculs décimaux**, nous pouvons utiliser la commande `bc` pour obtenir le résultat avec un nombre particulier de décimales. `bc` (Bash Calculator) est une calculatrice en ligne de commande qui prend en charge les calculs jusqu'à un certain nombre de points décimaux.

`echo "scale=2;22/7" | bc`

Où `scale` définit le nombre de décimales requises dans le résultat.

![Obtenir un résultat avec 2 décimales](https://www.freecodecamp.org/news/content/images/2022/03/image-110.png align="left")

*Obtenir un résultat avec 2 décimales*

### Comment lire les entrées de l'utilisateur

Parfois, vous aurez besoin de recueillir les entrées de l'utilisateur et d'effectuer les opérations correspondantes.

En bash, nous pouvons récupérer l'entrée de l'utilisateur en utilisant la commande `read`.

```bash
read nom_variable
```

Pour inviter l'utilisateur avec un message personnalisé, utilisez le drapeau `-p`.

`read -p "Entrez votre âge" nom_variable`

**Exemple :**

```bash
#!/bin/bash

echo "Entrez un nombre"
read a

echo "Entrez un nombre"
read b

var=$((a+b))
echo $var
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-111.png align="left")

### Opérateurs logiques de comparaison numérique

La comparaison est utilisée pour vérifier si des instructions sont évaluées à `vrai` (true) ou `faux` (false). Nous pouvons utiliser les opérateurs présentés ci-dessous pour comparer deux instructions :

| Opération | Syntaxe | Explication |
| --- | --- | --- |
| Égalité | num1 -eq num2 | num1 est-il égal à num2 |
| Supérieur ou égal à | num1 -ge num2 | num1 est-il supérieur ou égal à num2 |
| Supérieur à | num1 -gt num2 | num1 est-il supérieur à num2 |
| Inférieur ou égal à | num1 -le num2 | num1 est-il inférieur ou égal à num2 |
| Inférieur à | num1 -lt num2 | num1 est-il inférieur à num2 |
| Non Égal à | num1 -ne num2 | num1 est-il différent de num2 |

**Syntaxe** :

```bash
if [ conditions ]
    then
         commands
fi
```

**Exemple** :

Comparons deux nombres et trouvons leur relation :

```bash
read x
read y

if [ $x -gt $y ]
then
echo X est plus grand que Y
elif [ $x -lt $y ]
then
echo X est plus petit que Y
elif [ $x -eq $y ]
then
echo X est égal à Y
fi
```

Résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-112.png align="left")

### Instructions Conditionnelles (Prise de Décision)

Les conditions sont des expressions qui s'évaluent en un booléen (`true` ou `false`). Pour vérifier les conditions, nous pouvons utiliser `if`, `if-else`, `if-elif-else` et des conditions imbriquées.

La structure des instructions conditionnelles est la suivante :

* instructions `if...then...fi` 
    
* instructions `if...then...else...fi` 
    
* instructions `if..elif..else..fi` 
    
* instructions `if..then..else..if..then..fi..fi..` (Conditions imbriquées)
    

**Syntaxe** :

```bash
if [[ condition ]]
then
	statement
elif [[ condition ]]; then
	statement 
else
	do this by default
fi
```

Pour créer des comparaisons significatives, nous pouvons également utiliser AND `-a` et OR `-o`.

L'instruction ci-dessous se traduit par : Si `a` est supérieur à 40 et `b` est inférieur à 6.

`if [ $a -gt 40 -a $b -lt 6 ]`

**Exemple** : Trouvons le type de triangle en lisant les longueurs de ses côtés.

```bash
read a
read b
read c

if [ $a == $b -a $b == $c -a $a == $c ]
then
echo EQUILATERAL

elif [ $a == $b -o $b == $c -o $a == $c ]
then 
echo ISOSCELE
else
echo SCALENE

fi
```

**Résultat** :

Cas de test #1

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-113.png align="left")

Cas de test #2

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-114.png align="left")

Cas de test #3

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-115.png align="left")

### Boucles et sauts

Les boucles For vous permettent d'exécuter des instructions un nombre spécifique de fois.

#### Boucler avec des nombres :

Dans l'exemple ci-dessous, la boucle itérera 5 fois.

```bash
#!/bin/bash

for i in {1..5}
do
    echo $i
done
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Looping-with-numbers.png align="left")

#### Boucler avec des chaînes de caractères :

Nous pouvons également boucler à travers des chaînes.

```bash
#!/bin/bash

for X in cyan magenta yellow  
do
	echo $X
done
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Looping-with-strings.PNG align="left")

#### Boucle While

Les boucles While vérifient une condition et bouclent tant que la condition reste `vraie`. Nous devons fournir une instruction de compteur qui incrémente le compteur pour contrôler l'exécution de la boucle.

Dans l'exemple ci-dessous, `(( i += 1 ))` est l'instruction de compteur qui incrémente la valeur de `i`.

**Exemple :**

```bash
#!/bin/bash
i=1
while [[ $i -le 10 ]] ; do
   echo "$i"
  (( i += 1 ))
done
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-153.png align="left")

### Lecture de fichiers

Supposons que nous ayons un fichier `sample_file.txt` comme illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-151.png align="left")

Nous pouvons lire le fichier ligne par ligne et afficher le résultat à l'écran.

```bash
#!/bin/bash

LINE=1

while read -r CURRENT_LINE
	do
		echo "$LINE: $CURRENT_LINE"
    ((LINE++))
done < "sample_file.txt"
```

**Résultat :**

![Lignes imprimées avec numéro de ligne](https://www.freecodecamp.org/news/content/images/2022/03/image-152.png align="left")

*Lignes imprimées avec numéro de ligne*

### Comment exécuter des commandes avec des accents graves (backticks)

Si vous devez inclure la sortie d'une commande complexe dans votre script, vous pouvez écrire l'instruction à l'intérieur d'accents graves.

#### Syntaxe :

var= commandes

**Exemple** : Supposons que nous voulions obtenir la liste des points de montage contenant `tmpfs` dans leur nom. Nous pouvons formuler une instruction comme celle-ci : `df -h | grep tmpfs`.

Pour l'inclure dans le script bash, nous pouvons l'entourer d'accents graves.

```bash
#!/bin/bash

var=`df -h | grep tmpfs`
echo $var
```

Résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-118.png align="left")

### Comment obtenir des arguments pour les scripts depuis la ligne de commande

Il est possible de donner des arguments au script lors de l'exécution.

`$@` représente la position des paramètres, en commençant par un.

```bash
#!/bin/bash

for x in $@
do
    echo "L'argument saisi est $x"
done
```

Exécutez-le comme ceci :

`./script arg1 arg2`

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-155.png align="left")

## Comment Automatiser des Scripts en les Planifiant via des Tâches Cron

Cron est un utilitaire de planification de tâches présent dans les systèmes de type Unix. Vous pouvez planifier des tâches pour qu'elles s'exécutent quotidiennement, hebdomadairement, mensuellement ou à une heure précise de la journée. L'automatisation sous Linux repose largement sur les tâches cron.

Voici la syntaxe pour planifier des crons :

```bash
# Exemple de tâche cron
* * * * * sh /chemin/vers/script.sh
```

Ici, `*` représente respectivement minute(s) heure(s) jour(s) mois jour(s) de la semaine.

Voici quelques exemples de planification de tâches cron.

| PLANIFICATION | VALEUR PLANIFIÉE |
| --- | --- |
| 5 0 \* 8 \* | À 00h05 en août. |
| 5 4 \* \* 6 | À 04h05 le samedi. |
| 0 22 \* \* 1-5 | À 22h00 tous les jours de la semaine du lundi au vendredi. |

Vous pouvez en apprendre plus sur cron en détail dans ce [billet de blog](https://www.freecodecamp.org/news/cron-jobs-in-linux/).

## Comment Vérifier les Scripts Existants sur un Système

### Utiliser crontab

`crontab -l` liste les scripts déjà planifiés pour un utilisateur particulier.

![Mes scripts planifiés](https://www.freecodecamp.org/news/content/images/2022/03/image-103.png align="left")

*Mes scripts planifiés*

### Utiliser la commande find

La commande `find` aide à localiser des fichiers basés sur certains motifs. Comme la plupart des scripts se terminent par `.sh`, nous pouvons utiliser la commande find comme ceci :

```bash
find . -type f -name "*.sh"
```

Où,

* `.` représente le répertoire courant. Vous pouvez modifier le chemin en conséquence.
    
* `-type f` indique que le type de fichier que nous recherchons est un fichier texte.
    
* `*.sh` demande de faire correspondre tous les fichiers se terminant par `.sh`.
    

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-159.png align="left")

Si vous souhaitez lire des informations détaillées sur la commande find, consultez [mon autre article](https://www.freecodecamp.org/news/how-to-search-for-files-from-the-linux-command-line/).

## **Conclusion**

Dans ce tutoriel, nous avons appris les bases du scripting shell. Nous avons examiné des exemples et une syntaxe qui peuvent nous aider à écrire des programmes utiles.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Dites-le-moi sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

[Vecteur de travail créé par macrovector - www.freepik.com](https://www.freepik.com/vectors/work)