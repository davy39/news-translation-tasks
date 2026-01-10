---
title: Permissions Linux – Comment trouver les permissions d'un fichier
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-04-19T21:49:02.000Z'
originalURL: https://freecodecamp.org/news/linux-permissions-how-to-find-permissions-of-a-file
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Copy-of-python-append.png
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: Permissions Linux – Comment trouver les permissions d'un fichier
seo_desc: "Linux is a multi-user Operating System which means it supports multiple\
  \ users on a single system. \nEach user has its own rights which might be limited\
  \ as well to increase security. For example, users have a particular set of permissions\
  \ to access a f..."
---

Linux est un système d'exploitation multi-utilisateurs, ce qui signifie qu'il supporte plusieurs utilisateurs sur un seul système. 

Chaque utilisateur a ses propres droits, qui peuvent également être limités pour augmenter la sécurité. Par exemple, les utilisateurs ont un ensemble particulier de permissions pour accéder à un fichier – certains utilisateurs peuvent être en mesure d'écrire tandis que d'autres ne peuvent que lire.

Dans ce tutoriel, nous apprendrons :

* Quels sont les utilisateurs et les groupes et les différents types d'utilisateurs dans Linux.
* Visualisation des propriétés et des permissions.
* Comprendre les permissions de lecture, d'écriture et d'exécution.
* Lire les permissions via le mode symbolique.

## Utilisateurs et Groupes dans Linux

Avant de comprendre les permissions, nous devons comprendre les `utilisateurs` et les `groupes`, car les propriétés et les permissions s'appliquent à ces entités. 

### Utilisateurs et types d'utilisateurs dans Linux

Il existe deux types d'utilisateurs : les `utilisateurs système` et les `utilisateurs réguliers`.

* Les **utilisateurs système** sont responsables de l'exécution des processus non interactifs et en arrière-plan sur un système. Par exemple : `mail`, `daemon`, `syslog`, etc.
* Les **utilisateurs réguliers** sont les utilisateurs qui se connectent réellement au système et effectuent leurs tâches désignées de manière interactive.

Nous pouvons vérifier les détails des utilisateurs sur un système en consultant le fichier /etc/passwd. La première colonne avant `:` montre le nom d'utilisateur.

```bash
cat /etc/passwd
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-144.png)
_Contenu du fichier /etc/passwd_

### Superutilisateur ou l'utilisateur `root`.

En plus des deux types d'utilisateurs, il y a le superutilisateur, ou utilisateur `root`, qui a des droits élevés. Cet utilisateur a le pouvoir de créer et de modifier des utilisateurs ainsi que de remplacer toute propriété et permission de fichier. 

D'autres comptes utilisateurs peuvent également être configurés pour avoir des droits de "superutilisateur". La meilleure pratique est d'accorder des privilèges élevés aux utilisateurs réguliers en utilisant 'sudo'. Les utilisateurs capables d'utiliser 'sudo' peuvent également effectuer les mêmes tâches que l'utilisateur root.

### Groupes dans Linux

Les utilisateurs peuvent appartenir à des groupes. Les groupes sont une collection d'utilisateurs. Un groupe définit les droits collectifs pour les utilisateurs qu'il contient. Un utilisateur peut appartenir à plus d'un groupe également. 

Nous pouvons visualiser les groupes sur un système en consultant le fichier `/etc/group`.

```bash
cat /etc/group

```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-145.png)
_Contenu du fichier `/etc/group`._

## Comment visualiser les propriétés et les permissions dans Linux

Maintenant que nous connaissons les utilisateurs et les groupes, voyons comment nous pouvons visualiser les permissions d'un fichier ou d'un dossier.

Nous pouvons utiliser la liste longue qui est la commande `ls` avec l'option `-l`.

`ls -l`

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-146.png)
_Sortie de la liste longue_

Examinons de plus près la colonne mode dans la sortie ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-147.png)
_Détails du mode dans la liste longue._

**Mode** définit deux choses :

* **Type de fichier** : Le type de fichier définit le type du fichier. Pour les fichiers réguliers qui contiennent des données simples, il est vide `-`. Pour les autres types de fichiers spéciaux, le symbole est différent. Pour un répertoire qui est un fichier spécial, il est `d`. Les fichiers spéciaux sont traités différemment par le système d'exploitation.
* **Classes de permission** : Le prochain ensemble de caractères définit les permissions pour l'utilisateur, le groupe et les autres respectivement. 
– **Utilisateur** : Il s'agit du propriétaire d'un fichier et le propriétaire du fichier appartient à cette classe. 
– **Groupe** : Les membres du groupe du fichier appartiennent à cette classe 
– **Autre** : Tout utilisateur qui ne fait pas partie des classes utilisateur ou groupe appartient à cette classe.

### Comment lire les permissions symboliques

La représentation `rwx` est connue sous le nom de représentation symbolique des permissions. Dans l'ensemble des permissions, 

* **`r`** signifie **lecture**. Il est indiqué dans le premier caractère de la triade.
* **`w`** signifie **écriture**. Il est indiqué dans le deuxième caractère de la triade.
* **`x`** signifie **exécution**. Il est indiqué dans le troisième caractère de la triade.

## Comprendre les permissions symboliques

### Lecture

Pour les fichiers réguliers, les permissions de lecture permettent d'ouvrir et de lire uniquement le fichier. Les utilisateurs ne peuvent pas modifier le fichier. 

De même, pour les répertoires, les permissions de lecture permettent de lister le contenu du répertoire sans aucune modification dans le répertoire.

### Écriture

Lorsque les fichiers ont des permissions d'écriture, l'utilisateur peut modifier (éditer, supprimer) le fichier et l'enregistrer. 

Pour les dossiers, les permissions d'écriture permettent à un utilisateur de modifier son contenu (créer, supprimer et renommer les fichiers à l'intérieur), et de modifier le contenu des fichiers pour lesquels l'utilisateur a des permissions d'écriture.

### Exécution

Pour les fichiers, les permissions d'exécution permettent à l'utilisateur d'exécuter un script exécutable. Pour les répertoires, l'utilisateur peut y accéder et accéder aux détails des fichiers dans le répertoire.

## Exemples de permissions dans Linux

Maintenant que nous savons comment lire les permissions, voyons quelques exemples.

* `-rwx------` : Un fichier qui n'est accessible et exécutable que par son propriétaire.
* `-rw-rw-r--` : Un fichier qui est ouvert à la modification par son propriétaire et son groupe mais pas par les autres.
* `drwxrwx---` : Un répertoire qui peut être modifié par son propriétaire et son groupe.

## Conclusion

Dans ce tutoriel, nous avons appris à propos des utilisateurs et des groupes dans Linux. Nous avons également appris comment lire et visualiser les permissions. 

Il est important de comprendre ces permissions car elles font partie intégrante de l'administration système.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).