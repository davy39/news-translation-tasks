---
title: Le guide ultime de SSH - Configuration des clés SSH
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-03T18:03:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-ssh-setting-up-ssh-keys
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ee3740569d1a4ca3fb6.jpg
tags:
- name: ssh
  slug: ssh
seo_title: Le guide ultime de SSH - Configuration des clés SSH
seo_desc: 'Welcome to our ultimate guide to setting up SSH (Secure Shell) keys. This
  tutorial will walk you through the basics of creating SSH keys, and also how to
  manage multiple keys and key pairs.

  Create a New SSH Key Pair

  Open a terminal and run the follow...'
---

Bienvenue dans notre guide ultime pour la configuration des clés SSH (Secure Shell). Ce tutoriel vous guidera à travers les bases de la création de clés SSH, ainsi que la gestion de plusieurs clés et paires de clés.

## Créer une nouvelle paire de clés SSH

Ouvrez un terminal et exécutez la commande suivante :

```text
ssh-keygen
```

Vous verrez le texte suivant :

```text
Generating public/private rsa key pair.
Enter file in which to save the key (/home/username/.ssh/id_rsa):
```

Appuyez sur Entrée pour enregistrer vos clés dans le répertoire par défaut `/home/username/.ssh`.

Ensuite, vous serez invité à entrer un mot de passe :

```text
Enter passphrase (empty for no passphrase):
```

Il est recommandé d'entrer un mot de passe ici pour une couche supplémentaire de sécurité. En définissant un mot de passe, vous pourriez empêcher l'accès non autorisé à vos serveurs et comptes si quelqu'un obtient votre clé SSH privée ou votre machine.

Après avoir entré et confirmé votre mot de passe, vous verrez ce qui suit :

```text
Your identification has been saved in /home/username/.ssh/id_rsa.
Your public key has been saved in /home/username/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:/qRoWhRcIBTw0D4KpTUyK6YepyL6RQ2CQrtWsaicCb4 username@871e129f767b
The key's randomart image is:
+---[RSA 2048]----+
| .o=+....        |
|+.*o+o .         |
|+X.=o o          |
|@.=.oo .         |
|=O ...o S        |
|o.oo . .         |
|.E+ . . . .      |
|oo . ... +       |
|=.. .o. . .      |
+----[SHA256]-----+
```

Vous avez maintenant une paire de clés SSH publique et privée que vous pouvez utiliser pour accéder à des serveurs distants et pour gérer l'authentification pour des programmes en ligne de commande comme Git.

## Gérer plusieurs clés SSH

Bien qu'il soit considéré comme une bonne pratique d'avoir une seule paire de clés publique-privée par appareil, parfois vous devez utiliser plusieurs clés ou vous avez des noms de clés non orthodoxes. Par exemple, vous pourriez utiliser une paire de clés SSH pour travailler sur les projets internes de votre entreprise, mais vous pourriez utiliser une clé différente pour accéder aux serveurs d'un client. En plus de cela, vous pourriez utiliser une paire de clés différente pour accéder à votre propre serveur privé.

La gestion des clés SSH peut devenir fastidieuse dès que vous devez utiliser une deuxième clé. Traditionnellement, vous utiliseriez `ssh-add` pour stocker vos clés dans `ssh-agent`, en tapant le mot de passe pour chaque clé. Le problème est que vous devriez faire cela chaque fois que vous redémarrez votre ordinateur, ce qui peut rapidement devenir fastidieux.

Une meilleure solution est d'automatiser l'ajout des clés, de stocker les mots de passe et de spécifier quelle clé utiliser lors de l'accès à certains serveurs.

### SSH `config`

Entrez SSH `config`, qui est un fichier de configuration par utilisateur pour la communication SSH. Créez un nouveau fichier : `~/.ssh/config` et ouvrez-le pour l'éditer :

```text
nano ~/.ssh/config
```

### Gestion des clés SSH nommées personnalisées

La première chose que nous allons résoudre en utilisant ce fichier `config` est d'éviter d'avoir à ajouter des clés SSH nommées personnalisées en utilisant `ssh-add`. En supposant que votre clé SSH privée est nommée `~/.ssh/id_rsa`, ajoutez ce qui suit au fichier `config` :

```bash
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa
  IdentitiesOnly yes
```

Ensuite, assurez-vous que `~/.ssh/id_rsa` n'est pas dans `ssh-agent` en ouvrant un autre terminal et en exécutant la commande suivante :

```text
ssh-add -D
```

Cette commande supprimera toutes les clés de la session `ssh-agent` actuellement active.

Maintenant, si vous essayez de cloner un dépôt GitHub, votre fichier `config` utilisera la clé à `~/.ssh/ida_rsa`.

Voici quelques autres exemples de configuration utiles :

```bash
Host bitbucket-corporate
        HostName bitbucket.org
        User git
        IdentityFile ~/.ssh/id_rsa_corp
        IdentitiesOnly yes
```

Maintenant, vous pouvez utiliser `git clone git@bitbucket-corporate:company/project.git`

```bash
Host bitbucket-personal
        HostName bitbucket.org
        User git
        IdentityFile ~/.ssh/id_rsa_personal
        IdentitiesOnly yes
```

Maintenant, vous pouvez utiliser `git clone git@bitbucket-personal:username/other-pi-project.git`

```text
Host myserver
        HostName ssh.username.com
        Port 1111
        IdentityFile ~/.ssh/id_rsa_personal
        IdentitiesOnly yes
        User username
        IdentitiesOnly yes
```

Maintenant, vous pouvez vous connecter à votre serveur en utilisant `ssh myserver`. Vous n'avez plus besoin d'entrer un port et un nom d'utilisateur chaque fois que vous vous connectez à votre serveur privé.

### Gestion des mots de passe

La dernière pièce du puzzle est la gestion des mots de passe. Il peut devenir très fastidieux d'entrer un mot de passe chaque fois que vous initialisez une connexion SSH. Pour contourner cela, nous pouvons utiliser le logiciel de gestion des mots de passe qui vient avec macOS et diverses distributions Linux.

Pour ce tutoriel, nous utiliserons le programme Keychain Access de macOS. Commencez par ajouter votre clé à Keychain Access en passant l'option `-K` à la commande `ssh-add` :

```bash
ssh-add -K ~/.ssh/id_rsa_whatever
```

Maintenant, vous pouvez voir votre clé SSH dans Keychain Access :

![Keychain Access](https://raw.githubusercontent.com/fvoska/guides/master/static/images/pages/ssh/managing-multiple-ssh-keys/keychain-access.png)

Mais si vous supprimez les clés de `ssh-agent` avec `ssh-add -D` ou redémarrez votre ordinateur, vous serez à nouveau invité à entrer un mot de passe lorsque vous essayez d'utiliser SSH. Il s'avère qu'il y a encore un cerceau à franchir. Ouvrez votre fichier de configuration SSH en exécutant `nano ~/.ssh/config` et ajoutez ce qui suit :

```bash
Host *
  AddKeysToAgent yes
  UseKeychain yes
```

Avec cela, chaque fois que vous exécutez `ssh`, il recherchera les clés dans Keychain Access. Si elle en trouve une, vous ne serez plus invité à entrer un mot de passe. Les clés seront également automatiquement ajoutées à `ssh-agent` chaque fois que vous redémarrez votre machine.

Maintenant que vous connaissez les bases de la création de nouvelles clés SSH et de la gestion de plusieurs clés, allez-y et utilisez `ssh` à votre guise !