---
title: Que faire lorsque l'authentification basée sur les clés ne fonctionne pas après
  ssh-copy-id
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-06T16:54:49.000Z'
originalURL: https://freecodecamp.org/news/key-based-authentication-not-working-after-ssh-copy-id-abef7f401d23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*azA9xUZXf6WuDEcVBZ5W-g.png
tags:
- name: authentication
  slug: authentication
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Ubuntu
  slug: ubuntu
- name: Web Development
  slug: web-development
seo_title: Que faire lorsque l'authentification basée sur les clés ne fonctionne pas
  après ssh-copy-id
seo_desc: 'By Arit Amana

  I recently provisioned a Ubuntu virtual private server (VPS) on Vultr. I’m partial
  to CentOS myself, but the task I was working on recommended Ubuntu.

  To set up key-based authentication from my laptop to the server,


  I generated a new S...'
---

Par Arit Amana

J'ai récemment provisionné un serveur privé virtuel (VPS) Ubuntu sur Vultr. Je préfère personnellement CentOS, mais la tâche sur laquelle je travaillais recommandait Ubuntu.

Pour configurer l'authentification basée sur les clés depuis mon ordinateur portable vers le serveur,

* J'ai généré une nouvelle paire de clés SSH (nommée « ubuntu ») sur mon Mac en utilisant la commande : `ssh-keygen -t rsa -b 4096`
* J'ai ensuite utilisé l'utilitaire `ssh-copy-id` pour copier ma clé publique dans le fichier `authorized_keys` sur mon VPS Vultr : `ssh-copy-id -i .ssh/ubuntu aritdev@123.456.789.000`

Comme je m'y attendais, l'utilitaire a demandé le mot de passe de mon VPS pour compléter le transfert de la clé publique. Une fois tout cela terminé, j'ai tenté de me connecter à mon VPS.

Il aurait dû me laisser passer sans demander de mot de passe :

`ssh -i .ssh/ubuntu aritdev@123.456.789.000`

Mais je continuais à être invité à saisir un mot de passe. ?

* J'ai vérifié mon fichier `authorized_keys` sur le VPS pour m'assurer que ma clé publique avait été correctement copiée. Vérifié. ??
* Je me suis assuré que le fichier était en lecture-écriture uniquement pour moi et pour personne d'autre. Vérifié. ??
* Je me suis assuré que les options suivantes étaient activées dans `/etc/ssh/sshd_config` : `PubkeyAuthentication yes` et `AuthorizedKeysFile .ssh/authorized_keys`. Vérifié. ??

Pourtant, je continuais à être invité à saisir un mot de passe lors de la connexion depuis mon ordinateur portable.

Après quelques minutes sur StackOverflow, j'ai appris l'existence des répertoires personnels chiffrés, qui sont activés par défaut dans certains environnements, y compris Ubuntu.

Les répertoires personnels chiffrés ne sont pas déchiffrés tant que la première connexion n'est pas réussie. Cependant, mon fichier `authorized_keys` est stocké dans mon répertoire personnel.

Par conséquent, ma première tentative de connexion nécessitera un mot de passe. Les connexions suivantes réussiront sans mot de passe, car le service SSH pourra alors lire mon fichier `authorized_keys` dans mon répertoire personnel déchiffré.

Pour contourner cela, j'ai créé un répertoire portant le nom de mon utilisateur `aritdev` en dehors de mon répertoire personnel (j'ai choisi `/etc/`), et je lui ai donné des permissions complètes pour moi, mais des permissions de lecture-exécution pour tout le monde. Ensuite, j'ai déplacé mon fichier `authorized_keys` dans `/etc/aritdev/`. Puis, j'ai mis à jour le paramètre `AuthorizedKeysFile` dans `/etc/ssh/sshd_config` :

`AuthorizedKeysFile /etc/%u/authorized_keys`

Enfin, j'ai redémarré le service SSH. Pour tester, je me suis déconnecté de mon VPS, puis j'ai tenté de me reconnecter. BOOM - ça a marché ! ??

Quels problèmes liés à l'authentification serveur avez-vous rencontrés ? Comment les avez-vous résolus ? Partagez vos expériences ci-dessous ! ??