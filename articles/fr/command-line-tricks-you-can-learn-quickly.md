---
title: Astuces en Ligne de Commande que Vous Pouvez Apprendre Plus Vite que de Boire
  Votre Café du Matin
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2024-01-22T23:15:48.000Z'
originalURL: https://freecodecamp.org/news/command-line-tricks-you-can-learn-quickly
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/mazinger-z.png
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Astuces en Ligne de Commande que Vous Pouvez Apprendre Plus Vite que de
  Boire Votre Café du Matin
seo_desc: 'In this short tutorial, I want to share with you a few tricks and tips
  to help you deal with some common situations when you''re working in the Linux command
  line.

  We will cover the following:


  find


  xargs and nproc


  taskset


  numactl


  watch


  inotify-t...'
---

Dans ce court tutoriel, je souhaite partager avec vous quelques astuces et conseils pour vous aider à gérer certaines situations courantes lorsque vous travaillez en ligne de commande sous Linux.

Nous allons couvrir les points suivants :

* find
    
* xargs et nproc
    
* taskset
    
* numactl
    
* watch
    
* inotify-tools
    

Je vais vous présenter un défi et les outils démontrant comment résoudre chaque problème.

## Ce Dont Vous Avez Besoin :

* Une distribution Linux
    
* De la curiosité
    

## Comment Gérer les Répertoires avec de Nombreux Fichiers

Vous avez peut-être déjà rencontré ce problème : vous avez essayé de faire un `ls` sur un répertoire contenant un très grand nombre de fichiers, mais la commande a renvoyé une erreur 'argument list too long' :

```shell
josevnz@orangepi5:/data/test_xargs$ ls *
-bash: /usr/bin/ls: Argument list too long
```

Cela est dû au fait que les systèmes compatibles [POSIX](https://en.wikipedia.org/wiki/POSIX) ont une limite pour le nombre maximum d'octets que vous pouvez passer en tant qu'argument :

```shell
[josevnz@dmaf5 Documents]$ getconf ARG_MAX
2097152
```

2 millions d'octets peuvent sembler beaucoup – ou pas assez selon à qui vous demandez. Mais c'est aussi une protection contre les attaques ou les erreurs innocentes avec de mauvaises conséquences.

Dans tous les cas, comment pouvez-vous contourner cette limitation ? Eh bien, il existe de nombreuses façons de le faire.

### Utilisation des commandes intégrées au Shell

Les commandes intégrées à Bash n'ont pas la limitation ARG\_MAX :

```shell
josevnz@orangepi5:/data/test_xargs$ echo *|ls
...
test_file055554  test_file111110  test_file166666  test_file222222  test_file277778  test_file333334  test_file388890  test_file444446
test_file055555  test_file111111  test_file166667  test_file222223  test_file277779  test_file333335  test_file388891  test_file444447
test_file055556  test_file111112  test_file166668  test_file222224  test_file277780  test_file333336  test_file388892  test_file444448
```

C'est probablement la solution la plus simple, mais voyons une autre façon.

### Utilisation de `find` lorsque vous voulez des options de formatage

Ou vous pouvez utiliser ce flag bien connu de `find` :

```shell
find /data/test_xargs -type f -ls -printf '%name'
```

Ou avec *formatage*, pour imiter `ls` :

```shell
find /data/test_xargs -type f -printf '%f\n
```

C'est rapide et aussi la solution la plus complète. Mais avant de continuer, je vais vous montrer une autre façon.

### Utilisation de xargs

Ce qui suit fonctionne :

```shell
find /data/test_xargs -type f -print0 | xargs -0 ls
```

Mais ce n'est pas efficace, car vous lancez 3 processus pour afficher le contenu du répertoire. Et en plus de cela, xargs *limite* le nombre de fichiers qui seront passés à la commande ls.

Passons à un problème différent.

## Comment Exécuter Plus de Programmes Sans Planter le Serveur

### D'abord vous marchez, puis vous courez : Faites-le en série

Supposons que vous souhaitiez compresser tous les fichiers dans le répertoire donné de notre exemple précédent. Une première tentative serait comme ceci :

```shell
gzip *
```

Ce qui prendra beaucoup de temps car gzip traitera un fichier à la fois.

Vous pourriez penser à faire quelque chose comme ceci pour compresser les fichiers en parallèle :

```shell
josevnz@orangepi5:/data/test_xargs$ for file in $(ls data/test_xargs/*); do gzip $file &; done
-bash: /usr/bin/ls: Argument list too long
```

Encore une fois, ARG\_MAX frappe à nouveau.

Nous connaissons maintenant xargs ou find, alors que se passe-t-il si nous faisons ceci :

```shell
for file in $(find $PWD); do echo gzip $file &; done
wait
echo "Tous les fichiers compressés ?"
```

Cela fera soit **épuiser la mémoire de votre serveur** soit **le surcharger avec une utilisation très élevée du CPU** parce que vous lancez une instance gzip pour chaque fichier trouvé.

### Notre première tentative de parallélisme et de limitation (l'art de l'auto-contrôle)

Ce dont vous avez besoin, c'est d'un moyen de *limiter* vos demandes de compression, afin de ne pas lancer plus de processus que le nombre de CPU que vous avez.

Essayons à nouveau avec `find` et `xargs` :

```shell
find /data/test_xargs -type f -print0| xargs -0 -P $(($(nproc)-1)) -I % gzip %
```

Oh. Cela ressemble à une commande élégante. Laissez-moi expliquer comment cela fonctionne :

1. Utilisez `find` pour obtenir tous les fichiers dans le répertoire donné, utilisez le caractère nul comme séparateur pour pouvoir traiter ceux avec des noms étranges.
    
2. `nproc` vous indiquera combien de CPU vous avez, puis soustrayez 1 en utilisant l'arithmétique Bash comme ceci en utilisant des sous-shells : `$(($(nproc)-1))`
    
3. Enfin, `xargs` exécutera au plus -P processus (dans mon cas 8 CPU - 1 = 7 jobs), en remplaçant le '%' par le nom du fichier à compresser
    

Note : Il existe d'autres façons d'obtenir le nombre de CPU sur la machine, comme en analysant `/proc/cpuinfo`. Il existe d'autres compressions plus efficaces, mais gzip est disponible sur presque tous les systèmes Linux/Unix.

OK, il est temps de voir notre prochain problème.

## Affinité CPU avec taskset pour Maximiser le Temps d'Exécution

Malgré la limitation du nombre de CPU, certains travaux intensifs peuvent ralentir d'autres processus sur votre machine lorsqu'ils recherchent des ressources. Il y a quelques choses que vous pouvez faire pour garder les performances du serveur sous contrôle, comme utiliser [taskset](https://github.com/util-linux/util-linux/blob/master/schedutils/taskset.c) :

> La commande taskset est utilisée pour définir ou récupérer l'affinité CPU  
> d'un processus en cours d'exécution donné son pid, ou pour lancer une nouvelle commande  
> avec une affinité CPU donnée. L'affinité CPU est une propriété de l'ordonnanceur  
> qui "lie" un processus à un ensemble donné de CPU sur le système.

En général, nous voulons toujours laisser l'un des CPU "libre" pour les tâches du système d'exploitation. Le noyau est normalement très bon pour maintenir les processus en cours d'exécution collés à un CPU spécifique pour éviter le changement de contexte, mais si vous voulez imposer sur quels CPU votre processus s'exécutera, vous pouvez utiliser `taskset`

```shell
taskset -c 1,2,3,4,5,6,7 find /data/test_xargs -type f -print0| xargs -0 -P $(($(nproc)-1)) -I % gzip %
```

### taskset le seul jeu en ville ? pas si numactl rapide !

Qu'est-ce que [NUMA et pourquoi vous devriez vous en soucier](https://documentation.suse.com/sles/12-SP4/html/SLES-all/cha-tuning-numactl.html) ?

> Il existe des limitations physiques du matériel qui sont rencontrées lorsque de nombreux CPU et beaucoup de mémoire sont nécessaires. La limitation importante est qu'il y a une bande passante de communication limitée entre les CPU et la mémoire.
> 
> Une modification de l'architecture qui a été introduite pour répondre à ce problème est l'accès non uniforme à la mémoire (NUMA).

Ainsi, la plupart des machines de bureau simples n'ont qu'un seul nœud NUMA, comme la mienne :

```shell
[josevnz@dmaf5 ~]$ numactl --hardware
available: 1 nodes (0)
node 0 cpus: 0 1 2 3 4 5 6 7
node 0 size: 15679 MB
node 0 free: 5083 MB
node distances:
node   0 
  0:  10
# Ou avec lscpu
[josevnz@dmaf5 ~]$ lscpu |rg NUMA
NUMA node(s):                    1
NUMA node0 CPU(s):               0-7
```

Si vous avez plus d'un nœud NUMA, vous pouvez vouloir "épingler" ou définir l'affinité de votre programme pour utiliser les CPU et la mémoire du même nœud.

Par exemple, sur une machine avec 16 cœurs, 0-7 sur le nœud 0, 8-15 sur le nœud 1, nous pourrions forcer notre programme de compression à s'exécuter sur tous les CPU du nœud 1, et utiliser la mémoire du nœud 1 comme ceci :

```shell
numactl --physcpubind 8-15 --membind=1 find /data/test_xargs -type f -print0| xargs -0 -P $(($(nproc)-1)) -I % gzip %
```

## Garder un Œil sur les Choses

### Regardez simplement ce que je fais

La commande [watch](https://www.man7.org/linux/man-pages/man1/watch.1.html) vous permet d'exécuter périodiquement une commande, et même de vous montrer les différences avant les appels :

```shell
Every 10.0s: ls                                                                                                         orangepi5: Wed May 24 22:46:33 2023

test_file000001.gz
test_file000002.gz
test_file000003.gz
test_file000004.gz
test_file000005.gz
test_file000006.gz
test_file000007.gz
test_file000008.gz
test_file000009.gz
test_file000010.gz
...
```

Cela me montre la sortie de la commande `ls` toutes les 10 secondes. Pour détecter les changements dans un répertoire, c'est simple, mais pas facile à automatiser et définitivement pas efficace.

Ne serait-ce pas bien si le noyau pouvait me dire les changements dans mes répertoires ?

### Une meilleure façon de connaître les changements sur le système de fichiers, avec inotify-tools

Vous devrez peut-être installer cela séparément, mais cela devrait être facile à faire. Sur Ubuntu :

```shell
sudo apt-get install inotify-tools
```

Sur Fedora :

```shell
sudo dnf install -y inotify-tools
```

Alors, comment pouvons-nous surveiller les événements dans un répertoire donné ?

Dans un terminal, nous pouvons exécuter inotifywait :

```shell
josevnz@orangepi5:/data/test_xargs$ inotifywait --recursive /data/test_xargs/
Setting up watches.  Beware: since -r was given, this may take a while!
Watches established.
```

Et dans un autre terminal, nous pouvons toucher certains fichiers pour simuler un événement :

```shell
josevnz@orangepi5:/data/test_xargs$ pwd
/data/test_xargs
josevnz@orangepi5:/data/test_xargs$ touch test_file285707.gz test_file357136.gz test_file428565.gz
```

Le terminal original recevra le premier événement et quittera :

```shell
Watches established.
/data/test_xargs/ OPEN test_file285707.gz
```

Pour le faire écouter les événements pour toujours, nous faisons ceci :

```shell
josevnz@orangepi5:/data/test_xargs$ inotifywait --recursive --monitor /data/test_xargs/
```

Si nous touchons à nouveau le fichier dans un terminal séparé, alors cette fois nous verrons tous les événements :

```shell
Setting up watches.  Beware: since -r was given, this may take a while!
Watches established.
/data/test_xargs/ OPEN test_file285707.gz
/data/test_xargs/ ATTRIB test_file285707.gz
/data/test_xargs/ CLOSE_WRITE,CLOSE test_file285707.gz
/data/test_xargs/ OPEN test_file357136.gz
/data/test_xargs/ ATTRIB test_file357136.gz
/data/test_xargs/ CLOSE_WRITE,CLOSE test_file357136.gz
/data/test_xargs/ OPEN test_file428565.gz
/data/test_xargs/ ATTRIB test_file428565.gz
/data/test_xargs/ CLOSE_WRITE,CLOSE test_file428565.gz
```

Cela est moins exigeant pour le système d'exploitation que de demander les changements de répertoire à chaque fois, et de filtrer nous-mêmes les différences.

## Qu'est-ce qui Suit

Il y a tellement plus à explorer. Les conseils ci-dessus vous ont introduit à certains concepts importants, alors pourquoi ne pas en apprendre beaucoup plus à leur sujet ?

* Le [forum Ubuntu](https://askubuntu.com/questions/217764/argument-list-too-long-when-copying-files) a une grande conversation sur *xargs*, *find*, *ulimit* et autres choses. Le savoir est pouvoir.
    
* RedHat a [une belle page](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/monitoring_and_managing_system_status_and_performance/configuring-an-operating-system-to-optimize-cpu-utilization_monitoring-and-managing-system-status-and-performance) sur NUMA, taskset, la gestion des interruptions. Si vous êtes sérieux au sujet de l'optimisation des performances de vos processus, veuillez la lire.
    
* Vous avez aimé [inotify](https://en.wikipedia.org/wiki/Inotify) et souhaitez l'utiliser depuis votre script Python. Alors jetez un coup d'œil à [pynotify](https://github.com/seb-m/pyinotify/wiki).
    
* Find peut être intimidant, mais [ce tutoriel](https://www.digitalocean.com/community/tutorials/how-to-use-find-and-locate-to-search-for-files-on-linux) le rendra plus facile à comprendre.
    
* Le code source de ce tutoriel peut être trouvé [ici](https://github.com/josevnz/CommandLineTipsAndTricks).