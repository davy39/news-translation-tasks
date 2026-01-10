---
title: Comment monter automatiquement une partition de stockage au démarrage sous
  Linux
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-01-04T16:09:16.000Z'
originalURL: https://freecodecamp.org/news/automount-a-storage-partition-on-startup-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/LinuxAutomount.jpg
tags:
- name: automation
  slug: automation
- name: Linux
  slug: linux
seo_title: Comment monter automatiquement une partition de stockage au démarrage sous
  Linux
seo_desc: "By default, Linux OS does not automount any other partition at startup\
  \ other than the root and the home partition. \nYou can mount other partitions very\
  \ easily later, but you might want to enable some kind of automount feature on startup.\
  \ This means t..."
---

Par défaut, le système d'exploitation Linux ne monte automatiquement aucune autre partition au démarrage que la partition racine et la partition home. 

Vous pouvez monter d'autres partitions très facilement plus tard, mais vous pourriez vouloir activer une sorte de fonctionnalité de montage automatique au démarrage. Cela signifie que vous n'aurez pas besoin de les monter plus tard une par une ou toutes à la fois après vous être connecté à votre système d'exploitation Linux. 

Personnellement, j'aime activer la fonctionnalité de montage automatique au démarrage pour certaines de mes partitions que j'utilise beaucoup lorsque je travaille sur mon ordinateur de bureau. 

Comme j'ai besoin d'accéder à ces partitions tout le temps, je n'aime pas la corvée de les monter individuellement chaque fois que je me connecte à mes ordinateurs – c'est pourquoi j'utilise également la fonctionnalité de montage automatique sur elles. C'est pourquoi j'ai pensé, pourquoi ne pas partager comment faire cela ici aussi !

Eh bien, il existe de nombreuses façons de configurer le montage automatique. Dans cet article, je vais vous présenter un processus que je pense être plus simple et plus facile parmi eux. 

N'ayez crainte ! J'ai également réalisé un tutoriel vidéo sur cette procédure entière. Donc, si vous voulez un guide visuel, vous pouvez regarder cette vidéo [ici](https://youtu.be/0Hfde3Iy41E). 

%[https://youtu.be/0Hfde3Iy41E]

## Comment monter automatiquement une partition au démarrage sous Linux

Dans ce guide, je vais utiliser une application GUI simple nommée **gnome-disk-utility**. Vous pouvez consulter leur dépôt officiel sur [GitLab](https://gitlab.gnome.org/GNOME/gnome-disk-utility) également. 

Cette fois, j'utilise une distribution Linux bien connue nommée [Manjaro](https://manjaro.org/), mais vous pouvez appliquer la même méthode à n'importe quelle distribution Linux.

Tout d'abord, laissez-moi vous montrer mes disques et partitions. Actuellement, j'ai deux dispositifs de stockage sur mon ordinateur de bureau. L'un d'eux est un SSD de 240 Go et l'autre est un HDD de 2 To.

L'image ci-dessous montre les partitions que j'ai dans mon HDD :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/HDD-Partition.png)
_Partitions du HDD_

Et celle-ci montre les partitions que j'ai dans mon SSD :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/SSD-Partition.png)
_Partitions du SSD_

Pour appliquer la fonctionnalité de montage automatique sur mes partitions souhaitées, je dois installer l'application maintenant. Suivez les étapes données ci-dessous.

### Étapes pour configurer le montage automatique

1. Ouvrez votre centre de logiciels ou Ajouter/Retirer des logiciels.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Software-repo.png)
_Ajouter/Retirer des logiciels_

2. Recherchez gnome-disk-utility et vous obtiendrez ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disk-utility-app.png)
_gnome-disk-utility_

Dans ce cas, j'ai déjà installé l'application, et donc elle ne me demande pas de l'installer. 

Si vous n'avez pas encore installé cette application, vous devrez d'abord l'installer. La procédure d'installation est très basique. Il suffit de fournir la permission et elle s'installera elle-même.

3. Ouvrez l'application que nous venons d'installer. Vous pouvez la trouver dans le menu sous le nom **Disques**.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/disks-in-menu.png)
_Disques dans le menu_

Vous verrez les SSD/HDD que vous avez sur le côté gauche de l'application :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/UI-of-disks.png)
_SSD/HDD_

4. Sélectionnez le SSD/HDD sur lequel vous souhaitez activer la fonctionnalité de montage automatique. 

Dans ce cas, je veux activer cette fonctionnalité dans la partition de mon disque dur. Par conséquent, je vais sélectionner le `Disque dur de 2,0 To` sur le côté gauche. Après cela, il me montrera toutes les partitions actives que j'ai sur le disque dur.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/HDD-partition-in-disk.png)
_Partitions du HDD dans gnome-disk-utility_

5. Ensuite, sélectionnez simplement la partition sur laquelle vous souhaitez activer la fonctionnalité, puis cliquez sur l'icône du côté droit en bas à gauche. Cela ouvrira les "Options de partitions supplémentaires" pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ca.png)
_L'icône pour accéder aux options de partition supplémentaires_

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ca-2.png)
_Options de partition supplémentaires_

6. Ensuite, sélectionnez `Modifier les options de montage...` dans la barre de menu latérale :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/mount-option.png)
_Sélectionnez Modifier les options de montage..._

7. Décochez `User Session Defaults`.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/uncheck.png)
_User Session Defaults_

8. Assurez-vous que la case est cochée à côté de `Mount at system startup`. Vous pouvez personnaliser les autres paramètres également si vous le souhaitez, mais pour notre processus de montage automatique au démarrage du système, notre tâche est presque terminée.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/check.png)
_Mount at system startup_

9. Maintenant, cliquez sur `OK`. 

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ok.png)
_Options de montage complétées_

Et vous êtes prêt à partir de maintenant ! Cette même méthode est applicable pour toute partition de disque sur laquelle vous souhaitez activer la fonctionnalité de montage automatique.

## Conclusion

Merci d'avoir lu l'article entier. Si cela vous aide, vous pouvez également consulter d'autres articles de moi sur [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

Si vous souhaitez entrer en contact avec moi, vous pouvez le faire en utilisant [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [GitHub](https://github.com/FahimFBA). 

Vous pouvez également [VOUS ABONNER à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) si vous souhaitez apprendre divers types de langages de programmation avec beaucoup d'exemples pratiques régulièrement.

Si vous souhaitez consulter mes moments forts, vous pouvez le faire sur ma [chronologie Polywork](https://www.polywork.com/fahimbinamin).

Vous pouvez également [visiter mon site web](https://fahimbinamin.com/) pour en savoir plus sur moi et sur ce que je fais.

Merci beaucoup !