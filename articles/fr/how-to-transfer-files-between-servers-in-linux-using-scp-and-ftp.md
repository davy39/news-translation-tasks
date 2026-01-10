---
title: Comment transférer des fichiers entre des serveurs sous Linux en utilisant
  SCP et FTP
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-12-20T16:02:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-transfer-files-between-servers-in-linux-using-scp-and-ftp
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Transfer-files-FTP-and-SCP.png
tags:
- name: Linux
  slug: linux
seo_title: Comment transférer des fichiers entre des serveurs sous Linux en utilisant
  SCP et FTP
seo_desc: "Transferring files between machines is a very common operational task that\
  \ you'll do all the time as a developer. \nLinux provides a number of utilities\
  \ to transfer files. In this tutorial we will discuss FTP and SCP. Many automated\
  \ scripts also deplo..."
---

Transférer des fichiers entre des machines est une tâche opérationnelle très courante que vous effectuerez tout le temps en tant que développeur. 

Linux fournit un certain nombre d'utilitaires pour transférer des fichiers. Dans ce tutoriel, nous allons discuter de `FTP` et `SCP`. De nombreux scripts automatisés utilisent également FTP ou SCP pour déplacer des fichiers.

## Qu'est-ce que FTP ?

FTP est un protocole réseau utilisé pour échanger des fichiers sur le réseau. Il utilise le port 21. FTP vous permet d'accéder à un système distant pour échanger des fichiers en utilisant la commande `ftp`.

### Syntaxe FTP

La syntaxe FTP est la suivante :

```bash
ftp hôte
```

Ici, `hôte` peut être soit le nom d'hôte, soit l'adresse IP de l'hôte distant.

### Commandes FTP

Les commandes FTP sont similaires aux commandes Linux. Nous allons en discuter certaines.

<table>
<thead>
<tr>
<th>Commande</th>
<th>Utilisation</th>
</tr>
</thead>
<tbody>
<tr>
<td>open</td>
<td>Ouvre une connexion distante avec un autre ordinateur.</td>
</tr>
<tr>
<td>get</td>
<td>Copie un fichier du système distant vers le système local.</td>
</tr>
<tr>
<td>put</td>
<td>Copie un fichier du système local vers un répertoire sur le système distant.</td>
</tr>
<tr>
<td>mget</td>
<td>Transfère plusieurs fichiers du système distant vers le répertoire courant du système local.</td>
</tr>
<tr>
<td>mput</td>
<td>Transfère plusieurs fichiers du système local vers un répertoire sur le système distant.</td>
</tr>
<tr>
<td>bye/quit</td>
<td>Prépare la sortie de l'environnement FTP.</td>
</tr>
<tr>
<td>close</td>
<td>Termine la connexion FTP.</td>
</tr>
<tr>
<td>ascii</td>
<td>Active le mode de transfert de fichiers en ASCII</td>
</tr>
<tr>
<td>binary</td>
<td>Active le mode de transfert de fichiers en binaire.</td>
</tr>
</tbody>
</table>

### Comment transférer des fichiers via FTP

FTP offre deux modes de transfert : ASCII et Binaire.

1. **ASCII signifie **American Standard Code for Information Interchange**.** Il est utilisé pour transférer des fichiers simples tels que des fichiers texte.
2. **Mode binaire** : Le mode binaire est utilisé pour transférer des fichiers non texte tels que des images.

Le mode de transfert par défaut est ASCII.

#### Étape 1 – Se connecter à FTP

Dans l'exemple ci-dessous, `hostA` est l'hôte distant. Vous serez invité à entrer un nom d'utilisateur et un mot de passe.

```bash
$ ftp hostA
Connected to hostA.
220 hostA FTP server ready.
Name (hostA:user): user
331 Password required for user.
Password: password
230 User user logged in.
Remote system type is LINUX.

```

Une fois la connexion établie, vous remarquerez le symbole `ftp>` au début. Maintenant, nous pouvons exécuter les commandes FTP.

#### Étape 2 – Choisir le mode de transfert de fichiers

Vous pouvez choisir le mode (binaire ou ASCII) en fonction de votre type de fichier.

```bash
ftp> ascii
200 Type set to A.
```

#### Étape 3 – Transférer des fichiers

Nous utilisons la commande `get` pour transférer le fichier `sample.txt` du serveur FTP distant vers la machine locale.

```bash
ftp> get sample.txt
200 PORT command successful.
150 Opening ASCII mode data connection for sample.txt (22 bytes).
226 Transfer complete.
local: sample.txt remote: sample.txt
22 bytes received in 0.012 seconds (1.54 Kbytes/s)
```

#### Étape 4. Terminer la session

```bash
ftp> bye
221-You have transferred 22 bytes in 1 files.
221-Total traffic for this session was 126 bytes in 2 transfers. 221-Thank you for using the FTP service on hostA.
221 Goodbye.
```

### Comment transférer plusieurs fichiers via FTP

Pour transférer des fichiers en masse, il existe deux commandes : `mget` et `mput`.

Vous utilisez `mget` pour télécharger les fichiers, tandis que vous utilisez `mput` pour les téléverser.

```bash
ftp> mget sample_file.1 sample_file.2
```

```bash
ftp> mput sample_file.1 sample_file.2
```

Toutes les étapes que nous venons d'apprendre peuvent être placées dans un fichier exécutable et planifiées. Vous pouvez trouver le code pour l'automatisation [ici](https://github.com/zairahira/FTP-Automation-Script).

## Qu'est-ce que SCP ?

SCP signifie Secure Copy. Il utilise SSH et le port 22. Les données transférées via SCP sont chiffrées et les renifleurs ne peuvent pas y accéder. Cela rend SCP très sécurisé.

Vous pouvez utiliser SCP pour :

* Transférer des fichiers de la machine locale vers l'hôte distant.
* Transférer des fichiers de l'hôte distant vers la machine locale.

### Syntaxe SCP

Explorons la syntaxe de SCP.

```bash
scp [FLAG] [user@]SOURCE_HOST:]/chemin/vers/fichier1 [user@]DESTINATION_HOST:]/chemin/vers/fichier2

```

* `[FLAG]` spécifie les options qui peuvent être données à SCP. Voici quelques détails sur les flags :

<table>
<thead>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>-r</td>
<td>Pour copier récursivement des répertoires.</td>
</tr>
<tr>
<td>-q</td>
<td>Utilisé pour masquer le compteur de progression et toute autre information autre que les erreurs.</td>
</tr>
<tr>
<td>-C</td>
<td>Utilisé pour compresser les données lors de leur envoi à leur destination.</td>
</tr>
<tr>
<td>-P</td>
<td>Spécifie le port SSH de destination.</td>
</tr>
<tr>
<td>-p</td>
<td>Préserve les heures d'accès aux fichiers.</td>
</tr>
</tbody>
</table>

* `[user@]SOURCE_HOST` est la machine source.
* `[user@]DESTINATION_HOST:]` est la machine de destination.

**Note** : _Pour transférer des fichiers via SCP, les identifiants doivent être connus et l'utilisateur doit avoir les permissions d'écriture._

### Comment transférer des fichiers de la machine locale vers l'hôte distant via `SCP`

Pour transférer des fichiers vers un hôte distant, utilisez la commande suivante :

```bash
scp source_file.txt remote_username@10.13.13.11:/chemin/vers/répertoire/distant
```

Dans la commande ci-dessus, `source_file.txt` est le fichier à copier. `Remote_username` est le nom d'utilisateur pour l'hôte distant `10.13.13.11`. Après `:` le chemin de destination est spécifié.

Exemple de sortie :

```bash
remote_username@10.13.13.11's password:
source_file.txt                             100%    0     0.0KB/s   00:00

```

Le fichier `source_file.txt` sera maintenant placé dans `/chemin/vers/répertoire/distant`.

Pour copier des répertoires, utilisez le flag `-r` comme démontré ci-dessous.

```bash
scp -r /répertoire/local remote_username@10.13.13.11:/chemin/vers/répertoire/distant
```

### Comment transférer des fichiers de l'hôte distant vers la machine locale via `SCP`

Pour transférer des fichiers d'un hôte distant vers une machine locale, utilisez la commande suivante :

```bash
scp remote_username@10.13.13.11:/répertoire/source_file.txt /chemin/vers/répertoire/local
```

> Soyez très prudent lors du transfert de fichiers car SCP **écrase** les fichiers déjà existants.

## Conclusion

Dans ce tutoriel, vous avez appris comment transférer des fichiers et des répertoires en utilisant FTP et SCP via la ligne de commande. 

Lorsque ces commandes sont automatisées, elles servent des buts encore plus grands dans l'entreposage de données, l'ETL (Extract, Transform, Load), la génération de rapports, l'archivage et le traitement de fichiers en masse. Essayez ces commandes. Connectons-nous sur [Twitter](https://twitter.com/hira_zaira).