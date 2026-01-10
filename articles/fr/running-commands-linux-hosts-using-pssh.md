---
title: Comment exécuter des commandes sur plusieurs hôtes Linux en utilisant PSSH
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-01-09T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/running-commands-linux-hosts-using-pssh
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e08740569d1a4ca3af6.jpg
tags:
- name: Linux
  slug: linux
- name: Orchestration
  slug: orchestration
- name: ssh
  slug: ssh
- name: virtualization
  slug: virtualization
seo_title: Comment exécuter des commandes sur plusieurs hôtes Linux en utilisant PSSH
seo_desc: I'm sure you've heard that all the cool kids are playing with orchestration
  automation these days. But do you know why? Well first, the resources consumed by
  modern microservices workloads are becoming much more complex and deploy to far
  more instanc...
---

Je suis sûr que vous avez entendu dire que tous les enfants cool jouent avec l'automatisation de l'orchestration ces jours-ci. Mais savez-vous pourquoi ? Eh bien, premièrement, les ressources consommées par les charges de travail des microservices modernes deviennent beaucoup plus complexes et se déploient sur beaucoup plus d'instances que jamais auparavant. Et deuxièmement, de plus en plus de ces ressources sont virtuelles plutôt que physiques - donc beaucoup d'entre elles n'existeront que pendant quelques minutes ou même quelques secondes.

Tout cela signifie que même si vous vouliez vous connecter à chacun de vos nombreux serveurs, cela n'aurait tout simplement pas de sens. Dans la plupart des cas, en fait, cela ne serait même pas possible. Au lieu de cela, vous allez exécuter beaucoup de scripts intelligents. Et les outils que vous utilisez pour exécuter ce genre de scripts sont généralement appelés orchestrators.

Je suis sûr que vous avez rencontré au moins un ou deux membres du club d'orchestration. Outre Ansible, il y a Terraform, Chef, Puppet et d'autres. Mais il existe également des outils de niveau inférieur qui fonctionnent comme des modules complémentaires aux outils principaux de Linux comme SSH. Bien que, voyant comment il s'exécutera nativement sur Windows et, bien sûr, macOS, je ne suis pas sûr qu'il soit tout à fait correct d'appeler SSH un outil "Linux" anymore. 

L'un de ces modules complémentaires SSH est un ensemble d'outils appelé pssh - qui signifie Parallel SSH. C'est ce que nous allons apprendre dans cet article - qui est extrait de mon nouveau [cours Pluralsight, Linux System Optimization](https://pluralsight.pxf.io/RqrJb).

Pour l'instant, je vais vous parler un peu du laboratoire que j'utilise afin que vous puissiez le reproduire plus facilement et suivre à la maison. J'ai trois conteneurs Ubuntu [LXD](https://www.freecodecamp.org/news/linux-containers-lxc-lxd/) en cours d'exécution. La base de toutes nos opérations sera celle avec une adresse IP de 10.0.3.140, tandis que les deux nœuds hôtes que nous allons approvisionner à distance utiliseront 10.0.3.93 et 10.0.3.43.

Tout ce que nous allons faire suppose que nous avons un accès SSH sans mot de passe de mon conteneur de base à chacun des deux nœuds. Si vous n'êtes pas sûr de savoir comment faire cela, vous pouvez consulter le module SSH de mon [cours Protocol Deep Dive: SSH and Telnet](https://pluralsight.pxf.io/9DYVe) sur Pluralsight. Si vous êtes pressé, [ce tutoriel Red Hat](https://www.redhat.com/sysadmin/passwordless-ssh) vous mènera au même endroit.

L'installation de pssh sur Ubuntu est simple et rapide : `sudo apt install pssh`. Ce n'est pas plus difficile sur CentOS.

J'ai créé un simple fichier d'inventaire d'hôtes appelé sshhosts.txt qui ne contient rien de plus que les adresses IP de mes deux nœuds :

```
$ less sshhosts.txt
10.0.3.93
10.0.3.43

```

Maintenant, je vais exécuter la commande parallel-ssh de pssh pour exécuter une seule commande sur mes hôtes.

```
$ parallel-ssh -i -h sshhosts.txt df -ht ext4


```

-i indique au programme de s'exécuter en mode interactif - sinon nous ne verrions aucune sortie de commande. -h pointe vers le fichier d'hôtes que j'ai appelé sshhosts.txt. Et la commande elle-même sera l'ancien utilitaire Unix df. Cela retournera une liste des lecteurs attachés au système ainsi que leurs points de montage et leurs informations d'utilisation. Le -h ici affichera l'espace disque en unités lisibles par l'homme et le t limitera l'accès aux seuls lecteurs formatés en ext4. 

Pourquoi me soucie-je de cette affaire ext4 ? Parce qu'Ubuntu utilise le gestionnaire de paquets snap et chaque snap crée son propre périphérique virtuel. Et alors ? Eh bien, je ne veux pas avoir à parcourir une douzaine ou plus de périphériques virtuels signalant 0 espace libre juste pour accéder aux vrais lecteurs signalant une utilisation réelle.

```
$ parallel-ssh -i -h sshhosts.txt df -ht ext4
[1] 22:02:00 [SUCCESS] 10.0.3.43
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       457G  131G  304G  30% /
[2] 22:02:00 [SUCCESS] 10.0.3.93
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       457G  131G  304G  30% /

```

Et voilà ! Des informations complètes sur l'espace disque de mes deux nœuds. Je suis sûr que vous avez remarqué que les informations sont identiques. C'est parce que ce sont tous deux des conteneurs qui s'exécutent sur ma station de travail, donc autant qu'ils le sachent, ils ont tous les deux un accès complet à mon propre lecteur.

Pour mon prochain tour, je vais collecter les fichiers /etc/group de chacun de mes nœuds. Ce type d'opération pourrait être utile pour surveiller rapidement l'état de sécurité de vos nœuds. Vous pourriez ajouter un script qui analyse les données entrantes et vous alerte en cas d'anomalies. 

Avant de commencer, je vais créer un répertoire local appelé host-files. Ensuite, j'utiliserai la commande `parallel-slurp` - dont le nom décrit merveilleusement sa fonction. Encore une fois, -h pointe vers le fichier d'hôtes. Le `-L` définit le répertoire host-files comme l'emplacement cible pour écrire les données que nous allons générer, `/etc/group` est le fichier distant que nous voulons aspirer, et `group` est le nom que nous aimerions attribuer aux données localement.

```
mkdir host-files
parallel-slurp -h sshhosts.txt -L host-files/ /etc/group group

```

Lorsque c'est terminé, votre répertoire host-files contiendra des sous-répertoires nommés d'après l'adresse IP de chacun de vos nœuds. Comme vous pouvez le voir, il y a un fichier appelé "group" qui contient les données /etc/group de chaque nœud.

```
$ tree host-files/
host-files/
├── 10.0.3.43
│   └── group
└── 10.0.3.93
    └── group

```

Pssh vient-il avec d'autres surprises ? Oui. Et l'exécution de `apropos` vous donne la liste complète.

```
$ apropos parallel
parallel-nuke (1)    - parallel process kill program
parallel-rsync (1)   - parallel process kill program
parallel-scp (1)     - parallel process kill program
parallel-slurp (1)   - parallel process kill program
parallel-ssh (1)     - parallel ssh program

```

_Cet article est basé sur le contenu de mon [cours Pluralsight, "Linux System Optimization."](https://pluralsight.pxf.io/RqrJb) Il y a beaucoup plus de bonnes pratiques d'administration sous forme de livres, de cours et d'articles disponibles sur [bootstrap-it.com](https://bootstrap-it.com)._