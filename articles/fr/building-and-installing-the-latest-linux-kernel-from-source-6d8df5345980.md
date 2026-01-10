---
title: Comment construire et installer le dernier noyau Linux à partir du code source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-30T17:45:53.000Z'
originalURL: https://freecodecamp.org/news/building-and-installing-the-latest-linux-kernel-from-source-6d8df5345980
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4hAdaZsw1dptEybpt56VJQ.gif
tags:
- name: Computer Science
  slug: computer-science
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment construire et installer le dernier noyau Linux à partir du code
  source
seo_desc: 'By Sreehari

  I just finished my first assignment for a course on Advanced Operating Systems.
  And I decided to document my approach for building the Linux kernel from source
  and implementing my own system call.

  There are a number of blogs that already ...'
---

Par Sreehari

Je viens de terminer ma première tâche pour un cours sur les systèmes d'exploitation avancés. Et j'ai décidé de documenter mon approche pour construire le noyau Linux à partir du code source et implémenter mon propre appel système.

Il existe de nombreux blogs qui vous expliquent déjà comment procéder, mais certains sont obsolètes et d'autres semblent inutilement compliqués. Mon objectif est de présenter une approche simple pour le faire, ce qui devrait, je l'espère, vous aider à gagner beaucoup de temps.

Compiler le noyau Linux à partir du code source peut sembler une tâche ardue, même pour quelqu'un qui est assez à l'aise avec les ordinateurs en général. Cela peut aussi devenir vraiment irritant si vous ne suivez pas les bonnes instructions.

Voici donc un guide pour vous aider à travers le processus de [construction](http://stackoverflow.com/questions/2310261/what-is-the-difference-between-compile-code-and-executable-code) du noyau à partir du code source, et c'est un guide qui fonctionne ! Vous n'aurez pas à vous soucier de tout gâcher ou de perdre votre temps.

### Pourquoi construire le noyau à partir du code source ?

Si vous prévoyez de travailler sur les internes du noyau Linux ou de changer son comportement, vous devrez recompiler le noyau sur votre système.

Voici quelques cas spécifiques où vous devrez savoir comment travailler avec le code source du noyau :

1. Vous voulez écrire un programme vraiment cool 'Hello world'. (Chaque fois que vous [implémentez votre propre appel système](https://medium.com/@ssreehari/implementing-a-system-call-in-linux-kernel-4-7-1-6f98250a8c38#.wjl4xo6hx) ou modifiez le code source du noyau, vous devrez recompiler le noyau pour implémenter les changements)
2. Vous voulez activer des fonctionnalités expérimentales sur votre noyau qui ne sont pas activées par défaut (ou, désactiver des fonctionnalités par défaut que vous ne voulez pas)
3. Vous voulez déboguer le code source du noyau, activer la prise en charge d'un nouveau matériel, ou apporter des modifications à ses configurations existantes
4. Vous suivez un cours sur les systèmes d'exploitation avancés et n'avez pas le choix de le faire !

Dans chacune des situations ci-dessus, apprendre à construire le noyau à partir du code source sera utile.

### Ce dont vous aurez besoin

Un système d'exploitation basé sur Linux (j'ai essayé cela sur Ubuntu 14.04 LTS et les instructions écrites ici sont pour la même version).

Vous devrez installer quelques paquets avant de pouvoir commencer. Utilisez les commandes suivantes pour cela.

```
sudo apt-get update
```

```
sudo apt-get install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc
```

Vous aurez également besoin d'au moins 12 Go d'espace libre sur le disque, d'une connexion Internet pour télécharger le code source, et de beaucoup de temps (environ 45 à 90 minutes).

### Téléchargement et extraction de la dernière version du code source du noyau

Pour vérifier votre version actuelle du noyau, ouvrez le terminal et tapez :

```
uname -r
```

Allez sur [kernel.org](https://www.kernel.org/) et téléchargez la dernière version stable. Au moment de l'écriture de cet article, la dernière version stable du noyau était 4.7.1, et je ferai référence à celle-ci dans cet article. (Note : Essayez d'éviter de télécharger le code source depuis d'autres sites web)

Changez de répertoire pour celui où le fichier a été téléchargé et extrayez-le en utilisant :

```
tar xf linux-4.7.1.tar.xz
```

Changez pour le répertoire extrait linux-4.7.1.

```
cd linux-4.7.1
```

Il devrait contenir des dossiers appelés **arch**, **fs**, **crypto**, etc.

#### Configuration et compilation :

Avant de compiler le noyau, nous devons configurer quels modules doivent être inclus et lesquels doivent être laissés de côté.

Il existe de nombreuses façons de procéder.

Une méthode facile et directe consiste à d'abord copier votre fichier de configuration du noyau existant, puis à utiliser 'menuconfig' pour apporter des modifications (si nécessaire). C'est la méthode la plus rapide et probablement la plus sûre.

```
cp /boot/config-$(uname -r) .config   
```

```
make menuconfig
```

C'est la partie où vous pourriez finir par supprimer la prise en charge d'un pilote de périphérique ou faire quelque chose de similaire qui pourrait éventuellement entraîner un noyau endommagé. Si vous n'êtes pas sûr des modifications à apporter, sauvegardez simplement et quittez.

Note : L'une des alternatives à menuconfig est une interface de ligne de commande interactive accessible en utilisant 'make config'. Cela vous aide à configurer tout à partir de zéro. **Ne l'utilisez pas.** Vous serez interrogé sur plus de mille questions oui/non concernant l'activation ou la désactivation de modules, ce qui, je vous le promets, n'est pas du tout amusant. J'ai essayé cela une fois et j'ai réussi à tout gâcher avec les configurations du pilote d'affichage.

**gconfig** et **xconfig** sont des outils de configuration basés sur une interface graphique alternative que vous pourriez utiliser. Je ne les ai pas essayés moi-même. Pour cela, vous devrez utiliser **make gconfig** (ou **make xconfig**) au lieu de **make menuconfig**.

Maintenant, nous sommes tous prêts !

Pour compiler le noyau et ses modules, nous utilisons la commande **make**.

Cela est suivi par l'utilisation de **make modules_install** pour installer les modules du noyau.

Enfin, nous utilisons **make install** pour copier le noyau et le fichier .config dans le dossier /boot et pour générer le fichier system.map (qui est une table de symboles utilisée par le noyau).

Ces trois étapes prises ensemble prennent généralement beaucoup de temps. Utilisez la commande suivante pour effectuer les tâches ci-dessus :

```
sudo make -j 4 && sudo make modules_install -j 4 && sudo make install -j 4
```

Note : J'ai utilisé l'option -j pour spécifier le nombre de cœurs à utiliser. Cela tend à accélérer considérablement le processus. Vous pouvez utiliser **nproc** pour vérifier le nombre d'unités de traitement disponibles. Dans mon cas, il y avait 4 cœurs.

Idéalement, vous ne devriez pas avoir besoin de privilèges sudo, mais j'ai rencontré des problèmes lorsque je ne l'ai pas exécuté avec des privilèges sudo.

### Étapes finales

Une fois le noyau et ses modules compilés et installés, nous voulons utiliser le nouveau noyau la prochaine fois que nous démarrons.

Pour que cela se produise, nous devons utiliser la commande suivante :

```
update-initramfs -c -k 4.7.1   
```

Ensuite, utilisez la commande suivante, qui recherche automatiquement les noyaux présents dans le dossier /boot et les ajoute au fichier de configuration de grub.

```
update-grub  
```

Maintenant, redémarrez le système et vous devriez voir que le nouveau noyau est ajouté aux entrées du chargeur de démarrage.

En suivant les instructions, en supposant qu'il y a suffisamment d'espace disponible sur le disque et que la configuration actuelle du noyau fonctionne bien, vous ne devriez rencontrer aucun problème. Notez que vous pouvez toujours utiliser l'ancienne version du noyau en cas de problème et réessayer tout !

La commande **uname -r** devrait maintenant vous montrer la version actuelle du noyau utilisée.

### Une note importante

Les étapes ci-dessus sont nécessaires pour construire le noyau à partir du code source, pour la première fois. Une fois cela fait au moins une fois et qu'une nouvelle image du noyau est prête, apporter des modifications et écrire nos propres modules est simple. Vous n'utiliserez que les étapes répertoriées sous **Configuration et compilation** chaque fois que quelque chose de nouveau doit être implémenté ou configuré différemment.

C'est-à-dire, souvenez-vous simplement de ce qui suit :

```
cp /boot/config-$(uname -r) .config
```

```
make menuconfig
```

```
sudo make -j 4 && sudo make modules_install -j 4 && sudo make install -j 4
```

Je dois donner crédit aux ressources suivantes qui valent la peine — elles ont été extrêmement utiles pour cette tâche : [Ramkitech.com](http://www.ramkitech.com/), [askubuntu.com](http://askubuntu.com/), [kernel.org](http://www.kernel.org/) et [cyberciti.biz](http://www.cyberciti.biz/)