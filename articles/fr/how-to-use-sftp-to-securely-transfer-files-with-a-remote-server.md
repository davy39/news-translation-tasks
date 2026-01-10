---
title: Comment utiliser SFTP pour transférer des fichiers de manière sécurisée avec
  un serveur distant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d1c740569d1a4ca35f2.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: toothbrush
  slug: toothbrush
- name: unix
  slug: unix
seo_title: Comment utiliser SFTP pour transférer des fichiers de manière sécurisée
  avec un serveur distant
seo_desc: 'This article is a quick tutorial on how to use Secure File Transfer Protocol
  (SFTP) to exchange files with a server. This is useful for programming, as it allows
  you to code and test locally, and then send your work to the server when you are
  done.

  T...'
---

Cet article est un tutoriel rapide sur l'utilisation du protocole Secure File Transfer Protocol (SFTP) pour échanger des fichiers avec un serveur. Cela est utile pour la programmation, car il vous permet de coder et de tester localement, puis d'envoyer votre travail sur le serveur une fois terminé.

### **Tester SSH**

Si vous ne l'avez pas déjà fait, testez que vous êtes en mesure de vous connecter en SSH au serveur. SFTP utilise le protocole Secure Shell (SSH), donc si vous ne pouvez pas vous connecter en SSH, vous ne pourrez probablement pas utiliser SFTP non plus.

```unix
ssh votre_nom_dutilisateur@nom_dhote_ou_adresse_ip
```

### **Démarrer une session SFTP**

Cela utilise la même syntaxe que SSH et ouvre une session dans laquelle vous pouvez transférer des fichiers.

```unix
sftp votre_nom_dutilisateur@nom_dhote_ou_adresse_ip
```

Pour lister les commandes utiles :

```unix
help
```

### **Transférer des fichiers et des dossiers**

Pour télécharger un fichier :

```unix
get <nom_du_fichier>
```

Pour télécharger un dossier et son contenu, utilisez le drapeau "-r" (fonctionne également pour le téléversement) :

```unix
get -r <nom_du_dossier>
```

Pour téléverser un fichier :

```unix
put <nom_du_fichier>
```

### **Changer de dossiers**

Pour changer le dossier local :

```unix
lcd <chemin/vers/le/dossier>
```

Pour changer le dossier distant :

```unix
cd <chemin/vers/le/dossier>
```