---
title: Les meilleurs exemples Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-19T17:44:00.000Z'
originalURL: https://freecodecamp.org/news/linux-example-bash-command-line
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f30740569d1a4ca4148.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
seo_title: Les meilleurs exemples Linux
seo_desc: 'Linux is a powerful operating system that powers most servers and most
  mobile devices. In this guide, we will show you examples of how to use some of its
  most powerful features. This involves using the Bash command line.

  12 Simple and Useful Linux Co...'
---

Linux est un système d'exploitation puissant qui alimente la plupart des serveurs et la plupart des appareils mobiles. Dans ce guide, nous allons vous montrer des exemples de l'utilisation de certaines de ses fonctionnalités les plus puissantes. Cela implique l'utilisation de la ligne de commande Bash.

## 12 commandes Linux simples et utiles

Les commandes listées ici sont basiques et vous aideront à démarrer rapidement. Mais elles sont également puissantes et continueront à être utiles à mesure que votre expertise Linux s'étend.

1. Commande `echo` : Elle prend le texte que vous lui donnez et l'envoie quelque part—vers l'écran, vers un fichier ou vers une autre commande. Exemple : `echo "bonjour !"`
2. Commande `cat` : Pour afficher le contenu d'un fichier texte, tapez simplement `cat monfichier`.
3. Commande `find` : Elle fait ce qu'elle dit et elle est bonne dans ce domaine. Utilisez-la pour localiser des fichiers par chemin, taille, date, propriétaire et une série d'autres filtres utiles. Exemple : `find . -type f -mtime -1h # Liste les fichiers de ce répertoire modifiés dans la dernière heure`.
4. Commande `date` : Tapez simplement date lorsque vous voulez savoir quelle heure il est. Exemple : `date "+Il est %l:%m%p le %A"`. Utilisez-la dans un script pour nommer les fichiers selon la date actuelle.
5. Commande `ls` : Qu'y a-t-il dans ce répertoire ? Combinez `ls` avec quelques indicateurs utiles pour afficher et trier le contenu du répertoire par date et taille. Elle vous offre également de nombreuses options pour formater la sortie.
6. Commande `pwd` : Où suis-je ? Linux peut être impitoyable, en particulier lorsque vous supprimez quelque chose. Assurez-vous de savoir où vous êtes avant d'émettre vos commandes.
7. Commande `mail` : Le programme de messagerie de Linux n'est pas beau, mais il peut être vraiment utile. Vous pouvez créer un message et ajouter du texte, des destinataires et des pièces jointes en une seule commande. Exemple : `echo "Nous passons un bon moment." | mail -s "Nous aimerions que vous soyez ici !" -A cartepostale.png -t maman@example.com`
8. Commande `cut` : Lorsque vous avez une chaîne avec des séparateurs, utilisez `cut` pour filtrer certains champs. Exemple : `echo "ci, cela, et autre chose" | cut -d, -f2 # "cela"`
9. Commande `grep` : Pour trouver des lignes de texte qui contiennent une certaine chaîne, utilisez grep. Exemple : `grep 'root' /etc/passwd # root:x:0:0:root:/root:/bin/bash`
10. Commande `sed` : Utilisez `sed` pour trouver et changer une sous-chaîne dans un texte. Exemple : `echo "ci, cela, et autre chose" | sed 's/cela/ceux-la/' # "ci, ceux-la, et autre chose"`
11. Commande `shutdown` : Utilisez cette commande pour éteindre le système et couper l'alimentation. Exemple : `shutdown -h now` éteint le système immédiatement. `shutdown -h +5` éteint le système après cinq minutes.
12. Commande `wget` : Utilisez `wget` pour télécharger des fichiers depuis la ligne de commande. Exemple : `wget http://ftp.gnu.org/gnu/wget/wget-1.5.3.tar.gz`

Utilisez ces commandes dans des scripts et sur la ligne de commande. Ce sont toutes des commandes très puissantes, et la page principale de Linux contient beaucoup plus d'informations sur chacune d'elles.

## Exemple de commandes de gestion des utilisateurs Linux

De plus, les commandes importantes utilisées par les administrateurs système sont les suivantes :

1. Commande `uptime` : Dans Linux, la commande uptime montre combien de temps votre système a été en fonctionnement et le nombre d'utilisateurs actuellement connectés. Elle affiche également la charge moyenne pour des intervalles de 1, 5 et 15 minutes.
2. Commande `w` : Cela affichera les utilisateurs actuellement connectés et leurs processus, ainsi que les charges moyennes. Affiche également le nom de connexion, le nom tty, l'hôte distant, l'heure de connexion, le temps d'inactivité, JCPU, PCPU, la commande et les processus.
3. Commande `users` : affiche les utilisateurs actuellement connectés. Cette commande n'a pas d'autres paramètres que l'aide et la version.
4. Commande `who` : la commande who retourne simplement le nom d'utilisateur, la date, l'heure et les informations sur l'hôte. La commande who est similaire à la commande w. Contrairement à la commande w, who n'affiche pas ce que font les utilisateurs.
5. Commande `whoami` : la commande whoami affiche le nom de l'utilisateur actuel. Vous pouvez également utiliser « who am i » pour afficher l'utilisateur actuel. Si vous êtes connecté en tant que root en utilisant la commande sudo, « whoami » retourne root comme utilisateur actuel. Utilisez « who am i » si vous voulez connaître l'utilisateur exact connecté.
6. Commande `ls` : ls affiche une liste de fichiers dans un format lisible par l'homme.
7. Commande `crontab` : liste les tâches planifiées pour l'utilisateur actuel avec la commande crontab et l'option -l.
8. Commande `less` : la commande less vous permet de visualiser rapidement un fichier. Vous pouvez faire défiler les pages vers le haut et vers le bas. Appuyez sur 'q' pour quitter la fenêtre less.
9. Commande `more` : la commande more vous permet de visualiser rapidement un fichier et montre les détails en pourcentage. Vous pouvez faire défiler les pages vers le haut et vers le bas. Appuyez sur 'q' pour quitter la fenêtre more.
10. Commande `cp` : Copie un fichier de sa source vers sa destination tout en conservant le même mode.

## **Comment créer un utilisateur**

#### **Utilisez la commande `adduser` ou `useradd` pour ajouter un nouvel utilisateur à votre système.**

```text
$ sudo adduser nomutilisateur
```

Assurez-vous de remplacer `nomutilisateur` par l'utilisateur que vous souhaitez créer.

#### **Utilisez la commande `passwd` pour mettre à jour le mot de passe du nouvel utilisateur.**

```text
$ sudo passwd nomutilisateur
```

Un mot de passe fort est fortement recommandé !

## **Comment créer un utilisateur Sudo**

Pour créer un utilisateur `sudo`, vous devez d'abord créer un utilisateur régulier en utilisant la commande ci-dessus, puis ajouter cet utilisateur au groupe des `sudoers` en utilisant la commande `usermod`.

##### **Sur les systèmes Debian (Ubuntu/LinuxMint/ElementryOS), les membres du groupe `sudo` ont des privilèges sudo.**

```text
$ sudo usermod -aG sudo nomutilisateur
```

##### **Sur les systèmes basés sur RHEL (Fedora/CentOs), les membres du groupe `wheel` ont des privilèges sudo.**

```text
$ sudo usermod -aG wheel nomutilisateur
```

## **Comment supprimer un utilisateur**

##### **Pour Debian (Ubuntu)**

```text
$ sudo deluser nomutilisateur
```

##### **Pour RHEL (Fedora/CentOS)**

```text
$ sudo userdel nomutilisateur
```

##### **Création de groupes et ajout d'utilisateurs**

```text
$ sudo groupadd editorial
$ sudo usermod -a -G editorial nomutilisateur
```

#### **Remarque : Toutes les commandes ci-dessus peuvent être exécutées sans sudo en mode `root`**

Pour passer en root sur Ubuntu, exécutez la commande `su -i` suivie du mot de passe de l'utilisateur connecté. L'invite change en `#` au lieu de `$`.

##### **Sur les systèmes Debian (Ubuntu/LinuxMint/ElementryOS), les membres du groupe `sudo` ont des privilèges sudo.**

```text
$ sudo usermod -aG sudo nomutilisateur
```

## **Comment créer un groupe**

Pour créer un groupe, utilisez la commande `groupadd`

```text
$ sudo groupadd nomdugroupe
```

## **Comment supprimer un groupe**

Pour supprimer un groupe, utilisez la commande 'groupdel'

```text
$ sudo groupdel nomdugroupe
```

## Exemple de la commande Find de Linux

### Utilisation de la commande Find

La commande find de Linux est un outil puissant pour vous aider à localiser des fichiers et des répertoires sur votre serveur. Avec un peu de pratique, vous pouvez facilement suivre les choses en fonction du nom, du type, de la taille ou de la date (quand elles ont été créées ou mises à jour pour la dernière fois).

Pensez à find comme votre assistant empressé :

Vous : « Je cherche quelque chose sur mon serveur. »

Find : « Je peux aider ! Que pouvez-vous me dire à ce sujet ? »

Vous : « C'était un fichier, plus grand que 2 Go, quelque part sous mon répertoire personnel, mis à jour dans les dernières 48 heures. »

Find : « Tada ! »

Find est un programme, donc en réalité vous devriez lui dire `find ~ -type f -size +2G`.

Voici quelques exemples de commandes utilisant find :

* `find ~ -type d # Montrez-moi tous les sous-répertoires à l'intérieur de mon répertoire personnel`
* `find / -type f -name 'todo.txt' # Montrez-moi les fichiers nommés 'todo.txt' n'importe où sous le répertoire racine (c'est-à-dire n'importe où)`

Le premier paramètre nomme toujours le répertoire dans lequel nous allons chercher. Dans nos exemples ci-dessus, il s'agit de ~ (répertoire personnel de l'utilisateur actuel) et / (répertoire racine du système de fichiers).

D'autres paramètres sont optionnels et peuvent être combinés de toutes les manières que vous trouvez utiles :

* Le paramètre type vous permet de contraindre la recherche aux fichiers uniquement (f), aux répertoires uniquement (d) ou aux liens symboliques (l). Si vous omettez le paramètre type, vous rechercherez tous ces types.
* Le paramètre name vous permet de spécifier ce que vous voulez trouver par nom, soit avec une chaîne littérale ('nomdefichier.txt') soit en utilisant des caractères génériques ('fichier?.').

`man find` vous montrera beaucoup plus de paramètres et vaut la peine d'être revu. Find peut localiser des fichiers par nom, utilisateur, date de création, taille et bien plus encore. La prochaine fois que vous cherchez quelque chose, trouvez-le !

## **Exemple de la commande dd de Linux**

La commande « dd » peut être utilisée pour créer un fichier d'une taille spécifique. Cela est utile si vous souhaitez tester les vitesses de téléchargement, ou tout autre test, et avez besoin d'un fichier d'une taille spécifique.

```text
dd if=/dev/zero of=nom_du_fichier.txt bs=1024k count=10
```

Cela créera un fichier de 1 Mo appelé nom_du_fichier.txt.

bs est votre taille d'octet et count représente le nombre de blocs. Une façon simple de le voir est 1024K X 10.

Voici une manière encore plus simple de créer un fichier de 1 Mo :

```text
dd if=/dev/zero of=nom_du_fichier.txt bs=1MB count=1
```

## Exemple de la rédaction d'un script Bash Linux

### Rédaction d'un script Bash

En tapant des commandes sur la ligne de commande Linux, vous pouvez donner des instructions au serveur pour effectuer certaines tâches simples. Un script shell est un moyen de rassembler une série d'instructions pour faciliter cela. Les scripts shell deviennent encore plus puissants lorsque vous ajoutez de la logique comme `if` et `while` pour contrôler automatiquement leur comportement à mesure que les circonstances changent.

### Qu'est-ce que Bash ?

Bash est le nom d'un interpréteur de ligne de commande, un programme qui donne un sens aux commandes Linux que vous entrez à l'invite de commande ou dans votre script.

### Que contient un script ?

Un script est simplement un fichier. Un script de base est composé d'une ligne introductive qui indique au serveur ce qu'il doit en faire, et d'une ou plusieurs instructions à exécuter. Voici un exemple :

```text
#!/bin/bash
echo "Salut. Je suis votre nouveau script bash préféré."
```

La première ligne a une signification spéciale, que nous discuterons ci-dessous. La deuxième ligne est simplement une commande Linux, que vous pourriez taper sur la ligne de commande.

### Qu'est-ce qu'un commentaire ?

Les commentaires sont du texte que vous ajoutez à votre script et que vous destinez à ce que bash ignore. Les commentaires commencent par un signe dièse et sont utiles pour annoter votre code afin que vous et d'autres utilisateurs puissiez le comprendre. 

Pour ajouter un commentaire, tapez le caractère `#`, suivi de tout texte utile pour vous. Bash ignorera le `#` et tout ce qui le suit.

**Remarque :** la première ligne du script n'est pas un commentaire. Cette ligne est toujours la première, commence toujours par `#!` et a une signification spéciale pour bash.

Voici le script précédent, commenté :

```text
#!/bin/bash # Désigne le chemin vers le programme bash. Doit commencer par '#!' (mais ce n'est pas un commentaire).
echo "Salut. Je suis votre nouveau script bash préféré." # 'echo' est un programme qui envoie une chaîne à l'écran.
```

### Exécution d'un script

Vous pouvez ouvrir un éditeur de texte, coller ce code d'exemple et enregistrer le fichier, et vous avez un script. Les scripts sont conventionnellement nommés en se terminant par '.sh', vous pourriez donc enregistrer ce code sous myscript.sh.

Le script ne s'exécutera pas tant que nous n'aurons pas fait 2 choses :

**Premièrement, rendez-le exécutable.** (Nous n'aurons à faire cela qu'une seule fois.) Linux repose largement sur les permissions de fichiers. Elles déterminent beaucoup de choses sur le comportement de votre serveur. Il y a beaucoup à savoir sur les permissions, mais pour l'instant, nous devons seulement savoir ceci : vous ne pouvez pas exécuter votre script tant que vous ne vous êtes pas donné les permissions d'exécution. Pour cela, tapez :

`chmod +x myscript.sh`

**Deuxièmement, exécutez-le.** Nous exécutons le script depuis la ligne de commande comme toute autre commande comme `ls` ou `date`. Le nom du script est la commande, et vous devez le précéder d'un './' lorsque vous l'appelez :

`./myscript.sh # Affiche "Salut. Je suis votre nouveau script bash préféré." (Cette partie est un commentaire !)`

### Conditionnelles

Parfois, vous voulez que votre script fasse quelque chose seulement si quelque chose d'autre est vrai. Par exemple, afficher un message seulement si une valeur est inférieure à une certaine limite. Voici un exemple d'utilisation de `if` pour faire cela :

```text
#!/bin/bash

count=1 # Crée une variable nommée count et la définit à 1

if [[ $count -lt 11 ]]; then # Ceci est un bloc if (ou conditionnel). Teste pour voir si $count est 10 ou moins. Si c'est le cas, exécute les instructions à l'intérieur du bloc.
    echo "$count est 10 ou moins" # Cela s'affichera, car count = 1.
fi # Chaque if se termine par fi
```

De même, nous pouvons organiser le script pour qu'il exécute une instruction seulement tant que quelque chose est vrai. Nous allons changer le code pour que la valeur de la variable count change :

```text
#!/bin/bash

count=1 # Crée une variable nommée count et la définit à 1

while [[ $count -lt 11 ]]; do # Ceci est un bloc if (ou conditionnel). Teste pour voir si $count est 10 ou moins. Si c'est le cas, exécute les instructions à l'intérieur du bloc.
    echo "$count est 10 ou moins" # Cela s'affichera tant que count <= 10.
    count=$((count+1)) # Incrémente count
done # Chaque while se termine par done
```

La sortie de cette version de myscript.sh ressemblera à ceci :

```text
"1 est 10 ou moins"
"2 est 10 ou moins"
"3 est 10 ou moins"
"4 est 10 ou moins"
"5 est 10 ou moins"
"6 est 10 ou moins"
"7 est 10 ou moins"
"8 est 10 ou moins"
"9 est 10 ou moins"
"10 est 10 ou moins"
```

## **Scripts du monde réel**

Ces exemples ne sont pas terriblement utiles, mais les principes le sont. En utilisant `while`, `if`, et toute commande que vous pourriez autrement taper manuellement, vous pouvez créer des scripts qui font un travail précieux.