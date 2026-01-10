---
title: 'Le menu de récupération d''Ubuntu : démystifier la récupération du système
  Linux'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-30T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-ubuntu-recovery-menu-demystifying-linux-system-recovery
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/ubuntu-recovery.png
tags:
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
seo_title: 'Le menu de récupération d''Ubuntu : démystifier la récupération du système
  Linux'
seo_desc: 'Don’t try to convince yourself otherwise: along with all the good stuff,
  you’re going to have bad days with Linux.


  You (or the users you support) are going to mistype commands and permanently destroy
  documents.

  You’re going to experience that sinkin...'
---

Ne cherchez pas à vous convaincre du contraire : avec tout le bon côté, vous allez avoir des mauvais jours avec Linux.

* Vous (ou les utilisateurs que vous supportez) allez mal taper des commandes et détruire définitivement des documents.
* Vous allez ressentir cette sensation de découragement lorsque vous réaliserez qu'un élément matériel ou logiciel vraiment important vient de tomber en panne. C'est la gratitude après tout ce que vous avez fait pour lui pendant toutes ces années.

Avoir une sauvegarde appropriée signifie que vous pouvez abandonner un système d'exploitation ou un ordinateur non fonctionnel et tout reconstruire ailleurs. Mais ce sera toujours le Plan B. Le Plan A est de récupérer.

## Utilisation du mode de récupération sur Ubuntu

Linux ne vous permet pas de vous connecter normalement (peut-être que le processus de démarrage s'arrête de manière inattendue avant d'afficher l'écran de connexion, par exemple) ? Vous aurez besoin de quelques outils d'administration système de base.

Mais attendez : si Linux ne se charge pas, comment allez-vous lancer ces outils ? Eh bien, même si Linux ne se charge pas complètement jusqu'à une invite de commande normale, souvent il vous amènera au menu GRUB. À partir de là, vous pouvez utiliser les touches fléchées haut et bas puis Entrée pour sélectionner un noyau Linux fonctionnant en mode de récupération qui, comme vous le verrez bientôt, ouvrira une toute boîte à outils.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-54.png)
_Le menu « Options avancées » de GRUB d'une installation Ubuntu avec des liens vers les versions actuelles et plus anciennes du noyau ainsi que des options pour le lancement en mode de récupération_

Comme vous pouvez le voir sur la figure ci-dessous, une fois Ubuntu chargé en mode de récupération, un menu d'outils s'affichera pour résoudre certains problèmes courants au démarrage. Il vaut la peine d'essayer chacun de ceux qui semblent pouvoir résoudre votre problème racine. « Clean », par exemple, supprimera les fichiers inutilisés si vous suspectez que le problème vient d'un disque plein. « dpkg » tentera de réparer tout paquet logiciel basé sur apt qui pourrait causer des problèmes. (L'outil « dpkg » peut nécessiter que vous activiez d'abord le réseau.)

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-55.png)
_Le menu de récupération d'Ubuntu avec des liens vers quelques outils de diagnostic et de réparation de base, ainsi que l'option d'ouvrir une session shell en tant que « root »_

L'option « root » ouvrira une session shell de ligne de commande root pour vous où vous aurez Bash à votre disposition. En général, utiliser une simple session shell pour la récupération plutôt qu'un bureau GUI complet a beaucoup de sens, car moins vous avez de services compliqués en cours d'exécution, plus il est probable que vous puissiez au moins faire fonctionner votre système. Une fois que vous réussissez à obtenir une invite de commande fonctionnelle, vous pouvez commencer à explorer pour voir si vous pouvez identifier et résoudre le problème.

Mais dans le pire des cas, vous aurez l'air très cool en le faisant.

Mais quels sont ces outils ? Vous avez une machine Ubuntu en fonctionnement ? Allez jeter un coup d'œil par vous-même. Le code exécutant le menu doit déjà exister quelque part dans un système de fichiers Ubuntu. Utilisez « locate » pour le trouver.

```
locate recovery-mode
/lib/recovery-mode
/lib/recovery-mode/l10n.sh
/lib/recovery-mode/options
/lib/recovery-mode/recovery-menu
/lib/recovery-mode/options/apt-snapshots
/lib/recovery-mode/options/clean
/lib/recovery-mode/options/dpkg
/lib/recovery-mode/options/failsafeX
/lib/recovery-mode/options/fsck
/lib/recovery-mode/options/grub
/lib/recovery-mode/options/network
/lib/recovery-mode/options/root
/lib/recovery-mode/options/system-summary
```

Notez que le script « l10n.sh » définit les variables d'environnement appropriées pour le menu. Si vous naviguez vers le répertoire /lib/recovery-mode/, vous verrez que le fichier « recovery-menu » est le script qui affiche l'interface de menu que vous avez vue ci-dessus. Le répertoire /lib/recovery-mode/options/ contient des fichiers pour exécuter chacun des éléments du menu... comme « fsck » qui vérifiera et, si possible, réparera tout système de fichiers endommagé.

Puisque, sur la base des chapitres précédents du livre, vous êtes maintenant un expert en script Bash accompli, pourquoi ne pas jeter un coup d'œil à chacun des scripts dans le répertoire options/ pour voir si vous pouvez comprendre comment ils fonctionnent. Voici le contenu du script « fsck » pour vous lancer. Notez la façon dont le script est bien documenté (en utilisant le caractère « # ») pour vous aider à comprendre ce qui se passe.

```
cat /lib/recovery-mode/options/fsck
#!/bin/sh
. /lib/recovery-mode/l10n.sh  <1>
if [ "$1" = "test" ]; then
  echo $(eval_gettext "Check all file systems")
  exit 0
fi
# Actual code is in recovery-menu itself  <2>
exit 0
```

Voici quelques choses que vous pouvez essayer par vous-même :

* Exécutez manuellement le script « clean » sur une machine Debian/Ubuntu. Qu'est-il arrivé ?
* Ensuite, essayez d'éditer _soigneusement_ le script /lib/recovery-mode/recovery-menu (faites une copie de sauvegarde d'abord). Peut-être changez simplement quelque chose de simple, comme le titre du menu ou l'une des descriptions des scripts. Ensuite, redémarrez votre machine et, à partir du menu GRUB, allez dans le mode de récupération pour voir à quoi il ressemble.

Avec quelques variations et exceptions, vous devriez pouvoir mettre ces exemples à bonne utilisation ailleurs.

_Cet article est adapté du chapitre 6 (Outils d'urgence : construire un dispositif de récupération du système) de mon livre Manning « Linux in Action »_. Il y a beaucoup plus de divertissement là d'où cela vient, y compris un cours hybride appelé Linux in Motion qui est composé de plus de deux heures de vidéo et d'environ 40 % du texte de [Linux in Action](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1). Qui sait... vous pourriez aussi apprécier mon [Learn Amazon Web Services in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27).