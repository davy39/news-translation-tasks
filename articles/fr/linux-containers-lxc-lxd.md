---
title: Comment utiliser les conteneurs Linux avec LXC et LXD
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-01-16T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/linux-containers-lxc-lxd
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/containers.jpg
tags:
- name: containers
  slug: containers
- name: Linux
  slug: linux
- name: lxd
  slug: lxd
- name: virtualization
  slug: virtualization
seo_title: Comment utiliser les conteneurs Linux avec LXC et LXD
seo_desc: In the good old days, installing an operating system meant pulling together
  all the hardware components, firing your new computer up with an installation disk
  in a peripheral drive, and setting the installation process loose do its thing.
  The total e...
---

Dans le bon vieux temps, installer un système d'exploitation signifiait rassembler tous les composants matériels, démarrer votre nouvel ordinateur avec un disque d'installation dans un lecteur périphérique, et lancer le processus d'installation pour qu'il fasse son travail. Le temps total écoulé pouvait varier entre quelques heures et plusieurs semaines. 

De nos jours, je peux me dire "Je n'aurais pas contre tester cela sur un serveur exécutant une version particulière de CentOS" et - en fonction de plusieurs variables et en supposant que l'image originale a déjà été téléchargée - je peux avoir un système virtuel entièrement fonctionnel prêt en 30 secondes. Vos résultats exacts peuvent varier, mais pas de beaucoup. 

Vous pouvez voir comment tout cela fonctionne dans mon nouveau [cours Pluralsight "Linux System Optimization"](https://pluralsight.pxf.io/RqrJb) - sur lequel cet article est basé.

Qu'est-ce qui a été à l'origine de tous ces changements ? La virtualisation. Et, en particulier, la virtualisation par conteneurs. 

Un système d'exploitation virtualisé est un système de fichiers contenant toutes les bibliothèques logicielles, les binaires et les fichiers de configuration dont vous auriez besoin pour lancer une machine traditionnelle. C'est juste que ce système de fichiers particulier n'est pas stocké dans la partition racine ou de démarrage que votre ordinateur lirait au démarrage, mais sur une autre partie de votre volume de stockage. 

Et le "démarrage" de votre ordinateur virtuel se produit lorsque certains logiciels trompent habilement les fichiers en leur faisant croire qu'ils fonctionnent tous seuls sur leur propre matériel, alors qu'ils partagent en réalité l'espace et les ressources avec le système d'exploitation hôte et, peut-être, d'autres ordinateurs virtuels.

De manière générale, il existe deux types de systèmes logiciels utilisés pour l'administration de la virtualisation des serveurs : l'hyperviseur et le conteneur. 

Les hyperviseurs fournissent une couche d'abstraction qui permet aux machines virtuelles invitées de créer un environnement isolé avec accès au matériel du système qui émule un serveur bare metal. Cela signifie que les machines virtuelles de l'hyperviseur peuvent être construites à partir de n'importe quel système d'exploitation compatible avec votre matériel sous-jacent. Mais cela signifie également qu'elles utiliseront plus d'espace, plus de mémoire et plus de ressources de calcul.

## Virtualisation par conteneurs

Les conteneurs, en revanche, partagent le noyau du système d'exploitation de l'ordinateur hôte et existent dans des espaces soigneusement sécurisés et isolés gérés par des outils système comme cgroups. Parce qu'ils partagent le noyau, la mémoire et les ressources système consommées par les conteneurs peuvent être vraiment minimales, sans rien gaspiller. Et, comme vous le verrez, les vitesses que vous obtiendrez en exécutant des applications conteneurisées seront à couper le souffle.

Beaucoup d'attention liée aux conteneurs au cours des dernières années s'est concentrée sur Docker et, plus récemment, sur l'outil d'orchestration de conteneurs de Google, Kubernetes. En fait, Kubernetes est bien adapté pour les architectures de microservices à l'échelle de l'entreprise. 

Mais il existe une implémentation plus ancienne et, selon certains, plus mature du modèle de conteneur qui n'a pas disparu. Le [Projet Linux Container, LXC](https://linuxcontainers.org/), et son ensemble d'outils plus récent, LXD, ont des forces que beaucoup considèrent comme faisant de lui un meilleur candidat pour certains cas d'utilisation que Kubernetes. En particulier, LXC excelle dans la création d'environnements sandbox légers et rapides pour les tests et le développement d'applications.

Dans cet article, je vais vous montrer comment installer LXD, comment préparer et lancer un conteneur simple exécutant l'ultra-petit Alpine Linux, puis comment ouvrir une session shell dans votre nouveau conteneur. Je vais également expliquer comment trouver et lancer plusieurs versions d'autres distributions.

Une chose que je peux vous dire tout de suite, c'est que chaque fois que j'enseigne LXC, les étudiants réagissent avec émerveillement devant la puissance et l'efficacité de l'utilisation des conteneurs. 

Lorsque nous aurons terminé tout cela, vous pourrez démarrer des machines pour tester en pratique tout ce que vous apprenez ou sur quoi vous travaillez en quelques secondes. Lorsque une expérience tourne mal, vous pouvez instantanément arrêter et supprimer un conteneur et en construire un autre pour le remplacer. Il n'y a tout simplement plus aucune excuse pour ne pas apprendre.

## Construction de conteneurs LXD

Nous allons faire fonctionner LXC sur une nouvelle installation d'une machine Ubuntu 18.04. Dans cette démonstration, nous installerons et initialiserons un environnement LXD, puis utiliserons la version LXD de l'interface de ligne de commande LXC pour télécharger et lancer un conteneur Alpine Linux. Nous confirmerons que tout a fonctionné, puis nous jetterons un coup d'œil pour voir comment l'environnement est peuplé.

Je vais utiliser le gestionnaire de paquets snap pour installer LXD car c'est maintenant la recommandation officielle. Et pas seulement pour LXD, notez bien : toutes sortes d'applications passent à des gestionnaires alternatifs comme snap ou AppImmage et Flatpak. J'aime toujours mon aptitude Debian, mais on ne peut pas lutter contre le monde entier.

```
$ sudo snap install lxd

```

LXD - qui, encore une fois, est un ensemble d'outils mis à jour conçu pour gérer l'API LXC - vient dans un package qui inclut toutes les dépendances régulières de LXC. Une commande d'installation et nous avons terminé. 

Il est important d'initialiser l'environnement LXC en utilisant la commande lxd init. Vous pourriez configurer les choses vous-même manuellement, mais vous avez plus de chances de tout faire correctement de cette manière. Le processus d'initialisation vous posera une série de questions et, pour l'instant au moins, les réponses par défaut fonctionneront toutes.

```
$ sudo lxd init

```

Une fois cela fait, nous sommes prêts à construire votre premier conteneur. Quelle que soit la distribution Linux et la version que nous voulons, nous devrons trouver et télécharger l'image. Le projet LXC maintient un dépôt d'une assez large gamme d'images sur [images.linuxcontainers.org](https://us.images.linuxcontainers.org/). Vous pouvez voir qu'il y a généralement plusieurs versions de chaque distribution, vous permettant de construire des conteneurs qui fonctionneront avec presque n'importe quel logiciel que vous pouvez leur lancer.

Je vais utiliser la dernière version d'Alpine Linux parce qu'elle est vraiment petite. N'hésitez pas à utiliser n'importe quelle image que vous aimez - y compris les grandes distributions comme Ubuntu et CentOS. Alpine, bien sûr, se téléchargera très rapidement. 

Mais avant de faire cela, je devrais vous dire comment trouver la syntaxe de la ligne de commande nécessaire pour obtenir votre image. 

Comme vous pouvez le voir sur cette capture d'écran du site web de LXD, vous pouvez obtenir trois morceaux d'information dont vous aurez besoin à partir de la page elle-même : le nom de la distribution - Alpine, dans ce cas - le numéro de version - 3.10 - et l'architecture. Nous cherchons amd64.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/lxd-images-1.png)
_De la page images.linuxcontainers.org_

Nous sommes maintenant prêts à déclencher le téléchargement en exécutant la commande `launch` :

```
$ sudo lxc launch images:alpine/3.10/amd64 demo

```

Remarquez comment la syntaxe est "lxc" même si cela est techniquement une interface LXD. "images" indique à LXC que notre image se trouve dans le dépôt public que nous avons vu précédemment. Nos trois morceaux de données - le nom de la distribution, le numéro de version et l'architecture, sont entrés séparés par des barres obliques. J'utiliserai "demo" comme nom de mon conteneur. Cela devrait être tout ce dont nous avons besoin. 

Vous pouvez voir à quel point Alpine est petit par la rapidité avec laquelle il se télécharge. Ma connexion internet n'est pas si rapide et je n'ai pas joué avec l'enregistrement. Pour confirmer que cela a fonctionné, je vais exécuter "lxc ls" pour lister tous les conteneurs actuellement installés. Il n'y en a qu'un seul. Et son état actuel est "running".

```
sudo lxc ls
+------+---------+----------------------+------------+-----------+
| NAME |  STATE  |         IPV4         |    TYPE    | SNAPSHOTS |
+------+---------+----------------------+------------+-----------+
| demo | RUNNING | 10.125.45.119 (eth0) | PERSISTENT | 0         |
+------+---------+----------------------+------------+-----------+

```

Vous pouvez ouvrir une session root sans connexion dans un conteneur en utilisant la commande "lxc exec". Il suffit de spécifier le nom du conteneur puis de dire à LXC que vous voulez exécuter un shell en utilisant l'interpréteur sh (vous pourriez préférer `/bin/bash` si vous travaillez avec un conteneur Ubuntu ou CentOS - à vous de choisir). Comme vous pourrez le constater par vous-même si vous suivez à la maison, nous avons une invite de commande Linux normale et tout ce qui est Linux est maintenant possible.

```
$ sudo lxc exec demo sh
~ # 

```

Vous pourriez également exécuter une seule commande sans ouvrir un shell complet en tapant la commande au lieu de ce `sh`.

```
$ sudo lxc exec demo ls /
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr

```

Vous pouvez quitter le shell à tout moment en utilisant `exit` et revenir à votre hôte. Ici, outre la liste des conteneurs en cours d'exécution, je peux également lister tous les pools de stockage. Le pool par défaut qui a été créé pendant l'initialisation est là, et nous pouvons voir où l'image disque est stockée. /var/lib/lxd est, par défaut, l'endroit où toutes les ressources LXC sont conservées.

```
$ sudo lxc storage ls
+---------+-------------+--------+--------------------------------+---------+
|  NAME   | DESCRIPTION | DRIVER |             SOURCE             | USED BY |
+---------+-------------+--------+--------------------------------+---------+
| default |             | btrfs  | /var/lib/lxd/disks/default.img | 3       |
+---------+-------------+--------+--------------------------------+---------+

```

Je peux de même lister tous mes réseaux. Il se trouve qu'il y a quelques ponts réseau sur ce système (j'ai un peu joué, comme vous pouvez le voir). Il y a aussi le pont physique enp0s3 utilisé par le serveur hôte Ubuntu. Bien qu'entre vous et moi, celui-ci n'est pas physique non plus, car il s'agit en réalité d'une VM exécutée dans Virtual Box d'Oracle.

```
$ lxc network ls
+---------+----------+---------+-------------+---------+
|  NAME   |   TYPE   | MANAGED | DESCRIPTION | USED BY |
+---------+----------+---------+-------------+---------+
| enp0s3  | physical | NO      |             | 1       |
+---------+----------+---------+-------------+---------+
| lxdbr0  | bridge   | YES     |             | 1       |
+---------+----------+---------+-------------+---------+
| mynet   | bridge   | YES     |             | 0       |
+---------+----------+---------+-------------+---------+
| testbr0 | bridge   | YES     |             | 1       |
+---------+----------+---------+-------------+---------+

```

Si nous en avions besoin, nous pourrions facilement ajouter une nouvelle interface virtuelle à notre conteneur en utilisant la commande "lxc network attach". Ici, je vais spécifier le réseau physique puis le nom de notre conteneur.

```
$ lxc network attach enp0s3 demo

```

Une fois cela fait, vous pourriez ouvrir un nouveau shell dans le conteneur pour voir ce qui a changé. Il devrait maintenant y avoir une interface eth1 listée. Vous devrez peut-être redémarrer pour que tous les changements prennent pleinement effet. En faisant cela, vous pouvez également vous émerveiller de la rapidité avec laquelle cette chose peut se redémarrer - à toutes fins utiles, cela se produira plus rapidement que vous ne pouvez taper votre commande `exec` pour ouvrir un nouveau shell.

Profitez de votre nouvel environnement !

_Cet article est basé sur le contenu de mon [cours Pluralsight, "Linux System Optimization"](https://pluralsight.pxf.io/RqrJb). Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur [bootstrap-it.com](https://bootstrap-it.com)._