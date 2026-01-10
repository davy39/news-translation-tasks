---
title: 'Chroot : les pouvoirs magiques de guérison de l''outil de virtualisation Linux
  original'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-26T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/chroot-magical-linux-virtualization-tool
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/permission.jpg
tags:
- name: Linux
  slug: linux
- name: virtualization
  slug: virtualization
seo_title: 'Chroot : les pouvoirs magiques de guérison de l''outil de virtualisation
  Linux original'
seo_desc: You know that the passwords chosen by the people you support are probably
  not strong enough to protect your infrastructure against a serious attack. And even
  the few exceptions to the rule are probably being reused on multiple servers and
  accounts. Y...
---

Vous savez que les mots de passe choisis par les personnes que vous assistez ne sont probablement pas assez robustes pour protéger votre infrastructure contre une attaque sérieuse. Et même les rares exceptions à la règle sont probablement réutilisées sur plusieurs serveurs et comptes. Vous suppliez et harcelez, mais c'est une bataille perdue.

Mais tout n'est pas entièrement perdu. Le problème de la gestion de mots de passe suffisamment complexes peut être largement résolu en utilisant un bon coffre-fort de mots de passe comme KeePass2 ou LastPass. Et le problème de la surutilisation des mots de passe peut être au moins atténué en mettant en place une solution d'authentification unique comme Kerberos. D'accord. Pas _comme_ Kerberos, mais _Kerberos_.

Pourtant, des erreurs stupides vont toujours se produire.

Alors, que va-t-il arriver aux un ou deux utilisateurs qui se soucient assez pour inventer de bons mots de passe forts pour chaque serveur auquel ils accèdent ? De temps en temps, ils oublieront un mot de passe, bien sûr. Cela ne posera pas de problème s'il y a un autre administrateur avec des droits sudo qui peut se connecter au serveur et exécuter passwd pour créer un nouveau mot de passe pour l'utilisateur.

```
sudo  passwd username
[sudo] password for yourname:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
```

Mais si votre utilisateur malchanceux et oublieux était le seul administrateur avec un compte sur cette machine, vous avez un problème. Sauf que non. _chroot_ — le grand-père de toute la virtualisation Linux — va sauver votre journée.

Voici, comme je l'ai écrit dans [les chapitres 6 et 9 de mon livre Linux in Action](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1), une façon dont cela pourrait fonctionner. Utilisez un lecteur live-boot pour démarrer le serveur qui vous a verrouillé.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-155.png)
_Étapes pour créer une clé USB live boot Linux_

Ensuite, ouvrez un terminal et exécutez lsblk pour déterminer la désignation de votre partition racine sur le disque dur du serveur, et montez la partition racine dans un répertoire temporaire.

```
mkdir /run/mountdir/
mount /dev/sdb1 /run/mountdir/
```

Ensuite, vous murmurez les mots magiques et vous êtes dedans :

```
chroot /run/mountdir/
root@ubuntu:/#
```

C'est tout ce qu'il faut. À ce stade, vous êtes libre d'exécuter des commandes comme si vous travailliez sur une version en cours d'exécution du disque dur physique. Utilisez passwd pour donner à votre administrateur un nouveau mot de passe pour remplacer celui perdu et, après avoir tapé exit pour fermer votre session chroot, redémarrez la machine (sans le live-boot USB). Tout devrait maintenant être en ordre.

> _Chiffrer ou ne pas chiffrer_

> _Chiffrer les données sur vos disques de stockage à l'aide d'outils comme ecryptfs ou dm-crypt réduit considérablement les risques que vos données soient compromises. Mais d'un autre côté, de nombreuses opérations de secours et de récupération comme l'astuce chroot ci-dessus ne fonctionneront tout simplement pas sur un volume chiffré._

> _Trouver un équilibre entre sécurité et accessibilité n'est pas une science exacte. De nombreux administrateurs, par exemple, laisseront les serveurs locaux et les stations de travail de bureau non chiffrés — parce qu'ils sont au moins protégés par des portes de bureau verrouillées — mais insisteront pour que les appareils mobiles soient chiffrés._

## Récupérer une VM verrouillée

Vous pouvez appliquer la magie de chroot pour nettoyer toutes sortes de désordres. Verrouillé hors d'un serveur local (ou d'un conteneur LXC) ? N'hésitez pas à ouvrir un shell chroot pour désactiver ou même reconfigurer votre pare-feu.

Faire cela sur une machine physique devrait être simple maintenant. Mais voici comment cela fonctionnerait sur un conteneur LXC.

Tout d'abord, arrêtez le conteneur puis exécutez chroot contre le répertoire rootfs qui se trouve dans la hiérarchie de répertoires utilisée par votre conteneur LXC (var/lib/lxc/nom-de-votre-conteneur/). L'invite de commande que vous obtiendrez vous permettra d'exécuter des commandes comme si le conteneur était réellement en cours d'exécution. Désactivez maintenant ufw ou, si vous préférez, exécutez les commandes nécessaires pour résoudre le problème, puis quittez le shell chroot. Lorsque vous redémarrez le conteneur, vous devriez maintenant avoir un accès SSH.

```
lxc-stop -n nom-de-votre-conteneur
chroot /var/lib/lxc/nom-de-votre-conteneur/rootfs/
ufw disable
exit
lxc-start -d -n nom-de-votre-conteneur
```

_Cet article est extrait de mon livre_ [_Manning « Linux in Action »_](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9)_. Il y a beaucoup plus de divertissement_ [_d'où cela vient_](https://bootstrap-it.com/index.php/books/)_, y compris un cours hybride appelé_ [_Linux in Motion_](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1)_qui est composé de plus de deux heures de vidéo et d'environ 40 % du texte de Linux in Action. Qui sait... vous pourriez aussi apprécier mon récent_ [_Learn Amazon Web Services in a Month of Lunches_](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27)_.