---
title: Comment fonctionne la propriété et les permissions des fichiers dans RHEL
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-01-16T20:56:12.000Z'
originalURL: https://freecodecamp.org/news/file-ownership-permissions-rhel
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/file-ownership-permissions-rhel-cover.jpg
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: Comment fonctionne la propriété et les permissions des fichiers dans RHEL
seo_desc: 'Linux commands give you precise control over file ownership and permissions,
  ensuring data security and access control.

  This guide will delve into several essential commands: chown, chgrp, chmod, and
  umask. The examples will showcase their functional...'
---

Les commandes Linux vous donnent un contrôle précis sur la propriété et les permissions des fichiers, assurant la sécurité des données et le contrôle d'accès.

Ce guide explorera plusieurs commandes essentielles : `chown`, `chgrp`, `chmod` et `umask`. Les exemples illustreront leur fonctionnalité, leurs variations et leurs applications pratiques.

## **Table des matières**

Voici ce que nous allons couvrir dans ce guide complet :

* [ls -l – Voir les permissions des fichiers](#heading-ls-l-view-file-permissions)
    
* [chown – Changer la propriété d'un fichier](#heading-chown-change-file-ownership)
    
* [chgrp – Changer le groupe propriétaire d'un fichier](#heading-chgrp-change-file-group-ownership)
    
* [chmod – Modifier les permissions des fichiers](#heading-chmod-modify-file-permissions)
    
* [Listes de contrôle d'accès](#heading-access-control-lists)
    
* [La commande umask](#heading-the-umask-command)
    
* [Exercice pratique](#heading-practical-exercises)
    
* [Conclusion](#heading-wrapping-up)
    

## `ls -l` – Voir les permissions des fichiers

Dans le monde de Red Hat Enterprise Linux, utiliser la commande `ls -l` revient à jeter un coup d'œil dans le journal secret d'un répertoire. C'est un moyen d'obtenir une vue détaillée et rapprochée de ce qui se trouve à l'intérieur, presque comme feuilleter un catalogue avec tous les détails.

### Exemple de `ls -l`

L'exécution de cette commande affiche les permissions des fichiers, la propriété et d'autres détails pour les fichiers dans le répertoire courant.

```bash
ls -l /mydirectory
```

Voici le résultat :

```bash
OUTPUT

drwxr-xr-x 2 username group 4096 Jan 5 09:30 mydirectory
```

Décortiquons cette sortie partie par partie. Voici une illustration qui montre ce que chaque partie représente, et je vais la détailler ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Frame-1000004565.svg align="left")

*Sortie détaillée pour la commande ls -l*

* Type de fichier et permissions : La première colonne représente le type de fichier et les permissions. Elle se compose de dix caractères :
    
* Le premier caractère indique le type de fichier (`-` pour un fichier régulier, `d` pour un répertoire, `l` pour un lien symbolique, etc.).
    
* Les neuf caractères suivants représentent les permissions pour le propriétaire, le groupe et les autres (lecture, écriture, exécution).
    
* Nombre de liens : La deuxième colonne montre le nombre de liens physiques vers le fichier ou le répertoire.
    
* Propriétaire et groupe : Les troisième et quatrième colonnes affichent le propriétaire et le groupe associés au fichier ou au répertoire.
    
* Taille du fichier : La cinquième colonne indique la taille du fichier en octets.
    
* Dernière heure de modification : La sixième colonne montre le timestamp de la dernière modification.
    
* Nom du fichier ou du répertoire : La dernière colonne liste le nom du fichier ou du répertoire.
    

## `chown` – Changer la propriété d'un fichier

Dans Red Hat Enterprise Linux (RHEL), la puissante commande `chown` signifie "change owner" et permet aux utilisateurs de modifier la propriété des fichiers et des répertoires. Cet outil polyvalent est une ressource précieuse pour les administrateurs système afin de gérer efficacement les permissions et le contrôle d'accès.

### Syntaxe de `chown` :

```bash
chown [OPTIONS] [NEW_OWNER][:NEW_GROUP] FILE(s)/DIRECTORY(s)
```

Options :

* R, `--recursive` : Change récursivement la propriété des répertoires et de leur contenu.
    
* v, `--verbose` : Affiche un message pour chaque fichier traité.
    

Note : Seul l'utilisateur root ou un utilisateur avec les permissions appropriées peut utiliser chown pour changer la propriété.

### Exemples de `chown` :

Changer la propriété d'un fichier :

```bash
chown newowner myfile.txt
```

Cela changera le propriétaire d'un fichier en `newowner`.

Changer la propriété du groupe :

```bash
chown :newgroup myfile.txt
```

Cette commande fait rejoindre un fichier appelé `myfile.txt` à un nouveau groupe nommé `newgroup`, et ne modifie pas la personne qui possède le fichier. Vous pouvez effectuer ce changement de groupe en utilisant une commande appelée `chown`. Oh, et il y a une autre commande spéciale juste pour changer les groupes dont nous parlerons bientôt.

Changer à la fois le propriétaire et le groupe :

```bash
chown newowner:newgroup myfile.txt
```

Cela change le propriétaire en `newowner` et le groupe en `newgroup` pour le fichier myfile.txt.

Changement récursif (application des changements aux sous-répertoires) :

```bash
chown -R newowner:newgroup /path/to/directory
```

La commande ci-dessus demande au système de changer la propriété de tous les fichiers et répertoires dans le répertoire spécifié et ses sous-répertoires pour le nouveau propriétaire et groupe spécifiés. Cela garantit que l'opération est effectuée de manière récursive dans toute la structure du répertoire.

Mode verbeux :

```bash
chown -v newowner:newgroup myfile.txt
```

La commande demande au système de changer la propriété du fichier spécifié, en fournissant une sortie détaillée des modifications apportées. La sortie détaillée est affichée car nous utilisons l'option `-v` avec `chown`.

Propriété par UID/GID :

```bash
chown 1001:1002 myfile.txt
```

La commande demande au système de modifier la propriété du fichier spécifié, en l'attribuant à un utilisateur et un groupe spécifiques identifiés par leurs identifiants numériques respectifs (1001, 1002).

## `chgrp` – Changer le groupe propriétaire d'un fichier

La commande `chgrp` dans Red Hat Enterprise Linux (RHEL) est utilisée pour changer le groupe propriétaire des fichiers ou répertoires. Elle est particulièrement utile lorsque vous souhaitez modifier uniquement le groupe propriétaire sans affecter le propriétaire utilisateur du fichier ou ses permissions.

### Syntaxe de `chgrp` :

```bash
chgrp [OPTIONS] NEW_GROUP FILE...
```

### Exemples de `chgrp` :

Changer le groupe propriétaire d'un fichier :

```bash
chgrp newgroup myfile.txt
```

Cela change le groupe propriétaire d'un fichier nommé `myfile.txt` en un groupe appelé `newgroup`.

Changer le groupe propriétaire d'un répertoire de manière récursive :

```bash
chgrp -R newgroup /path/to/directory
```

Cela modifie le groupe propriétaire non seulement du répertoire spécifié, mais aussi de tout son contenu de manière récursive. Cela garantit que tout dans cette structure de répertoire est maintenant associé au groupe nommé `newgroup`.

Changer le groupe propriétaire et afficher les changements de manière verbeuse :

```bash
chgrp -v newgroup myfile.txt
```

Cela change le groupe propriétaire de `myfile.txt` en `newgroup` mais fournit également un message confirmant cette action. Cela rend le processus plus transparent et vous informe des changements au fur et à mesure qu'ils se produisent.

## `chmod` – Modifier les permissions des fichiers

La capacité à contrôler les permissions des fichiers est un aspect crucial de Red Hat Enterprise Linux (RHEL). La commande `chmod` est un outil puissant à cet effet. En utilisant cette commande, vous pouvez spécifier les niveaux d'accessibilité pour la lecture, l'écriture et l'exécution d'un fichier.

### Syntaxe de `chmod` :

```bash
chmod [OPTIONS] MODE FILE...
```

#### Permissions :

* Lire (`r`) : Permet de lire ou de voir le contenu d'un fichier.
    
* Écrire (`w`) : Permet de modifier ou de supprimer le fichier.
    
* Exécuter (`x`) : Accorde la permission d'exécuter un fichier (pour les scripts ou les binaires).
    

#### Représentation numérique :

* **0** : Aucune permission.
    
* **1** : Exécuter.
    
* **2** : Écrire.
    
* **3** : Écrire et exécuter. (2+1)
    
* **4** : Lire.
    
* **5** : Lire et exécuter. (4+1)
    
* **6** : Lire et écrire. (4+2)
    
* **7** : Lire, écrire et exécuter. (4+2+1)
    

#### Représentation symbolique :

* `u` : Utilisateur/Propriétaire.
    
* `g` : Groupe.
    
* `o` : Autres.
    
* `a` : Tous (équivalent à `ugo`).
    

### Exemples de `chmod` :

Attribuer des permissions de lecture et d'écriture pour le propriétaire :

```bash
chmod 600 myfile.txt
```

Après avoir exécuté `chmod 600 myfile.txt`, le propriétaire de `myfile.txt` aura un accès complet en lecture et écriture au fichier (le `6` dans `**6**00`), tandis que le groupe et les autres n'auront aucune permission (les deux 0 suivants dans `6**00**`).

Autoriser la lecture et l'exécution pour le propriétaire, la lecture pour le groupe, et aucun accès pour les autres :

```bash
chmod 540 script.sh
```

Le propriétaire du fichier a à la fois des permissions de lecture et d'exécution (`5`). Le groupe associé au fichier a un accès en lecture seule (`4`). Les autres utilisateurs (ceux qui ne sont pas dans le groupe propriétaire) n'ont aucune permission pour le fichier (`0`).

Fournir des permissions complètes pour tous (Lire, Écrire, Exécuter) :

```bash
chmod 777 important_file.txt
```

Le propriétaire, le groupe et tous les autres utilisateurs ont un accès complet pour lire, écrire et exécuter `important_file.txt`. Ce paramètre accorde les permissions les plus larges possibles, ce qui peut être risqué pour les fichiers sensibles ou importants en raison de l'accès non restreint.

Attribuer des permissions de lecture et d'écriture à l'utilisateur :

```bash
chmod u+rw myfile.txt
```

Le propriétaire de `myfile.txt` (`u`) obtient des permissions de lecture et d'écriture (`rw`), lui permettant de lire et d'écrire dans le fichier.

Supprimer la permission d'écriture pour les autres

```bash
chmod o-w myfile.txt
```

Les autres (utilisateurs ne faisant pas partie du groupe propriétaire – `o`) perdent leur permission d'écriture sur `myfile.txt` (`-w`). Ils pourront lire le fichier mais ne seront pas autorisés à le modifier.

## Listes de contrôle d'accès

Les listes de contrôle d'accès (ACL) dans Red Hat Enterprise Linux (RHEL) sont des extensions des permissions de fichier standard. Elles offrent un contrôle plus granulaire sur qui peut accéder à un fichier ou un répertoire en vous permettant de définir des permissions pour des utilisateurs ou des groupes spécifiques au-delà du propriétaire, du groupe et des autres traditionnels.

* Les permissions traditionnelles (lecture, écriture, exécution) régissent l'accès basé sur le propriétaire, le groupe et les autres.
    
* Les ACL étendent cela en permettant des permissions pour plusieurs utilisateurs et groupes.
    

Dans Red Hat Enterprise Linux (RHEL), `getfacl` et `setfacl` sont des commandes utilisées pour gérer les listes de contrôle d'accès (ACL) sur les fichiers et les répertoires.

### Exemples de listes de contrôle d'accès :

Comment afficher les ACL :

```bash
getfacl filename
```

Cela récupère et affiche les informations ACL pour ce fichier ou répertoire spécifique. Il fournit une vue plus complète des droits d'accès et des permissions configurés pour ce fichier particulier dans le système.

Comment définir les ACL :

**Syntaxe :**

```bash
setfacl -m u:username:permissions filename
```

**Exemple :**

```bash
setfacl -m u:john:rw important_file.txt
```

Le code ci-dessus modifie l'ACL de `important_file.txt`, accordant spécifiquement des permissions de lecture et d'écriture à l'utilisateur nommé `john`. Cela lui permet de lire et d'écrire dans le fichier sans affecter les permissions des autres utilisateurs.

Décortiquons le code :

* `setfacl` : La commande utilisée pour définir les ACL.
    
* `-m` : Cette option signifie "modifier" et est utilisée pour modifier les ACL existantes d'un fichier ou d'un répertoire sans altérer d'autres permissions qui pourraient déjà être définies.
    
* `u:username:permissions` : Cette partie spécifie l'utilisateur, son nom d'utilisateur et les permissions accordées ou modifiées pour cet utilisateur.
    
* `u` : Indique que l'entrée suivante concerne un utilisateur spécifique.
    
* `username` : Représente le nom d'utilisateur de l'utilisateur dont les permissions sont modifiées.
    
* `permissions` : Désigne les permissions spécifiques attribuées à l'utilisateur.
    

## La commande `umask`

Dans Red Hat Enterprise Linux (RHEL), `umask` signifie "user file creation mask". C'est une commande et un masque de création de mode de fichier qui détermine les permissions de fichier par défaut lors de la création d'un nouveau fichier ou répertoire.

Il est représenté sous la forme d'un nombre octal à trois chiffres (par exemple, 022, 002, etc.).

**Calcul :** La valeur `umask` soustrait les permissions des permissions par défaut maximales :

* Pour les fichiers : Commencez avec 666 (rw-rw-rw-) et soustrayez la valeur `umask`.
    
* Pour les répertoires : Commencez avec 777 (rwxrwxrwx) et soustrayez la valeur `umask`.
    

### Exemple de calcul de `umask`

Prenons un exemple où la valeur umask est `022`.

Pour les fichiers :

* Permissions maximales par défaut : `666` (`rw-rw-rw-`)
    
* Valeur umask : `022`
    
* Soustraction de la valeur umask (`022`) des permissions de fichier par défaut (`666`) :
    
* Pour le propriétaire : `6 (rw)` - `0 (pas d'écriture)` = `6 (rw-)`
    
* Pour le groupe : `6 (rw)` - `2 (pas d'écriture)` = `4 (r--)`
    
* Pour les autres : `6 (rw)` - `2 (pas d'écriture)` = `4 (r--)`
    

Après application de l'umask (`022`), les permissions résultantes pour les nouveaux fichiers deviennent `644` (`rw-r--r--`).

Pour les répertoires :

* Permissions maximales par défaut : `777` (`rwxrwxrwx`)
    
* Valeur umask : `022`
    
* Soustraction de la valeur umask (`022`) des permissions de répertoire par défaut (`777`) :
    
* Pour le propriétaire : `7 (rwx)` - `0 (pas d'écriture)` = `7 (rwx)`
    
* Pour le groupe : `7 (rwx)` - `2 (pas d'écriture)` = `5 (r-x)`
    
* Pour les autres : `7 (rwx)` - `2 (pas d'écriture)` = `5 (r-x)`
    

Après application de l'umask (`022`), les permissions résultantes pour les nouveaux répertoires deviennent `755` (`rwxr-xr-x`).

Ainsi, avec une valeur umask de `022`, les nouveaux fichiers auront des permissions par défaut de `644` (`rw-r--r--`) et les nouveaux répertoires auront des permissions par défaut de `755` (`rwxr-xr-x`).

### Exemples de `umask` :

Vérifier le `umask` actuel :

```bash
umask
```

Changer temporairement le `umask`

```bash
umask [new_umask_value]
```

* Le premier chiffre représente les permissions supprimées pour le propriétaire du fichier.
    
* Le deuxième chiffre représente les permissions supprimées pour le groupe.
    
* Le troisième chiffre représente les permissions supprimées pour les autres (utilisateurs ne faisant pas partie du groupe propriétaire).
    

Exemples de valeurs umask et leurs implications :

* `000` : Aucune permission n'est supprimée, résultant en des permissions complètes de lecture, d'écriture et d'exécution pour tout le monde (non recommandé en raison des implications de sécurité).
    
* `022` : Supprime la permission d'écriture pour les autres, couramment utilisé pour s'assurer que les autres peuvent lire mais pas modifier les fichiers créés par le propriétaire.
    
* `077` : Supprime toutes les permissions pour le groupe et les autres, permettant uniquement au propriétaire des permissions complètes de lecture, d'écriture et d'exécution.
    
* `002` : Similaire à `022`, mais permet en plus aux membres du groupe d'écrire dans les fichiers qu'ils créent.
    

#### Changement permanent de `umask`

Si vous souhaitez ou avez besoin de changer le `umask` à l'échelle du système (ce qui est permanent), voici comment faire :

* Pour les changements à l'échelle du système, modifiez les fichiers de configuration du système comme `/etc/profile`, `/etc/bashrc`, ou les fichiers spécifiques au shell.
    
* Modifiez le fichier en utilisant un éditeur de texte avec des privilèges administratifs :
    

```bash
 sudo nano /etc/profile
```

* Localisez la ligne définissant la valeur `umask` et ajustez-la en conséquence.
    
* Enregistrez le fichier et quittez l'éditeur de texte.
    

Vous pouvez également changer le `umask` spécifique à l'utilisateur (également permanent). Voici comment faire :

* Pour les changements spécifiques à un utilisateur, modifiez son fichier d'initialisation (par exemple, `~/.bashrc`, `~/.bash_profile`, `~/.profile`)
    

```bash
vim ~/.bashrc
```

* Ajoutez ou modifiez la ligne `umask` selon les besoins.
    
* Enregistrez le fichier et quittez l'éditeur de texte.
    

Pour confirmer les changements, tapez cette commande :

```bash
umask
```

## Exercices pratiques

Voici quelques exercices pour vous aider à pratiquer ce que nous avons couvert ici. Essayez de les faire par vous-même.

### Voir les permissions des fichiers :

* Utilisez la commande `ls -l` pour voir les permissions détaillées des fichiers dans votre répertoire courant.
    
* Interprétez la sortie, en comprenant le type de fichier, les permissions, le nombre de liens, le propriétaire, le groupe, la taille du fichier, l'heure de la dernière modification, et le nom du fichier/répertoire.
    

### Changer la propriété d'un fichier :

* Créez un fichier nommé `example.txt` en utilisant n'importe quel éditeur de texte (par exemple, `touch example.txt`).
    
* Utilisez la commande `ls -l` pour vérifier la propriété de `example.txt`.
    
* Utilisez la commande `chown` pour changer la propriété de `example.txt` à un autre utilisateur (remplacez `newowner` par un nom d'utilisateur réel).
    
* Vérifiez le changement de propriété en utilisant `ls -l`.
    

#### Changer le groupe propriétaire d'un fichier :

* Créez un autre fichier nommé `data.txt`.
    
* Utilisez la commande `ls -l` pour vérifier le groupe propriétaire de `data.txt`.
    
* Utilisez la commande `chgrp` pour changer le groupe propriétaire de `data.txt` à un autre groupe (remplacez `newgroup` par un nom de groupe réel).
    
* Confirmez le changement de groupe propriétaire en utilisant `ls -l`.
    

#### Modifier les permissions d'un fichier :

* Créez un troisième fichier nommé `script.sh`.
    
* Utilisez la commande `ls -l` pour voir les permissions par défaut de `script.sh`.
    
* Utilisez la commande `chmod` pour donner au propriétaire des permissions de lecture et d'exécution, au groupe des permissions de lecture, et aucune permission aux autres.
    
* Vérifiez les changements de permissions en utilisant `ls -l`.
    

#### Définir les ACL :

* Créez un répertoire nommé `secure_folder`.
    
* Utilisez `getfacl` pour voir les ACL du répertoire.
    
* Utilisez `setfacl` pour accorder des permissions de lecture et d'écriture à un utilisateur spécifique (remplacez `john` par un nom d'utilisateur réel).
    
* Vérifiez les changements d'ACL en utilisant `getfacl`.
    

#### Comprendre Umask :

* Vérifiez la valeur umask actuelle en utilisant la commande `umask`.
    
* Créez un nouveau fichier nommé `confidential.txt`.
    
* Utilisez `ls -l` pour voir les permissions par défaut de `confidential.txt`.
    
* Changez temporairement la valeur umask à `027` en utilisant la commande `umask`.
    
* Créez un autre fichier nommé `secret.txt` et vérifiez ses permissions par défaut.
    

#### Changement permanent de Umask :

* Pour les changements à l'échelle du système, modifiez le fichier de configuration du système (par exemple, `/etc/profile`, `/etc/bashrc`) pour définir un nouveau umask par défaut.
    
* Pour les changements spécifiques à un utilisateur, modifiez le fichier d'initialisation de l'utilisateur (par exemple, `~/.bashrc`, `~/.bash_profile`) pour définir un nouveau umask.
    
* Vérifiez les changements en créant un nouveau fichier et en vérifiant ses permissions par défaut.
    

## Conclusion

Merci d'avoir exploré le monde de l'administration de Red Hat Enterprise Linux (RHEL) avec moi aujourd'hui.

Nous avons couvert les commandes essentielles pour une gestion précise des fichiers dans Red Hat Enterprise Linux, offrant des exemples pratiques et des exercices pour renforcer la compréhension et la maîtrise.

Vous pouvez plonger plus profondément dans le domaine de l'expertise Linux et rester à l'écoute pour plus de contenu perspicace dans mes futurs tutoriels.

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)