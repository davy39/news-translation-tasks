---
title: Aperçu et historique de systemd — le gestionnaire de processus Linux
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-24T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/a-brief-overview-and-history-of-systemd-the-linux-process-manager
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca13f740569d1a4ca4d86.jpg
tags:
- name: history
  slug: history
- name: Linux
  slug: linux
seo_title: Aperçu et historique de systemd — le gestionnaire de processus Linux
seo_desc: Intelligently running Linux services includes knowing how to test for their
  status which, in turn, requires understanding how modern Linux distributions manage
  processes. This article  will briefly explore the function and history of systemd — the
  pr...
---

Exécuter intelligemment les services Linux inclut savoir comment tester leur statut, ce qui nécessite de comprendre comment les distributions Linux modernes gèrent les processus. Cet article explorera brièvement la fonction et l'histoire de systemd — le gestionnaire de processus qui semble être aimé, craint et détesté en parts égales.

Quelque chose sur votre machine Linux ne fonctionne pas ? Le dépannage est votre ami. Mais avant d'en arriver là, ne devriez-vous pas vous assurer que le service sous-jacent est réellement en cours d'exécution ? Parfois, les fichiers de configuration sont par défaut définis sur inactif.

Vous pouvez utiliser _systemctl status_ pour savoir si un service — OpenSSH dans cet exemple — est en cours d'exécution sur votre machine :

$ systemctl status ssh  
● ssh.service - OpenBSD Secure Shell server  
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)  
   Active: active (running) since Mon 2017-05-15 12:37:18 UTC; 4h 47min ago    
 Main PID: 280 (sshd)   
    Tasks: 8  
   Memory: 10.1M  
      CPU: 1.322s  
   CGroup: /system.slice/ssh.service  
           └─ 280 /usr/sbin/sshd -D  
           └─ 894 sshd: ubuntu [priv]   
           └─ 903 sshd: ubuntu@pts/4    
           └─ 904 -bash  
           └─1612 bash  
           └─1628 sudo systemctl status ssh  
           └─1629 systemctl status ssh  
[...]

Dans ce cas, comme vous pouvez le voir à la ligne Active de la sortie, tout est correct. Si vous deviez le démarrer vous-même, vous utiliseriez à nouveau systemctl, mais cette fois avec _start_ à la place de _status_. Ennuyé avec votre nouveau jouet ? `systemctl stop` le mettra de côté pour vous.

`# systemctl stop ssh`

Ce systemctl semble assez sympathique, mais nous n'avons guère eu l'occasion de le rencontrer. Creusons un peu plus.

## Gestion des processus Linux

Tout d'abord, qu'est-ce que systemctl et que fait-il réellement ? Pour répondre correctement à cette question, vous devrez réfléchir un peu à la manière dont Linux gère les processus système en général. Et comme il est toujours agréable de rencontrer de nouveaux amis, vous apprendrez également quelques outils de suivi des processus pour faciliter la compréhension du fonctionnement des choses.

Le logiciel, comme je suis sûr que vous le savez déjà, est du code de programmation contenant des instructions pour contrôler le matériel informatique au nom des utilisateurs humains. Un système d'exploitation est un outil pour organiser et gérer les packages logiciels afin qu'ils puissent exploiter efficacement les ressources matérielles d'un ordinateur. Organiser et gérer les processus pour un environnement d'exploitation multi-processus et multi-utilisateurs complexe n'est pas une tâche simple. Pour que cela fonctionne, vous aurez besoin d'une sorte d'agent de circulation pour contrôler étroitement les nombreuses pièces mobiles. Permettez-moi de vous présenter systemctl, un officier travailleur de la division de la circulation du département de police Linux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OD9MOvg4XlBFYezYqwUSMA.png)
_La disponibilité et la réactivité de nombreux services système sont gérées par le gestionnaire de processus systemctl de systemd_

## Visualisation des processus avec la commande ps

Sortons un microscope électronique et voyons si nous ne pouvons pas repérer un processus réel dans son habitat naturel. Le tout premier processus à se réveiller et à lancer tout le reste lorsqu'un ordinateur Linux démarre s'appelle init (bien que, comme nous le découvrirons bientôt, ce nom peut être trompeur). Vous pouvez voir par vous-même qu'init est le premier en exécutant la commande ps suivante exactement comme elle est imprimée ici — je vais expliquer les détails dans une minute.

$ ps -ef | grep init   
root         1     0  0 12:36 ?        00:00:00 /sbin/init   
ubuntu    1406   904  0 16:26 pts/4    00:00:00 grep --color=auto init

La colonne la plus à droite de la sortie (/sbin/init sur la première ligne) représente l'emplacement et le nom du fichier derrière le processus lui-même. Dans ce cas, il s'agit d'un fichier appelé « init » qui réside dans le répertoire /sbin. La colonne la plus à gauche de cette première ligne contient le mot _root_ et nous indique que le propriétaire de ce processus est l'utilisateur root. La seule autre information qui nous intéresse pour l'instant est le nombre 1, qui est l'identifiant de processus (PID) du processus init. La seule façon d'obtenir le PID 1 est d'y arriver avant tout le monde.

Au fait, la deuxième ligne affichée par cette commande ps est le processus attribué à la commande grep elle-même. Notez comment son propriétaire est ubuntu (mon nom d'utilisateur) et son PID est beaucoup plus élevé que 1.

Avant de continuer, il vaut la peine de passer un peu plus de temps avec ps. Comme vous l'avez vu, ps affiche des informations sur les processus actifs. Il est souvent important d'avoir accès aux informations liées aux processus afin que nous puissions planifier et dépanner correctement le comportement du système. Vous pouvez vous attendre à utiliser ps tôt et souvent.

Si vous tapiez simplement ps et l'exécutiez, vous obtiendriez probablement seulement deux résultats : le premier, un processus appelé bash qui représente l'interpréteur de commandes Bash utilisé par votre session shell actuelle, et la commande la plus récente (qui, bien sûr, était ps). Mais en regardant le PID attribué à Bash (7447, dans cet exemple), vous savez qu'il y a beaucoup, beaucoup d'autres processus déjà au travail quelque part sur votre système. Ceux-ci auront été engendrés par des shells parents remontant jusqu'au processus init lui-même.

$ ps  
 PID TTY          TIME CMD  
7447 pts/3    00:00:00 bash  
8041 pts/3    00:00:00 ps

L'ajout de l'argument -e à ps comme nous l'avons fait ci-dessus retournera non seulement les processus en cours d'exécution dans votre shell enfant actuel, mais tous les processus de tous les shells parents jusqu'à init.

Un shell parent est un environnement shell à partir duquel de nouveaux shells (enfants) peuvent être lancés ultérieurement et à travers lequel des programmes sont exécutés. Vous pouvez considérer votre session de bureau GUI comme un shell, et le terminal que vous ouvrez pour obtenir une ligne de commande comme son enfant. Le shell de niveau supérieur (le grand-parent ?) est celui qui est exécuté en premier lorsque Linux démarre.

Si vous voulez visualiser les shells/processus parents et enfants, vous pouvez utiliser la commande `pstree` (en ajoutant l'argument -p pour afficher les numéros PID de chaque processus). Notez comment le tout premier processus (auquel est attribué le PID 1) est _systemd_. Sur les anciennes versions de Linux, cela aurait été appelé _init_ à la place.

$ pstree -p  
systemd(1)├─agetty(264)   
           ├─agetty(266)  
           ├─agetty(267)  
           ├─agetty(268)  
           ├─agetty(269)  
           ├─apache2(320)├─apache2(351)  
           │              ├─apache2(352)  
           │              ├─apache2(353)  
           │              ├─apache2(354)  
           │              └─apache2(355)  
           ├─cron(118)  
           ├─dbus-daemon(109)  
           ├─dhclient(204)  
           ├─dockerd(236)├─docker-containe(390)├─{docker-containe}(392)  
           │              │                      └─{docker-containe}(404)  
           │              ├─{dockerd}(306)  
           │              └─{dockerd}(409)  
           ├─mysqld(280)├─{mysqld}(325)  
           │             ├─{mysqld}(326)  
           │             └─{mysqld}(399)  
           ├─nmbd(294)  
           ├─rsyslogd(116)├─{in:imklog}(166)  
           │               ├─{in:imuxsock}(165)  
           │               └─{rs:main Q:Reg}(167)  
           ├─smbd(174)├─smbd(203)  
           │           └─smbd(313)  
           ├─sshd(239)───sshd(840)───sshd(849)───bash(850)───pstree(15328)  
           ├─systemd-journal(42)  
           └─systemd-logind(108)

Allez-y et essayez toutes ces commandes sur votre propre machine. Même sur un système calme, vous verrez probablement des dizaines de processus ; un PC de bureau ou un serveur occupé peut facilement en avoir des milliers.

## Travailler avec systemd

Il y a quelque chose d'intéressant concernant ce fichier /sbin/init que nous venons de voir. « file » est un programme Unix vénérable qui vous donne des informations internes sur un fichier. Si vous exécutez _file_ avec /sbin/init comme argument, vous verrez que le fichier init n'est pas réellement un programme, mais simplement un lien symbolique vers un programme appelé systemd.

$ file /sbin/init  
/sbin/init: symbolic link to /lib/systemd/systemd

Après de nombreuses années de fragmentation et quelques luttes politiques vigoureuses, presque toutes les distributions Linux utilisent désormais le même gestionnaire de processus : systemd. systemd est un remplacement direct pour le processus init. Par « remplacement direct », je veux dire que, même si la manière dont il accomplit les choses peut être assez différente, pour l'observateur occasionnel, systemd fonctionne exactement comme init l'a toujours fait. C'est pourquoi le fichier /sbin/init n'est désormais rien de plus qu'un lien vers le programme systemd.

Cela est un peu théorique puisque vous n'invoquerez probablement jamais le programme systemd lui-même par son nom — soit directement, soit par l'intermédiaire de son interface /sbin/init. Cela est dû au fait que, comme vous l'avez déjà vu, les tâches clés d'administration sont gérées par systemctl au nom de systemd.

Techniquement, le travail principal de systemd est de contrôler les façons dont les processus individuels naissent, vivent leur vie, puis meurent. La commande systemctl que nous avons utilisée ci-dessus est l'outil de choix pour ces tâches. Mais — de manière quelque peu controversée — les développeurs de systemd ont étendu la fonctionnalité bien au-delà du rôle traditionnel de gestion des processus pour prendre le contrôle de divers services système. Inclus sous le nouvel umbrella systemd se trouvent des outils comme un gestionnaire de journalisation (journald), un gestionnaire de réseau (networkd) et un gestionnaire de périphériques (vous l'avez deviné : udevd). Curieux ? Le « d » signifie démon ; un processus système en arrière-plan.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ufSpWkBfRakYB-Ex.jpg)

_Cet article est adapté du chapitre 3 (Connectivité à distance : accéder en toute sécurité aux machines en réseau) de mon livre_ [_Manning « Linux in Action »_](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9)_. Il y a beaucoup plus de plaisir d'où cela vient — y compris des_ [_cours d'administration Linux et Docker sur Pluralsight_](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) _et un cours hybride appelé_ [_Linux in Motion_](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) _qui est composé de plus de deux heures de vidéo et d'environ 40 % du texte de Linux in Action. Qui sait... vous pourriez également apprécier [mes autres livres et cours.](https://bootstrap-it.com)_