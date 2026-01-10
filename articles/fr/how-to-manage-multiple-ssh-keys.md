---
title: Comment gérer plusieurs clés SSH
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T21:46:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-multiple-ssh-keys
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d43740569d1a4ca36c9.jpg
tags:
- name: ssh
  slug: ssh
seo_title: Comment gérer plusieurs clés SSH
seo_desc: It is safe to say that most developers in the web sphere have at some point
  encountered SSH. SSH is one of the most used protocols for safe data exchange. You
  use SSH for connecting to remote servers, which also includes managing your code
  using Git ...
---

Il est sûr de dire que la plupart des développeurs dans le domaine du web ont à un moment donné rencontré SSH. SSH est l'un des protocoles les plus utilisés pour l'échange sécurisé de données. Vous utilisez SSH pour vous connecter à des serveurs distants, ce qui inclut également la gestion de votre code avec Git et la synchronisation avec des dépôts distants.

Bien qu'il soit considéré comme une bonne pratique d'avoir une paire de clés privée-publique par appareil, parfois vous devez utiliser plusieurs clés et/ou vous avez des noms de clés non orthodoxes.

Vous pourriez utiliser une paire de clés SSH pour travailler sur les projets internes de votre entreprise, mais vous pourriez utiliser une clé différente pour accéder aux serveurs d'un client d'entreprise. Vous pourriez même utiliser une clé différente pour accéder à votre propre serveur privé.

La gestion des clés SSH peut devenir fastidieuse dès que vous devez utiliser une deuxième clé. J'espère que cet article sera utile à quiconque a des problèmes avec la gestion des clés SSH.

Je suppose que le lecteur a des connaissances de base sur Git et SSH. La plupart des exemples tout au long de l'article utiliseront Git. Bien sûr, tout cela s'appliquera à toute autre communication SSH. Cela dit, il y a quelques astuces spécifiques à Git incluses.

Attachez vos ceintures, c'est parti !

## Gérer une seule clé SSH

Tout d'abord, voyons à quoi pourrait ressembler votre flux de travail avant d'avoir plusieurs clés à gérer.

Vous avez une clé privée stockée dans `~/.ssh/id_rsa` avec une clé publique correspondante `~/.ssh/id_rsa.pub`.

Imaginons que vous souhaitez pousser/tirer des modifications de code vers/depuis un serveur Git distant – disons GitHub, pourquoi pas. Pour ce faire, vous devez d'abord ajouter votre clé publique à GitHub.

Je ne vais pas passer par cette étape, il devrait être assez facile de trouver comment faire. J'ai également supposé que votre nom est Steve et que vous travaillez sur un projet top-secret qui utilise des Raspberry Pi pour espionner le trafic réseau.

Pour commencer votre travail, vous devez cloner un dépôt git en utilisant SSH :

```bash
git clone git@github.com:steve/raspberry-spy.git
```

À ce moment-là, GitHub sera comme : « Yo, c'est un dépôt privé ! Nous devons chiffrer le trafic en utilisant cette clé publique que j'ai ici et votre clé privée. »

Vous avez ajouté la clé publique à votre profil sur GitHub, mais SSH doit somehow déterminer où se trouve votre clé privée correspondante.

Puisque nous n'avons aucune idée de quelle clé privée doit être utilisée lorsque nous nous connectons via SSH à `git@github.com`, le client SSH essaie de trouver une clé à l'emplacement par défaut, qui est `~/.ssh/id_rsa` - c'est son meilleur choix. Si aucun fichier n'est présent à cet emplacement, vous obtiendrez une erreur :

```bash
Cloning into 'raspberry-spy'...
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

Si vous avez une clé privée stockée dans le fichier `~/.ssh/id_rsa`, le client SSH utilisera cette clé privée pour le chiffrement de la communication. Si cette clé est protégée par un mot de passe (comme elle devrait l'être), vous serez invité à entrer un mot de passe, comme ceci :

```bash
Enter passphrase for key '/Users/steve/.ssh/id_rsa':
```

Si vous entrez la phrase de passe correcte et si cette clé privée correspond effectivement à la clé publique que vous avez attachée à votre profil, tout se passera bien et le dépôt sera cloné avec succès.

Mais que se passe-t-il si vous avez nommé votre clé différemment (ex. `~/.ssh/_id_rsa`) ? Le client SSH ne pourra pas déterminer où la clé privée est stockée. Vous obtiendrez la même erreur `Permission denied ...` qu'auparavant.

Si vous souhaitez utiliser une clé privée que vous avez nommée différemment, vous devez l'ajouter manuellement :

```bash
ssh-add ~/.ssh/_id_rsa
```

Après avoir entré la phrase de passe, vous pouvez vérifier si la clé a été ajoutée à `ssh-agent` (client SSH) en exécutant `ssh-add -l`. Cette commande listera toutes les clés qui sont actuellement disponibles pour le client SSH.

Si vous essayez de cloner le dépôt maintenant, cela sera réussi.

## **Jusqu'à présent, tout va bien ?**

Si vous êtes perspicace, vous pourriez commencer à remarquer certains problèmes potentiels.

Tout d'abord, si vous redémarrez votre ordinateur, `ssh-agent` redémarrera et vous devrez ajouter vos clés non nommées par défaut en utilisant `ssh-add` à nouveau, en tapant les mots de passe et tout ce travail fastidieux.

Pouvons-nous automatiser l'ajout des clés ou spécifier d'une manière ou d'une autre quelle clé utiliser lors de l'accès à certains serveurs ?

Pouvons-nous enregistrer les mots de passe d'une manière ou d'une autre pour ne pas avoir à les taper à chaque fois ? Si seulement il existait quelque chose comme un _trousseau_ pour enregistrer les clés SSH protégées par mot de passe.

Soyez assuré, il existe des réponses à toutes ces questions.

## **Entrez, SSH `config`**

Il s'avère que le fichier de configuration SSH est une chose, une chose qui peut nous aider. C'est un fichier de configuration par utilisateur pour la communication SSH. Créez un nouveau fichier : `~/.ssh/config` et ouvrez-le pour l'éditer.

### **Gestion des clés SSH avec des noms personnalisés**

La première chose que nous allons résoudre en utilisant ce fichier `config` est d'éviter d'avoir à ajouter des clés SSH avec des noms personnalisés en utilisant `ssh-add`. En supposant que votre clé SSH s'appelle `~/.ssh/_id_rsa`, ajoutez ce qui suit au fichier `config` :

```bash
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/_id_rsa
  IdentitiesOnly yes
```

Maintenant, assurez-vous que `~/.ssh/_id_rsa` n'est pas dans `ssh-agent` en exécutant `ssh-add -D`. Cette commande supprimera toutes les clés de la session `ssh-agent` actuellement active. La session est réinitialisée chaque fois que vous vous déconnectez ou redémarrez (ou si vous tuez manuellement le processus `ssh-agent`). Nous pouvons « simuler » un redémarrage en exécutant la commande mentionnée.

Si vous essayez de cloner votre dépôt GitHub maintenant, ce sera la même chose que si nous avions ajouté la clé manuellement (comme nous l'avons fait avant). Vous serez invité à entrer un mot de passe :

```bash
git clone git@github.com:steve/raspberry-spy.git
Cloning into 'raspberry-spy'...
Enter passphrase for key '/Users/steve/.ssh/_id_rsa':
```

Vous aurez remarqué que la clé pour laquelle nous sommes invités à entrer un mot de passe est la même clé que celle que nous avons spécifiée dans notre fichier `config`. Après avoir entré le mot de passe correct de la clé SSH, le dépôt sera cloné avec succès.

Remarque : si, après un clonage réussi, vous essayez `git pull`, vous serez à nouveau invité à entrer un mot de passe. Nous résoudrons cela plus tard.

Il est important que `Host github.com` de `config` et `github.com` de l'URI `git@github.com:steve/raspberry-spy.git` correspondent. Vous pouvez également changer `config` pour être `Host mygithub` et cloner en utilisant l'URI `git@mygithub:steve/raspberry-spy.git`.

Cela ouvre les vannes. Alors que vous lisez ceci, votre esprit s'emballe et pense à la façon dont tous vos problèmes avec les clés SSH sont résolus. Voici quelques exemples de configurations utiles :

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

Maintenant, vous pouvez utiliser `git clone git@bitbucket-personal:steve/other-pi-project.git`

```text
Host myserver
        HostName ssh.steve.com
        Port 1111
        IdentityFile ~/.ssh/id_rsa_personal
        IdentitiesOnly yes
        User steve
        IdentitiesOnly yes
```

Maintenant, vous pouvez vous connecter à votre serveur en utilisant `ssh myserver`. N'est-ce pas génial ? Vous n'avez pas besoin de saisir le port et le nom d'utilisateur manuellement à chaque fois que vous exécutez la commande `ssh`.

### Bonus : Paramètres par dépôt

Vous pouvez également définir quelle clé spécifique doit être utilisée pour un certain dépôt, en remplaçant tout ce qui se trouve dans la configuration SSH. Une commande SSH spécifique peut être définie en définissant `sshCommand` sous `core` dans `<project>/.git/config`. Exemple :

```bash
[core]
        sshCommand = ssh -i ~/.ssh/id_rsa_corp
```

Cela est possible avec git 2.10 ou ultérieur. Vous pouvez également utiliser cette commande pour éviter d'éditer le fichier manuellement :

```bash
git config core.sshCommand 'ssh -i ~/.ssh/id_rsa_corp'
```

## Gestion des mots de passe

La dernière pièce du puzzle est la gestion des mots de passe. Nous voulons éviter d'avoir à entrer un mot de passe à chaque fois qu'une connexion SSH est initiée. Pour ce faire, nous pouvons utiliser le logiciel de gestion de trousseau qui vient avec MacOS et diverses distributions Linux.

Commencez par ajouter votre clé au trousseau en passant l'option `-K` à la commande `ssh-add` :

```bash
ssh-add -K ~/.ssh/id_rsa_whatever
```

Maintenant, vous pouvez voir votre clé SSH dans le trousseau. Sur MacOS, cela ressemble à quelque chose comme ceci :

![Keychain Access](https://raw.githubusercontent.com/fvoska/guides/master/static/images/pages/ssh/managing-multiple-ssh-keys/keychain-access.png)

Si vous supprimez les clés de `ssh-agent` via `ssh-add -D` (cela se produira lorsque vous redémarrerez votre ordinateur, comme mentionné précédemment) et essayez de vous connecter via SSH, vous serez à nouveau invité à entrer un mot de passe. Pourquoi ? Nous venons d'ajouter la clé au trousseau. Si vous vérifiez à nouveau l'accès au trousseau, vous remarquerez que la clé que vous avez ajoutée en utilisant `ssh-add -K` est toujours dans le trousseau. Bizarre, hein ?

Il s'avère qu'il y a encore un cerceau à franchir. Ouvrez votre fichier de configuration SSH et ajoutez ce qui suit :

```bash
Host *
  AddKeysToAgent yes
  UseKeychain yes
```

Maintenant, SSH recherchera la clé dans le trousseau et si elle la trouve, vous ne serez pas invité à entrer un mot de passe. La clé sera également ajoutée à `ssh-agent`. Sur MacOS, cela fonctionnera sur MacOS Sierra 10.12.2 ou ultérieur. Sur Linux, vous pouvez utiliser quelque chose comme `gnome-keyring` et cela pourrait fonctionner même sans cette dernière modification de la configuration SSH. Quant à Windows - qui sait, n'est-ce pas ?

J'espère que quelqu'un a trouvé cela utile. Maintenant, allez configurer votre fichier de configuration SSH !

## En savoir plus sur SSH :

* [Le guide ultime des clés SSH](https://www.freecodecamp.org/news/the-ultimate-guide-to-ssh-setting-up-ssh-keys/)
* [Une introduction de haut en bas à SSH](https://www.freecodecamp.org/news/a-top-down-introduction-to-ssh-965f4fadd32e/)