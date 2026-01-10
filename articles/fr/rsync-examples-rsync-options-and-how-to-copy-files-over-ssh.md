---
title: Exemples RSync – Options RSync et comment copier des fichiers via SSH
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-08T20:54:31.000Z'
originalURL: https://freecodecamp.org/news/rsync-examples-rsync-options-and-how-to-copy-files-over-ssh
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/rsync.png
tags:
- name: ssh
  slug: ssh
seo_title: Exemples RSync – Options RSync et comment copier des fichiers via SSH
seo_desc: 'Rsync stands for “remote synchronization”. It is a remote and local file
  synchronization tool that helps you efficiently transfer files.

  What RSync Is

  Rsync is faster than tools like Secure Copy Protocol (SCP). It uses the delta-transfer
  algorithm th...'
---

Rsync signifie « remote synchronization » (synchronisation à distance). C'est un outil de synchronisation de fichiers locaux et distants qui vous aide à transférer des fichiers de manière efficace.

## Qu'est-ce que RSync

Rsync est plus rapide que des outils comme [Secure Copy Protocol (SCP)](https://www.geeksforgeeks.org/scp-command-in-linux-with-examples/). Il utilise l'algorithme [delta-transfer](https://www.dynamsoft.com/help/SAW%20Standalone/Getting%20Started/Delta%20Transfer.htm) qui minimise le transfert de données en ne copiant que les sections d'un fichier qui ont été mises à jour.

Parmi les fonctionnalités supplémentaires de Rsync, on trouve :

* Prise en charge de la copie des liens, des périphériques, des propriétaires, des groupes et des permissions
* Ne nécessite pas de privilèges super-utilisateur
* Pipeline les transferts de fichiers pour [minimiser les coûts de latence](https://whatis.techtarget.com/definition/latency)

Vous ne pouvez transférer des fichiers que de local vers distant ou de distant vers local. Rsync ne prend pas en charge les transferts de fichiers de distant vers distant.

## Comment fonctionne RSync

Maintenant que vous savez ce qu'est Rsync, voyons comment l'utiliser.

Rsync fonctionne de manière similaire à d'autres outils de gestion de serveurs distants comme SSH et SCP.

Voici la syntaxe de base de Rsync :

```
rsync [options] source [destination]
```

Voici la syntaxe pour transférer un fichier de votre système local vers un serveur distant. On parle aussi d'opération « push ».

```
rsync local_file_path user@remote-host:remote_file_path
```

Voici comment transférer un fichier d'un serveur distant vers votre système local, également appelé opération « pull ».

```
rsync user@remote-host:remote_file_path local_file_path
```

> Remarque : Lorsque vous travaillez avec des systèmes distants, assurez-vous d'avoir [un accès SSH au système distant](https://www.hostinger.in/tutorials/ssh-tutorial-how-does-ssh-work?__cf_chl_jschl_tk__=f550a12fdfece557e30dc21901117b432d5a8e1d-1599060891-0-AQrE-UcUtiSpJOvL7PClSP8WK3uhRkd2Va_WJS_Hr7mHzy4lylrjibVz-sFxPrqTOYzEL8kjWnc_WKPSFQq4_CGDfTHPmPF3uv3IBQyDJnHm3v_FHx9-6uH7IG663DhoKDAdMayU1_iN33sQ5fsuniN5ga8w33sjEXqwdW-0-dKQeXXGPN37aTbwu7NlmtFf8MGAvsqbs2NEFChJ2Mpi9qasX6dy0guXG446JenTxsOz_P3g9wzw1qv8hXZtfC7UOdR4s_guli8xDi_EOuzgNoYVRe2r2nRBQ3jNb0fzLwK5frAhmmbv6LClLgrF5r8NRYqxsBPD4FCXp8wvFo7agjs). Rsync établit la connexion en utilisant SSH afin de permettre le transfert de fichiers.

## Comment utiliser les flags dans RSync

Rsync vous permet d'ajouter des options supplémentaires via des flags en ligne de commande. Examinons quelques flags utiles.

### Récursif

Si vous ajoutez l'option **-r**, RSync exécutera un transfert de fichiers récursif. Cela est utile lorsque vous travaillez avec des répertoires. Voici un exemple :

```
rsync -r user@remote-host:remote_directory/ local_directory
```

### Archive

Le flag **-a** est utilisé pour préserver les [liens symboliques](https://www.geeksforgeeks.org/soft-hard-links-unixlinux/) lors du transfert de fichiers. Le flag d'archive préserve également les fichiers spéciaux et périphériques, les heures de modification et les permissions du répertoire source.

Le flag d'archive synchronise également les fichiers de manière récursive, il est donc plus utilisé que le flag récursif. Voici comment l'utiliser :

```
rsync -a user@remote-host:remote_directory/ local_directory
```

### Compression

Vous pouvez également compresser les fichiers en utilisant le flag **-z**. La compression des fichiers peut réduire la charge réseau et accélérer le transfert de fichiers.

```
rsync -az user@remote-host:remote_directory/ local_directory
```

### Progression

Pour les transferts de gros fichiers, il est utile de connaître la progression de l'opération. Vous pouvez utiliser le flag **-P** pour connaître la progression du transfert de fichiers. Avec Rsync, vous pouvez également reprendre les transferts de fichiers s'ils sont interrompus.

```
rsync -aP user@remote-host:remote_directory/ local_directory
```

### Verbose

Enfin, la commande verbose peut vous aider à comprendre chaque étape du transfert de fichiers. Vous pouvez utiliser le flag **-v** pour cela.

```
rsync -av user@remote-host:remote_directory/ local_directory
```

Vous pouvez également utiliser la commande d'aide avec RSync pour obtenir une liste de toutes les options et flags.

```
rsync --help
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-02-at-9.07.47-PM.png)
_rsync help_

## Conclusion

Rsync simplifie l'ensemble du processus de transfert de fichiers en offrant un outil robuste, polyvalent et flexible par rapport à des alternatives comme SCP.

RSync est idéal pour les opérations de maintenance, les sauvegardes et les opérations générales sur les fichiers entre machines locales et distantes.

## Références

* [https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps](https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps)
* [https://linux.die.net/man/1/rsync](https://linux.die.net/man/1/rsync)
* [https://www.geeksforgeeks.org/rsync-command-in-linux-with-examples/](https://www.geeksforgeeks.org/rsync-command-in-linux-with-examples/)

Je suis [Manish](https://www.manishmshiva.com/) et j'écris sur la cybersécurité, l'intelligence artificielle et DevOps. Si vous avez aimé cet article, [vous pouvez trouver mon blog ici](https://medium.com/manishmshiva).