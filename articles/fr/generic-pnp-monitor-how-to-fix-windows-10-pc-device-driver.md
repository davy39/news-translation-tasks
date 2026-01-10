---
title: Moniteur PnP générique – Comment réparer le pilote de périphérique sur PC Windows
  10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-09-21T16:18:08.000Z'
originalURL: https://freecodecamp.org/news/generic-pnp-monitor-how-to-fix-windows-10-pc-device-driver
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/monitor-1307227_1280.jpg
tags:
- name: Windows 10
  slug: windows-10
seo_title: Moniteur PnP générique – Comment réparer le pilote de périphérique sur
  PC Windows 10
seo_desc: "Have you acquired a new monitor only to find out it's not displaying anything\
  \ from your computer? Or maybe the monitor suddenly stops working? \nOn many occasions,\
  \ this problem is caused by a faulty generic PNP monitor driver.\nApart from driver\
  \ issues..."
---

Avez-vous fait l'acquisition d'un nouveau moniteur pour constater qu'il n'affiche rien depuis votre ordinateur ? Ou peut-être que le moniteur s'arrête soudainement de fonctionner ? 

Dans de nombreux cas, ce problème est causé par un pilote de moniteur PnP générique défectueux.

En dehors des problèmes de pilote, le moniteur peut ne pas fonctionner en raison d'une mauvaise connexion liée aux câbles. Cela peut également arriver si le moniteur est défectueux.

En réponse à cette erreur, la plupart des moniteurs affichent "Pas de signal" ou "Vérifier le câble de connexion". Cela vous donne un indice sur la première chose à faire – vérifier les câbles de connexion.

## Comment résoudre les problèmes de moniteur PnP générique sur Windows 10

### Assurez-vous que tous les câbles sont correctement connectés

Tout d'abord, assurez-vous que tous les câbles sont correctement connectés. Si vous utilisez un câble VGA, HDMI ou DisplayPort, regardez les ports de connexion des câbles sur le moniteur et l'ordinateur et assurez-vous qu'ils ne sont pas desserrés.

Si vous êtes certain que les câbles sont connectés de la bonne manière et que le moniteur n'affiche toujours rien, vous devrez peut-être changer de câble. 

Si vous utilisiez le HDMI au début, passez au VGA ou au DisplayPort. Et si vous utilisiez un DisplayPort mais que le moniteur n'affiche toujours rien, passez au VGA ou au HDMI.

### Comment réparer le moniteur PnP générique en mettant à jour les pilotes

Si votre moniteur ne fonctionne pas, vous devriez mettre à jour les pilotes de votre carte graphique (Display Adapter) et les pilotes du moniteur.

#### Comment mettre à jour le pilote de la carte graphique

Pour mettre à jour le pilote de la carte graphique, rendez-vous dans le Gestionnaire de périphériques en faisant un clic droit sur Démarrer et en sélectionnant Gestionnaire de périphériques.

![devicemanager](https://www.freecodecamp.org/news/content/images/2022/09/devicemanager.jpg)

Développez Cartes graphiques, faites un clic droit sur le périphérique que vous voyez (généralement "Intel(R) HD Graphics…"), et sélectionnez "Mettre à jour le pilote".

![ss1-4](https://www.freecodecamp.org/news/content/images/2022/09/ss1-4.png) 

Sélectionnez "Rechercher automatiquement les pilotes" afin que votre ordinateur puisse vérifier sur Internet la version la plus récente du pilote.

![ss2-4](https://www.freecodecamp.org/news/content/images/2022/09/ss2-4.png) 

Si le pilote n'est vraiment pas à jour, votre ordinateur téléchargera une version mise à jour du pilote et vous invitera à l'installer.

#### Comment mettre à jour le pilote du moniteur PnP générique

Retournez dans le Gestionnaire de périphériques et développez Moniteurs. Faites un clic droit sur "Moniteur PnP générique" et sélectionnez Mettre à jour le pilote.

PnP signifie Plug and Play. C'est le pilote que votre ordinateur installe pour un moniteur qu'il ne reconnaît pas.

![ss3-4](https://www.freecodecamp.org/news/content/images/2022/09/ss3-4.png) 

Sélectionnez "Rechercher automatiquement les pilotes".

![ss2-4](https://www.freecodecamp.org/news/content/images/2022/09/ss2-4.png)

Votre ordinateur vous invitera à installer le pilote mis à jour une fois qu'il sera téléchargé.

Si vous mettez à jour les pilotes nécessaires et que le moniteur ne fonctionne toujours pas, il s'agit alors d'un problème avec vos connexions de câbles. Cette fois, vous devrez peut-être vous procurer un adaptateur externe ou un convertisseur externe.

### Utilisez un adaptateur ou un convertisseur externe avec vos câbles de connexion 

Si vous essayez tous les câbles possibles et que le moniteur n'affiche toujours rien, cela peut signifier que votre moniteur ne fonctionnera pas à moins que vous ne connectiez un **adaptateur d'affichage** à la partie du câble reliée à votre ordinateur portable ou à votre unité centrale.

Dans ce cas, il existe plusieurs adaptateurs que vous pouvez utiliser :

- VGA vers HDMI
- USB vers HDMI
- VGA vers DisplayPort

Vous pouvez vous procurer ces adaptateurs dans n'importe quel magasin d'informatique de votre région ou en ligne.

Dans la plupart des cas, le passage de VGA vers HDMI ou de VGA vers DisplayPort fonctionne. Lorsque j'ai eu le même problème, c'est l'adaptateur VGA vers HDMI qui a fonctionné pour moi. 

![ss5-4](https://www.freecodecamp.org/news/content/images/2022/09/ss5-4.png)


## Conclusion
J'espère que cet article vous aidera à résoudre tout problème que vous rencontrez avec votre moniteur. 

Gardez à l'esprit qu'une fois que vous avez mis à jour les pilotes nécessaires (pilote du moniteur et pilote de la carte graphique) et que le moniteur ne s'affiche toujours pas, il s'agit probablement d'un problème avec vos câbles de connexion.

Merci de votre lecture.