---
title: Le guide ultime de Linux - Créer un utilisateur Sudo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-18T17:05:00.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-linux-creating-a-sudo-user
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9fe6740569d1a4ca4564.jpg
tags:
- name: Linux
  slug: linux
seo_title: Le guide ultime de Linux - Créer un utilisateur Sudo
seo_desc: sudo stands for either "superuser do" or "switch user do", and sudo users
  can execute commands with root/administrative permissions, even malicious ones.
  Be careful who you grant sudo permissions to – you are quite literally handing them
  the key your...
---

`sudo` signifie soit "superutilisateur do" ou "switch user do", et les utilisateurs `sudo` peuvent exécuter des commandes avec des permissions root/administratives, même malveillantes. Soyez prudent quant à qui vous accordez les permissions `sudo` – vous leur donnez littéralement la clé de votre maison.

Avant de créer un nouvel utilisateur `sudo`, vous devez d'abord créer un nouvel utilisateur.

## Comment créer un nouvel utilisateur

### Utilisez `adduser` ou `useradd` pour ajouter un nouvel utilisateur

```text
sudo adduser username
```

Assurez-vous de remplacer `username` par le nom de l'utilisateur que vous souhaitez créer. Notez également que pour créer un nouvel utilisateur, vous devez également être un utilisateur `sudo` vous-même.

### Utilisez `passwd` pour mettre à jour le mot de passe du nouvel utilisateur

```text
sudo passwd username
```

Un mot de passe fort est fortement recommandé !

## Accorder des permissions Sudo au nouvel utilisateur

Après avoir créé un nouvel utilisateur, ajoutez-le au groupe approprié en utilisant la commande `usermod`.

### Sur les systèmes Debian (Ubuntu / Linux Mint / ElementryOS), ajoutez les utilisateurs au groupe `sudo`

```text
sudo usermod -aG sudo username
```

### Sur les systèmes basés sur RHEL (Fedora / CentOS), ajoutez les utilisateurs au groupe `wheel`

```text
sudo usermod -aG wheel username
```

## Comment supprimer un utilisateur

Pour supprimer un utilisateur, utilisez les commandes suivantes.

### Systèmes basés sur Debian (Ubuntu / Linux Mint / ElementryOS)

```text
sudo deluser username
```

### Systèmes basés sur RHEL (Fedora / CentOS)

```text
sudo userdel username
```

C'est tout ce que vous devez savoir sur la création d'un nouvel utilisateur `sudo` dans Linux. Et rappelez-vous, "Un grand pouvoir implique de grandes responsabilités."