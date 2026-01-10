---
title: Comment récupérer votre mot de passe root perdu dans CentOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-05T13:47:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-recover-your-lost-root-password-in-centos
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/Untitled-design--1-.png
tags:
- name: Linux
  slug: linux
seo_title: Comment récupérer votre mot de passe root perdu dans CentOS
seo_desc: 'By Thanoshan MV

  In Linux, when you forget your account password, you can easily reset it using a
  root account. But when you forget your root account password, then you''re in a
  bad situation.

  You can’t reset your root account password using a regular ...'
---

Par Thanoshan MV

Dans Linux, lorsque vous oubliez le mot de passe de votre compte, vous pouvez facilement le réinitialiser en utilisant un compte root. Mais lorsque vous oubliez le mot de passe de votre compte root, vous êtes dans une mauvaise situation.

Vous ne pouvez pas réinitialiser le mot de passe de votre compte root en utilisant un compte utilisateur régulier, car un compte utilisateur ne peut généralement pas effectuer de telles tâches.

Dans cet article, nous allons voir comment récupérer le mot de passe root de CentOS. Alors, voyons comment faire.

## Comment récupérer votre mot de passe root - étape par étape

Dans CentOS, il est possible d'avoir des scripts qui s'exécutent à partir de l'initramfs pour déboguer le shell à certains points, fournir un shell root et continuer lorsque ce shell existe.

Bien que cela soit principalement destiné au débogage, cela peut également être utilisé pour récupérer un mot de passe root perdu.

Suivez ces étapes pour récupérer votre mot de passe root perdu.

Tout d'abord, redémarrez le système.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/1.png)

Interrompez le compte à rebours du chargeur de démarrage en appuyant sur n'importe quelle touche.

Déplacez le curseur sur l'entrée qui doit être démarrée.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/2.png)

Appuyez sur "e" pour sélectionner cette entrée. Après avoir sélectionné cette entrée, les commandes du noyau suivantes apparaîtront.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/3.png)

Dans la ligne de commande du noyau, déplacez le curseur sur la ligne qui commence par linux16.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/4.png)

Appuyez sur la touche "Fin" pour déplacer le curseur à la fin de celle-ci. Tapez "rd.break" (Cela interrompra juste avant que le contrôle ne soit transféré de l'initramfs au système réel).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/5.png)

Ensuite, appuyez sur "Ctrl+x" pour enregistrer ces modifications. Le shell de débogage Initramfs apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/6.png)

Ensuite, nous devons fournir des permissions de lecture et d'écriture à /sysroot en tapant la commande suivante :

```
mount -o remount,rw /sysroot/
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/7.png)

Maintenant, basculez dans le chroot jail.

```
chroot /sysroot
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/8.png)

Ici, /sysroot est traité comme la racine de l'arborescence du système de fichiers.

Ensuite, vous définirez un nouveau mot de passe root.

```
passwd root
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/9.png)

Et réétiquetez les fichiers.

```
touch /.autorelabel
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/10.png)

Enfin, tapez "exit" deux fois.

La première fois quittera le chroot jail.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/11.png)

La suivante quittera le shell de débogage initramfs et redémarrera le système.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/12.png)

Maintenant, vous pouvez vous connecter en tant que root avec votre mot de passe mis à jour.

N'hésitez pas à me faire savoir si vous avez des questions. Vous pouvez me contacter et me rejoindre sur [Twitter](https://twitter.com/ThanoshanMV).

Merci pour votre lecture.

**Bon codage !**