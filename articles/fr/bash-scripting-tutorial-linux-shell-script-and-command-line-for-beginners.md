---
title: Tutoriel de Scripting Bash – Script Shell Linux et Ligne de Commande pour Débutants
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-03-20T17:35:58.000Z'
originalURL: https://freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Copy-of-Cast-a-Function-in-SQL
seo_title: Tutoriel de Scripting Bash – Script Shell Linux et Ligne de Commande pour
  Débutants
---

Convert-Char-to-Int-SQL-Server-Example.png
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: Script Shell
  slug: script-shell
seo_title: null
seo_desc: "Sous Linux, l'automatisation des processus repose en grande partie sur le scripting shell. Cela implique la création d'un fichier contenant une série de commandes pouvant être exécutées ensemble.\n\nDans cet article, nous commencerons par les bases du scripting bash, ce qui inclut les variables, les comm..."
---

Sous Linux, l'automatisation des processus repose en grande partie sur le scripting shell. Cela implique la création d'un fichier contenant une série de commandes pouvant être exécutées ensemble.

Dans cet article, nous commencerons par les bases du scripting bash, ce qui inclut les variables, les commandes, les entrées/sorties et le débogage. Nous verrons également des exemples pour chaque concept tout au long du parcours.

C'est parti ! 🚀

## Table des matières

1. [Prérequis](#heading-prerequis)
2. [Introduction](#heading-introduction)
- [Définition du scripting Bash](#heading-definition-du-scripting-bash)
- [Avantages du scripting Bash](#heading-avantages-du-scripting-bash)
- [Présentation du shell Bash et de l'interface de ligne de commande](#heading-presentation-du-shell-bash-et-de-linterface-de-ligne-de-commande)
3. [Comment débuter avec le scripting Bash](#heading-comment-debuter-avec-le-scripting-bash)
- [Comment exécuter des commandes Bash depuis la ligne de commande](#comment-executer-des-commandes-bash-depuis-la-ligne-de-commande)
- [Comment créer et exécuter des scripts Bash](#heading-comment-creer-et-executer-des-scripts-bash)
4. [Les bases du scripting Bash](#heading-les-bases-du-scripting-bash)

* [Commentaires en scripting bash](#heading-commentaires-en-scripting-bash)
* [Variables et types de données dans Bash](#heading-variables-et-types-de-donnees-dans-bash)
* [Entrées et sorties dans les scripts Bash](#heading-entrees-et-sorties-dans-les-scripts-bash)
* [Commandes Bash de base (echo, read, etc.)](#heading-commandes-bash-de-base-echo-read-etc)
* [Instructions conditionnelles (if/else)](#heading-instructions-conditionnelles-ifelse)

5. [Boucles et branchements en Bash](#heading-boucles-et-branchements-en-bash)
- [Boucle While](#heading-boucle-while)
- [Boucle For](#heading-boucle-for)
- [Instructions Case](#heading-instructions-case)
6. [Comment planifier des scripts avec cron](#heading-comment-planifier-des-scripts-avec-cron)
7. [Comment déboguer et dépanner des scripts Bash](#heading-comment-deboguer-et-depanner-des-scripts-bash)
8. [Conclusion](#heading-conclusion)
- [Ressources pour en apprendre davantage sur le scripting Bash](#heading-ressources-pour-en-apprendre-davantage-sur-le-scripting-bash)

## Prérequis

Pour suivre ce tutoriel, vous devez disposer des accès suivants :

* Une version de Linux en cours d'exécution avec accès à la ligne de commande.

Si Linux n'est pas installé sur votre machine ou si vous débutez, vous pouvez facilement accéder à la ligne de commande Linux via [Replit](https://replit.com/~). Replit est un IDE basé sur le navigateur où vous pouvez accéder au shell bash en quelques minutes.

Vous pouvez également installer Linux sur votre système Windows en utilisant WSL (Windows Subsystem for Linux). [Voici](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/) un tutoriel à ce sujet.

## Introduction

### Définition du scripting Bash

Un script bash est un fichier contenant une séquence de commandes qui sont exécutées par le programme bash ligne par ligne. Il vous permet d'effectuer une série d'actions, telles que naviguer vers un répertoire spécifique, créer un dossier et lancer un processus à l'aide de la ligne de commande.

En enregistrant ces commandes dans un script, vous pouvez répéter la même séquence d'étapes plusieurs fois et les exécuter en lançant simplement le script.

### Avantages du scripting Bash

Le scripting Bash est un outil puissant et polyvalent pour automatiser les tâches d'administration système, gérer les ressources système et effectuer d'autres tâches de routine dans les systèmes Unix/Linux. Voici quelques avantages du scripting shell :

* **Automatisation** : Les scripts shell vous permettent d'automatiser les tâches et processus répétitifs, ce qui fait gagner du temps et réduit le risque d'erreurs pouvant survenir lors d'une exécution manuelle.
* **Portabilité** : Les scripts shell peuvent être exécutés sur diverses plateformes et systèmes d'exploitation, notamment Unix, Linux, macOS et même Windows via l'utilisation d'émulateurs ou de machines virtuelles.
* **Flexibilité** : Les scripts shell sont hautement personnalisables et peuvent être facilement modifiés pour répondre à des besoins spécifiques. Ils peuvent également être combinés avec d'autres langages de programmation ou utilitaires pour créer des scripts plus puissants.
* **Accessibilité** : Les scripts shell sont faciles à écrire et ne nécessitent aucun outil ou logiciel spécial. Ils peuvent être édités à l'aide de n'importe quel éditeur de texte, et la plupart des systèmes d'exploitation disposent d'un interpréteur shell intégré.
* **Intégration** : Les scripts shell peuvent être intégrés à d'autres outils et applications, tels que des bases de données, des serveurs web et des services cloud, permettant des tâches d'automatisation et de gestion de système plus complexes.
* **Débogage** : Les scripts shell sont faciles à déboguer, et la plupart des shells disposent d'outils de débogage et de rapport d'erreurs intégrés qui peuvent aider à identifier et à corriger les problèmes rapidement.

### Présentation du shell Bash et de l'interface de ligne de commande

Les termes « shell » et « bash » sont souvent utilisés de manière interchangeable. Mais il existe une subtile différence entre les deux.

Le terme « shell » fait référence à un programme qui fournit une interface en ligne de commande pour interagir avec un système d'exploitation. Bash (Bourne-Again SHell) est l'un des shells Unix/Linux les plus couramment utilisés et constitue le shell par défaut dans de nombreuses distributions Linux.

Une interface shell ou de ligne de commande ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-135.png)
_Le shell accepte les commandes de l'utilisateur et affiche la sortie_

Dans la sortie ci-dessus, `zaira@Zaira` est l'invite du shell (prompt). Lorsqu'un shell est utilisé de manière interactive, il affiche un `$` lorsqu'il attend une commande de la part de l'utilisateur.

Si le shell est exécuté en tant que root (un utilisateur avec des droits d'administration), l'invite est remplacée par `#`. L'invite du shell superutilisateur ressemble à ceci :

```bash
[root@host ~]#
```

Bien que Bash soit un type de shell, il existe d'autres shells disponibles, tels que le shell Korn (ksh), le shell C (csh) et le shell Z (zsh). Chaque shell possède sa propre syntaxe et son propre ensemble de fonctionnalités, mais ils partagent tous l'objectif commun de fournir une interface en ligne de commande pour interagir avec le système d'exploitation.

Vous pouvez déterminer votre type de shell à l'aide de la commande `ps` :

```bash
ps
```

Voici le résultat pour moi :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-134.png)
_Vérification du type de shell. J'utilise le shell bash_

En résumé, alors que « shell » est un terme large qui désigne tout programme fournissant une interface en ligne de commande, « Bash » est un type spécifique de shell largement utilisé dans les systèmes Unix/Linux.

Note : Dans ce tutoriel, nous utiliserons le shell « bash ».

## Comment débuter avec le scripting Bash

### Comment exécuter des commandes Bash depuis la ligne de commande

Comme mentionné précédemment, l'invite du shell ressemble à ceci :

```bash
[username@host ~]$
```

Vous pouvez saisir n'importe quelle commande après le signe `$` et voir le résultat sur le terminal.

En général, les commandes suivent cette syntaxe :

```
commande [OPTIONS] arguments
```

Saluons quelques commandes bash de base et voyons leurs résultats. Assurez-vous de pratiquer en même temps :)

* `date` : Affiche la date actuelle

```bash
zaira@Zaira:~/shell-tutorial$ date
Tue Mar 14 13:08:57 PKT 2023
```

* `pwd` : Affiche le répertoire de travail actuel (present working directory).

```bash
zaira@Zaira:~/shell-tutorial$ pwd
/home/zaira/shell-tutorial
```

* `ls` : Liste le contenu du répertoire actuel.

```bash
zaira@Zaira:~/shell-tutorial$ ls
check_plaindrome.sh  count_odd.sh  env  log  temp
```

* `echo` : Affiche une chaîne de texte ou la valeur d'une variable sur le terminal.

```bash
zaira@Zaira:~/shell-tutorial$ echo "Hello bash"
Hello bash
```

Vous pouvez toujours consulter le manuel d'une commande avec la commande `man`.

Par exemple, le manuel de `ls` ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-138.png)
_Vous pouvez voir les options d'une commande en détail en utilisant `man`_

### Comment créer et exécuter des scripts Bash

#### Conventions de nommage des scripts

Par convention de nommage, les scripts bash se terminent par `.sh`. Cependant, les scripts bash peuvent parfaitement fonctionner sans l'extension `sh`.

#### Ajout du Shebang

Les scripts Bash commencent par un `shebang`. Le shebang est une combinaison de `bash #` et `bang !` suivie du chemin du shell bash. C'est la première ligne du script. Le shebang indique au shell de l'exécuter via le shell bash. Le shebang est simplement un chemin absolu vers l'interprète bash.

Voici un exemple de déclaration shebang.

```bash
#!/bin/bash
```

Vous pouvez trouver le chemin de votre shell bash (qui peut varier par rapport à celui ci-dessus) en utilisant la commande :

```bash
which bash
```

#### Création de notre premier script bash

Notre premier script demande à l'utilisateur de saisir un chemin. En retour, son contenu sera listé.

Créez un fichier nommé `run_all.sh` à l'aide de la commande `vi`. Vous pouvez utiliser l'éditeur de votre choix.

```bash
vi run_all.sh
```

Ajoutez les commandes suivantes dans votre fichier et enregistrez-le :

```bash
#!/bin/bash
echo "Aujourd'hui, nous sommes le " `date`

echo -e "\nentrez le chemin du répertoire"
read the_path

echo -e "\nvotre chemin contient les fichiers et dossiers suivants : "
ls $the_path
```

Analysons le script ligne par ligne. J'affiche à nouveau le même script, mais cette fois avec des numéros de ligne.

```bash
  1 #!/bin/bash
  2 echo "Aujourd'hui, nous sommes le " `date`
  3
  4 echo -e "\nentrez le chemin du répertoire"
  5 read the_path
  6
  7 echo -e "\nvotre chemin contient les fichiers et dossiers suivants : "
  8 ls $the_path
```

* Ligne #1 : Le shebang (`#!/bin/bash`) pointe vers le chemin du shell bash.
* Ligne #2 : La commande `echo` affiche la date et l'heure actuelles sur le terminal. Notez que `date` est entre accents graves (backticks).
* Ligne #4 : Nous voulons que l'utilisateur saisisse un chemin valide.
* Ligne #5 : La commande `read` lit l'entrée et la stocke dans la variable `the_path`.
* Ligne #8 : La commande `ls` prend la variable contenant le chemin stocké et affiche les fichiers et dossiers actuels.

#### Exécution du script bash

Pour rendre le script exécutable, attribuez les droits d'exécution à votre utilisateur à l'aide de cette commande :

```bash
chmod u+x run_all.sh
```

Ici,

* `chmod` modifie les permissions d'un fichier pour l'utilisateur actuel : `u`.
* `+x` ajoute les droits d'exécution à l'utilisateur actuel. Cela signifie que l'utilisateur propriétaire peut maintenant lancer le script.
* `run_all.sh` est le fichier que nous souhaitons exécuter.

Vous pouvez lancer le script en utilisant l'une des méthodes suivantes :

* `sh run_all.sh`
* `bash run_all.sh`
* `./run_all.sh`

Voyons-le en action 🚀

![Image](https://www.freecodecamp.org/news/content/images/2023/03/run-script-bash-2.gif)

## Les bases du scripting Bash

### Commentaires en scripting bash

Les commentaires commencent par un `#` en scripting bash. Cela signifie que toute ligne commençant par un `#` est un commentaire et sera ignorée par l'interprète.

Les commentaires sont très utiles pour documenter le code, et c'est une bonne pratique de les ajouter pour aider les autres à comprendre le code.

Voici des exemples de commentaires :

```bash
# Ceci est un exemple de commentaire
# Ces deux lignes seront ignorées par l'interprète
```

### Variables et types de données dans Bash

Les variables vous permettent de stocker des données. Vous pouvez utiliser des variables pour lire, accéder et manipuler des données tout au long de votre script.

Il n'y a pas de types de données dans Bash. Dans Bash, une variable est capable de stocker des valeurs numériques, des caractères individuels ou des chaînes de caractères.

Dans Bash, vous pouvez utiliser et définir les valeurs des variables des manières suivantes :

1. Attribuer la valeur directement :

```bash
country=Pakistan
```

2. Attribuer la valeur basée sur la sortie obtenue d'un programme ou d'une commande, en utilisant la substitution de commande. Notez que `$` est nécessaire pour accéder à la valeur d'une variable existante.

```bash
same_country=$country
```

Pour accéder à la valeur de la variable, ajoutez `$` au nom de la variable.

```bash
zaira@Zaira:~$ country=Pakistan
zaira@Zaira:~$ echo $country
Pakistan
zaira@Zaira:~$ new_country=$country
zaira@Zaira:~$ echo $new_country
Pakistan
```

### Conventions de nommage des variables

En scripting Bash, voici les conventions de nommage des variables :

1. Les noms de variables doivent commencer par une lettre ou un souligné (`_`).
2. Les noms de variables peuvent contenir des lettres, des chiffres et des soulignés (`_`).
3. Les noms de variables sont sensibles à la casse.
4. Les noms de variables ne doivent pas contenir d'espaces ou de caractères spéciaux.
5. Utilisez des noms descriptifs qui reflètent l'utilité de la variable.
6. Évitez d'utiliser des mots-clés réservés, tels que `if`, `then`, `else`, `fi`, etc., comme noms de variables.

Voici quelques exemples de noms de variables valides dans Bash :

```bash
name
count
_var
myVar
MY_VAR
```

Et voici quelques exemples de noms de variables invalides :

```bash
2ndvar (le nom de la variable commence par un chiffre)
my var (le nom de la variable contient un espace)
my-var (le nom de la variable contient un trait d'union)
```

Le respect de ces conventions de nommage aide à rendre les scripts Bash plus lisibles et plus faciles à maintenir.

### Entrées et sorties dans les scripts Bash

#### Collecte des entrées

Dans cette section, nous aborderons quelques méthodes pour fournir des entrées à nos scripts.

1. Lire l'entrée de l'utilisateur et la stocker dans une variable

Nous pouvons lire l'entrée de l'utilisateur à l'aide de la commande `read`.

```bash
#!/bin/bash 

echo "Quel est votre nom ?" 

read entered_name 

echo -e "\nBienvenue dans le tutoriel bash" $entered_name
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/name-sh.gif)

2. Lire à partir d'un fichier

Ce code lit chaque ligne d'un fichier nommé `input.txt` et l'affiche sur le terminal. Nous étudierons les boucles while plus tard dans cet article.

```bash
while read line
do
  echo $line
done < input.txt
```

3. Arguments de la ligne de commande

Dans un script ou une fonction bash, `$1` désigne le premier argument passé, `$2` désigne le second argument passé, et ainsi de suite.

Ce script prend un nom comme argument de ligne de commande et affiche une salutation personnalisée.

```bash
echo "Bonjour, $1 !"
```

Nous avons fourni `Zaira` comme argument au script.

```bash
#!/bin/bash
echo "Bonjour, $1 !"
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2023/03/name-sh-1.gif)

#### Affichage de la sortie

Ici, nous discuterons de quelques méthodes pour recevoir la sortie des scripts.

1. Affichage sur le terminal :

```bash
echo "Hello, World!"
```

Ceci affiche le texte "Hello, World!" sur le terminal.

2. Écriture dans un fichier :

```bash
echo "Ceci est du texte." > output.txt
```

Ceci écrit le texte "Ceci est du texte." dans un fichier nommé `output.txt`. Notez que l'opérateur `>` écrase un fichier s'il contient déjà du contenu.

3. Ajout à la fin d'un fichier :

```bash
echo "Plus de texte." >> output.txt
```

Ceci ajoute le texte "Plus de texte." à la fin du fichier `output.txt`.

4. Redirection de la sortie :

```bash
ls > files.txt
```

Ceci liste les fichiers du répertoire actuel et écrit la sortie dans un fichier nommé `files.txt`. Vous pouvez rediriger la sortie de n'importe quelle commande vers un fichier de cette manière.

### Commandes Bash de base (echo, read, etc.)

Voici une liste de certaines des commandes bash les plus couramment utilisées :

1. `cd` : Changer de répertoire vers un emplacement différent.
2. `ls` : Lister le contenu du répertoire actuel.
3. `mkdir` : Créer un nouveau répertoire.
4. `touch` : Créer un nouveau fichier.
5. `rm` : Supprimer un fichier ou un répertoire.
6. `cp` : Copier un fichier ou un répertoire.
7. `mv` : Déplacer ou renommer un fichier ou un répertoire.
8. `echo` : Afficher du texte sur le terminal.
9. `cat` : Concaténer et afficher le contenu d'un fichier.
10. `grep` : Rechercher un motif dans un fichier.
11. `chmod` : Modifier les permissions d'un fichier ou d'un répertoire.
12. `sudo` : Exécuter une commande avec des privilèges administratifs.
13. `df` : Afficher la quantité d'espace disque disponible.
14. `history` : Afficher une liste des commandes exécutées précédemment.
15. `ps` : Afficher des informations sur les processus en cours d'exécution.

### Instructions conditionnelles (if/else)

Les expressions qui produisent un résultat booléen, soit vrai soit faux, sont appelées conditions. Il existe plusieurs façons d'évaluer les conditions, notamment `if`, `if-else`, `if-elif-else` et les conditionnelles imbriquées.

**Syntaxe** :

```bash
if [[ condition ]];
then
	instruction
elif [[ condition ]]; then
	instruction 
else
	faites ceci par défaut
fi
```

Nous pouvons utiliser des opérateurs logiques tels que ET `-a` et OU `-o` pour effectuer des comparaisons plus complexes.

```bash
if [ $a -gt 60 -a $b -lt 100 ]
```

Voyons un exemple de script Bash qui utilise les instructions `if`, `if-else` et `if-elif-else` pour déterminer si un nombre saisi par l'utilisateur est positif, négatif ou nul :

```bash
#!/bin/bash

echo "Veuillez entrer un nombre : "
read num

if [ $num -gt 0 ]; then
  echo "$num est positif"
elif [ $num -lt 0 ]; then
  echo "$num est négatif"
else
  echo "$num est nul"
fi
```

Le script invite d'abord l'utilisateur à saisir un nombre. Ensuite, il utilise une instruction `if` pour vérifier si le nombre est supérieur à 0. Si c'est le cas, le script indique que le nombre est positif. Si le nombre n'est pas supérieur à 0, le script passe à l'instruction suivante, qui est une instruction `if-elif`. Ici, le script vérifie si le nombre est inférieur à 0. Si c'est le cas, le script indique que le nombre est négatif. Enfin, si le nombre n'est ni supérieur à 0 ni inférieur à 0, le script utilise une instruction `else` pour indiquer que le nombre est nul.

Voyons-le en action 🚀

![Image](https://www.freecodecamp.org/news/content/images/2023/03/test-odd.gif)

## Boucles et branchements en Bash

### Boucle While

Les boucles While vérifient une condition et bouclent tant que la condition reste `true`. Nous devons fournir une instruction de compteur qui incrémente le compteur pour contrôler l'exécution de la boucle.

Dans l'exemple ci-dessous, `(( i += 1 ))` est l'instruction de compteur qui incrémente la valeur de `i`. La boucle s'exécutera exactement 10 fois.

```bash
#!/bin/bash
i=1
while [[ $i -le 10 ]] ; do
   echo "$i"
  (( i += 1 ))
done
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-187.png)

### Boucle For

La boucle `for`, tout comme la boucle `while`, vous permet d'exécuter des instructions un nombre spécifique de fois. Chaque boucle diffère par sa syntaxe et son utilisation.

Dans l'exemple ci-dessous, la boucle itérera 5 fois.

```bash
#!/bin/bash

for i in {1..5}
do
    echo $i
done
```

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-186.png)

### Instructions Case

En Bash, les instructions case sont utilisées pour comparer une valeur donnée à une liste de motifs et exécuter un bloc de code basé sur le premier motif qui correspond. La syntaxe d'une instruction case en Bash est la suivante :

```bash
case expression in
    pattern1)
        # code à exécuter si l'expression correspond au motif1
        ;;
    pattern2)
        # code à exécuter si l'expression correspond au motif2
        ;;
    pattern3)
        # code à exécuter si l'expression correspond au motif3
        ;;
    *)
        # code à exécuter si aucun des motifs ci-dessus ne correspond à l'expression
        ;;
esac
```

Ici, "expression" est la valeur que nous voulons comparer, et "motif1", "motif2", "motif3", et ainsi de suite, sont les motifs auxquels nous voulons la comparer.

Le double point-virgule ";;" sépare chaque bloc de code à exécuter pour chaque motif. L'astérisque "*" représente le cas par défaut, qui s'exécute si aucun des motifs spécifiés ne correspond à l'expression.

Voyons un exemple.

```bash
fruit="apple"

case $fruit in
    "apple")
        echo "C'est un fruit rouge."
        ;;
    "banana")
        echo "C'est un fruit jaune."
        ;;
    "orange")
        echo "C'est un fruit orange."
        ;;
    *)
        echo "Fruit inconnu."
        ;;
esac
```

Dans cet exemple, comme la valeur de "fruit" est "apple", le premier motif correspond, et le bloc de code qui affiche "C'est un fruit rouge." est exécuté. Si la valeur de "fruit" était plutôt "banana", le deuxième motif correspondrait et le bloc de code qui affiche "C'est un fruit jaune." s'exécuterait, et ainsi de suite. Si la valeur de "fruit" ne correspond à aucun des motifs spécifiés, le cas par défaut est exécuté, affichant "Fruit inconnu."

## Comment planifier des scripts avec cron

Cron est un puissant utilitaire de planification de tâches disponible dans les systèmes d'exploitation de type Unix. En configurant cron, vous pouvez mettre en place des tâches automatisées pour qu'elles s'exécutent quotidiennement, hebdomadairement, mensuellement ou à une heure précise. Les capacités d'automatisation fournies par cron jouent un rôle crucial dans l'administration système Linux.

Voici la syntaxe pour planifier des crons :

```bash
# Exemple de tâche cron
* * * * * sh /chemin/vers/script.sh
```

Ici, les `*` représentent respectivement minute(s) heure(s) jour(s) mois(s) jour(s) de la semaine.

Voici quelques exemples de planification de tâches cron.

<table>
<thead>
<tr>
<th>Planification</th>
<th>Description</th>
<th>Exemple</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>0 0 * * *</code></td>
<td>Exécuter un script à minuit chaque jour</td>
<td><code>0 0 * * * /chemin/vers/script.sh</code></td>
</tr>
<tr>
<td><code>*/5 * * * *</code></td>
<td>Exécuter un script toutes les 5 minutes</td>
<td><code>*/5 * * * * /chemin/vers/script.sh</code></td>
</tr>
<tr>
<td><code>0 6 * * 1-5</code></td>
<td>Exécuter un script à 6 heures du matin du lundi au vendredi</td>
<td><code>0 6 * * 1-5 /chemin/vers/script.sh</code></td>
</tr>
<tr>
<td><code>0 0 1-7 * *</code></td>
<td>Exécuter un script les 7 premiers jours de chaque mois</td>
<td><code>0 0 1-7 * * /chemin/vers/script.sh</code></td>
</tr>
<tr>
<td><code>0 12 1 * *</code></td>
<td>Exécuter un script le premier jour de chaque mois à midi</td>
<td><code>0 12 1 * * /chemin/vers/script.sh</code></td>
</tr>
</tbody>
</table>

#### Utilisation de crontab

L'utilitaire `crontab` est utilisé pour ajouter et modifier les tâches cron.

`crontab -l` liste les scripts déjà planifiés pour un utilisateur particulier.

Vous pouvez ajouter et modifier le cron via `crontab -e`.

Vous pouvez en savoir plus sur les tâches cron dans mon [autre article ici](https://www.freecodecamp.org/news/cron-jobs-in-linux/).

## Comment déboguer et dépanner des scripts Bash

Le débogage et le dépannage sont des compétences essentielles pour tout scripteur Bash. Bien que les scripts Bash puissent être incroyablement puissants, ils peuvent également être sujets à des erreurs et à des comportements inattendus. Dans cette section, nous aborderons quelques conseils et techniques pour déboguer et dépanner les scripts Bash.

### Définir l'option `set -x`

L'une des techniques les plus utiles pour déboguer les scripts Bash est de définir l'option `set -x` au début du script. Cette option active le mode débogage, ce qui amène Bash à afficher chaque commande qu'il exécute sur le terminal, précédée d'un signe `+`. Cela peut être extrêmement utile pour identifier l'endroit où des erreurs se produisent dans votre script.

```bash
#!/bin/bash

set -x

# Votre script va ici
```

### Vérifier le code de sortie

Lorsque Bash rencontre une erreur, il définit un code de sortie qui indique la nature de l'erreur. Vous pouvez vérifier le code de sortie de la commande la plus récente à l'aide de la variable `$?`. Une valeur de `0` indique un succès, tandis que toute autre valeur indique une erreur.

```bash
#!/bin/bash

# Votre script va ici

if [ $? -ne 0 ]; then
    echo "Une erreur s'est produite."
fi
```

### Utiliser des instructions `echo`

Une autre technique utile pour déboguer les scripts Bash consiste à insérer des instructions `echo` tout au long de votre code. Cela peut vous aider à identifier où les erreurs se produisent et quelles valeurs sont transmises aux variables.

```bash
#!/bin/bash

# Votre script va ici

echo "La valeur de la variable x est : $x"

# Plus de code ici
```

### Utiliser l'option `set -e`

Si vous souhaitez que votre script s'arrête immédiatement dès qu'une commande du script échoue, vous pouvez utiliser l'option `set -e`. Cette option forcera Bash à s'arrêter avec une erreur si une commande du script échoue, ce qui facilite l'identification et la correction des erreurs dans votre script.

```bash
#!/bin/bash

set -e

# Votre script va ici
```

### Dépannage des crons en vérifiant les logs

Nous pouvons dépanner les crons en utilisant les fichiers de log. Les logs sont conservés pour toutes les tâches planifiées. Vous pouvez vérifier dans les logs si une tâche spécifique s'est déroulée comme prévu ou non.

Pour Ubuntu/Debian, vous pouvez trouver les logs de `cron` à :

```bash
/var/log/syslog
```

L'emplacement varie pour les autres distributions.

Un fichier log de tâche cron peut ressembler à ceci :

```bash
2022-03-11 00:00:01 Tâche démarrée
2022-03-11 00:00:02 Exécution du script /chemin/vers/script.sh
2022-03-11 00:00:03 Script terminé avec succès
2022-03-11 00:05:01 Tâche démarrée
2022-03-11 00:05:02 Exécution du script /chemin/vers/script.sh
2022-03-11 00:05:03 Erreur : impossible de se connecter à la base de données
2022-03-11 00:05:03 Script arrêté avec le code d'erreur 1
2022-03-11 00:10:01 Tâche démarrée
2022-03-11 00:10:02 Exécution du script /chemin/vers/script.sh
2022-03-11 00:10:03 Script terminé avec succès
```

## Conclusion

Dans cet article, nous avons commencé par voir comment accéder au terminal, puis nous avons exécuté quelques commandes bash de base. Nous avons également étudié ce qu'est un shell bash. Nous avons brièvement examiné le branchement du code à l'aide de boucles et de conditionnelles. Enfin, nous avons discuté de l'automatisation des scripts à l'aide de cron, suivie de quelques techniques de dépannage.

### Ressources pour en apprendre davantage sur le scripting Bash

Si vous souhaitez approfondir vos connaissances dans le monde du scripting bash, je vous suggère de jeter un œil à ce cours de 6 heures sur Linux chez freeCodeCamp.

%[https://youtu.be/sWbUDq4S6Y8]

Quelle est votre chose préférée apprise dans ce tutoriel ? Vous pouvez également me contacter sur l'une de ces [plateformes](https://zaira_.bio.link/). 📧

À bientôt dans le prochain tutoriel, bon codage ! 😁

Crédits de l'image de bannière : Image par [Freepik](https://www.freepik.com/free-vector/hand-drawn-flat-design-devops-illustration_25726540.htm#query=programmer%20linux&position=4&from_view=search&track=ais)